import TenthDiscriminant.Radial

/-! The scalar radial inequality as an actual 2-by-2 matrix statement.
The identification with the derivative trace Gram rows remains separate. -/
namespace TenthDiscriminant
open Finset Matrix

noncomputable def weightedMomentMatrix {ι : Type*} (s : Finset ι) (w x : ι → ℝ) :
    Matrix (Fin 2) (Fin 2) ℝ :=
  !![∑ i ∈ s, w i, ∑ i ∈ s, w i*x i;
     ∑ i ∈ s, w i*x i, ∑ i ∈ s, w i*(x i)^2]

theorem momentMatrix_bound {ι : Type*} (s : Finset ι) (w x : ι → ℝ) (a : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hl : ∀ i ∈ s, a ≤ x i)
    (hu : ∀ i ∈ s, x i ≤ 4*a) :
    (weightedMomentMatrix s w x).det ≤
      (9/25 : ℝ) * ((weightedMomentMatrix s w x) 0 0 * (weightedMomentMatrix s w x) 1 1) := by
  simpa [weightedMomentMatrix, Matrix.det_fin_two, pow_two] using weighted_block_bound s w x a hw hl hu

/-- Attainment in the weighted-moment class: weights 4,1 and multipliers 1,4. -/
theorem radial_constant_attained :
    (weightedMomentMatrix (Finset.univ : Finset (Fin 2)) ![4,1] ![1,4]).det =
      (9/25 : ℝ) * (5*20) := by
  norm_num [weightedMomentMatrix, Matrix.det_fin_two, Fin.sum_univ_two]

/-- Dropping the multiplier range invalidates 9/25: weights 99,1; multipliers 1,100. -/
theorem multiplier_range_is_essential :
    (9/25 : ℝ) * (100*10099) <
      (weightedMomentMatrix (Finset.univ : Finset (Fin 2)) ![99,1] ![1,100]).det := by
  norm_num [weightedMomentMatrix, Matrix.det_fin_two, Fin.sum_univ_two]

end TenthDiscriminant
