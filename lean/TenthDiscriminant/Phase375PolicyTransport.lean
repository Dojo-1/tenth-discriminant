import TenthDiscriminant.Phase374ManifestRefinement

/-!
Phase375 — versioned authorization with typed semantic remainder.

Migration does not change when a task was issued. A fresh policy may widen
permissions but cannot retroactively create a permit under an older policy.
Transport requires old AND new permission, equality of the relevant
source/scope/execution/native-clock meaning, and an explicitly distinct
approver. This Lean model does not verify cryptography, signer independence,
trusted time, GitHub, or number-field correctness.
-/

namespace TenthDiscriminant.Phase375
open TenthDiscriminant.Phase373
open TenthDiscriminant.Phase374
set_option autoImplicit false

inductive Source
  | originalTraceGram | maximalOrderD203
  deriving DecidableEq, Repr

inductive Scope
  | sourceContract | matrixGeneral | encodedLemma | fieldSemantic
  deriving DecidableEq, Repr

inductive Executor
  | local | externalHuman
  deriving DecidableEq, Repr

/-- A meaning is multi-typed: not a scalar score or a coordinate label. -/
structure ArmMeaning where
  source : Source
  scope : Scope
  execution : Executor
  nativeClock : ResearchClock
  deriving DecidableEq, Repr

structure Policy where
  version : Nat
  eligible : Fin 8 → Bool
  meaning : Fin 8 → ArmMeaning

/-- The original issuing policy is fixed in the type. -/
structure FrozenPermit (p : Policy) where
  arm : Fin 8
  issuer : Nat
  issuedAt : Nat
  permissionAtIssue : p.eligible arm = true

/-- A migration witness is a *conditional* formal certificate.
The external approver field is an untrusted symbolic identity until checked. -/
structure MigrationEdge (p q : Policy) (a : Fin 8) (issuer : Nat) where
  oldAllowed : p.eligible a = true
  newAllowed : q.eligible a = true
  meaningPreserved : p.meaning a = q.meaning a
  approver : Nat
  notSelfApproved : approver ≠ issuer
  versionAdvances : p.version < q.version

/-- A transported view retains the ORIGINAL permit and its version. -/
structure TransportedView (p q : Policy) where
  original : FrozenPermit p
  edge : MigrationEdge p q original.arm original.issuer

theorem transport_retains_original_permission {p q : Policy}
    (t : TransportedView p q) :
    p.eligible t.original.arm = true :=
  t.original.permissionAtIssue

theorem transport_has_target_permission {p q : Policy}
    (t : TransportedView p q) :
    q.eligible t.original.arm = true :=
  t.edge.newAllowed

theorem transport_preserves_typed_meaning {p q : Policy}
    (t : TransportedView p q) :
    p.meaning t.original.arm = q.meaning t.original.arm :=
  t.edge.meaningPreserved

theorem transport_does_not_rewrite_version {p q : Policy}
    (t : TransportedView p q) :
    p.version < q.version :=
  t.edge.versionAdvances

/-- Sequential authorized edges compose without erasing original authority.
The second approver remains a distinct symbolic principal, not an independently
authenticated key. -/
def MigrationEdge.comp {p q r : Policy} {a : Fin 8} {issuer : Nat}
    (f : MigrationEdge p q a issuer) (g : MigrationEdge q r a issuer) :
    MigrationEdge p r a issuer :=
  { oldAllowed := f.oldAllowed
    newAllowed := g.newAllowed
    meaningPreserved := f.meaningPreserved.trans g.meaningPreserved
    approver := g.approver
    notSelfApproved := g.notSelfApproved
    versionAdvances := lt_trans f.versionAdvances g.versionAdvances }

/-- Phase374's *checked finite* source eligibility is the old policy floor.
Semantics below are symbolic representations of the same source-contract arm;
only this arm is used in the concrete counterexamples. -/
def baselineMeaning : ArmMeaning :=
  { source := .originalTraceGram, scope := .sourceContract,
    execution := .local, nativeClock := .meso }

def d203Meaning : ArmMeaning :=
  { source := .maximalOrderD203, scope := .sourceContract,
    execution := .local, nativeClock := .meso }

def oldFastPolicy : Policy :=
  { version := 374
    eligible := fun a => manifestEligible a .fast 9 true false
    meaning := fun _ => baselineMeaning }

def widenedFastPolicy : Policy :=
  { version := 375
    eligible := fun a => if a.val = 0 then true else manifestEligible a .fast 9 true false
    meaning := fun _ => baselineMeaning }

def changedSourcePolicy : Policy :=
  { version := 376
    eligible := fun _ => true
    meaning := fun a => if a.val = 0 then d203Meaning else baselineMeaning }

def compatiblePolicy : Policy :=
  { version := 376
    eligible := fun _ => true
    meaning := fun _ => baselineMeaning }

theorem historical_fast_not_allowed :
    oldFastPolicy.eligible (0 : Fin 8) = false := by
  decide

theorem newly_widened_fast_permission :
    widenedFastPolicy.eligible (0 : Fin 8) = true := by
  decide

/-- Later permission widening cannot issue a task under an earlier policy. -/
theorem no_retroactive_fast_issuance :
    ¬ ∃ t : FrozenPermit oldFastPolicy, t.arm = (0 : Fin 8) := by
  rintro ⟨t, ht⟩
  have allowed : oldFastPolicy.eligible (0 : Fin 8) = true := by
    simpa [ht] using t.permissionAtIssue
  have rejected : oldFastPolicy.eligible (0 : Fin 8) = false := by decide
  rw [rejected] at allowed
  cases allowed

/-- Target permission alone does not create a migration certificate. -/
theorem widening_without_prior_permission_not_migratable :
    ¬ Nonempty (MigrationEdge oldFastPolicy widenedFastPolicy (0 : Fin 8) 7) := by
  rintro ⟨edge⟩
  have rejected : oldFastPolicy.eligible (0 : Fin 8) = false := by decide
  have allowed := edge.oldAllowed
  rw [rejected] at allowed
  cases allowed

theorem changed_source_prevents_silent_migration :
    ¬ Nonempty (MigrationEdge widenedFastPolicy changedSourcePolicy (0 : Fin 8) 7) := by
  rintro ⟨edge⟩
  have changed :
      widenedFastPolicy.meaning (0 : Fin 8) ≠
        changedSourcePolicy.meaning (0 : Fin 8) := by
    decide
  exact changed edge.meaningPreserved

/-- Constructive positive control for an explicit, semantically compatible
migration; these policies are synthetic and NOT signed repository policies. -/
def compatibleEdge : MigrationEdge widenedFastPolicy compatiblePolicy (0 : Fin 8) 7 :=
  { oldAllowed := by decide
    newAllowed := by decide
    meaningPreserved := by decide
    approver := 8
    notSelfApproved := by decide
    versionAdvances := by decide }

theorem compatible_transition_exists :
    Nonempty (MigrationEdge widenedFastPolicy compatiblePolicy (0 : Fin 8) 7) :=
  ⟨compatibleEdge⟩

end TenthDiscriminant.Phase375

#print axioms TenthDiscriminant.Phase375.no_retroactive_fast_issuance
#print axioms TenthDiscriminant.Phase375.changed_source_prevents_silent_migration
#print axioms TenthDiscriminant.Phase375.compatible_transition_exists
