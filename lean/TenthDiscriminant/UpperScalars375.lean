import TenthDiscriminant.Lower375
import TenthDiscriminant.RadiusRatio375
import TenthDiscriminant.ThinEllipseCount375
import TenthDiscriminant.TunedAnalyticCutoff

/-!
# Phase176: reprove old-radius analytic scalar bounds at fourth-root 375

The original R = floor(D/4), S = floor(R/25), rho = ceil((13/25)D^(3/4))
and padded cardinality upper are unchanged. This rederives the old
normalized analytic UPPER input without invoking any old D >= 450^4
hypothesis: no call to root_large, log_large_geometry, dimensions,
radius_bounds, or normalized_upper at their old domains.

None of these scalar estimates bounds an integer Gram determinant on
its own. The same-original-thin-Q upper remains a separate theorem.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- The original padded radius is positive already at D >= 375^4. -/
theorem radius_pos_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    0 < rho D := by
  have ht := fourthRoot_ge_375 D hD
  have hcube : (1 : Real) ≤ fourthRoot D^3 := by
    have h := pow_le_pow_left₀ (by norm_num : (0 : Real) ≤ 1)
      (show (1 : Real) ≤ fourthRoot D by linarith) 3
    simpa using h
  have hl : (13/25 : Real)*fourthRoot D^3 ≤ (rho D : Real) := by
    unfold rho
    exact Nat.le_ceil _
  have hp : (0 : Real) < rho D := by
    nlinarith only [hcube,hl]
  exact_mod_cast hp

/-- The original radius lies strictly below the original dimension. -/
theorem radius_lt_R_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    rho D < R D := by
  have hR := R_ge_ninety_cubes_375 D hD
  have hu := rho_upper_375 D hD
  have ht := fourthRoot_ge_375 D hD
  have hc : (0 : Real) < fourthRoot D^3 :=
    pow_pos (by linarith : (0 : Real) < fourthRoot D) 3
  have hr : (rho D : Real) < R D := by
    nlinarith only [hR,hu,hc]
  exact_mod_cast hr

/-- Same padded count upper at the new floor, with the same pi bound. -/
theorem count_le_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    ellipsePaddedUpperCount D (rho D) (ellipseVerticalBound D (rho D)) ≤
      4*(D : Real) := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_375 D hD
  have htpos : 0 < fourthRoot D := by linarith
  have hdpos : 0 < Real.sqrt (D : Real) := by
    rw [← hi.2.1]
    positivity
  have hu := rho_upper_375 D hD
  have hr0 : (0 : Real) ≤ rho D := Nat.cast_nonneg _
  have hr : (rho D : Real) ≤ (3/5 : Real)*fourthRoot D^3 := by
    nlinarith only [hu,pow_nonneg hi.1 3]
  have hrsq := pow_le_pow_left₀ hr0 hr 2
  have hpi := mul_le_mul_of_nonneg_right Real.pi_lt_four.le
    (sq_nonneg (rho D : Real))
  have hf : ((ellipseVerticalBound D (rho D) : Nat) : Real) ≤
      (rho D : Real)/Real.sqrt D := by
    unfold ellipseVerticalBound
    exact Nat.floor_le (by positivity)
  have hfm := (le_div_iff₀ hdpos).mp hf
  have haxis := mul_le_mul_of_nonneg_right hr (sq_nonneg (fourthRoot D))
  have hp3 : fourthRoot D^3 ≤ fourthRoot D^6 :=
    pow_le_pow_right₀ (by linarith) (by decide)
  have hp2 : fourthRoot D^2 ≤ fourthRoot D^6 :=
    pow_le_pow_right₀ (by linarith) (by decide)
  have hp5 : 300*fourthRoot D^5 ≤ fourthRoot D^6 := by
    have h := mul_le_mul_of_nonneg_right
      (show (300 : Real) ≤ fourthRoot D by linarith) (pow_nonneg hi.1 5)
    nlinarith only [h]
  unfold ellipsePaddedUpperCount
  push_cast
  apply (mul_le_mul_iff_of_pos_right hdpos).mp
  rw [add_mul,add_mul,div_mul_cancel₀ _ hdpos.ne']
  rw [← hi.2.1] at hfm ⊢
  rw [← hi.2.2]
  nlinarith only [hfm,hpi,hrsq,haxis,hr,hp3,hp2,hp5]

/-- The old logarithmic radius ceiling with the same -0.65 constant. -/
theorem log_radius_upper_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    Real.log (rho D) ≤ (3/4 : Real)*Real.log D-65/100 := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_375 D hD
  have htpos : 0 < fourthRoot D := by linarith
  have hrpos : (0 : Real) < rho D := by
    exact_mod_cast radius_pos_375 D hD
  have hlog := Real.log_le_log hrpos (rho_upper_375 D hD)
  rw [Real.log_mul (by norm_num : (521/1000 : Real)≠0)
      (pow_ne_zero _ htpos.ne'),Real.log_pow] at hlog
  have hroot : 4*Real.log (fourthRoot D)=Real.log D := by
    have h := congrArg Real.log hi.2.2
    rw [Real.log_pow] at h
    simpa only [Nat.cast_ofNat] using h
  have hc : Real.log (521/1000 : Real) ≤ -65/100 := by
    have he : (521/500 : Real)=2*(521/1000) := by norm_num
    have h := Real.log_le_sub_one_of_pos
      (by norm_num : (0 : Real)<521/500)
    rw [he,Real.log_mul (by norm_num : (2 : Real)≠0)
      (by norm_num : (521/1000 : Real)≠0)] at h
    linarith [Real.log_two_gt_d9]
  norm_num only [Nat.cast_ofNat] at hlog
  linarith

/-- The same coarse log(D)/R cost; 375 is more than enough for 300. -/
theorem log_over_R_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    Real.log D/(R D : Real) ≤ 1/9000 := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_375 D hD
  have hd := dimensions_375 D hD
  have hspos : 0 < Real.sqrt (D : Real) := by
    rw [← hi.2.1]
    positivity
  have hrpos : (0 : Real) < R D := by
    exact_mod_cast (show 0 < R D by omega)
  have hlog := Real.log_le_sub_one_of_pos hspos
  have he : 2*Real.log (Real.sqrt D)=Real.log D := by
    have h := congrArg Real.log
      (Real.sq_sqrt (Nat.cast_nonneg D : (0 : Real) ≤ D))
    rw [Real.log_pow] at h
    simpa only [Nat.cast_ofNat] using h
  have hs : (90000 : Real) ≤ Real.sqrt D := by
    rw [← hi.2.1]
    nlinarith [sq_nonneg (fourthRoot D-300)]
  have hsq := Real.sq_sqrt (Nat.cast_nonneg D : (0 : Real) ≤ D)
  have hg := mul_nonneg hspos.le
    (show 0 ≤ Real.sqrt D-90000 by linarith)
  apply (div_le_iff₀ hrpos).2
  have hR := hd.2.2.2.2.1
  nlinarith only [hlog,he,hg,hsq,hR]

theorem log_ratio_bounds_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    0 ≤ Real.log ((R D : Real)/rho D) ∧
    Real.log ((R D : Real)/rho D) ≤ Real.log D := by
  have hrho := radius_pos_375 D hD
  have hr := radius_lt_R_375 D hD
  have hp : (0 : Real) < rho D := by exact_mod_cast hrho
  have hRp : (0 : Real) < R D := by exact_mod_cast (lt_trans hrho hr)
  have hlr := (log_R_bounds_375 D hD).2
  have hlp : 0 ≤ Real.log (rho D) :=
    Real.log_nonneg (by exact_mod_cast hrho)
  have hratio : (1 : Real) ≤ (R D : Real)/rho D := by
    apply (le_div_iff₀ hp).2
    simpa only [one_mul] using
      (show (rho D : Real) ≤ R D by exact_mod_cast hr.le)
  refine ⟨Real.log_nonneg hratio,?_⟩
  rw [Real.log_div hRp.ne' hp.ne']
  linarith

theorem count_log_error_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    Real.log (2*ellipsePaddedUpperCount D (rho D)
      (ellipseVerticalBound D (rho D))*S D)/(R D : Real) ≤ 1/4000 := by
  have hd := dimensions_375 D hD
  have hr : (0 : Real) < R D := by
    exact_mod_cast (show 0 < R D by omega)
  have hs : (0 : Real) < S D := by
    exact_mod_cast (show 0 < S D by omega)
  have hdp : (0 : Real) < D := by
    exact_mod_cast (show 0 < D by omega)
  have hn := count_le_375 D hD
  have hnp : 0 < ellipsePaddedUpperCount D (rho D)
      (ellipseVerticalBound D (rho D)) := by
    unfold ellipsePaddedUpperCount
    positivity
  have hS : (S D : Real) ≤ D := by
    linarith [hd.2.2.2.2.2.1,hd.2.2.2.2.2.2]
  have harg : 2*ellipsePaddedUpperCount D (rho D)
      (ellipseVerticalBound D (rho D))*S D ≤ 8*(D : Real)^2 := by
    nlinarith [mul_le_mul hn hS hs.le
      (by positivity : (0 : Real) ≤ 4*D)]
  have hl := Real.log_le_log
    (by positivity : 0 < 2*ellipsePaddedUpperCount D (rho D)
      (ellipseVerticalBound D (rho D))*S D) harg
  rw [Real.log_mul (by norm_num : (8 : Real)≠0)
    (pow_ne_zero _ hdp.ne'),Real.log_pow] at hl
  have h8 : Real.log (8 : Real) ≤ 3 := by
    have h := Real.log_le_sub_one_of_pos
      (by norm_num : (0 : Real) < 2)
    have he : (8 : Real)=2^3 := by norm_num
    rw [he,Real.log_pow]
    norm_num only [Nat.cast_ofNat]
    linarith
  have hlog := (div_le_iff₀ hr).mp (log_over_R_375 D hD)
  have hR : (100000000 : Real) ≤ R D := by
    exact_mod_cast hd.1
  apply (div_le_iff₀ hr).2
  norm_num only [Nat.cast_ofNat] at hl
  linarith

theorem endpoint_error_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    2*((S D : Real)-1)/(R D : Real)^2*
      (rho D+Real.log ((R D : Real)/rho D)) ≤ 1/1000 := by
  have hd := dimensions_375 D hD
  have hr : (0 : Real) < R D := by
    exact_mod_cast (show 0 < R D by omega)
  have hs : (0 : Real) ≤ (S D : Real)-1 := by
    have h : (500000 : Real) ≤ S D := by exact_mod_cast hd.2.1
    linarith
  have hratio := log_ratio_bounds_375 D hD
  have hrad := (div_le_iff₀ hr).mp (radius_over_R_375 D hD)
  have hlog := (div_le_iff₀ hr).mp (log_over_R_375 D hD)
  have hc : 2*((S D : Real)-1) ≤ (R D : Real)/10 := by
    linarith [hd.2.2.2.2.2.2]
  have hpos : 0 ≤ (rho D : Real)+Real.log ((R D : Real)/rho D) :=
    add_nonneg (Nat.cast_nonneg _) hratio.1
  have hm := mul_le_mul_of_nonneg_right hc hpos
  have hsbound : (rho D : Real)+Real.log ((R D : Real)/rho D) ≤
      (1/100 : Real)*R D := by
    linarith
  have he := mul_le_mul_of_nonneg_left hsbound hr.le
  have hdiv : 2*((S D : Real)-1)*
      (rho D+Real.log ((R D : Real)/rho D))/(R D : Real)^2 ≤
      1/1000 := by
    apply (div_le_iff₀ (sq_pos_of_pos hr)).2
    nlinarith only [hm,he]
  convert hdiv using 1
  ring

/-- The SAME old normalized analytic majorant, at the honest new floor.
This is an upper bound on enderUpperB, not yet on a Gram log. -/
theorem normalized_upper_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    enderUpperB (R D) (S D) (S D) (rho D)
      (ellipsePaddedUpperCount D (rho D)
        (ellipseVerticalBound D (rho D)))/comparisonScale (R D) (S D) ≤
      (4/5 : Real)*Real.log D-813/1000 := by
  have hd := dimensions_375 D hD
  have hRn : 0 < R D := by omega
  have hSn : 1 ≤ S D := by omega
  have hr : (0 : Real) < R D := by exact_mod_cast hRn
  have hs : (0 : Real) ≤ S D := Nat.cast_nonneg _
  rw [upperB_normalized _ _ _ _ hRn hSn (radius_pos_375 D hD)]
  have hfirst := count_log_error_375 D hD
  have hend := endpoint_error_375 D hD
  have hu := TenthDiscriminant.log_large_from_375_fourth_power D hD
  have hlogR := (log_R_bounds_375 D hD).2
  have hlogrho := log_radius_upper_375 D hD
  have hx : (S D : Real)/R D ≤ 1/25 :=
    (div_le_iff₀ hr).2 (by linarith [hd.2.2.2.2.2.2])
  have hx0 : (0 : Real) ≤ (S D : Real)/R D := by positivity
  have ha : 0 ≤ 1-(S D : Real)/R D := by linarith
  have hrad := mul_le_mul_of_nonneg_left hlogrho ha
  have hcoef : (0 : Real) ≤ 2*((S D : Real)-1)/R D := by
    apply div_nonneg _ hr.le
    have h : (1 : Real) ≤ S D := by exact_mod_cast hSn
    linarith
  have hRlog := mul_le_mul_of_nonneg_left
    (sub_le_sub_right hlogR 1) hcoef
  have hdrop : 2*((S D : Real)-1)/R D*
      (Real.log D-138/100-1) ≤
      2*((S D : Real)/R D)*(Real.log D-238/100) := by
    have he : 2*((S D : Real)-1)/R D ≤
        2*((S D : Real)/R D) := by
      apply (div_le_iff₀ hr).2
      field_simp
    have hm := mul_le_mul_of_nonneg_right he
      (show 0 ≤ Real.log D-238/100 by linarith)
    convert hm using 1
    ring
  have hmain := mul_le_mul_of_nonneg_right hx
    (show 0 ≤ (5/4 : Real)*Real.log D-411/100 by linarith)
  nlinarith only [hfirst,hend,hrad,hRlog,hdrop,hmain]

/-- Source-exact positivity and dimensional guards for the next Qthin
Hadamard step; old source radius remains smaller than R. -/
theorem thin_radius_guards_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    10 ≤ thinRadius D ∧ thinRadius D < rho D ∧
      thinRadius D < R D := by
  have ht := fourthRoot_ge_375 D hD
  have hcube : (375 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (11/25 : Real)*fourthRoot D^3 ≤ thinRadius D := by
    unfold thinRadius
    exact Nat.le_ceil _
  have h10 : (10 : Real) ≤ thinRadius D := by
    nlinarith only [hceil,hcube]
  have hratio := thin_radius_fraction_375 D hD
  have hold : 0 < rho D := radius_pos_375 D hD
  have holdReal : (0 : Real) < rho D := by exact_mod_cast hold
  have hsmall : (thinRadius D : Real) < rho D := by
    nlinarith only [hratio,holdReal]
  have hsmnat : thinRadius D < rho D := by exact_mod_cast hsmall
  refine ⟨by exact_mod_cast h10, hsmnat, ?_⟩
  exact lt_trans hsmnat (radius_lt_R_375 D hD)

end
end TenthDiscriminant.FirstCertificate.Tuned
