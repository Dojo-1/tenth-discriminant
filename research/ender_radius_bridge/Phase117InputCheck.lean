import TenthDiscriminant

#audit_namespace TenthDiscriminant.RadialOperator
#check TenthDiscriminant.RadialOperator.term_bounds
#check TenthDiscriminant.RadialOperator.target_in_range
#check TenthDiscriminant.RadialOperator.targetFin_labels
#check TenthDiscriminant.RadialOperator.lower_triangular
#check TenthDiscriminant.RadialOperator.diagonal_one
#check TenthDiscriminant.RadialOperator.determinant_one
#check TenthDiscriminant.RadialOperator.integral_inverse
#check TenthDiscriminant.RadialOperator.polynomial_expansion
#check TenthDiscriminant.RadialOperator.row_action
#check TenthDiscriminant.RadialOperator.polynomial_action
#check TenthDiscriminant.RadialOperator.jet_action
#check TenthDiscriminant.RadialOperator.complex_jet_action
#check TenthDiscriminant.RadialOperator.integer_jet_action
#check TenthDiscriminant.RadialOperator.gram_congruence
#check TenthDiscriminant.RadialOperator.gram_det
#check TenthDiscriminant.RadialOperator.gram_map
#check TenthDiscriminant.RadialOperator.real_cast
#check TenthDiscriminant.RadialOperator.mapped_det_one
#check TenthDiscriminant.RadialOperator.real_posSemidef
#check TenthDiscriminant.RadialOperator.real_posDef
#check TenthDiscriminant.RadialOperator.reduced_rank
#check TenthDiscriminant.RadialOperator.integer_bridge
#check TenthDiscriminant.RadialOperator.empty_control
#check TenthDiscriminant.RadialOperator.pilot_row_control
#check TenthDiscriminant.RadialOperator.ordinary_controls
#check TenthDiscriminant.RadialOperator.origin_and_ring_controls
#check TenthDiscriminant.RadialOperator.reduction_control
#print TenthDiscriminant.RadialOperator.target
#print TenthDiscriminant.RadialOperator.matrix
#print TenthDiscriminant.RadialOperator.targetFin
#print TenthDiscriminant.RadialOperator.polynomial
#print TenthDiscriminant.RadialOperator.integerJet
#print TenthDiscriminant.RadialOperator.gram

open Lean Elab Command
elab "#phase117_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE117_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
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
      throwError "PHASE117_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE117_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE117_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE117_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE117_INPUTS_OK {target}: {count} reached;70forbidden roots excluded;axioms {state.axioms}"


#phase117_inputs TenthDiscriminant.RadialOperator.polynomial_action

#phase117_inputs TenthDiscriminant.RadialOperator.complex_jet_action

#phase117_inputs TenthDiscriminant.RadialOperator.integer_bridge
