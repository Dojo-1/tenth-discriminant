import TenthDiscriminant.AffineCoefficientTransport

/-!
# Explicit basis-certificate bridge for affine Z transport

The public theorem says `of_basis_certificate`: its structural premises are
not a proof of the universal affine polynomial theorem. This branch compiles
and audits the exact conditional helper before constructing those premises.
-/
namespace TenthDiscriminant
open Polynomial Matrix
noncomputable section

/-- Cancel the invertible basis determinant, never the source determinant. -/
theorem det_transport_of_basis_certificate
    {R : Type*} [CommRing R] [IsDomain R]
    {n : Type*} [Fintype n] [DecidableEq n]
    (A target T B D : Matrix n n R) (q s : R)
    (hM : T * A * D = target * B)
    (hT : T.det = q * B.det) (hD : D.det = s) (hB : B.det ≠ 0) :
    target.det = q * A.det * s := by
  have hd := congrArg Matrix.det hM
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_mul, hT, hD] at hd
  apply mul_right_cancel₀ hB
  calc
    target.det * B.det = (q * B.det) * A.det * s := hd.symm
    _ = (q * A.det * s) * B.det := by ring

/-- Affine transform of the original bivariate polynomial. -/
def affineBivariate {K : Type*} [Field K] (F : Polynomial (Polynomial K))
    (l u h v b : K) : Polynomial (Polynomial K) :=
  Polynomial.C (Polynomial.C l) *
    (F.map (affineWHom v b)).comp
      (Polynomial.C (Polynomial.C u) * Polynomial.X +
       Polynomial.C (Polynomial.C h))

variable {K : Type*} [Field K]

theorem polynomial_matrix_det_eval {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n (Polynomial K)) (t : K) :
    (A.map (Polynomial.evalRingHom t)).det = A.det.eval t :=
  (RingHom.map_det (Polynomial.evalRingHom t) A).symm

/-- Conditional actual-matrix transport, with every missing basis fact explicit. -/
theorem derivativeSylvester_affine_eval_of_basis_certificate
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (l u h v b t : K)
    (T B D : Matrix (Fin (a+(a-1))) (Fin (a+(a-1))) K)
    (hM : T * (fixedSylvesterMatrix F F.derivative a (a-1)).map
          (Polynomial.evalRingHom (v*t+b)) * D =
        (fixedSylvesterMatrix (affineBivariate F l u h v b)
          (affineBivariate F l u h v b).derivative a (a-1)).map
          (Polynomial.evalRingHom t) * B)
    (hT : T.det = u^(a*(a-1)) * B.det)
    (hD : D.det = l^(a+(a-1)) * u^a)
    (hB : B.det ≠ 0) :
    (derivativeSylvesterDet (affineBivariate F l u h v b) a).eval t =
      l^(a+(a-1)) * u^(a*a) * (derivativeSylvesterDet F a).eval (v*t+b) := by
  have hd := det_transport_of_basis_certificate
    ((fixedSylvesterMatrix F F.derivative a (a-1)).map
      (Polynomial.evalRingHom (v*t+b)))
    ((fixedSylvesterMatrix (affineBivariate F l u h v b)
      (affineBivariate F l u h v b).derivative a (a-1)).map
      (Polynomial.evalRingHom t))
    T B D (u^(a*(a-1))) (l^(a+(a-1)) * u^a) hM hT hD hB
  rw [polynomial_matrix_det_eval, polynomial_matrix_det_eval] at hd
  have he : a*(a-1)+a = a*a := by
    calc
      a*(a-1)+a = a*((a-1)+1) := by ring
      _ = a*a := by rw [Nat.sub_add_cancel ha]
  unfold derivativeSylvesterDet
  rw [hd]
  calc
    _ = l^(a+(a-1)) * (u^(a*(a-1)) * u^a) *
        (fixedSylvesterMatrix F F.derivative a (a-1)).det.eval (v*t+b) := by ring
    _ = _ := by rw [← pow_add, he]

end
end TenthDiscriminant
