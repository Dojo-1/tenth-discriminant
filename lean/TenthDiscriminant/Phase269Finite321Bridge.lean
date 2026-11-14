import TenthDiscriminant.FiniteSieveBridge

/-!
# Phase269 — honest finite-certificate interface at the 321^4 bound

The Boolean condition is the ORIGINAL ordinary modular-root predicate.
This file does not mistake the two external CPU enumerations for a
Lean proof of exhaustive coverage. In particular, the variable
hfinite below is an explicit UNDISCHARGED certificate premise.

This is separate from (and does not import) the already existing
unconditional nine-field classification.
-/
namespace TenthDiscriminant.Phase269
set_option autoImplicit false

def finite321Primes : List Nat :=
  [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
    83,89,97,101,103,107,109]

theorem finite321Primes_checked :
    checkedOddPrimes finite321Primes = true := by decide +kernel

/-- Once the arithmetic Boolean certificate is checked IN LEAN, it
excludes class number one in the bounded range. No classification
theorem or numeric external evidence is used as a hidden premise. -/
theorem no_classNumber_one_of_finite321_certificate
    (hfinite : ∀ d : Nat, 163 < d → d < (321 : Nat)^4 → d % 8 = 3 →
      guardedPrimeTests d finite321Primes = false)
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hlo : 163 < d) (hhi : d < (321 : Nat)^4) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  intro hc
  have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
  have htests := guardedPrimeTests_of_classNumber_one d hsq hc hmod
    finite321Primes finite321Primes_checked
  have hbad := hfinite d hlo hhi hmod
  rw [hbad] at htests
  cases htests

end TenthDiscriminant.Phase269
