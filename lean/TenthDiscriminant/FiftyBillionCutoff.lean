import TenthDiscriminant.StrongSmallPrimeRecoveryGain
import TenthDiscriminant.ImaginaryQuadraticRepresentation

/-! A fixed endpoint obtained from recovered existing prime weights.
No earlier cutoff or finite-answer theorem is used in the proof. -/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

theorem log_large_50b (D : Nat) (hD : 50000000000 ≤ D) : (246304/10000 : Real) ≤ Real.log D := by
  have hb : (50000000000 : Real) ≤ D := by exact_mod_cast hD
  have hl := Real.log_le_log (by norm_num : (0 : Real)<50000000000) hb
  have he : (50000000000 : Real)=2^10*5^11 := by norm_num
  rw [he,Real.log_mul (by norm_num : (2 : Real)^10≠0)
    (by norm_num : (5 : Real)^11≠0),Real.log_pow,Real.log_pow] at hl
  norm_num only [Nat.cast_ofNat] at hl
  linarith [Real.log_two_gt_d9,log_five_lower]

theorem fifty_affine_separation (u : Real) (hu : 246304/10000 ≤ u) :
    (4/5 : Real)*u-813/1000 < (999997/1000000 : Real)*u-5820/1000+81/1000 := by
  linarith

theorem fifty_log246_rejected :
    ¬ (4/5 : Real)*(246/10)-813/1000 <
      (999997/1000000 : Real)*(246/10)-5820/1000+81/1000 := by norm_num

theorem fifty_endpoint_identity : (2 : Nat)^10*5^11=50000000000 := by norm_num

theorem fifty_dimensions (D : Nat) (hD : 50000000000 ≤ D) :
    100 ≤ S D ∧ 25*S D ≤ R D ∧ R D ≤ 26*S D := by
  have hd := dimensions D (by omega)
  refine ⟨by omega, ?_, by omega⟩
  unfold S
  omega

theorem fifty_normalized_lower (D : Nat) (hD : 50000000000 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5739/1000 ≤
      recoveredPrimeMassLower (R D) (S D) FirstEnderInterval.tailBudget /
        comparisonScale (R D) (S D) := by
  have hd := fifty_dimensions D (by omega)
  have hh := strong_raw_normalized_add_gain_le_recovered (R D) (S D)
    FirstEnderInterval.tailBudget hd.1 hd.2.1 hd.2.2
  linarith [normalized_lower D (by omega)]

theorem odd_large_classNumber_ne_one_50b (D : Nat) (hD : 50000000000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≠1 := by
  intro hc
  have hd := dimensions D (by omega)
  have hp := comparisonScale_pos (R D) (S D) (by omega) (by omega)
  have hs : 1 ≤ S D := by omega
  have htail := certifiedPrimeMassLower_antitone_tail (R D) (S D) hs
    FirstEnderInterval.tail_le_budget
  have hrec : recoveredPrimeMassLower (R D) (S D) FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower (R D) (S D) (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith
  have hprod := recoveredPrimeMassLower_le_production (R D) (S D)
    (enderTailIntegral 10000) (by omega) hs
  have hactual := ellipse_enderPrimeMassLower_le_counted_upperB D D D (rho D)
    (R D) (S D) (ellipseVerticalBound D (rho D)) 10000
    (by omega) le_rfl le_rfl (by omega) hs (by decide) hd.2.2.2.1 hsq hc
    (strict_inertness D) (radius_lt_R D (by omega)) le_rfl (chosen_radius D (by omega))
  have hsep := fifty_affine_separation (Real.log D) (log_large_50b D hD)
  have hgap : enderUpperB (R D) (S D) (S D) (rho D)
      (ellipsePaddedUpperCount D (rho D) (ellipseVerticalBound D (rho D))) /
      comparisonScale (R D) (S D) <
      recoveredPrimeMassLower (R D) (S D) FirstEnderInterval.tailBudget /
      comparisonScale (R D) (S D) := by
    linarith [normalized_upper D (by omega), fifty_normalized_lower D (by omega)]
  have hg := (div_lt_div_iff_of_pos_right hp).mp hgap
  exact (not_lt_of_ge (hrec.trans (hprod.trans hactual))) hg

end
end TenthDiscriminant.FirstCertificate.Tuned

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

theorem imaginaryQuadratic_large_classNumber_ne_one_50b (d : Nat)
    [Fact (0<d)] (hsq : Squarefree d) (hd : 50000000000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hc
    exact FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

theorem imaginaryQuadratic_classNumber_one_discriminant_bound_50b
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs < 50000000000 := by
  have hrad : d < 50000000000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_50b d hsq (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter,ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter,if_neg hnot]
    omega

theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_50b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2) (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 50000000000 := by
  obtain ⟨d, hd, hsq, a, ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_50b d hsq hcan

end
end TenthDiscriminant
