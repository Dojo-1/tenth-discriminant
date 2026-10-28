import TenthDiscriminant

/-! The field is arbitrary; its quadratic chart is constructed inside the proof. -/
open scoped NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.EvenFieldTwoClass
set_option autoImplicit false
noncomputable section

theorem even_chart_of_even_parameter (d : Nat) (hsq : Squarefree d)
    (heven : Even (absoluteDiscriminantParameter d)) :
    (d : Int)%4=1 ∨ (d : Int)%4=2 := by
  rcases squarefree_mod_four_cases d hsq with hodd | hchart
  · have hd : Even d := by simpa only [absoluteDiscriminantParameter,if_pos hodd] using heven
    obtain ⟨k,hk⟩ := hd
    omega
  · exact hchart

theorem arbitrary_even_discriminant_bound (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K≤2) (heven : Even (NumberField.discr K).natAbs) :
    (NumberField.discr K).natAbs<2^52 := by
  obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hdisc : (NumberField.discr K).natAbs=absoluteDiscriminantParameter d := by
    rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
    exact imaginaryQuadratic_discr_natAbs d hsq
  have hm := even_chart_of_even_parameter d hsq (hdisc ▸ heven)
  have he := OddFieldTwoClass.field_classNumber_eq (ImaginaryQuadraticField d) K e
  have hcan : NumberField.classNumber (ImaginaryQuadraticField d)≤2 := by
    rw [he]
    exact hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  have hb := EvenTwoClass.even_discriminant_bound d hsq hm hcan
  simpa only [show 4*(2 : Nat)^50=2^52 by norm_num] using hb

theorem arbitrary_discriminant_bound (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K≤2) : (NumberField.discr K).natAbs<2^52 := by
  rcases Nat.even_or_odd (NumberField.discr K).natAbs with heven | hodd
  · exact arbitrary_even_discriminant_bound K hdegree hc heven
  · exact lt_trans (OddFieldTwoClass.arbitrary_odd_discriminant_bound K hdegree hc hodd)
      (by norm_num : (2 : Nat)^50<2^52)

theorem parity_refined_discriminant_bound (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K≤2) :
    (Odd (NumberField.discr K).natAbs → (NumberField.discr K).natAbs<2^50) ∧
    (Even (NumberField.discr K).natAbs → (NumberField.discr K).natAbs<2^52) := by
  exact ⟨fun hodd => OddFieldTwoClass.arbitrary_odd_discriminant_bound K hdegree hc hodd,
    fun heven => arbitrary_even_discriminant_bound K hdegree hc heven⟩

theorem classNumber_gt_two_of_large_discriminant (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hlarge : 2^52≤(NumberField.discr K).natAbs) : 2<NumberField.classNumber K := by
  by_contra hn
  have hc : NumberField.classNumber K≤2 := Nat.le_of_not_gt hn
  have hb := arbitrary_discriminant_bound K hdegree hc
  omega

theorem even_parameter_control : absoluteDiscriminantParameter 2=8 := by
  norm_num [absoluteDiscriminantParameter]

theorem odd_parameter_control : absoluteDiscriminantParameter 3=3 := by
  norm_num [absoluteDiscriminantParameter]

theorem factor_four_control : 4*(2 : Nat)^50=2^52 ∧ 4*(2 : Nat)^50≠2^50 := by
  norm_num

theorem odd_chart_exclusion_control : ¬ ((3 : Int)%4=1 ∨ (3 : Int)%4=2) := by
  decide
end
end TenthDiscriminant.EvenFieldTwoClass

#check TenthDiscriminant.EvenFieldTwoClass.even_chart_of_even_parameter
#check TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound
#check TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound
#check TenthDiscriminant.EvenFieldTwoClass.parity_refined_discriminant_bound
#check TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant
#check TenthDiscriminant.EvenFieldTwoClass.even_parameter_control
#check TenthDiscriminant.EvenFieldTwoClass.odd_parameter_control
#check TenthDiscriminant.EvenFieldTwoClass.factor_four_control
#check TenthDiscriminant.EvenFieldTwoClass.odd_chart_exclusion_control
#print axioms TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound
#print axioms TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound
#print axioms TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant
#audit_namespace TenthDiscriminant.EvenFieldTwoClass

open Lean Elab Command

elab "#phase107_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE107_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let common : Array Name := #[
    ``TenthDiscriminant.ellipse_primeMass_product_dvd,
    ``TenthDiscriminant.ellipse_primeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_log_le_hadamard,
    ``TenthDiscriminant.smallPrimeNormLifting_of_classNumber_one,
    ``TenthDiscriminant.smallPrime_nonsquare_of_classNumber_one,
    ``TenthDiscriminant.rectangularTraceGram_valuation_of_classNumber_one,
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
    ``TenthDiscriminant.classNumber_one_of_field_equiv,
    ``TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample]
  let evenOnly : Array Name := #[
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
    ``TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget]
  let forbidden := if target==``TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound
    then common++evenOnly else common
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE107_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE107_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE107_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE107_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE107_INPUTS_OK {target}: {count} reached; {forbidden.size} forbidden roots excluded; axioms {state.axioms}"

#phase107_inputs TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound
#phase107_inputs TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound
#phase107_inputs TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant
