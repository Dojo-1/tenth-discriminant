import TenthDiscriminant.TunedRadiusFamily
import TenthDiscriminant.LogEnclosure

/-!
# Phase197 — 324-fourth-root arithmetic preflight, never a field theorem

We keep the SAME dimension R = floor(D/4), certified source
floor 249*D <= 1000*R, and p=3/5 recovery proposed in Phase196.
A sounder bound for log(1000/249) repairs a 0.009 loss in the old
log R -> log D transport. We do not assert positivity or any
lower/upper inequality for an integer Gram here.
-/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

/-- Existing N=8 rational binary logarithm enclosure, no floating point. -/
theorem log_floor_ratio_upper_1391 :
    Real.log (1000/249 : Real) ≤ 1391/1000 := by
  have h := checkPositiveLogBounds_sound 8 (1000/249) 2
    (139/100) (1391/1000)
    (by norm_num [checkPositiveLogBounds,
      binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h.2

/-- Better logarithmic lower estimate on the UNCHANGED original floor R.
The proposition requires D >= 324^4 so the existing R/D floor guard holds. -/
theorem log_R_lower_324 (D : Nat) (hD : (324 : Nat)^4 ≤ D) :
    Real.log (D : Real)-1391/1000 ≤
      Real.log (FirstCertificate.Tuned.R D) := by
  have hn : 249*D ≤ 1000*FirstCertificate.Tuned.R D := by
    simpa [FirstCertificate.Tuned.R] using
      (FirstCertificate.envelope_floor_ratio D (by omega))
  have hr : (249 : Real)*D ≤
      1000*FirstCertificate.Tuned.R D := by exact_mod_cast hn
  have hp : (0 : Real) < D := by
    exact_mod_cast (show 0 < D by omega)
  have hR : (D : Real)/(1000/249) ≤
      FirstCertificate.Tuned.R D := by
    apply (div_le_iff₀ (by norm_num : (0 : Real) < 1000/249)).2
    linarith
  have hl := Real.log_le_log (div_pos hp (by norm_num)) hR
  rw [Real.log_div hp.ne' (by norm_num : (1000/249 : Real) ≠ 0)] at hl
  linarith [log_floor_ratio_upper_1391]

/-- N=5 finite rational interval for log 324, including tail bound. -/
theorem log_324_rational_enclosure :
    (57807/10000 : Real) ≤ Real.log 324 ∧
    Real.log 324 ≤ (57808/10000 : Real) := by
  have hc : checkPositiveLogBounds 5 324 8
      (57807/10000) (57808/10000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 324 8
    (57807/10000) (57808/10000) hc
  norm_num at h
  constructor
  · linarith [h.1]
  · linarith [h.2]

private theorem log_324_power_four :
    Real.log (((324 : Nat)^4 : Nat) : Real) =
      4*Real.log (324 : Real) := by
  rw [Nat.cast_pow,Real.log_pow]
  ring

/-- A guarded log-D lower at 324^4, no invented real approximation. -/
theorem log_floor_from_324_fourth_power (D : Nat)
    (hD : (324 : Nat)^4 ≤ D) :
    (231228/10000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) < (((324 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((324 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [log_324_power_four] at hm
  linarith [log_324_rational_enclosure.1]

/-- PURE SCALAR: after proving separate matching source Gram bounds,
this affine comparison would rule out class number one at D >= 324^4.
No determinant or number-field statement is assumed or claimed here. -/
theorem strict_affine_separator_324 (u : Real)
    (hu : (231228/10000 : Real) ≤ u) :
    (4/5 : Real)*u-1851/2000 <
    (999997/1000000 : Real)*u-57215/10000+Real.log 2/4 := by
  have h2 := log_two_rational_control.1
  linarith

/-- Exact positive rational margin, independent of any geometry. -/
theorem exact_324_scalar_margin :
    (999997/1000000-4/5 : Real)*(231228/10000)
      -57215/10000+1851/2000+6931/40000 =
        (4414079/2500000000 : Real) ∧
      (0 : Real) < 4414079/2500000000 := by
  norm_num

/-- Independent N=5 rational enclosure at the neighboring lower root. -/
theorem log_323_rational_enclosure :
    (57776/10000 : Real) ≤ Real.log 323 ∧
    Real.log 323 ≤ (57777/10000 : Real) := by
  have hc : checkPositiveLogBounds 5 323 8
      (57776/10000) (57777/10000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 323 8
    (57776/10000) (57777/10000) hc
  norm_num at h
  constructor
  · linarith [h.1]
  · linarith [h.2]

/-- A NEGATIVE CONTROL for the exact fixed affine envelopes at 323^4.
It does not exclude 323 by other arithmetic, other source geometry, or
an improved pair of estimates; it only kills automatic scalar reuse. -/
theorem fixed_affine_separator_fails_at_323 :
    ¬ ((4/5 : Real)*(4*Real.log 323)-1851/2000 <
      (999997/1000000 : Real)*(4*Real.log 323)-57215/10000+
        Real.log 2/4) := by
  intro h
  have h323 := log_323_rational_enclosure.2
  have h2 := log_two_rational_control.2
  linarith

theorem fourth_power_324_control :
    (324 : Nat)^4 = 11019960576 ∧
    (324 : Nat)^4 < (327 : Nat)^4 := by
  norm_num

theorem original_cell_covering_buffer_324 :
    (0 : Real) <
      (11/25-1001/1000*407/1000)*324-10 := by
  norm_num

end
end TenthDiscriminant
