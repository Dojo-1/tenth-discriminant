import TenthDiscriminant.Phase343Log307
import TenthDiscriminant.Phase336ScalarRadius313

/-!
# Phase343 — conditional 307-domain scalar separation without mixed H

This is a strict inequality of two REAL formulas after proving
log D >= 22904/1000 for D >= 307^4. It does NOT establish that
either formula bounds the original source Gram on the 307 domain.

The 313-domain source upper is unavailable at 307: its old 78-cube
radius guard has a verified exact negative endpoint control.
Promoting a field theorem requires a separately rederived upper
and lower on one unchanged ordinary-Z trace Gram.
-/

namespace TenthDiscriminant.Phase343
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- The VERIFIED 307-log floor and the VERIFIED 27/200 radius saving
provide a strict separation of two real expressions WITHOUT the
unverified mixed H determinant gain (+0.00665).

Important: this compares real formulas only. It is not a conclusion
about any source Gram until the two SAME-Gram bounds are obtained
separately for the entire 307-domain. -/
theorem strong_scalar_separation_307_without_mixed (D : Nat)
    (hD : (307 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D-1923/2000 <
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) := by
  have hlog := TenthDiscriminant.Phase343.log_floor_from_307_fourth_power D hD
  have hlog2 := TenthDiscriminant.log_two_rational_control.1
  have hDint : 8882874001 ≤ D := by
    have he : (307 : Nat)^4 = 8882874001 := by norm_num
    simpa only [he] using hD
  have hDreal : (8882874001 : Real) ≤ (D : Real) :=
    by exact_mod_cast hDint
  have hDpos : (0 : Real) < D := by linarith
  have hDden : (0 : Real) < 625000*(D : Real) := by positivity
  have hDerr : (16895455 : Real)/(625000*(D : Real)) ≤ 1/100000 := by
    apply (div_le_iff₀ hDden).2
    nlinarith only [hDreal]
  have hRnat : 100000000 ≤ Tuned.R D := by
    unfold Tuned.R envelopeR
    omega
  have hRreal : (100000000 : Real) ≤ Tuned.R D := by
    exact_mod_cast hRnat
  have hRpos : (0 : Real) < (Tuned.R D : Real) := by linarith
  have hRerr : (2 : Real)/(Tuned.R D : Real) +
      40/(Tuned.R D : Real) ≤ 1/1000000 := by
    calc
      (2 : Real)/(Tuned.R D : Real) +
        40/(Tuned.R D : Real) =
          42/(Tuned.R D : Real) := by ring
      _ ≤ 1/1000000 := by
        apply (div_le_iff₀ hRpos).2
        nlinarith only [hRreal]
  linarith only [hlog,hlog2,hDerr,hRerr]

/-- A source-fidelity conditional contradiction on one common REAL
value g. The hypotheses explicitly demand BOTH numerical bounds.
This intentionally does NOT claim that a Gram satisfies them at 307. -/
theorem no_scalar_overlap_307_without_mixed
    (D : Nat) (hD : (307 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-1923/2000)
    (hLower :
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) ≤ g) :
    False := by
  have hgap := strong_scalar_separation_307_without_mixed D hD
  linarith

end
end TenthDiscriminant.Phase343

#print axioms TenthDiscriminant.Phase343.strong_scalar_separation_307_without_mixed
#print axioms TenthDiscriminant.Phase343.no_scalar_overlap_307_without_mixed
