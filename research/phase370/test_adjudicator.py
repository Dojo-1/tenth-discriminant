"""Phase370: verifier fixture tests. NO live keys or CI API calls."""
from dataclasses import replace
import unittest
from test_attestation import fixture, HEAD
from adjudicator import WorkflowEvidence, attest_ci_task
from attestation import ContractError


class ExternalVerifierControls(unittest.TestCase):
    def data(self, task):
        return WorkflowEvidence('Dojo-1/tenth-discriminant','44753393399',
             '136346823629',task.repository_head,'success','success',
             'PHASE370_TASK_ID=' + task.id + '\nVERIFIED_PROLOG_TESTS\n',True)

    def test_issued_bound_workflow_with_external_key_fixture(self):
        loop,key=fixture();t=loop.issue(HEAD,1,nonce='nonce-verifier-0001')
        r=attest_ci_task(t,self.data(t),key=key,verifier_id='auditor-outside-policy',
              role='source_guard',marker='VERIFIED_PROLOG_TESTS',diagnostic=True)
        loop.accept(r)
        self.assertTrue(loop.verify_chain())

    def test_old_success_run_not_sufficient(self):
        loop,key=fixture();t=loop.issue(HEAD,1,nonce='nonce-verifier-0002')
        old=replace(self.data(t),log_text='PASS nonreal_full_original_evaluation_gram\nPHASE367_BOUNDED_FACTOR_ORACLE_PASS\n')
        with self.assertRaisesRegex(ContractError,'not bound to issued'):
            attest_ci_task(t,old,key=key,verifier_id='auditor-outside-policy',
                          role='source_guard',marker='VERIFIED_PROLOG_TESTS')

    def test_historical_false_green_is_rejected(self):
        loop,key=fixture();t=loop.issue(HEAD,1,nonce='nonce-verifier-0003')
        old=replace(self.data(t),run_id='44753105275',
          log_text='PHASE370_TASK_ID='+t.id+'\nVERIFIED_PROLOG_TESTS\n'
                   'warning: unknown directive consult/1\n'
                   'uncaught exception: error(existence_error(procedure,test/2))\n')
        with self.assertRaisesRegex(ContractError,'forbidden'):
            attest_ci_task(t,old,key=key,verifier_id='auditor-outside-policy',
                          role='source_guard',marker='VERIFIED_PROLOG_TESTS')

    def test_yamls_command_echo_not_valid(self):
        loop,key=fixture();t=loop.issue(HEAD,1,nonce='nonce-verifier-0004')
        old=replace(self.data(t),log_text='run: echo PHASE370_TASK_ID='+t.id+'\n'
                                        'run: echo VERIFIED_PROLOG_TESTS\n')
        with self.assertRaisesRegex(ContractError,'not bound'):
            attest_ci_task(t,old,key=key,verifier_id='auditor-outside-policy',
                          role='source_guard',marker='VERIFIED_PROLOG_TESTS')

    def test_wrong_head_and_unsigned_fetch(self):
        loop,key=fixture();t=loop.issue(HEAD,1,nonce='nonce-verifier-0005')
        for d in (replace(self.data(t),head_sha='f'*40),
                  replace(self.data(t),trusted_fetch=False),
                  replace(self.data(t),run_conclusion='failure')):
            with self.subTest(d=d),self.assertRaises(ContractError):
                attest_ci_task(t,d,key=key,verifier_id='auditor-outside-policy',
                               role='source_guard',marker='VERIFIED_PROLOG_TESTS')

    def test_gh_runner_echoed_guard_not_a_failure(self):
        loop,key=fixture();t=loop.issue(HEAD,1,nonce='nonce-verifier-0007')
        stamp='2026-11-20T14:27:25.7964355Z '
        txt=(stamp + "if grep -E 'uncaught exception' /tmp/log; then exit 1; fi" + "\n"
             + stamp + 'PHASE370_TASK_ID=' + t.id + "\n"
             + stamp + 'VERIFIED_PROLOG_TESTS' + "\n")
        good=replace(self.data(t),log_text=txt)
        receipt=attest_ci_task(t,good,key=key,verifier_id='auditor-outside-policy',
                  role='source_guard',marker='VERIFIED_PROLOG_TESTS',diagnostic=True)
        loop.accept(receipt)
        self.assertTrue(loop.verify_chain())

    def test_field_claim_not_signed_from_ci(self):
        loop,key=fixture();t=loop.issue(HEAD,1,nonce='nonce-verifier-0006')
        with self.assertRaisesRegex(ContractError,'independent field review'):
            attest_ci_task(t,self.data(t),key=key,verifier_id='auditor-outside-policy',
                           role='independent_human',marker='VERIFIED_PROLOG_TESTS',local_closure=True)

if __name__=='__main__': unittest.main()
