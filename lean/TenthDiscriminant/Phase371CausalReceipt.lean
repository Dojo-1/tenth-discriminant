import Mathlib

/-!
# Phase371 — authorized evidence-transition state machine

Formal governance model for the Phase370 issued-task / verified-receipt boundary.
This file is NOT a formalization of Ed25519, GitHub, Python, or number theory.
The booleans signatureAuthorized and executionVerified are external
assumptions and MUST be checked by independent mechanisms outside the policy.

The purpose here is to prove that, GIVEN sound external input flags, a typed
transition cannot credit a never-issued task, reuse a task or a run identifier,
or lose the no-duplicate accounting invariant over an arbitrary transition trace.
The same-original integer trace Gram source is not changed by this module.
-/

namespace TenthDiscriminant.Phase371

set_option autoImplicit false

structure Task where
  id : Nat
  source : Nat
  repositoryHead : Nat
  scope : Nat
  deriving DecidableEq, Repr

structure Receipt where
  task : Task
  runId : Nat
  signatureAuthorized : Bool
  roleAuthorized : Bool
  executionVerified : Bool
  markerPresent : Bool
  noException : Bool
  deriving Repr

structure Ledger where
  pending : List Task
  creditedTasks : List Nat
  creditedRuns : List Nat
  deriving Repr

def IssueOK (s : Ledger) (t : Task) : Prop :=
  t.id ∉ s.creditedTasks ∧
    ∀ p ∈ s.pending, p.id ≠ t.id

def ReceiptOK (s : Ledger) (r : Receipt) : Prop :=
  r.task ∈ s.pending ∧
  r.task.id ∉ s.creditedTasks ∧
  r.runId ∉ s.creditedRuns ∧
  r.signatureAuthorized = true ∧
  r.roleAuthorized = true ∧
  r.executionVerified = true ∧
  r.markerPresent = true ∧
  r.noException = true

def issue (s : Ledger) (t : Task) : Ledger :=
  { s with pending := t :: s.pending }

def credit (s : Ledger) (r : Receipt) : Ledger :=
  { pending := s.pending.filter (fun t => t ≠ r.task)
    creditedTasks := r.task.id :: s.creditedTasks
    creditedRuns := r.runId :: s.creditedRuns }

/-- The two transition constructors keep issuance and credit distinct.
The only way to credit is a genuine ReceiptOK witness. -/
inductive Step : Ledger → Ledger → Prop
  | issued (s : Ledger) (t : Task) :
      IssueOK s t → Step s (issue s t)
  | credited (s : Ledger) (r : Receipt) :
      ReceiptOK s r → Step s (credit s r)

def WellFormed (s : Ledger) : Prop :=
  s.creditedTasks.Nodup ∧ s.creditedRuns.Nodup

theorem no_credit_without_issue (s : Ledger) (r : Receipt)
    (h : s.pending = []) : ¬ ReceiptOK s r := by
  intro hr
  have hm : r.task ∈ s.pending := hr.1
  simpa [h] using hm

theorem credit_requires_unconsumed_task_and_run
    (s : Ledger) (r : Receipt) (h : ReceiptOK s r) :
    r.task ∈ s.pending ∧
      r.task.id ∉ s.creditedTasks ∧ r.runId ∉ s.creditedRuns :=
  ⟨h.1, h.2.1, h.2.2.1⟩

theorem credit_requires_external_validation
    (s : Ledger) (r : Receipt) (h : ReceiptOK s r) :
    r.signatureAuthorized = true ∧
      r.roleAuthorized = true ∧
      r.executionVerified = true ∧
      r.markerPresent = true ∧
      r.noException = true :=
  ⟨h.2.2.2.1, h.2.2.2.2.1, h.2.2.2.2.2.1,
   h.2.2.2.2.2.2.1, h.2.2.2.2.2.2.2⟩

/-- One admissible step preserves the no-double-credit accounting invariant. -/
theorem wellFormed_step {s t : Ledger}
    (h : Step s t) (hs : WellFormed s) : WellFormed t := by
  cases h with
  | issued s task hi =>
      simpa [WellFormed, issue] using hs
  | credited s r hr =>
      have ht : r.task.id ∉ s.creditedTasks := hr.2.1
      have hu : r.runId ∉ s.creditedRuns := hr.2.2.1
      constructor
      · change (r.task.id :: s.creditedTasks).Nodup
        exact List.nodup_cons.mpr ⟨ht, hs.1⟩
      · change (r.runId :: s.creditedRuns).Nodup
        exact List.nodup_cons.mpr ⟨hu, hs.2⟩

/-- Arbitrarily many allowed issue/credit steps. -/
inductive Reach : Ledger → Ledger → Prop
  | refl (s : Ledger) : Reach s s
  | step {s t u : Ledger} : Step s t → Reach t u → Reach s u

/-- Core multi-step replay safety theorem. No universal claim about the
truth of an externally signed statement is embedded in this result. -/
theorem wellFormed_reachable {s t : Ledger}
    (h : Reach s t) (hs : WellFormed s) : WellFormed t := by
  induction h with
  | refl _ => exact hs
  | step hst htu ih =>
      exact ih (wellFormed_step hst hs)

theorem empty_ledger_wellFormed :
    WellFormed { pending := [], creditedTasks := [], creditedRuns := [] } := by
  simp [WellFormed]

/-- A deliberately invalid claim is NOT asserted: a successful CI status
without a task in pending cannot produce a valid credit. -/
theorem success_flag_alone_not_enough (r : Receipt)
    (h : r.executionVerified = true) :
    ¬ ReceiptOK { pending := [], creditedTasks := [], creditedRuns := [] } r := by
  exact no_credit_without_issue _ _ rfl

end TenthDiscriminant.Phase371

#print axioms TenthDiscriminant.Phase371.wellFormed_reachable
#print axioms TenthDiscriminant.Phase371.success_flag_alone_not_enough
