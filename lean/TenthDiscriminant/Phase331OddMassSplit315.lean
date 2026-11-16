import TenthDiscriminant.Phase331JointBinaryOddLog315
import TenthDiscriminant.Phase262HorizontalLogBridge321
import TenthDiscriminant.Phase331OddTenNormalizedGain315

/-!
# Phase331: no-double-counting finite ray/Frobenius mass split

The original combined odd-prime exponent is exactly the already
certified p=3,5 enhanced valuation, plus ONE additional p²
horizontal term for each selected prime 7,...,41.
This is a theorem about the ONE original Gram product, not
independent multiplication of two local factors at a fixed prime.

The pairwise selected-prime contribution is controlled by the
already checked uniform log p >= 189/100.
-/
namespace TenthDiscriminant.Phase331
open scoped BigOperators
open TenthDiscriminant
open TenthDiscriminant.Phase323
open TenthDiscriminant.Phase259
open TenthDiscriminant.Phase261
set_option autoImplicit false
noncomputable section

/-- The extended valuation is the old enhanced 3/5 valuation,
plus one horizontal source weight for the ten additional primes. -/
theorem extendedOddValuationWeight_refines (R S p : Nat) :
    extendedOddValuationWeight R S p =
      enhancedValuationWeight R S p +
        (if p ∈ oddHorizontalPrimes then R*floorMass (p*p) S else 0) := by
  classical
  by_cases hp3 : p = 3
  · subst p
    simp [extendedOddValuationWeight, enhancedValuationWeight,
      selectedOddHorizontalPrime, oddHorizontalPrimes]
  by_cases hp5 : p = 5
  · subst p
    simp [extendedOddValuationWeight, enhancedValuationWeight,
      selectedOddHorizontalPrime, oddHorizontalPrimes]
  by_cases hten : p ∈ oddHorizontalPrimes
  · simp [extendedOddValuationWeight, enhancedValuationWeight,
      selectedOddHorizontalPrime, hp3, hp5, hten]
  · simp [extendedOddValuationWeight, enhancedValuationWeight,
      selectedOddHorizontalPrime, hp3, hp5, hten]

/-- All ten primes are strictly below R when R >= 42,
and hence belong to the SAME source odd-prime product. -/
theorem tenPrimes_subset_oddPrimesBelow (R : Nat) (hR : 42 ≤ R) :
    oddHorizontalPrimes ⊆ oddPrimesBelow R := by
  intro p hp
  have hprimes : p = 7 ∨ p = 11 ∨ p = 13 ∨ p = 17 ∨
      p = 19 ∨ p = 23 ∨ p = 29 ∨ p = 31 ∨ p = 37 ∨ p = 41 := by
    simpa [oddHorizontalPrimes] using hp
  have hpbound : p < R := by omega
  have hp2 : p ≠ 2 := by omega
  have hpprime : p.Prime := by
    rcases hprimes with rfl | rfl | rfl | rfl | rfl |
      rfl | rfl | rfl | rfl | rfl
    all_goals norm_num
  simp [oddPrimesBelow, hpbound, hpprime, hp2]

/-- Every exact source prime weight differs from the p=3,5 enhanced
mass by only the single ten-prime extra term. -/
theorem jointOddMass_point_split (R S p : Nat) :
    (2*extendedOddValuationWeight R S p : Nat)*
        Real.log (p : Real) =
    (2*enhancedValuationWeight R S p : Nat)*
        Real.log (p : Real) +
      (if p ∈ oddHorizontalPrimes then
        (2*R*floorMass (p*p) S : Nat)*Real.log (p : Real)
       else 0) := by
  classical
  rw [extendedOddValuationWeight_refines]
  by_cases hten : p ∈ oddHorizontalPrimes
  · simp only [if_pos hten, Nat.mul_add, Nat.cast_add, Nat.cast_mul]
    ring
  · simp [hten]

/-- Exact finite sum identity for the original odd-prime source
factor, using a subset of the SAME original oddPrimesBelow R. -/
theorem jointOddMass_eq_enhanced_plus_ten
    (R S : Nat) (hR : 42 ≤ R) :
    jointOddMass R S =
      enhancedOddMass R S +
        ∑ p ∈ oddHorizontalPrimes,
          (2*R*floorMass (p*p) S : Nat)*Real.log (p : Real) := by
  classical
  let f : Nat → Real := fun p =>
    (2*R*floorMass (p*p) S : Nat)*Real.log (p : Real)
  have hsubset := tenPrimes_subset_oddPrimesBelow R hR
  have hfin :
      (∑ p ∈ oddPrimesBelow R,
          if p ∈ oddHorizontalPrimes then f p else 0) =
        ∑ p ∈ oddHorizontalPrimes, f p := by
    have hsub :
        (∑ p ∈ oddHorizontalPrimes,
            if p ∈ oddHorizontalPrimes then f p else 0) =
        (∑ p ∈ oddPrimesBelow R,
            if p ∈ oddHorizontalPrimes then f p else 0) := by
      apply Finset.sum_subset hsubset
      intro p hpold hpnot
      simp [hpnot]
    calc
      _ = ∑ p ∈ oddHorizontalPrimes,
            if p ∈ oddHorizontalPrimes then f p else 0 := hsub.symm
      _ = ∑ p ∈ oddHorizontalPrimes, f p := by
        apply Finset.sum_congr rfl
        intro p hp
        simp [hp]
  calc
    jointOddMass R S =
      ∑ p ∈ oddPrimesBelow R,
        ((2*enhancedValuationWeight R S p : Nat)*
          Real.log (p : Real) +
          (if p ∈ oddHorizontalPrimes then f p else 0)) := by
            unfold jointOddMass
            apply Finset.sum_congr rfl
            intro p hp
            exact jointOddMass_point_split R S p
    _ = enhancedOddMass R S +
        ∑ p ∈ oddPrimesBelow R,
          if p ∈ oddHorizontalPrimes then f p else 0 := by
            rw [Finset.sum_add_distrib]
            rfl
    _ = enhancedOddMass R S + ∑ p ∈ oddHorizontalPrimes, f p := by
      rw [hfin]
    _ = _ := rfl

/-- Every new p² term pays at least the uniform 1.89 log. The
second coefficient is precisely the one used by the ten-prime
normalized integer rounding certificate. -/
theorem ten_prime_real_mass_lower (R S : Nat) :
    ((2*R*(∑ p ∈ oddHorizontalPrimes,
         floorMass (p*p) S) : Nat) : Real)*(189/100 : Real) ≤
      ∑ p ∈ oddHorizontalPrimes,
        (2*R*floorMass (p*p) S : Nat)*Real.log (p : Real) := by
  have hsum : (∑ p ∈ oddHorizontalPrimes,
        ((2*R*floorMass (p*p) S : Nat) : Real)*(189/100 : Real)) ≤
      ∑ p ∈ oddHorizontalPrimes,
        (2*R*floorMass (p*p) S : Nat)*Real.log (p : Real) := by
    apply Finset.sum_le_sum
    intro p hp
    exact mul_le_mul_of_nonneg_left
      (oddHorizontalPrime_log_lower p hp)
      (Nat.cast_nonneg _)
  have hfactor :
      (∑ p ∈ oddHorizontalPrimes,
        ((2*R*floorMass (p*p) S : Nat) : Real)*(189/100 : Real)) =
      ((2*R*(∑ p ∈ oddHorizontalPrimes,
        floorMass (p*p) S) : Nat) : Real)*(189/100 : Real) := by
    push_cast
    rw [Finset.sum_mul]
    rw [← Finset.mul_sum]
    ring
  rw [hfactor] at hsum
  exact hsum

/-- Source-exact payoff: the proved ten-prime mass is paid ONCE by
the joint odd product, in addition to already-proved old recovered
mass plus its p=3,5 horizontal contribution. -/
theorem jointOddMass_ge_old_plus_three_five_and_ten
    (R S : Nat) (hR : 42 ≤ R) :
    exactOddPrimeMass R S +
      (horizontalPrimeMass R S : Real)/500 +
      ((2*R*(∑ p ∈ oddHorizontalPrimes,
        floorMass (p*p) S) : Nat) : Real)*(189/100 : Real) ≤
      jointOddMass R S := by
  have h35 := TenthDiscriminant.Phase262.enhancedOddMass_ge_old_plus_horizontal
    R S (by omega)
  have hten := ten_prime_real_mass_lower R S
  rw [jointOddMass_eq_enhanced_plus_ten R S hR]
  linarith

end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.jointOddMass_ge_old_plus_three_five_and_ten
