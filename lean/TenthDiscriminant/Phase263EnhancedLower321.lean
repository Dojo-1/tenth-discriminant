import TenthDiscriminant.Phase262HorizontalLogBridge321
import TenthDiscriminant.SourcePositivity321
import TenthDiscriminant.Lower322
import TenthDiscriminant.BinaryGap375

/-!
# Phase263: 321⁴ lower envelope on the same positive original Gram

Unlike the older 322⁴ specialization, every source-size, prime-tail and
log-floor hypothesis is re-established at 321⁴. The original thin-Q
ordinary-jet trace Gram is unchanged. The once-counted horizontal p²
mass from Phase262 is added only after the exact odd-prime comparison.

This file proves a *lower* bound, not the required 321⁴ analytic upper
or the actual-field exclusion. It does not use the nine-field theorem.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
open TenthDiscriminant.RadialCutoff
set_option autoImplicit false
noncomputable section

/-- The same production R=floor(D/4), S=floor(R/25) at 321⁴.
The old 322⁴ dimensions theorem is NOT invoked. -/
theorem dimensions_321 (D : Nat) (hD : (321 : Nat)^4 ≤ D) :
    100000000 ≤ R D ∧ 500000 ≤ S D ∧ 10*R D ≤ 251*S D ∧
    R D ≤ 10000*S D ∧ (D : Real)/5 ≤ R D ∧
    (R D : Real) ≤ (D : Real)/4 ∧ (S D : Real) ≤ (R D : Real)/25 := by
  have hlo : D ≤ 5*(D/4) := by omega
  have hhi : 4*(D/4) ≤ D := by omega
  have hs : 25*((D/4)/25) ≤ D/4 := by omega
  refine ⟨by unfold R envelopeR; omega, by unfold S R envelopeR; omega,
    by unfold S R envelopeR; omega, by unfold S R envelopeR; omega,
    ?_, ?_, ?_⟩
  · have h : (D : Real) ≤ 5*(D/4 : Nat) := by exact_mod_cast hlo
    change (D : Real)/5 ≤ (D/4 : Nat)
    linarith
  · have h : 4*((D/4 : Nat) : Real) ≤ D := by exact_mod_cast hhi
    change ((D/4 : Nat) : Real) ≤ (D : Real)/4
    linarith
  · have h : 25*(((D/4)/25 : Nat) : Real) ≤ (D/4 : Nat) := by
      exact_mod_cast hs
    change (((D/4)/25 : Nat) : Real) ≤ ((D/4 : Nat) : Real)/25
    linarith

/-- A sound log(D) floor at the smaller fourth root; no 322-domain
log bound is transported across a weaker hypothesis. -/
theorem log_floor_from_321_fourth_power (D : Nat)
    (hD : (321 : Nat)^4 ≤ D) :
    (230856/10000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) < (((321 : Nat)^4 : Nat) : Real) := by
    norm_num
  have hDreal : (((321 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [Nat.cast_pow, Real.log_pow] at hm
  have h321 := TenthDiscriminant.log_321_rational_enclosure.1
  linarith

/-- The original R floor ratio, with its actual 321-domain guard. -/
theorem log_R_lower_321 (D : Nat) (hD : (321 : Nat)^4 ≤ D) :
    Real.log (D : Real)-13904/10000 ≤ Real.log (R D) := by
  have hn : 249*D ≤ 1000*R D := by
    simpa [R] using
      (FirstCertificate.envelope_floor_ratio D (by omega))
  have hr : (249 : Real)*D ≤ 1000*R D := by
    exact_mod_cast hn
  have hp : (0 : Real) < D := by
    exact_mod_cast (show 0 < D by omega)
  have hR : (D : Real)/(1000/249) ≤ R D := by
    apply (div_le_iff₀ (by norm_num : (0 : Real) < 1000/249)).2
    linarith
  have hl := Real.log_le_log (div_pos hp (by norm_num)) hR
  rw [Real.log_div hp.ne' (by norm_num : (1000/249 : Real) ≠ 0)] at hl
  linarith [TenthDiscriminant.log_floor_ratio_upper_13904]

/-- Re-run the original aspect-ratio estimate at 321⁴, using the
same raw prime mass and the sound 321 log floor. -/
theorem normalized_lower_321 (D : Nat) (hD : (321 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-58094/10000 ≤
      rawPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_321 D hD
  have hl := log_R_lower_321 D hD
  have hu := log_floor_from_321_fourth_power D hD
  have hr : (10 : Real)*R D ≤ 251*S D := by
    exact_mod_cast hd.2.2.1
  have hratio : (R D : Real) ≤ (251/10)*S D := by linarith
  have hm := aspect_ratio_25_point_1_control (R D) (S D)
    hd.1 hd.2.1 hratio (by linarith)
  linarith

/-- The original +0.0901 recovery is dimension-only and remains
valid at 321⁴. No additional prime is introduced. -/
theorem recovered_normalized_lower_321 (D : Nat)
    (hD : (321 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-57193/10000 ≤
      recoveredPrimeMassLower (R D) (S D)
        FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions_321 D hD
  have hS : 500000 ≤ S D := hd.2.1
  have h25 : 25*S D ≤ R D := by unfold S; omega
  have hfloor : R D ≤ 25*S D+24 := by unfold S; omega
  have hh := phase200_raw_normalized_add_gain_322 (R D) (S D)
    FirstEnderInterval.tailBudget hS h25 hfloor
  linarith [normalized_lower_321 D hD]

/-- Exact old odd-prime mass dominates the recovered lower mass.
The only needed source guard is R<=10000*S, re-proved above. -/
theorem recovered_mass_le_exact_odd_321 (D : Nat)
    (hD : (321 : Nat)^4 ≤ D) :
    recoveredPrimeMassLower (R D) (S D)
      FirstEnderInterval.tailBudget ≤
      exactOddPrimeMass (R D) (S D) := by
  have hd := dimensions_321 D hD
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

end
end TenthDiscriminant.FirstCertificate.Tuned

namespace TenthDiscriminant
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- For ANY original observation support with positive trace Gram,
the 321⁴ normalized lower uses the old recovered prime mass, exactly
one 2-primary factor, and exactly one horizontal p² contribution. -/
theorem original_source_enhanced_normalized_lower_of_pos_321
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (321 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hpositive : 0 < (integerRectangularTraceGram Q D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det) :
    (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) ≤
    Real.log ((integerRectangularTraceGram Q D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
      comparisonScale (Tuned.R D) (Tuned.S D) := by
  have hd := Tuned.dimensions_321 D hD
  have hp := comparisonScale_pos (Tuned.R D) (Tuned.S D)
    (by omega) (by omega)
  have hsource :=
    Phase262.original_binary_odd_plus_horizontal_log_of_pos
      Q D (Tuned.R D) (Tuned.S D)
      hsq hc (Tuned.strict_inertness D) (by omega) hpositive
  have hodd := Tuned.recovered_mass_le_exact_odd_321 D hD
  have hmass :
      (binaryNullGramExponent (Tuned.R D) (Tuned.S D) : Real)*
        Real.log 2 +
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
        FirstEnderInterval.tailBudget +
      (Phase259.horizontalPrimeMass (Tuned.R D) (Tuned.S D) : Real)/500 ≤
      Real.log ((integerRectangularTraceGram Q D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) := by
    linarith
  have hdiv := div_le_div_of_nonneg_right hmass hp.le
  rw [add_div, add_div] at hdiv
  have hbase := Tuned.recovered_normalized_lower_321 D hD
  have hbin := normalized_binary_quarter
    (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hgain := Phase259.production_horizontal_gain_lower D hD
  change (4659/625000 : Real)-16895455/(625000*(D : Real)) ≤
    (Phase259.horizontalPrimeMass (Tuned.R D) (Tuned.S D) : Real)/500 /
      comparisonScale (Tuned.R D) (Tuned.S D) at hgain
  linarith

/-- Same original THIN ellipse Gram at 321⁴, with positivity from
the 321 source-geometry module and no 322-domain geometry hypothesis. -/
theorem thin_original_enhanced_normalized_lower_321
    (D : Nat) (hD : (321 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) ≤
    Real.log ((integerRectangularTraceGram
      (ellipsePairs D (Tuned.thinRadius D)) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
      comparisonScale (Tuned.R D) (Tuned.S D) := by
  exact original_source_enhanced_normalized_lower_of_pos_321
    (ellipsePairs D (Tuned.thinRadius D)) D hD hsq hc
    (Tuned.thin_original_gram_pos_321 D hD)

end
end TenthDiscriminant

#print axioms TenthDiscriminant.FirstCertificate.Tuned.dimensions_321
#print axioms TenthDiscriminant.FirstCertificate.Tuned.recovered_normalized_lower_321
#print axioms TenthDiscriminant.FirstCertificate.Tuned.recovered_mass_le_exact_odd_321
#print axioms TenthDiscriminant.original_source_enhanced_normalized_lower_of_pos_321
#print axioms TenthDiscriminant.thin_original_enhanced_normalized_lower_321
