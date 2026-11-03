import TenthDiscriminant.Phase197Scalar324

/-!
Phase199 — source-preserving logarithmic floor and scalar preflight at 323^4.

No new source, no new primes, no altered trace pairing, no original-Gram
upper/lower inequality and NO number-field theorem is claimed here.
This strictly strengthens the raw constant 5.811 to 5.810 using the exact
same proved bound log R >= log D - 1.391 and aspect-ratio lemma.
-/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

/-- Reapply the same original R=floor(D/4) estimate at the smaller domain.
It uses the exact existing 249*D <= 1000*R floor bound, no 324 hypothesis. -/
theorem log_R_lower_323 (D : Nat) (hD : (323 : Nat)^4 ≤ D) :
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

/-- Rational micro-slack from the already proved aspect-ratio control. -/
theorem raw_constant_5810_is_supported :
    (4419/1000 : Real) +
      (999997/1000000)*(1391/1000) <
      (5810/1000 : Real) := by
  norm_num

/-- A deliberately conservative 323 logarithm floor from the already
sound and focused-Lean-checked N=5 Phase197 enclosure. -/
theorem log_floor_from_323_fourth_power (D : Nat)
    (hD : (323 : Nat)^4 ≤ D) :
    (231104/10000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) < (((323 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((323 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  have hp : Real.log (((323 : Nat)^4 : Nat) : Real) =
      4*Real.log (323 : Real) := by
    rw [Nat.cast_pow,Real.log_pow]
    ring
  rw [hp] at hm
  linarith [log_323_rational_enclosure.1]

/-- CONDITIONAL affine collision only: source bounds remain to be proved. -/
theorem strict_affine_separator_323 (u : Real)
    (hu : (231104/10000 : Real) ≤ u) :
    (4/5 : Real)*u-1851/2000 <
      (999997/1000000 : Real)*u-57205/10000+Real.log 2/4 := by
  have h2 := log_two_rational_control.1
  linarith

/-- Exact positive margin for the sharpened *fixed* 323 comparison. -/
theorem exact_323_scalar_margin :
    (999997/1000000-4/5 : Real)*(231104/10000)
      -57205/10000+1851/2000+6931/40000 =
      (178543/625000000 : Real) ∧
      (0 : Real) < 178543/625000000 := by
  norm_num

/-- A sound independently checked N=5 logarithm enclosure at root 322. -/
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

/-- Negative control: the proposed fixed affine envelopes fail at 322.
Does NOT assert that a different proof cannot succeed at 322^4. -/
theorem fixed_affine_separator_fails_at_322 :
    ¬ ((4/5 : Real)*(4*Real.log 322)-1851/2000 <
      (999997/1000000 : Real)*(4*Real.log 322)-57205/10000+
        Real.log 2/4) := by
  intro h
  have h322 := log_322_rational_enclosure.2
  have h2 := log_two_rational_control.2
  linarith

/-- The same original ellipse radius has positive cell-covering
sufficient-condition buffer at root 323; this is not interpolation. -/
theorem original_cell_covering_buffer_323 :
    (0 : Real) <
      (11/25-1001/1000*407/1000)*323-10 := by
  norm_num

theorem fourth_power_323_control :
    (323 : Nat)^4 = 10884540241 ∧
    (323 : Nat)^4 < (324 : Nat)^4 := by
  norm_num

end
end TenthDiscriminant
