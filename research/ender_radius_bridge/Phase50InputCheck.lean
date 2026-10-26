import TenthDiscriminant

#check @TenthDiscriminant.rectangularBasisMatrix_eq_zero_of_parity_ne
#check @TenthDiscriminant.rectangularBasisMatrix_commutes_sign
#check @TenthDiscriminant.integerRectangularTraceGram_commutes_sign
#check @TenthDiscriminant.oddness_required_parity_control
#print axioms TenthDiscriminant.rectangularBasisMatrix_eq_zero_of_parity_ne
#print axioms TenthDiscriminant.rectangularBasisMatrix_commutes_sign
#print axioms TenthDiscriminant.integerRectangularTraceGram_commutes_sign
#print axioms TenthDiscriminant.oddness_required_parity_control

open TenthDiscriminant
example : rectangularBasisMatrix 4 2 3 * rectangularSignMatrix 4 2 =
    rectangularSignMatrix 4 2 * rectangularBasisMatrix 4 2 3 :=
  rectangularBasisMatrix_commutes_sign 4 2 3 (by decide) (by decide)

example : integerRectangularTraceGram (ellipsePairs 19 5) 19 7 4 2 *
    rectangularSignMatrix 4 2 = rectangularSignMatrix 4 2 *
      integerRectangularTraceGram (ellipsePairs 19 5) 19 7 4 2 :=
  integerRectangularTraceGram_commutes_sign _ _ _ _ _
    (ellipsePairs_central_symmetry 19 5 (by decide))

example : rectangularBasisMatrix 3 2 2 4 1 ≠ 0 := by
  rw [oddness_required_parity_control.1]
  norm_num
