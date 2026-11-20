import TenthDiscriminant.ThinEllipseCount
import TenthDiscriminant.EllipseCellArea

/-!
# Phase353 — source-exact uniform thin-ellipse count from the original cell-area lemma

This reuses the already kernel-checked complete-ellipse cell-area bound
and the UNCHANGED Tuned.thinRadius, R and S. It makes no five-band
resampling and introduces no new analytic / arithmetic determinant theorem.

Put t = D^(1/4). For t>=21 we prove:
 (1+t^2)/2 <= t^3/40
 rho - (1+sqrt D)/2 >= (83/200)t^3
 3*(83/200)^2 > 51/100 >= (2R+S)/D

The original full-ellipse area estimate then forces
  card(ellipsePairs D (thinRadius D)) > 2R+S.
The original interpolation criterion follows immediately.

This is only geometry; not a new actual-field discriminant bound.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

private theorem fourthRoot_ge_twentyone (D : Nat)
    (hD : (21 : Nat)^4 ≤ D) :
    (21 : Real) ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (21 : Nat)^2^2 ≤ D by omega)

/-- At fourth root 21, the old lattice-cell half-diagonal
is at most one fortieth of t^3. -/
private theorem cell_error_le_cube_fortieth (t : Real)
    (ht : 21 ≤ t) :
    (1+t^2)/2 ≤ t^3/40 := by
  have hs : (441 : Real) ≤ t^2 := by
    have hmul : 0 ≤ (t-21)*(t+21) :=
      mul_nonneg (by linarith) (by linarith)
    nlinarith only [hmul]
  have hm : 0 ≤ (t-21)*t^2 :=
    mul_nonneg (by linarith) (sq_nonneg t)
  nlinarith only [hs,hm]

/-- A fully rational positivity margin; no numerical approximation of pi. -/
private theorem rational_cell_gap (t : Real) (ht : 0 < t) :
    (51/100 : Real)*t^6 <
      (3 : Real)*((83/200 : Real)*t^3)^2 := by
  have h6 : 0 < t^6 := pow_pos ht 6
  nlinarith only [h6]

/-- The SAME original thinRadius chosen in Phase140 already has
enough ORIGINAL lattice points for the ordinary-jet interpolation
guard at every integer D >= 21^4, substantially below the earlier
conservative cell-radius threshold and the Phase352 five-band target.

This does NOT alter the analytic upper or arithmetic lower budget
of the actual field theorem. -/
theorem thin_radius_interpolation_count_21 (D : Nat)
    (hD : (21 : Nat)^4 ≤ D) :
    2*(R D-1)+(S D-1) <
      (ellipsePairs D (thinRadius D)).card := by
  let t : Real := fourthRoot D
  let rr : Real := thinRadius D
  let delta : Real := (1+Real.sqrt D)/2
  let mm : Real := (83/200 : Real)*t^3
  have hi := fourthRoot_identities D
  have ht : (21 : Real) ≤ t := fourthRoot_ge_twentyone D hD
  have htpos : 0 < t := by linarith
  have ht2pos : 0 < t^2 := pow_pos htpos 2
  have hDpos : 0 < D := by omega
  have hceil : (11/25 : Real)*t^3 ≤ rr := by
    change (11/25 : Real)*fourthRoot D^3 ≤ (thinRadius D : Real)
    unfold thinRadius
    exact Nat.le_ceil _
  have herror : delta ≤ t^3/40 := by
    dsimp [delta,t]
    rw [← hi.2.1]
    exact cell_error_le_cube_fortieth (fourthRoot D)
      (fourthRoot_ge_twentyone D hD)
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
      _ < (3 : Real)*mm^2 := by
        exact rational_cell_gap t htpos
      _ ≤ Real.pi*mm^2 := by
        exact mul_le_mul_of_nonneg_right
          (le_of_lt Real.pi_gt_three) (sq_nonneg mm)
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

/-- This pure mathematical boundary control certifies the rational
margin used above and excludes accidental floating truncation. -/
theorem rational_margin_control :
    (51/100 : Real) < 3*((83/200 : Real)^2) := by norm_num

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_interpolation_count_21
#print axioms TenthDiscriminant.FirstCertificate.Tuned.rational_margin_control
