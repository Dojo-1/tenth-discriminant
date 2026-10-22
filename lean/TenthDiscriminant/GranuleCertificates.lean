import Mathlib

/-!
# Exact contracts for soft granule weights

Weights may come from fuzzy memberships or empirical operational models.
No weight is evidence that an input bound is valid. Bounds must refer to the
same scalar, and every positive-weight input needs its own valid inequality.
These generic inequalities do not certify any Ender bound or Python program.
-/
namespace TenthDiscriminant
open scoped BigOperators
noncomputable section

/-- A convex combination of valid, active lower bounds is a lower bound. -/
theorem granule_weighted_lower {i : Type*} [Fintype i]
    (w lower : i -> Real) (target : Real)
    (hw : forall k, 0 <= w k) (hs : (Finset.univ.sum w) = 1)
    (hvalid : forall k, w k ≠ 0 -> lower k <= target) :
    (Finset.univ.sum (fun k => w k * lower k)) <= target := by
  classical
  calc
    _ <= Finset.univ.sum (fun k => w k * target) := by
      apply Finset.sum_le_sum
      intro k hk
      by_cases hz : w k = 0
      · simp [hz]
      · exact mul_le_mul_of_nonneg_left (hvalid k hz) (hw k)
    _ = target := by rw [← Finset.sum_mul, hs, one_mul]

/-- The analogous upper-bound contract. -/
theorem granule_weighted_upper {i : Type*} [Fintype i]
    (w upper : i -> Real) (target : Real)
    (hw : forall k, 0 <= w k) (hs : (Finset.univ.sum w) = 1)
    (hvalid : forall k, w k ≠ 0 -> target <= upper k) :
    target <= Finset.univ.sum (fun k => w k * upper k) := by
  classical
  calc
    target = Finset.univ.sum (fun k => w k * target) := by
      rw [← Finset.sum_mul, hs, one_mul]
    _ <= _ := by
      apply Finset.sum_le_sum
      intro k hk
      by_cases hz : w k = 0
      · simp [hz]
      · exact mul_le_mul_of_nonneg_left (hvalid k hz) (hw k)

/-- Positivity needs valid premises, not confidence in those premises. -/
theorem granule_positive_of_blend {i : Type*} [Fintype i]
    (w lower : i -> Real) (target : Real)
    (hw : forall k, 0 <= w k) (hs : (Finset.univ.sum w) = 1)
    (hvalid : forall k, w k ≠ 0 -> lower k <= target)
    (hpos : 0 < Finset.univ.sum (fun k => w k * lower k)) : 0 < target :=
  lt_of_lt_of_le hpos (granule_weighted_lower w lower target hw hs hvalid)

/-- A blend cannot exceed any upper bound on all its active component bounds. -/
theorem granule_blend_le_best {i : Type*} [Fintype i]
    (w lower : i -> Real) (best : Real)
    (hw : forall k, 0 <= w k) (hs : (Finset.univ.sum w) = 1)
    (hbest : forall k, w k ≠ 0 -> lower k <= best) :
    Finset.univ.sum (fun k => w k * lower k) <= best :=
  granule_weighted_lower w lower best hw hs hbest

/-- A unit-mass nonnegative family cannot have an uncovered point. -/
theorem granule_active_exists {i : Type*} [Fintype i]
    (w : i -> Real) (hw : forall k, 0 <= w k)
    (hs : Finset.univ.sum w = 1) : Exists (fun k => 0 < w k) := by
  classical
  by_contra hn
  push_neg at hn
  have hz : forall k, w k = 0 := fun k => le_antisymm (hn k) (hw k)
  have hzero : Finset.univ.sum w = 0 := Finset.sum_eq_zero (fun k hk => hz k)
  linarith

/-- Normalizing memberships is algebra, not probabilistic calibration. -/
theorem granule_normalized_sum {i : Type*} [Fintype i]
    (mu : i -> Real) (hne : Finset.univ.sum mu ≠ 0) :
    Finset.univ.sum (fun k => mu k / Finset.univ.sum mu) = 1 := by
  simp only [div_eq_mul_inv, ← Finset.sum_mul]
  exact mul_inv_cancel₀ hne

/-- Positive best lower bound can be lost by averaging valid weaker bounds. -/
theorem granule_averaging_can_lose_positivity :
    (1/2 : Real) * (-2) + (1/2 : Real) * 1 <= 0 ∧ (0 : Real) < 1 := by
  norm_num

/-- Normalization alone is insufficient: negative weights can overshoot. -/
theorem granule_negative_weight_counterexample :
    (-1 : Real) + 2 = 1 ∧ (1 : Real) < (-1 : Real) * 0 + 2 * 1 := by
  norm_num

end
end TenthDiscriminant
