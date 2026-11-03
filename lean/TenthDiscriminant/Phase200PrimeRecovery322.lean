import TenthDiscriminant.RecoveryGainFloorRatio
import TenthDiscriminant.Phase200Scalar322

/-!
# Phase200B — the actual original p=3,5 valuation-weight gain at fourth-root 322

The Phase200Scalar322 file proved a *rational budget* for the improved
0.0901 recovery. Here we separately bridge that budget to the original
valuationWeight and small35Mass objects, using exactly the existing
saturated-row estimates and the exact floor relation.

This is NOT a Gram bound, a class-number statement, or a field cutoff.
The needed S>=500000, 25*S<=R<=25*S+24 hypotheses remain visible.
No auxiliary primes and no binary factor enter these statements.
-/

namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Both strengthened logarithms concern the SAME existing primes. -/
theorem phase200_original_prime_log_controls :
    (1098/1000 : Real) ≤ Real.log 3 ∧
    (1609/1000 : Real) ≤ Real.log 5 := by
  exact ⟨TenthDiscriminant.log_three_lower_1098,
    TenthDiscriminant.log_five_lower_1609⟩

/-- Source-typed 0.0901 recovered mass on the original valuationWeights.
The new bound comes from sharper sound log 3/log 5 brackets, not new primes. -/
theorem phase200_original_prime_gain_scale_322
    (R S : Nat) (hS : 500000 ≤ S)
    (h25 : 25*S ≤ R) (hfloor : R ≤ 25*S+24) :
    comparisonScale R S*(901/10000 : Real) ≤ 2*small35Mass R S := by
  have hs1 : 1 ≤ S := by omega
  have hr3 : 3*S ≤ R := by omega
  have hr5 : 5*S ≤ R := by omega
  have h3 : ((R-3*S : Nat) : Real)*S*((S-1 : Nat) : Real) ≤
      2*(valuationWeight R S 3 : Real) := by
    exact_mod_cast saturated_rows_lower_weight R S 3 (by decide)
  have h5 : ((R-5*S : Nat) : Real)*S*((S-1 : Nat) : Real) ≤
      2*(valuationWeight R S 5 : Real) := by
    exact_mod_cast saturated_rows_lower_weight R S 5 (by decide)
  rw [Nat.cast_sub hr3, Nat.cast_sub hs1] at h3
  rw [Nat.cast_sub hr5, Nat.cast_sub hs1] at h5
  push_cast at h3 h5
  have hw3 := mul_le_mul_of_nonneg_left h3
    (by norm_num : (0 : Real) ≤ 1098/1000)
  have hw5 := mul_le_mul_of_nonneg_left h5
    (by norm_num : (0 : Real) ≤ 1609/1000)
  have hs : (500000 : Real) ≤ S := by exact_mod_cast hS
  have hlo : (25 : Real)*S ≤ R := by exact_mod_cast h25
  have hhi : (R : Real) ≤ (250001/10000 : Real)*S := by
    have hc : (R : Real) ≤ 25*S+24 := by exact_mod_cast hfloor
    linarith
  have hs0 : (0 : Real) ≤ S := Nat.cast_nonneg S
  have hcoef : (56336/1000 : Real)*S ≤
      (2707/1000 : Real)*R-(11339/1000 : Real)*S := by linarith
  have hprod := mul_le_mul_of_nonneg_right hcoef
    (mul_nonneg hs0 (show (0 : Real) ≤ S-1 by linarith))
  have hsapprox : (499999/500000 : Real)*S ≤ (S : Real)-1 := by linarith
  have hcubic := mul_le_mul_of_nonneg_left hsapprox
    (show (0 : Real) ≤ (56336/1000 : Real)*(S : Real)^2 by positivity)
  have hlower : ((56336/1000 : Real)*(499999/500000))*(S : Real)^3 ≤
      2*((1098/1000 : Real)*(valuationWeight R S 3 : Real)+
        (1609/1000 : Real)*(valuationWeight R S 5 : Real)) := by
    nlinarith only [hw3,hw5,hprod,hcubic]
  have hmult := mul_nonneg (sub_nonneg.mpr hhi)
    (show (0 : Real) ≤ (250001/10000 : Real)*(S : Real)+(R : Real)
      by positivity)
  have hsq : (R : Real)^2 ≤
      (62500500001/100000000 : Real)*(S : Real)^2 := by
    nlinarith only [hmult]
  have hscale : comparisonScale R S ≤
      (62500500001/100000000 : Real)*(S : Real)^3 := by
    unfold comparisonScale
    have hh := mul_le_mul_of_nonneg_right hsq hs0
    nlinarith only [hh]
  obtain ⟨hl3,hl5⟩ := phase200_original_prime_log_controls
  have hm3 := mul_le_mul_of_nonneg_left hl3
    (Nat.cast_nonneg (valuationWeight R S 3))
  have hm5 := mul_le_mul_of_nonneg_left hl5
    (Nat.cast_nonneg (valuationWeight R S 5))
  have hweighted : 2*((1098/1000 : Real)*(valuationWeight R S 3 : Real)+
      (1609/1000 : Real)*(valuationWeight R S 5 : Real)) ≤
      2*small35Mass R S := by
    unfold small35Mass
    nlinarith only [hm3,hm5]
  have hscalar : (901/10000 : Real)*(62500500001/100000000) ≤
      (56336/1000 : Real)*(499999/500000) := by norm_num
  have hcube : (0 : Real) ≤ (S : Real)^3 := by positivity
  calc
    comparisonScale R S*(901/10000 : Real) ≤
        ((62500500001/100000000 : Real)*(S : Real)^3)*
          (901/10000 : Real) :=
      mul_le_mul_of_nonneg_right hscale (by norm_num)
    _ = ((901/10000 : Real)*(62500500001/100000000))*
          (S : Real)^3 := by ring
    _ ≤ ((56336/1000 : Real)*(499999/500000))*(S : Real)^3 :=
      mul_le_mul_of_nonneg_right hscalar hcube
    _ ≤ 2*((1098/1000 : Real)*(valuationWeight R S 3 : Real)+
      (1609/1000 : Real)*(valuationWeight R S 5 : Real)) := hlower
    _ ≤ 2*small35Mass R S := hweighted

/-- Exact normalized gain, with the size and floor prerequisites explicit. -/
theorem phase200_original_prime_normalized_gain_322 (R S : Nat) (I : Real)
    (hS : 500000 ≤ S) (h25 : 25*S ≤ R) (hfloor : R ≤ 25*S+24) :
    (901/10000 : Real) ≤
      (recoveredPrimeMassLower R S I-certifiedPrimeMassLower R S I)/
        comparisonScale R S := by
  have hp := comparisonScale_pos R S (by omega) (by omega)
  have heq : recoveredPrimeMassLower R S I-certifiedPrimeMassLower R S I =
      2*small35Mass R S := by
    unfold recoveredPrimeMassLower
    ring
  rw [heq]
  apply (le_div_iff₀ hp).mpr
  nlinarith only [phase200_original_prime_gain_scale_322 R S hS h25 hfloor]

/-- Reusable strengthened raw-mass estimate, not yet a determinant lower. -/
theorem phase200_raw_normalized_add_gain_322 (R S : Nat) (I : Real)
    (hS : 500000 ≤ S) (h25 : 25*S ≤ R) (hfloor : R ≤ 25*S+24) :
    rawPrimeMassLower R S I/comparisonScale R S+(901/10000 : Real) ≤
      recoveredPrimeMassLower R S I/comparisonScale R S := by
  have hp := comparisonScale_pos R S (by omega) (by omega)
  have hh := div_le_div_of_nonneg_right
    (rawPrimeMassLower_le_certified R S I) hp.le
  have hg := phase200_original_prime_normalized_gain_322 R S I
    hS h25 hfloor
  rw [sub_div] at hg
  linarith

/-- Historical missing-size-guard negative control: at S=1 the original
valuation mass is zero, so a positive normalized 0.0901 gain is false. -/
theorem phase200_missing_S_guard_rejected (I : Real) :
    ¬ ((901/10000 : Real) ≤
      (recoveredPrimeMassLower 25 1 I-certifiedPrimeMassLower 25 1 I)/
        comparisonScale 25 1) := by
  have hz : small35Mass 25 1 = 0 := by
    simp [small35Mass,valuationWeight]
  have heq : recoveredPrimeMassLower 25 1 I-certifiedPrimeMassLower 25 1 I =
      2*small35Mass 25 1 := by
    unfold recoveredPrimeMassLower
    ring
  rw [heq,hz]
  norm_num

end
end TenthDiscriminant.FirstCertificate
