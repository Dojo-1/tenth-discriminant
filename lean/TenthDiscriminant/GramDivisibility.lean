import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
# A two-sided determinant factor

An elementary row change and its matching column change preserve the
determinant. If the resulting integer matrix factors with `p` on the selected
row *and* column, its determinant is divisible by `p²`. The factorization
requires a `p²`-divisible shared pivot: divisibility of the row and column
separately would not suffice (the `1 × 1` matrix `[p]` is a counterexample).

This is a generic matrix lemma, not a proof that a particular Gram matrix
admits the factorization or of any universal inert-prime valuation bound.
-/
namespace TenthDiscriminant

/-- Scale just the selected coordinate by `p`. -/
def pivotScale {n : Type*} [DecidableEq n] (i : n) (p : Int) : n → Int :=
  fun k => if k = i then p else 1

/-- Add `c` times row `j` to row `i`, then perform the matching column change. -/
def gramShear {n : Type*} [DecidableEq n] (A : Matrix n n Int)
    (i j : n) (c : Int) : Matrix n n Int :=
  let B := Matrix.updateRow A i (A i + c • A j)
  Matrix.updateCol B i (fun k => B k i + c • B k j)

theorem gramShear_det {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n Int) {i j : n} (hij : i ≠ j) (c : Int) :
    (gramShear A i j c).det = A.det := by
  unfold gramShear
  rw [Matrix.det_updateCol_add_smul_self _ hij c,
    Matrix.det_updateRow_add_smul_self _ hij c]

/-- The same selected basis coordinate contributes one factor `p` on each
side. The integral middle matrix witnesses the necessary pivot factor. -/
theorem sq_dvd_det_of_two_sided_pivot {n : Type*} [Fintype n] [DecidableEq n]
    (B K : Matrix n n Int) (i : n) (p : Int)
    (hB : B = Matrix.diagonal (pivotScale i p) * K *
      Matrix.diagonal (pivotScale i p)) :
    p ^ 2 ∣ B.det := by
  have hprod : (∏ k, pivotScale i p k) = p := by
    simp [pivotScale, Fintype.prod_ite_eq']
  rw [hB, Matrix.det_mul, Matrix.det_mul, Matrix.det_diagonal, hprod]
  refine ⟨K.det, ?_⟩
  ring

/-- An elementary matching row/column change followed by an integral
two-sided pivot factor forces `p²` to divide the original determinant. -/
theorem sq_dvd_det_of_gramShear_factor {n : Type*} [Fintype n] [DecidableEq n]
    (A K : Matrix n n Int) {i j : n} (hij : i ≠ j) (c p : Int)
    (hfactor : gramShear A i j c = Matrix.diagonal (pivotScale i p) * K *
      Matrix.diagonal (pivotScale i p)) :
    p ^ 2 ∣ A.det := by
  rw [← gramShear_det A hij c]
  exact sq_dvd_det_of_two_sided_pivot (gramShear A i j c) K i p hfactor

end TenthDiscriminant
