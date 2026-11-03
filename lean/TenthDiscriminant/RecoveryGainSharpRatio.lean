import TenthDiscriminant.StrongSmallPrimeRecoveryGain

/-!
# Phase190: sharpen only the *same* original saturated p=3,5 rows
No new primes, no new valuation source, no field cutoff.
The old 26S ceiling is replaced by the already source-available
10R <= 251S ratio. This is a generic strengthening requiring that guard.
-/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Exact numerical budget governing the proposed +0.0879 recovery. -/
theorem sharp_smallprime_rational_budget :
    (879/10000 : Real)*(63001/100) < 277101/5000 := by
  norm_num

theorem strong_recovered_scale_gain_sharp_ratio (R S : Nat) (hS : 100 ≤ S)
    (h25 : 25*S ≤ R) (h251 : 10*R ≤ 251*S) :
    comparisonScale R S*(879/10000 : Real) ≤ 2*small35Mass R S := by
  have hs1 : 1 ≤ S := by omega
  have hr3 : 3*S ≤ R := by omega
  have hr5 : 5*S ≤ R := by omega
  have h3 : ((R-3*S : Nat) : Real)*S*((S-1 : Nat) : Real) ≤
      2*(valuationWeight R S 3 : Real) := by
    exact_mod_cast saturated_rows_lower_weight R S 3 (by decide)
  have h5 : ((R-5*S : Nat) : Real)*S*((S-1 : Nat) : Real) ≤
      2*(valuationWeight R S 5 : Real) := by
    exact_mod_cast saturated_rows_lower_weight R S 5 (by decide)
  rw [Nat.cast_sub hr3,Nat.cast_sub hs1] at h3
  rw [Nat.cast_sub hr5,Nat.cast_sub hs1] at h5
  push_cast at h3 h5
  have hw3 := mul_le_mul_of_nonneg_left h3 (by norm_num : (0 : Real)≤109/100)
  have hw5 := mul_le_mul_of_nonneg_left h5 (by norm_num : (0 : Real)≤8/5)
  have hs : (100 : Real) ≤ S := by exact_mod_cast hS
  have hlo : (25 : Real)*S ≤ R := by exact_mod_cast h25
  have hhi : (R : Real) ≤ (251/10 : Real)*S := by
    have hc : (10 : Real)*R ≤ 251*S := by exact_mod_cast h251
    linarith
  have hs0 : (0 : Real) ≤ S := Nat.cast_nonneg S
  have hcoef : (2799/50 : Real)*S ≤ (269/100 : Real)*R-(1127/100 : Real)*S := by linarith
  have hprod := mul_le_mul_of_nonneg_right hcoef
    (mul_nonneg hs0 (show (0 : Real)≤S-1 by linarith))
  have hsapprox : (99/100 : Real)*S ≤ (S : Real)-1 := by linarith
  have hcubic := mul_le_mul_of_nonneg_left hsapprox
    (show (0 : Real)≤(2799/50 : Real)*(S : Real)^2 by positivity)
  have hlower : (277101/5000 : Real)*(S : Real)^3 ≤
      2*((109/100 : Real)*(valuationWeight R S 3 : Real)+
        (8/5 : Real)*(valuationWeight R S 5 : Real)) := by
    nlinarith only [hw3,hw5,hprod,hcubic]
  have hmult := mul_nonneg (sub_nonneg.mpr hhi)
    (show (0 : Real)≤(251/10 : Real)*(S : Real)+(R : Real) by positivity)
  have hsq : (R : Real)^2 ≤ (63001/100 : Real)*(S : Real)^2 := by nlinarith only [hmult]
  have hscale : comparisonScale R S ≤ (63001/100 : Real)*(S : Real)^3 := by
    unfold comparisonScale
    have hh := mul_le_mul_of_nonneg_right hsq hs0
    nlinarith only [hh]
  obtain ⟨hl3,hl5⟩ := recovery_log_controls
  have hm3 := mul_le_mul_of_nonneg_left hl3 (Nat.cast_nonneg (valuationWeight R S 3))
  have hm5 := mul_le_mul_of_nonneg_left hl5 (Nat.cast_nonneg (valuationWeight R S 5))
  have hbudget : 2*((109/100 : Real)*(valuationWeight R S 3 : Real)+
      (8/5 : Real)*(valuationWeight R S 5 : Real)) ≤ 2*small35Mass R S := by
    unfold small35Mass
    nlinarith only [hm3,hm5]
  have hcube : (0 : Real)≤(S : Real)^3 := by positivity
  nlinarith only [hlower,hbudget,hscale,hcube]

theorem strong_recovered_normalized_gap_sharp_ratio (R S : Nat) (I : Real) (hS : 100 ≤ S)
    (h25 : 25*S ≤ R) (h251 : 10*R ≤ 251*S) : (879/10000 : Real) ≤
      (recoveredPrimeMassLower R S I-certifiedPrimeMassLower R S I)/comparisonScale R S := by
  have hp := comparisonScale_pos R S (by omega) (by omega)
  have heq : recoveredPrimeMassLower R S I-certifiedPrimeMassLower R S I = 2*small35Mass R S := by
    unfold recoveredPrimeMassLower
    ring
  rw [heq]
  apply (le_div_iff₀ hp).mpr
  nlinarith only [strong_recovered_scale_gain_sharp_ratio R S hS h25 h251]

theorem strong_raw_normalized_add_gain_sharp_ratio_le_recovered (R S : Nat) (I : Real)
    (hS : 100 ≤ S) (h25 : 25*S ≤ R) (h251 : 10*R ≤ 251*S) :
    rawPrimeMassLower R S I/comparisonScale R S+(879/10000 : Real) ≤
      recoveredPrimeMassLower R S I/comparisonScale R S := by
  have hp := comparisonScale_pos R S (by omega) (by omega)
  have hh := div_le_div_of_nonneg_right (rawPrimeMassLower_le_certified R S I) hp.le
  have hg := strong_recovered_normalized_gap_sharp_ratio R S I hS h25 h251
  rw [sub_div] at hg
  linarith


end
end TenthDiscriminant.FirstCertificate
