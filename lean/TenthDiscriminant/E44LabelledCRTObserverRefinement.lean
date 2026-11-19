import TenthDiscriminant.E43IndependentConjugationObserver
import TenthDiscriminant.E33ConductorCRTExactness

/-!
# E44 — Labelled Gaussian CRT probes refine the sign-blind original Gram

On the SAME original integer-pair source in the Gaussian order D=1,
E43's complete positive trace Gram is blind to injective per-point
conjugation even at arbitrary original ordinary-jet orders.

E33's distinct LABELLED Gaussian split-prime probes mod 5 carry
an extra odd-in-conjugation residue gap:
  (a+2b) - (a-2b) = 4b mod 5.

Aggregating this additional observer over the SAME original Finset
distinguishes one E43 partial-sign collision that every original Gram
fails to separate, but remains noninjective on all possible supports.

This is a NEW OBSERVATION, not a new factor of the original Gram,
nor a number-field class-number, p-adic or complexity theorem.
-/

namespace TenthDiscriminant.E44
set_option autoImplicit false
noncomputable section

/-- The E33 labelled prime-gap observer applied directly to
an ORIGINAL integer Gaussian coefficient sample, D=1. -/
def sourcePrimeGap (q : Int × Int) : ZMod 5 :=
  E33.primeGap ((q.1 : ZMod 5),(q.2 : ZMod 5))

def totalPrimeGap (Q : Finset (Int × Int)) : ZMod 5 :=
  Q.sum sourcePrimeGap

/-- Exact source coefficient formula for the labelled Gaussian
split-prime difference; orientation is recorded mod 5. -/
theorem source_prime_gap_eq_four_imag
    (q : Int × Int) :
    sourcePrimeGap q = (4 : ZMod 5) * (q.2 : ZMod 5) := by
  rcases q with ⟨a,b⟩
  simp [sourcePrimeGap, E33.primeGap, E28.splitPlus, E28.splitMinus]
  ring

theorem total_prime_gap_is_imag_moment_mod5
    (Q : Finset (Int × Int)) :
    totalPrimeGap Q =
      (4 : ZMod 5) * Q.sum (fun q => (q.2 : ZMod 5)) := by
  unfold totalPrimeGap
  calc
    Q.sum sourcePrimeGap =
        Q.sum (fun q => (4 : ZMod 5) * (q.2 : ZMod 5)) := by
      apply Finset.sum_congr rfl
      intro q hq
      exact source_prime_gap_eq_four_imag q
    _ = _ := by rw [Finset.mul_sum]

/-- The specific E41 partial-sign collision is resolved by the
new labelled split-prime observer: gap 3 versus gap 0. -/
theorem labelled_prime_gap_distinguishes_partial_sign_sources :
    totalPrimeGap (E41.complexTwoSource 0 1 1 1) = 3 ∧
    totalPrimeGap (E41.complexTwoSource 0 1 1 (-1)) = 0 := by
  decide

/-- One ORIGINAL Gram, for EVERY original ordinary-jet rectangle,
is not enough to identify this source pair, while the additional
labelled Gaussian CRT observer DOES distinguish it. -/
theorem same_original_gram_but_different_labelled_crt
    (J R S : Nat) :
    (integerRectangularTraceGram
        (E41.complexTwoSource 0 1 1 1) 1 J R S =
      integerRectangularTraceGram
        (E41.complexTwoSource 0 1 1 (-1)) 1 J R S) ∧
      (totalPrimeGap (E41.complexTwoSource 0 1 1 1) ≠
        totalPrimeGap (E41.complexTwoSource 0 1 1 (-1))) := by
  constructor
  · exact (E43.non_global_partial_sign_collision_all_original_jets
      1 J R S).symm
  · rw [labelled_prime_gap_distinguishes_partial_sign_sources.1,
      labelled_prime_gap_distinguishes_partial_sign_sources.2]
    decide

/-- But one scalar gap is not a complete source reconstruction:
two distinct, globally conjugate supports have the same aggregate
labelled gap (zero) and the SAME original Gram at every row/jet. -/
def oppositeMixedSource : Finset (Int × Int) :=
  {(0,-1),(1,1)}

theorem gap_not_complete_even_with_entire_original_gram
    (J R S : Nat) :
    E41.complexTwoSource 0 1 1 (-1) ≠ oppositeMixedSource ∧
      totalPrimeGap (E41.complexTwoSource 0 1 1 (-1)) =
        totalPrimeGap oppositeMixedSource ∧
      integerRectangularTraceGram
        (E41.complexTwoSource 0 1 1 (-1)) 1 J R S =
      integerRectangularTraceGram oppositeMixedSource 1 J R S := by
  constructor
  · decide
  constructor
  · decide
  · have hconj :
        (E41.complexTwoSource 0 1 1 (-1)).image pairConj =
          oppositeMixedSource := by decide
    rw [← hconj]
    exact (integerRectangularTraceGram_conj
      (E41.complexTwoSource 0 1 1 (-1)) 1 J R S).symm

end
end TenthDiscriminant.E44

#print axioms TenthDiscriminant.E44.source_prime_gap_eq_four_imag
#print axioms TenthDiscriminant.E44.total_prime_gap_is_imag_moment_mod5
#print axioms TenthDiscriminant.E44.same_original_gram_but_different_labelled_crt
#print axioms TenthDiscriminant.E44.gap_not_complete_even_with_entire_original_gram
