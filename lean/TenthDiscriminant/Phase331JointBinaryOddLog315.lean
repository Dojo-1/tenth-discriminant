import TenthDiscriminant.Phase331JointBinaryOddProduct315
import TenthDiscriminant.Phase261EnhancedLog321

/-!
Phase331: one original positive integer Gram, one exact binary-plus-odd
prime product, and a corresponding rigorous LOG inequality.

The odd sum includes vertical valuationWeight once for every odd prime
and p^2 horizontal mass once for each selected prime
3,5,7,11,13,17,19,23,29,31,37,41. The binary sum is the verified
simultaneous vertical+horizontal 2-power. No independent binary
determinant divisor is multiplied by another such divisor.

This is a theorem about the original determinant. It does not yet
prove a normalized lower gain or a 315^4 field bound.
-/
namespace TenthDiscriminant.Phase331
open scoped BigOperators
open TenthDiscriminant
open TenthDiscriminant.Phase323
set_option autoImplicit false

private noncomputable def jointOddFactor (R S : Nat) : Nat :=
  ∏ p ∈ oddPrimesBelow R,
    p^(2*extendedOddValuationWeight R S p)

noncomputable def jointOddMass (R S : Nat) : Real :=
  ∑ p ∈ oddPrimesBelow R,
    (2*extendedOddValuationWeight R S p : Nat)*Real.log (p : Real)

private theorem jointOddFactor_pos (R S : Nat) :
    0 < jointOddFactor R S := by
  unfold jointOddFactor
  apply Finset.prod_pos
  intro p hp
  have hprime : p.Prime := (Finset.mem_filter.mp hp).2.1
  exact pow_pos hprime.pos _

theorem log_jointOddFactor_eq (R S : Nat) :
    Real.log ((jointOddFactor R S : Nat) : Real) =
      jointOddMass R S := by
  unfold jointOddFactor
  simp only [Nat.cast_prod, Nat.cast_pow]
  rw [Real.log_prod]
  · simp only [Real.log_pow, jointOddMass]
  · intro p hp
    have hprime : p.Prime := (Finset.mem_filter.mp hp).2.1
    have hpos : (0 : Real) < (p : Real) := by
      exact_mod_cast hprime.pos
    exact (pow_pos hpos _).ne'

/-- The *single* combined source product implies a sound
logarithmic inequality for the same positive original Gram. -/
theorem joint_binary_odd_log_of_pos
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4)
    (hdet : 0 < (integerRectangularTraceGram Q D S R S).det) :
    (jointBinaryGramExponent R S : Real)*Real.log 2 +
      jointOddMass R S ≤
      Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  have hdvd :
      ((2^jointBinaryGramExponent R S * jointOddFactor R S : Nat) : Int) ∣
        (integerRectangularTraceGram Q D S R S).det := by
    simpa only [jointOddFactor] using
      (joint_binary_extended_odd_original_gram_dvd
        Q D R S hsq hc hRcut)
  have hle :
      ((2^jointBinaryGramExponent R S * jointOddFactor R S : Nat) : Int) ≤
        (integerRectangularTraceGram Q D S R S).det :=
    Int.le_of_dvd hdet hdvd
  have hoddPos : 0 < jointOddFactor R S :=
    jointOddFactor_pos R S
  have hoddNe : ((jointOddFactor R S : Nat) : Real) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hoddPos)
  have hprodNat :
      0 < (2^jointBinaryGramExponent R S * jointOddFactor R S : Nat) := by
    exact mul_pos
      (pow_pos (by decide : (0 : Nat) < 2) _) hoddPos
  have hprodReal : (0 : Real) <
      ((2^jointBinaryGramExponent R S * jointOddFactor R S : Nat) : Real) := by
    exact_mod_cast hprodNat
  have hcast :
      ((2^jointBinaryGramExponent R S * jointOddFactor R S : Nat) : Real) ≤
        ((integerRectangularTraceGram Q D S R S).det : Real) := by
    exact_mod_cast hle
  have hlog := Real.log_le_log hprodReal hcast
  have hlogProduct :
      Real.log
        ((2^jointBinaryGramExponent R S * jointOddFactor R S : Nat) : Real) =
        (jointBinaryGramExponent R S : Real)*Real.log 2 +
          jointOddMass R S := by
    calc
      Real.log
        ((2^jointBinaryGramExponent R S * jointOddFactor R S : Nat) : Real) =
          Real.log ((2 : Real)^jointBinaryGramExponent R S *
            ((jointOddFactor R S : Nat) : Real)) := by norm_num
      _ = Real.log ((2 : Real)^jointBinaryGramExponent R S) +
            Real.log ((jointOddFactor R S : Nat) : Real) := by
              rw [Real.log_mul
                (pow_ne_zero _ (by norm_num : (2 : Real) ≠ 0)) hoddNe]
      _ = (jointBinaryGramExponent R S : Real)*Real.log 2 +
            jointOddMass R S := by
              rw [Real.log_pow, log_jointOddFactor_eq]
  rw [hlogProduct] at hlog
  exact hlog

end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.joint_binary_odd_log_of_pos
