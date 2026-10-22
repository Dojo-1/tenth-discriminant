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
  let F : Polynomial (Polynomial Rat) := Polynomial.X^2 - Polynomial.C Polynomial.X
  change (fixedSylvesterMatrix F F.derivative 3 2).det = 0
  have hF : F.natDegree <= 2 := by
    dsimp only [F]
    exact (Polynomial.natDegree_sub_le _ _).trans (by norm_num)
  have hG : F.derivative.natDegree <= 1 :=
    (Polynomial.natDegree_derivative_le F).trans (Nat.sub_le_sub_right hF 1)
  apply Matrix.det_eq_zero_of_row_eq_zero (4 : Fin 5)
  intro j
  change (fixedSylvesterColumns F F.derivative 3 2 j).coeff 4 = 0
  apply Polynomial.coeff_eq_zero_of_natDegree_lt
  unfold fixedSylvesterColumns
  split_ifs with hj
  · have hd : (Polynomial.X^j.val * F).natDegree <=
        (Polynomial.X^j.val : Polynomial (Polynomial Rat)).natDegree + F.natDegree :=
      Polynomial.natDegree_mul_le
    have hx : (Polynomial.X^j.val : Polynomial (Polynomial Rat)).natDegree <= j.val := by simp
    omega
  · have hd : (Polynomial.X^(j.val-2) * F.derivative).natDegree <=
        (Polynomial.X^(j.val-2) : Polynomial (Polynomial Rat)).natDegree + F.derivative.natDegree :=
      Polynomial.natDegree_mul_le
    have hx : (Polynomial.X^(j.val-2) : Polynomial (Polynomial Rat)).natDegree <= j.val-2 := by simp
    have hj5 := j.isLt
    omega

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
    Polynomial.derivative_mul, Polynomial.coeff_X, Polynomial.coeff_one,
    Polynomial.coeff_C, mul_add, add_mul] <;> ring

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
    Polynomial.derivative_mul, Polynomial.coeff_X, Polynomial.coeff_one,
    Polynomial.coeff_C, mul_sub, sub_mul] <;> ring

/-- For odd block sizes, the chosen coefficient-map sign differs from the usual resultant. -/
theorem comparatorR1_odd_block_sign :
    let F : Polynomial (Polynomial Rat) := Polynomial.X + Polynomial.C Polynomial.X
    let G : Polynomial (Polynomial Rat) := Polynomial.X + 1
    (fixedSylvesterMatrix F G 1 1).det = Polynomial.X - 1 := by
  dsimp only
  unfold fixedSylvesterMatrix polynomialCoefficientMatrix
  rw [Matrix.det_fin_two]
  norm_num [fixedSylvesterColumns, Polynomial.coeff_X, Polynomial.coeff_one,
    Polynomial.coeff_C]

/-- Taylor coefficient, not just its determinant, at a negative center. -/
theorem comparatorR1_taylor_negative :
    taylorCoefficientMatrix 3 (-1 : Rat) 1 2 = -2 := by
  norm_num [taylorCoefficientMatrix, pow_two, mul_add, add_mul,
    Polynomial.coeff_X, Polynomial.coeff_one, Polynomial.coeff_C]

/-- A rational center prevents accidental reliance on integer-only arithmetic. -/
theorem comparatorR1_taylor_rational :
    taylorCoefficientMatrix 3 (1/2 : Rat) 0 2 = 1/4 := by
  norm_num [taylorCoefficientMatrix, pow_two, mul_add, add_mul,
    Polynomial.coeff_X, Polynomial.coeff_one, Polynomial.coeff_C]

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
  have h3 : (3 : ZMod 3) = 0 := by decide
  have hp3 : (3 : Polynomial (ZMod 3)) = 0 := by
    calc
      (3 : Polynomial (ZMod 3)) = Polynomial.C (3 : ZMod 3) :=
        (map_natCast (Polynomial.C : ZMod 3 →+* Polynomial (ZMod 3)) 3).symm
      _ = 0 := by rw [h3, map_zero]
  simp [Polynomial.derivative_X_pow, hp3]

end
end TenthDiscriminant
