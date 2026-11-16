import TenthDiscriminant.Phase328MovingFrameCovariance
import Mathlib.Tactic.Group

/-!
# Phase329: algebraic handle-slide (knot) return and conjugacy quandle

A general integral change of presentation T with inverse Tinv
acts on an auxiliary bilinear form by T^T * Bhat * T.
Transport the source inclusion by Tinv, and the return by T.
The original source Gram is recovered exactly. This theorem is
generic: it does NOT assume the existence of the desired new
ray-class representation on the unchanged ordinary-Z jet lattice.

Conjugation quandle identities underlie Reidemeister moves; the
finite knot-coloring experiments are in research/phase329/.
The move is a knot-theoretic *analogy* until a framed link or
braid presentation of the particular arithmetic object is supplied.
-/
namespace TenthDiscriminant.Phase329
set_option autoImplicit false

/-- An arbitrary invertible integral handle-slide presentation
preserves a retraction to the original source rows. -/
theorem integral_slide_retraction {n m : Nat}
    (T Tinv : Matrix (Fin m) (Fin m) Int)
    (Iota : Matrix (Fin m) (Fin n) Int)
    (Pi : Matrix (Fin n) (Fin m) Int)
    (hTi : T * Tinv = 1)
    (hretract : Pi * Iota = 1) :
    (Pi * T) * (Tinv * Iota) = 1 := by
  calc
    _ = Pi * (T * Tinv) * Iota := by simp only [Matrix.mul_assoc]
    _ = Pi * Iota := by simp [hTi]
    _ = 1 := hretract

/-- The exact source Gram is recovered after an arbitrary integral
handle-slide congruence. The source metric Bhat must be transported
along with its embedding; there is no new arithmetic divisor. -/
theorem integral_slide_gram_return {n m : Nat}
    (B : Matrix (Fin n) (Fin n) Int)
    (Bhat T Tinv : Matrix (Fin m) (Fin m) Int)
    (Iota : Matrix (Fin m) (Fin n) Int)
    (hTi : T * Tinv = 1)
    (hsource : Iota.transpose * Bhat * Iota = B) :
    (Tinv * Iota).transpose *
        (T.transpose * Bhat * T) * (Tinv * Iota) = B := by
  have htr : Tinv.transpose * T.transpose = 1 := by
    calc
      Tinv.transpose * T.transpose =
          (T * Tinv).transpose := by rw [Matrix.transpose_mul]
      _ = 1 := by simp [hTi]
  calc
    _ = Iota.transpose * (Tinv.transpose * T.transpose) * Bhat *
          ((T * Tinv) * Iota) := by
      simp only [Matrix.transpose_mul, Matrix.mul_assoc]
    _ = Iota.transpose * Bhat * Iota := by simp [htr, hTi]
    _ = B := hsource

/-- The integral determinant is invariant under a determinant-one
handle-slide matrix. No increase in p-adic valuation is possible. -/
theorem integral_slide_det_return {m : Nat}
    (Bhat T : Matrix (Fin m) (Fin m) Int)
    (hdet : T.det = 1) :
    (T.transpose * Bhat * T).det = Bhat.det := by
  simp [Matrix.det_mul, Matrix.det_transpose, hdet]

variable {G : Type*} [Group G]

/-- The conjugation quandle in which the colors may be rational
Frobenius elements of a Galois group. -/
def conjugationQuandle (x y : G) : G := y⁻¹ * x * y

/-- Reidemeister-I algebra: a strand conjugates itself trivially. -/
theorem quandle_idempotent (x : G) :
    conjugationQuandle x x = x := by
  simp [conjugationQuandle]

/-- Reidemeister-II algebra: right conjugation has a right inverse. -/
theorem quandle_right_inverse (x y : G) :
    y * conjugationQuandle x y * y⁻¹ = x := by
  dsimp [conjugationQuandle]
  group

/-- Reidemeister-III algebra: self-distributivity for an arbitrary,
possibly noncommutative group. This is not a prime bound. -/
theorem quandle_self_distributive (x y z : G) :
    conjugationQuandle (conjugationQuandle x y) z =
      conjugationQuandle (conjugationQuandle x z)
        (conjugationQuandle y z) := by
  dsimp [conjugationQuandle]
  group

/-- Positive Hurwitz crossing, product-preserving for any group. -/
def hurwitzPositive (x y : G) : G × G :=
  (x * y * x⁻¹, x)

/-- The product of two strands is invariant under a Hurwitz crossing. -/
theorem hurwitz_product_preserved (x y : G) :
    (hurwitzPositive x y).1 * (hurwitzPositive x y).2 = x * y := by
  dsimp [hurwitzPositive]
  group

end TenthDiscriminant.Phase329

#print axioms TenthDiscriminant.Phase329.integral_slide_retraction
#print axioms TenthDiscriminant.Phase329.integral_slide_gram_return
#print axioms TenthDiscriminant.Phase329.integral_slide_det_return
#print axioms TenthDiscriminant.Phase329.quandle_self_distributive
#print axioms TenthDiscriminant.Phase329.hurwitz_product_preserved
