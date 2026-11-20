"""Phase375 versioned policy migration guard (offline research prototype).

A manifest is an input snapshot, not authenticated merely by hashing it.
A registered historical task is a TRUST INPUT, not a verified GitHub event.
Verifier public keys are external assumptions. Signed fixtures in the tests
use synthetic keys. This module cannot promote mathematical claims.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
from pathlib import Path
import copy
import json
import re
import sys

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase368"))
from polybandit import PolyBandit, ContractError as BanditContractError

HEX64 = re.compile(r"^[0-9a-f]{64}$")
HEX40 = re.compile(r"^[0-9a-f]{40}$")


class ContractError(ValueError):
    pass


def canonical_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("ascii")


@dataclass(frozen=True)
class Snapshot:
    version: int
    json_bytes: bytes
    sha256: str

    @classmethod
    def from_manifest(cls, version: int, manifest: dict) -> "Snapshot":
        if type(version) is not int or version < 0:
            raise ContractError("version must be a nonnegative ordinal")
        # Parse/copy into immutable serialized bytes before storing.
        raw = canonical_bytes(manifest)
        try:
            PolyBandit(json.loads(raw))
        except (BanditContractError, KeyError, TypeError) as err:
            raise ContractError("invalid Phase368 policy manifest") from err
        return cls(version, raw, sha256(raw).hexdigest())

    def manifest(self) -> dict:
        if not HEX64.fullmatch(self.sha256) or sha256(self.json_bytes).hexdigest() != self.sha256:
            raise ContractError("snapshot digest inconsistent with bytes")
        return json.loads(self.json_bytes)

    def arm(self, arm_id: str) -> dict:
        match = [a for a in self.manifest()["arms"] if a["id"] == arm_id]
        if len(match) != 1:
            raise ContractError("arm is missing or duplicated")
        return match[0]

    def meaning(self, arm_id: str) -> tuple:
        m = self.manifest()
        a = self.arm(arm_id)
        w = next(x for x in m["worldlets"] if x["id"] == a["worldlet"])
        # Cost is a resource obligation, so compare and sign it separately.
        return (a["id"], a["worldlet"], a["source"], a["scope"],
                a["execution"], a["purpose"], a["transport"],
                a["remainder"], a["hyperedge"], tuple(sorted(w["clocks"])),
                w["source"])

    def eligible(self, arm_id: str, tier: str, budget: int,
                 include_human: bool, include_contrast: bool) -> bool:
        policy = PolyBandit(self.manifest())
        return arm_id in {a.id for a in policy.eligible(
            budget, include_human=include_human, phase=tier,
            include_contrast=include_contrast)}


@dataclass(frozen=True)
class OriginTask:
    task_id: str
    arm_id: str
    source_snapshot_sha256: str
    issuer_id: str
    tier: str
    budget: int
    include_human: bool
    include_contrast: bool
    issued_external_reference: str


@dataclass(frozen=True)
class MigrationClaim:
    task_id: str
    arm_id: str
    from_snapshot_sha256: str
    to_snapshot_sha256: str
    from_version: int
    to_version: int
    from_cost: int
    to_cost: int
    issuer_id: str
    approver_id: str
    original_external_reference: str
    migration_external_reference: str
    purpose: str = "policy_migration"


@dataclass(frozen=True)
class SignedMigration:
    claim: MigrationClaim
    signature_hex: str


@dataclass(frozen=True)
class PublicAuthority:
    public_key_hex: str
    allowed_roles: tuple[str, ...]


class PolicyMigrationGate:
    """No private signing keys. No external fetch. No theorem-promotion API."""
    def __init__(self, authorities: dict[str, PublicAuthority]):
        self.authorities = dict(authorities)
        self.policies: dict[str, Snapshot] = {}
        self.version_ids: dict[int, str] = {}
        self.tasks: dict[str, OriginTask] = {}
        self.accepted: set[tuple[str, str]] = set()
        self.events: list[dict] = []

    def register_snapshot(self, snapshot: Snapshot) -> None:
        snapshot.manifest()  # revalidate bytes; this alone is not external auth
        if snapshot.sha256 in self.policies:
            raise ContractError("snapshot digest already registered")
        if snapshot.version in self.version_ids:
            raise ContractError("version ordinal cannot point at new bytes")
        self.version_ids[snapshot.version] = snapshot.sha256
        self.policies[snapshot.sha256] = snapshot
        self.events.append({"event": "untrusted_snapshot_registered",
                            "sha256": snapshot.sha256, "version": snapshot.version})

    def register_origin(self, task: OriginTask) -> None:
        """Only a snapshot-relative ELIGIBILITY check, not proof of issuance."""
        if task.task_id in self.tasks or not HEX64.fullmatch(task.task_id):
            raise ContractError("duplicate or malformed task identity")
        if not task.issuer_id or not task.issued_external_reference:
            raise ContractError("missing external issuance identity")
        old = self.policies.get(task.source_snapshot_sha256)
        if old is None:
            raise ContractError("unregistered issuing policy")
        if not old.eligible(task.arm_id, task.tier, task.budget,
                            task.include_human, task.include_contrast):
            raise ContractError("original policy never authorized this arm")
        self.tasks[task.task_id] = task
        self.events.append({"event": "untrusted_origin_registered",
                            "task_id": task.task_id,
                            "policy": old.sha256})

    def verify(self, receipt: SignedMigration) -> None:
        r = receipt.claim
        if r.purpose != "policy_migration":
            raise ContractError("wrong authorization purpose")
        task = self.tasks.get(r.task_id)
        if task is None:
            raise ContractError("unregistered original task")
        if (r.task_id, r.to_snapshot_sha256) in self.accepted:
            raise ContractError("migration already credited")
        old = self.policies.get(r.from_snapshot_sha256)
        new = self.policies.get(r.to_snapshot_sha256)
        if old is None or new is None:
            raise ContractError("one policy snapshot is missing")
        if not (old.version < new.version and
                r.from_version == old.version and r.to_version == new.version):
            raise ContractError("non-forward or mislabelled version transport")
        if (r.task_id, r.arm_id, r.from_snapshot_sha256,
            r.issuer_id, r.original_external_reference) != (
            task.task_id, task.arm_id, task.source_snapshot_sha256,
            task.issuer_id, task.issued_external_reference):
            raise ContractError("signed migration changed historical issuance")
        if not r.migration_external_reference:
            raise ContractError("missing external migration authorization reference")
        if r.approver_id == task.issuer_id:
            raise ContractError("issuer cannot approve its own migration")
        signer = self.authorities.get(r.approver_id)
        if signer is None or "policy_migration" not in signer.allowed_roles:
            raise ContractError("untrusted migration authority")
        if not HEX64.fullmatch(signer.public_key_hex):
            raise ContractError("invalid registered public key")
        if not old.eligible(task.arm_id, task.tier, task.budget,
                            task.include_human, task.include_contrast):
            raise ContractError("original arm is not authorized")
        if not new.eligible(task.arm_id, task.tier, task.budget,
                            task.include_human, task.include_contrast):
            raise ContractError("target manifest refuses eligibility")
        if old.meaning(task.arm_id) != new.meaning(task.arm_id):
            raise ContractError("source/scope/worldlet/clock/authority meaning changed")
        old_cost, new_cost = old.arm(task.arm_id)["cost"], new.arm(task.arm_id)["cost"]
        if (r.from_cost, r.to_cost) != (old_cost, new_cost):
            raise ContractError("cost information mismatches frozen versions")
        # A cost change may be authorized only if explicitly recorded and
        # budget eligibility remains true in BOTH versions.
        try:
            sig = bytes.fromhex(receipt.signature_hex)
            Ed25519PublicKey.from_public_bytes(bytes.fromhex(
                signer.public_key_hex)).verify(sig, canonical_bytes(asdict(r)))
        except (InvalidSignature, ValueError, TypeError) as err:
            raise ContractError("invalid signed migration claim") from err
        # Record only after ALL checks, with the original issuance unchanged.
        self.accepted.add((r.task_id, r.to_snapshot_sha256))
        self.events.append({"event": "migration_allowed_in_fixture",
                            "task_id": r.task_id,
                            "origin": old.sha256, "target": new.sha256,
                            "external_reference": r.migration_external_reference,
                            "approver": r.approver_id})

    def snapshot(self) -> dict:
        return {"origin_tasks": len(self.tasks),
                "registered_policies": len(self.policies),
                "accepted_migrations": len(self.accepted),
                "no_claim_promotion_api": True,
                "external_authentication_implemented": False}
