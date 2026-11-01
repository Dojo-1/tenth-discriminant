import TenthDiscriminant.BinaryNullRowAction
import TenthDiscriminant.BinaryGramGeneric
import TenthDiscriminant.BinaryPrimeMassBridge

/-!
# Unconditional binary lower bound on the SAME original integer trace Gram

This module discharges the earlier explicit hbinary assumption for the
univariate F(Z)=Z^4-Z^2 construction. Original Q, original ordinary-Z
derivative rows, original 2 and 2D trace weights, and field prerequisites
for the old odd-prime mass are unmodified.

The four-generator improvements of the Phase162 paper dossier remain
separate until an equally source-typed matrix proof is available.
-/
namespace TenthDiscriminant

set_option autoImplicit false

/-- Choose an integral quotient for every actual original transformed
jet. Existence comes from the checked polynomial/source row action. -/
noncomputable def binaryNullNormalizedJet (D R S : Nat) :
    Fin (R*S) → Int × Int → Nat → Zsqrtd (-(D : Int)) :=
  fun i a j => Classical.choose
    (binaryNullBasisMatrix_actualRow_dvd D R S i a j)

/-- The original integer jet family, changed ONLY by the explicit
unimodular row matrix, has the required integral quotient jets. -/
theorem binaryNullTransformedJet_scale
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    zsqrtdJetTransform (binaryNullBasisMatrix R S)
      (rectangularCanonicalJet D R S) i a j =
        ((2 : Int)^binaryNullBasisExponent R S i) •
          binaryNullNormalizedJet D R S i a j := by
  have h := Classical.choose_spec
    (binaryNullBasisMatrix_actualRow_dvd D R S i a j)
  simpa only [zsqrtdJetTransform, rectangularCanonicalJet,
    binaryNullNormalizedJet, zsmul_eq_mul, Int.cast_pow,
    Int.cast_natCast] using h

/-- Original row-major indexing repeats r/4 exactly S times.
No information about the observation support Q enters this identity. -/
theorem binaryNullBasisExponent_sum (R S : Nat) :
    (∑ i : Fin (R*S), binaryNullBasisExponent R S i) =
      S * ∑ r ∈ Finset.range R, r/4 := by
  classical
  by_cases hS : S = 0
  · subst S
    simp
  have hSpos : 0 < S := Nat.pos_of_ne_zero hS
  have hlabel (r : Fin R) (s : Fin S) :
      (finProdFinEquiv (r,s)).val / S = r.val := by
    change (s.val + S * r.val) / S = r.val
    rw [Nat.add_mul_div_left _ _ hSpos]
    simp [Nat.div_eq_of_lt s.isLt]
  have he := Fintype.sum_equiv
    (finProdFinEquiv : Fin R × Fin S ≃ Fin (R*S))
    (fun rs => binaryNullBasisExponent R S (finProdFinEquiv rs))
    (binaryNullBasisExponent R S) (fun _ => rfl)
  rw [←he]
  simp only [Fintype.sum_prod_type]
  have hrewrite :
      (∑ r : Fin R, ∑ s : Fin S,
        binaryNullBasisExponent R S (finProdFinEquiv (r,s))) =
      ∑ r : Fin R, ∑ _s : Fin S, r.val / 4 := by
    apply Finset.sum_congr rfl
    intro r hr
    apply Finset.sum_congr rfl
    intro s hs
    simp only [binaryNullBasisExponent, hlabel]
  rw [hrewrite]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin,
    nsmul_eq_mul, ← Finset.mul_sum, Finset.sum_fin_eq_sum_range]
  have hguard :
      (∑ x ∈ Finset.range R, if h : x < R then x / 4 else 0) =
        ∑ x ∈ Finset.range R, x / 4 := by
    apply Finset.sum_congr rfl
    intro x hx
    simp [Finset.mem_range.mp hx]
  rw [hguard]
  simp

/-- An unconditional divisor for the original integer trace Gram.
Positivity is NOT required for divisibility; it is needed only to take
logarithms in the field-level determinant sandwich. -/
theorem binaryNull_originalTraceGram_dvd
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    (2 : Int)^binaryNullGramExponent R S ∣
      (integerRectangularTraceGram Q D J R S).det := by
  have h := binaryGramFactor_dvd_generic Q D J
    (binaryNullBasisMatrix R S)
    (rectangularCanonicalJet D R S)
    (binaryNullNormalizedJet D R S)
    (binaryNullBasisExponent R S)
    (binaryNullBasisMatrix_det R S)
    (by
      intro i a j ha hj
      exact binaryNullTransformedJet_scale D R S i a j)
  have he : R*S + 2*(∑ i : Fin (R*S),
        binaryNullBasisExponent R S i) =
      binaryNullGramExponent R S := by
    rw [binaryNullBasisExponent_sum]
    unfold binaryNullGramExponent
    ring
  rw [he] at h
  simpa only [rectangularCanonicalJet, zsqrtdJetGram_canonical] using h

/-- Under EXACTLY the old field prerequisites, the now-proved binary
power and the checked odd-prime mass multiply by coprimality. -/
theorem originalGram_binary_oddMass_unconditional
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    ((2^binaryNullGramExponent R S *
        ∏ p ∈ oddPrimesBelow R,
          p^(2*valuationWeight R S p) : Nat) : Int) ∣
      (integerRectangularTraceGram Q D S R S).det := by
  exact originalGram_binary_and_odd_mass_dvd Q D R S
    hsq hclass hRcut (binaryNull_originalTraceGram_dvd Q D S R S)

end TenthDiscriminant
