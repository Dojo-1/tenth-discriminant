import TenthDiscriminant.Phase371CausalReceipt

/-!
# Phase372 — GitHub run family is not an execution identity

The source of the distinction is an actual Phase371 GitHub rerun:
runId 44809412040 was reused, while attempt 1 had jobId 136541801767
and attempt 2 had jobId 136542423196, at a fixed head SHA.

Formal claim: with externally verified issuance time, attempt identity,
head, role and execution booleans, transitions preserve no-double-credit
invariants. External verification and Ed25519 are NOT formalized here.

The field-discriminant source and Phase367 Gram remain unchanged.
-/
namespace TenthDiscriminant.Phase372

set_option autoImplicit false

structure ExecutionKey where
  runId : Nat
  attempt : Nat
  jobId : Nat
  head : Nat
  deriving DecidableEq, Repr

structure IssuedTask where
  task : TenthDiscriminant.Phase371.Task
  issuedAt : Nat
  deriving DecidableEq, Repr

structure AttemptReceipt where
  issued : IssuedTask
  execution : ExecutionKey
  startedAt : Nat
  signatureAuthorized : Bool
  roleAuthorized : Bool
  runSuccess : Bool
  jobSuccess : Bool
  markerPresent : Bool
  noException : Bool
  deriving Repr

structure Ledger where
  pending : List IssuedTask
  creditedTasks : List Nat
  creditedExecutions : List ExecutionKey
  creditedJobs : List Nat
  deriving Repr

def IssueOK (s : Ledger) (t : IssuedTask) : Prop :=
  t.task.id ∉ s.creditedTasks ∧
    ∀ p ∈ s.pending, p.task.id ≠ t.task.id

def ReceiptOK (s : Ledger) (r : AttemptReceipt) : Prop :=
  r.issued ∈ s.pending ∧
  r.issued.task.id ∉ s.creditedTasks ∧
  r.execution ∉ s.creditedExecutions ∧
  r.execution.jobId ∉ s.creditedJobs ∧
  r.execution.head = r.issued.task.repositoryHead ∧
  0 < r.execution.attempt ∧
  r.issued.issuedAt < r.startedAt ∧
  r.signatureAuthorized = true ∧
  r.roleAuthorized = true ∧
  r.runSuccess = true ∧
  r.jobSuccess = true ∧
  r.markerPresent = true ∧
  r.noException = true

def issue (s : Ledger) (t : IssuedTask) : Ledger :=
  { s with pending := t :: s.pending }

def credit (s : Ledger) (r : AttemptReceipt) : Ledger :=
  { pending := s.pending.filter (fun t => t ≠ r.issued)
    creditedTasks := r.issued.task.id :: s.creditedTasks
    creditedExecutions := r.execution :: s.creditedExecutions
    creditedJobs := r.execution.jobId :: s.creditedJobs }

inductive Step : Ledger → Ledger → Prop
  | issued (s : Ledger) (t : IssuedTask) :
      IssueOK s t → Step s (issue s t)
  | credited (s : Ledger) (r : AttemptReceipt) :
      ReceiptOK s r → Step s (credit s r)

def WellFormed (s : Ledger) : Prop :=
  s.creditedTasks.Nodup ∧
  s.creditedExecutions.Nodup ∧
  s.creditedJobs.Nodup

theorem no_credit_without_issue (s : Ledger) (r : AttemptReceipt)
    (h : s.pending = []) : ¬ ReceiptOK s r := by
  intro hr
  have hm : r.issued ∈ s.pending := hr.1
  simpa [h] using hm

theorem no_credit_for_preissuance_execution (s : Ledger) (r : AttemptReceipt)
    (h : r.startedAt ≤ r.issued.issuedAt) : ¬ ReceiptOK s r := by
  intro hr
  simp only [ReceiptOK] at hr
  rcases hr with ⟨_, _, _, _, _, _, htime, _⟩
  omega

theorem no_credit_for_reused_execution (s : Ledger) (r : AttemptReceipt)
    (h : r.execution ∈ s.creditedExecutions) : ¬ ReceiptOK s r := by
  intro hr
  exact hr.2.2.1 h

theorem no_credit_for_reused_job (s : Ledger) (r : AttemptReceipt)
    (h : r.execution.jobId ∈ s.creditedJobs) : ¬ ReceiptOK s r := by
  intro hr
  exact hr.2.2.2.1 h

theorem wellFormed_step {s t : Ledger}
    (h : Step s t) (hs : WellFormed s) : WellFormed t := by
  cases h with
  | issued task hi =>
      simpa [WellFormed, issue] using hs
  | credited r hr =>
      have ht : r.issued.task.id ∉ s.creditedTasks := hr.2.1
      have he : r.execution ∉ s.creditedExecutions := hr.2.2.1
      have hj : r.execution.jobId ∉ s.creditedJobs := hr.2.2.2.1
      rcases hs with ⟨h_tasks, h_execs, h_jobs⟩
      refine ⟨?_, ?_, ?_⟩
      · change (r.issued.task.id :: s.creditedTasks).Nodup
        exact List.nodup_cons.mpr ⟨ht, h_tasks⟩
      · change (r.execution :: s.creditedExecutions).Nodup
        exact List.nodup_cons.mpr ⟨he, h_execs⟩
      · change (r.execution.jobId :: s.creditedJobs).Nodup
        exact List.nodup_cons.mpr ⟨hj, h_jobs⟩

inductive Reach : Ledger → Ledger → Prop
  | refl (s : Ledger) : Reach s s
  | step {s t u : Ledger} : Step s t → Reach t u → Reach s u

theorem wellFormed_reachable {s t : Ledger}
    (h : Reach s t) (hs : WellFormed s) : WellFormed t := by
  induction h with
  | refl _ => exact hs
  | step hst htu ih => exact ih (wellFormed_step hst hs)

/-- Historical pair has one run family, TWO distinct execution identities.
The head is encoded by an inert Nat label here, NOT by formal SHA256. -/
def firstAttempt : ExecutionKey :=
  {runId := 44809412040, attempt := 1, jobId := 136541801767, head := 372}

def secondAttempt : ExecutionKey :=
  {runId := 44809412040, attempt := 2, jobId := 136542423196, head := 372}

theorem same_run_distinct_execution :
    firstAttempt.runId = secondAttempt.runId ∧
    firstAttempt ≠ secondAttempt := by
  decide

theorem empty_ledger_wellFormed :
    WellFormed { pending := [], creditedTasks := [],
                 creditedExecutions := [], creditedJobs := [] } := by
  simp [WellFormed]

end TenthDiscriminant.Phase372

#print axioms TenthDiscriminant.Phase372.wellFormed_reachable
#print axioms TenthDiscriminant.Phase372.same_run_distinct_execution

-- Exact-head CI freeze: the signer and timestamp semantics remain external assumptions.
