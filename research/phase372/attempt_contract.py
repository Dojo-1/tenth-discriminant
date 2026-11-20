"""Phase372: attempt-aware signed observations, without a theorem promotion API.

Provenance layers: GitHub run family != execution attempt != job.
The selector holds public keys only and must not generate its own signatures.
All clock/issuance facts supplied to this library require an external reader.
This module does NOT fetch or authenticate GitHub or verify number theory.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase370"))
from attestation import (EvidenceLoop, TaskIntent, TrustEntry, Receipt,
                         ContractError, canonical, digest, HEX40, HEX64)

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

POSITIVE_DECIMAL=re.compile(r"^[1-9][0-9]*$")


@dataclass(frozen=True)
class ExecutionIdentity:
    run_id: str
    attempt: int
    job_id: str
    head_sha: str

    def validate(self) -> None:
        if not POSITIVE_DECIMAL.fullmatch(self.run_id):
            raise ContractError("invalid GitHub run family")
        if not POSITIVE_DECIMAL.fullmatch(self.job_id):
            raise ContractError("invalid GitHub job identity")
        if not isinstance(self.attempt,int) or isinstance(self.attempt,bool) or self.attempt<1:
            raise ContractError("invalid attempt ordinal")
        if not HEX40.fullmatch(self.head_sha):
            raise ContractError("invalid execution commit")


@dataclass(frozen=True)
class Issuance:
    task_id: str
    external_reference: str
    issued_at: str


@dataclass(frozen=True)
class AttemptOutcome:
    task_id: str
    arm: str
    source: str
    scope: str
    cost_units: int
    execution: ExecutionIdentity
    issuance_reference: str
    issued_at: str
    started_at: str
    verifier_id: str
    validator_role: str
    log_sha256: str
    completion_marker: str
    marker_present: bool
    execution_ok: bool
    exception_present: bool
    diagnostic: bool
    local_closure: bool


@dataclass(frozen=True)
class SignedAttempt:
    data: AttemptOutcome
    signature_hex: str


def utc_epoch(value: str) -> float:
    try:
        if not isinstance(value,str) or not value.endswith("Z"):
            raise ValueError("UTC Z suffix required")
        ts=datetime.fromisoformat(value.replace("Z","+00:00"))
        if ts.tzinfo != timezone.utc:
            raise ValueError("UTC offset required")
        return ts.timestamp()
    except (TypeError,ValueError,OverflowError) as exc:
        raise ContractError("invalid canonical UTC timestamp") from exc


class AttemptEvidenceLoop:
    """Phase370 scheduler + stronger Phase372 attempt-specific receipt gate.

    Registering issuance is a TRUST INPUT, not authentication. Production must
    authenticate the external issuance reference and actual GitHub metadata.
    """
    def __init__(self,manifest:dict,trust:dict[str,TrustEntry]):
        self.base=EvidenceLoop(manifest,trust)
        self.issuances:dict[str,Issuance]={}
        self.consumed_tasks:set[str]=set()
        self.consumed_executions:set[ExecutionIdentity]=set()
        self.consumed_jobs:set[str]=set()

    def issue(self,head:str,budget:int=1,phase:str="meso",
              nonce:str|None=None)->TaskIntent:
        return self.base.issue(head,budget,phase,nonce)

    def register_issuance(self,issuance:Issuance)->None:
        if issuance.task_id not in self.base.tasks:
            raise ContractError("externally referenced task not issued by selector")
        if issuance.task_id in self.issuances:
            raise ContractError("issuance already registered")
        if not issuance.external_reference.strip():
            raise ContractError("missing external issuance reference")
        utc_epoch(issuance.issued_at)
        self.issuances[issuance.task_id]=issuance
        self.base._append("external_issuance_registered",
                          {"task_id":issuance.task_id,
                           "reference":issuance.external_reference})

    def accept(self,signed:SignedAttempt)->None:
        a=signed.data
        task=self.base.tasks.get(a.task_id)
        if task is None or a.task_id in self.consumed_tasks:
            raise ContractError("unsolicited or replayed task")
        issue=self.issuances.get(a.task_id)
        if issue is None:
            raise ContractError("no authenticated external issuance witness")
        if self.base.policy.pending.get(task.arm)!=task.issued_epoch:
            raise ContractError("no outstanding matching selection")
        e=a.execution
        e.validate()
        if ((a.arm,a.scope,a.source,a.cost_units,e.head_sha) !=
            (task.arm,task.scope,task.source,task.cost_units,task.repository_head)):
            raise ContractError("attempt not bound to selected source/scope/commit")
        if (a.issuance_reference!=issue.external_reference or
            a.issued_at!=issue.issued_at):
            raise ContractError("issuance timestamp or reference not bound")
        if not utc_epoch(a.issued_at)<utc_epoch(a.started_at):
            raise ContractError("execution did not start AFTER task issuance")
        if e in self.consumed_executions or e.job_id in self.consumed_jobs:
            raise ContractError("execution/job replay")
        if a.task_id in self.consumed_tasks:
            raise ContractError("task replay")
        if not HEX64.fullmatch(a.log_sha256):
            raise ContractError("invalid evidence digest")
        if not a.completion_marker.startswith("VERIFIED_"):
            raise ContractError("unrecognized completion marker")
        if not (a.execution_ok and a.marker_present and not a.exception_present):
            raise ContractError("execution failed or marker absent")
        permissions={"encoded_lemma":"lean_kernel",
                     "source_contract":"source_guard",
                     "matrix_general":"prolog_exact"}
        arm=self.base.policy.arms[task.arm]
        expected=permissions.get(task.scope)
        if task.scope=="field_301_semantic":
            if arm.execution=="human" and arm.purpose=="field_review":
                expected="independent_human"
            elif arm.execution=="local":
                expected="prolog_exact" if arm.purpose=="falsify" else "source_guard"
        if expected is None or a.validator_role!=expected:
            raise ContractError("validator role not authorized for task type")
        signer=self.base.trust.get(a.verifier_id)
        if signer is None or a.validator_role not in signer.allowed_roles:
            raise ContractError("signature verifier unknown or forbidden")
        if not HEX64.fullmatch(signer.public_key_hex):
            raise ContractError("invalid registered public key")
        if a.local_closure and not (
            (task.scope=="encoded_lemma" and a.validator_role=="lean_kernel") or
            (arm.purpose=="field_review" and a.validator_role=="independent_human")):
            raise ContractError("attempt to self-promote a diagnostic into closure")
        try:
            Ed25519PublicKey.from_public_bytes(bytes.fromhex(signer.public_key_hex)).verify(
                bytes.fromhex(signed.signature_hex),canonical(asdict(a)))
        except (InvalidSignature,ValueError,TypeError) as exc:
            raise ContractError("signature verification failed") from exc
        # Phase368's own evidence taxonomy uses "prolog_exact" for a
        # source guard diagnostic; NEVER use that alias as a proof closure.
        validator=("human_external" if a.validator_role=="independent_human" else
                   "prolog_exact" if a.validator_role=="source_guard" else
                   a.validator_role)
        receipt=Receipt(a.task_id,a.arm,a.source,a.scope,validator,
                        a.diagnostic,a.local_closure)
        self.base.policy.approved_receipts[a.task_id]=receipt
        try:
            self.base.policy.observe(receipt)
        finally:
            self.base.policy.approved_receipts.pop(a.task_id,None)
        self.consumed_tasks.add(a.task_id)
        self.consumed_executions.add(e)
        self.consumed_jobs.add(e.job_id)
        self.base._append("attempt_credited",{"task_id":a.task_id,
           "run_id":e.run_id,"attempt":e.attempt,"job_id":e.job_id,
           "head_sha":e.head_sha,"log_sha256":a.log_sha256,
           "validator":a.verifier_id,"local_closure":a.local_closure})

    def snapshot(self)->dict:
        return {"credited_task_count":len(self.consumed_tasks),
                "credited_execution_count":len(self.consumed_executions),
                "credited_job_count":len(self.consumed_jobs),
                "pending":sorted(self.base.policy.pending),
                "integrity_ok":self.base.verify_chain(),
                "no_claim_promotion_interface":True}


@dataclass(frozen=True)
class GitHubAttemptObservation:
    """Frozen data supplied by a read-only GitHub adapter (not authenticated here)."""
    repository: str
    execution: ExecutionIdentity
    started_at: str
    run_conclusion: str
    job_conclusion: str
    log_text: str


def parse_log_lines(log_text:str)->list[str]:
    """Return candidate *actual output* lines, excluding echoed runner commands."""
    cleaned=[]
    for raw in log_text.splitlines():
        line=re.sub(r"\x1b\[[0-9;]*m","",raw)
        line=re.sub(r"^\d{4}-\d\d-\d\dT[^ ]+Z\s*","",line).strip()
        if not line or line.startswith(("##[group]Run ","run: ","shell: ",
             "grep ","if grep ","echo ","test ","##[endgroup]",
             "[command]","##[debug]")):
            continue
        cleaned.append(line)
    return cleaned


def check_readonly_github_observation(task:TaskIntent,issuance:Issuance,
    actual:GitHubAttemptObservation,marker:str)->str:
    """Validate a transport snapshot, WITHOUT signing or claiming auth.

    A separate trusted fetcher must establish that actual came from GitHub.
    This guard is never itself an independent attestation.
    """
    e=actual.execution
    e.validate()
    if actual.repository!="Dojo-1/tenth-discriminant":
        raise ContractError("wrong GitHub repository")
    if e.head_sha!=task.repository_head:
        raise ContractError("execution not on issued commit")
    if issuance.task_id!=task.id:
        raise ContractError("issuance does not match task")
    if utc_epoch(actual.started_at)<=utc_epoch(issuance.issued_at):
        raise ContractError("attempt started before issuance")
    if actual.run_conclusion!="success" or actual.job_conclusion!="success":
        raise ContractError("workflow/job did not both succeed")
    if not marker.startswith("VERIFIED_"):
        raise ContractError("weak completion marker")
    lines=parse_log_lines(actual.log_text)
    required=[f"PHASE371_TASK_ID={task.id}",
              f"PHASE371_RUN_ID={e.run_id}",
              f"PHASE371_RUN_ATTEMPT={e.attempt}",marker]
    if any(lines.count(s)!=1 for s in required):
        raise ContractError("missing, duplicated or command-echo-only markers")
    forbidden=("uncaught exception","warning: unknown directive",
               "sorryax","admitax","unsolved goals")
    if any(bad in line.lower() for line in lines for bad in forbidden):
        raise ContractError("log contains unhandled failure")
    return digest({"execution":asdict(e),"task_id":task.id,
                   "log_sha256":digest({"log":actual.log_text})})
