import TenthDiscriminant.BinaryNullBidirectionalRowAction
import TenthDiscriminant.BinaryNullHorizontalTraceGram
import TenthDiscriminant.BinaryNullTraceGram

/-!
Phase331: one original integer ordinary-Z-jet trace Gram, one
unimodular composed binary row action, one simultaneous exponent.
This does not imply the proposed field bound without the odd-prime
and analytic normalized-log bridge.
-/
namespace TenthDiscriminant
open scoped BigOperators
set_option autoImplicit false

noncomputable def binaryNullBidirectionalNormalizedJet (D R S : Nat) :
    Fin (R*S) → Int × Int → Nat → Zsqrtd (-(D : Int)) :=
  fun i a j => Classical.choose
    (binaryNullBidirectionalBasisMatrix_actualRow_dvd D R S i a j)

theorem binaryNullBidirectionalTransformedJet_scale
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    zsqrtdJetTransform (binaryNullBidirectionalBasisMatrix R S)
      (rectangularCanonicalJet D R S) i a j =
        ((2 : Int)^binaryNullBidirectionalExponent R S i) •
          binaryNullBidirectionalNormalizedJet D R S i a j := by
  have h := Classical.choose_spec
    (binaryNullBidirectionalBasisMatrix_actualRow_dvd D R S i a j)
  simpa only [zsqrtdJetTransform, rectangularCanonicalJet,
    binaryNullBidirectionalNormalizedJet, zsmul_eq_mul,
    Int.cast_pow, Int.cast_natCast] using h

theorem binaryNullBidirectionalBasisExponent_sum (R S : Nat) :
    (∑ i : Fin (R*S), binaryNullBidirectionalExponent R S i) =
      S*(∑ r ∈ Finset.range R, r/4) +
      R*(∑ s ∈ Finset.range S, s/4) := by
  rw [binaryNullBidirectionalExponent_sum,
    binaryNullBasisExponent_sum,
    binaryNullHorizontalBasisExponent_sum]

/-- Unconditional simultaneous source-exact 2-adic divisor. -/
theorem binaryNullBidirectional_originalTraceGram_dvd
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    (2 : Int)^
      (R*S + 2*(S*(∑ r ∈ Finset.range R, r/4) +
                 R*(∑ s ∈ Finset.range S, s/4))) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  have h := binaryGramFactor_dvd_generic Q D J
    (binaryNullBidirectionalBasisMatrix R S)
    (rectangularCanonicalJet D R S)
    (binaryNullBidirectionalNormalizedJet D R S)
    (binaryNullBidirectionalExponent R S)
    (binaryNullBidirectionalBasisMatrix_det R S)
    (by
      intro i a j ha hj
      exact binaryNullBidirectionalTransformedJet_scale
        D R S i a j)
  have he :
      R*S + 2*(∑ i : Fin (R*S),
        binaryNullBidirectionalExponent R S i) =
      R*S + 2*(S*(∑ r ∈ Finset.range R, r/4) +
               R*(∑ s ∈ Finset.range S, s/4)) := by
    rw [binaryNullBidirectionalBasisExponent_sum]
  rw [he] at h
  simpa only [rectangularCanonicalJet,
    zsqrtdJetGram_canonical] using h

theorem binaryNullBidirectionalExponent_eq_old_add (R S : Nat) :
    R*S + 2*(S*(∑ r ∈ Finset.range R, r/4) +
              R*(∑ s ∈ Finset.range S, s/4)) =
      binaryNullGramExponent R S +
        2*R*(∑ s ∈ Finset.range S, s/4) := by
  unfold binaryNullGramExponent
  ring

end TenthDiscriminant

#print axioms TenthDiscriminant.binaryNullBidirectional_originalTraceGram_dvd
#print axioms TenthDiscriminant.binaryNullBidirectionalExponent_eq_old_add
