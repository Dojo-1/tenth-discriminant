"""Phase376 bounded adversarial fixtures; all signer keys are locally GENERATED.
Passing this suite does not establish a live independent key custodian.
"""
import copy
from dataclasses import asdict, replace
import json
from pathlib import Path
import sys
import unittest

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

sys.path.insert(0,str(Path(__file__).resolve().parent))
from revocation_gate import (
    PublicCredential, SignedOrigin, RevocationNotice, SignedRevocation,
    RevocationAwareMigration, ContractError, canonical_bytes
)
from policy_transport import (
    Snapshot, OriginTask, MigrationClaim, SignedMigration
)

MANIFEST=json.loads((Path(__file__).resolve().parents[1]/
                     "phase368"/"manifest.json").read_text())
ARM="source_anchor_mutation"
TASK_ID="c"*64


def keypair(label,role,registered=0):
    private=Ed25519PrivateKey.generate()
    pub=private.public_key().public_bytes(
        serialization.Encoding.Raw,serialization.PublicFormat.Raw).hex()
    return private,PublicCredential(label,pub,(role,),registered)


def fixture(*,registrations=(0,0,0),key_roles=("issue_task","policy_migration","revoke_key")):
    keys=[keypair(name,role,start) for name,role,start in zip(
        ("issuer","approver","guardian"),key_roles,registrations)]
    g=RevocationAwareMigration(tuple(pair[1] for pair in keys))
    old=Snapshot.from_manifest(374,MANIFEST)
    target_manifest=copy.deepcopy(MANIFEST)
    target_manifest["name"]="phase376-compatible-version-fixture"
    new=Snapshot.from_manifest(375,target_manifest)
    g.register_snapshot(old);g.register_snapshot(new)
    t=OriginTask(TASK_ID,ARM,old.sha256,"issuer","meso",1,
                 False,False,"fixture:externally-unverified-origin")
    return g,keys,t,old,new


def signed_origin(keys,task,*,signer="issuer",override=None):
    k=dict((pair[1].key_id,pair[0]) for pair in keys)[signer]
    payload=task if override is None else override
    return SignedOrigin(payload,signer,
                        k.sign(canonical_bytes(asdict(payload))).hex())


def signed_migration(keys,task,old,new,**changes):
    claim=MigrationClaim(task.task_id,task.arm_id,old.sha256,new.sha256,
        old.version,new.version,old.arm(task.arm_id)["cost"],
        new.arm(task.arm_id)["cost"],"issuer","approver",
        task.issued_external_reference,"fixture:unverified-migration")
    claim=replace(claim,**changes)
    key=dict((pair[1].key_id,pair[0]) for pair in keys)["approver"]
    return SignedMigration(claim,key.sign(canonical_bytes(asdict(claim))).hex())


def signed_revoke(keys,target,tick,*,guardian="guardian",**changes):
    notice=RevocationNotice(target,guardian,tick,"fixture key compromised")
    notice=replace(notice,**changes)
    key=dict((pair[1].key_id,pair[0]) for pair in keys)[guardian]
    return SignedRevocation(notice,key.sign(canonical_bytes(asdict(notice))).hex())


def accepted_origin(g,keys,t):
    g.advance(1)
    g.register_origin(signed_origin(keys,t))


class RevocationControls(unittest.TestCase):
    def test_valid_distinct_issuer_approver(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t);g.advance(2)
        e=g.approve(signed_migration(keys,t,o,n))
        self.assertEqual(e.accepted_at,2)
        self.assertEqual(g.snapshot()["historical_acceptances"],1)
        self.assertFalse(g.snapshot()["external_key_registry_authenticated"])

    def test_approver_revocation_blocks_new_approval(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t)
        g.advance(3);g.revoke(signed_revoke(keys,"approver",3))
        with self.assertRaisesRegex(ContractError,"revoked"):
            g.approve(signed_migration(keys,t,o,n))
        self.assertEqual(g.snapshot()["historical_acceptances"],0)

    def test_issuer_revocation_blocks_new_approval(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t)
        g.advance(3);g.revoke(signed_revoke(keys,"issuer",3))
        with self.assertRaisesRegex(ContractError,"revoked"):
            g.approve(signed_migration(keys,t,o,n))

    def test_historical_approval_not_erased_by_later_revocation(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t);g.advance(2)
        history=g.approve(signed_migration(keys,t,o,n))
        g.advance(4);g.revoke(signed_revoke(keys,"approver",4))
        self.assertEqual(g.accepted[(t.task_id,n.sha256)],history)
        self.assertEqual(g.snapshot()["historical_acceptances"],1)

    def test_revoked_signer_cannot_authorize_second_task(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t)
        g.advance(2);g.approve(signed_migration(keys,t,o,n))
        g.advance(3);g.revoke(signed_revoke(keys,"approver",3))
        t2=replace(t,task_id="d"*64)
        g.register_origin(signed_origin(keys,t2))
        with self.assertRaises(ContractError):
            g.approve(signed_migration(keys,t2,o,n))

    def test_revocation_enforced_at_cutoff_not_just_after(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t)
        g.advance(4);g.revoke(signed_revoke(keys,"approver",4))
        with self.assertRaises(ContractError):
            g.approve(signed_migration(keys,t,o,n))

    def test_clock_rollback_after_revocation_denied(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t)
        g.advance(4);g.revoke(signed_revoke(keys,"approver",4))
        with self.assertRaisesRegex(ContractError,"non-monotone"):
            g.advance(2)

    def test_revocation_cannot_backdate(self):
        g,keys,t,o,n=fixture();g.advance(5)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"approver",4))

    def test_revocation_cannot_be_future_dated(self):
        g,keys,t,o,n=fixture();g.advance(5)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"approver",6))

    def test_repeated_revocation_rejected(self):
        g,keys,t,o,n=fixture();g.advance(4)
        r=signed_revoke(keys,"approver",4);g.revoke(r)
        with self.assertRaises(ContractError):g.revoke(r)

    def test_guardian_cannot_self_revoke(self):
        g,keys,t,o,n=fixture();g.advance(4)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"guardian",4))

    def test_issuer_is_not_revocation_guardian(self):
        g,keys,t,o,n=fixture();g.advance(4)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"approver",4,guardian="issuer"))

    def test_invalid_governance_signature_rejected(self):
        g,keys,t,o,n=fixture();g.advance(4)
        good=signed_revoke(keys,"approver",4)
        bogus=SignedRevocation(good.notice,Ed25519PrivateKey.generate().sign(
            canonical_bytes(asdict(good.notice))).hex())
        with self.assertRaises(ContractError):g.revoke(bogus)

    def test_forged_revocation_payload_rejected(self):
        g,keys,t,o,n=fixture();g.advance(4)
        good=signed_revoke(keys,"approver",4)
        forged=SignedRevocation(replace(good.notice,reason="forged"),good.signature_hex)
        with self.assertRaises(ContractError):g.revoke(forged)

    def test_unqualified_revocation_rejected(self):
        g,keys,t,o,n=fixture();g.advance(4)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"approver",4,reason=" "))

    def test_wrong_revocation_regime_rejected(self):
        g,keys,t,o,n=fixture();g.advance(4)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"approver",4,regime="unauthorized"))

    def test_unknown_revocation_target_rejected(self):
        g,keys,t,o,n=fixture();g.advance(4)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"unknown",4))

    def test_origin_requires_issuer_signature(self):
        g,keys,t,o,n=fixture();g.advance(1)
        with self.assertRaises(ContractError):
            g.register_origin(SignedOrigin(t,"issuer","00"*64))

    def test_origin_mismatched_key_rejected(self):
        g,keys,t,o,n=fixture();g.advance(1)
        with self.assertRaises(ContractError):
            g.register_origin(signed_origin(keys,t,signer="approver"))

    def test_issuer_key_role_required(self):
        g,keys,t,o,n=fixture(key_roles=("source_guard","policy_migration","revoke_key"))
        g.advance(1)
        with self.assertRaises(ContractError):
            g.register_origin(signed_origin(keys,t))

    def test_approver_role_required(self):
        g,keys,t,o,n=fixture(key_roles=("issue_task","source_guard","revoke_key"))
        accepted_origin(g,keys,t);g.advance(2)
        with self.assertRaises(ContractError):
            g.approve(signed_migration(keys,t,o,n))

    def test_guardian_key_role_required(self):
        g,keys,t,o,n=fixture(key_roles=("issue_task","policy_migration","source_guard"))
        g.advance(4)
        with self.assertRaises(ContractError):
            g.revoke(signed_revoke(keys,"approver",4))

    def test_issuer_approver_same_public_bytes_different_alias_rejected(self):
        keys=[keypair("issuer","issue_task"),
              keypair("guardian","revoke_key")]
        same=replace(keys[0][1],key_id="approver",roles=("policy_migration",))
        with self.assertRaisesRegex(ContractError,"alias"):
            RevocationAwareMigration((keys[0][1],same,keys[1][1]))

    def test_unregistered_approver_rejected(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t);g.advance(2)
        r=signed_migration(keys,t,o,n,approver_id="unknown")
        with self.assertRaises(ContractError):g.approve(r)

    def test_pre_registration_signer_rejected(self):
        g,keys,t,o,n=fixture(registrations=(5,0,0));g.advance(1)
        with self.assertRaises(ContractError):
            g.register_origin(signed_origin(keys,t))

    def test_source_drift_rejected_by_inherited_phase375(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t);g.advance(2)
        with self.assertRaises(ContractError):
            g.approve(signed_migration(keys,t,o,n,arm_id="d203_worldlet_contrast"))

    def test_scope_reassignment_disallowed_by_original_task(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t);g.advance(2)
        with self.assertRaises(ContractError):
            g.approve(signed_migration(keys,t,o,n,from_snapshot_sha256="f"*64))

    def test_old_fast_unauthorized_under_issuing_version(self):
        g,keys,t,o,n=fixture();g.advance(1)
        bad=replace(t,tier="fast",budget=9)
        with self.assertRaises(ContractError):
            g.register_origin(signed_origin(keys,bad))

    def test_same_migration_cannot_be_replayed(self):
        g,keys,t,o,n=fixture();accepted_origin(g,keys,t);g.advance(2)
        r=signed_migration(keys,t,o,n);g.approve(r)
        with self.assertRaises(ContractError):g.approve(r)

    def test_no_claim_promotion_interface(self):
        g,keys,t,o,n=fixture()
        self.assertFalse(g.snapshot()["field_theorem_promotion_api"])
        self.assertFalse(g.snapshot()["durable_external_event_log"])
        self.assertFalse(g.snapshot()["external_clock_authenticated"])

if __name__=="__main__":
    unittest.main()
