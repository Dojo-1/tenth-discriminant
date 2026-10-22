import TenthDiscriminant.SylvesterLocal

/-!
# The coefficient-variable degree of the actual fixed Sylvester determinant

This file proves a degree bound, not nonzero determinant. In particular,
Lean's natDegree of zero is zero; no finite root budget may be inferred
without a separate nonzero-polynomial hypothesis.
-/
namespace TenthDiscriminant
open Polynomial Matrix
open scoped BigOperators
noncomputable section

/-- Each determinant term takes one entry from each column. -/
theorem polynomialMatrix_det_natDegree_le_columns
    {K : Type*} [CommRing K] {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n (Polynomial K)) (d : n -> Nat)
    (h : forall i j, (A i j).natDegree <= d j) :
    A.det.natDegree <= Finset.univ.sum d := by
  rw [Matrix.det_apply]
  apply Polynomial.natDegree_sum_le_of_forall_le
  intro sigma hsigma
  calc
    (Equiv.Perm.sign sigma • Finset.univ.prod (fun i => A (sigma i) i)).natDegree <=
        (Finset.univ.prod (fun i => A (sigma i) i)).natDegree := by
      rcases Int.units_eq_one_or (Equiv.Perm.sign sigma) with hs | hs
      · rw [hs, one_smul]
      · rw [hs, Units.neg_smul, one_smul, Polynomial.natDegree_neg]
    _ <= Finset.univ.sum (fun i => (A (sigma i) i).natDegree) :=
      Polynomial.natDegree_prod_le _ _
    _ <= Finset.univ.sum d := Finset.sum_le_sum (fun i hi => h (sigma i) i)

/-- Uniform entry degree bound, including empty and singular matrices. -/
theorem polynomialMatrix_det_natDegree_le
    {K : Type*} [CommRing K] {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n (Polynomial K)) (b : Nat)
    (h : forall i j, (A i j).natDegree <= b) :
    A.det.natDegree <= Fintype.card n * b := by
  simpa using polynomialMatrix_det_natDegree_le_columns A (fun _ => b) h

variable {K : Type*} [Field K]

/-- Shifting in Z does not increase the W-degree of any coefficient. -/
theorem shifted_coefficient_natDegree_le
    (F : Polynomial (Polynomial K)) (b : Nat)
    (hF : forall i, (F.coeff i).natDegree <= b) (k i : Nat) :
    ((Polynomial.X^k * F).coeff i).natDegree <= b := by
  rw [Polynomial.coeff_X_pow_mul']
  split_ifs
  · exact hF _
  · simp

/-- Ordinary Z differentiation multiplies coefficients by scalar integers. -/
theorem derivative_coefficient_natDegree_le
    (F : Polynomial (Polynomial K)) (b : Nat)
    (hF : forall i, (F.coeff i).natDegree <= b) (i : Nat) :
    (F.derivative.coeff i).natDegree <= b := by
  rw [Polynomial.coeff_derivative]
  calc
    (F.coeff (i+1) * ((i+1 : Nat) : Polynomial K)).natDegree <=
        (F.coeff (i+1)).natDegree + (((i+1 : Nat) : Polynomial K)).natDegree :=
      Polynomial.natDegree_mul_le
    _ <= b + 0 := Nat.add_le_add (hF (i+1)) (by simp)
    _ = b := Nat.add_zero _

/-- Degree control is for the existing matrix, without a new resultant convention. -/
theorem fixedSylvesterMatrix_entry_natDegree_le
    (F G : Polynomial (Polynomial K)) (a c b : Nat)
    (hF : forall i, (F.coeff i).natDegree <= b)
    (hG : forall i, (G.coeff i).natDegree <= b)
    (i j : Fin (a+c)) :
    (fixedSylvesterMatrix F G a c i j).natDegree <= b := by
  change ((fixedSylvesterColumns F G a c j).coeff i.val).natDegree <= b
  unfold fixedSylvesterColumns
  split_ifs
  · exact shifted_coefficient_natDegree_le F b hF _ _
  · exact shifted_coefficient_natDegree_le G b hG _ _

/-- The all-parameter coefficient-degree bound needed by the tangency argument. -/
theorem fixedDerivativeSylvester_natDegree_le
    (F : Polynomial (Polynomial K)) (a b : Nat)
    (hF : forall i, (F.coeff i).natDegree <= b) :
    (fixedSylvesterMatrix F F.derivative a (a-1)).det.natDegree <=
      (a+(a-1))*b := by
  have hg := derivative_coefficient_natDegree_le F b hF
  simpa using polynomialMatrix_det_natDegree_le
    (fixedSylvesterMatrix F F.derivative a (a-1)) b
    (fixedSylvesterMatrix_entry_natDegree_le F F.derivative a (a-1) b hF hg)

/-- The positive-degree spelling uses exactly 2a-1 rows and columns. -/
theorem fixedDerivativeSylvester_natDegree_le_positive
    (F : Polynomial (Polynomial K)) (a b : Nat) (ha : 1 <= a)
    (hF : forall i, (F.coeff i).natDegree <= b) :
    (fixedSylvesterMatrix F F.derivative a (a-1)).det.natDegree <= (2*a-1)*b := by
  have he : a+(a-1) = 2*a-1 := by omega
  simpa only [he] using fixedDerivativeSylvester_natDegree_le F a b hF

/-- The entrywise bound can be sharp; no universal factor 2a-2 is valid. -/
theorem fixedDerivativeSylvester_degree_sharp_control :
    let F : Polynomial (Polynomial Rat) :=
      Polynomial.C Polynomial.X * (Polynomial.X^2 + Polynomial.X + 1)
    (fixedSylvesterMatrix F F.derivative 2 1).det = 3 * Polynomial.X^3 := by
  dsimp only
  unfold fixedSylvesterMatrix polynomialCoefficientMatrix
  rw [Matrix.det_fin_three]
  norm_num [fixedSylvesterColumns, Polynomial.derivative_C_mul,
    Polynomial.derivative_X_sq, Polynomial.coeff_X, Polynomial.coeff_one,
    Polynomial.coeff_C, mul_add, add_mul] <;> ring

end
end TenthDiscriminant
