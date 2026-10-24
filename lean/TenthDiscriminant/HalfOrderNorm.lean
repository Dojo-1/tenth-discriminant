import TenthDiscriminant.HalfOrderResidue
import Mathlib.RingTheory.Norm.Basic

/-!
# The two-dimensional norm chart of the half-integral order

The determinant calculation below is exact over `ℤ`. Connecting it
to `Algebra.norm` requires identifying this matrix with left
multiplication in the power basis of `AdjoinRoot`.
-/
namespace TenthDiscriminant

open Polynomial

/-- The sole reduction rule needed for multiplication in the order. -/
theorem halfOrder_root_sq (D : ℕ) :
    (AdjoinRoot.root (halfOrderPolynomial D)) ^ 2 =
      AdjoinRoot.root (halfOrderPolynomial D) -
        AdjoinRoot.of (halfOrderPolynomial D) (((D : ℤ) + 1) / 4) := by
  have h := AdjoinRoot.eval₂_root (halfOrderPolynomial D)
  change (X ^ 2 - X + C (((D : ℤ) + 1) / 4)).eval₂
    (AdjoinRoot.of (halfOrderPolynomial D))
    (AdjoinRoot.root (halfOrderPolynomial D)) = 0 at h
  simp only [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C] at h
  linear_combination h

/-- The second column of the claimed multiplication matrix is an
actual equality in the quotient order, not a formal symbol rewrite. -/
theorem halfOrder_mul_root (D : ℕ) (x y : ℤ) :
    (AdjoinRoot.of (halfOrderPolynomial D) x +
      AdjoinRoot.of (halfOrderPolynomial D) y *
        AdjoinRoot.root (halfOrderPolynomial D)) *
      AdjoinRoot.root (halfOrderPolynomial D) =
    AdjoinRoot.of (halfOrderPolynomial D)
        (-(((D : ℤ) + 1) / 4) * y) +
      AdjoinRoot.of (halfOrderPolynomial D) (x + y) *
        AdjoinRoot.root (halfOrderPolynomial D) := by
  let f := halfOrderPolynomial D
  let t := AdjoinRoot.root f
  let c : ℤ := ((D : ℤ) + 1) / 4
  have ht : t ^ 2 = t - AdjoinRoot.of f c := halfOrder_root_sq D
  change (AdjoinRoot.of f x + AdjoinRoot.of f y * t) * t =
    AdjoinRoot.of f (-c * y) + AdjoinRoot.of f (x + y) * t
  rw [map_add, map_mul, map_neg]
  linear_combination AdjoinRoot.of f y * ht

/-- Multiplication by `x+yT` in the ordered basis `(1,T)`, using
`T²=T-c`. -/
def halfOrderMultiplicationMatrix (c x y : ℤ) : Matrix (Fin 2) (Fin 2) ℤ :=
  !![x, -c * y; y, x + y]

/-- Its determinant is the positive-definite principal quadratic
form when `c=(D+1)/4` and `D>0`. This theorem asserts only the
matrix identity, not yet that this is `Algebra.norm`. -/
theorem halfOrderMultiplicationMatrix_det (c x y : ℤ) :
    (halfOrderMultiplicationMatrix c x y).det = x ^ 2 + x * y + c * y ^ 2 := by
  simp only [halfOrderMultiplicationMatrix, Matrix.det_fin_two_of]
  ring

/-- The `D=15` coefficient is `4`, giving the concrete form. -/
theorem fifteen_halfOrder_matrix_control (x y : ℤ) :
    (halfOrderMultiplicationMatrix 4 x y).det = x ^ 2 + x * y + 4 * y ^ 2 :=
  halfOrderMultiplicationMatrix_det 4 x y

end TenthDiscriminant
