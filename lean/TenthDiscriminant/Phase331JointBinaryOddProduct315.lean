import TenthDiscriminant.BinaryNullBidirectionalTraceGram
import TenthDiscriminant.Phase323OddPrimeProduct

/-!
# Phase331 joint binary plus selected odd primes on one original Gram

The Phase331 simultaneous binary determinant divisor is combined
with the old odd-prime local construction by genuine coprimality:
the 2-primary exponent occurs ONCE; for every odd prime its vertical
part occurs ONCE and its horizontal part occurs at most ONCE.

No second Gram, conjugate jet, source sample, metric, or determinant
is introduced. The original rectangular ordinary-Z-jet trace Gram
of the 315^4 program remains the sole integer target.
-/
namespace TenthDiscriminant.Phase331
open scoped BigOperators Classical
open TenthDiscriminant
open TenthDiscriminant.Phase323
set_option autoImplicit false

/-- Simultaneous vertical and horizontal binary null exponents, with
one original trace factor. -/
def jointBinaryGramExponent (R S : Nat) : Nat :=
    R*S + 2*(S*(∑ r ∈ Finset.range R, r/4) +
               R*(∑ s ∈ Finset.range S, s/4))

/-- Under the exact Phase323 class-number-one/inertness premises,
the full binary and selected odd primes divide ONE unchanged source
determinant. This uses the newly proved original-jet joint 2-power,
not the previously independent horizontal binary divisor. -/
theorem joint_binary_extended_odd_original_gram_dvd
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    ((2^jointBinaryGramExponent R S *
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
    (jointBinaryGramExponent R S)
    (integerRectangularTraceGram Q D S R S).det
    hnot hprime hlocal
    (by
      simpa only [jointBinaryGramExponent] using
        (binaryNullBidirectional_originalTraceGram_dvd Q D S R S))

/-- The old binary exponent is accounted for ONCE; exactly one
horizontal 2-adic row exponent is newly added. -/
theorem jointBinaryGramExponent_eq_old_add (R S : Nat) :
    jointBinaryGramExponent R S =
      binaryNullGramExponent R S +
        2*R*(∑ s ∈ Finset.range S, s/4) := by
  exact binaryNullBidirectionalExponent_eq_old_add R S

end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.joint_binary_extended_odd_original_gram_dvd
