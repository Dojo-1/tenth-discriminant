import TenthDiscriminant.UniformRadiusFamily

/-! All error terms in the normalized production upper bound stay explicit. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem envelope_radius_pos (D : Nat) (hD : 200000000000 ≤ D) :
    0 < envelopeRadius D := by
  have ht := fourthRoot_large D hD
  have hl := (envelope_radius_bounds D hD).1
  have hp : 0 < (11/20 : Real)*fourthRoot D^3 := by positivity
  have : (0 : Real) < envelopeRadius D := hp.trans_le hl
  exact_mod_cast this

theorem envelope_count_le (D : Nat) (hD : 200000000000 ≤ D) :
    ellipsePaddedUpperCount D (envelopeRadius D)
      (ellipseVerticalBound D (envelopeRadius D)) ≤ 4*(D : Real) := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_large D hD
  have htpos : 0 < fourthRoot D := by linarith
  have hdpos : 0 < Real.sqrt (D : Real) := by rw [← hi.2.1]; positivity
  have hu := (envelope_radius_bounds D hD).2
  have hr0 : (0 : Real) ≤ envelopeRadius D := Nat.cast_nonneg _
  have hr : (envelopeRadius D : Real) ≤ (3/5 : Real)*fourthRoot D^3 := by
    nlinarith only [hu, pow_nonneg hi.1 3]
  have hrsq := pow_le_pow_left₀ hr0 hr 2
  have hpi := mul_le_mul_of_nonneg_right Real.pi_lt_four.le
    (sq_nonneg (envelopeRadius D : Real))
  have hf : ((ellipseVerticalBound D (envelopeRadius D) : Nat) : Real) ≤
      (envelopeRadius D : Real)/Real.sqrt D := by
    unfold ellipseVerticalBound
    exact Nat.floor_le (by positivity)
  have hfm := (le_div_iff₀ hdpos).mp hf
  have haxis := mul_le_mul_of_nonneg_right hr (sq_nonneg (fourthRoot D))
  have hp3 : fourthRoot D^3 ≤ fourthRoot D^6 :=
    pow_le_pow_right₀ (by linarith) (by decide)
  have hp2 : fourthRoot D^2 ≤ fourthRoot D^6 :=
    pow_le_pow_right₀ (by linarith) (by decide)
  have hp5 : 300*fourthRoot D^5 ≤ fourthRoot D^6 := by
    have h := mul_le_mul_of_nonneg_right ht (pow_nonneg hi.1 5)
    nlinarith only [h]
  unfold ellipsePaddedUpperCount
  push_cast
  apply (mul_le_mul_iff_of_pos_right hdpos).mp
  rw [add_mul, add_mul, div_mul_cancel₀ _ hdpos.ne']
  rw [← hi.2.1] at hfm ⊢
  rw [← hi.2.2]
  nlinarith only [hfm, hpi, hrsq, haxis, hr, hp3, hp2, hp5]

theorem envelope_log_radius_upper (D : Nat) (hD : 200000000000 ≤ D) :
    Real.log (envelopeRadius D) ≤ (3/4 : Real)*Real.log D-59/100 := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_large D hD
  have htpos : 0 < fourthRoot D := by linarith
  have hrpos : (0 : Real) < envelopeRadius D := by exact_mod_cast envelope_radius_pos D hD
  have hlog := Real.log_le_log hrpos (envelope_radius_bounds D hD).2
  rw [Real.log_mul (by norm_num : (551/1000 : Real) ≠ 0) (pow_ne_zero _ htpos.ne'),
    Real.log_pow] at hlog
  have hroot : 4*Real.log (fourthRoot D) = Real.log D := by
    have h := congrArg Real.log hi.2.2
    rw [Real.log_pow] at h
    simpa only [Nat.cast_ofNat] using h
  have hcoeff : Real.log (551/1000 : Real) ≤ -59/100 := by
    have he : (551/500 : Real) = 2*(551/1000) := by norm_num
    have h := Real.log_le_sub_one_of_pos (by norm_num : (0 : Real) < 551/500)
    rw [he, Real.log_mul (by norm_num : (2 : Real) ≠ 0)
      (by norm_num : (551/1000 : Real) ≠ 0)] at h
    linarith [Real.log_two_gt_d9]
  norm_num only [Nat.cast_ofNat] at hlog
  linarith

theorem envelope_log_R_upper (D : Nat) (hD : 200000000000 ≤ D) :
    Real.log (envelopeR D) ≤ Real.log D-138/100 := by
  have hd := envelope_dimensions D hD
  have hrpos : (0 : Real) < envelopeR D := by exact_mod_cast (show 0 < envelopeR D by omega)
  have hdpos : (0 : Real) < D := by exact_mod_cast (show 0 < D by omega)
  have hl := Real.log_le_log hrpos hd.2.2.2.2.2.1
  rw [Real.log_div hdpos.ne' (by norm_num : (4 : Real) ≠ 0)] at hl
  have h4 : Real.log (4 : Real) = 2*Real.log 2 := by
    have he : (4 : Real) = 2^2 := by norm_num
    rw [he, Real.log_pow]
    norm_num
  rw [h4] at hl
  linarith [Real.log_two_gt_d9]

/-- The elementary log inequality controls u/R; exponential monotonicity
and a high-precision numerical tail are unnecessary here. -/
theorem envelope_log_over_R (D : Nat) (hD : 200000000000 ≤ D) :
    Real.log D/(envelopeR D : Real) ≤ 1/9000 := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_large D hD
  have hd := envelope_dimensions D hD
  have hspos : 0 < Real.sqrt (D : Real) := by rw [← hi.2.1]; positivity
  have hrpos : (0 : Real) < envelopeR D := by exact_mod_cast (show 0 < envelopeR D by omega)
  have hlog := Real.log_le_sub_one_of_pos hspos
  have he : 2*Real.log (Real.sqrt D) = Real.log D := by
    have h := congrArg Real.log (Real.sq_sqrt (Nat.cast_nonneg D : (0 : Real) ≤ D))
    rw [Real.log_pow] at h
    simpa only [Nat.cast_ofNat] using h
  have hs : (90000 : Real) ≤ Real.sqrt D := by
    rw [← hi.2.1]
    nlinarith [sq_nonneg (fourthRoot D-300)]
  have hsq := Real.sq_sqrt (Nat.cast_nonneg D : (0 : Real) ≤ D)
  have hg := mul_nonneg hspos.le (show 0 ≤ Real.sqrt D-90000 by linarith)
  apply (div_le_iff₀ hrpos).2
  have hR := hd.2.2.2.2.1
  nlinarith only [hlog, he, hg, hsq, hR]

theorem envelope_radius_over_R (D : Nat) (hD : 200000000000 ≤ D) :
    (envelopeRadius D : Real)/envelopeR D ≤ 551/60000 := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_large D hD
  have hd := envelope_dimensions D hD
  have hrpos : (0 : Real) < envelopeR D := by exact_mod_cast (show 0 < envelopeR D by omega)
  have hlarge := mul_le_mul_of_nonneg_right ht (pow_nonneg hi.1 3)
  have hR := hd.2.2.2.2.1
  have hr := (envelope_radius_bounds D hD).2
  apply (div_le_iff₀ hrpos).2
  nlinarith only [hlarge, hR, hr, hi.2.2]

theorem envelope_log_ratio_bounds (D : Nat) (hD : 200000000000 ≤ D) :
    0 ≤ Real.log ((envelopeR D : Real)/envelopeRadius D) ∧
    Real.log ((envelopeR D : Real)/envelopeRadius D) ≤ Real.log D := by
  have hrho := envelope_radius_pos D hD
  have hr := envelope_radius_lt_R D hD
  have hp : (0 : Real) < envelopeRadius D := by exact_mod_cast hrho
  have hRp : (0 : Real) < envelopeR D := by exact_mod_cast (lt_trans hrho hr)
  have hlr := envelope_log_R_upper D hD
  have hlp : 0 ≤ Real.log (envelopeRadius D) := Real.log_nonneg (by exact_mod_cast hrho)
  have hratio : (1 : Real) ≤ (envelopeR D : Real)/envelopeRadius D := by
    apply (le_div_iff₀ hp).2
    simpa only [one_mul] using (show (envelopeRadius D : Real) ≤ envelopeR D by exact_mod_cast hr.le)
  refine ⟨Real.log_nonneg hratio, ?_⟩
  rw [Real.log_div hRp.ne' hp.ne']
  linarith

theorem envelope_count_log_error (D : Nat) (hD : 200000000000 ≤ D) :
    Real.log (2*ellipsePaddedUpperCount D (envelopeRadius D)
      (ellipseVerticalBound D (envelopeRadius D))*envelopeS D)/(envelopeR D : Real) ≤ 1/4000 := by
  have hd := envelope_dimensions D hD
  have hr : (0 : Real) < envelopeR D := by exact_mod_cast (show 0 < envelopeR D by omega)
  have hs : (0 : Real) < envelopeS D := by exact_mod_cast (show 0 < envelopeS D by omega)
  have hdp : (0 : Real) < D := by exact_mod_cast (show 0 < D by omega)
  have hn := envelope_count_le D hD
  have hnp : 0 < ellipsePaddedUpperCount D (envelopeRadius D)
      (ellipseVerticalBound D (envelopeRadius D)) := by
    unfold ellipsePaddedUpperCount
    positivity
  have hS : (envelopeS D : Real) ≤ D := by
    linarith [hd.2.2.2.2.2.1, hd.2.2.2.2.2.2]
  have harg : 2*ellipsePaddedUpperCount D (envelopeRadius D)
      (ellipseVerticalBound D (envelopeRadius D))*envelopeS D ≤ 8*(D : Real)^2 := by
    nlinarith [mul_le_mul hn hS hs.le (by positivity : (0 : Real) ≤ 4*D)]
  have hl := Real.log_le_log (by positivity : 0 < 2*ellipsePaddedUpperCount D
    (envelopeRadius D) (ellipseVerticalBound D (envelopeRadius D))*envelopeS D) harg
  rw [Real.log_mul (by norm_num : (8 : Real) ≠ 0) (pow_ne_zero _ hdp.ne'), Real.log_pow] at hl
  have h8 : Real.log (8 : Real) ≤ 3 := by
    have h := Real.log_le_sub_one_of_pos (by norm_num : (0 : Real) < 2)
    have he : (8 : Real) = 2^3 := by norm_num
    rw [he, Real.log_pow]
    norm_num only [Nat.cast_ofNat]
    linarith
  have hlog := (div_le_iff₀ hr).mp (envelope_log_over_R D hD)
  have hR : (100000000 : Real) ≤ envelopeR D := by exact_mod_cast hd.1
  apply (div_le_iff₀ hr).2
  norm_num only [Nat.cast_ofNat] at hl
  linarith

theorem envelope_endpoint_error (D : Nat) (hD : 200000000000 ≤ D) :
    2*((envelopeS D : Real)-1)/(envelopeR D : Real)^2*
      (envelopeRadius D+Real.log ((envelopeR D : Real)/envelopeRadius D)) ≤ 1/1000 := by
  have hd := envelope_dimensions D hD
  have hr : (0 : Real) < envelopeR D := by exact_mod_cast (show 0 < envelopeR D by omega)
  have hs : (0 : Real) ≤ (envelopeS D : Real)-1 := by
    have : (500000 : Real) ≤ envelopeS D := by exact_mod_cast hd.2.1
    linarith
  have hratio := envelope_log_ratio_bounds D hD
  have hrad := (div_le_iff₀ hr).mp (envelope_radius_over_R D hD)
  have hlog := (div_le_iff₀ hr).mp (envelope_log_over_R D hD)
  have hc : 2*((envelopeS D : Real)-1) ≤ (envelopeR D : Real)/10 := by
    linarith [hd.2.2.2.2.2.2]
  have hpos : 0 ≤ (envelopeRadius D : Real)+
      Real.log ((envelopeR D : Real)/envelopeRadius D) :=
    add_nonneg (Nat.cast_nonneg _) hratio.1
  have hm := mul_le_mul_of_nonneg_right hc hpos
  have hsbound : (envelopeRadius D : Real)+Real.log ((envelopeR D : Real)/envelopeRadius D) ≤
      (1/100 : Real)*envelopeR D := by linarith
  have he := mul_le_mul_of_nonneg_left hsbound hr.le
  have hdiv : 2*((envelopeS D : Real)-1)*
      (envelopeRadius D+Real.log ((envelopeR D : Real)/envelopeRadius D)) /
        (envelopeR D : Real)^2 ≤ 1/1000 := by
    apply (div_le_iff₀ (sq_pos_of_pos hr)).2
    nlinarith only [hm, he]
  convert hdiv using 1
  ring

theorem envelope_normalized_upper (D : Nat) (hD : 200000000000 ≤ D) :
    enderUpperB (envelopeR D) (envelopeS D) (envelopeS D) (envelopeRadius D)
      (ellipsePaddedUpperCount D (envelopeRadius D) (ellipseVerticalBound D (envelopeRadius D))) /
      comparisonScale (envelopeR D) (envelopeS D) ≤
      (13/16 : Real)*Real.log D-1593/2000 := by
  have hd := envelope_dimensions D hD
  have hRn : 0 < envelopeR D := by omega
  have hSn : 1 ≤ envelopeS D := by omega
  have hr : (0 : Real) < envelopeR D := by exact_mod_cast hRn
  have hs : (0 : Real) ≤ envelopeS D := Nat.cast_nonneg _
  rw [upperB_normalized _ _ _ _ hRn hSn (envelope_radius_pos D hD)]
  have hfirst := envelope_count_log_error D hD
  have hend := envelope_endpoint_error D hD
  have hu := moderate_D_log D hD
  have hlogR := envelope_log_R_upper D hD
  have hlogrho := envelope_log_radius_upper D hD
  have hlowR := envelope_log_R_lower D hD
  have hx : (envelopeS D : Real)/envelopeR D ≤ 1/20 :=
    (div_le_iff₀ hr).2 (by linarith [hd.2.2.2.2.2.2])
  have hx0 : (0 : Real) ≤ (envelopeS D : Real)/envelopeR D := by positivity
  have ha : 0 ≤ 1-(envelopeS D : Real)/envelopeR D := by linarith
  have hrad := mul_le_mul_of_nonneg_left hlogrho ha
  have hcoef : (0 : Real) ≤ 2*((envelopeS D : Real)-1)/envelopeR D := by
    apply div_nonneg _ hr.le
    have : (1 : Real) ≤ envelopeS D := by exact_mod_cast hSn
    linarith
  have hRlog := mul_le_mul_of_nonneg_left (sub_le_sub_right hlogR 1) hcoef
  have hdrop : 2*((envelopeS D : Real)-1)/envelopeR D*(Real.log D-138/100-1) ≤
      2*((envelopeS D : Real)/envelopeR D)*(Real.log D-238/100) := by
    have he : 2*((envelopeS D : Real)-1)/envelopeR D ≤
        2*((envelopeS D : Real)/envelopeR D) := by
      apply (div_le_iff₀ hr).2
      field_simp
    have hm := mul_le_mul_of_nonneg_right he (show 0 ≤ Real.log D-238/100 by linarith)
    convert hm using 1
    ring
  have hmain := mul_le_mul_of_nonneg_right hx (show 0 ≤ (5/4 : Real)*Real.log D-417/100 by linarith)
  nlinarith only [hfirst, hend, hrad, hRlog, hdrop, hmain]

/-- The full odd, squarefree, large-D exclusion. No classification or
even-discriminant case is asserted by this chart. -/
theorem odd_large_classNumber_ne_one (D : Nat) (hD : 700000000000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  have hDom : 200000000000 ≤ D := by omega
  have hd := envelope_dimensions D hDom
  apply classNumber_ne_one_of_normalized_envelopes D D D (envelopeRadius D)
    (envelopeR D) (envelopeS D) (ellipseVerticalBound D (envelopeRadius D))
    (by omega) le_rfl le_rfl (by omega) (by omega) hd.2.2.2.1 hsq
    (envelope_strict_inertness D) (envelope_radius_lt_R D hDom) le_rfl
    (envelope_chosen_radius D hDom) (large_D_log D hD)
    (envelope_normalized_upper D hDom) (envelope_normalized_lower D hDom)

end
end TenthDiscriminant.FirstCertificate
