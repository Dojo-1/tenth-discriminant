import TenthDiscriminant.DeterminantMultiplicity

/-!
# Coefficient and scalar transport of the actual fixed Sylvester matrix

This source is being verified on an isolated review branch. No global
nonvanishing theorem follows from transport alone. The Z-affine theorem in
AffineBasisCertificate retains explicit structural certificate hypotheses.
-/
namespace TenthDiscriminant
open Polynomial Matrix
noncomputable section

variable {K : Type*} [Field K]

/-- Keep the original dimensions even when a coefficient map drops degree. -/
theorem fixedSylvesterMatrix_coeff_map
    (F G : Polynomial (Polynomial K)) (a b : Nat)
    (phi : Polynomial K →+* Polynomial K) :
    fixedSylvesterMatrix (F.map phi) (G.map phi) a b =
      (fixedSylvesterMatrix F G a b).map phi := by
  have hcol (j : Fin (a+b)) :
      fixedSylvesterColumns (F.map phi) (G.map phi) a b j =
        (fixedSylvesterColumns F G a b j).map phi := by
    unfold fixedSylvesterColumns
    split_ifs <;> simp
  ext i j
  change (fixedSylvesterColumns (F.map phi) (G.map phi) a b j).coeff i.val =
    phi ((fixedSylvesterColumns F G a b j).coeff i.val)
  rw [hcol, Polynomial.coeff_map]

/-- Determinant commutes with the same coefficient map, with no rank assumption. -/
theorem fixedSylvesterDet_coeff_map
    (F G : Polynomial (Polynomial K)) (a b : Nat)
    (phi : Polynomial K →+* Polynomial K) :
    (fixedSylvesterMatrix (F.map phi) (G.map phi) a b).det =
      phi (fixedSylvesterMatrix F G a b).det := by
  rw [fixedSylvesterMatrix_coeff_map]
  exact (RingHom.map_det phi (fixedSylvesterMatrix F G a b)).symm

/-- Naming the existing determinant does not introduce a substitute witness. -/
def derivativeSylvesterDet (F : Polynomial (Polynomial K)) (a : Nat) : Polynomial K :=
  (fixedSylvesterMatrix F F.derivative a (a-1)).det

/-- Ordinary Z differentiation commutes with coefficient-ring substitution. -/
theorem derivativeSylvesterDet_coeff_map
    (F : Polynomial (Polynomial K)) (a : Nat)
    (phi : Polynomial K →+* Polynomial K) :
    derivativeSylvesterDet (F.map phi) a = phi (derivativeSylvesterDet F a) := by
  unfold derivativeSylvesterDet
  rw [Polynomial.derivative_map]
  exact fixedSylvesterDet_coeff_map F F.derivative a (a-1) phi

/-- Multiply both input polynomials by the same coefficient-ring element. -/
theorem fixedSylvesterMatrix_common_scale
    (F G : Polynomial (Polynomial K)) (a b : Nat) (c : Polynomial K) :
    fixedSylvesterMatrix (Polynomial.C c * F) (Polynomial.C c * G) a b =
      c • fixedSylvesterMatrix F G a b := by
  ext i j
  simp only [fixedSylvesterMatrix, polynomialCoefficientMatrix, fixedSylvesterColumns,
    Matrix.smul_apply, smul_eq_mul]
  split_ifs <;>
    simp only [mul_left_comm (Polynomial.X^_) (Polynomial.C c), Polynomial.coeff_C_mul]

/-- Zero scales and singular matrices are allowed in this identity. -/
theorem fixedSylvesterDet_common_scale
    (F G : Polynomial (Polynomial K)) (a b : Nat) (c : Polynomial K) :
    (fixedSylvesterMatrix (Polynomial.C c * F) (Polynomial.C c * G) a b).det =
      c^(a+b) * (fixedSylvesterMatrix F G a b).det := by
  rw [fixedSylvesterMatrix_common_scale, Matrix.det_smul]
  simp only [Fintype.card_fin]

theorem derivativeSylvesterDet_common_scale
    (F : Polynomial (Polynomial K)) (a : Nat) (c : Polynomial K) :
    derivativeSylvesterDet (Polynomial.C c * F) a =
      c^(a+(a-1)) * derivativeSylvesterDet F a := by
  unfold derivativeSylvesterDet
  rw [Polynomial.derivative_C_mul]
  exact fixedSylvesterDet_common_scale F F.derivative a (a-1) c

/-- Affine change of W in the coefficient ring; no inverse is needed here. -/
def affineWHom (v b : K) : Polynomial K →+* Polynomial K :=
  Polynomial.eval₂RingHom Polynomial.C
    (Polynomial.C v * Polynomial.X + Polynomial.C b)

@[simp] theorem affineWHom_apply (v b : K) (p : Polynomial K) :
    affineWHom v b p = p.comp (Polynomial.C v * Polynomial.X + Polynomial.C b) := rfl

theorem derivativeSylvesterDet_affineW
    (F : Polynomial (Polynomial K)) (a : Nat) (v b : K) :
    derivativeSylvesterDet (F.map (affineWHom v b)) a =
      (derivativeSylvesterDet F a).comp
        (Polynomial.C v * Polynomial.X + Polynomial.C b) := by
  rw [derivativeSylvesterDet_coeff_map, affineWHom_apply]

theorem derivativeSylvesterDet_affineW_eval
    (F : Polynomial (Polynomial K)) (a : Nat) (v b t : K) :
    (derivativeSylvesterDet (F.map (affineWHom v b)) a).eval t =
      (derivativeSylvesterDet F a).eval (v*t+b) := by
  rw [derivativeSylvesterDet_affineW, Polynomial.eval_comp]
  simp

/-- Combined scalar and W transport, still no Z-affine claim. -/
theorem derivativeSylvesterDet_scalar_affineW_eval
    (F : Polynomial (Polynomial K)) (a : Nat) (l v b t : K) :
    (derivativeSylvesterDet
      (Polynomial.C (Polynomial.C l) * F.map (affineWHom v b)) a).eval t =
      l^(a+(a-1)) * (derivativeSylvesterDet F a).eval (v*t+b) := by
  rw [derivativeSylvesterDet_common_scale, Polynomial.eval_mul, Polynomial.eval_pow,
    Polynomial.eval_C, derivativeSylvesterDet_affineW_eval]

/-- Inverse W transport requires v nonzero. The source witness is explicit. -/
theorem derivativeSylvesterDet_scalar_affineW_witness
    (F : Polynomial (Polynomial K)) (a : Nat) (l v b t : K)
    (hl : l ≠ 0) (hv : v ≠ 0)
    (ht : (derivativeSylvesterDet F a).eval t ≠ 0) :
    (derivativeSylvesterDet
      (Polynomial.C (Polynomial.C l) * F.map (affineWHom v b)) a).eval ((t-b)/v) ≠ 0 := by
  rw [derivativeSylvesterDet_scalar_affineW_eval]
  have he : v*((t-b)/v)+b = t := by field_simp [hv]; ring
  rw [he]
  exact mul_ne_zero (pow_ne_zero _ hl) ht

end
end TenthDiscriminant
