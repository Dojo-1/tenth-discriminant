import Mathlib

/-!
# The diagonal-product determinant bound

A real positive-semidefinite matrix has a real Gram factor. Apply Mathlib's
volume-form bound to its columns, then square. This includes singular and
zero-dimensional matrices; no positive-definiteness hypothesis is smuggled in.
-/
namespace TenthDiscriminant
open Matrix

/-- Hadamard's squared column-norm bound, using the existing volume-form theorem. -/
theorem real_det_sq_le_column_sq (n : Nat) (B : Matrix (Fin n) (Fin n) Real) :
    B.det ^ 2 <= Finset.univ.prod (fun i => Finset.univ.sum (fun j => B j i ^ 2)) := by
  let b := EuclideanSpace.basisFun (Fin n) Real
  let v : Fin n -> EuclideanSpace Real (Fin n) :=
    fun j => (WithLp.equiv 2 (Fin n -> Real)).symm (fun i => B i j)
  letI : Fact (Module.finrank Real (EuclideanSpace Real (Fin n)) = n) :=
    ⟨by simp⟩
  have hv : b.toBasis.toMatrix v = B := by
    ext i j
    rfl
  have hd : b.toBasis.det v = B.det := by
    change (b.toBasis.toMatrix v).det = B.det
    rw [hv]
  have h := b.toBasis.orientation.abs_volumeForm_apply_le v
  rw [b.toBasis.orientation.volumeForm_robust b rfl, hd] at h
  have hn (i : Fin n) : ‖v i‖ ^ 2 = Finset.univ.sum (fun j => B j i ^ 2) := by
    rw [EuclideanSpace.norm_eq, Real.sq_sqrt]
    · simp [v, Real.norm_eq_abs, sq_abs]
    · exact Finset.sum_nonneg (fun _ _ => sq_nonneg _)
  calc
    B.det ^ 2 = |B.det| ^ 2 := (sq_abs B.det).symm
    _ <= (Finset.univ.prod (fun i => ‖v i‖)) ^ 2 :=
      pow_le_pow_left₀ (abs_nonneg _) h 2
    _ = Finset.univ.prod (fun i => ‖v i‖ ^ 2) := (Finset.prod_pow _ _ _).symm
    _ = _ := by simp_rw [hn]

/-- The Gram determinant is nonnegative, also when the matrix is singular. -/
theorem real_psd_det_nonneg (n : Nat) (A : Matrix (Fin n) (Fin n) Real)
    (hA : A.PosSemidef) : 0 <= A.det := by
  obtain ⟨B, rfl⟩ := Matrix.posSemidef_iff_eq_transpose_mul_self.mp hA
  rw [Matrix.det_mul, Matrix.det_conjTranspose]
  simpa only [star_trivial, pow_two] using sq_nonneg B.det

/-- Hadamard's diagonal-product bound for real PSD matrices. -/
theorem real_psd_det_le_diag (n : Nat) (A : Matrix (Fin n) (Fin n) Real)
    (hA : A.PosSemidef) : A.det <= Finset.univ.prod (fun i => A i i) := by
  obtain ⟨B, rfl⟩ := Matrix.posSemidef_iff_eq_transpose_mul_self.mp hA
  have h := real_det_sq_le_column_sq n B
  simpa [Matrix.det_mul, Matrix.det_conjTranspose, Matrix.mul_apply,
    Matrix.conjTranspose_apply, pow_two] using h

end TenthDiscriminant
