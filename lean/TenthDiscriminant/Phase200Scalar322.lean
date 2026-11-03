import TenthDiscriminant.TunedRadiusFamily
import TenthDiscriminant.LogEnclosure

/-!
Phase200 — unchanged-source 322^4 scalar preflight, NOT a field theorem.

Three rational precision releases on original objects:
  (1) stronger log R from R=floor(D/4),
  (2) sound p=3,5 logarithms and a candidate recovered-mass budget,
  (3) sharper log of the unchanged padded radius coefficient 521/1000.
No original-Gram lower/upper or number-field result is asserted here.
-/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

/-- Sound finite N=8 upper logarithm on the original floor ratio. -/
theorem log_floor_ratio_upper_13904 :
    Real.log (1000/249 : Real) ≤ 13904/10000 := by
  have h := checkPositiveLogBounds_sound 8 (1000/249) 2
    (139/100) (13904/10000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ])
  push_cast at h
  exact h.2

/-- The same original R=floor(D/4), no new dimension or lattice. -/
theorem log_R_lower_322 (D : Nat) (hD : (322 : Nat)^4 ≤ D) :
    Real.log (D : Real)-13904/10000 ≤
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
  linarith [log_floor_ratio_upper_13904]

/-- Keep one more digit in the radius log with the original 521/1000. -/
theorem log_1000_over_521_lower_652 :
    (652/1000 : Real) ≤ Real.log (1000/521 : Real) := by
  have h := checkPositiveLogBounds_sound 5 (1000/521) 0
    (652/1000) (653/1000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ])
  push_cast at h
  exact h.1

theorem log_521_over_1000_upper_652 :
    Real.log (521/1000 : Real) ≤ -652/1000 := by
  have he : (521/1000 : Real) = (1000/521 : Real)⁻¹ := by norm_num
  rw [he, Real.log_inv]
  linarith [log_1000_over_521_lower_652]

/-- Sound N=5 prime logs, retaining the SAME original primes 3 and 5. -/
theorem log_three_lower_1098 :
    (1098/1000 : Real) ≤ Real.log 3 := by
  have h := checkPositiveLogBounds_sound 5 3 1
    (1098/1000) (11/10)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ])
  norm_num at h
  exact h.1

theorem log_five_lower_1609 :
    (1609/1000 : Real) ≤ Real.log 5 := by
  have h := checkPositiveLogBounds_sound 5 5 2
    (1609/1000) (161/100)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ])
  norm_num at h
  exact h.1

/-- Exact rational headroom for the unchanged aspect-ratio raw lower. -/
theorem floor_transported_raw_slack_322 :
    (58094/10000 : Real)-
      ((4419/1000)+(999997/1000000)*(13904/10000)) =
      (2607/625000000 : Real) ∧
      (0 : Real) < 2607/625000000 := by
  norm_num

/-- Rational saturated-row budget only. Still must be promoted to a
proof about original valuationWeight to claim a recovered-prime bound. -/
theorem p3p5_candidate_gain_budget_322 :
    (56336/1000 : Real)*(499999/500000) -
      (901/10000)*(250001/10000)^2 =
      (22936827099/1000000000000 : Real) ∧
      (0 : Real) < 22936827099/1000000000000 := by
  norm_num

theorem log_322_rational_enclosure :
    (57745/10000 : Real) ≤ Real.log 322 ∧
    Real.log 322 ≤ (57746/10000 : Real) := by
  have hc : checkPositiveLogBounds 5 322 8
      (57745/10000) (57746/10000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 322 8
    (57745/10000) (57746/10000) hc
  norm_num at h
  constructor
  · linarith [h.1]
  · linarith [h.2]

private theorem log_322_power_four :
    Real.log (((322 : Nat)^4 : Nat) : Real) =
      4*Real.log (322 : Real) := by
  rw [Nat.cast_pow, Real.log_pow]
  ring

theorem log_floor_from_322_fourth_power (D : Nat)
    (hD : (322 : Nat)^4 ≤ D) :
    (230980/10000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) < (((322 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((322 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [log_322_power_four] at hm
  linarith [log_322_rational_enclosure.1]

/-- A conditional affine gap: this does not assert the Gram inequalities. -/
theorem strict_affine_separator_322 (u : Real)
    (hu : (230980/10000 : Real) ≤ u) :
    (4/5 : Real)*u-1853/2000 <
      (999997/1000000 : Real)*u-57193/10000+Real.log 2/4 := by
  have h2 := log_two_rational_control.1
  linarith

theorem exact_322_scalar_margin :
    (999997/1000000-4/5 : Real)*(230980/10000)
      -57193/10000+1853/2000+6931/40000 =
      (2853/500000000 : Real) ∧
      (0 : Real) < 2853/500000000 := by
  norm_num

/-- Sound N=5 log321 upper for a fixed-envelope falsification control. -/
theorem log_321_rational_enclosure :
    (57714/10000 : Real) ≤ Real.log 321 ∧
    Real.log 321 ≤ (57715/10000 : Real) := by
  have hc : checkPositiveLogBounds 5 321 8
      (57714/10000) (57715/10000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 321 8
    (57714/10000) (57715/10000) hc
  norm_num at h
  constructor
  · linarith [h.1]
  · linarith [h.2]

/-- The *same* fixed 322 affine pair does not automatically reach 321. -/
theorem fixed_affine_separator_fails_at_321 :
    ¬ ((4/5 : Real)*(4*Real.log 321)-1853/2000 <
      (999997/1000000 : Real)*(4*Real.log 321)-57193/10000+
      Real.log 2/4) := by
  intro h
  have h321 := log_321_rational_enclosure.2
  have h2 := log_two_rational_control.2
  linarith

/-- Original source cell-covering *sufficient condition* is positive at
root 322. This arithmetic statement is not interpolation or positivity. -/
theorem original_cell_covering_buffer_322 :
    (0 : Real) <
      (11/25-1001/1000*407/1000)*322-10 := by
  norm_num

theorem fourth_power_322_control :
    (322 : Nat)^4 = 10750371856 ∧
    (322 : Nat)^4 < (323 : Nat)^4 := by
  norm_num

end
end TenthDiscriminant
