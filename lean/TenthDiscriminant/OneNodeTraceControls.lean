import TenthDiscriminant.BinaryExponentNormalization

/-!
# Phase167 — One-node and empty-support controls on the original trace Gram

These are direct, small, kernel-reducible computations on the ORIGINAL
integer ordinary-Z-derivative matrix, not a stand-in Hasse jet or a new
Gram convention. In the one-dimensional monomial space R=S=J=1, the
single row is the constant polynomial 1 and its trace weight is 2.

D=7 is a concrete small radicand. This file does not need the
large-D geometry or a field-level class-number-one assumption.
-/

namespace TenthDiscriminant.OneNodeTraceControls
set_option autoImplicit false
set_option maxRecDepth 4096
set_option maxHeartbeats 400000

private def originQ : Finset (Int × Int) := {(0, 0)}
private def translatedQ : Finset (Int × Int) := {(1, 0)}
private def twoQ : Finset (Int × Int) := {(0, 0), (1, 0)}

/-- A constant ordinary jet evaluated at the original integer source
point yields trace pairing 2*(1*1 + 7*0*0)=2. -/
theorem origin_single_node_gram_det :
    (integerRectangularTraceGram originQ 7 1 1 1).det = 2 := by
  decide

/-- Translating the sample does not alter the constant one-row Gram:
a minimal representation-invariance check, NOT a general invariance claim. -/
theorem translated_single_node_gram_det :
    (integerRectangularTraceGram translatedQ 7 1 1 1).det = 2 := by
  decide

/-- Two distinct samples add their trace weights in this 1x1 case.
The determinant becomes 4, not 2: distinct supports are NOT identical. -/
theorem two_node_gram_det :
    (integerRectangularTraceGram twoQ 7 1 1 1).det = 4 := by
  decide

/-- With no samples the trace Gram is zero. One must supply positivity
explicitly before taking a logarithm; it cannot be inferred for any Q. -/
theorem empty_node_gram_det :
    (integerRectangularTraceGram (∅ : Finset (Int × Int)) 7 1 1 1).det = 0 := by
  decide

/-- For R=S=1 the old univariate binary exponent is exactly one. -/
theorem binary_exponent_one_by_one :
    binaryNullGramExponent 1 1 = 1 := by
  decide

/-- There are no odd primes below R=1: the product is empty, not zero. -/
theorem no_odd_primes_below_one :
    oddPrimesBelow 1 = ∅ := by
  decide

/-- A nonvacuous exact tiny instance of the *numerical* log identity.
Only the original explicit integer source Gram is used; no field
class-number-one theorem or large-D hypothesis is silently assumed. -/
theorem original_one_node_log_equality :
    (binaryNullGramExponent 1 1 : Real) * Real.log 2 +
      exactOddPrimeMass 1 1 =
      Real.log ((integerRectangularTraceGram originQ 7 1 1 1).det : Real) := by
  rw [binary_exponent_one_by_one, origin_single_node_gram_det]
  simp [exactOddPrimeMass, no_odd_primes_below_one]

end TenthDiscriminant.OneNodeTraceControls
