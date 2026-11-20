import TenthDiscriminant.Phase366ObservationClockPSD
import TenthDiscriminant.GramDivisibility

/-!
# Phase367 — original integer source evaluation matrices

For the SAME original Q, ordinary Z derivative holding W fixed, and row family,
define integer real-coordinate and imaginary-coordinate evaluation matrices
indexed by **all** (j,q) with 0 <= j < J and q in Q.

Prove EXACTLY the original integerTraceGramMatrix equality, retaining the
2*(ac + Dbd) trace and the complete row-major rectangular source.
No selected minor, alternate Gram, padded source or Hasse jets enter.
No new field cutoff follows from the matrix algebra.
-/
namespace TenthDiscriminant.Phase367

open TenthDiscriminant Matrix
set_option autoImplicit false
noncomputable section

/-- The original ordinary-Z derivative's first integer-pair coordinate. -/
def originalRealEvaluation {n : Nat} (Q : Finset (Int × Int)) (D J : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) (Fin J × Q) Int :=
  fun i c => (integerDerivativeRow D (rows i).1 (rows i).2 c.1 c.2).1

/-- The original ordinary-Z derivative's second integer-pair coordinate. -/
def originalImagEvaluation {n : Nat} (Q : Finset (Int × Int)) (D J : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) (Fin J × Q) Int :=
  fun i c => (integerDerivativeRow D (rows i).1 (rows i).2 c.1 c.2).2

/-- The exact full feature-matrix product with the ORIGINAL integral trace
weights. Factor 2 and the coefficient D are required; dropping either
changes the same original Gram. -/
def originalEvaluationGram {n : Nat} (Q : Finset (Int × Int)) (D J : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) (Fin n) Int :=
  fun a b =>
    2 * (((originalRealEvaluation Q D J rows) *
            (originalRealEvaluation Q D J rows).transpose) a b +
      (D : Int) * ((originalImagEvaluation Q D J rows) *
            (originalImagEvaluation Q D J rows).transpose) a b)

/-- Exact inner-product formula, with the full original finite Q and
ordinary derivative clock range. This proof works even at D=0. -/
theorem original_integer_trace_gram_factorization {n : Nat}
    (Q : Finset (Int × Int)) (D J : Nat) (rows : Fin n → Nat × Nat) :
    integerTraceGramMatrix Q D J rows =
      originalEvaluationGram Q D J rows := by
  classical
  have hsum (f : Nat → (Int × Int) → Int) :
      (Finset.univ.sum (fun c : Fin J × Q => f c.1 c.2)) =
        (Finset.range J).sum (fun j => Q.sum (f j)) := by
    rw [Fintype.sum_prod_type]
    calc
      _ = Finset.univ.sum (fun j : Fin J => Q.sum (f j)) := by
        apply Finset.sum_congr rfl
        intro j hj
        exact Finset.sum_coe_sort Q (f j)
      _ = _ := Fin.sum_univ_eq_sum_range (fun j => Q.sum (f j)) J
  ext a b
  have hReal := hsum (fun j p =>
    (integerDerivativeRow D (rows a).1 (rows a).2 j p).1 *
      (integerDerivativeRow D (rows b).1 (rows b).2 j p).1)
  have hImag := hsum (fun j p =>
    (integerDerivativeRow D (rows a).1 (rows a).2 j p).2 *
      (integerDerivativeRow D (rows b).1 (rows b).2 j p).2)
  simp only [integerTraceGramMatrix, integerTraceGramEntry,
    integerPairTrace, originalEvaluationGram, Matrix.mul_apply,
    Matrix.transpose_apply, originalRealEvaluation, originalImagEvaluation] 
  rw [hReal, hImag]
  simp only [Finset.mul_sum, Finset.sum_add_distrib, mul_add]
  ring

/-- The original row-major R by S object is a literal specialization,
not a minor or alternative source. -/
theorem original_rectangular_integer_gram_factorization
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    integerRectangularTraceGram Q D J R S =
      originalEvaluationGram Q D J
        (fun i : Fin (R*S) => (i.val / S, i.val % S)) := by
  exact original_integer_trace_gram_factorization Q D J _

/-- An INTEGRAL row-frame with determinant one leaves the determinant
of the exact same original Gram unchanged; it need not fix the entries. -/
theorem original_gram_unimodular_det {n : Nat}
    (Q : Finset (Int × Int)) (D J : Nat) (rows : Fin n → Nat × Nat)
    (U : Matrix (Fin n) (Fin n) Int) (hU : U.det = 1) :
    (U * integerTraceGramMatrix Q D J rows * U.transpose).det =
      (integerTraceGramMatrix Q D J rows).det := by
  simp only [Matrix.det_mul, Matrix.det_transpose, hU, one_mul, mul_one]

end
end TenthDiscriminant.Phase367

#print axioms TenthDiscriminant.Phase367.original_integer_trace_gram_factorization
#print axioms TenthDiscriminant.Phase367.original_rectangular_integer_gram_factorization
#print axioms TenthDiscriminant.Phase367.original_gram_unimodular_det
