"""Phase370: offline adversarial contract tests using SYNTHETIC signing keys.
The generated test keys DO NOT represent independent review authority.
"""
from dataclasses import replace, asdict
from pathlib import Path
import json
import unittest

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

from attestation import (EvidenceLoop, SignedOutcome, Outcome, TrustEntry,
                         ContractError, canonical, digest)

MANIFEST = json.loads((Path(__file__).resolve().parents[1] / 'phase368' / 'manifest.json').read_text())
HEAD = 'b497d7a211d2ea2d8460b9ebef93f6c6a328f07d'


def fixture():
    key = Ed25519PrivateKey.generate()
    pub = key.public_key().public_bytes(serialization.Encoding.Raw,
                                         serialization.PublicFormat.Raw).hex()
    trust = {'auditor-outside-policy': TrustEntry(pub, (
       'source_guard','prolog_exact','lean_kernel'))}
    return EvidenceLoop(MANIFEST, trust), key


def signed(key, task, *, role='source_guard', diag=True, close=False, verifier_id='auditor-outside-policy', **changes):
    data = Outcome(task.id,task.arm,task.scope,task.source,
                   task.repository_head,role,verifier_id,
                   digest({'synthetic_artifact':task.id}), 'run-demo-42',
                   'VERIFIED_TEST_ARTIFACT',True,False,True,diag,close,
                   task.cost_units)
    data=replace(data,**changes)
    return SignedOutcome(data,key.sign(canonical(asdict(data))).hex())


class ProvenanceTests(unittest.TestCase):
    def test_good_signed_receipt_and_chain(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000001')
        loop.accept(signed(key,task))
        self.assertEqual(loop.policy.state[task.arm].diagnostic_hits,1)
        self.assertEqual(loop.snapshot()['verified_observations'],1)
        self.assertTrue(loop.snapshot()['integrity_ok'])
        self.assertNotIn(task.arm,loop.policy.pending)
        self.assertNotIn('promoted_claims',str(loop.snapshot()))

    def test_reject_no_issue_and_duplicate(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000002')
        out=signed(key,task)
        loop.accept(out)
        with self.assertRaises(ContractError): loop.accept(out)
        bogus=replace(out.data,task_id='f'*64)
        with self.assertRaises(ContractError): loop.accept(SignedOutcome(bogus,out.signature_hex))

    def test_unsigned_and_wrong_signer(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000003')
        good=signed(key,task)
        with self.assertRaises(ContractError):loop.accept(SignedOutcome(good.data,'00'*64))
        with self.assertRaises(ContractError):loop.accept(signed(Ed25519PrivateKey.generate(),task))
        self.assertIn(task.arm,loop.policy.pending)

    def test_mutated_signed_payload(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000004')
        good=signed(key,task)
        hacked=replace(good.data,diagnostic=False)
        with self.assertRaises(ContractError):loop.accept(SignedOutcome(hacked,good.signature_hex))

    def test_cross_source_and_stale_commit(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000005')
        with self.assertRaises(ContractError):loop.accept(signed(key,task,source='maximal-order-D203-phase306'))
        with self.assertRaises(ContractError):loop.accept(signed(key,task,repository_head='f'*40))
        self.assertEqual(loop.policy.state[task.arm].observations,0)

    def test_false_green_exception_or_missing_marker(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000006')
        for changes in ({'exception_present':True},{'marker_present':False},
                        {'success_marker':''},{'execution_ok':False}):
            with self.subTest(**changes),self.assertRaises(ContractError):
                loop.accept(signed(key,task,**changes))
        self.assertEqual(loop.policy.state[task.arm].observations,0)

    def test_no_prolog_promotion(self):
        loop,key=fixture(); t=loop.issue(HEAD,2,phase='fast',nonce='nonce-0000000000007')
        self.assertEqual(t.arm,'prolog_clock_counterworld')
        with self.assertRaises(ContractError):loop.accept(signed(key,t,role='prolog_exact',close=True))
        loop.accept(signed(key,t,role='prolog_exact',diag=True))
        self.assertEqual(loop.policy.state[t.arm].closure_hits,0)

    def test_field_review_requires_external_signature(self):
        loop,key=fixture()
        t=loop.issue(HEAD,8,phase='review',nonce='nonce-0000000000008')
        while t.arm!='external_field_chart_reconstruction':
            t=loop.issue(HEAD,8,phase='review',nonce='nonce-'+str(loop.policy.epoch).zfill(16))
        with self.assertRaises(ContractError):loop.accept(signed(key,t,role='lean_kernel',close=True))
        human = Ed25519PrivateKey.generate()
        pub = human.public_key().public_bytes(serialization.Encoding.Raw,serialization.PublicFormat.Raw).hex()
        loop.trust['external-human-review'] = TrustEntry(pub,('independent_human',))
        loop.accept(signed(human,t,role='independent_human',close=True,verifier_id='external-human-review'))
        self.assertEqual(loop.policy.state[t.arm].closure_hits,1)
        self.assertNotIn('promoted_claims',str(loop.snapshot()))

    def test_untrusted_validator_role_not_authorized(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000009')
        loop.trust['auditor-outside-policy']=TrustEntry(
            loop.trust['auditor-outside-policy'].public_key_hex,('prolog_exact',))
        with self.assertRaises(ContractError):loop.accept(signed(key,task))

    def test_unselected_task_and_conflicting_nonce(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000010')
        with self.assertRaises(ContractError):loop.issue(HEAD,1,nonce=task.nonce)
        with self.assertRaises(ContractError):loop.issue(HEAD,1,nonce='nonce-0000000000011')

    def test_accounting_before_acceptance(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000012')
        self.assertEqual(loop.policy.state[task.arm].observations,0)
        self.assertEqual(loop.snapshot()['verified_observations'],0)
        self.assertEqual(len(loop.policy.pending),1)

    def test_tampered_ledger_detected(self):
        loop,key=fixture();task=loop.issue(HEAD,1,nonce='nonce-0000000000013')
        self.assertTrue(loop.verify_chain())
        loop.chain[0]['data']['arm']='forged'
        self.assertFalse(loop.verify_chain())

    def test_deterministic_digest_nonmatching_payload(self):
        self.assertNotEqual(digest({'a':1}),digest({'a':2}))
        self.assertEqual(digest({'a':1,'b':2}),digest({'b':2,'a':1}))

    def test_no_shared_ci_and_external_human_key(self):
        loop,key=fixture()
        pub=loop.trust['auditor-outside-policy'].public_key_hex
        bad={'ci':TrustEntry(pub,('source_guard',)),
             'external':TrustEntry(pub,('independent_human',))}
        with self.assertRaises(ContractError):EvidenceLoop(MANIFEST,bad)

    def test_no_dual_role_signer(self):
        loop,key=fixture()
        pub=loop.trust['auditor-outside-policy'].public_key_hex
        with self.assertRaises(ContractError):EvidenceLoop(MANIFEST,{
            'self':TrustEntry(pub,('source_guard','independent_human'))})

    def test_one_run_cannot_pay_two_tasks(self):
        loop,key=fixture()
        first=loop.issue(HEAD,1,nonce='nonce-run-reuse-0001')
        loop.accept(signed(key,first))
        next_task=loop.issue(HEAD,1,nonce='nonce-run-reuse-0002')
        with self.assertRaises(ContractError):loop.accept(signed(key,next_task))
        self.assertEqual(loop.policy.state[next_task.arm].observations,1)

    def test_reject_invalid_commit(self):
        loop,_=fixture()
        with self.assertRaises(ContractError):loop.issue('not-a-commit',1)
        self.assertEqual(loop.policy.epoch,0)

if __name__=='__main__': unittest.main()
