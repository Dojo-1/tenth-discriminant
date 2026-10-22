import TenthDiscriminant.TraceGram
import TenthDiscriminant.GramHadamard

/-!
# The full real derivative trace-Gram matrix

Entries use the existing `traceGramEntry`, not a surrogate PSD matrix.
A real/imaginary factorization proves semidefiniteness and the sum-of-squares
identity. Hadamard bounds the determinant by the actual moment diagonals.
No interpolation, integrality, valuation or class-number theorem is assumed.
-/
namespace TenthDiscriminant
open Matrix
open scoped ComplexConjugate

noncomputable section

/-- Any finite ordered family of actual derivative rows; repeated labels are allowed. -/
def traceGramMatrix {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) : Matrix (Fin n) (Fin n) Real :=
  fun a b => traceGramEntry P J (rows a).1 (rows a).2 (rows b).1 (rows b).2

def traceRealFeatures {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) : Matrix (Fin n) (Fin J × P) Real :=
  fun a c => (derivativeRow (rows a).1 (rows a).2 c.1 c.2).re

def traceImagFeatures {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) : Matrix (Fin n) (Fin J × P) Real :=
  fun a c => (derivativeRow (rows a).1 (rows a).2 c.1 c.2).im

/-- Exact factorization retaining the factor two in the real trace product. -/
theorem traceGramMatrix_factorization {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) :
    traceGramMatrix P J rows =
      (traceRealFeatures P J rows * (traceRealFeatures P J rows).conjTranspose +
       traceImagFeatures P J rows * (traceImagFeatures P J rows).conjTranspose) +
      (traceRealFeatures P J rows * (traceRealFeatures P J rows).conjTranspose +
       traceImagFeatures P J rows * (traceImagFeatures P J rows).conjTranspose) := by
  classical
  have hsum (f : Nat -> Complex -> Real) :
      (Finset.univ.sum (fun c : Fin J × P => f c.1 c.2)) =
        (Finset.range J).sum (fun j => P.sum (f j)) := by
    rw [Fintype.sum_prod_type]
    calc
      _ = Finset.univ.sum (fun j : Fin J => P.sum (f j)) := by
        apply Finset.sum_congr rfl
        intro j hj
        exact Finset.sum_coe_sort P (f j)
      _ = _ := Fin.sum_univ_eq_sum_range (fun j => P.sum (f j)) J
  ext a b
  have hRe := hsum (fun j z =>
    (derivativeRow (rows a).1 (rows a).2 j z).re *
      (derivativeRow (rows b).1 (rows b).2 j z).re)
  have hIm := hsum (fun j z =>
    (derivativeRow (rows a).1 (rows a).2 j z).im *
      (derivativeRow (rows b).1 (rows b).2 j z).im)
  simp only [traceGramMatrix, traceGramEntry, Matrix.add_apply, Matrix.mul_apply,
    Matrix.conjTranspose_apply, star_trivial, traceRealFeatures, traceImagFeatures]
  rw [hRe, hIm]
  simp only [Complex.mul_re, Complex.conj_re, Complex.conj_im,
    mul_neg, sub_neg_eq_add, Finset.sum_add_distrib]
  ring

/-- Semidefiniteness holds without any row-independence assumption. -/
theorem traceGramMatrix_posSemidef {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) : (traceGramMatrix P J rows).PosSemidef := by
  classical
  rw [traceGramMatrix_factorization]
  have h := (Matrix.posSemidef_self_mul_conjTranspose (traceRealFeatures P J rows)).add
    (Matrix.posSemidef_self_mul_conjTranspose (traceImagFeatures P J rows))
  exact h.add h

/-- Expand a real Gram quadratic form as a sum of actual coordinate squares. -/
theorem real_gram_quadratic {n : Nat} {c : Type*} [Fintype c]
    (A : Matrix (Fin n) c Real) (x : Fin n -> Real) :
    dotProduct x ((A * A.conjTranspose).mulVec x) =
      Finset.univ.sum (fun j => (Finset.univ.sum (fun i => A i j * x i)) ^ 2) := by
  rw [← Matrix.mulVec_mulVec, Matrix.dotProduct_mulVec]
  simp only [Matrix.vecMul, Matrix.mulVec, Matrix.conjTranspose_apply, star_trivial,
    dotProduct]
  apply Finset.sum_congr rfl
  intro j hj
  rw [show (Finset.univ.sum (fun i => x i * A i j)) =
    Finset.univ.sum (fun i => A i j * x i) by
      apply Finset.sum_congr rfl
      intro i hi
      ring]
  ring

/-- The exact quadratic-form identity, not just a Boolean positivity check. -/
theorem traceGramMatrix_quadratic {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (x : Fin n -> Real) :
    dotProduct x ((traceGramMatrix P J rows).mulVec x) =
      2 * Finset.univ.sum (fun c : Fin J × P =>
        (Finset.univ.sum (fun i => traceRealFeatures P J rows i c * x i)) ^ 2 +
        (Finset.univ.sum (fun i => traceImagFeatures P J rows i c * x i)) ^ 2) := by
  classical
  rw [traceGramMatrix_factorization]
  simp only [Matrix.add_mulVec, dotProduct_add, real_gram_quadratic,
    Finset.sum_add_distrib]
  ring

theorem traceGramMatrix_det_nonneg {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) : 0 <= (traceGramMatrix P J rows).det :=
  real_psd_det_nonneg n _ (traceGramMatrix_posSemidef P J rows)

theorem traceGramMatrix_det_le_diag {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) :
    (traceGramMatrix P J rows).det <=
      Finset.univ.prod (fun i => traceGramEntry P J (rows i).1 (rows i).2
        (rows i).1 (rows i).2) :=
  real_psd_det_le_diag n _ (traceGramMatrix_posSemidef P J rows)

/-- The product uses the previously proved diagonal moment formula. -/
theorem traceGramMatrix_det_le_moments {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) :
    (traceGramMatrix P J rows).det <= Finset.univ.prod (fun i =>
      2 * (Finset.range J).sum (fun j =>
        if j <= (rows i).1 then ((rows i).1.descFactorial j : Real)^2 *
          normMoment P ((rows i).1 + (rows i).2 - j) else 0)) := by
  simpa only [traceGram_diagonal] using traceGramMatrix_det_le_diag P J rows

/-- Row-major enumeration of the R by S derivative grid, including the empty cases. -/
def rectangularTraceGram (P : Finset Complex) (J R S : Nat) :
    Matrix (Fin (R*S)) (Fin (R*S)) Real :=
  traceGramMatrix P J (fun i => (i.val / S, i.val % S))

theorem rectangularTraceGram_posSemidef (P : Finset Complex) (J R S : Nat) :
    (rectangularTraceGram P J R S).PosSemidef :=
  traceGramMatrix_posSemidef _ _ _

/-- Duplicate actual derivative rows have determinant zero. -/
theorem traceGramMatrix_duplicate_rows {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (a b : Fin n) (hab : a ≠ b) (heq : rows a = rows b) :
    (traceGramMatrix P J rows).det = 0 := by
  apply Matrix.det_zero_of_row_eq hab
  funext k
  simp [traceGramMatrix, heq]

/-- A single nonzero row gives the nonzero determinant 2, with the origin retained. -/
theorem traceGramMatrix_single_control :
    (traceGramMatrix {0} 2 (fun _ : Fin 1 => (0,0))).det = 2 := by
  simp [Matrix.det_unique, traceGramMatrix, traceGram_origin_control]

/-- Repeated labels cannot be promoted from PSD to a positive determinant. -/
theorem traceGramMatrix_duplicate_control :
    (traceGramMatrix {0} 2 (fun _ : Fin 2 => (0,0))).det = 0 := by
  exact traceGramMatrix_duplicate_rows _ _ _ 0 1 (by decide) rfl

/-- The successor row's unmatched derivative column makes this determinant 4, not 0. -/
theorem traceGramMatrix_unmatched_control :
    (traceGramMatrix {1} 2 (fun i : Fin 2 => if i = 0 then (0,0) else (1,1))).det = 4 := by
  norm_num [Matrix.det_fin_two, traceGramMatrix, traceGramEntry, derivativeRow,
    Finset.sum_range_succ, Nat.descFactorial]

theorem traceGramMatrix_zero_derivatives_control :
    (traceGramMatrix {1} 0 (fun i : Fin 2 => (i.val,0))).det = 0 := by
  simp [Matrix.det_fin_two, traceGramMatrix, traceGramEntry]

end
end TenthDiscriminant
