import Mathlib

/-! Exact interval stitching. This does not validate any Arb inequality. -/
namespace TenthDiscriminant

/-- Every interval starts at the previous endpoint; no gap or reversed interval is accepted. -/
def checkChain : ℕ → ℕ → List (ℕ × ℕ) → Bool
  | lo, hi, [] => lo == hi
  | lo, hi, (a,b)::rest => (lo == a) && (a ≤ b) && checkChain b hi rest

/-- A successful chain check covers every integer in [lo,hi). -/
theorem checkChain_sound (xs : List (ℕ × ℕ)) (lo hi x : ℕ)
    (hc : checkChain lo hi xs = true) (hlo : lo ≤ x) (hhi : x < hi) :
    ∃ a b, (a,b) ∈ xs ∧ a ≤ x ∧ x ≤ b := by
  induction xs generalizing lo with
  | nil =>
      simp [checkChain] at hc
      omega
  | cons ab xs ih =>
      rcases ab with ⟨a,b⟩
      simp only [checkChain, Bool.and_eq_true, beq_iff_eq, decide_eq_true_eq] at hc
      obtain ⟨⟨heq, hab⟩, htail⟩ := hc
      by_cases hx : x ≤ b
      · exact ⟨a,b,by simp,by omega,hx⟩
      · obtain ⟨c,d,hmem,hc,hd⟩ := ih b htail (by omega)
        exact ⟨c,d,by simp [hmem],hc,hd⟩

/-- An off-by-one gap must not be accepted by the certificate checker. -/
theorem gap_rejected : checkChain 0 4 [(0,2),(3,4)] = false := by decide

theorem reversed_interval_rejected : checkChain 0 4 [(0,3),(3,2),(2,4)] = false := by decide

theorem adjacent_intervals_accepted : checkChain 0 4 [(0,2),(2,4)] = true := by decide

/-- Rank-guard failure for sparse annuli cannot be repaired by changing J alone. -/
theorem rank_guard_impossible (n R S J : ℕ) (hn : n ≤ R+S) :
    ¬ (2*R*S + J*(R+S) < n*J) := by
  have h := Nat.mul_le_mul_right J hn
  nlinarith

end TenthDiscriminant
