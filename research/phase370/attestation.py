"""Phase370: provenance-bound OUTCOME ROUTING, not a mathematical proof oracle.

Only a separate key custodian / verifier can sign receipts. The selector holds
PUBLIC verification keys; it has no signing key and no claim-promotion method.

Cryptography authenticates an external signer's statement, not its truth.
The signer must independently verify actual CI logs and math semantics.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import hashlib
import json
import re
import secrets
from typing import Mapping

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'phase368'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'phase369'))
from polybandit import ContractError, Receipt
from policy import PendingParetoBandit


HEX40 = re.compile(r'^[a-f0-9]{40}$')
HEX64 = re.compile(r'^[a-f0-9]{64}$')


def canonical(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, ensure_ascii=True,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(obj: object) -> str:
    return hashlib.sha256(canonical(obj)).hexdigest()


@dataclass(frozen=True)
class TaskIntent:
    id: str
    arm: str
    scope: str
    source: str
    repository_head: str
    issued_epoch: int
    research_clock: str
    cost_units: int
    nonce: str


@dataclass(frozen=True)
class Outcome:
    task_id: str
    arm: str
    scope: str
    source: str
    repository_head: str
    validator_role: str
    verifier_id: str
    artifact_digest: str
    run_id: str
    success_marker: str
    marker_present: bool
    exception_present: bool
    execution_ok: bool
    diagnostic: bool
    local_closure: bool
    cost_units: int


@dataclass(frozen=True)
class SignedOutcome:
    data: Outcome
    signature_hex: str


@dataclass(frozen=True)
class TrustEntry:
    public_key_hex: str
    allowed_roles: tuple[str, ...]


class EvidenceLoop:
    """Scheduling + receipt-authentication facade. NOT a process sandbox.

    A mutable Python caller can still alter its own memory. A real service
    must isolate it and authenticate verifier messages over a separate channel.
    """
    def __init__(self, manifest: dict, trust: Mapping[str, TrustEntry]):
        self.policy = PendingParetoBandit(manifest)
        self.trust = dict(trust)
        self.tasks: dict[str, TaskIntent] = {}
        self.consumed: set[str] = set()
        self.chain: list[dict] = []
        self.ledger_head = '0' * 64

    def _append(self, event: str, data: dict) -> None:
        record = {'seq': len(self.chain) + 1, 'event': event, 'data': data,
                  'previous': self.ledger_head}
        record['hash'] = digest(record)
        self.chain.append(record)
        self.ledger_head = record['hash']

    def issue(self, repository_head: str, budget: int, phase: str = 'meso',
              nonce: str | None = None) -> TaskIntent:
        if HEX40.fullmatch(repository_head) is None:
            raise ContractError('exact 40-character commit SHA required')
        if nonce is None:
            nonce = secrets.token_hex(16)
        if len(nonce) < 16:
            raise ContractError('nonce too short')
        if any(task.nonce == nonce for task in self.tasks.values()):
            raise ContractError('reused task nonce')
        chosen = self.policy.choose(budget, phase=phase)
        fields = {'arm': chosen.id, 'scope': chosen.scope,
                  'source': chosen.source, 'repository_head': repository_head,
                  'issued_epoch': self.policy.epoch, 'research_clock': phase,
                  'cost_units': chosen.cost, 'nonce': nonce}
        task = TaskIntent(digest(fields), **fields)
        self.tasks[task.id] = task
        self._append('task_issued', {'task_id': task.id, 'arm': task.arm,
                                     'head': task.repository_head})
        return task

    def accept(self, signed: SignedOutcome) -> None:
        """Validate BEFORE any observation-state mutation; fail closed.

        The signing verifier must separately check actual CI job/log/artifacts.
        This method cannot independently establish mathematical field semantics.
        """
        a = signed.data
        task = self.tasks.get(a.task_id)
        if task is None or a.task_id in self.consumed:
            raise ContractError('unsolicited or replayed task receipt')
        if self.policy.pending.get(task.arm) != task.issued_epoch:
            raise ContractError('task not outstanding at its exact epoch')
        if ((a.arm, a.scope, a.source, a.repository_head, a.cost_units) !=
            (task.arm, task.scope, task.source, task.repository_head,
             task.cost_units)):
            raise ContractError('receipt is not the issued task or source')
        if not HEX64.fullmatch(a.artifact_digest):
            raise ContractError('invalid artifact digest')
        if not a.run_id or a.run_id == '0':
            raise ContractError('no externally traceable execution identifier')
        allowed_role = {'encoded_lemma': 'lean_kernel',
                        'source_contract': 'source_guard',
                        'matrix_general': 'prolog_exact',
                        'field_301_semantic': 'independent_human'}
        expected = allowed_role.get(task.scope)
        if task.scope == 'field_301_semantic' and self.policy.arms[task.arm].execution == 'local':
            expected = ('prolog_exact' if self.policy.arms[task.arm].purpose == 'falsify'
                        else 'source_guard')
        if expected is None or a.validator_role != expected:
            raise ContractError('wrong authority for task claim scope')
        signer = self.trust.get(a.verifier_id)
        if signer is None or a.validator_role not in signer.allowed_roles:
            raise ContractError('unknown or unauthorized external verifier')
        if not HEX64.fullmatch(signer.public_key_hex):
            raise ContractError('invalid trusted public key')
        try:
            Ed25519PublicKey.from_public_bytes(bytes.fromhex(signer.public_key_hex)).verify(
                bytes.fromhex(signed.signature_hex), canonical(asdict(a)))
        except (InvalidSignature, ValueError, TypeError) as exc:
            raise ContractError('invalid external signature') from exc
        if not (a.execution_ok and a.marker_present and not a.exception_present):
            raise ContractError('workflow false green / missing success witness')
        if not a.success_marker.startswith('VERIFIED_'):
            raise ContractError('invalid required success marker')
        if a.local_closure and not (
             (task.scope == 'encoded_lemma' and a.validator_role == 'lean_kernel')
             or (self.policy.arms[task.arm].purpose == 'field_review'
                 and a.validator_role == 'independent_human')):
            raise ContractError('only scoped formal or external review can close its local obligation')
        receipt = Receipt(a.task_id, a.arm, a.source, a.scope,
                          'human_external' if a.validator_role == 'independent_human'
                          else a.validator_role, a.diagnostic, a.local_closure)
        # Phase368's Receipt vocabulary omits source_guard; verified source
        # guard checks remain routing diagnostics and never theorem closure.
        if a.validator_role == 'source_guard':
            receipt = Receipt(a.task_id, a.arm, a.source, a.scope,
                              'prolog_exact', a.diagnostic, False)
        self.policy.approved_receipts[a.task_id] = receipt
        try:
            self.policy.observe(receipt)
        finally:
            self.policy.approved_receipts.pop(a.task_id, None)
        self.consumed.add(a.task_id)
        self._append('verified_observation', {'task_id': a.task_id,
                         'artifact_sha256': a.artifact_digest,
                         'verifier': a.verifier_id, 'run_id': a.run_id,
                         'diagnostic': a.diagnostic,
                         'local_closure': a.local_closure})

    def verify_chain(self) -> bool:
        previous = '0' * 64
        for idx, entry in enumerate(self.chain, 1):
            if entry['seq'] != idx or entry['previous'] != previous:
                return False
            unsigned = {k: v for k, v in entry.items() if k != 'hash'}
            if digest(unsigned) != entry['hash']:
                return False
            previous = entry['hash']
        return previous == self.ledger_head

    def snapshot(self) -> dict:
        return {'pending': sorted(self.policy.pending),
                'verified_observations': len(self.consumed),
                'ledger_head': self.ledger_head,
                'integrity_ok': self.verify_chain(),
                'routing': self.policy.export(),
                'no_claim_promotion_interface': True}
