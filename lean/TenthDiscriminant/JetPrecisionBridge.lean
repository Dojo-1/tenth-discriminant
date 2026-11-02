import TenthDiscriminant.IntegerTraceGram

/-!
The distinction between original ordinary partial-Z jets and integral
Taylor/Hasse coefficients is a load-bearing arithmetic invariant.
This adds no new field bound and does not replace any existing Gram.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Integral Taylor coefficient, before specialization W=conjugate(Z).
This is a diagnostic comparison object, NOT the production ordinary jet. -/
def integerHasseCoefficientRow (D r s j : Nat) (q : Int × Int) : Int × Int :=
  if j <= r then
    pairScale (r.choose j : Int)
      (pairMul D (pairPow D q (r - j)) (pairPow D (pairConj q) s))
  else (0, 0)

/-- The ordinary jet differs by j! over integers. Cancelling j! is legitimate
only if it is a unit in the chosen residue field: q<=j is a nonunit seam. -/
theorem integerDerivativeRow_eq_factorial_hasse (D r s j : Nat)
    (q : Int × Int) :
    integerDerivativeRow D r s j q =
      pairScale (j.factorial : Int) (integerHasseCoefficientRow D r s j q) := by
  by_cases hj : j <= r
  · simp [integerDerivativeRow, integerHasseCoefficientRow, hj, pairScale,
      Nat.descFactorial_eq_factorial_mul_choose, Nat.cast_mul, mul_assoc]
  · simp [integerDerivativeRow, integerHasseCoefficientRow, hj, pairScale]

/-- Ordinary ∂_Z³(Z³)=6 whereas its third Taylor/Hasse coefficient is 1. -/
theorem ordinary_hasse_integer_control :
    integerDerivativeRow 1 3 0 3 (1, 0) = (6, 0) /\
    integerHasseCoefficientRow 1 3 0 3 (1, 0) = (1, 0) := by
  constructor <;> decide

/-- An integral unimodular frame is an admissible determinant-preserving
transport of the exact original ordinary-jet Gram. -/
theorem unimodular_ordinary_jet_gram_det
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (U : Matrix (Fin (R*S)) (Fin (R*S)) Int) (hU : U.det = 1) :
    (U * integerRectangularTraceGram Q D J R S * U.transpose).det =
      (integerRectangularTraceGram Q D J R S).det := by
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose, hU]
  ring

end TenthDiscriminant
