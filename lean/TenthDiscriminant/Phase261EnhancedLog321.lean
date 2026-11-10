import TenthDiscriminant.Phase260EnhancedOriginalGram321
import TenthDiscriminant.BinaryThinLogBridge

/-!
# Phase261: logarithm of the enhanced SAME-original-Gram divisor

The new horizontal p² mass at 3 and 5 is assembled with the existing
vertical mass and binary exponent before taking logarithms.  This file
only takes the logarithm of that SINGLE integer product and preserves
the original positive integer trace-Gram determinant.

The old exact odd mass, the extra 3/5 terms, the 321-domain analytic
upper and the actual-field return are further distinct obligations.
-/

namespace TenthDiscriminant.Phase261
open scoped BigOperators
open TenthDiscriminant.Phase260

/-- A single enhanced odd-prime factor, not a product of overlapping
local certificates for p=3 or p=5. -/
private def enhancedOddFactor (R S : Nat) : Nat :=
  ∏ p ∈ oddPrimesBelow R,
    p^(2*enhancedValuationWeight R S p)

noncomputable def enhancedOddMass (R S : Nat) : Real :=
  ∑ p ∈ oddPrimesBelow R,
    (2*enhancedValuationWeight R S p : Nat)*Real.log (p : Real)

private theorem enhancedOddFactor_pos (R S : Nat) :
    0 < enhancedOddFactor R S := by
  unfold enhancedOddFactor
  apply Finset.prod_pos
  intro p hp
  have hprime : p.Prime := (Finset.mem_filter.mp hp).2.1
  exact pow_pos hprime.pos _

/-- Exact finite logarithm of the improved odd-only product. -/
theorem log_enhancedOddFactor_eq (R S : Nat) :
    Real.log ((enhancedOddFactor R S : Nat) : Real) =
      enhancedOddMass R S := by
  unfold enhancedOddFactor
  simp only [Nat.cast_prod, Nat.cast_pow]
  rw [Real.log_prod]
  · simp only [Real.log_pow, enhancedOddMass]
  · intro p hp
    have hprime : p.Prime := (Finset.mem_filter.mp hp).2.1
    have hpos : (0 : Real) < (p : Real) := by
      exact_mod_cast hprime.pos
    exact (pow_pos hpos _).ne'

/-- Original binary factor plus the enhanced odd product, bounded by
the logarithm of the ONE positive original integer trace Gram.
No separate determinant, jet convention, or extra p=3/5 factor. -/
theorem enhanced_binary_odd_log_of_pos
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4)
    (hdet : 0 < (integerRectangularTraceGram Q D S R S).det) :
    (binaryNullGramExponent R S : Real)*Real.log 2 +
      enhancedOddMass R S ≤
      Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  have hdvd :
      ((2^binaryNullGramExponent R S * enhancedOddFactor R S : Nat) : Int) ∣
        (integerRectangularTraceGram Q D S R S).det := by
    simpa only [enhancedOddFactor] using
      (enhanced_binary_odd_original_gram_dvd Q D R S hsq hc hRcut)
  have hle :
      ((2^binaryNullGramExponent R S * enhancedOddFactor R S : Nat) : Int) ≤
        (integerRectangularTraceGram Q D S R S).det :=
    Int.le_of_dvd hdet hdvd
  have hoddPos : 0 < enhancedOddFactor R S :=
    enhancedOddFactor_pos R S
  have hoddNe : ((enhancedOddFactor R S : Nat) : Real) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hoddPos)
  have hprodNat :
      0 < (2^binaryNullGramExponent R S * enhancedOddFactor R S : Nat) := by
    exact mul_pos
      (pow_pos (by decide : (0 : Nat) < 2) _) hoddPos
  have hprodReal :
      (0 : Real) <
        ((2^binaryNullGramExponent R S * enhancedOddFactor R S : Nat) : Real) := by
    exact_mod_cast hprodNat
  have hcast :
      ((2^binaryNullGramExponent R S * enhancedOddFactor R S : Nat) : Real) ≤
        ((integerRectangularTraceGram Q D S R S).det : Real) := by
    exact_mod_cast hle
  have hlog := Real.log_le_log hprodReal hcast
  have hlogProduct :
      Real.log
        ((2^binaryNullGramExponent R S * enhancedOddFactor R S : Nat) : Real) =
        (binaryNullGramExponent R S : Real)*Real.log 2 +
          enhancedOddMass R S := by
    calc
      Real.log
        ((2^binaryNullGramExponent R S * enhancedOddFactor R S : Nat) : Real) =
          Real.log ((2 : Real)^binaryNullGramExponent R S *
            ((enhancedOddFactor R S : Nat) : Real)) := by
              norm_num
      _ = Real.log ((2 : Real)^binaryNullGramExponent R S) +
            Real.log ((enhancedOddFactor R S : Nat) : Real) := by
              rw [Real.log_mul
                (pow_ne_zero _ (by norm_num : (2 : Real) ≠ 0)) hoddNe]
      _ = (binaryNullGramExponent R S : Real)*Real.log 2 +
            enhancedOddMass R S := by
              rw [Real.log_pow, log_enhancedOddFactor_eq]
  rw [hlogProduct] at hlog
  exact hlog

end TenthDiscriminant.Phase261

#print axioms TenthDiscriminant.Phase261.log_enhancedOddFactor_eq
#print axioms TenthDiscriminant.Phase261.enhanced_binary_odd_log_of_pos
