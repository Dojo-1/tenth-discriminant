import TenthDiscriminant.Phase260EnhancedOriginalGram321
import TenthDiscriminant.Phase323FinitePrimeCertificate

/-!
# Phase323: source-exact extended odd-prime product

The already verified Phase260 local theorem works for every eligible
odd prime. This file selects 3,5 and ten explicit further primes and
assembles their full vertical+horizontal exponents ONCE per prime,
without assuming independent determinant factors.

The binary exponent remains the old Phase162 exponent in this module.
Its proposed horizontal strengthening needs a separate combined
unimodular original-jet proof; do not multiply two 2-adic divisors.
-/
namespace TenthDiscriminant.Phase323
open scoped BigOperators Classical
open TenthDiscriminant.Phase259
open TenthDiscriminant.Phase260
set_option autoImplicit false

def selectedOddHorizontalPrime (p : Nat) : Prop :=
  p = 3 ∨ p = 5 ∨ p ∈ oddHorizontalPrimes

/-- Exactly one complete exponent is assigned to each selected prime. -/
noncomputable def extendedOddValuationWeight (R S p : Nat) : Nat :=
  valuationWeight R S p +
    (if selectedOddHorizontalPrime p then R*floorMass (p*p) S else 0)

/-- Every eligible odd prime gets either the combined source exponent
or the original vertical source exponent, never their product. -/
theorem extended_local_dvd_of_classNumber_one
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    [Fact p.Prime] [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D) (hp2 : p ≠ 2)
    (hsmall : (p : Int) < ((D : Int)+1)/4)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    (p : Int)^(2*extendedOddValuationWeight R S p) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  classical
  by_cases hsel : selectedOddHorizontalPrime p
  · have h := combined_local_mass_dvd_of_classNumber_one
      Q D J R S p hsq hp2 hsmall hc
    simpa [extendedOddValuationWeight, hsel] using h
  · have h := rectangularTraceGram_valuation_of_classNumber_one
      Q D J R S p hsq hp2 hsmall hc
    simpa [extendedOddValuationWeight, hsel] using h

/-- The existing binary exponent and all selected odd exponents divide
one unchanged original integer trace Gram. This is an odd-prime
strengthening, NOT YET the proposed two-sided binary strengthening. -/
theorem extended_original_odd_binary_gram_dvd
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    ((2^binaryNullGramExponent R S *
      ∏ p ∈ oddPrimesBelow R,
        p^(2*extendedOddValuationWeight R S p) : Nat) : Int) ∣
      (integerRectangularTraceGram Q D S R S).det := by
  classical
  let P := oddPrimesBelow R
  have hnot : 2 ∉ P := by simp [P, oddPrimesBelow]
  have hprime : ∀ p ∈ P, p.Prime := by
    intro p hp
    exact (Finset.mem_filter.mp hp).2.1
  have hlocal : ∀ p ∈ P,
      (p : Int)^(2*extendedOddValuationWeight R S p) ∣
        (integerRectangularTraceGram Q D S R S).det := by
    intro p hp
    letI : Fact p.Prime := ⟨hprime p hp⟩
    have hp2 : p ≠ 2 := (Finset.mem_filter.mp hp).2.2
    have hpR : p < R := Finset.mem_range.mp (Finset.mem_filter.mp hp).1
    have hpRi : (p : Int) < R := by exact_mod_cast hpR
    exact extended_local_dvd_of_classNumber_one
      Q D S R S p hsq hp2 (hpRi.trans hRcut) hc
  exact binaryOddLocalProduct_dvd P
    (fun p => 2*extendedOddValuationWeight R S p)
    (binaryNullGramExponent R S)
    (integerRectangularTraceGram Q D S R S).det
    hnot hprime hlocal
    (binaryNull_originalTraceGram_dvd Q D S R S)

/-- Negative control: 2 remains excluded from the odd prime product. -/
theorem two_not_in_odd_product (R : Nat) :
    2 ∉ oddPrimesBelow R := by
  simp [oddPrimesBelow]

end TenthDiscriminant.Phase323

#print axioms TenthDiscriminant.Phase323.extended_original_odd_binary_gram_dvd
