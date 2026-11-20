"""Phase375 negative controls. Every Ed25519 key is SYNTHETIC test material.
No GitHub issuance, real independent approval, or number-theory verification.
"""
import copy
from dataclasses import asdict, replace
import json
from pathlib import Path
import sys
import unittest

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

sys.path.insert(0, str(Path(__file__).resolve().parent))
from policy_transport import (Snapshot, OriginTask, MigrationClaim,
    SignedMigration, PublicAuthority, PolicyMigrationGate, ContractError,
    canonical_bytes)

MANIFEST=json.loads((Path(__file__).resolve().parents[1]/
                     "phase368"/"manifest.json").read_text())
ARM="source_anchor_mutation"
OLD_TASK_ID="a"*64
ORIGIN_REF="github:issuecomment:synthetic-original-1"
MIGRATION_REF="github:issuecomment:synthetic-migration-2"


def fixture(*,version=375,mutator=None,tier="meso",budget=1,
            issuer_id="scheduler",approver_id="external-policy-reviewer",
            allowed_roles=("policy_migration",)):
    old=Snapshot.from_manifest(374,MANIFEST)
    changed=copy.deepcopy(MANIFEST)
    changed["name"]="phase375-synthetic-policy-version"
    if mutator is not None:
        mutator(changed)
    target=Snapshot.from_manifest(version,changed)
    key=Ed25519PrivateKey.generate()
    pub=key.public_key().public_bytes(
        serialization.Encoding.Raw,serialization.PublicFormat.Raw).hex()
    gate=PolicyMigrationGate({approver_id:PublicAuthority(pub,allowed_roles)})
    gate.register_snapshot(old)
    gate.register_snapshot(target)
    task=OriginTask(OLD_TASK_ID,ARM,old.sha256,issuer_id,tier,budget,
                    False,False,ORIGIN_REF)
    gate.register_origin(task)
    return gate,key,task,old,target


def signed(gate,key,task,old,target,**changes):
    a=MigrationClaim(task.task_id,task.arm_id,old.sha256,target.sha256,
          old.version,target.version,old.arm(task.arm_id)["cost"],
          target.arm(task.arm_id)["cost"],task.issuer_id,
          "external-policy-reviewer",ORIGIN_REF,MIGRATION_REF)
    a=replace(a,**changes)
    return SignedMigration(a,key.sign(canonical_bytes(asdict(a))).hex())


class VersionedMigrationTests(unittest.TestCase):
    def test_unrelated_manifest_change_allows_explicit_migration(self):
        g,k,t,o,n=fixture()
        g.verify(signed(g,k,t,o,n))
        self.assertEqual(g.snapshot()["accepted_migrations"],1)
        self.assertTrue(g.snapshot()["no_claim_promotion_api"])
        self.assertFalse(g.snapshot()["external_authentication_implemented"])
        self.assertEqual(g.tasks[t.task_id].source_snapshot_sha256,o.sha256)

    def test_same_receipt_replay_rejected(self):
        g,k,t,o,n=fixture(); r=signed(g,k,t,o,n);g.verify(r)
        with self.assertRaises(ContractError):g.verify(r)

    def test_target_clock_change_rejected_even_if_meso_tier_admits_fast(self):
        def mutate(x):
            next(w for w in x["worldlets"] if w["id"]=="source.original")["clocks"]=["fast"]
        g,k,t,o,n=fixture(mutator=mutate)
        self.assertTrue(n.eligible(ARM,"meso",1,False,False))
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_scope_drift_rejected(self):
        def mutate(x):
            next(a for a in x["arms"] if a["id"]==ARM)["scope"]="matrix_general"
        g,k,t,o,n=fixture(mutator=mutate)
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_human_authority_drift_rejected(self):
        def mutate(x):
            next(a for a in x["arms"] if a["id"]==ARM)["execution"]="human"
        g,k,t,o,n=fixture(mutator=mutate,tier="review")
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_source_drift_rejected(self):
        def mutate(x):
            next(w for w in x["worldlets"] if w["id"]=="source.original")["source"]="maximal-order-D203-phase306"
            next(a for a in x["arms"] if a["id"]==ARM)["source"]="maximal-order-D203-phase306"
        g,k,t,o,n=fixture(mutator=mutate)
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_unauthorized_target_due_to_increased_cost(self):
        def mutate(x):
            next(a for a in x["arms"] if a["id"]==ARM)["cost"]=2
        g,k,t,o,n=fixture(mutator=mutate,budget=1)
        self.assertFalse(n.eligible(ARM,"meso",1,False,False))
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_explicit_cost_change_with_sufficient_budget(self):
        def mutate(x):
            next(a for a in x["arms"] if a["id"]==ARM)["cost"]=2
        g,k,t,o,n=fixture(mutator=mutate,budget=2)
        g.verify(signed(g,k,t,o,n))
        self.assertEqual(g.snapshot()["accepted_migrations"],1)

    def test_cost_signature_mismatch_rejected(self):
        g,k,t,o,n=fixture()
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n,to_cost=99))

    def test_old_fast_not_retroactively_admitted(self):
        old=Snapshot.from_manifest(374,MANIFEST)
        m=copy.deepcopy(MANIFEST)
        next(w for w in m["worldlets"] if w["id"]=="source.original")["clocks"]=["fast"]
        new=Snapshot.from_manifest(375,m)
        self.assertFalse(old.eligible(ARM,"fast",9,False,False))
        self.assertTrue(new.eligible(ARM,"fast",9,False,False))
        g=PolicyMigrationGate({})
        g.register_snapshot(old);g.register_snapshot(new)
        t=OriginTask(OLD_TASK_ID,ARM,old.sha256,"scheduler",
                     "fast",9,False,False,ORIGIN_REF)
        with self.assertRaises(ContractError):g.register_origin(t)

    def test_contrast_not_rewritten_as_original(self):
        o=Snapshot.from_manifest(374,MANIFEST)
        self.assertFalse(o.eligible("d203_worldlet_contrast","meso",9,False,False))
        self.assertTrue(o.eligible("d203_worldlet_contrast","meso",9,False,True))

    def test_unissued_task_rejected(self):
        g,k,t,o,n=fixture()
        r=signed(g,k,t,o,n,task_id="b"*64)
        with self.assertRaises(ContractError):g.verify(r)

    def test_changed_original_snapshot_rejected(self):
        g,k,t,o,n=fixture()
        r=signed(g,k,t,o,n,from_snapshot_sha256="f"*64)
        with self.assertRaises(ContractError):g.verify(r)

    def test_changed_original_reference_rejected(self):
        g,k,t,o,n=fixture()
        r=signed(g,k,t,o,n,original_external_reference="unrelated")
        with self.assertRaises(ContractError):g.verify(r)

    def test_changed_version_label_rejected(self):
        g,k,t,o,n=fixture()
        r=signed(g,k,t,o,n,to_version=999)
        with self.assertRaises(ContractError):g.verify(r)

    def test_backwards_or_equal_version_rejected(self):
        g,k,t,o,n=fixture(version=373)
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_issuer_cannot_sign_own_migration(self):
        g,k,t,o,n=fixture(issuer_id="external-policy-reviewer")
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_wrong_signer_key_rejected(self):
        g,k,t,o,n=fixture()
        with self.assertRaises(ContractError):g.verify(
            signed(g,Ed25519PrivateKey.generate(),t,o,n))

    def test_tampered_payload_rejected(self):
        g,k,t,o,n=fixture()
        good=signed(g,k,t,o,n)
        wrong=SignedMigration(replace(good.claim,migration_external_reference="tampered"),
                              good.signature_hex)
        with self.assertRaises(ContractError):g.verify(wrong)

    def test_wrong_signer_role_rejected(self):
        g,k,t,o,n=fixture(allowed_roles=("source_guard",))
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_unregistered_policy_rejected(self):
        g,k,t,o,n=fixture()
        del g.policies[n.sha256]
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_duplicate_version_ordinal_new_bytes_rejected(self):
        g,k,t,o,n=fixture()
        m=copy.deepcopy(MANIFEST);m["name"]="different-name"
        with self.assertRaises(ContractError):
            g.register_snapshot(Snapshot.from_manifest(374,m))

    def test_two_labels_do_not_make_one_digest_two_policies(self):
        g,k,t,o,n=fixture()
        with self.assertRaises(ContractError):
            g.register_snapshot(Snapshot.from_manifest(376,MANIFEST))

    def test_missing_external_migration_ref_rejected(self):
        g,k,t,o,n=fixture()
        with self.assertRaises(ContractError):
            g.verify(signed(g,k,t,o,n,migration_external_reference=""))

    def test_wrong_purpose_rejected(self):
        g,k,t,o,n=fixture()
        with self.assertRaises(ContractError):
            g.verify(signed(g,k,t,o,n,purpose="field_theorem_promotion"))

    def test_worldlet_retargeting_rejected(self):
        def mutate(x):
            next(a for a in x["arms"] if a["id"]==ARM)["worldlet"]="proof.lean"
            next(h for h in x["hyperedges"] if h["id"]=="source_falsification")["participants"].append("proof.lean")
        g,k,t,o,n=fixture(mutator=mutate)
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_remainder_reclassification_rejected(self):
        def mutate(x):
            a=next(a for a in x["arms"] if a["id"]==ARM)
            a["transport"]="lossy"
            a["remainder"]="new_unproven_remainder"
        g,k,t,o,n=fixture(mutator=mutate)
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_mutated_stored_snapshot_bytes_detected(self):
        g,k,t,o,n=fixture()
        from dataclasses import replace as dc_replace
        g.policies[o.sha256]=dc_replace(o,json_bytes=b"{}")
        with self.assertRaises(ContractError):g.verify(signed(g,k,t,o,n))

    def test_separate_origin_task_receipt_cannot_be_reassigned(self):
        g,k,t,o,n=fixture()
        task2=replace(t,task_id="b"*64)
        g.register_origin(task2)
        with self.assertRaises(ContractError):
            g.verify(signed(g,k,t,o,n,task_id=task2.task_id,
                            original_external_reference="wrong-ref"))

    def test_unrelated_field_claim_unchanged(self):
        g,k,t,o,n=fixture()
        g.verify(signed(g,k,t,o,n))
        self.assertNotIn("promoted_claims",g.snapshot())
        self.assertNotIn("field_proof",g.snapshot())

if __name__=="__main__":
    unittest.main()
