import TenthDiscriminant
import TenthDiscriminant.RadialCutoff

/-! Phase122: one fixed endpoint certificate; no new geometric estimate. -/
namespace TenthDiscriminant.Phase122Endpoint
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
  exact hc.trans (Real.log_le_log (by norm_num : (0 : Real) < 47500000000) hb)

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
end TenthDiscriminant.Phase122Endpoint

#audit_namespace TenthDiscriminant.Phase122Endpoint

open Lean Elab Command
elab "#phase122_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE122_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
    ``TenthDiscriminant.RadialCutoff.odd_large_classNumber_ne_one_48b,
    ``TenthDiscriminant.RadialCutoff.imaginaryQuadratic_large_classNumber_ne_one_48b,
    ``TenthDiscriminant.RadialCutoff.imaginaryQuadratic_classNumber_one_discriminant_bound_48b,
    ``TenthDiscriminant.RadialCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_48b,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.FirstCertificate.Tuned.fifty_normalized_lower,
    ``TenthDiscriminant.FirstCertificate.Tuned.fifty_dimensions,
    ``TenthDiscriminant.ellipse_enderPrimeMassLower_le_counted_upperB,
    ``TenthDiscriminant.ellipse_enderPrimeMassLower_le_upperB,
    ``TenthDiscriminant.ellipse_primeMass_log_le_upperB,
    ``TenthDiscriminant.ellipse_primeMass_product_dvd,
    ``TenthDiscriminant.ellipse_primeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_log_le_hadamard,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff,
    ``TenthDiscriminant.known_nine_classNumber_one,
    ``TenthDiscriminant.phase36_all_fibers,
    ``TenthDiscriminant.classNumber_one_candidates_below_million,
    ``TenthDiscriminant.classNumber_one_iff_below_million,
    ``TenthDiscriminant.phase35_q0_translate,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_parameter_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b,
    ``TenthDiscriminant.FirstCertificate.rawPrimeMassLower_uniform,
    ``TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two,
    ``TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound,
    ``TenthDiscriminant.ControlledClassCount.controlled_class_form_and_count,
    ``TenthDiscriminant.PrincipalBasis.principal_form_of_class,
    ``TenthDiscriminant.PrincipalBasis.principal_class_form_and_prime_count,
    ``TenthDiscriminant.ActualPrimeAxis.actual_axis_card_le_two,
    ``TenthDiscriminant.ActualPrimeAxis.controlled_class_prime_count,
    ``TenthDiscriminant.ControlledPrimeFamily.controlled_family,
    ``TenthDiscriminant.ControlledPrimeFamily.fixed_family_odd_four,
    ``TenthDiscriminant.ControlledPrimeFamily.fixed_family_finite,
    ``TenthDiscriminant.ResidueMultiplicity.actualResidueMap,
    ``TenthDiscriminant.ResidueMultiplicity.actual_residue_pair_ne,
    ``TenthDiscriminant.ClassAggregation.prime_prefix_bound,
    ``TenthDiscriminant.ClassAggregation.uniform_two_class_bound,
    ``TenthDiscriminant.SplitPrimeBudget.countBound,
    ``TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound,
    ``TenthDiscriminant.SplitPrimeBudget.actual_gram_budget,
    ``TenthDiscriminant.ClosedKernel.actual_majorant,
    ``TenthDiscriminant.ClosedKernel.closed_count_kernel,
    ``TenthDiscriminant.ClosedKernel.closed_actual_gram_budget,
    ``TenthDiscriminant.OddMinkowski.actual_minkowski,
    ``TenthDiscriminant.OddMinkowski.normalized_count_kernel,
    ``TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget,
    ``TenthDiscriminant.EvenTwoClass.even_classNumber_gt_two,
    ``TenthDiscriminant.EvenTwoClass.even_radicand_bound,
    ``TenthDiscriminant.EvenTwoClass.even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.parity_refined_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant,
    ``TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_cast,
    ``TenthDiscriminant.CoordinateTranslation.shifted_posDef,
    ``TenthDiscriminant.CoordinateTranslation.shifted_valuation,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE122_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE122_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE122_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE122_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE122_INPUTS_OK {target}: {count} reached;77forbidden roots excluded;axioms {state.axioms}"

#phase122_inputs TenthDiscriminant.Phase122Endpoint.endpoint_certificate
#phase122_inputs TenthDiscriminant.Phase122Endpoint.odd_large_classNumber_ne_one_47_5b
#phase122_inputs TenthDiscriminant.Phase122Endpoint.totallyComplex_degree_two_classNumber_one_discriminant_bound_47_5b
