"""Phase373 offline negative controls with SYNTHETIC external keys.

The apparent external issuances and time stamps are TEST INPUTS.
Passing these tests does not authenticate a live GitHub verifier or
prove that the research controller improves theorem discovery.
"""
from dataclasses import asdict, replace
import json
from pathlib import Path
import sys
import unittest

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase372"))
from attempt_contract import (AttemptOutcome, SignedAttempt, ExecutionIdentity,
                              Issuance, TrustEntry, ContractError, canonical)
from clock_contract import (ClockBoundLoop, ClockStamp, SignedClockStamp,
                            PositiveAffineClockMap)

MANIFEST=json.loads((Path(__file__).resolve().parents[1]/
                     "phase368"/"manifest.json").read_text())
HEAD="b07bb172ad819b297bed46be1547488d3c215d73"
ISSUE_AT="2026-11-20T20:14:40Z"
START_AT="2026-11-20T20:14:48Z"
VALID_AT="2026-11-20T20:15:20Z"


def fixture():
    key=Ed25519PrivateKey.generate()
    pub=key.public_key().public_bytes(serialization.Encoding.Raw,
                                       serialization.PublicFormat.Raw).hex()
    loop=ClockBoundLoop(MANIFEST,{"ci-auditor":TrustEntry(pub,("source_guard","prolog_exact"))})
    task=loop.issue(HEAD,1,phase="meso",nonce="phase373-issued-task-0001")
    loop.register_issuance(Issuance(task.id,"github:issuecomment:fixture",ISSUE_AT))
    return loop,key,task


def sign_both(loop,key,task, *, attempt=2,job="136542423196",
              clock_changes=None,attempt_changes=None):
    execution=ExecutionIdentity("44809412040",attempt,job,task.repository_head)
    a=AttemptOutcome(task.id,task.arm,task.source,task.scope,task.cost_units,
         execution,"github:issuecomment:fixture",ISSUE_AT,START_AT,"ci-auditor",
         "source_guard","a"*64,"VERIFIED_PHASE371_SOURCE_ANCHOR",
         True,True,False,True,False)
    if attempt_changes:
        a=replace(a,**attempt_changes)
    p=loop.permits[task.id]
    clock=ClockStamp(task.id,execution,p.policy_sha256,p.research_phase,
          p.native_worldlet_clock,p.worldlet_id,p.source,ISSUE_AT,START_AT,
          VALID_AT,"ci-auditor")
    if clock_changes:
        clock=replace(clock,**clock_changes)
    return (SignedAttempt(a,key.sign(canonical(asdict(a))).hex()),
            SignedClockStamp(clock,key.sign(canonical(asdict(clock))).hex()))


class ClockSquareTests(unittest.TestCase):
    def test_source_arm_exact_native_meso(self):
        loop,key,task=fixture()
        self.assertEqual(task.arm,"source_anchor_mutation")
        self.assertEqual(task.research_clock,"meso")
        self.assertEqual(loop.permits[task.id].native_worldlet_clock,"meso")

    def test_historical_fast_source_not_scheduled(self):
        key=Ed25519PrivateKey.generate()
        pub=key.public_key().public_bytes(serialization.Encoding.Raw,
                                           serialization.PublicFormat.Raw).hex()
        loop=ClockBoundLoop(MANIFEST,{"ci-auditor":TrustEntry(pub,("source_guard",))})
        with self.assertRaises(ContractError):
            loop.issue(HEAD,1,phase="fast",nonce="phase373-fast-invalid-0001")
        self.assertEqual(len(loop.permits),0)

    def test_nested_meso_admits_fast_prolog_arm(self):
        loop,key,task=fixture()
        other=loop.issue(HEAD,2,phase="meso",nonce="phase373-prolog-allowed-0002")
        self.assertEqual(other.arm,"prolog_clock_counterworld")
        self.assertEqual(loop.permits[other.id].research_phase,"meso")
        self.assertEqual(loop.permits[other.id].native_worldlet_clock,"fast")

    def test_policy_digest_is_canonical(self):
        loop,key,task=fixture()
        self.assertEqual(len(loop.manifest_sha256),64)
        self.assertEqual(loop.snapshot()["manifest_sha256"],loop.permits[task.id].policy_sha256)

    def test_signed_clock_and_attempt_can_be_credited(self):
        loop,key,task=fixture()
        loop.accept(*sign_both(loop,key,task))
        self.assertEqual(loop.snapshot()["credited_count"],1)
        self.assertTrue(loop.snapshot()["integrity_ok"])
        self.assertTrue(loop.snapshot()["no_claim_promotion_interface"])

    def test_replay_credited_task(self):
        loop,key,task=fixture();r=sign_both(loop,key,task);loop.accept(*r)
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_wrong_clock_signature(self):
        loop,key,task=fixture();attempt,clock=sign_both(loop,key,task)
        with self.assertRaises(ContractError):
            loop.accept(attempt,SignedClockStamp(clock.data,"ff"*64))

    def test_wrong_clock_signer(self):
        loop,key,task=fixture()
        attempt,clock=sign_both(loop,key,task,clock_changes={"verifier_id":"unregistered"})
        with self.assertRaises(ContractError):loop.accept(attempt,clock)

    def test_research_phase_tampering_rejected(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"research_phase":"fast"})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_native_clock_tampering_rejected(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"native_worldlet_clock":"fast"})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_manifest_digest_tampering_rejected(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"policy_sha256":"f"*64})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_worldlet_tampering_rejected(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"worldlet_id":"logic.prolog"})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_source_tampering_rejected(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"source":"maximal-order-D203-phase306"})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_policy_mutation_after_issuance_rejected(self):
        loop,key,task=fixture();r=sign_both(loop,key,task)
        loop.manifest["worldlets"][0]["clocks"]=["fast"]
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_execution_attempt_mismatch_rejected(self):
        loop,key,task=fixture()
        other=ExecutionIdentity("44809412040",3,"136542423197",HEAD)
        r=sign_both(loop,key,task,clock_changes={"execution":other})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_execution_head_mismatch_rejected(self):
        loop,key,task=fixture()
        other=ExecutionIdentity("44809412040",2,"136542423196","f"*40)
        r=sign_both(loop,key,task,clock_changes={"execution":other})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_clock_and_attempt_issuance_disagree(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"issued_at":"2026-11-20T20:14:39Z"})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_clock_and_attempt_start_disagree(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"started_at":"2026-11-20T20:14:49Z"})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_validation_before_execution_rejected(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"validated_at":"2026-11-20T20:14:47Z"})
        with self.assertRaises(ContractError):loop.accept(*r)

    def test_equal_validation_and_execution_allowed(self):
        loop,key,task=fixture()
        r=sign_both(loop,key,task,clock_changes={"validated_at":START_AT})
        loop.accept(*r)
        self.assertEqual(loop.snapshot()["credited_count"],1)

    def test_attempt_preissue_rejected(self):
        loop,key,task=fixture()
        a=sign_both(loop,key,task,attempt_changes={"started_at":"2026-11-20T20:14:39Z"})
        with self.assertRaises(ContractError):loop.accept(*a)

    def test_no_task_or_issuance_rejected(self):
        loop,key,task=fixture()
        loop.attempts.issuances.clear()
        with self.assertRaises(ContractError):loop.accept(*sign_both(loop,key,task))

    def test_no_local_closure_from_source_guard(self):
        loop,key,task=fixture()
        a=sign_both(loop,key,task,attempt_changes={"local_closure":True})
        with self.assertRaises(ContractError):loop.accept(*a)
        self.assertEqual(loop.snapshot()["credited_count"],0)

    def test_failed_marker_rejected(self):
        loop,key,task=fixture()
        a=sign_both(loop,key,task,attempt_changes={"marker_present":False})
        with self.assertRaises(ContractError):loop.accept(*a)

    def test_untrusted_role_rejected(self):
        loop,key,task=fixture()
        a=sign_both(loop,key,task,attempt_changes={"validator_role":"lean_kernel"})
        with self.assertRaises(ContractError):loop.accept(*a)

    def test_positive_affine_preserves_strict_order(self):
        m=PositiveAffineClockMap(7,31)
        for a in range(-3,4):
            for b in range(-3,4):
                self.assertTrue(m.preserves_before(a,b))

    def test_constant_map_rejected(self):
        with self.assertRaises(ContractError):PositiveAffineClockMap(0,0)

    def test_time_reversal_rejected(self):
        with self.assertRaises(ContractError):PositiveAffineClockMap(-1,0)

    def test_bool_scale_rejected(self):
        with self.assertRaises(ContractError):PositiveAffineClockMap(True,0)

    def test_noninteger_tick_rejected(self):
        with self.assertRaises(ContractError):PositiveAffineClockMap(1,0).map(1.5)

    def test_two_distinct_attempts_one_run_family(self):
        loop,key,task=fixture()
        loop.accept(*sign_both(loop,key,task))
        task2=loop.issue(HEAD,1,phase="meso",nonce="phase373-second-task-0002")
        loop.register_issuance(Issuance(task2.id,"github:issuecomment:fixture",ISSUE_AT))
        loop.accept(*sign_both(loop,key,task2,attempt=3,job="136542423197"))
        self.assertEqual(loop.snapshot()["credited_count"],2)
        self.assertEqual({e.run_id for e in loop.attempts.consumed_executions},
                         {"44809412040"})

    def test_same_attempt_reused_for_second_task_rejected(self):
        loop,key,task=fixture()
        loop.accept(*sign_both(loop,key,task))
        task2=loop.issue(HEAD,1,phase="meso",nonce="phase373-second-task-0003")
        loop.register_issuance(Issuance(task2.id,"github:issuecomment:fixture",ISSUE_AT))
        with self.assertRaises(ContractError):
            loop.accept(*sign_both(loop,key,task2))
        self.assertEqual(loop.snapshot()["credited_count"],1)

if __name__=="__main__":
    unittest.main()
