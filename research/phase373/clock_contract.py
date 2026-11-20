"""Phase373: source-exact, manifest-version-bound research-clock admission.

A research-clock phase (fast/meso/review) is NOT a UTC timestamp. The
current Phase368 scheduler regards meso as admitting fast+meso arms, and
review as admitting fast+meso+review arms. Keep this exact hierarchy.

This module checks permissions and signed metadata; it neither fetches
GitHub nor authenticates external issuance records or signs outcomes.
No claim promotion method exists. All tests use synthetic signatures.
"""
from __future__ import annotations

import copy
from dataclasses import asdict, dataclass
from pathlib import Path
import sys

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase372"))
from attempt_contract import (
    AttemptEvidenceLoop, ExecutionIdentity, SignedAttempt, ContractError,
    HEX64, canonical, digest, utc_epoch,
)

PHASE_CAPABILITIES = {
    "fast": frozenset(("fast",)),
    "meso": frozenset(("fast", "meso")),
    "review": frozenset(("fast", "meso", "review")),
}
CLOCK_ORDER = ("review", "meso", "fast")


@dataclass(frozen=True)
class ClockPermit:
    task_id: str
    policy_sha256: str
    research_phase: str
    native_worldlet_clock: str
    worldlet_id: str
    source: str


@dataclass(frozen=True)
class ClockStamp:
    task_id: str
    execution: ExecutionIdentity
    policy_sha256: str
    research_phase: str
    native_worldlet_clock: str
    worldlet_id: str
    source: str
    issued_at: str
    started_at: str
    validated_at: str
    verifier_id: str


@dataclass(frozen=True)
class SignedClockStamp:
    data: ClockStamp
    signature_hex: str


@dataclass(frozen=True)
class PositiveAffineClockMap:
    """Illustration of a strictly order-preserving map on integer ticks.

    A positive scale preserves and reflects order; a constant map does not.
    A claimed map is not evidence that any physical clock follows it.
    """
    scale: int
    offset: int

    def __post_init__(self) -> None:
        if isinstance(self.scale, bool) or not isinstance(self.scale, int) or self.scale <= 0:
            raise ContractError("time map must be strictly increasing")
        if isinstance(self.offset, bool) or not isinstance(self.offset, int):
            raise ContractError("time-map offset must be an integer")

    def map(self, tick: int) -> int:
        if isinstance(tick, bool) or not isinstance(tick, int):
            raise ContractError("tick must be an integer")
        return self.scale * tick + self.offset

    def preserves_before(self, a: int, b: int) -> bool:
        return (a < b) == (self.map(a) < self.map(b))


class ClockBoundLoop:
    """Auditable *simulation* of the two independent authorization edges.

    Edge 1: original policy snapshot authorizes (arm, scheduling phase).
    Edge 2: external signer states the run/attempt/time evidence for that task.

    The authority of the signer, trust in timestamps and SHA256 manifest
    preservation are explicit assumptions, not mathematical conclusions.
    """
    def __init__(self, manifest: dict, trust: dict):
        self.manifest = copy.deepcopy(manifest)
        self.manifest_sha256 = digest(self.manifest)
        self.attempts = AttemptEvidenceLoop(copy.deepcopy(self.manifest), trust)
        self.permits: dict[str, ClockPermit] = {}

    def issue(self, head: str, budget: int, phase: str = "meso",
              nonce: str | None = None):
        if phase not in PHASE_CAPABILITIES:
            raise ContractError("unknown scheduling phase")
        if digest(self.manifest) != self.manifest_sha256:
            raise ContractError("policy snapshot mutated")
        # The inherited selector must genuinely select this arm.
        task = self.attempts.issue(head, budget, phase, nonce)
        policy = self.attempts.base.policy
        arm = policy.arms[task.arm]
        worldlet = policy.worldlets[arm.worldlet]
        eligible_clocks = set(worldlet.clocks) & PHASE_CAPABILITIES[phase]
        if not eligible_clocks:
            raise ContractError("internal scheduler/manifest authorization mismatch")
        selected = next(c for c in CLOCK_ORDER if c in eligible_clocks)
        permit = ClockPermit(task.id, self.manifest_sha256, phase,
                             selected, arm.worldlet, task.source)
        self.permits[task.id] = permit
        return task

    def register_issuance(self, issuance):
        # TRUST INPUT: caller has not independently authenticated comment/time.
        self.attempts.register_issuance(issuance)

    def accept(self, signed_attempt: SignedAttempt,
               signed_clock: SignedClockStamp) -> None:
        task_id = signed_attempt.data.task_id
        task = self.attempts.base.tasks.get(task_id)
        permit = self.permits.get(task_id)
        stamp = signed_clock.data
        if task is None or permit is None:
            raise ContractError("clock receipt not attached to a selected task")
        if digest(self.manifest) != self.manifest_sha256:
            raise ContractError("policy snapshot changed after task issuance")
        if task.research_clock != permit.research_phase:
            raise ContractError("scheduler task clock differs from frozen clock permit")
        policy = self.attempts.base.policy
        arm = policy.arms[task.arm]
        native = policy.worldlets[arm.worldlet].clocks
        if (permit.native_worldlet_clock not in native or
            permit.native_worldlet_clock not in PHASE_CAPABILITIES[permit.research_phase]):
            raise ContractError("native clock lacks authorized scheduling transport")
        if ((stamp.task_id, stamp.execution, stamp.policy_sha256,
             stamp.research_phase, stamp.native_worldlet_clock,
             stamp.worldlet_id, stamp.source)
            != (task_id, signed_attempt.data.execution, permit.policy_sha256,
                permit.research_phase, permit.native_worldlet_clock,
                permit.worldlet_id, permit.source)):
            raise ContractError("signed clock square does not commute")
        if stamp.verifier_id != signed_attempt.data.verifier_id:
            raise ContractError("clock and attempt are signed by different authorities")
        if (stamp.issued_at != signed_attempt.data.issued_at or
            stamp.started_at != signed_attempt.data.started_at):
            raise ContractError("clock and execution timestamps disagree")
        if utc_epoch(stamp.started_at) > utc_epoch(stamp.validated_at):
            raise ContractError("validation preceded execution")
        if utc_epoch(stamp.issued_at) >= utc_epoch(stamp.started_at):
            raise ContractError("no strict causal issuance-to-start order")
        if not HEX64.fullmatch(stamp.policy_sha256):
            raise ContractError("invalid policy snapshot digest")
        signer = self.attempts.base.trust.get(stamp.verifier_id)
        if signer is None or signed_attempt.data.validator_role not in signer.allowed_roles:
            raise ContractError("clock metadata signed by unauthorized principal")
        try:
            Ed25519PublicKey.from_public_bytes(bytes.fromhex(signer.public_key_hex)).verify(
                bytes.fromhex(signed_clock.signature_hex), canonical(asdict(stamp)))
        except (InvalidSignature, ValueError, TypeError) as exc:
            raise ContractError("invalid external clock signature") from exc
        # The Phase372 gate enforces signature, role, task/attempt identity,
        # source, head, issuance and replay constraints separately.
        self.attempts.accept(signed_attempt)
        self.attempts.base._append("clock_square_accepted", {
            "task_id": task_id,
            "policy_sha256": permit.policy_sha256,
            "phase": permit.research_phase,
            "native_clock": permit.native_worldlet_clock,
            "worldlet": permit.worldlet_id,
        })

    def snapshot(self) -> dict:
        return {
            "manifest_sha256": self.manifest_sha256,
            "permit_count": len(self.permits),
            "credited_count": len(self.attempts.consumed_tasks),
            "integrity_ok": self.attempts.base.verify_chain(),
            "no_claim_promotion_interface": True,
        }
