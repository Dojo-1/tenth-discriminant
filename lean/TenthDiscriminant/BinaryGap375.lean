import TenthDiscriminant.Log375Certificate
import TenthDiscriminant.BinaryExponentNormalization
import TenthDiscriminant.NormalizedComparison

/-!
# Phase173: source-exact binary quarter and conditional scalar separation

This is an algebraic interface for a future SAME-original-Gram proof.
The 2-adic exponent is the existing binaryNullGramExponent, not an
additional auxiliary prime. Nothing here establishes a log-det upper
at 375^4, positivity for an ellipse, or a smaller field bound.
-/
namespace TenthDiscriminant
open FirstCertificate
set_option autoImplicit false
noncomputable section

/-- The ALREADY proven binary exponent gives log(2)/4 after dividing
by the positive original comparison scale R^2*S. No asymptotic limit. -/
theorem normalized_binary_quarter (R S : Nat)
    (hR : 0 < R) (hS : 0 < S) :
    Real.log 2 / 4 ≤
      (binaryNullGramExponent R S : Real) * Real.log 2 /
        comparisonScale R S := by
  have hp := comparisonScale_pos R S hR hS
  have hn := binaryNullGramExponent_quarter_lower R S
  have hc : ((S*R^2 : Nat) : Real) ≤
      ((4*binaryNullGramExponent R S : Nat) : Real) := by
    exact_mod_cast hn
  have hscale : comparisonScale R S ≤
      4*(binaryNullGramExponent R S : Real) := by
    unfold comparisonScale
    push_cast at hc
    nlinarith only [hc]
  have hlog := mul_le_mul_of_nonneg_right hscale
    (Real.log_nonneg (by norm_num : (1 : Real) ≤ 2))
  apply (le_div_iff₀ hp).2
  nlinarith only [hlog]

/-- Pure rational buffer between the OLD affine expressions when the
NEW 23.7 log floor is available. It makes NO claim that the old
lower and upper envelopes already hold at D >= 375^4. -/
theorem affine_binary_buffer_375 (u : Real)
    (hu : (237/10 : Real) ≤ u) :
    (4/5 : Real)*u-1849/2000+98/1000 <
      (999997/1000000 : Real)*u-5739/1000+Real.log 2/4 := by
  have h2 := log_two_rational_control.1
  linarith

/-- A strictly conditional scalar impossibility. To apply it in a
field argument, both inequalities MUST be proved for the SAME
positive original integer trace Gram and the SAME dimensions. -/
theorem no_shared_scalar_interval_375
    (D : Nat) (hD : (375 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-1849/2000)
    (hLower : (999997/1000000 : Real)*Real.log D-5739/1000+
      Real.log 2/4 ≤ g) : False := by
  have hu := log_large_from_375_fourth_power D hD
  have hsep := affine_binary_buffer_375 (Real.log D) hu
  linarith

end
end TenthDiscriminant
