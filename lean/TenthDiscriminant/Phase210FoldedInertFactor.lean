import TenthDiscriminant.Phase209WholeGramFold
import TenthDiscriminant.InertFrobenius

/-!
# Phase210 — old Frobenius row action on the NEWLY VERIFIED whole-Gram fold

This file joins two ALREADY EXISTING source-exact Lean interfaces:
* RectangularRowAction and RectangularGramFactor prove that the repository's
  original integer basis matrix acts on the original ordinary derivative rows
  and factors the original Gram under nonsquare local Frobenius.
* Phase209WholeGramFold proves that the complete original ellipse trace Gram
  equals the integral conjugate-folded Gram, with weights 2, 4, 4D.

This is an explicit same-matrix composition, not a new p-adic depth theorem.
The additional Phase209 E_p(j) factors and weighted Cauchy-Binet remain OPEN.
-/
namespace TenthDiscriminant.Phase210FoldedInertFactor

open TenthDiscriminant
open TenthDiscriminant.Phase209WholeGramFold

/-- The existing unimodular rectangular binomial basis factors the
FULL conjugate-folded ORIGINAL Gram for any odd inert prime.  The integral
middle matrix is the already-proved normalized ordinary-jet Gram,
not an unrelated surrogate matrix or an assertion about new depth. -/
theorem original_folded_basis_factor_of_inert
    (D rho J R S p : Nat) [Fact p.Prime]
    (hD : 0 < D) (hp2 : p ≠ 2)
    (hinert : ¬ IsSquare (-(D : ZMod p))) :
    ∃ K : Matrix (Fin (R * S)) (Fin (R * S)) Int,
      rectangularBasisMatrix R S p *
          originalFoldedRectangularGram D rho J R S *
          (rectangularBasisMatrix R S p).transpose =
        Matrix.diagonal (fun i => (p : Int) ^
          rectangularBasisExponent R S p i) * K *
        Matrix.diagonal (fun i => (p : Int) ^
          rectangularBasisExponent R S p i) := by
  obtain ⟨K, hK⟩ :=
    rectangularTraceGram_basis_factor_of_frobenius
      (ellipsePairs D rho) D J R S p (Fact.out : p.Prime).pos
      (fun a => integerPair_frobenius_of_nonsquare D p hp2 hinert a)
  refine ⟨K, ?_⟩
  rw [← original_rectangular_gram_folds D rho J R S hD]
  exact hK

/-- The already-counted p^(2F(p)) divisibility applies to the entire
exact folded Gram.  In particular, this does NOT add the unproved
Phase209 derivative-depth bonus to the old Frobenius factor. -/
theorem original_folded_det_valuation_of_inert
    (D rho J R S p : Nat) [Fact p.Prime]
    (hD : 0 < D) (hp2 : p ≠ 2)
    (hinert : ¬ IsSquare (-(D : ZMod p))) :
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (originalFoldedRectangularGram D rho J R S).det := by
  rw [← original_rectangular_gram_folds D rho J R S hD]
  exact rectangularTraceGram_valuation_of_nonsquare
    (ellipsePairs D rho) D J R S p hp2 hinert

end TenthDiscriminant.Phase210FoldedInertFactor

#print axioms TenthDiscriminant.Phase210FoldedInertFactor.original_folded_basis_factor_of_inert
#print axioms TenthDiscriminant.Phase210FoldedInertFactor.original_folded_det_valuation_of_inert
