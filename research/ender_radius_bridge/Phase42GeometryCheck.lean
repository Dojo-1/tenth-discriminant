import TenthDiscriminant

/-! Verify only the accepted geometry/lower bridge after the full cutoff
attempt's resource stop. This does not run the unaccepted upper candidate. -/
open Lean Elab Command

elab "#geometry_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "GEOMETRY_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
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
    if state.visited.contains name then throwError "GEOMETRY_FORBIDDEN_INPUT {target}: {name}"
  for name in state.visited do
    match env.checked.get.find? name with
    | none => throwError "GEOMETRY_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "GEOMETRY_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "GEOMETRY_NONSTANDARD_AXIOM {name}"
  logInfo m!"GEOMETRY_INPUTS_OK {target}: {state.visited.size} reached; none of16 listed cutoff/classification/finite-answer inputs; axioms {state.axioms}"

#check TenthDiscriminant.FirstCertificate.Tuned.dimensions
#check TenthDiscriminant.FirstCertificate.Tuned.radius_bounds
#check TenthDiscriminant.FirstCertificate.Tuned.chosen_radius
#check TenthDiscriminant.FirstCertificate.Tuned.normalized_lower
#check TenthDiscriminant.FirstCertificate.Tuned.unguarded_radius_rounding_rejected
#check TenthDiscriminant.FirstCertificate.Tuned.inclusive_inertness_endpoint_rejected
#check TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b
#geometry_inputs TenthDiscriminant.FirstCertificate.Tuned.chosen_radius
#geometry_inputs TenthDiscriminant.FirstCertificate.Tuned.normalized_lower

-- No new cutoff roots are present in this partial library.
run_cmd do
  let env ← getEnv
  for name in #[`TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b,
      `TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b] do
    if env.contains name then throwError "UNACCEPTED_CUTOFF_LEAKED {name}"
  logInfo "NO_UNACCEPTED_100B_CUTOFF_IN_LIBRARY"

example : NumberField.classNumber (TenthDiscriminant.ImaginaryQuadraticField 1)=1 :=
  TenthDiscriminant.known_nine_classNumber_one 1 (by decide)
example : NumberField.classNumber (TenthDiscriminant.ImaginaryQuadraticField 2)=1 :=
  TenthDiscriminant.known_nine_classNumber_one 2 (by decide)
example : NumberField.classNumber (TenthDiscriminant.ImaginaryQuadraticField 163)=1 :=
  TenthDiscriminant.known_nine_classNumber_one 163 (by decide)
