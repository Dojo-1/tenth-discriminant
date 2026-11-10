import TenthDiscriminant.Phase210FiniteInertBudget
import TenthDiscriminant.Phase265ThinUpper321

/-!
# Phase268 — class-number-free inert-prime budget at the 321⁴ source floor

This transports the previously checked Phase210 finite-inert-prime
same-original-Gram logarithmic budget from 322⁴ to the independently
proved 321⁴ source positivity and analytic upper. The field class-number
hypothesis does NOT occur in this statement.

For any finite set of distinct odd primes nonsquare modulo -D, the
OLD vertical Frobenius mass is bounded by the analytic upper on the
SAME original thin-ellipse integer ordinary-Z-jet trace Gram.

This does not infer inertness for arbitrary quadratic characters, does
not import a zero-dependent prime-bias lower bound, and does not prove
a Landau–Siegel-zero-free region. It also does not include the separate
horizontal p=3,5 bonus: that would require a new class-number-free
enhanced finite-prime product theorem, not informal double counting.
-/
namespace TenthDiscriminant.Phase268FiniteInertBudget321

open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- For EVERY finite set of odd inert primes, its already-counted
vertical Frobenius valuation mass fits under the original positive
thin trace-Gram upper at the sharper 321⁴ domain. No class-number-one
assumption and no external zero estimate is used. -/
theorem thin_inert_mass_budget_321
    (D : Nat) (hD : (321 : Nat)^4 ≤ D) (P : Finset Nat)
    (hprime : ∀ p ∈ P, p.Prime)
    (hodd : ∀ p ∈ P, p ≠ 2)
    (hinert : ∀ p ∈ P, ¬ IsSquare (-(D : ZMod p))) :
    (∑ p ∈ P,
      ((2 * valuationWeight (Tuned.R D) (Tuned.S D) p : Nat) : Real) *
        Real.log (p : Real)) /
      comparisonScale (Tuned.R D) (Tuned.S D) ≤
      (4/5 : Real) * Real.log D - 1853/2000 := by
  have hdim := Tuned.dimensions_321 D hD
  have hscale := comparisonScale_pos
    (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hmass := Phase210FiniteInertBudget.finite_inert_mass_le_original_log
    P D (Tuned.thinRadius D) (Tuned.S D)
    (Tuned.R D) (Tuned.S D)
    (Tuned.thin_original_gram_pos_321 D hD)
    hprime hodd hinert
  exact (div_le_div_of_nonneg_right hmass hscale.le).trans
    (ThinUpper321.thin_production_normalized_upper_321 D hD)

end
end TenthDiscriminant.Phase268FiniteInertBudget321

#print axioms TenthDiscriminant.Phase268FiniteInertBudget321.thin_inert_mass_budget_321
