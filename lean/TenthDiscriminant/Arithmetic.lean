import Mathlib

/-!
# Arithmetic components of ledger/ender.txt
These declarations do not identify a class group or assert the determinant lemma.
The norm form uses an integer fundamental-discriminant parameter D = 3 mod 4.
-/
namespace TenthDiscriminant
open Finset

/-- Principal form from the repository; its field interpretation is a separate obligation. -/
def principalNorm (D x y : ℤ) : ℤ := x ^ 2 + x * y + ((D + 1) / 4) * y ^ 2

theorem principalNorm_four (D x y : ℤ) (hD : D % 4 = 3) :
    4 * principalNorm D x y = (2 * x + y) ^ 2 + D * y ^ 2 := by
  have h : 4 * ((D + 1) / 4) = D + 1 := by omega
  unfold principalNorm
  calc
    4 * (x ^ 2 + x * y + ((D + 1) / 4) * y ^ 2) =
        (2 * x + y) ^ 2 + (4 * ((D + 1) / 4) - 1) * y ^ 2 := by ring
    _ = (2 * x + y) ^ 2 + D * y ^ 2 := by rw [h]; ring

/-- Every nonrational integral-coordinate principal norm is at least (D+1)/4. -/
theorem principalNorm_lower (D x y : ℤ) (hD : D % 4 = 3)
    (hpos : 0 ≤ D) (hy : y ≠ 0) : (D + 1) / 4 ≤ principalNorm D x y := by
  have hy1 : 1 ≤ y ^ 2 := by
    have : y ≤ -1 ∨ 1 ≤ y := by omega
    rcases this with h | h <;> nlinarith
  have hid := principalNorm_four D x y hD
  have hprod : 0 ≤ D * (y ^ 2 - 1) := mul_nonneg hpos (by omega)
  have hn : D ≤ 4 * principalNorm D x y := by nlinarith [sq_nonneg (2*x+y)]
  omega

theorem small_norm_impossible (D x y p : ℤ) (hD : D % 4 = 3)
    (hpos : 0 ≤ D) (hy : y ≠ 0) (hn : principalNorm D x y = p)
    (hp : p < (D + 1) / 4) : False := by
  have h := principalNorm_lower D x y hD hpos hy
  omega

/-- Ender's strict integer cutoff, without a zero-weight endpoint exception. -/
theorem strict_cutoff (D : ℕ) : 4 * (D / 4) < D + 1 := by omega

theorem interval_strict_cutoff (D₁ D : ℕ) (h : D₁ ≤ D) :
    4 * (D₁ / 4) < D + 1 := by omega

def floorSum (R q : ℕ) : ℕ := ∑ r ∈ range R, r / q

def valuationWeight (R S p : ℕ) : ℕ := ∑ r ∈ range R, ∑ t ∈ range S, min (r / p) t

theorem floorSum_succ (R q : ℕ) : floorSum (R + 1) q = floorSum R q + R / q := by
  simp [floorSum, sum_range_succ]

theorem valuationWeight_eq_zero (R S p : ℕ) (h : R ≤ p) : valuationWeight R S p = 0 := by
  apply sum_eq_zero
  intro r hr
  have hrp : r < p := lt_of_lt_of_le (mem_range.mp hr) h
  simp [Nat.div_eq_of_lt hrp]

/-- Concrete endpoint regression: Q_163(0,1)=41; no inertness is assumed. -/
theorem boundary_norm_163 : principalNorm 163 0 1 = 41 := by decide

theorem cutoff_163 : 4 * (40 : ℕ) < 163 + 1 ∧ ¬ (4 * (41 : ℕ) < 163 + 1) := by decide

theorem endpoint_zero_weight : valuationWeight 41 2 41 = 0 :=
  valuationWeight_eq_zero 41 2 41 le_rfl

set_option maxRecDepth 10000 in
theorem next_endpoint_positive_weight : valuationWeight 42 2 41 = 1 := by decide

/-- Scaled exact identity used when every quotient k is smaller than S. -/
theorem sum_min_identity (S k : ℕ) (hk : k ≤ S) :
    2 * (∑ t ∈ range S, min k t) + k * (k + 1) = 2 * S * k := by
  induction S generalizing k with
  | zero =>
      have : k = 0 := by omega
      subst k
      simp
  | succ S ih =>
      by_cases h : k ≤ S
      · rw [sum_range_succ, min_eq_left h]
        have hi := ih k h
        nlinarith
      · have heq : k = S + 1 := by omega
        subst k
        have hs : (∑ t ∈ range S, min (S + 1) t) = ∑ t ∈ range S, min S t := by
          apply sum_congr rfl
          intro t ht
          have htS : t ≤ S := Nat.le_of_lt (mem_range.mp ht)
          rw [min_eq_right (by omega : t ≤ S + 1), min_eq_right htS]
        rw [sum_range_succ, hs, min_eq_right (Nat.le_succ S)]
        have hi := ih S le_rfl
        nlinarith

end TenthDiscriminant
