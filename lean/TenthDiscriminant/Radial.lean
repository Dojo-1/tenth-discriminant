import Mathlib

/-!
# The scalar core of ledger/radial_bounds.txt
Actual finite weighted moments are used, not a supplied correlation conclusion.
The bridge from derivative rows to these moments and the full Fischer product
are NOT asserted here.
-/
namespace TenthDiscriminant
open Finset

/-- Unnormalized Kantorovich-type bound for multipliers in [a,4a]. -/
theorem weighted_correlation_bound {ι : Type*} (s : Finset ι) (w x : ι → ℝ) (a : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hl : ∀ i ∈ s, a ≤ x i)
    (hu : ∀ i ∈ s, x i ≤ 4*a) :
    16 * ((∑ i ∈ s, w i) * (∑ i ∈ s, w i * (x i)^2)) ≤
      25 * (∑ i ∈ s, w i * x i)^2 := by
  have hpoint : ∀ i ∈ s, w i * (x i)^2 ≤ 5*a*(w i*x i) - 4*a^2*w i := by
    intro i hi
    have hq : 0 ≤ (x i-a)*(4*a-x i) :=
      mul_nonneg (sub_nonneg.mpr (hl i hi)) (sub_nonneg.mpr (hu i hi))
    have hp := mul_nonneg (hw i hi) hq
    nlinarith
  have hs := sum_le_sum hpoint
  rw [sum_sub_distrib, ← mul_sum, ← mul_sum] at hs
  have hW : 0 ≤ ∑ i ∈ s, w i := sum_nonneg hw
  have hm := mul_le_mul_of_nonneg_left hs hW
  nlinarith [sq_nonneg (5*(∑ i ∈ s, w i*x i) - 8*a*(∑ i ∈ s, w i))]

/-- The 9/25 bound for the exact two-row weighted Gram determinant. -/
theorem weighted_block_bound {ι : Type*} (s : Finset ι) (w x : ι → ℝ) (a : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hl : ∀ i ∈ s, a ≤ x i)
    (hu : ∀ i ∈ s, x i ≤ 4*a) :
    (∑ i ∈ s, w i) * (∑ i ∈ s, w i*(x i)^2) - (∑ i ∈ s, w i*x i)^2 ≤
      (9/25 : ℝ) * ((∑ i ∈ s, w i) * (∑ i ∈ s, w i*(x i)^2)) := by
  have h := weighted_correlation_bound s w x a hw hl hu
  nlinarith

/-- Exact denominator condition for the derivative multiplier, including J=1. -/
theorem derivative_multiplier_bound (r J : ℕ) (hJ : 1 ≤ J) (hr : 2*(J-1) ≤ r) :
    0 < (r : ℝ) + 2 - J ∧ ((r : ℝ)+1)/((r : ℝ)+2-J) ≤ 2 := by
  have hn : J ≤ r + 1 ∧ r + 1 ≤ 2*(r+2-J) := by omega
  have hrJ : (J : ℝ) ≤ (r : ℝ)+1 := by exact_mod_cast hn.1
  have htwo : 2*(J : ℝ) ≤ (r : ℝ)+3 := by
    have : 2*J ≤ r+3 := by omega
    exact_mod_cast this
  constructor
  · linarith
  · apply (div_le_iff₀ (by linarith : 0 < (r : ℝ)+2-J)).2
    linarith

/-- The guaranteed m-pair gain has the stated 1/R ceiling. -/
theorem normalized_pair_gain (R S m c : ℝ) (hR : 0 < R) (hS : 0 < S)
    (hc : 0 ≤ c) (hm : 2*m ≤ R*S) :
    m*c/(R^2*S) ≤ c/(2*R) := by
  apply (div_le_div_iff₀ (by positivity : 0 < R^2*S) (by positivity : 0 < 2*R)).2
  calc
    m*c*(2*R) = (2*m)*(c*R) := by ring
    _ ≤ (R*S)*(c*R) := mul_le_mul_of_nonneg_right hm (mul_nonneg hc (le_of_lt hR))
    _ = c*(R^2*S) := by ring

end TenthDiscriminant
