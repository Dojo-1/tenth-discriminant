"""Phase370 external verifier contract (test harness only).

This MUST run outside the selector process with a separately held private key.
A production adapter must FETCH run metadata and log bytes from GitHub over
an authenticated read-only channel. Supplying in-memory records is a fixture,
not independent adjudication. Old CI runs are not eligible as newly issued tasks.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import hashlib

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from attestation import ContractError, Outcome, SignedOutcome, TaskIntent, canonical


@dataclass(frozen=True)
class WorkflowEvidence:
    repository: str
    run_id: str
    job_id: str
    head_sha: str
    run_conclusion: str
    job_conclusion: str
    log_text: str
    trusted_fetch: bool  # set by external read-only fetcher, NOT user input


def attest_ci_task(task: TaskIntent, evidence: WorkflowEvidence,
                   *, key: Ed25519PrivateKey, verifier_id: str,
                   role: str, marker: str, diagnostic: bool = False,
                   local_closure: bool = False) -> SignedOutcome:
    """Check externally obtained CI response. No field theorem authority.

    The caller and signer MUST independently verify the source of evidence.
    The 'trusted_fetch' switch is a seam for a real external fetcher, NOT
    an authenticated property in this sample class.
    """
    if role not in {'lean_kernel','prolog_exact','source_guard'}:
        raise ContractError('CI signer cannot attest independent field review')
    if evidence.repository != 'Dojo-1/tenth-discriminant':
        raise ContractError('wrong repository')
    if evidence.head_sha != task.repository_head:
        raise ContractError('wrong commit for issued work')
    if evidence.run_conclusion != 'success' or evidence.job_conclusion != 'success':
        raise ContractError('failed or incomplete CI job')
    if not evidence.run_id.isdigit() or not evidence.job_id.isdigit():
        raise ContractError('untraceable CI identity')
    if not evidence.trusted_fetch:
        raise ContractError('CI payload not delivered by external trusted fetcher')
    logs = evidence.log_text.splitlines()
    if f'PHASE370_TASK_ID={task.id}' not in logs:
        raise ContractError('workflow not bound to issued task ID')
    if marker not in logs or not marker.startswith('VERIFIED_'):
        raise ContractError('workflow lacks exact checked completion marker')
    forbidden = ('uncaught exception', 'warning: unknown directive',
                 'sorryax', 'admitax', 'unsolved goals')
    if any(s in evidence.log_text.lower() for s in forbidden):
        raise ContractError('job log contains forbidden error or proof escape')
    data = Outcome(task.id, task.arm, task.scope, task.source,
                   task.repository_head, role, verifier_id,
                   hashlib.sha256(evidence.log_text.encode('utf-8')).hexdigest(),
                   evidence.run_id, marker, True, False, True,
                   diagnostic, local_closure, task.cost_units)
    return SignedOutcome(data, key.sign(canonical(asdict(data))).hex())
