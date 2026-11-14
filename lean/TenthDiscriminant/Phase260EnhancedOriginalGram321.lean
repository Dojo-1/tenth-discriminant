import TenthDiscriminant.Phase259Horizontal321
import TenthDiscriminant.BinaryNullTraceGram
import TenthDiscriminant.BinaryPrimeMassBridge
import TenthDiscriminant.ClassNumberInertBridge

/-!
# Phase260: one original Gram, one exponent per odd prime

The Phase228 combined unimodular source frame supplies BOTH old vertical
and new horizontal Frobenius row exponents at an inert prime.  Class
number one supplies inertness for each strict small odd prime.  The
result below assembles a SINGLE odd-prime product, with an extra
horizontal exponent only at p=3 and p=5, and multiplies it by the
separately proved 2-primary divisor using the existing coprime assembly.

No analytic upper, numerical field cutoff, or independent prime
multiplicity is asserted here.  In particular the original Gram, Q,
ordinary jets, and binary factor are not replaced.
-/

namespace TenthDiscriminant.Phase260
open scoped BigOperators
open TenthDiscriminant.Phase228
open TenthDiscriminant.Phase259

/-- Exact local class-number-one divisor from the SAME combined source
frame, including both row weights.  The old weight is counted once. -/
theorem combined_local_mass_dvd_of_classNumber_one
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    [Fact p.Prime] [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D) (hp2 : p ≠ 2)
    (hsmall : (p : Int) < ((D : Int)+1)/4)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    (p : Int)^(2*(valuationWeight R S p+R*floorMass (p*p) S)) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  have hns := smallPrime_nonsquare_of_classNumber_one
    D p hsq hp2 hsmall hc
  have hraw := combinedTraceGram_valuation_of_inert
    Q D J R S p hp2 hns
  have hsum :
      (∑ i : Fin (R*S),
        (rectangularBasisExponent R S p i+
          horizontalBasisExponent R S p i)) =
        valuationWeight R S p+R*floorMass (p*p) S := by
    rw [Finset.sum_add_distrib, sum_rectangularBasisExponent,
      sum_horizontalBasisExponent]
    rfl
  simpa only [hsum] using hraw

/-- One exponent for each odd prime, with horizontal mass only at 3,5.
This is NOT a product of the old and new local certificates. -/
def enhancedValuationWeight (R S p : Nat) : Nat :=
  valuationWeight R S p +
    (if p = 3 then R*floorMass 9 S
     else if p = 5 then R*floorMass 25 S
     else 0)

theorem enhancedValuationWeight_three (R S : Nat) :
    enhancedValuationWeight R S 3 =
      valuationWeight R S 3+R*floorMass 9 S := by
  simp [enhancedValuationWeight]

theorem enhancedValuationWeight_five (R S : Nat) :
    enhancedValuationWeight R S 5 =
      valuationWeight R S 5+R*floorMass 25 S := by
  simp [enhancedValuationWeight]

theorem enhancedValuationWeight_other (R S p : Nat)
    (hp3 : p ≠ 3) (hp5 : p ≠ 5) :
    enhancedValuationWeight R S p = valuationWeight R S p := by
  simp [enhancedValuationWeight, hp3, hp5]

/-- All local odd factors divide the original determinant, with exactly
the combined (vertical + horizontal) source factor at p=3,5. -/
theorem enhanced_local_mass_dvd_of_classNumber_one
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    [Fact p.Prime] [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D) (hp2 : p ≠ 2)
    (hsmall : (p : Int) < ((D : Int)+1)/4)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    (p : Int)^(2*enhancedValuationWeight R S p) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  by_cases hp3 : p = 3
  · subst p
    have h := combined_local_mass_dvd_of_classNumber_one
      Q D J R S 3 hsq hp2 hsmall hc
    simpa [enhancedValuationWeight] using h
  by_cases hp5 : p = 5
  · subst p
    have h := combined_local_mass_dvd_of_classNumber_one
      Q D J R S 5 hsq hp2 hsmall hc
    simpa [enhancedValuationWeight] using h
  · have h := rectangularTraceGram_valuation_of_classNumber_one
      Q D J R S p hsq hp2 hsmall hc
    simpa [enhancedValuationWeight, hp3, hp5] using h

/-- SOURCE-EXACT GLOBAL PRODUCT on ONE original integer ordinary-jet
trace Gram.  The 2-primary factor is included ONCE and the odd primes
are assembled ONCE with their enhanced per-prime exponents. -/
theorem enhanced_binary_odd_original_gram_dvd
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    ((2^binaryNullGramExponent R S *
        ∏ p ∈ oddPrimesBelow R,
          p^(2*enhancedValuationWeight R S p) : Nat) : Int) ∣
      (integerRectangularTraceGram Q D S R S).det := by
  classical
  let P := oddPrimesBelow R
  have hnot : 2 ∉ P := by simp [P, oddPrimesBelow]
  have hprime : ∀ p ∈ P, p.Prime := by
    intro p hp
    exact (Finset.mem_filter.mp hp).2.1
  have hlocal : ∀ p ∈ P,
      (p : Int)^(2*enhancedValuationWeight R S p) ∣
        (integerRectangularTraceGram Q D S R S).det := by
    intro p hp
    letI : Fact p.Prime := ⟨hprime p hp⟩
    have hp2 : p ≠ 2 := (Finset.mem_filter.mp hp).2.2
    have hpR : p < R :=
      Finset.mem_range.mp (Finset.mem_filter.mp hp).1
    have hpRi : (p : Int) < R := by exact_mod_cast hpR
    exact enhanced_local_mass_dvd_of_classNumber_one
      Q D S R S p hsq hp2 (hpRi.trans hRcut) hc
  exact binaryOddLocalProduct_dvd P
    (fun p => 2*enhancedValuationWeight R S p)
    (binaryNullGramExponent R S)
    (integerRectangularTraceGram Q D S R S).det
    hnot hprime hlocal
    (binaryNull_originalTraceGram_dvd Q D S R S)

/-- Negative guard: 2 must never be included in the odd-prime product. -/
theorem binary_not_in_oddPrimesBelow (R : Nat) :
    2 ∉ oddPrimesBelow R := by
  simp [oddPrimesBelow]

end TenthDiscriminant.Phase260

#print axioms TenthDiscriminant.Phase260.combined_local_mass_dvd_of_classNumber_one
#print axioms TenthDiscriminant.Phase260.enhanced_local_mass_dvd_of_classNumber_one
#print axioms TenthDiscriminant.Phase260.enhanced_binary_odd_original_gram_dvd
