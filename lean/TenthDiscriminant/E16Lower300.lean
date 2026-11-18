import TenthDiscriminant.E16Dimensions300
import TenthDiscriminant.Lower315
import TenthDiscriminant.E15EuclidUpper

/-!
RESEARCH ONLY: 300-domain candidate, not a certificate until exact-head Lean CI
and independent source-fidelity inspection. Uses same original Qthin ordinary
Z jets and the same integer trace Gram as the 313-domain theorem.
Phase338: original odd-prime mass lower on the complete 300-domain.
No extra mixed binary gain. Keep original R, S, Q, jets and Gram.
Proof obligations are new at 300, not inherited from hD >= 315^4.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
open TenthDiscriminant.RadialCutoff
set_option autoImplicit false
noncomputable section

theorem normalized_lower_300 (D : Nat) (hD : (300 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-58094/10000 ≤
      rawPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_300 D hD
  have hl := (log_R_bounds_300 D hD).1
  have hu := log_R_ge_two_300 D hD
  have hr : (10 : Real)*R D ≤ 251*S D := by exact_mod_cast hd.2.2.1
  have hratio : (R D : Real) ≤ (251/10)*S D := by linarith
  have hm := aspect_ratio_25_point_1_control (R D) (S D)
    hd.1 hd.2.1 hratio (by linarith)
  linarith

/-- The existing +0.0901 recovery remains valid under the same
dimension and floor guards at the 315^4 domain. -/
theorem recovered_normalized_lower_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-57193/10000 ≤
      recoveredPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_300 D hD
  have hS : 500000 ≤ S D := hd.2.1
  have h25 : 25*S D ≤ R D := by unfold S; omega
  have hfloor : R D ≤ 25*S D+24 := by unfold S; omega
  have hh := phase200_raw_normalized_add_gain_322 (R D) (S D)
    FirstEnderInterval.tailBudget hS h25 hfloor
  linarith [normalized_lower_300 D hD]

/-- The recovered lower mass remains below the exact original odd
production mass at the smaller domain. -/
theorem recovered_mass_le_exact_odd_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    recoveredPrimeMassLower (R D) (S D)
      FirstEnderInterval.tailBudget ≤ exactOddPrimeMass (R D) (S D) := by
  have hd := dimensions_300 D hD
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
theorem recovered_mass_le_source_gram_log_300
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hdet : 0 < (integerRectangularTraceGram Q D
      (S D) (R D) (S D)).det) :
    recoveredPrimeMassLower (R D) (S D)
      FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram Q D (S D) (R D) (S D)).det : Real) := by
  have hm := recovered_mass_le_exact_odd_300 D hD
  have hsrc := TenthDiscriminant.BinaryThinLogBridge.original_binary_and_exact_odd_mass_log_of_pos
    Q D (R D) (S D) hsq hclass (strict_inertness D) hdet
  have hb : (0 : Real) ≤
      (binaryNullGramExponent (R D) (S D) : Real)*Real.log 2 :=
    mul_nonneg (Nat.cast_nonneg _) (Real.log_nonneg (by norm_num))
  linarith

/-- Normalized recovered lower for the original source Gram at 315^4. -/
theorem normalized_source_gram_lower_300
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hdet : 0 < (integerRectangularTraceGram Q D
      (S D) (R D) (S D)).det) :
    (999997/1000000 : Real)*Real.log D-57193/10000 ≤
      Real.log ((integerRectangularTraceGram Q D (S D) (R D) (S D)).det : Real) /
        comparisonScale (R D) (S D) := by
  have hd := dimensions_300 D hD
  have hp := comparisonScale_pos (R D) (S D) (by omega) (by omega)
  have hm := recovered_mass_le_source_gram_log_300 Q D hD hsq hclass hdet
  have hnorm := recovered_normalized_lower_300 D hD
  have hdiv := div_le_div_of_nonneg_right hm hp.le
  linarith

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.recovered_normalized_lower_300
#print axioms TenthDiscriminant.FirstCertificate.Tuned.recovered_mass_le_exact_odd_300
