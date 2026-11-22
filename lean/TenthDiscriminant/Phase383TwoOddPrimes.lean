import TenthDiscriminant.FiniteSieveBridge

/-!
# Phase383 — source-faithful bounded class-one sieve using only p=3 and p=7

This theorem uses existing, genuinely typed imaginary-quadratic class-number
and norm-lifting lemmas. It does NOT assume the global nine-classification
theorem, any RH or zero-free hypothesis, or a surrogate determinant.

The 2-adic obstruction is already proved in OddPrimeTwo:
large class-number-one squarefree radicands satisfy d % 8 = 3.
Only the TWO additional odd primes 3 and 7 are needed below 200.

The finite Boolean certificate is an independent endpoint check.
The external analytic argument needed to reduce an arbitrary field to
the finite domain is not supplied here.
-/

namespace TenthDiscriminant.Phase383

def oddTwoPrimeCandidate (d : Nat) : Bool :=
  decide (d % 8 = 3) && guardedPrimeTests d [3, 7]

def oddTwoPrimeCandidatesBelow200 : List Nat :=
  (List.range 200).filter oddTwoPrimeCandidate

theorem odd_two_prime_candidates_exact :
    oddTwoPrimeCandidatesBelow200 = [3, 11, 19, 43, 67, 163] := by
  decide +kernel

theorem odd_primes_checked : checkedOddPrimes [3, 7] = true := by
  decide +kernel

/-- On the ACTUAL squarefree imaginary quadratic field family, the
existing maximal-order norm argument and 2-adic source theorem force
a two-odd-prime finite list without importing global classification. -/
theorem classNumber_one_parameter_below_200
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hclass : NumberField.classNumber (ImaginaryQuadraticField d) = 1)
    (hd : d < 200) :
    d ∈ ([1, 2, 3, 7, 11, 19, 43, 67, 163] : List Nat) := by
  rcases imaginaryQuadratic_classNumber_one_small_or_mod_eight d hsq hclass with
    h1 | h2 | h3 | h7 | hmod
  · simp [h1]
  · simp [h2]
  · simp [h3]
  · simp [h7]
  · have htest : guardedPrimeTests d [3, 7] = true :=
      guardedPrimeTests_of_classNumber_one d hsq hclass hmod
        [3, 7] odd_primes_checked
    have hmem : d ∈ oddTwoPrimeCandidatesBelow200 := by
      change d ∈ (List.range 200).filter oddTwoPrimeCandidate
      exact List.mem_filter.mpr
        ⟨List.mem_range.mpr hd, by simp [oddTwoPrimeCandidate, hmod, htest]⟩
    rw [odd_two_prime_candidates_exact] at hmem
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem ⊢
    tauto

/-- Removing the prime 7 weakens the candidate sieve, as an exact
negative control rather than a claim about the underlying class number. -/
theorem missing_seven_allows_187 :
    oddTwoPrimeCandidate 187 = false ∧
    (decide (187 % 8 = 3) && guardedPrimeTests 187 [3]) = true := by
  decide +kernel

/-- Removing the prime 3 similarly admits the composite radicand 27. -/
theorem missing_three_allows_27 :
    oddTwoPrimeCandidate 27 = false ∧
    (decide (27 % 8 = 3) && guardedPrimeTests 27 [7]) = true := by
  decide +kernel

/-- Deliberately false closed-interval strengthening: d=163 and p=41
is the endpoint guard from the original source, and must not be changed
from its strict norm threshold. -/
theorem strict_prime_guard_regression :
    guardedPrimeTest 163 41 = true ∧
    modularRootTest 163 41 = true := by
  decide +kernel

end TenthDiscriminant.Phase383

#print axioms TenthDiscriminant.Phase383.classNumber_one_parameter_below_200
#print axioms TenthDiscriminant.Phase383.odd_two_prime_candidates_exact
