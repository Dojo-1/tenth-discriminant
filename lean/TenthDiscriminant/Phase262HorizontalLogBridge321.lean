import TenthDiscriminant.Phase261EnhancedLog321
import TenthDiscriminant.Phase200Scalar322

/-!
# Phase262: no-double-counted horizontal log gain on the original Gram

The single enhanced odd-prime product is split into the PRE-EXISTING
exactOddPrimeMass plus exactly one p² horizontal row-mass contribution
at each of 3 and 5.  The proven rational lower log bounds for these
two primes turn this into the Phase259 horizontalPrimeMass/500.

This is a source-exact determinant LOG lower theorem on arbitrary
original Q with a positive Gram, not a 321⁴ analytic upper or field
exclusion.  No external classification or new observation matrix.
-/

namespace TenthDiscriminant.Phase262
open scoped BigOperators
open TenthDiscriminant.Phase259
open TenthDiscriminant.Phase260
open TenthDiscriminant.Phase261

/-- Both horizontal primes are members of the original odd-prime
family when R>=6; otherwise the extra-mass identity is not asserted. -/
private theorem three_mem_oddPrimesBelow (R : Nat) (hR : 6 ≤ R) :
    3 ∈ oddPrimesBelow R := by
  have h3 : 3 < R := by omega
  simp [oddPrimesBelow, h3, show Nat.Prime 3 by decide]

private theorem five_mem_oddPrimesBelow (R : Nat) (hR : 6 ≤ R) :
    5 ∈ oddPrimesBelow R := by
  have h5 : 5 < R := by omega
  simp [oddPrimesBelow, h5, show Nat.Prime 5 by decide]

/-- The exact finite-log splitting: no horizontal term is counted
at any prime other than 3 or 5, and each old valuation remains once. -/
theorem enhancedOddMass_eq_old_plus (R S : Nat) (hR : 6 ≤ R) :
    enhancedOddMass R S =
      exactOddPrimeMass R S +
        (2*R*floorMass 9 S : Nat)*Real.log 3 +
        (2*R*floorMass 25 S : Nat)*Real.log 5 := by
  classical
  let a : Real := (2*R*floorMass 9 S : Nat)*Real.log 3
  let b : Real := (2*R*floorMass 25 S : Nat)*Real.log 5
  have h3 := three_mem_oddPrimesBelow R hR
  have h5 := five_mem_oddPrimesBelow R hR
  have hpoint (p : Nat) :
      (2*enhancedValuationWeight R S p : Nat)*Real.log (p : Real) =
        (2*valuationWeight R S p : Nat)*Real.log (p : Real) +
        (if p = 3 then a else 0) +
        (if p = 5 then b else 0) := by
    by_cases hp3 : p = 3
    · subst p
      simp [enhancedValuationWeight, a, b, Nat.mul_add,
        Nat.cast_add, Nat.cast_mul, add_mul]
      <;> ring
      all_goals simp
    by_cases hp5 : p = 5
    · subst p
      simp [enhancedValuationWeight, a, b, Nat.mul_add,
        Nat.cast_add, Nat.cast_mul, add_mul]
      <;> ring
      all_goals simp
    · simp [enhancedValuationWeight, hp3, hp5]
  have hsum3 :
      (∑ p ∈ oddPrimesBelow R, if p = 3 then a else 0) = a := by
    rw [Finset.sum_eq_single 3]
    · simp
    · intro p hp hp3
      simp [hp3]
    · intro hnot
      exact False.elim (hnot h3)
  have hsum5 :
      (∑ p ∈ oddPrimesBelow R, if p = 5 then b else 0) = b := by
    rw [Finset.sum_eq_single 5]
    · simp
    · intro p hp hp5
      simp [hp5]
    · intro hnot
      exact False.elim (hnot h5)
  calc
    enhancedOddMass R S =
        (∑ p ∈ oddPrimesBelow R,
          (2*valuationWeight R S p : Nat)*Real.log (p : Real)) +
        (∑ p ∈ oddPrimesBelow R, if p = 3 then a else 0) +
        (∑ p ∈ oddPrimesBelow R, if p = 5 then b else 0) := by
      unfold enhancedOddMass
      simp_rw [hpoint]
      rw [Finset.sum_add_distrib, Finset.sum_add_distrib]
    _ = exactOddPrimeMass R S +
          (2*R*floorMass 9 S : Nat)*Real.log 3 +
          (2*R*floorMass 25 S : Nat)*Real.log 5 := by
      rw [hsum3, hsum5]
      rfl

/-- The EXACT additional logarithmic mass dominates the rational
horizontalPrimeMass/500, using source-checked prime log enclosures. -/
theorem enhancedOddMass_ge_old_plus_horizontal
    (R S : Nat) (hR : 6 ≤ R) :
    exactOddPrimeMass R S +
      (horizontalPrimeMass R S : Real)/500 ≤ enhancedOddMass R S := by
  have h3 : (1098/1000 : Real) ≤ Real.log 3 :=
    TenthDiscriminant.log_three_lower_1098
  have h5 : (1609/1000 : Real) ≤ Real.log 5 :=
    TenthDiscriminant.log_five_lower_1609
  have h3mul := mul_le_mul_of_nonneg_left h3
    (show (0 : Real) ≤ (2*R*floorMass 9 S : Nat) by positivity)
  have h5mul := mul_le_mul_of_nonneg_left h5
    (show (0 : Real) ≤ (2*R*floorMass 25 S : Nat) by positivity)
  have hmass :
      (horizontalPrimeMass R S : Real)/500 ≤
        (2*R*floorMass 9 S : Nat)*Real.log 3 +
        (2*R*floorMass 25 S : Nat)*Real.log 5 := by
    rw [horizontalPrimeMass_eq]
    calc
      ((R*(1098*floorMass 9 S+1609*floorMass 25 S) : Nat) : Real)/500 =
          (2*R*floorMass 9 S : Nat)*(1098/1000 : Real) +
          (2*R*floorMass 25 S : Nat)*(1609/1000 : Real) := by
        push_cast
        ring
      _ ≤ _ := add_le_add h3mul h5mul
  rw [enhancedOddMass_eq_old_plus R S hR]
  simpa only [add_assoc] using
    (add_le_add_left hmass (exactOddPrimeMass R S))

/-- Original source determinant: the old exact odd mass and the new
horizontal mass are both paid by ONE integer determinant, with the
original binary exponent counted exactly once. -/
theorem original_binary_odd_plus_horizontal_log_of_pos
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4)
    (hR : 6 ≤ R)
    (hdet : 0 < (integerRectangularTraceGram Q D S R S).det) :
    (binaryNullGramExponent R S : Real)*Real.log 2 +
      exactOddPrimeMass R S +
      (horizontalPrimeMass R S : Real)/500 ≤
        Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  have hlog := enhanced_binary_odd_log_of_pos
    Q D R S hsq hc hRcut hdet
  have hmass := enhancedOddMass_ge_old_plus_horizontal R S hR
  linarith

end TenthDiscriminant.Phase262

#print axioms TenthDiscriminant.Phase262.enhancedOddMass_eq_old_plus
#print axioms TenthDiscriminant.Phase262.enhancedOddMass_ge_old_plus_horizontal
#print axioms TenthDiscriminant.Phase262.original_binary_odd_plus_horizontal_log_of_pos
