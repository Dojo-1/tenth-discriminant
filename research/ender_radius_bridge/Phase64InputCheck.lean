import TenthDiscriminant

open Lean Elab Command

elab "#phase64_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE64_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.FirstCertificate.rawPrimeMassLower_uniform]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE64_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE64_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE64_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE64_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE64_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"



#check TenthDiscriminant.QuadraticRows.off_axis_area_bound
#check TenthDiscriminant.QuadraticRows.width_integral
#check TenthDiscriminant.QuadraticRows.height_scale
#phase64_inputs TenthDiscriminant.QuadraticRows.width_integral
#phase64_inputs TenthDiscriminant.QuadraticRows.off_axis_area_bound
#print axioms TenthDiscriminant.QuadraticRows.off_axis_area_bound

example (U : Finset (Int × Int)) (a b c t : Real)
    (ha : 0 < a) (hD : 0 < 4*a*c-b^2) (ht : 0 ≤ t)
    (hQ : ∀ p ∈ U, a*(p.1 : Real)^2+b*(p.1 : Real)*(p.2 : Real)+c*(p.2 : Real)^2 ≤ t)
    (hy : ∀ p ∈ U, p.2 ≠ 0) :
    (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt (4*a*c-b^2)+4*Real.sqrt (a*t/(4*a*c-b^2)) :=
  TenthDiscriminant.QuadraticRows.off_axis_area_bound U a b c t ha hD ht hQ hy
