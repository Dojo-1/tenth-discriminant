import TenthDiscriminant.AffineCoefficients

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
  apply Matrix.ext
  intro i j
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
  apply Matrix.ext
  intro i j
  simp only [fixedSylvesterMatrix, polynomialCoefficientMatrix, fixedSylvesterColumns]
  simp only [Matrix.of_apply]
  split_ifs with h
  · rw [show Polynomial.X^j.val * (Polynomial.C c * F) =
        Polynomial.C c * (Polynomial.X^j.val * F) by ring, Polynomial.coeff_C_mul]
  · rw [show Polynomial.X^(j.val-b) * (Polynomial.C c * G) =
        Polynomial.C c * (Polynomial.X^(j.val-b) * G) by ring, Polynomial.coeff_C_mul]

/-- Every column is rescaled, including the derivative columns. -/
theorem fixedDerivativeSylvester_scale {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (a : Nat) (c : Polynomial K) :
    (fixedSylvesterMatrix (Polynomial.C c * F)
      (Polynomial.C c * F).derivative a (a-1)).det =
      c^(a+(a-1)) * (fixedSylvesterMatrix F F.derivative a (a-1)).det := by
  rw [Polynomial.derivative_C_mul, fixedSylvesterMatrix_common_scale,
    Matrix.det_mul_column]
  simp

/-- Exact reindexing bridge; the auxiliary matrix is not a substitute witness. -/
theorem fixedSylvester_det_eq {K : Type*} [Field K]
    (F G : Polynomial (Polynomial K)) (a b : Nat) :
    (fixedSylvesterMatrix F G a b).det = (sylvesterCoefficients F G b a).det := by
  let e := finCongr (Nat.add_comm a b)
  have he : fixedSylvesterMatrix F G a b =
      (sylvesterCoefficients F G b a).submatrix e e := by
    apply Matrix.ext
    intro i j
    simp [e, fixedSylvesterMatrix, polynomialCoefficientMatrix, fixedSylvesterColumns,
      sylvesterCoefficients, coefficientMatrix, sylvesterColumns, Matrix.submatrix]
  rw [he, Matrix.det_submatrix_equiv_self]

/-- The derivative contributes an additional slope factor in each of its a columns. -/
theorem fixedDerivativeSylvester_outer_affine {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (hF : F.natDegree <= a) (u h : Polynomial K) (hu : u ≠ 0) :
    (fixedSylvesterMatrix (F.comp (affinePolynomial u h))
      (F.comp (affinePolynomial u h)).derivative a (a-1)).det =
      u^(a*a) * (fixedSylvesterMatrix F F.derivative a (a-1)).det := by
  have hd : (F.comp (affinePolynomial u h)).derivative =
      Polynomial.C u * F.derivative.comp (affinePolynomial u h) := by
    rw [Polynomial.derivative_comp]
    simp [affinePolynomial, Polynomial.derivative_C_mul]
  rw [hd]
  simp_rw [fixedSylvester_det_eq]
  rw [sylvesterCoefficients_scale_right]
  rw [sylvesterCoefficients_affine F F.derivative (a-1) a hF
    ((Polynomial.natDegree_derivative_le F).trans (Nat.sub_le_sub_right hF 1)) u h hu]
  have he : a + (a-1)*a = a*a := by
    calc
      a + (a-1)*a = ((a-1)+1)*a := by ring
      _ = a*a := by rw [Nat.sub_add_cancel ha]
  rw [← mul_assoc, ← pow_add, he]

/-- The original fixed-size determinant, with a short name for the public API. -/
def fixedDerivativeDeterminant {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (a : Nat) : Polynomial K :=
  (fixedSylvesterMatrix F F.derivative a (a-1)).det

/-- Inner-variable affine substitution as a coefficient-ring homomorphism. -/
def parameterAffineHom {K : Type*} [Field K] (v b : K) :
    RingHom (Polynomial K) (Polynomial K) := Polynomial.compRingHom (affinePolynomial v b)

/-- lambda F(u Z+h, v W+b); all parameters live in the declared field. -/
def affineTransportPolynomial {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (lam u h v b : K) : Polynomial (Polynomial K) :=
  Polynomial.C (Polynomial.C lam) *
    ((F.map (parameterAffineHom v b)).comp
      (affinePolynomial (Polynomial.C u) (Polynomial.C h)))

/-- Full affine law for the actual fixed matrix, at the exact positive global degree. -/
theorem fixedDerivativeDeterminant_affine {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a) (hF : F.natDegree = a)
    (lam u h v b : K) (hu : u ≠ 0) :
    fixedDerivativeDeterminant (affineTransportPolynomial F lam u h v b) a =
      Polynomial.C (lam^(2*a-1) * u^(a*a)) *
        (fixedDerivativeDeterminant F a).comp (affinePolynomial v b) := by
  unfold affineTransportPolynomial fixedDerivativeDeterminant
  rw [fixedDerivativeSylvester_scale]
  rw [fixedDerivativeSylvester_outer_affine _ a ha
    (Polynomial.natDegree_map_le.trans hF.le) _ _ (by simpa)]
  rw [fixedDerivativeSylvester_map]
  have hn : a+(a-1) = 2*a-1 := by omega
  simp only [hn]
  change (Polynomial.C lam)^(2*a-1) * ((Polynomial.C u)^(a*a) *
    (fixedSylvesterMatrix F F.derivative a (a-1)).det.comp (affinePolynomial v b)) = _
  rw [← Polynomial.C_pow, ← Polynomial.C_pow, ← mul_assoc, ← Polynomial.C_mul]

/-- Transport an exact evaluation to the inverse affine parameter point. -/
theorem affineTransport_witness_value {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a) (hF : F.natDegree = a)
    (lam u h v b t d : K) (hu : u ≠ 0) (hv : v ≠ 0)
    (hd : (fixedDerivativeDeterminant F a).eval t = d) :
    (fixedDerivativeDeterminant (affineTransportPolynomial F lam u h v b) a).eval
      ((t-b)/v) = lam^(2*a-1) * u^(a*a) * d := by
  rw [fixedDerivativeDeterminant_affine F a ha hF lam u h v b hu]
  rw [Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_comp]
  have ht : (affinePolynomial v b).eval ((t-b)/v) = t := by
    simp only [affinePolynomial, Polynomial.eval_add, Polynomial.eval_mul,
      Polynomial.eval_C, Polynomial.eval_X]
    field_simp [hv] <;> ring
  rw [ht, hd]

/-- A nonzero witness remains nonzero under nondegenerate frame transport. -/
theorem affineTransport_witness_nonzero {K : Type*} [Field K]
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a) (hF : F.natDegree = a)
    (lam u h v b t d : K) (hlam : lam ≠ 0) (hu : u ≠ 0) (hv : v ≠ 0)
    (hd : (fixedDerivativeDeterminant F a).eval t = d) (hd0 : d ≠ 0) :
    (fixedDerivativeDeterminant (affineTransportPolynomial F lam u h v b) a).eval
      ((t-b)/v) ≠ 0 := by
  rw [affineTransport_witness_value F a ha hF lam u h v b t d hu hv hd]
  exact mul_ne_zero (mul_ne_zero (pow_ne_zero _ hlam) (pow_ne_zero _ hu)) hd0

end
end TenthDiscriminant
