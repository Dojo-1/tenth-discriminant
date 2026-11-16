import TenthDiscriminant.BinaryNullHorizontalRowAction
import TenthDiscriminant.BinaryNullTraceGram
import TenthDiscriminant.Phase228CombinedBasis

/-!
# Phase323-D: horizontal binary factor on the original trace Gram

This module transports the verified horizontal row action through the
existing generic unimodular Gram-factor theorem. It preserves the same
sample set, ordinary-Z jets, trace weights, and integer Gram.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Integral quotient jets for the actual horizontal transformed rows. -/
noncomputable def binaryNullHorizontalNormalizedJet (D R S : Nat) :
    Fin (R*S) → Int × Int → Nat → Zsqrtd (-(D : Int)) :=
  fun i a j => Classical.choose
    (binaryNullHorizontalBasisMatrix_actualRow_dvd D R S i a j)

/-- The horizontal matrix scales every actual original jet by its
certified power of two. -/
theorem binaryNullHorizontalTransformedJet_scale
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    zsqrtdJetTransform (binaryNullHorizontalBasisMatrix R S)
      (rectangularCanonicalJet D R S) i a j =
        ((2 : Int)^binaryNullHorizontalExponent R S i) •
          binaryNullHorizontalNormalizedJet D R S i a j := by
  have h := Classical.choose_spec
    (binaryNullHorizontalBasisMatrix_actualRow_dvd D R S i a j)
  simpa only [zsqrtdJetTransform, rectangularCanonicalJet,
    binaryNullHorizontalNormalizedJet, zsmul_eq_mul, Int.cast_pow,
    Int.cast_natCast] using h

/-- The horizontal exponent is repeated once for each first-coordinate
row: sum_i floor((i mod S)/4) = R * sum_{s<S} floor(s/4). -/
theorem binaryNullHorizontalBasisExponent_sum (R S : Nat) :
    (∑ i : Fin (R*S), binaryNullHorizontalExponent R S i) =
      R * ∑ s ∈ Finset.range S, s/4 := by
  -- Phase228 has already checked the same horizontal row-major
  -- count for an arbitrary p; specialize to p=2 without a new
  -- enumerative argument or any assumptions on the source data.
  simpa [binaryNullHorizontalExponent, Phase228.horizontalBasisExponent] using
    (Phase228.sum_horizontalBasisExponent R S 2)

/-- The horizontal binary-null factor divides the determinant of the
same original integer rectangular trace Gram. -/
theorem binaryNullHorizontal_originalTraceGram_dvd
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    (2 : Int)^(R*S +
      2*(R * ∑ s ∈ Finset.range S, s/4)) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  have h := binaryGramFactor_dvd_generic Q D J
    (binaryNullHorizontalBasisMatrix R S)
    (rectangularCanonicalJet D R S)
    (binaryNullHorizontalNormalizedJet D R S)
    (binaryNullHorizontalExponent R S)
    (binaryNullHorizontalBasisMatrix_det R S)
    (by
      intro i a j ha hj
      exact binaryNullHorizontalTransformedJet_scale D R S i a j)
  have he :
      R*S + 2*(∑ i : Fin (R*S),
        binaryNullHorizontalExponent R S i) =
      R*S + 2*(R * ∑ s ∈ Finset.range S, s/4) := by
    rw [binaryNullHorizontalBasisExponent_sum]
  rw [he] at h
  simpa only [rectangularCanonicalJet, zsqrtdJetGram_canonical] using h

end TenthDiscriminant

#print axioms TenthDiscriminant.binaryNullHorizontal_originalTraceGram_dvd
