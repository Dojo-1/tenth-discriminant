import Mathlib

/-!
# Fixed-size determinant multiplicity via Taylor coordinates

A root-multiplicity hypothesis on every specialized column is transported
through a determinant-one Taylor matrix. Whole rows then contain X - C w.
No rank-normal-form assumption, nonzero leading coefficient at specialization,
or global jet-uniqueness premise is used. Z is the outer polynomial variable;
W is the coefficient-ring variable. Compilation is checked by repository CI.
-/
namespace TenthDiscriminant
open Matrix Polynomial
noncomputable section

variable {K : Type*} [Field K]

/-- Extract one divisor from each row; no nonsingularity hypothesis. -/
theorem row_divisors_dvd_det {n : Type*} [Fintype n] [DecidableEq n]
    {R : Type*} [CommRing R] (A : Matrix n n R) (d : n -> R)
    (h : forall i j, d i ∣ A i j) : (Finset.univ.prod d) ∣ A.det := by
  classical
  choose B hB using h
  have hA : A = Matrix.of (fun i j => d i * B i j) := by
    ext i j
    exact hB i j
  rw [hA, Matrix.det_mul_column]
  exact dvd_mul_right _ _

/-- Vanishing selected rows supply at least their cardinality in multiplicity. -/
theorem polynomial_rows_vanish_pow_dvd_det {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n (Polynomial K)) (w : K) (s : Finset n)
    (h : forall i ∈ s, forall j, (A i j).eval w = 0) :
    (Polynomial.X - Polynomial.C w)^s.card ∣ A.det := by
  classical
  have hd : forall i j, (if i ∈ s then Polynomial.X - Polynomial.C w else 1) ∣ A i j := by
    intro i j
    by_cases hi : i ∈ s
    · simp only [if_pos hi]
      exact Polynomial.dvd_iff_isRoot.mpr (h i hi j)
    · simp [hi]
  have hh := row_divisors_dvd_det A (fun i => if i ∈ s then Polynomial.X - Polynomial.C w else 1) hd
  simpa using hh

/-- A determinant-one constant row transformation preserves the divisor. -/
theorem constant_row_transform_pow_dvd_det {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n (Polynomial K)) (U : Matrix n n K) (hU : U.det = 1)
    (w : K) (s : Finset n)
    (h : forall i ∈ s, forall j, (U * A.map (Polynomial.evalRingHom w)) i j = 0) :
    (Polynomial.X - Polynomial.C w)^s.card ∣ A.det := by
  classical
  have he : forall i ∈ s, forall j,
      ((U.map Polynomial.C * A) i j).eval w = 0 := by
    intro i hi j
    simpa [Matrix.mul_apply, Matrix.map_apply, Polynomial.eval_finset_sum] using h i hi j
  have hd := polynomial_rows_vanish_pow_dvd_det (U.map Polynomial.C * A) w s he
  have hu : (U.map Polynomial.C).det = 1 := by
    rw [← RingHom.map_det]
    simp [hU]
  simpa [Matrix.det_mul, hu] using hd

/-- The finite coefficient matrix of translation Z -> Z+z. -/
def taylorCoefficientMatrix (n : Nat) (z : K) : Matrix (Fin n) (Fin n) K :=
  Matrix.of (fun i j => ((Polynomial.X + Polynomial.C z)^j.val).coeff i.val)

theorem taylorCoefficientMatrix_det (n : Nat) (z : K) :
    (taylorCoefficientMatrix n z).det = 1 := by
  apply Matrix.det_matrixOfPolynomials
    (fun j : Fin n => (Polynomial.X + Polynomial.C z)^j.val)
  · intro i
    exact Polynomial.natDegree_pow_X_add_C _ _
  · intro i
    exact (Polynomial.monic_X_add_C z).pow i.val

/-- Reconstruct a column in the fixed n-dimensional polynomial space. -/
def finiteColumnPolynomial {n : Nat} (A : Matrix (Fin n) (Fin n) K) (j : Fin n) : Polynomial K :=
  Finset.univ.sum (fun k => Polynomial.C (A k j) * Polynomial.X^k.val)

/-- Taylor change of coefficient coordinates is the actual matrix product. -/
theorem taylorCoefficientMatrix_mul {n : Nat} (z : K)
    (A : Matrix (Fin n) (Fin n) K) (i j : Fin n) :
    (taylorCoefficientMatrix n z * A) i j =
      (Polynomial.taylor z (finiteColumnPolynomial A j)).coeff i.val := by
  classical
  simp [taylorCoefficientMatrix, finiteColumnPolynomial, Matrix.mul_apply,
    Polynomial.taylor_apply, Polynomial.sum_comp, Polynomial.mul_comp,
    Polynomial.pow_comp, Polynomial.coeff_C_mul, mul_comm]

/-- A root of order c has its first c Taylor coefficients zero. -/
theorem taylor_coeff_zero_of_root_power (p : Polynomial K) (z : K) (c i : Nat)
    (hp : (Polynomial.X - Polynomial.C z)^c ∣ p) (hi : i < c) :
    (Polynomial.taylor z p).coeff i = 0 := by
  obtain ⟨q, rfl⟩ := hp
  simp [Polynomial.taylor_apply, Polynomial.mul_comp, Polynomial.pow_comp,
    Polynomial.sub_comp, Polynomial.coeff_X_pow_mul, Nat.not_le_of_lt hi]

/-- Generic fixed-size local multiplicity theorem, with no degree-loss exception. -/
theorem column_root_power_dvd_det {n : Nat}
    (A : Matrix (Fin n) (Fin n) (Polynomial K)) (w z : K) (c : Nat) (hc : c <= n)
    (h : forall j, (Polynomial.X - Polynomial.C z)^c ∣
      finiteColumnPolynomial (A.map (Polynomial.evalRingHom w)) j) :
    (Polynomial.X - Polynomial.C w)^c ∣ A.det := by
  classical
  let e : Fin c ↪ Fin n :=
    ⟨fun i => ⟨i.val, lt_of_lt_of_le i.isLt hc⟩,
      by intro a b hab; apply Fin.ext; exact congrArg Fin.val hab⟩
  let s : Finset (Fin n) := Finset.univ.map e
  have hs : s.card = c := by simp [s]
  rw [← hs]
  apply constant_row_transform_pow_dvd_det A (taylorCoefficientMatrix n z)
    (taylorCoefficientMatrix_det n z) w s
  intro i hi j
  obtain ⟨k, hk, rfl⟩ := Finset.mem_map.mp hi
  rw [taylorCoefficientMatrix_mul]
  exact taylor_coeff_zero_of_root_power _ z c k.val (h j) k.isLt

/-- Columns are polynomials in Z with coefficients polynomial in W. -/
def polynomialCoefficientMatrix {n : Nat} (cols : Fin n -> Polynomial (Polynomial K)) :
    Matrix (Fin n) (Fin n) (Polynomial K) := fun i j => (cols j).coeff i.val

theorem finiteColumnPolynomial_eq_specialization {n : Nat}
    (cols : Fin n -> Polynomial (Polynomial K)) (w : K)
    (hdeg : forall j, (cols j).natDegree < n) (j : Fin n) :
    finiteColumnPolynomial ((polynomialCoefficientMatrix cols).map (Polynomial.evalRingHom w)) j =
      (cols j).map (Polynomial.evalRingHom w) := by
  classical
  have hm := congrArg (Polynomial.map (Polynomial.evalRingHom w))
    ((cols j).as_sum_range' n (hdeg j))
  rw [Polynomial.map_sum] at hm
  simp only [Polynomial.map_monomial] at hm
  rw [finiteColumnPolynomial, Fin.sum_univ_eq_sum_range]
  simpa [polynomialCoefficientMatrix, Matrix.map_apply, Polynomial.C_mul_X_pow_eq_monomial] using hm.symm

/-- Specialized column-root divisibility implies determinant-root divisibility. -/
theorem polynomial_columns_root_power_dvd_det {n : Nat}
    (cols : Fin n -> Polynomial (Polynomial K)) (w z : K) (c : Nat) (hc : c <= n)
    (hdeg : forall j, (cols j).natDegree < n)
    (hroot : forall j, (Polynomial.X - Polynomial.C z)^c ∣
      (cols j).map (Polynomial.evalRingHom w)) :
    (Polynomial.X - Polynomial.C w)^c ∣ (polynomialCoefficientMatrix cols).det := by
  apply column_root_power_dvd_det _ w z c hc
  intro j
  rw [finiteColumnPolynomial_eq_specialization cols w hdeg j]
  exact hroot j

/-- Fixed Sylvester columns: b shifts of F and a shifts of G, even after degree loss. -/
def fixedSylvesterColumns (F G : Polynomial (Polynomial K)) (a b : Nat)
    (j : Fin (a+b)) : Polynomial (Polynomial K) :=
  if j.val < b then Polynomial.X^j.val * F else Polynomial.X^(j.val-b) * G

def fixedSylvesterMatrix (F G : Polynomial (Polynomial K)) (a b : Nat) :
    Matrix (Fin (a+b)) (Fin (a+b)) (Polynomial K) :=
  polynomialCoefficientMatrix (fixedSylvesterColumns F G a b)

theorem fixedSylvesterColumns_degree (F G : Polynomial (Polynomial K)) (a b : Nat)
    (hF : F.natDegree <= a) (hG : G.natDegree <= b) (j : Fin (a+b)) :
    (fixedSylvesterColumns F G a b j).natDegree < a+b := by
  unfold fixedSylvesterColumns
  split_ifs with hj
  · have hd := Polynomial.natDegree_mul_le (Polynomial.X^j.val) F
    have hx : (Polynomial.X^j.val : Polynomial (Polynomial K)).natDegree <= j.val := by simp
    omega
  · have hd := Polynomial.natDegree_mul_le (Polynomial.X^(j.val-b)) G
    have hx : (Polynomial.X^(j.val-b) : Polynomial (Polynomial K)).natDegree <= j.val-b := by simp
    have hlt := j.isLt
    omega

/-- The fixed-size Sylvester determinant pays for common specialized root multiplicity. -/
theorem fixedSylvester_root_power_dvd_det (F G : Polynomial (Polynomial K)) (a b : Nat)
    (hF : F.natDegree <= a) (hG : G.natDegree <= b) (w z : K) (c : Nat) (hc : c <= a+b)
    (hf : (Polynomial.X - Polynomial.C z)^c ∣ F.map (Polynomial.evalRingHom w))
    (hg : (Polynomial.X - Polynomial.C z)^c ∣ G.map (Polynomial.evalRingHom w)) :
    (Polynomial.X - Polynomial.C w)^c ∣ (fixedSylvesterMatrix F G a b).det := by
  apply polynomial_columns_root_power_dvd_det _ w z c hc
    (fixedSylvesterColumns_degree F G a b hF hG)
  intro j
  unfold fixedSylvesterColumns
  split_ifs with hj
  · simpa using dvd_mul_of_dvd_right hf (Polynomial.X^j.val)
  · simpa using dvd_mul_of_dvd_right hg (Polynomial.X^(j.val-b))

/-- Application to F and its Z derivative. The bound m<=a is explicit. -/
theorem fixedDerivativeSylvester_multiplicity (F : Polynomial (Polynomial K)) (a : Nat)
    (hF : F.natDegree <= a) (w z : K) (m : Nat) (hm : m <= a)
    (hroot : (Polynomial.X - Polynomial.C z)^m ∣ F.map (Polynomial.evalRingHom w)) :
    (Polynomial.X - Polynomial.C w)^(m-1) ∣
      (fixedSylvesterMatrix F F.derivative a (a-1)).det := by
  apply fixedSylvester_root_power_dvd_det F F.derivative a (a-1) hF
    ((Polynomial.natDegree_derivative_le F).trans (Nat.sub_le_sub_right hF 1)) w z (m-1)
    (by omega)
  · exact (pow_dvd_pow _ (by omega : m-1 <= m)).trans hroot
  · rw [Polynomial.derivative_map]
    exact Polynomial.pow_sub_one_dvd_derivative_of_pow_dvd hroot

end
end TenthDiscriminant
