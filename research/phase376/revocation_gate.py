"""Phase376: offline revocation-aware, key-separated migration admission.

Security boundary:
- Public keys are provided by an UNAUTHENTICATED local directory;
- the local tick is NOT a trusted external clock;
- synthetic signatures in tests are NOT independent human witnesses;
- the event list is not externally anchored and can be rewritten.

The gate intentionally has NO field-theorem-promotion function.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from hashlib import sha256
import re
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase375"))
from policy_transport import (
    Snapshot, OriginTask, SignedMigration, MigrationClaim,
    PolicyMigrationGate, PublicAuthority, ContractError, canonical_bytes
)

HEX64 = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class PublicCredential:
    key_id: str
    public_key_hex: str
    roles: tuple[str, ...]
    registered_at: int


@dataclass(frozen=True)
class SignedOrigin:
    task: OriginTask
    signed_by_key_id: str
    signature_hex: str


@dataclass(frozen=True)
class RevocationNotice:
    key_id: str
    signed_by_governor: str
    effective_at: int
    reason: str
    regime: str = "phase376-fixture-registry-v1"


@dataclass(frozen=True)
class SignedRevocation:
    notice: RevocationNotice
    signature_hex: str


@dataclass(frozen=True)
class HistoricalAcceptance:
    task_id: str
    old_policy_digest: str
    new_policy_digest: str
    issuer_key_id: str
    approver_key_id: str
    accepted_at: int
    signed_claim_sha256: str


class RevocationAwareMigration:
    """History-preserving authorization gate; external facts are trust inputs.

    Replays are refused by Phase375's task/target receipt accounting.
    New approvals fail if either issuer or approver key is currently revoked.
    Accepted historical records remain immutable *as Python values* but the
    in-memory dictionary itself is not append-only or independent.
    """

    def __init__(self, keys: tuple[PublicCredential, ...]):
        self.keys: dict[str, PublicCredential] = {}
        fingerprints: set[str] = set()
        for key in keys:
            if (not key.key_id or key.key_id in self.keys
                or not HEX64.fullmatch(key.public_key_hex)
                or key.public_key_hex in fingerprints
                or type(key.registered_at) is not int or key.registered_at < 0
                or not key.roles):
                raise ContractError("invalid or alias-reused public-key identity")
            self.keys[key.key_id] = key
            fingerprints.add(key.public_key_hex)
        self.phase375 = PolicyMigrationGate({
            k: PublicAuthority(v.public_key_hex,v.roles)
            for k,v in self.keys.items()
        })
        self.tick = 0
        self.revoked_at: dict[str,int] = {}
        self.origin_evidence: dict[str, tuple[str,int,str]] = {}
        self.accepted: dict[tuple[str,str],HistoricalAcceptance] = {}
        self.events: list[dict[str,Any]] = []

    def advance(self, new_tick: int) -> None:
        # No rollback once a revocation has been observed. Tick itself is
        # still caller-controlled; authentication belongs to an outside clock.
        if type(new_tick) is not int or new_tick < self.tick:
            raise ContractError("non-monotone registry observation clock")
        self.tick = new_tick

    def _active(self, key_id: str, role: str) -> PublicCredential:
        key = self.keys.get(key_id)
        if key is None or role not in key.roles:
            raise ContractError("unregistered or unauthorized key role")
        if self.tick < key.registered_at:
            raise ContractError("key used before registration")
        if key_id in self.revoked_at and self.tick >= self.revoked_at[key_id]:
            raise ContractError("key revoked for new admissions")
        return key

    @staticmethod
    def _verify(key: PublicCredential, signature_hex: str, value: object) -> None:
        try:
            sig = bytes.fromhex(signature_hex)
            Ed25519PublicKey.from_public_bytes(bytes.fromhex(
                key.public_key_hex)).verify(sig,canonical_bytes(value))
        except (InvalidSignature, ValueError, TypeError) as exc:
            raise ContractError("invalid signed envelope") from exc

    def register_snapshot(self,snapshot:Snapshot) -> None:
        self.phase375.register_snapshot(snapshot)

    def register_origin(self,origin:SignedOrigin) -> None:
        if origin.signed_by_key_id != origin.task.issuer_id:
            raise ContractError("origin signer and issuer identity mismatch")
        issuer=self._active(origin.signed_by_key_id,"issue_task")
        self._verify(issuer,origin.signature_hex,asdict(origin.task))
        self.phase375.register_origin(origin.task)
        digest=sha256(canonical_bytes(asdict(origin.task))).hexdigest()
        self.origin_evidence[origin.task.task_id]=(issuer.key_id,self.tick,digest)
        self.events.append({"kind":"origin_accepted_fixture","task_id":origin.task.task_id,
                            "issuer_key_id":issuer.key_id,"tick":self.tick})

    def revoke(self, signed:SignedRevocation) -> None:
        n=signed.notice
        target=self.keys.get(n.key_id)
        if target is None or n.key_id in self.revoked_at:
            raise ContractError("unknown or already revoked target")
        if not n.reason.strip() or n.regime!="phase376-fixture-registry-v1":
            raise ContractError("unqualified revocation")
        if type(n.effective_at) is not int or n.effective_at != self.tick:
            raise ContractError("backdated or future revocation forbidden")
        guardian=self._active(n.signed_by_governor,"revoke_key")
        if guardian.public_key_hex==target.public_key_hex:
            raise ContractError("key cannot revoke itself")
        self._verify(guardian,signed.signature_hex,asdict(n))
        self.revoked_at[n.key_id]=self.tick
        self.events.append({"kind":"revocation_recorded_fixture","target":n.key_id,
                            "guardian":guardian.key_id,"tick":self.tick,
                            "reason":n.reason})

    def approve(self, signed:SignedMigration) -> HistoricalAcceptance:
        claim=signed.claim
        historical=self.origin_evidence.get(claim.task_id)
        if historical is None:
            raise ContractError("historical origin was not independently signed in fixture")
        issuer_id,_,_ = historical
        if issuer_id != claim.issuer_id:
            raise ContractError("claim does not name original issuer key")
        issuer=self._active(issuer_id,"issue_task")
        approver=self._active(claim.approver_id,"policy_migration")
        if issuer.public_key_hex == approver.public_key_hex:
            raise ContractError("same signing key cannot be its own external approval")
        # Phase375 verifies both policy versions, semantic identity,
        # cost and source, exact signed claim, and replay before recording.
        self.phase375.verify(signed)
        evidence=HistoricalAcceptance(
            claim.task_id, claim.from_snapshot_sha256, claim.to_snapshot_sha256,
            issuer_id, claim.approver_id, self.tick,
            sha256(canonical_bytes(asdict(claim))).hexdigest()
        )
        self.accepted[(claim.task_id,claim.to_snapshot_sha256)]=evidence
        self.events.append({"kind":"migration_accepted_fixture","task_id":claim.task_id,
                            "approver":claim.approver_id,"tick":self.tick,
                            "target":claim.to_snapshot_sha256})
        return evidence

    def snapshot(self) -> dict:
        return {
            "tick":self.tick,
            "revoked_keys":dict(self.revoked_at),
            "historical_acceptances":len(self.accepted),
            "origin_acceptances":len(self.origin_evidence),
            "external_key_registry_authenticated":False,
            "external_clock_authenticated":False,
            "durable_external_event_log":False,
            "field_theorem_promotion_api":False
        }
