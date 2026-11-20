"""Phase372 attempt-level adversarial tests, using SYNTHETIC Ed25519 keys.

All local signatures, issuance timestamps and GH data are fixture inputs.
Passing tests are NOT independently authenticated production evidence.
"""
from dataclasses import asdict,replace
from pathlib import Path
import json,sys,unittest

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

sys.path.insert(0,str(Path(__file__).resolve().parent))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase370"))
from attestation import TaskIntent, TrustEntry, ContractError, canonical
from attempt_contract import (ExecutionIdentity,Issuance,AttemptOutcome,
    SignedAttempt,AttemptEvidenceLoop,GitHubAttemptObservation,
    check_readonly_github_observation,parse_log_lines,utc_epoch)

MANIFEST=json.loads((Path(__file__).resolve().parents[1]/
                     "phase368"/"manifest.json").read_text())
HEAD="b07bb172ad819b297bed46be1547488d3c215d73"
STAMP="2026-11-20T20:14:40Z"
START="2026-11-20T20:14:48Z"
SOURCE="original-integer-pair-ordinary-Z-gram@phase367"
REAL_TASK_ID="c930bcad33042b0f7004f74252f5ae6789617e5f36abfda6728287c4dc135c01"

def fixture():
    key=Ed25519PrivateKey.generate()
    pub=key.public_key().public_bytes(
        serialization.Encoding.Raw,serialization.PublicFormat.Raw).hex()
    loop=AttemptEvidenceLoop(MANIFEST,{
        "outside-ci-verifier":TrustEntry(pub,("source_guard","prolog_exact","lean_kernel"))})
    task=loop.issue(HEAD,budget=1,phase="fast",nonce="phase372-test-issuance-0001")
    loop.register_issuance(Issuance(task.id,"github:issuecomment:7049599129",STAMP))
    return loop,key,task

def signed(key,task,*,issued_at=STAMP,started_at=START,
           run_id="44809412040",attempt=2,job_id="136542423196",
           role="source_guard",validator="outside-ci-verifier",
           **changes):
    e=ExecutionIdentity(run_id,attempt,job_id,task.repository_head)
    a=AttemptOutcome(task.id,task.arm,task.source,task.scope,task.cost_units,
        e,"github:issuecomment:7049599129",issued_at,started_at,
        validator,role,"a"*64,"VERIFIED_PHASE371_SOURCE_ANCHOR",
        True,True,False,True,False)
    a=replace(a,**changes)
    return SignedAttempt(a,key.sign(canonical(asdict(a))).hex())

def real_task():
    return TaskIntent(REAL_TASK_ID,"source_anchor_mutation","source_contract",
       SOURCE,HEAD,1,"fast",1,"phase371-source-anchor-external-issue-20261120-v1")

def real_observation(attempt=2,job_id="136542423196",started=START,content=None):
    task=real_task()
    lines=content if content is not None else (
         "2026-11-20T20:15:00Z Ran 7 tests in 0.001s\n"
         "2026-11-20T20:15:00Z OK\n"
         "2026-11-20T20:15:01Z PHASE371_TASK_ID="+task.id+"\n"
         "2026-11-20T20:15:01Z PHASE371_RUN_ID=44809412040\n"
         "2026-11-20T20:15:01Z PHASE371_RUN_ATTEMPT="+str(attempt)+"\n"
         "2026-11-20T20:15:01Z VERIFIED_PHASE371_SOURCE_ANCHOR\n")
    return GitHubAttemptObservation("Dojo-1/tenth-discriminant",
        ExecutionIdentity("44809412040",attempt,job_id,HEAD),
        started,"success","success",lines)

class AttemptContractTests(unittest.TestCase):
    def test_real_run_family_collision(self):
        first=ExecutionIdentity("44809412040",1,"136541801767",HEAD)
        second=ExecutionIdentity("44809412040",2,"136542423196",HEAD)
        self.assertEqual(first.run_id,second.run_id)
        self.assertNotEqual(first,second)
        self.assertNotEqual(first.job_id,second.job_id)

    def test_issued_authorized_attempt_is_credited(self):
        loop,key,t=fixture()
        loop.accept(signed(key,t))
        self.assertEqual(loop.snapshot()["credited_execution_count"],1)
        self.assertTrue(loop.snapshot()["integrity_ok"])
        self.assertNotIn("promoted_claims",str(loop.snapshot()))

    def test_duplicated_receipt_rejected(self):
        loop,key,t=fixture();r=signed(key,t);loop.accept(r)
        with self.assertRaises(ContractError):loop.accept(r)

    def test_unissued_task_rejected(self):
        loop,key,t=fixture()
        other=replace(t,id="f"*64)
        with self.assertRaises(ContractError):loop.accept(signed(key,other))

    def test_issuance_registration_required(self):
        loop,key,t=fixture();loop.issuances.clear()
        with self.assertRaises(ContractError):loop.accept(signed(key,t))

    def test_wrong_issuance_reference(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,issuance_reference="an-unrelated-comment"))

    def test_wrong_issuance_timestamp(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,issued_at="2026-11-20T20:13:00Z"))

    def test_execution_before_issue_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,started_at="2026-11-20T20:14:39Z"))

    def test_equal_timestamp_not_causal(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,started_at=STAMP))

    def test_same_run_distinct_attempts_distinct_tasks_allowed(self):
        loop,key,t1=fixture()
        loop.accept(signed(key,t1))
        t2=loop.issue(HEAD,budget=1,phase="fast",nonce="phase372-test-issuance-0002")
        loop.register_issuance(Issuance(t2.id,"github:issuecomment:7049599129",
                                        STAMP))
        loop.accept(signed(key,t2,attempt=3,job_id="136542423197",
                           started_at="2026-11-20T20:15:48Z"))
        self.assertEqual(loop.snapshot()["credited_execution_count"],2)
        self.assertEqual({x.run_id for x in loop.consumed_executions},
                         {"44809412040"})

    def test_same_job_under_different_attempt_rejected(self):
        loop,key,t1=fixture();loop.accept(signed(key,t1))
        t2=loop.issue(HEAD,budget=1,phase="fast",nonce="phase372-test-issuance-0003")
        loop.register_issuance(Issuance(t2.id,"github:issuecomment:7049599129",
                                        STAMP))
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t2,attempt=3,job_id="136542423196"))

    def test_wrong_head_rejected(self):
        loop,key,t=fixture()
        e=ExecutionIdentity("44809412040",2,"136542423196","f"*40)
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,execution=e))

    def test_zero_attempt_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,attempt=0))

    def test_wrong_signature_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(
            signed(Ed25519PrivateKey.generate(),t))

    def test_tampered_signed_payload_rejected(self):
        loop,key,t=fixture();r=signed(key,t)
        with self.assertRaises(ContractError):loop.accept(SignedAttempt(
            replace(r.data,diagnostic=False),r.signature_hex))

    def test_wrong_role_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,role="lean_kernel"))

    def test_wrong_source_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,source="maximal-order-D203-phase306"))

    def test_diagnostic_cannot_promote(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,local_closure=True))
        self.assertEqual(loop.snapshot()["credited_task_count"],0)

    def test_false_green_missing_marker(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,marker_present=False))

    def test_false_green_exception(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,exception_present=True))

    def test_wrong_cost_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,cost_units=999))

    def test_malformed_utc_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):loop.accept(signed(
            key,t,started_at="2026-11-20T21:14:48+01:00"))

    def test_frozen_real_attempt_snapshot(self):
        # Recorded GitHub fields are a fixture, NOT a new remote fetch.
        task=real_task()
        issue=Issuance(task.id,"github:issuecomment:7049599129",STAMP)
        result=check_readonly_github_observation(task,issue,real_observation(),
            "VERIFIED_PHASE371_SOURCE_ANCHOR")
        self.assertEqual(len(result),64)

    def test_frozen_first_attempt_not_eligible(self):
        task=real_task();issue=Issuance(task.id,"github:issuecomment:7049599129",STAMP)
        obs=real_observation(1,"136541801767","2026-11-20T20:13:40Z")
        with self.assertRaises(ContractError):
            check_readonly_github_observation(task,issue,obs,
                "VERIFIED_PHASE371_SOURCE_ANCHOR")

    def test_echoed_commands_not_output(self):
        task=real_task();issue=Issuance(task.id,"github:issuecomment:7049599129",STAMP)
        content=("2026-11-20T20:15:01Z echo PHASE371_TASK_ID="+task.id+"\n"
           "2026-11-20T20:15:01Z echo PHASE371_RUN_ID=44809412040\n"
           "2026-11-20T20:15:01Z echo PHASE371_RUN_ATTEMPT=2\n"
           "2026-11-20T20:15:01Z echo VERIFIED_PHASE371_SOURCE_ANCHOR\n")
        with self.assertRaises(ContractError):
            check_readonly_github_observation(task,issue,
                real_observation(content=content),"VERIFIED_PHASE371_SOURCE_ANCHOR")

    def test_duplicate_real_marker_rejected(self):
        task=real_task();issue=Issuance(task.id,"github:issuecomment:7049599129",STAMP)
        orig=real_observation()
        extra="2026-11-20T20:15:02Z VERIFIED_PHASE371_SOURCE_ANCHOR\n"
        with self.assertRaises(ContractError):
            check_readonly_github_observation(task,issue,
                replace(orig,log_text=orig.log_text+extra),
                "VERIFIED_PHASE371_SOURCE_ANCHOR")

    def test_run_green_job_failed_rejected(self):
        task=real_task();issue=Issuance(task.id,"github:issuecomment:7049599129",STAMP)
        with self.assertRaises(ContractError):
            check_readonly_github_observation(task,issue,
                replace(real_observation(),job_conclusion="failure"),
                "VERIFIED_PHASE371_SOURCE_ANCHOR")

    def test_no_excess_authority_from_approved_diag(self):
        loop,key,t=fixture()
        loop.accept(signed(key,t,diagnostic=True,local_closure=False))
        self.assertEqual(loop.base.policy.state[t.arm].closure_hits,0)
        self.assertEqual(loop.base.policy.state[t.arm].diagnostic_hits,1)

    def test_external_issuance_duplicate_rejected(self):
        loop,key,t=fixture()
        with self.assertRaises(ContractError):
            loop.register_issuance(Issuance(t.id,"github:issuecomment:7049599129",STAMP))

    def test_ledger_tamper_detected(self):
        loop,key,t=fixture();loop.accept(signed(key,t))
        self.assertTrue(loop.base.verify_chain())
        loop.base.chain[0]["data"]["head"]="f"*40
        self.assertFalse(loop.base.verify_chain())

if __name__=="__main__":
    unittest.main()
