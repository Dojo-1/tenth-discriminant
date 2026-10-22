import TenthDiscriminant.SylvesterLocal
import TenthDiscriminant.JetKernel

/-!
# Comparator round 1: boundary and convention controls
Frozen target: 791ebf4815d8eb4be5da3b01527ca7f0877b6d0e.
These are concrete regression statements, not a global nonvanishing theorem.
The reviewer has prior exposure; this is not blind or independent authorship.
-/
namespace TenthDiscriminant
open Polynomial Matrix
noncomputable section

/-- An upper degree bound is insufficient for a NONZERO fixed determinant. -/
theorem comparatorR1_overpadding :
    let F : Polynomial (Polynomial Rat) := Polynomial.X^2 - Polynomial.C Polynomial.X
    (fixedSylvesterMatrix F F.derivative 3 2).det = 0 := by
  dsimp only
  apply Matrix.det_eq_zero_of_row_eq_zero (4 : Fin 5)
  intro j
  fin_cases j <;>
    norm_num [fixedSylvesterMatrix, polynomialCoefficientMatrix,
      fixedSylvesterColumns, Polynomial.derivative_X_sq, mul_sub]

/-- Degree loss retains the original coefficient matrix, rather than a smaller resultant. -/
theorem comparatorR1_degree_drop :
    let F : Polynomial (Polynomial Rat) :=
      Polynomial.C Polynomial.X * Polynomial.X^2 + Polynomial.X + 1
    (fixedSylvesterMatrix F F.derivative 2 1).det =
      4 * Polynomial.X^2 - Polynomial.X := by
  dsimp only
  unfold fixedSylvesterMatrix polynomialCoefficientMatrix
  rw [Matrix.det_fin_three]
  norm_num [fixedSylvesterColumns, Polynomial.derivative_X_sq,
    Polynomial.derivative_mul, mul_add, add_mul] <;> ring

/-- Translated double-root contact has the same local exponent. -/
theorem comparatorR1_translated_quadratic :
    let F : Polynomial (Polynomial Rat) :=
      Polynomial.X^2 - 2 * Polynomial.X + Polynomial.C (3 - Polynomial.X)
    (fixedSylvesterMatrix F F.derivative 2 1).det =
      8 - 4 * Polynomial.X := by
  dsimp only
  unfold fixedSylvesterMatrix polynomialCoefficientMatrix
  rw [Matrix.det_fin_three]
  norm_num [fixedSylvesterColumns, Polynomial.derivative_X_sq,
    Polynomial.derivative_mul, mul_sub, sub_mul] <;> ring

/-- For odd block sizes, the chosen coefficient-map sign differs from the usual resultant. -/
theorem comparatorR1_odd_block_sign :
    let F : Polynomial (Polynomial Rat) := Polynomial.X + Polynomial.C Polynomial.X
    let G : Polynomial (Polynomial Rat) := Polynomial.X + 1
    (fixedSylvesterMatrix F G 1 1).det = Polynomial.X - 1 := by
  dsimp only
  unfold fixedSylvesterMatrix polynomialCoefficientMatrix
  rw [Matrix.det_fin_two]
  norm_num [fixedSylvesterColumns]

/-- Taylor coefficient, not just its determinant, at a negative center. -/
theorem comparatorR1_taylor_negative :
    taylorCoefficientMatrix 3 (-1 : Rat) 1 2 = -2 := by
  norm_num [taylorCoefficientMatrix, pow_two, mul_add, add_mul]

/-- A rational center prevents accidental reliance on integer-only arithmetic. -/
theorem comparatorR1_taylor_rational :
    taylorCoefficientMatrix 3 (1/2 : Rat) 0 2 = 1/4 := by
  norm_num [taylorCoefficientMatrix, pow_two, mul_add, add_mul]

/-- Complex coordinate translation need not preserve a real-coefficient Gram determinant. -/
theorem comparatorR1_complex_translation :
    (traceGramMatrix {0} 1 (fun i : Fin 2 => (i.val,0))).det = 0 := by
  norm_num [Matrix.det_fin_two, traceGramMatrix, traceGramEntry, derivativeRow,
    Finset.sum_range_succ, Nat.descFactorial]

/-- The translated sample has determinant 4; complex and real independence differ. -/
theorem comparatorR1_complex_translation_after :
    (traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det = 4 :=
  traceGramMatrix_real_complex_control

/-- Characteristic-zero is essential to the later derivative-coprimality argument. -/
theorem comparatorR1_characteristic_three :
    (Polynomial.X^3 - Polynomial.C Polynomial.X :
      Polynomial (Polynomial (ZMod 3))).derivative = 0 := by
  norm_num [Polynomial.derivative_X_pow]

end
end TenthDiscriminant
