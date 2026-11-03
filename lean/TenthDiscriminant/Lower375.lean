import TenthDiscriminant.Log375Certificate
import TenthDiscriminant.BinaryThinLogBridge

/-!
# Phase172: the original odd-prime lower envelope at 375^4

The source definitions R=floor(D/4) and S=floor(R/25), the exact
odd-prime product, the binary exponent and the integer ordinary-jet
trace Gram are unchanged. This is a re-proof of the LOWER budget at
a smaller domain; it is not a normalized UPPER bound or a field cutoff.

No old 450^4 theorem is invoked with a weakened hypothesis.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
open TenthDiscriminant.RadialCutoff
set_option autoImplicit false
noncomputable section

/-- Same original integer dimension bounds at D>=375^4. -/
theorem dimensions_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
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

/-- Original logarithmic R bounds. The left side uses the already
guarded floor ratio for D>=1000, not any large-root hypothesis. -/
theorem log_R_bounds_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    Real.log D-140/100 ≤ Real.log (R D) ∧
    Real.log (R D) ≤ Real.log D-138/100 := by
  have hd := dimensions_375 D hD
  have hp : (0 : Real)<D := by exact_mod_cast (show 0<D by omega)
  have hRpos : (0 : Real)<R D := by exact_mod_cast (show 0<R D by omega)
  constructor
  · have hn := envelope_floor_ratio D (by omega)
    have hr : (249 : Real)*D ≤ 1000*R D := by exact_mod_cast hn
    have hR : (D : Real)/(1000/249) ≤ R D := by
      apply (div_le_iff₀ (by norm_num : (0 : Real)<1000/249)).2
      linarith
    have hl := Real.log_le_log (div_pos hp (by norm_num)) hR
    rw [Real.log_div hp.ne' (by norm_num : (1000/249 : Real)≠0)] at hl
    linarith [log_floor_ratio_upper]
  · have hl := Real.log_le_log hRpos hd.2.2.2.2.2.1
    rw [Real.log_div hp.ne' (by norm_num : (4 : Real)≠0)] at hl
    have h4 : Real.log (4 : Real)=2*Real.log 2 := by
      have he : (4 : Real)=2^2 := by norm_num
      rw [he, Real.log_pow]
      norm_num
    rw [h4] at hl
    linarith [Real.log_two_gt_d9]

/-- Source-exact normalized raw odd budget at D>=375^4.
The only logarithmic floor used is the Phase169 23.7 theorem. -/
theorem normalized_lower_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5820/1000 ≤
      rawPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_375 D hD
  have hl := (log_R_bounds_375 D hD).1
  have hu := TenthDiscriminant.log_large_from_375_fourth_power D hD
  have hr : (10 : Real)*R D ≤ 251*S D := by exact_mod_cast hd.2.2.1
  have hratio : (R D : Real) ≤ (251/10)*S D := by linarith
  have hm := aspect_ratio_25_point_1_control (R D) (S D)
    hd.1 hd.2.1 hratio (by linarith)
  linarith

/-- Odd-prime recovery gain +0.081 is preserved without using the old
production guards or changing the source prime product. -/
theorem recovered_normalized_lower_375 (D : Nat)
    (hD : (375 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5739/1000 ≤
      recoveredPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_375 D hD
  have hS : 100 ≤ S D := by omega
  have h25 : 25*S D ≤ R D := by unfold S; omega
  have h26 : R D ≤ 26*S D := by unfold S; omega
  have hh := strong_raw_normalized_add_gain_le_recovered (R D) (S D)
    FirstEnderInterval.tailBudget hS h25 h26
  linarith [normalized_lower_375 D hD]

/-- The same prime-tail and odd-only interval estimates apply to
the original rectangular dimensions at the new lower D floor. -/
theorem recovered_mass_le_exact_odd_375 (D : Nat)
    (hD : (375 : Nat)^4 ≤ D) :
    recoveredPrimeMassLower (R D) (S D)
      FirstEnderInterval.tailBudget ≤
      exactOddPrimeMass (R D) (S D) := by
  have hd := dimensions_375 D hD
  have hs : 1 ≤ S D := by omega
  have htail := certifiedPrimeMassLower_antitone_tail
    (R D) (S D) hs FirstEnderInterval.tail_le_budget
  have hrec :
      recoveredPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower (R D) (S D)
        (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith [htail]
  have hprod := recoveredPrimeMassLower_le_production
    (R D) (S D) (enderTailIntegral 10000) (by omega) hs
  have hmass := enderPrimeMassLower_le_exact_production
    (R D) (S D) 10000 (by omega) hs (by decide) hd.2.2.2.1
  exact hrec.trans (hprod.trans hmass)

/-- For ANY original observation support with a POSITIVE integer Gram,
the exact odd mass remains below the log of THAT SAME Gram; no
previously proven cardinality property is smuggled in. -/
theorem recovered_mass_le_source_gram_log_375
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (375 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hdet : 0 < (integerRectangularTraceGram Q D (S D) (R D) (S D)).det) :
    recoveredPrimeMassLower (R D) (S D)
      FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram Q D (S D) (R D) (S D)).det : Real) := by
  have hm := recovered_mass_le_exact_odd_375 D hD
  have hsrc := TenthDiscriminant.BinaryThinLogBridge.original_binary_and_exact_odd_mass_log_of_pos
    Q D (R D) (S D) hsq hclass (strict_inertness D) hdet
  have hb : (0 : Real) ≤
      (binaryNullGramExponent (R D) (S D) : Real)*Real.log 2 :=
    mul_nonneg (Nat.cast_nonneg _) (Real.log_nonneg (by norm_num))
  linarith

/-- Actual lower inequality for ONE unchanged positive source Gram,
at 375^4. Upper geometry and a new field cutoff are still open. -/
theorem normalized_source_gram_lower_375
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (375 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hdet : 0 < (integerRectangularTraceGram Q D (S D) (R D) (S D)).det) :
    (999997/1000000 : Real)*Real.log D-5739/1000 ≤
      Real.log ((integerRectangularTraceGram Q D (S D) (R D) (S D)).det : Real) /
        comparisonScale (R D) (S D) := by
  have hd := dimensions_375 D hD
  have hp := comparisonScale_pos (R D) (S D) (by omega) (by omega)
  have hm := recovered_mass_le_source_gram_log_375 Q D hD hsq hclass hdet
  have hnorm := recovered_normalized_lower_375 D hD
  have hdiv := div_le_div_of_nonneg_right hm hp.le
  linarith

end
end TenthDiscriminant.FirstCertificate.Tuned
