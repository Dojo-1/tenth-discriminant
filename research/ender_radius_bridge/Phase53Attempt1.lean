import TenthDiscriminant.SmallPrimeRecovery
import TenthDiscriminant.NormalizedComparison

/-! A fixed positive normalized gain from already recovered3/5 weights.
No new endpoint, prime table, valuation or radius guard is asserted. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Rows beyond p*S already have a saturated staircase in the s coordinate. -/
theorem saturated_rows_lower_weight (R S p : Nat) (hp : 0 < p) :
    (R-p*S)*S*(S-1) ≤ 2*valuationWeight R S p := by
  have hpart : (R-p*S)*(∑ t ∈ Finset.range S, t) ≤ valuationWeight R S p := by
    calc
      _ = ∑ _r ∈ Finset.Ico (p*S) R, ∑ t ∈ Finset.range S, t := by
        simp [nsmul_eq_mul]
      _ ≤ ∑ r ∈ Finset.Ico (p*S) R, ∑ t ∈ Finset.range S, min (r/p) t := by
        apply Finset.sum_le_sum
        intro r hr
        have hdiv : S ≤ r/p := (Nat.le_div_iff_mul_le hp).mpr
          (by simpa only [Nat.mul_comm] using (Finset.mem_Ico.mp hr).1)
        apply Finset.sum_le_sum
        intro t ht
        exact le_min (by have := Finset.mem_range.mp ht; omega) le_rfl
      _ ≤ valuationWeight R S p := by
        unfold valuationWeight
        apply Finset.sum_le_sum_of_subset_of_nonneg
        · intro r hr
          exact Finset.mem_range.mpr (Finset.mem_Ico.mp hr).2
        · intro r hr hnot
          exact Nat.zero_le _
  calc
    _ = (R-p*S)*(S*(S-1)) := by ring
    _ = (R-p*S)*((∑ t ∈ Finset.range S, t)*2) := by
      rw [Finset.sum_range_id_mul_two]
    _ = 2*((R-p*S)*(∑ t ∈ Finset.range S, t)) := by ring
    _ ≤ _ := Nat.mul_le_mul_left 2 hpart

private theorem one_le_log_three_and_five :
    (1 : Real) ≤ Real.log 3 ∧ (1 : Real) ≤ Real.log 5 := by
  have h2 := log_two_rational_control.1
  have h3 : Real.log ((2 : Real)^3) ≤ Real.log ((3 : Real)^2) :=
    Real.log_le_log (by positivity) (by norm_num)
  have h5 : Real.log ((2 : Real)^2) ≤ Real.log 5 :=
    Real.log_le_log (by positivity) (by norm_num)
  rw [Real.log_pow, Real.log_pow] at h3
  rw [Real.log_pow] at h5
  constructor <;> linarith

/-- A fixed gain in the actual aspect-ratio range; conservative, not optimal. -/
theorem recovered_scale_gain (R S : Nat) (hS : 100 ≤ S)
    (h25 : 25*S ≤ R) (h26 : R ≤ 26*S) :
    comparisonScale R S*(3/50 : Real) ≤ 2*small35Mass R S := by
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
  have hs : (100 : Real) ≤ S := by exact_mod_cast hS
  have hlo : (25 : Real)*S ≤ R := by exact_mod_cast h25
  have hhi : (R : Real) ≤ 26*S := by exact_mod_cast h26
  have hs0 : (0 : Real) ≤ S := Nat.cast_nonneg S
  have hcoef : (42 : Real)*S ≤ 2*R-8*S := by linarith
  have hprod := mul_le_mul_of_nonneg_right hcoef
    (mul_nonneg hs0 (show (0 : Real) ≤ S-1 by linarith))
  have hsapprox : (99/100 : Real)*S ≤ (S : Real)-1 := by linarith
  have hcubic := mul_le_mul_of_nonneg_left hsapprox
    (show (0 : Real) ≤ 42*(S : Real)^2 by positivity)
  have hlower : (2079/50 : Real)*(S : Real)^3 ≤
      2*((valuationWeight R S 3 : Real)+(valuationWeight R S 5 : Real)) := by
    nlinarith only [h3,h5,hprod,hcubic]
  have hmult := mul_nonneg (sub_nonneg.mpr hhi)
    (show (0 : Real) ≤ 26*(S : Real)+(R : Real) by positivity)
  have hsq : (R : Real)^2 ≤ 676*(S : Real)^2 := by nlinarith only [hmult]
  have hscale : comparisonScale R S ≤ 676*(S : Real)^3 := by
    unfold comparisonScale
    have hh := mul_le_mul_of_nonneg_right hsq hs0
    nlinarith only [hh]
  obtain ⟨hl3,hl5⟩ := one_le_log_three_and_five
  have hm3 := mul_le_mul_of_nonneg_left hl3 (Nat.cast_nonneg (valuationWeight R S 3))
  have hm5 := mul_le_mul_of_nonneg_left hl5 (Nat.cast_nonneg (valuationWeight R S 5))
  have hbudget : 2*((valuationWeight R S 3 : Real)+(valuationWeight R S 5 : Real)) ≤
      2*small35Mass R S := by
    unfold small35Mass
    nlinarith only [hm3,hm5]
  have hcube : (0 : Real) ≤ (S : Real)^3 := by positivity
  nlinarith only [hlower,hbudget,hscale,hcube]

theorem recovered_normalized_gap (R S : Nat) (I : Real) (hS : 100 ≤ S)
    (h25 : 25*S ≤ R) (h26 : R ≤ 26*S) :
    (3/50 : Real) ≤
      (recoveredPrimeMassLower R S I-certifiedPrimeMassLower R S I)/comparisonScale R S := by
  have hp := comparisonScale_pos R S (by omega) (by omega)
  have heq : recoveredPrimeMassLower R S I-certifiedPrimeMassLower R S I =
      2*small35Mass R S := by unfold recoveredPrimeMassLower; ring
  rw [heq]
  apply (le_div_iff₀ hp).mpr
  nlinarith only [recovered_scale_gain R S hS h25 h26]

theorem raw_normalized_add_gain_le_recovered (R S : Nat) (I : Real)
    (hS : 100 ≤ S) (h25 : 25*S ≤ R) (h26 : R ≤ 26*S) :
    rawPrimeMassLower R S I/comparisonScale R S+(3/50 : Real) ≤
      recoveredPrimeMassLower R S I/comparisonScale R S := by
  have hp := comparisonScale_pos R S (by omega) (by omega)
  have hh := div_le_div_of_nonneg_right (rawPrimeMassLower_le_certified R S I) hp.le
  have hg := recovered_normalized_gap R S I hS h25 h26
  rw [sub_div] at hg
  linarith

theorem saturated_rows_zero_p_rejected :
    ¬ (4-0*2)*2*(2-1) ≤ 2*valuationWeight 4 2 0 := by decide

theorem normalized_gain_missing_S_guard_false (I : Real) :
    ¬ (3/50 : Real) ≤
      (recoveredPrimeMassLower 25 1 I-certifiedPrimeMassLower 25 1 I)/comparisonScale 25 1 := by
  have hz : small35Mass 25 1=0 := by simp [small35Mass,valuationWeight]
  norm_num [recoveredPrimeMassLower,hz]

end
end TenthDiscriminant.FirstCertificate
