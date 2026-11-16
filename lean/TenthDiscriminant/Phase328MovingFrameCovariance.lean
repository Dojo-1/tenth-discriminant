import TenthDiscriminant.Phase328StabilizedSourceReturn

/-!
# Phase328 — generic integral moving-Gram covariance

This proves the conditional *universal matrix-algebra transport*
without assuming a new action on original ordinary-Z polynomial jets.

For rectangular matrices Iota and Pi with Pi*Iota=1, Gram Bhat
and a frame U with U^T*U=1, the transformed maps and moving metric
return exactly to the original Gram. Unimodular determinant-one
frames preserve det Bhat under the moving congruence. The passage
from the specialized Bhat=B+I+I+I to det(Bhat)=det B is separate:
this file does not silently claim that latter theorem.
-/
namespace TenthDiscriminant.Phase328
set_option autoImplicit false

/-- A covariantly transported integral projection remains a retraction. -/
theorem moving_retraction {n m : Nat}
    (U : Matrix (Fin m) (Fin m) Int)
    (Iota : Matrix (Fin m) (Fin n) Int)
    (Pi : Matrix (Fin n) (Fin m) Int)
    (horth : U.transpose * U = 1)
    (hretract : Pi * Iota = 1) :
    (Pi * U.transpose) * (U * Iota) = 1 := by
  calc
    _ = Pi * (U.transpose * U) * Iota := by
      simp only [Matrix.mul_assoc]
    _ = Pi * Iota := by simp [horth]
    _ = 1 := hretract

/-- A changing metric and changing inclusion recover exactly B.
This is an algebraic covariance identity, not an additional prime
divisor in B or an H_D action on the source jets. -/
theorem moving_gram_return {n m : Nat}
    (B : Matrix (Fin n) (Fin n) Int)
    (Bhat U : Matrix (Fin m) (Fin m) Int)
    (Iota : Matrix (Fin m) (Fin n) Int)
    (horth : U.transpose * U = 1)
    (hsource : Iota.transpose * Bhat * Iota = B) :
    (U * Iota).transpose *
        (U * Bhat * U.transpose) * (U * Iota) = B := by
  calc
    _ = (Iota.transpose * (U.transpose * U)) * Bhat *
          ((U.transpose * U) * Iota) := by
      simp only [Matrix.transpose_mul, Matrix.mul_assoc]
    _ = Iota.transpose * Bhat * Iota := by
      simp [horth]
    _ = B := hsource

/-- Determinant equality for a determinant-one integral moving frame. -/
theorem moving_det_return {m : Nat}
    (Bhat U : Matrix (Fin m) (Fin m) Int)
    (hdet : U.det = 1) :
    (U * Bhat * U.transpose).det = Bhat.det := by
  simp [Matrix.det_mul, Matrix.det_transpose, hdet]

end TenthDiscriminant.Phase328

#print axioms TenthDiscriminant.Phase328.moving_retraction
#print axioms TenthDiscriminant.Phase328.moving_gram_return
#print axioms TenthDiscriminant.Phase328.moving_det_return
