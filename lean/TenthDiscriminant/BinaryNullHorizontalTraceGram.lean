import TenthDiscriminant.BinaryNullHorizontalRowAction
import TenthDiscriminant.BinaryNullTraceGram

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
  classical
  by_cases hS : S = 0
  · subst S
    simp
  have hSpos : 0 < S := Nat.pos_of_ne_zero hS
  have hlabel (r : Fin R) (s : Fin S) :
      (finProdFinEquiv (r,s)).val % S = s.val := by
    change (s.val + S*r.val) % S = s.val
    omega
  have he := Fintype.sum_equiv
    (finProdFinEquiv : Fin R × Fin S ≃ Fin (R*S))
    (fun rs => binaryNullHorizontalExponent R S (finProdFinEquiv rs))
    (binaryNullHorizontalExponent R S) (fun _ => rfl)
  rw [← he]
  simp only [Fintype.sum_prod_type]
  have hrewrite :
      (∑ r : Fin R, ∑ s : Fin S,
        binaryNullHorizontalExponent R S (finProdFinEquiv (r,s))) =
      ∑ r : Fin R, ∑ _s : Fin S, s.val / 4 := by
    apply Finset.sum_congr rfl
    intro r hr
    apply Finset.sum_congr rfl
    intro s hs
    simp only [binaryNullHorizontalExponent, hlabel]
  rw [hrewrite]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin,
    nsmul_eq_mul, ← Finset.mul_sum, Finset.sum_fin_eq_sum_range]
  have hguard :
      (∑ x ∈ Finset.range S, if h : x < S then x / 4 else 0) =
        ∑ x ∈ Finset.range S, x / 4 := by
    apply Finset.sum_congr rfl
    intro x hx
    simp [Finset.mem_range.mp hx]
  rw [hguard]
  simp

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
