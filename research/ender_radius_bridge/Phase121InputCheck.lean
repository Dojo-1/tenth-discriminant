import TenthDiscriminant

#audit_namespace TenthDiscriminant.RadialJetMajorant
#check TenthDiscriminant.RadialJetMajorant.coefficient_bound
#check TenthDiscriminant.RadialJetMajorant.linear_power_derivative
#check TenthDiscriminant.RadialJetMajorant.leibniz_jet
#check TenthDiscriminant.RadialJetMajorant.opposite_jet
#check TenthDiscriminant.RadialJetMajorant.coefficient_one
#check TenthDiscriminant.RadialJetMajorant.coefficient_no_loss
#check TenthDiscriminant.RadialJetMajorant.centered_disc
#check TenthDiscriminant.RadialJetMajorant.ordinary_jet_no_loss
#check TenthDiscriminant.RadialJetMajorant.high_jet_zero
#check TenthDiscriminant.RadialJetMajorant.ordinary_jet_gain
#check TenthDiscriminant.RadialJetMajorant.logarithm_gain
#check TenthDiscriminant.RadialJetMajorant.scale_gain
#check TenthDiscriminant.RadialJetMajorant.endpoint_separation
#check TenthDiscriminant.RadialJetMajorant.coefficient_controls
#check TenthDiscriminant.RadialJetMajorant.zero_s_control
#check TenthDiscriminant.RadialJetMajorant.ordinary_controls
#check TenthDiscriminant.RadialJetMajorant.rounding_control
#check TenthDiscriminant.RadialJetMajorant.single_column_control
#check TenthDiscriminant.RadialJetMajorant.negative_endpoint_control
#print TenthDiscriminant.RadialJetMajorant.coefficient
#print TenthDiscriminant.RadialJetMajorant.jet


#audit_namespace TenthDiscriminant.RadialDetBound
#check TenthDiscriminant.RadialDetBound.chart_pair
#check TenthDiscriminant.RadialDetBound.actual_jet_value
#check TenthDiscriminant.RadialDetBound.trace_square
#check TenthDiscriminant.RadialDetBound.actual_diagonal
#check TenthDiscriminant.RadialDetBound.rowFactor_pos
#check TenthDiscriminant.RadialDetBound.rowFactor_log
#check TenthDiscriminant.RadialDetBound.actual_jet_square
#check TenthDiscriminant.RadialDetBound.actual_diagonal_uniform
#check TenthDiscriminant.RadialDetBound.actual_log_diagonal
#check TenthDiscriminant.RadialDetBound.penalty_sum
#check TenthDiscriminant.RadialDetBound.baseline_sum
#check TenthDiscriminant.RadialDetBound.integer_log_upper
#check TenthDiscriminant.RadialDetBound.normalized_integer_upper
#check TenthDiscriminant.RadialDetBound.production_guards
#check TenthDiscriminant.RadialDetBound.production_normalized_upper
#check TenthDiscriminant.RadialDetBound.constant_trace_control
#check TenthDiscriminant.RadialDetBound.empty_rows_control
#check TenthDiscriminant.RadialDetBound.singleton_control
#check TenthDiscriminant.RadialDetBound.singular_control
#check TenthDiscriminant.RadialDetBound.origin_control
#check TenthDiscriminant.RadialDetBound.single_column_control
#check TenthDiscriminant.RadialDetBound.empty_eligible_control
#print TenthDiscriminant.RadialDetBound.chart
#print TenthDiscriminant.RadialDetBound.rowFactor
#print TenthDiscriminant.RadialDetBound.rowPenalty
#print TenthDiscriminant.RadialDetBound.rowLog


#audit_namespace TenthDiscriminant.RadialCutoff
#check TenthDiscriminant.RadialCutoff.integer_det_positive
#check TenthDiscriminant.RadialCutoff.prime_mass_log_lower
#check TenthDiscriminant.RadialCutoff.recovered_normalized_lower
#check TenthDiscriminant.RadialCutoff.recovered_mass_le_actual_log
#check TenthDiscriminant.RadialCutoff.endpoint_log_controls
#check TenthDiscriminant.RadialCutoff.endpoint_log_lower
#check TenthDiscriminant.RadialCutoff.odd_large_classNumber_ne_one_48b
#check TenthDiscriminant.RadialCutoff.imaginaryQuadratic_large_classNumber_ne_one_48b
#check TenthDiscriminant.RadialCutoff.imaginaryQuadratic_classNumber_one_discriminant_bound_48b
#check TenthDiscriminant.RadialCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_48b
#check TenthDiscriminant.RadialCutoff.endpoint_identity
#check TenthDiscriminant.RadialCutoff.negative_endpoint_control
#check TenthDiscriminant.RadialCutoff.empty_prime_product_control
#check TenthDiscriminant.RadialCutoff.duplicate_prime_control
#check TenthDiscriminant.RadialCutoff.actual_even_discriminant_control


open Lean Elab Command
elab "#phase121_geom_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE121_GEOM_ROOT_MISSING {target}"
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
      throwError "PHASE121_GEOM_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE121_GEOM_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE121_GEOM_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE121_GEOM_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE121_GEOM_INPUTS_OK {target}: {count} reached;70forbidden roots excluded;axioms {state.axioms}"





open Lean Elab Command
elab "#phase121_arith_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE121_ARITH_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
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
      throwError "PHASE121_ARITH_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE121_ARITH_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE121_ARITH_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE121_ARITH_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE121_ARITH_INPUTS_OK {target}: {count} reached;73forbidden roots excluded;axioms {state.axioms}"






#phase121_geom_inputs TenthDiscriminant.RadialJetMajorant.coefficient_bound
#phase121_geom_inputs TenthDiscriminant.RadialJetMajorant.ordinary_jet_gain
#phase121_geom_inputs TenthDiscriminant.RadialJetMajorant.scale_gain
#phase121_geom_inputs TenthDiscriminant.RadialDetBound.actual_diagonal
#phase121_geom_inputs TenthDiscriminant.RadialDetBound.integer_log_upper
#phase121_geom_inputs TenthDiscriminant.RadialDetBound.production_normalized_upper
#phase121_arith_inputs TenthDiscriminant.RadialCutoff.prime_mass_log_lower
#phase121_arith_inputs TenthDiscriminant.RadialCutoff.odd_large_classNumber_ne_one_48b
#phase121_arith_inputs TenthDiscriminant.RadialCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_48b
