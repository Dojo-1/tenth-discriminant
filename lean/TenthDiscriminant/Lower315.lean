import TenthDiscriminant.Phase200Scalar322
import TenthDiscriminant.Phase200PrimeRecovery322
import TenthDiscriminant.BinaryThinLogBridge
import TenthDiscriminant.Log315Certificate

/-!
# Phase323-F: source-exact arithmetic lower at 315^4

This is the old odd-prime recovered lower transported to the smaller
315^4 domain. It keeps the same R=floor(D/4), S=floor(R/25), original
prime mass, original integer trace Gram, and original binary vertical
factor. New horizontal factors are intentionally not counted here;
they are a separate additive same-Gram obligation.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
open TenthDiscriminant.RadialCutoff
set_option autoImplicit false
noncomputable section

/-- Original integer dimension bounds at D >= 315^4. -/
theorem dimensions_315 (D : Nat) (hD : (315 : Nat)^4 ≤ D) :
    100000000 ≤ R D ∧ 500000 ≤ S D ∧ 10*R D ≤ 251*S D ∧
    R D ≤ 10000*S D ∧ (D : Real)/5 ≤ R D ∧
    (R D : Real) ≤ (D : Real)/4 ∧ (S D : Real) ≤ (R D : Real)/25 := by
  have hlo : D ≤ 5*(D/4) := by omega
  have hhi : 4*(D/4) ≤ D := by omega
  have hs : 25*((D/4)/25) ≤ D/4 := by omega
  refine ⟨by unfold R envelopeR; omega, by unfold S R envelopeR; omega,
    by unfold S R envelopeR; omega, by unfold S R envelopeR; omega, ?_, ?_, ?_⟩
  · have h : (D : Real) ≤ 5*(D/4 : Nat) := by exact_mod_cast hlo
    change (D : Real)/5 ≤ (D/4 : Nat)
    linarith
  · have h : 4*((D/4 : Nat) : Real) ≤ D := by exact_mod_cast hhi
    change ((D/4 : Nat) : Real) ≤ (D : Real)/4
    linarith
  · have h : 25*(((D/4)/25 : Nat) : Real) ≤ (D/4 : Nat) := by exact_mod_cast hs
    change (((D/4)/25 : Nat) : Real) ≤ ((D/4 : Nat) : Real)/25
    linarith

/-- Reprove the floor-ratio logarithm at 315^4; do not weaken the
existing 322-domain theorem. -/
theorem log_R_lower_315 (D : Nat) (hD : (315 : Nat)^4 ≤ D) :
    Real.log D-13904/10000 ≤ Real.log (R D) := by
  have hn : 249*D ≤ 1000*R D := by
    simpa [R] using
      (FirstCertificate.envelope_floor_ratio D (by omega))
  have hr : (249 : Real)*D ≤ 1000*R D := by exact_mod_cast hn
  have hp : (0 : Real) < D := by exact_mod_cast (show 0 < D by omega)
  have hR : (D : Real)/(1000/249) ≤ R D := by
    apply (div_le_iff₀ (by norm_num : (0 : Real) < 1000/249)).2
    linarith
  have hl := Real.log_le_log (div_pos hp (by norm_num)) hR
  rw [Real.log_div hp.ne' (by norm_num : (1000/249 : Real) ≠ 0)] at hl
  linarith [TenthDiscriminant.log_floor_ratio_upper_13904]

/-- Both logarithmic bounds for the unchanged floor R=floor(D/4). -/
theorem log_R_bounds_315 (D : Nat) (hD : (315 : Nat)^4 ≤ D) :
    Real.log D-13904/10000 ≤ Real.log (R D) ∧
    Real.log (R D) ≤ Real.log D-138/100 := by
  have hd := dimensions_315 D hD
  have hp : (0 : Real) < D := by exact_mod_cast (show 0<D by omega)
  have hRpos : (0 : Real) < R D := by exact_mod_cast (show 0<R D by omega)
  constructor
  · exact log_R_lower_315 D hD
  · have hl := Real.log_le_log hRpos hd.2.2.2.2.2.1
    rw [Real.log_div hp.ne' (by norm_num : (4 : Real) ≠ 0)] at hl
    have h4 : Real.log (4 : Real)=2*Real.log 2 := by
      have he : (4 : Real)=2^2 := by norm_num
      rw [he,Real.log_pow]
      norm_num
    rw [h4] at hl
    linarith [Real.log_two_gt_d9]

/-- Re-run the original aspect-ratio prime lower at 315^4 using the
sound 23.0096 logarithmic floor. -/
theorem normalized_lower_315 (D : Nat) (hD : (315 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-58094/10000 ≤
      rawPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_315 D hD
  have hl := (log_R_bounds_315 D hD).1
  have hu := TenthDiscriminant.log_floor_from_315_fourth_power D hD
  have hr : (10 : Real)*R D ≤ 251*S D := by exact_mod_cast hd.2.2.1
  have hratio : (R D : Real) ≤ (251/10)*S D := by linarith
  have hm := aspect_ratio_25_point_1_control (R D) (S D)
    hd.1 hd.2.1 hratio (by linarith)
  linarith

/-- The existing +0.0901 recovery remains valid under the same
dimension and floor guards at the 315^4 domain. -/
theorem recovered_normalized_lower_315 (D : Nat)
    (hD : (315 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-57193/10000 ≤
      recoveredPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_315 D hD
  have hS : 500000 ≤ S D := hd.2.1
  have h25 : 25*S D ≤ R D := by unfold S; omega
  have hfloor : R D ≤ 25*S D+24 := by unfold S; omega
  have hh := phase200_raw_normalized_add_gain_322 (R D) (S D)
    FirstEnderInterval.tailBudget hS h25 hfloor
  linarith [normalized_lower_315 D hD]

/-- The recovered lower mass remains below the exact original odd
production mass at the smaller domain. -/
theorem recovered_mass_le_exact_odd_315 (D : Nat)
    (hD : (315 : Nat)^4 ≤ D) :
    recoveredPrimeMassLower (R D) (S D)
      FirstEnderInterval.tailBudget ≤ exactOddPrimeMass (R D) (S D) := by
  have hd := dimensions_315 D hD
  have hs : 1 ≤ S D := by omega
  have htail := certifiedPrimeMassLower_antitone_tail
    (R D) (S D) hs FirstEnderInterval.tail_le_budget
  have hrec :
      recoveredPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower (R D) (S D) (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith [htail]
  have hprod := recoveredPrimeMassLower_le_production
    (R D) (S D) (enderTailIntegral 10000) (by omega) hs
  have hmass := enderPrimeMassLower_le_exact_production
    (R D) (S D) 10000 (by omega) hs (by decide) hd.2.2.2.1
  exact hrec.trans (hprod.trans hmass)

/-- Actual recovered arithmetic lower on ONE positive original trace
Gram at the 315^4 domain. -/
theorem recovered_mass_le_source_gram_log_315
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (315 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hdet : 0 < (integerRectangularTraceGram Q D
      (S D) (R D) (S D)).det) :
    recoveredPrimeMassLower (R D) (S D)
      FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram Q D (S D) (R D) (S D)).det : Real) := by
  have hm := recovered_mass_le_exact_odd_315 D hD
  have hsrc := TenthDiscriminant.BinaryThinLogBridge.original_binary_and_exact_odd_mass_log_of_pos
    Q D (R D) (S D) hsq hclass (strict_inertness D) hdet
  have hb : (0 : Real) ≤
      (binaryNullGramExponent (R D) (S D) : Real)*Real.log 2 :=
    mul_nonneg (Nat.cast_nonneg _) (Real.log_nonneg (by norm_num))
  linarith

/-- Normalized recovered lower for the original source Gram at 315^4. -/
theorem normalized_source_gram_lower_315
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (315 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hdet : 0 < (integerRectangularTraceGram Q D
      (S D) (R D) (S D)).det) :
    (999997/1000000 : Real)*Real.log D-57193/10000 ≤
      Real.log ((integerRectangularTraceGram Q D (S D) (R D) (S D)).det : Real) /
        comparisonScale (R D) (S D) := by
  have hd := dimensions_315 D hD
  have hp := comparisonScale_pos (R D) (S D) (by omega) (by omega)
  have hm := recovered_mass_le_source_gram_log_315 Q D hD hsq hclass hdet
  have hnorm := recovered_normalized_lower_315 D hD
  have hdiv := div_le_div_of_nonneg_right hm hp.le
  linarith

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.normalized_source_gram_lower_315
