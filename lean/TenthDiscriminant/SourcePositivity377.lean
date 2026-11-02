import TenthDiscriminant.ThinEllipseCount377
import TenthDiscriminant.RadialCutoff
import TenthDiscriminant.ThinRadiusAnalyticGain

/-!
# Phase174: positivity for the actual original trace Grams at 377^4

The original Qthin and Qold have their usual definitions:
  Qthin = ellipsePairs D (thinRadius D)
  Qold  = ellipsePairs D (rho D).
Both use exactly the original integer ordinary-jet trace Gram,
not a surrogate ellipsoid determinant or a new analytic metric.

Crucially, positivity of Qold is transported from the proven thin-Q
interpolation count by set inclusion. We do NOT reuse the old stronger
3R+S cell-area-radius certificate, which fails its sufficient guard
at fourth-root 377.

These are geometry and positivity lemmas ONLY. No upper logarithmic
determinant inequality or field-discriminant cutoff is claimed.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

private theorem dimensions_positive_377 (D : Nat) (hD : (377 : Nat)^4 ≤ D) :
    1 ≤ R D ∧ 1 ≤ S D := by
  constructor
  · unfold R envelopeR
    omega
  · unfold S R envelopeR
    omega

/-- At 377^4 the original thin radius does not exceed the original
padded radius, by exact ceiling bounds. No change of lattice. -/
theorem thin_radius_le_old_radius_377 (D : Nat)
    (hD : (377 : Nat)^4 ≤ D) : thinRadius D ≤ rho D := by
  have ht := fourthRoot_ge_377 D hD
  have hcube : (377 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hsmall : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hlarge : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  have hle : (thinRadius D : Real) ≤ rho D := by
    nlinarith only [hcube,hsmall,hlarge]
  exact_mod_cast hle

/-- The already accepted source-ellipse monotonicity transports the
point-count lower bound to the OLD larger padded radius. -/
theorem padded_interpolation_count_377 (D : Nat)
    (hD : (377 : Nat)^4 ≤ D) :
    2*(R D-1)+(S D-1) <
      (ellipsePairs D (rho D)).card := by
  have hD0 : 0 < D := by omega
  have hthin := thin_radius_interpolation_count_377 D hD
  have hm := ellipsePairs_card_mono_radius D
    (thinRadius D) (rho D) hD0
    (thin_radius_le_old_radius_377 D hD)
  omega

/-- The existing original padded cardinality MAJORANT also bounds
the smaller original ellipse, without equating the two Gram matrices. -/
theorem thin_card_le_old_padded_majorant_377 (D : Nat)
    (hD : (377 : Nat)^4 ≤ D) :
    ((ellipsePairs D (thinRadius D)).card : Real) ≤
      ellipsePaddedUpperCount D (rho D)
        (ellipseVerticalBound D (rho D)) := by
  have hD0 : 0 < D := by omega
  have hm := ellipsePairs_card_mono_radius D
    (thinRadius D) (rho D) hD0
    (thin_radius_le_old_radius_377 D hD)
  have hcm : ((ellipsePairs D (thinRadius D)).card : Real) ≤
      ((ellipsePairs D (rho D)).card : Real) := by
    exact_mod_cast hm
  have hp := ellipsePairs_card_le_padded_upper_count
    D D (rho D) (ellipseVerticalBound D (rho D))
    hD0 le_rfl le_rfl
  exact hcm.trans hp

/-- Strict positivity of that majorant derives from the verified
ORIGINAL thin-Q count, not the obsolete padded 3R+S certificate. -/
theorem old_padded_majorant_pos_377 (D : Nat)
    (hD : (377 : Nat)^4 ≤ D) :
    0 < ellipsePaddedUpperCount D (rho D)
        (ellipseVerticalBound D (rho D)) := by
  have hc := thin_radius_interpolation_count_377 D hD
  have hpos : 0 < (ellipsePairs D (thinRadius D)).card := by omega
  have hposReal : (0 : Real) <
      ((ellipsePairs D (thinRadius D)).card : Real) := by
    exact_mod_cast hpos
  exact lt_of_lt_of_le hposReal
    (thin_card_le_old_padded_majorant_377 D hD)

/-- Positivity of the same ORIGINAL thin integer ordinary-jet Gram.
In a future theorem the prime lower and geometric upper must both
refer to this exact determinant. -/
theorem thin_original_gram_pos_377 (D : Nat)
    (hD : (377 : Nat)^4 ≤ D) :
    0 < (integerRectangularTraceGram
       (ellipsePairs D (thinRadius D)) D (S D) (R D) (S D)).det := by
  have hp := dimensions_positive_377 D hD
  exact TenthDiscriminant.RadialCutoff.integer_det_positive
    (ellipsePairs D (thinRadius D)) D (R D) (S D)
    (by omega) hp.1 hp.2
    (thin_radius_interpolation_count_377 D hD)

/-- Likewise, the ORIGINAL padded Gram is positive, independently
of the invalid old stronger cell-area sufficient proof. -/
theorem old_original_gram_pos_377 (D : Nat)
    (hD : (377 : Nat)^4 ≤ D) :
    0 < (integerRectangularTraceGram
       (ellipsePairs D (rho D)) D (S D) (R D) (S D)).det := by
  have hp := dimensions_positive_377 D hD
  exact TenthDiscriminant.RadialCutoff.integer_det_positive
    (ellipsePairs D (rho D)) D (R D) (S D)
    (by omega) hp.1 hp.2
    (padded_interpolation_count_377 D hD)

end
end TenthDiscriminant.FirstCertificate.Tuned
