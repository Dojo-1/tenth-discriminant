import TenthDiscriminant

#check TenthDiscriminant.EndpointCutoff.endpoint_certificate
#check TenthDiscriminant.EndpointCutoff.endpoint_log_lower
#check TenthDiscriminant.EndpointCutoff.endpoint_separation
#check TenthDiscriminant.EndpointCutoff.odd_large_classNumber_ne_one_47_5b
#check TenthDiscriminant.EndpointCutoff.imaginaryQuadratic_large_classNumber_ne_one_47_5b
#check TenthDiscriminant.EndpointCutoff.imaginaryQuadratic_classNumber_one_discriminant_bound_47_5b
#check TenthDiscriminant.EndpointCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_47_5b
#check TenthDiscriminant.EndpointCutoff.endpoint_controls
#check TenthDiscriminant.EndpointCutoff.coarse_endpoint_control
#check TenthDiscriminant.EndpointCutoff.nonpositive_certificate_controls


#audit_namespace TenthDiscriminant.EndpointCutoff

open Lean Elab Command
elab "#phase128_125_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE125_ROOT_MISSING {target}"
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
      throwError "PHASE125_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE125_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE125_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE125_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE125_INPUTS_OK {target}: {count} reached;77forbidden roots excluded;axioms {state.axioms}"

#phase128_125_inputs TenthDiscriminant.EndpointCutoff.endpoint_certificate
#phase128_125_inputs TenthDiscriminant.EndpointCutoff.odd_large_classNumber_ne_one_47_5b
#phase128_125_inputs TenthDiscriminant.EndpointCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_47_5b

#check TenthDiscriminant.FieldClassification.field_classNumber_one_iff
#check TenthDiscriminant.FieldClassification.field_classNumber_one_discriminant_mem


#audit_namespace TenthDiscriminant.FieldClassification

open Lean Elab Command
elab "#phase128_126_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE126_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let required : Array Name := #[
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff,
    ``TenthDiscriminant.exists_squarefree_root_of_totallyComplex_degree_two,
    ``TenthDiscriminant.imaginaryQuadraticEquivOfRoot,
    ``TenthDiscriminant.classNumber_one_of_field_equiv]
  for name in required do
    unless state.visited.contains name do
      throwError "PHASE126_REQUIRED_INPUT_MISSING {target}: {name}"
  let forbidden : Array Name := #[
    ``TenthDiscriminant.RadialCutoff.odd_large_classNumber_ne_one_48b,
    ``TenthDiscriminant.RadialCutoff.imaginaryQuadratic_large_classNumber_ne_one_48b,
    ``TenthDiscriminant.RadialCutoff.imaginaryQuadratic_classNumber_one_discriminant_bound_48b,
    ``TenthDiscriminant.RadialCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_48b,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE126_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE126_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE126_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE126_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE126_INPUTS_OK {target}: {count} reached;4required/8forbidden;axioms {state.axioms}"

#phase128_126_inputs TenthDiscriminant.FieldClassification.field_classNumber_one_iff
#phase128_126_inputs TenthDiscriminant.FieldClassification.field_classNumber_one_discriminant_mem

#check TenthDiscriminant.RadialAction.matrix_zero
#check TenthDiscriminant.RadialAction.matrix_add
#check TenthDiscriminant.RadialAction.matrix_neg
#check TenthDiscriminant.RadialAction.matrix_commute
#check TenthDiscriminant.RadialAction.transform_add
#check TenthDiscriminant.RadialAction.gram_add
#check TenthDiscriminant.RadialAction.nonmultiplicative_control


#audit_namespace TenthDiscriminant.RadialAction

open Lean Elab Command
elab "#phase128_127_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE127_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  unless state.visited.contains ``TenthDiscriminant.RadialOperator.matrix do
    throwError "PHASE127_ACTUAL_MATRIX_MISSING {target}"
  let forbidden : Array Name := #[
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
      throwError "PHASE127_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE127_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE127_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE127_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE127_INPUTS_OK {target}: {count} reached;70forbidden roots excluded;axioms {state.axioms}"

#phase128_127_inputs TenthDiscriminant.RadialAction.matrix_add
#phase128_127_inputs TenthDiscriminant.RadialAction.transform_add
#phase128_127_inputs TenthDiscriminant.RadialAction.gram_add

