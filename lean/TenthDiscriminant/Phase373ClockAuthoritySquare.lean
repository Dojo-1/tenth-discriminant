import TenthDiscriminant.Phase372ExecutionAttempts

/-!
# Phase373 — clock-authority compatibility square

Research CLOCKS (fast, meso, review) are NOT GitHub event times.
An issued research task must be authorized on its original manifest clock,
and executable on the target plane, before any timestamp transport.
A strict order-preserving time map can transport a causal inequality;
a merely monotone map may collapse issuance and execution.

This models only explicit policy and order constraints. It does NOT implement
GitHub, SHA256, Ed25519, external timestamp authentication or number theory.
-/
namespace TenthDiscriminant.Phase373

set_option autoImplicit false

inductive ResearchClock
  | fast | meso | review
  deriving DecidableEq, Repr

inductive ResearchArm
  | sourceAnchor | prologCounterworld | leanFormalization | externalReview
  deriving DecidableEq, Repr

inductive ExecutionPlane
  | githubCI | humanReview
  deriving DecidableEq, Repr

/-- This is an audited four-arm *projection* of the frozen Phase368 manifest,
not a claim that Lean parses the entire JSON manifest. -/
def Allowed : ResearchArm → ResearchClock → Prop
  | .sourceAnchor, .meso => True
  | .prologCounterworld, .fast => True
  | .leanFormalization, .meso => True
  | .externalReview, .review => True
  | _, _ => False

def CanExecute : ResearchArm → ResearchClock → ExecutionPlane → Prop
  | .sourceAnchor, .meso, .githubCI => True
  | .prologCounterworld, .fast, .githubCI => True
  | .leanFormalization, .meso, .githubCI => True
  | .externalReview, .review, .humanReview => True
  | _, _, _ => False

/-- Scheduling tiers in the original Phase368 Python *nest*:
meso includes fast-native Worldlets and review includes both lower tiers.
They are not wall-clock timestamps. -/
def TierAdmits : ResearchClock → ResearchClock → Prop
  | .fast, .fast => True
  | .meso, .fast => True
  | .meso, .meso => True
  | .review, _ => True
  | _, _ => False

def NativeAdmissible (a : ResearchArm) (tier native : ResearchClock) : Prop :=
  Allowed a native ∧ TierAdmits tier native

def TierAuthorizable (a : ResearchArm) (tier native : ResearchClock)
    (p : ExecutionPlane) : Prop :=
  NativeAdmissible a tier native ∧ CanExecute a native p

theorem fast_native_prolog_on_meso_tier :
    TierAuthorizable .prologCounterworld .meso .fast .githubCI := by
  simp [TierAuthorizable, NativeAdmissible, TierAdmits, Allowed, CanExecute]

theorem source_native_meso_not_on_fast_tier :
    ¬ TierAuthorizable .sourceAnchor .fast .meso .githubCI := by
  simp [TierAuthorizable, NativeAdmissible, TierAdmits]

def Authorizable (a : ResearchArm) (c : ResearchClock)
    (p : ExecutionPlane) : Prop :=
  Allowed a c ∧ CanExecute a c p

/-- Historical Phase371 fast issuance CANNOT be transported as a current
Phase368 source-anchor selection. This rejection is intentional. -/
theorem historical_fast_source_rejected :
    ¬ Authorizable .sourceAnchor .fast .githubCI := by
  simp [Authorizable, Allowed]

theorem meso_source_authorized :
    Authorizable .sourceAnchor .meso .githubCI := by
  simp [Authorizable, Allowed, CanExecute]

theorem review_requires_human :
    ¬ Authorizable .externalReview .review .githubCI := by
  simp [Authorizable, CanExecute]

theorem review_human_authorized :
    Authorizable .externalReview .review .humanReview := by
  simp [Authorizable, Allowed, CanExecute]

/-- A clock map includes a *strict* temporal transport law.
Any independent trust in this map must come from an external witness. -/
structure StrictTimeTransport where
  toUtc : Nat → Nat
  strict : StrictMono toUtc

/-- Preserve strict causal ordering across a certified clock change. -/
theorem causal_order_forward (f : StrictTimeTransport) {issue start : Nat}
    (h : issue < start) : f.toUtc issue < f.toUtc start :=
  f.strict h

/-- Reflect causal ordering: a strict transport cannot invent a positive
order separation between timestamps that were not ordered originally. -/
theorem causal_order_reflect (f : StrictTimeTransport) {issue start : Nat}
    (h : f.toUtc issue < f.toUtc start) : issue < start := by
  by_contra hn
  have hrev : start ≤ issue := by omega
  have hmap : f.toUtc start ≤ f.toUtc issue := f.strict.monotone hrev
  omega

/-- Mere nondecreasing maps need not preserve strict event separation. -/
theorem constant_time_map_collapses_causality :
    Monotone (fun _ : Nat => (0 : Nat)) ∧
    ¬ StrictMono (fun _ : Nat => (0 : Nat)) := by
  constructor
  · intro a b hab
    simp
  · intro h
    have hh : (0 : Nat) < (1 : Nat) := by decide
    have bad := h hh
    simpa using bad

/-- Authorized transition between logical research clocks.
The map must transport both permission and strict order. -/
structure ClockBridge (a : ResearchArm) (c₁ c₂ : ResearchClock) where
  permission : Allowed a c₁ → Allowed a c₂
  transport : StrictTimeTransport

def ClockBridge.comp {a : ResearchArm}
    {c₁ c₂ c₃ : ResearchClock}
    (f : ClockBridge a c₁ c₂) (g : ClockBridge a c₂ c₃) :
    ClockBridge a c₁ c₃ :=
  { permission := fun h => g.permission (f.permission h)
    transport :=
      { toUtc := g.transport.toUtc ∘ f.transport.toUtc
        strict := g.transport.strict.comp f.transport.strict } }

/-- No permission-preserving meso-to-fast bridge can be constructed for the
source-anchor arm under this exact frozen policy projection. -/
theorem no_source_meso_to_fast_bridge :
    ¬ Nonempty (ClockBridge .sourceAnchor .meso .fast) := by
  rintro ⟨bridge⟩
  have h : Allowed .sourceAnchor .meso := by trivial
  have bad := bridge.permission h
  simp [Allowed] at bad

/-- A viable task has an ORIGINAL authorization witness, not a claim about
where its result later happens to be observed. -/
structure AuthorizedTask where
  arm : ResearchArm
  schedulingTier : ResearchClock
  nativeClock : ResearchClock
  executionPlane : ExecutionPlane
  policyVersion : Nat
  authorized : TierAuthorizable arm schedulingTier nativeClock executionPlane

/-- Evidence transport keeps authorization with the *original* task. -/
structure EvidenceSquare where
  task : AuthorizedTask
  sourceVersion : Nat
  receiptVersion : Nat
  issued : Nat
  started : Nat
  validated : Nat
  timeTransport : StrictTimeTransport
  sourceMatched : sourceVersion = receiptVersion
  issuedBeforeStart : timeTransport.toUtc issued < started
  startBeforeValidation : started ≤ validated

theorem evidence_square_causality (s : EvidenceSquare) :
    s.timeTransport.toUtc s.issued < s.validated := by
  exact lt_of_lt_of_le s.issuedBeforeStart s.startBeforeValidation

theorem evidence_square_preserves_policy_authority (s : EvidenceSquare) :
    TierAuthorizable s.task.arm s.task.schedulingTier
      s.task.nativeClock s.task.executionPlane :=
  s.task.authorized

/-- A constant timestamp map cannot discharge the positive causal constraint,
even though it is monotone. -/
theorem flat_clock_invalid_transport :
    ¬ ∃ t : StrictTimeTransport, (∀ n, t.toUtc n = 0) := by
  rintro ⟨t, ht⟩
  have h := t.strict (show (0 : Nat) < 1 by omega)
  rw [ht 0, ht 1] at h
  omega

end TenthDiscriminant.Phase373

#print axioms TenthDiscriminant.Phase373.fast_native_prolog_on_meso_tier
#print axioms TenthDiscriminant.Phase373.causal_order_reflect
#print axioms TenthDiscriminant.Phase373.no_source_meso_to_fast_bridge
#print axioms TenthDiscriminant.Phase373.evidence_square_causality
