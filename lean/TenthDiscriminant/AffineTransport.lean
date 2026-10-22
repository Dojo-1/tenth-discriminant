import TenthDiscriminant.DeterminantMultiplicity

/-!
# Affine transport for the actual fixed-size Sylvester determinant

Work is isolated from the experimental routers. No nonvanishing conclusion is
assumed, and the fixed matrix dimensions are never recomputed on specialization.
-/
namespace TenthDiscriminant
open Matrix Polynomial
noncomputable section

/-- Coefficient homomorphisms preserve the actual fixed-size matrix. -/
theorem fixedSylvesterMatrix_map {K L : Type*} [Field K] [Field L]
    (F G : Polynomial (Polynomial K)) (a b : Nat)
    (phi : RingHom (Polynomial K) (Polynomial L)) :
    fixedSylvesterMatrix (F.map phi) (G.map phi) a b =
      (fixedSylvesterMatrix F G a b).map phi := by
  ext i j
  simp only [fixedSylvesterMatrix, polynomialCoefficientMatrix, Matrix.map_apply,
    fixedSylvesterColumns]
  split_ifs with h
  · change (Polynomial.X^j.val * F.map phi).coeff i.val =
      phi ((Polynomial.X^j.val * F).coeff i.val)
    rw [show Polynomial.X^j.val * F.map phi =
        (Polynomial.X^j.val * F).map phi by simp, Polynomial.coeff_map]
  · change (Polynomial.X^(j.val-b) * G.map phi).coeff i.val =
      phi ((Polynomial.X^(j.val-b) * G).coeff i.val)
    rw [show Polynomial.X^(j.val-b) * G.map phi =
        (Polynomial.X^(j.val-b) * G).map phi by simp, Polynomial.coeff_map]

/-- Naturality of the derivative determinant for the unchanged size. -/
theorem fixedDerivativeSylvester_map {K L : Type*} [Field K] [Field L]
    (F : Polynomial (Polynomial K)) (a : Nat)
    (phi : RingHom (Polynomial K) (Polynomial L)) :
    (fixedSylvesterMatrix (F.map phi) (F.map phi).derivative a (a-1)).det =
      phi ((fixedSylvesterMatrix F F.derivative a (a-1)).det) := by
  rw [Polynomial.derivative_map, fixedSylvesterMatrix_map]
  exact (RingHom.map_det phi _).symm

/-- Rescaling both polynomial arguments rescales every actual matrix entry. -/
theorem fixedSylvesterMatrix_common_scale {K : Type*} [Field K]
    (F G : Polynomial (Polynomial K)) (a b : Nat) (c : Polynomial K) :
    fixedSylvesterMatrix (Polynomial.C c * F) (Polynomial.C c * G) a b =
      Matrix.of (fun i j => c * fixedSylvesterMatrix F G a b i j) := by
  ext i j
  simp only [fixedSylvesterMatrix, polynomialCoefficientMatrix, fixedSylvesterColumns]
  split_ifs <;> simp [mul_left_comm, Polynomial.coeff_C_mul]

/-- Every column is rescaled, including the derivative columns. -/
theorem fixedDerivativeSylvester_scale {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (a : Nat) (c : Polynomial K) :
    (fixedSylvesterMatrix (Polynomial.C c * F)
      (Polynomial.C c * F).derivative a (a-1)).det =
      c^(a+(a-1)) * (fixedSylvesterMatrix F F.derivative a (a-1)).det := by
  rw [Polynomial.derivative_C_mul, fixedSylvesterMatrix_common_scale,
    Matrix.det_mul_column]
  simp

-- Temporary API probes; removed before the final artifact.
#check Matrix.det_of_upperTriangular
#check Polynomial.coeff_pow
#check Polynomial.coeff_pow_of_natDegree_le
#check Polynomial.compRingHom
#check Fin.sum_univ_add
#check Fin.prod_univ_add
#check Polynomial.as_sum_range'
#check Polynomial.coeff_comp_X_add_C
#check Polynomial.coeff_comp_C_mul_X
#check Polynomial.coeff_X_pow
#check Polynomial.coeff_X_add_C_pow
#check Polynomial.sum_range_C_mul_X_pow
#check Matrix.det_mul_row
#check Matrix.det_mul_column

end
end TenthDiscriminant
