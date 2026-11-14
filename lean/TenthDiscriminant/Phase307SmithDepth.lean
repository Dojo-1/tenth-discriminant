import Mathlib

/-!
Phase307: finite p-adic Smith-depth accounting, isolated from field bounds.
For a finite list of elementary exponents b_i, K(n)=sum_i min(n,b_i).
The increment K(n+1)-K(n) counts exponents strictly above n.
This module does NOT assert that a sampled source has these exponents,
nor derive any class-number-one discriminant bound.
-/

namespace TenthDiscriminant.Phase307

def smithKernelLog (exponents : List ℕ) (n : ℕ) : ℕ :=
  (exponents.map (fun b => min n b)).sum

def smithDepthLayer (exponents : List ℕ) (n : ℕ) : ℕ :=
  (exponents.map (fun b => if n < b then 1 else 0)).sum

theorem min_succ_indicator (n b : ℕ) :
    min (n + 1) b = min n b + (if n < b then 1 else 0) := by
  by_cases h : n < b
  · have h1 : n + 1 ≤ b := by omega
    have h2 : n ≤ b := by omega
    simp [h, min_eq_left h1, min_eq_left h2]
  · have h1 : b ≤ n := by omega
    have h2 : b ≤ n + 1 := by omega
    simp [h, min_eq_right h1, min_eq_right h2]

theorem smithKernelLog_succ
    (exponents : List ℕ) (n : ℕ) :
    smithKernelLog exponents (n + 1) =
      smithKernelLog exponents n + smithDepthLayer exponents n := by
  induction exponents with
  | nil =>
      simp [smithKernelLog, smithDepthLayer]
  | cons b rest ih =>
      simp only [smithKernelLog, smithDepthLayer,
        List.map_cons, List.sum_cons] at ih ⊢
      rw [min_succ_indicator, ih]
      omega

end TenthDiscriminant.Phase307
