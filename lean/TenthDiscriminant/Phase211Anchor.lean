import TenthDiscriminant.Phase210SharpOrdinaryJet
import TenthDiscriminant.RectangularGramFactor
import TenthDiscriminant.RectangularRowAction

/-!
# Phase211: normalize the actual ninth ordinary-jet row (p=3)

This is a source-specific equality, not an alternative matrix.
We reuse the *existing* rectangularNormalizedJet, whose
definition is the integral quotient chosen from the actual
rectangularBasisMatrix row action.

The anchor is the original row (r,s)=(9,0) in the rectangle
R=S=10 and the ninth ordinary derivative (W frozen).  Its old
Frobenius row exponent is 3; 362880 = 3^3*13440.
All a : Int x Int are covered under the existing global
Frobenius-congruence premise that makes the chosen quotient available.
-/

namespace TenthDiscriminant.Phase211Anchor

open TenthDiscriminant

theorem transformed_ninth_source_exact (D : Nat) (a : Int × Int) :
    zsqrtdJetTransform (rectangularBasisMatrix 10 10 3)
      (rectangularCanonicalJet D 10 10)
      (⟨90, by decide⟩ : Fin (10 * 10)) a 9 =
        (362880 : Zsqrtd (-(D : Int))) := by
  unfold zsqrtdJetTransform rectangularCanonicalJet
  rw [rectangularBasisMatrix_row_action 10 10 3 (by decide)
    (⟨90, by decide⟩ : Fin (10 * 10))
    (fun h : Fin (10 * 10) =>
      pairZsqrtdEquiv D
        (integerDerivativeRow D (h.val / 10) (h.val % 10) 9 a))]
  norm_num [rectangularBasisExponent, rectangularBasisTargetFin,
    rectangularBasisTarget, integerDerivativeRow,
    pairScale, pairMul, pairPow, pairConj, pairZsqrtdEquiv,
    Finset.sum_range_succ, Nat.descFactorial]

/-- The *actual* choice of integral normalized original jet is the
integer 13440, not merely a hypothetical quotient polynomial.
Both Zsqrtd integer coordinates are determined by cancellation.
This theorem is uniform in every original integer-pair sample a. -/
theorem actual_normalized_ninth_jet
    (D : Nat)
    (hzero : ∀ a : Int × Int,
      (3 : Int) ∣ (pairPow D a 3).1 - (pairConj a).1 ∧
      (3 : Int) ∣ (pairPow D a 3).2 - (pairConj a).2)
    (a : Int × Int) :
    rectangularNormalizedJet D 10 10 3 (by decide) hzero
      (⟨90, by decide⟩ : Fin (10 * 10)) a 9 =
      (⟨13440, 0⟩ : Zsqrtd (-(D : Int))) := by
  have hscale := rectangularTransformedJet_scale
    D 10 10 3 (by decide) hzero
    (⟨90, by decide⟩ : Fin (10 * 10)) a 9
  rw [transformed_ninth_source_exact D a,
    Phase210SharpOrdinaryJet.originalP3Nine_basis_weight] at hscale
  apply Zsqrtd.ext
  · have hre := congrArg Zsqrtd.re hscale
    norm_num [zsmul_eq_mul] at hre ⊢
    omega
  · have him := congrArg Zsqrtd.im hscale
    norm_num [zsmul_eq_mul] at him ⊢
    omega

end TenthDiscriminant.Phase211Anchor

#print axioms TenthDiscriminant.Phase211Anchor.transformed_ninth_source_exact
#print axioms TenthDiscriminant.Phase211Anchor.actual_normalized_ninth_jet
