import TenthDiscriminant.HalfOrderNorm

/-!
# Algebraic norm of the explicit half-integral quadratic order

The monic relation `T²-T+c=0` gives a free rank-two order with
basis `(1,T)`. The norm is the determinant of multiplication in that
basis, not an independently chosen quadratic form. This file does
not identify the order with a number field's maximal integer ring.
-/

namespace TenthDiscriminant
open Polynomial

private noncomputable def qpoly (c : ℤ) : Polynomial ℤ := X ^ 2 - X + C c

private theorem qmonic (c : ℤ) : (qpoly c).Monic := by
  have hle : ((-X + C c : Polynomial ℤ).degree) ≤ 1 := by compute_degree!
  have hdeg : ((-X + C c : Polynomial ℤ).degree) < 2 :=
    lt_of_le_of_lt hle (by norm_num)
  simpa only [qpoly, sub_eq_add_neg, add_assoc] using monic_X_pow_add hdeg

private theorem qdegree (c : ℤ) : (qpoly c).natDegree = 2 := by
  unfold qpoly
  compute_degree!

private noncomputable def qbasis (c : ℤ) : Basis (Fin 2) ℤ (AdjoinRoot (qpoly c)) :=
  (AdjoinRoot.powerBasis' (qmonic c)).basis.reindex (finCongr (qdegree c))

private theorem qbasis_zero (c : ℤ) : qbasis c 0 = 1 := by
  rw [qbasis, Basis.reindex_apply]
  rw [PowerBasis.basis_eq_pow]
  simp

private theorem qbasis_one (c : ℤ) : qbasis c 1 = AdjoinRoot.root (qpoly c) := by
  rw [qbasis, Basis.reindex_apply]
  rw [PowerBasis.basis_eq_pow]
  simp

private theorem qbasis_repr (c x y : ℤ) (i : Fin 2) :
    ((qbasis c).repr (AdjoinRoot.of (qpoly c) x +
      AdjoinRoot.of (qpoly c) y * AdjoinRoot.root (qpoly c))) i =
      (if i = 0 then x else y) := by
  have hs : AdjoinRoot.of (qpoly c) x +
      AdjoinRoot.of (qpoly c) y * AdjoinRoot.root (qpoly c) =
        x • qbasis c 0 + y • qbasis c 1 := by
    simp [qbasis_zero, qbasis_one, Algebra.smul_def]
  rw [hs, map_add, map_smul, map_smul]
  fin_cases i <;> simp

private theorem qroot_sq (c : ℤ) :
    (AdjoinRoot.root (qpoly c)) ^ 2 =
      AdjoinRoot.root (qpoly c) - AdjoinRoot.of (qpoly c) c := by
  have h := AdjoinRoot.eval₂_root (qpoly c)
  change (X ^ 2 - X + C c).eval₂
    (AdjoinRoot.of (qpoly c)) (AdjoinRoot.root (qpoly c)) = 0 at h
  simp only [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C] at h
  linear_combination h

private theorem qmul_root (c x y : ℤ) :
    (AdjoinRoot.of (qpoly c) x +
      AdjoinRoot.of (qpoly c) y * AdjoinRoot.root (qpoly c)) *
      AdjoinRoot.root (qpoly c) =
    AdjoinRoot.of (qpoly c) (-c * y) +
      AdjoinRoot.of (qpoly c) (x + y) * AdjoinRoot.root (qpoly c) := by
  have ht := qroot_sq c
  rw [map_add, map_mul, map_neg]
  linear_combination AdjoinRoot.of (qpoly c) y * ht

private theorem qleftMulMatrix (c x y : ℤ) :
    (Algebra.leftMulMatrix (qbasis c))
      (AdjoinRoot.of (qpoly c) x +
        AdjoinRoot.of (qpoly c) y * AdjoinRoot.root (qpoly c)) =
      !![x, -c * y; y, x + y] := by
  ext i j
  have hj : j = 0 ∨ j = 1 := by fin_cases j <;> simp
  rcases hj with rfl | rfl
  · rw [Algebra.leftMulMatrix_eq_repr_mul, qbasis_zero, mul_one]
    have h := qbasis_repr c x y i
    fin_cases i <;> simpa using h
  · rw [Algebra.leftMulMatrix_eq_repr_mul, qbasis_one, qmul_root]
    have h := qbasis_repr c (-c * y) (x + y) i
    fin_cases i <;> simpa using h

private theorem qnorm (c x y : ℤ) :
    Algebra.norm ℤ (AdjoinRoot.of (qpoly c) x +
      AdjoinRoot.of (qpoly c) y * AdjoinRoot.root (qpoly c)) =
      x ^ 2 + x * y + c * y ^ 2 := by
  rw [Algebra.norm_eq_matrix_det (qbasis c), qleftMulMatrix]
  simp only [Matrix.det_fin_two_of]
  ring

/-- The algebraic norm on the monic quadratic order is the
determinant of its actual multiplication map. -/
theorem quadraticOrder_norm (c x y : ℤ) :
    Algebra.norm ℤ (AdjoinRoot.of (X ^ 2 - X + C c) x +
      AdjoinRoot.of (X ^ 2 - X + C c) y *
        AdjoinRoot.root (X ^ 2 - X + C c)) =
      x ^ 2 + x * y + c * y ^ 2 := by
  simpa only [qpoly] using qnorm c x y

/-- In the repository's discriminant coordinates, this is exactly
the existing `principalNorm`, not merely a similar formula. -/
theorem halfOrder_norm_eq_principalNorm (D : ℕ) (x y : ℤ) :
    Algebra.norm ℤ (AdjoinRoot.of (halfOrderPolynomial D) x +
      AdjoinRoot.of (halfOrderPolynomial D) y *
        AdjoinRoot.root (halfOrderPolynomial D)) =
      principalNorm (D : ℤ) x y := by
  simpa only [halfOrderPolynomial, principalNorm] using
    quadraticOrder_norm (((D : ℤ) + 1) / 4) x y

/-- `D=15` has coefficient `4`; the generator's norm checks it. -/
theorem fifteen_halfOrder_norm_root :
    Algebra.norm ℤ (AdjoinRoot.root (halfOrderPolynomial 15)) = 4 := by
  simpa [principalNorm] using halfOrder_norm_eq_principalNorm 15 0 1

/-- A scalar acts by `x` on each of the two basis vectors. -/
theorem halfOrder_norm_scalar (D : ℕ) (x : ℤ) :
    Algebra.norm ℤ (AdjoinRoot.of (halfOrderPolynomial D) x) = x ^ 2 := by
  simpa [principalNorm] using halfOrder_norm_eq_principalNorm D x 0

end TenthDiscriminant
