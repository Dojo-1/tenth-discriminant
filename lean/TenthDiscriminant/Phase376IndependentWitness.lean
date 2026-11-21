import TenthDiscriminant.Phase375PolicyTransport

/-!
# Phase376 — independent witnesses and revocation time

A public-key fingerprint, not an editable actor alias, distinguishes
authorities. Revocation blocks NEW approvals at or after its cutoff;
an accepted historic record retains its ORIGINAL authorizing snapshot.

All keys, fingerprints, timestamps, signatures and policy versions are
symbolic. Lean does not verify Ed25519, an authenticated key directory,
historical timestamps, GitHub evidence, or number-theoretic claims.
-/

namespace TenthDiscriminant.Phase376
set_option autoImplicit false

structure Credential where
  keyId : Nat
  publicFingerprint : Nat
  registeredAt : Nat
  revokedAt : Option Nat
  deriving DecidableEq, Repr

def ActiveAt (c : Credential) (tick : Nat) : Prop :=
  c.registeredAt ≤ tick ∧
    ∀ cutoff : Nat, c.revokedAt = some cutoff → tick < cutoff

theorem revoked_blocks_new_authority (c : Credential)
    (cutoff tick : Nat) (hrev : c.revokedAt = some cutoff)
    (hclock : cutoff ≤ tick) : ¬ ActiveAt c tick := by
  intro hactive
  have hlt := hactive.2 cutoff hrev
  omega

theorem pre_registration_not_active (c : Credential) (tick : Nat)
    (h : tick < c.registeredAt) : ¬ ActiveAt c tick := by
  intro hactive
  exact Nat.not_le_of_gt h hactive.1

/-- The authority witness has an explicit observation time: issuer and
approver identity cannot be established from actor aliases alone. -/
structure AuthorizedAt (issuer approver : Credential) (tick : Nat) where
  distinctPublicKeys : issuer.publicFingerprint ≠ approver.publicFingerprint
  issuerActive : ActiveAt issuer tick
  approverActive : ActiveAt approver tick

theorem alias_names_do_not_establish_independence
    (issuer approver : Credential) (tick : Nat)
    (h : issuer.publicFingerprint = approver.publicFingerprint) :
    ¬ Nonempty (AuthorizedAt issuer approver tick) := by
  rintro ⟨w⟩
  exact w.distinctPublicKeys h

theorem revoked_approver_cannot_authorize (issuer approver : Credential)
    (cutoff tick : Nat) (hrev : approver.revokedAt = some cutoff)
    (hclock : cutoff ≤ tick) :
    ¬ Nonempty (AuthorizedAt issuer approver tick) := by
  rintro ⟨w⟩
  exact revoked_blocks_new_authority approver cutoff tick hrev hclock
    w.approverActive

theorem revoked_issuer_cannot_authorize (issuer approver : Credential)
    (cutoff tick : Nat) (hrev : issuer.revokedAt = some cutoff)
    (hclock : cutoff ≤ tick) :
    ¬ Nonempty (AuthorizedAt issuer approver tick) := by
  rintro ⟨w⟩
  exact revoked_blocks_new_authority issuer cutoff tick hrev hclock
    w.issuerActive

/-- Revocation events require a third, distinct governance public key.
Their external signing and time source remain unproved. -/
structure RevocationWitness (target guardian : Credential) where
  effectiveAt : Nat
  targetRevoked : target.revokedAt = some effectiveAt
  guardianActive : ActiveAt guardian effectiveAt
  notSamePublicKey : target.publicFingerprint ≠ guardian.publicFingerprint

/-- A migration still carries its exact Phase375 original permit and edge.
These are not restated as post-revocation permissions. -/
structure WitnessedMigration (p q : Phase375.Policy) where
  original : Phase375.FrozenPermit p
  edge : Phase375.MigrationEdge p q original.arm original.issuer
  issuerCredential : Credential
  approverCredential : Credential
  decidedAt : Nat
  issuerMatches : original.issuer = issuerCredential.keyId
  approverMatches : edge.approver = approverCredential.keyId
  authorization : AuthorizedAt issuerCredential approverCredential decidedAt

theorem witnessed_migration_preserves_original_policy {p q : Phase375.Policy}
    (r : WitnessedMigration p q) :
    p.eligible r.original.arm = true :=
  r.original.permissionAtIssue

theorem witnessed_migration_preserves_meaning {p q : Phase375.Policy}
    (r : WitnessedMigration p q) :
    p.meaning r.original.arm = q.meaning r.original.arm :=
  r.edge.meaningPreserved

/-- A *historical* acceptance does not mutate when registry policy later
changes. The new registry must be used for NEW admission decisions. -/
structure HistoricalAcceptance (p q : Phase375.Policy) where
  approval : WitnessedMigration p q
  recordedAt : Nat
  recordedAfterDecision : approval.decidedAt ≤ recordedAt

theorem historical_record_retains_origin {p q : Phase375.Policy}
    (record : HistoricalAcceptance p q) :
    p.eligible record.approval.original.arm = true :=
  record.approval.original.permissionAtIssue

/-- Registered clock watermarks cannot move backwards; a supplied clock
value alone is not an authenticated monotonic clock. -/
structure ClockWatermark where
  lastObserved : Nat

def MayAdvance (s : ClockWatermark) (next : Nat) : Prop :=
  s.lastObserved ≤ next

theorem clock_rollback_rejected (s : ClockWatermark) (next : Nat)
    (hrollback : next < s.lastObserved) : ¬ MayAdvance s next := by
  intro h
  exact Nat.not_le_of_gt hrollback h

def demoKey : Credential :=
  { keyId := 12, publicFingerprint := 42,
    registeredAt := 2, revokedAt := some 7 }

theorem demo_key_valid_before_revocation : ActiveAt demoKey 6 := by
  constructor
  · decide
  · intro cutoff h
    change some (7 : Nat) = some cutoff at h
    have hc : 7 = cutoff := Option.some.inj h
    omega

theorem demo_key_invalid_at_cutoff : ¬ ActiveAt demoKey 7 := by
  exact revoked_blocks_new_authority demoKey 7 7 rfl (Nat.le_refl 7)

end TenthDiscriminant.Phase376

#print axioms TenthDiscriminant.Phase376.revoked_blocks_new_authority
#print axioms TenthDiscriminant.Phase376.alias_names_do_not_establish_independence
#print axioms TenthDiscriminant.Phase376.witnessed_migration_preserves_original_policy
