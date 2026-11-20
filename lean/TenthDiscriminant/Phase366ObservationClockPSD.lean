import TenthDiscriminant.IntegerTraceGram
import TenthDiscriminant.GramMatrix

/-!
# Phase366 — original observation-clock increments are positive semidefinite

Keep the original ordinary Z-jet, fixed conjugate W, original 2*(ac+Dbd)
trace, fixed finite sample Q and fixed polynomial row family. Advancing the
derivative clock from J to J+1 adds exactly ONE unchanged derivative observation
at j=J; it is not an integral row-basis isomorphism. The added matrix is PSD,
but its integer determinant prime valuations need NOT be monotone.

The field threshold 301^4 is not used and receives no additional prime factor.
-/
namespace TenthDiscriminant.Phase366

open TenthDiscriminant Matrix
open scoped ComplexConjugate
set_option autoImplicit false
noncomputable section

/-- The new real-valued observation row at exact derivative clock J. -/
def clockRealFeatures {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) P Real :=
  fun i z => (derivativeRow (rows i).1 (rows i).2 J z.1).re

/-- The imaginary-valued observation row, with W held fixed. -/
def clockImagFeatures {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) P Real :=
  fun i z => (derivativeRow (rows i).1 (rows i).2 J z.1).im

/-- Same trace pairing as in the ORIGINAL full derivative source, but
with only the newly added observation j=J retained. -/
def clockDelta {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) (Fin n) Real :=
  fun a b => 2 * P.sum (fun z =>
    (derivativeRow (rows a).1 (rows a).2 J z *
      conj (derivativeRow (rows b).1 (rows b).2 J z)).re)

/-- A single observation clock decomposes into the exact real and imaginary
feature matrices of the original ordinary derivative rows. -/
theorem clockDelta_factorization {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n → Nat × Nat) :
    clockDelta P J rows =
      (clockRealFeatures P J rows * (clockRealFeatures P J rows).conjTranspose +
       clockImagFeatures P J rows * (clockImagFeatures P J rows).conjTranspose) +
      (clockRealFeatures P J rows * (clockRealFeatures P J rows).conjTranspose +
       clockImagFeatures P J rows * (clockImagFeatures P J rows).conjTranspose) := by
  classical
  have hsum (f : Complex → Real) :
      (Finset.univ.sum (fun z : P => f z.1)) = P.sum f :=
    Finset.sum_coe_sort P f
  ext a b
  have hRe := hsum (fun z =>
    (derivativeRow (rows a).1 (rows a).2 J z).re *
      (derivativeRow (rows b).1 (rows b).2 J z).re)
  have hIm := hsum (fun z =>
    (derivativeRow (rows a).1 (rows a).2 J z).im *
      (derivativeRow (rows b).1 (rows b).2 J z).im)
  simp only [clockDelta, Matrix.add_apply, Matrix.mul_apply,
    Matrix.conjTranspose_apply, star_trivial, clockRealFeatures,
    clockImagFeatures]
  rw [hRe, hIm]
  simp only [Complex.mul_re, Complex.conj_re, Complex.conj_im,
    mul_neg, sub_neg_eq_add, Finset.sum_add_distrib]
  ring

/-- This is genuine PSD for a fixed original row and source, without
assuming that any determinant is positive. -/
theorem clockDelta_posSemidef {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n → Nat × Nat) :
    (clockDelta P J rows).PosSemidef := by
  classical
  rw [clockDelta_factorization]
  have h := (Matrix.posSemidef_self_mul_conjTranspose
    (clockRealFeatures P J rows)).add
    (Matrix.posSemidef_self_mul_conjTranspose
      (clockImagFeatures P J rows))
  exact h.add h

/-- Exact entrywise clock increment of the old REAL trace-Gram matrix. -/
theorem traceGramMatrix_clock_succ {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n → Nat × Nat) :
    traceGramMatrix P (J+1) rows =
      traceGramMatrix P J rows + clockDelta P J rows := by
  ext a b
  simp only [traceGramMatrix, traceGramEntry, clockDelta,
    Matrix.add_apply, Finset.sum_range_succ]
  ring

/-- Universal observation-clock Loewner monotonicity.
NOT a statement about p-adic valuations or arbitrary source changes. -/
theorem traceGramMatrix_clock_increment_posSemidef {n : Nat}
    (P : Finset Complex) (J : Nat) (rows : Fin n → Nat × Nat) :
    (traceGramMatrix P (J+1) rows -
      traceGramMatrix P J rows).PosSemidef := by
  have heq : traceGramMatrix P (J+1) rows -
      traceGramMatrix P J rows = clockDelta P J rows := by
    rw [traceGramMatrix_clock_succ]
    abel
  rw [heq]
  exact clockDelta_posSemidef P J rows

/-- Exact integer-coordinate clock step on the ORIGINAL finite source Q. -/
theorem integerTraceGramEntry_clock_succ
    (Q : Finset (Int × Int)) (D J r s t u : Nat) :
    integerTraceGramEntry Q D (J+1) r s t u =
      integerTraceGramEntry Q D J r s t u +
        Q.sum (fun p => integerPairTrace D
          (integerDerivativeRow D r s J p)
          (integerDerivativeRow D t u J p)) := by
  simp only [integerTraceGramEntry, Finset.sum_range_succ]

/-- The matching original integer matrix statement retains every row. -/
theorem integerTraceGramMatrix_clock_succ {n : Nat}
    (Q : Finset (Int × Int)) (D J : Nat) (rows : Fin n → Nat × Nat) :
    integerTraceGramMatrix Q D (J+1) rows =
      integerTraceGramMatrix Q D J rows +
        (fun a b => Q.sum (fun p => integerPairTrace D
          (integerDerivativeRow D (rows a).1 (rows a).2 J p)
          (integerDerivativeRow D (rows b).1 (rows b).2 J p)) :
          Matrix (Fin n) (Fin n) Int) := by
  ext a b
  exact integerTraceGramEntry_clock_succ Q D J
    (rows a).1 (rows a).2 (rows b).1 (rows b).2

/-- Source-locked integer-pair version of Loewner order, with the SAME Q,
row labels, ordinary-Z derivatives, 2*(ac+Dbd) weights and J clock. -/
theorem integerTraceGramMatrix_clock_increment_posSemidef {n : Nat}
    (Q : Finset (Int × Int)) (D J : Nat)
    (rows : Fin n → Nat × Nat) (hD : 0 < D) :
    ((integerTraceGramMatrix Q D (J+1) rows).map
        (Int.castRingHom Real) -
      (integerTraceGramMatrix Q D J rows).map
        (Int.castRingHom Real)).PosSemidef := by
  rw [integerTraceGramMatrix_cast Q D (J+1) rows hD,
    integerTraceGramMatrix_cast Q D J rows hD]
  exact traceGramMatrix_clock_increment_posSemidef
    (Q.image (pairEval D)) J rows

/-- Particular original row-major R-by-S source; no selected minor or
replacement of thin Q by padded Q is involved. -/
theorem integerRectangularTraceGram_clock_increment_posSemidef
    (Q : Finset (Int × Int)) (D J R S : Nat) (hD : 0 < D) :
    ((integerRectangularTraceGram Q D (J+1) R S).map
        (Int.castRingHom Real) -
      (integerRectangularTraceGram Q D J R S).map
        (Int.castRingHom Real)).PosSemidef := by
  exact integerTraceGramMatrix_clock_increment_posSemidef
    Q D J (fun i : Fin (R*S) => (i.val / S, i.val % S)) hD

end
end TenthDiscriminant.Phase366

#print axioms TenthDiscriminant.Phase366.traceGramMatrix_clock_increment_posSemidef
#print axioms TenthDiscriminant.Phase366.integerRectangularTraceGram_clock_increment_posSemidef
