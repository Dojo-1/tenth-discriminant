import TenthDiscriminant.RadialCutoff

/-! Phase125: one fixed endpoint certificate; no new geometric estimate. -/
namespace TenthDiscriminant.EndpointCutoff
open FirstCertificate RadialCutoff
set_option autoImplicit false
noncomputable section

theorem endpoint_certificate :
    checkPositiveLogBounds 4 47500000000 35 (24582/1000) (24585/1000)=true := by
  norm_num [checkPositiveLogBounds,binaryLogLowerRat,binaryLogUpperRat,
    oddLogPrefixRat,oddLogRemainderRat,Finset.sum_range_succ]

theorem endpoint_log_lower (D : Nat) (hD : 47500000000 ≤ D) :
    (24582/1000 : Real) ≤ Real.log D := by
  have hc := (checkPositiveLogBounds_sound 4 47500000000 35
    (24582/1000) (24585/1000) endpoint_certificate).1
  norm_num at hc
  have hb : (47500000000 : Real) ≤ D := by exact_mod_cast hD
  convert hc.trans (Real.log_le_log (by norm_num : (0 : Real) < 47500000000) hb) using 1 <;> norm_num

theorem endpoint_separation (u : Real) (hu : 24582/1000 ≤ u) :
    (4/5*u-823/1000)+326254/1000000000 ≤ 999997/1000000*u-5739/1000 := by
  linarith

theorem odd_large_classNumber_ne_one_47_5b (D : Nat) (hD : 47500000000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≠1 := by
  intro hc
  have hgeom : 41006250000 ≤ D := by omega
  have hd := Tuned.dimensions D hgeom
  have hp := comparisonScale_pos (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hupper := RadialDetBound.production_normalized_upper D hgeom
  have hactual := div_le_div_of_nonneg_right (recovered_mass_le_actual_log D hgeom hsq hc) hp.le
  have hlower := recovered_normalized_lower D hgeom
  have hsep := endpoint_separation (Real.log D) (endpoint_log_lower D hD)
  linarith

theorem imaginaryQuadratic_large_classNumber_ne_one_47_5b (d : Nat)
    [Fact (0<d)] (hsq : Squarefree d) (hd : 47500000000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_47_5b d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

theorem imaginaryQuadratic_classNumber_one_discriminant_bound_47_5b
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs < 47500000000 := by
  have hrad : d < 47500000000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_47_5b d hsq (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter,ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter,if_neg hnot]
    omega

theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_47_5b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 47500000000 := by
  obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_47_5b d hsq hcan

theorem endpoint_controls :
    (41006250000 : Nat) ≤ 47500000000 ∧ 47500000000 < 48000000000 ∧
    (0 : Real) < 326254/1000000000 := by norm_num

theorem coarse_endpoint_control :
    ¬(4/5*(2458/100 : Real)-823/1000 < 999997/1000000*(2458/100)-5739/1000) := by
  exact RadialJetMajorant.negative_endpoint_control

theorem nonpositive_certificate_controls :
    checkPositiveLogBounds 4 0 0 0 0=false ∧
    checkPositiveLogBounds 4 (-1) 0 0 0=false := by
  norm_num [checkPositiveLogBounds]

end
end TenthDiscriminant.EndpointCutoff
