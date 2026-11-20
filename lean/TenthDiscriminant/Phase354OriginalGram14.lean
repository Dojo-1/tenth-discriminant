import TenthDiscriminant.Phase353DirectCellAreaCount
import TenthDiscriminant.IntegerTraceGram

/-!
# Phase354: stronger original count and full original Gram positivity at root fourteen

This retains the unchanged complete ellipse, original ordinary Z derivatives,
trace metric 2*(ac + D*bd), and every rectangular row. It reuses the old
cell-area theorem but applies the pinned Mathlib lower pi bound 157/50
rather than Phase353's weaker bound three.

The source/cardinality theorem is independent of any class-number-one field
hypothesis. It does NOT imply a stronger actual field discriminant bound.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

private theorem fourthRoot_ge_fourteen (D : Nat)
    (hD : (14 : Nat)^4 ≤ D) :
    (14 : Real) ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (14 : Nat)^2^2 ≤ D by omega)

/-- For t >= 14, the exact lattice-cell half-diagonal delta=(1+t²)/2
fits inside the sharper error envelope 9/250*t³. -/
private theorem cell_error_le_nine_250_cube (t : Real)
    (ht : 14 ≤ t) :
    (1+t^2)/2 ≤ (9/250 : Real)*t^3 := by
  have hs : (196 : Real) ≤ t^2 := by
    have hmul : 0 ≤ (t-14)*(t+14) :=
      mul_nonneg (by linarith) (by linarith)
    nlinarith only [hmul]
  have hm : 0 ≤ (t-14)*t^2 :=
    mul_nonneg (by linarith) (sq_nonneg t)
  nlinarith only [hs, hm]

/-- All constants are rational, and the strict margin is positive.
In particular (157/50)*(101/250)^2 - 51/100 = 15614/6250000. -/
private theorem rational_cell_gap_fourteen (t : Real) (ht : 0 < t) :
    (51/100 : Real)*t^6 <
      (157/50 : Real)*((101/250 : Real)*t^3)^2 := by
  have h6 : 0 < t^6 := pow_pos ht 6
  nlinarith only [h6]

/-- An exact uniform ORIGINAL-SOURCE geometric theorem.
No change of Q, full row family, ordinary Z derivatives or trace. -/
theorem thin_radius_interpolation_count_14 (D : Nat)
    (hD : (14 : Nat)^4 ≤ D) :
    2*(R D-1)+(S D-1) <
      (ellipsePairs D (thinRadius D)).card := by
  let t : Real := fourthRoot D
  let rr : Real := thinRadius D
  let delta : Real := (1+Real.sqrt D)/2
  let mm : Real := (101/250 : Real)*t^3
  have hi := fourthRoot_identities D
  have ht : (14 : Real) ≤ t := fourthRoot_ge_fourteen D hD
  have htpos : 0 < t := by linarith
  have ht2pos : 0 < t^2 := pow_pos htpos 2
  have hDpos : 0 < D := by omega
  have hceil : (11/25 : Real)*t^3 ≤ rr := by
    change (11/25 : Real)*fourthRoot D^3 ≤ (thinRadius D : Real)
    unfold thinRadius
    exact Nat.le_ceil _
  have herror : delta ≤ (9/250 : Real)*t^3 := by
    dsimp [delta,t]
    rw [← hi.2.1]
    exact cell_error_le_nine_250_cube (fourthRoot D)
      (fourthRoot_ge_fourteen D hD)
  have hmpos : 0 ≤ mm := by
    dsimp [mm]
    positivity
  have hside : mm ≤ rr-delta := by
    dsimp [mm]
    linarith [hceil,herror]
  have hsidenonneg : 0 ≤ rr-delta := le_trans hmpos hside
  have hrho : (1+Real.sqrt D)/2 ≤ (thinRadius D : Real) := by
    dsimp [rr,delta] at hsidenonneg
    linarith
  have harea := ellipsePairs_cell_area_bound
    D (thinRadius D) hDpos hrho
  have hsq : mm^2 ≤ (rr-delta)^2 := by
    have hprod : 0 ≤ ((rr-delta)-mm)*((rr-delta)+mm) :=
      mul_nonneg (sub_nonneg.mpr hside)
        (add_nonneg hsidenonneg hmpos)
    nlinarith only [hprod]
  have hrnat : 4*R D ≤ D := by
    dsimp [R,envelopeR]
    omega
  have hsnat : 25*S D ≤ R D := by
    dsimp [S]
    omega
  have hrreal : (4 : Real)*(R D : Real) ≤ (D : Real) := by
    exact_mod_cast hrnat
  have hsreal : (25 : Real)*(S D : Real) ≤ (R D : Real) := by
    exact_mod_cast hsnat
  have hq : ((2*R D+S D : Nat) : Real) ≤
      (51/100 : Real)*(D : Real) := by
    push_cast
    linarith only [hrreal,hsreal]
  have hpi : (157/50 : Real) < Real.pi := by
    convert Real.pi_gt_d2 using 1 <;> norm_num
  have hbound :
      ((2*R D+S D : Nat) : Real)*t^2 <
        ((ellipsePairs D (thinRadius D)).card : Real)*t^2 := by
    calc
      ((2*R D+S D : Nat) : Real)*t^2 ≤
          ((51/100 : Real)*(D : Real))*t^2 :=
        mul_le_mul_of_nonneg_right hq (sq_nonneg t)
      _ = (51/100 : Real)*t^6 := by
        dsimp [t]
        rw [← hi.2.2]
        ring
      _ < (157/50 : Real)*mm^2 := by
        exact rational_cell_gap_fourteen t htpos
      _ ≤ Real.pi*mm^2 := by
        exact mul_le_mul_of_nonneg_right
          (le_of_lt hpi) (sq_nonneg mm)
      _ ≤ Real.pi*(rr-delta)^2 := by
        exact mul_le_mul_of_nonneg_left hsq Real.pi_pos.le
      _ ≤ ((ellipsePairs D (thinRadius D)).card : Real)*t^2 := by
        simpa only [rr,delta,t,← hi.2.1] using harea
  have hcast :
      ((2*R D+S D : Nat) : Real) <
        ((ellipsePairs D (thinRadius D)).card : Real) :=
    (mul_lt_mul_right ht2pos).mp hbound
  have hnat : 2*R D+S D <
      (ellipsePairs D (thinRadius D)).card := by
    exact_mod_cast hcast
  omega

/-- Full original integer ordinary-Z-jet Gram is strictly positive.
This is not positivity of a selected minor or a modified Gram. -/
theorem thin_original_integer_gram_pos_14 (D : Nat)
    (hD : (14 : Nat)^4 ≤ D) :
    0 < (integerRectangularTraceGram
      (ellipsePairs D (thinRadius D)) D
      (S D) (R D) (S D)).det := by
  exact ellipseIntegerTraceGram_det_pos_of_count
    D (thinRadius D) (S D) (R D) (S D)
    (by omega)
    (by change 1 ≤ D/4; omega)
    (by change 1 ≤ D/4/25; omega)
    le_rfl
    (thin_radius_interpolation_count_14 D hD)

/-- Consequently no logarithm-of-zero or singular-original-Gram
shortcut is permitted in this lower domain. -/
theorem thin_original_integer_gram_nonzero_14 (D : Nat)
    (hD : (14 : Nat)^4 ≤ D) :
    (integerRectangularTraceGram
      (ellipsePairs D (thinRadius D)) D
      (S D) (R D) (S D)).det ≠ 0 :=
  ne_of_gt (thin_original_integer_gram_pos_14 D hD)

/-- Original REAL Gram positivity AND the true original Hadamard
majorant follow from the same unchanged complete source count. -/
theorem thin_original_real_gram_hadamard_14 (D : Nat)
    (hD : (14 : Nat)^4 ≤ D) :
    0 < (rectangularTraceGram
        (ellipsePoints D (thinRadius D)) (S D) (R D) (S D)).det ∧
      (rectangularTraceGram
        (ellipsePoints D (thinRadius D)) (S D) (R D) (S D)).det ≤
        Finset.univ.prod (fun i =>
          rectangularTraceGram
            (ellipsePoints D (thinRadius D)) (S D) (R D) (S D) i i) := by
  exact ellipseTraceGram_det_bounds
    D (thinRadius D) (S D) (R D) (S D)
    (by omega)
    (by change 1 ≤ D/4; omega)
    (by change 1 ≤ D/4/25; omega)
    le_rfl
    (thin_radius_interpolation_count_14 D hD)

/-- A deliberately false *error-envelope* strengthening at t=13.
Its falsity does NOT mean the actual original interpolation count fails. -/
theorem thirteen_error_envelope_rejected :
    ¬ (1+(13 : Real)^2)/2 ≤
      (9/250 : Real)*(13 : Real)^3 := by
  norm_num

/-- Strict rational coefficient check, independent of pi approximations. -/
theorem fourteen_rational_margin :
    (51/100 : Real) < (157/50 : Real)*(101/250 : Real)^2 := by
  norm_num

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_interpolation_count_14
#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_original_integer_gram_pos_14
#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_original_integer_gram_nonzero_14
#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_original_real_gram_hadamard_14
#print axioms TenthDiscriminant.FirstCertificate.Tuned.thirteen_error_envelope_rejected
