import TenthDiscriminant.QuadraticDiscriminant

/-! A direct smaller analytic cutoff for the same auxiliary family.
No classification, nine-positive theorem or finite certificate is used. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem sharp_affine_envelopes_separated (u : Real) (hu : 26≤u) :
    (13/16 : Real)*u-1593/2000 < (999997/1000000 : Real)*u-5635/1000 := by
  linarith

theorem sharp_affine_log25_rejected :
    ¬ (13/16 : Real)*25-1593/2000 < (999997/1000000 : Real)*25-5635/1000 := by
  norm_num

theorem odd_large_classNumber_ne_one_200b (D : Nat) (hD : 200000000000≤D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≠1 := by
  have hd := envelope_dimensions D hD
  apply classNumber_ne_one_of_certified_budget_comparison D D D (envelopeRadius D)
    (envelopeR D) (envelopeS D) (ellipseVerticalBound D (envelopeRadius D))
    (by omega) le_rfl le_rfl (by omega) (by omega) hd.2.2.2.1 hsq
    (envelope_strict_inertness D) (envelope_radius_lt_R D hD) le_rfl
    (envelope_chosen_radius D hD)
  have ht := comparisonScale_pos (envelopeR D) (envelopeS D) (by omega) (by omega)
  have hu := envelope_normalized_upper D hD
  have hl := envelope_normalized_lower_sharp D hD
  have hg := sharp_affine_envelopes_separated (Real.log D) (moderate_D_log D hD)
  have hh := lt_of_le_of_lt hu (hg.trans_le hl)
  have hraw := (div_lt_div_iff_of_pos_right ht).mp hh
  exact hraw.trans_le (rawPrimeMassLower_le_certified _ _ _)

end
end TenthDiscriminant.FirstCertificate

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

theorem imaginaryQuadratic_large_classNumber_ne_one_200b (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hd : 200000000000≤d) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hc
    exact FirstCertificate.odd_large_classNumber_ne_one_200b d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

theorem imaginaryQuadratic_classNumber_one_radicand_bound_200b (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    d<200000000000 := by
  by_contra h
  exact imaginaryQuadratic_large_classNumber_ne_one_200b d hsq (by omega) hc

theorem imaginaryQuadratic_classNumber_one_discriminant_bound_200b (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs<200000000000 := by
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter,ho] using
      imaginaryQuadratic_classNumber_one_radicand_bound_200b d hsq hc
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter,if_neg hnot]
    omega

end
end TenthDiscriminant
