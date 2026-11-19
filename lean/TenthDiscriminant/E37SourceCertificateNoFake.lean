import TenthDiscriminant.E36UnimodularMovingRowFrame
import TenthDiscriminant.GramDivisibility

/-!
# E37 — The same-source certificate exists here and cannot exist there

This is a SOURCE-SPECIFIC application of GramDivisibility, whose
general n-row integral factor theorem already existed in this repo.
It is not a new proof of that abstract theorem.

For the original shifted source Q={(1,0),(6,0)}, the actual original
ordinary-jet Gram has a valid det-one integer moving frame and
an actual integer two-sided factorization at 5.

For the original E31 unit source Q={(0,0),(1,0)}, NO det-one
integer frame with ANY integer middle matrix can produce the
same 5-scaled factorization. The obstruction is the exact
original determinant 4, not a heuristic conductor kernel.

The fake nonunimodular frame does yield the same terminal matrix,
but fails the hypothesis, demonstrating why transport provenance
is essential. Nothing here improves the 307^4 field bound.
-/

namespace TenthDiscriminant.E37
set_option autoImplicit false
noncomputable section

def primeFiveRowWeights : Fin 2 → Int :=
  pivotScale (1 : Fin 2) 5

def integerMiddle : Matrix (Fin 2) (Fin 2) Int :=
  !![4,2;2,2]

theorem weights_product_five :
    (∏ i : Fin 2, primeFiveRowWeights i) = 5 := by
  decide

/-- A REAL factorization of the ORIGINAL shifted-source Gram.
There is no replacement of Q or of the positive trace. -/
theorem shifted_source_has_integral_factor :
    E36.integerMovingRowFrame *
      integerRectangularTraceGram E36.shiftedRealSource 25 1 2 1 *
      E36.integerMovingRowFrame.transpose =
    Matrix.diagonal primeFiveRowWeights *
      integerMiddle * Matrix.diagonal primeFiveRowWeights := by
  rw [E36.moved_same_original_gram_equals_positive_control,
    E34.original_five_gram_matrix]
  decide

/-- Recover the original determinant's 25 factor using the PREEXISTING
general n-row theorem, not by merely computing det=100. -/
theorem shifted_source_factor_via_generic_gram_theorem :
    (5 : Int)^2 ∣
      (integerRectangularTraceGram E36.shiftedRealSource 25 1 2 1).det := by
  have h := prod_sq_dvd_det_of_unimodular_gram_factor
    (integerRectangularTraceGram E36.shiftedRealSource 25 1 2 1)
    E36.integerMovingRowFrame integerMiddle primeFiveRowWeights
    E36.moving_row_frame_unimodular
    shifted_source_has_integral_factor
  rw [weights_product_five] at h
  exact h

/-- Negative theorem QUANTIFIES OVER ALL det-one integral row frames
and ALL integral middle matrices, rather than testing one proposed U. -/
theorem unit_source_has_no_unimodular_five_factor :
    ¬ ∃ (U K : Matrix (Fin 2) (Fin 2) Int),
      U.det = 1 ∧
      U * integerRectangularTraceGram E31.realSource 25 1 2 1 *
        U.transpose =
        Matrix.diagonal primeFiveRowWeights * K *
        Matrix.diagonal primeFiveRowWeights := by
  rintro ⟨U,K,hU,hfactor⟩
  have h := prod_sq_dvd_det_of_unimodular_gram_factor
    (integerRectangularTraceGram E31.realSource 25 1 2 1)
    U K primeFiveRowWeights hU hfactor
  rw [weights_product_five] at h
  rw [E31.actual_original_gram_det_four] at h
  norm_num at h

/-- The existing fake terminal Gram equality is no counterexample:
the fabricated scaler has determinant 5, not 1. -/
theorem fake_transport_not_an_admissible_witness :
    E36.fakeRowScaler.det ≠ (1 : Int) ∧
    (E36.fakeRowScaler *
      integerRectangularTraceGram E31.realSource 25 1 2 1 *
      E36.fakeRowScaler.transpose =
      Matrix.diagonal primeFiveRowWeights *
        integerMiddle * Matrix.diagonal primeFiveRowWeights) := by
  constructor
  · rw [E36.fakeRowScaler_not_unimodular]
    decide
  · rw [E36.fake_scaling_same_terminal_gram,
        E34.original_five_gram_matrix]
    decide

end
end TenthDiscriminant.E37

#print axioms TenthDiscriminant.E37.shifted_source_has_integral_factor
#print axioms TenthDiscriminant.E37.shifted_source_factor_via_generic_gram_theorem
#print axioms TenthDiscriminant.E37.unit_source_has_no_unimodular_five_factor
#print axioms TenthDiscriminant.E37.fake_transport_not_an_admissible_witness
