import TenthDiscriminant.BinaryNullBasisMatrix
import TenthDiscriminant.BinaryNullHorizontalBasisMatrix

/-!
# Phase323: composed vertical/horizontal binary change of basis

The two maps are integer matrices on THE SAME original monomial
rectangle. Their product is unimodular because each factor is.
This does NOT yet show that the composed original ordinary jet has
the sum of the two powers of two; the source row action is a
separate, required theorem.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Vertical Z-null basis followed by horizontal W-null basis. -/
def binaryNullBidirectionalBasisMatrix (R S : Nat) :
    Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  binaryNullBasisMatrix R S * binaryNullHorizontalBasisMatrix R S

/-- A genuine integral unimodular transformation, without determinant
or source substitutions. -/
theorem binaryNullBidirectionalBasisMatrix_det (R S : Nat) :
    (binaryNullBidirectionalBasisMatrix R S).det = 1 := by
  unfold binaryNullBidirectionalBasisMatrix
  rw [Matrix.det_mul, binaryNullBasisMatrix_det,
    binaryNullHorizontalBasisMatrix_det]
  norm_num

/-- The target joint row exponent, not yet a proved jet factor. -/
def binaryNullBidirectionalExponent (R S : Nat) (i : Fin (R*S)) : Nat :=
  binaryNullBasisExponent R S i + binaryNullHorizontalExponent R S i

/-- This identity counts each row exactly once. It is not a
determinant valuation until the joint jet theorem is established. -/
theorem binaryNullBidirectionalExponent_sum (R S : Nat) :
    (∑ i : Fin (R*S), binaryNullBidirectionalExponent R S i) =
      (∑ i : Fin (R*S), binaryNullBasisExponent R S i) +
      (∑ i : Fin (R*S), binaryNullHorizontalExponent R S i) := by
  simp [binaryNullBidirectionalExponent, Finset.sum_add_distrib]

end TenthDiscriminant

#print axioms TenthDiscriminant.binaryNullBidirectionalBasisMatrix_det
