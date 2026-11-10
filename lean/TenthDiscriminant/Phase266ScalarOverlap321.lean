import TenthDiscriminant.Phase265ThinUpper321
import TenthDiscriminant.Phase263EnhancedLower321

/-!
# Phase266: exact 321⁴ same-original-Gram scalar separation

The original analytic upper from Phase265 and the source-exact enhanced
lower from Phase263 refer to ONE thin-ellipse integer ordinary-jet
trace Gram. The new horizontal contribution is paid once, at p=3,5.
This module makes only the final real/rational separation; the actual
field-class-number transport is kept in the following module.

The margin is exact and positive at the endpoint 321⁴. The Lean file
must pass exact-head compilation before it is called a formal result.
-/

namespace TenthDiscriminant
open FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Rational endpoint margin with the conservative horizontal floor
bound and the existing sound lower log(2) bracket. -/
theorem enhanced_scalar_margin_321 :
    (0 : Real) <
      (999997/1000000-4/5)*(230856/10000)
        -57193/10000+1853/2000+6931/40000
        +4659/625000
        -16895455/(625000*((321 : Nat)^4 : Real)) := by
  norm_num

/-- For every D >= 321⁴, the same-original-Gram enhanced lower
lies STRICTLY above the already certified original analytic upper.
No field classification, determinant comparison, or extra prime. -/
theorem strict_affine_separator_321_enhanced
    (D : Nat) (hD : (321 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D-1853/2000 <
      (999997/1000000 : Real)*Real.log D-57193/10000 +
        Real.log 2/4 +
        ((4659/625000 : Real)-16895455/(625000*(D : Real))) := by
  have hlog := Tuned.log_floor_from_321_fourth_power D hD
  have h2 := log_two_rational_control.1
  have hDreal : (((321 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hDpos : (0 : Real) < D := by
    have h : (0 : Real) < (((321 : Nat)^4 : Nat) : Real) := by
      norm_num
    linarith
  have hdenD : (0 : Real) < 625000*(D : Real) := by positivity
  have hden0 : (0 : Real) <
      625000*(((321 : Nat)^4 : Nat) : Real) := by norm_num
  have hfrac :
      (16895455 : Real)/(625000*(D : Real)) ≤
      16895455/(625000*(((321 : Nat)^4 : Nat) : Real)) := by
    apply (div_le_div_iff₀ hdenD hden0).2
    nlinarith only [hDreal]
  have hfixed := enhanced_scalar_margin_321
  linarith

/-- Final scalar no-overlap for ONE normalized real Gram log. -/
theorem no_scalar_overlap_321_enhanced
    (D : Nat) (hD : (321 : Nat)^4 ≤ D) (g : Real)
    (hupper : g ≤ (4/5 : Real)*Real.log D-1853/2000)
    (hlower :
      (999997/1000000 : Real)*Real.log D-57193/10000 +
        Real.log 2/4 +
        ((4659/625000 : Real)-16895455/(625000*(D : Real))) ≤ g) :
    False := by
  have hsep := strict_affine_separator_321_enhanced D hD
  linarith

end
end TenthDiscriminant

#print axioms TenthDiscriminant.enhanced_scalar_margin_321
#print axioms TenthDiscriminant.strict_affine_separator_321_enhanced
#print axioms TenthDiscriminant.no_scalar_overlap_321_enhanced
