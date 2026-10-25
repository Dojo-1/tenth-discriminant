import TenthDiscriminant

/-! UNEXECUTED full-cutoff input-check candidate. Phase42 hit its resource
cap before cutoff acceptance, so the named new cutoff roots are unavailable
in the library. Retained as planned checks, not verification evidence. -/
open Lean Elab Command

elab "#tuned_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "TUNED_ROOT_MISSING {target}"
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
    if state.visited.contains name then
      throwError "TUNED_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "TUNED_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "TUNED_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "TUNED_NONSTANDARD_AXIOM {name}"
  logInfo m!"TUNED_INPUTS_OK {target}: {count} reached; none of16 listed old-cutoff/classification/finite-answer/fixed-ratio inputs; axioms {state.axioms}"

#check TenthDiscriminant.FirstCertificate.Tuned.dimensions
#check TenthDiscriminant.FirstCertificate.Tuned.chosen_radius
#check TenthDiscriminant.FirstCertificate.Tuned.unguarded_radius_rounding_rejected
#check TenthDiscriminant.FirstCertificate.Tuned.inclusive_inertness_endpoint_rejected
#check TenthDiscriminant.FirstCertificate.aspect_ratio_floor25_equality_rejected
#check TenthDiscriminant.FirstCertificate.candidate_aspect_affine_separation
#check TenthDiscriminant.FirstCertificate.candidate_aspect_log25_rejected
#check TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b
#check TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b
#check TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b
#print axioms TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b
#tuned_inputs TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one
#tuned_inputs TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b
#tuned_inputs TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b

-- Positive controls belong here, not among the cutoff proof's inputs.
example : NumberField.classNumber (TenthDiscriminant.ImaginaryQuadraticField 1)=1 :=
  TenthDiscriminant.known_nine_classNumber_one 1 (by decide)
example : NumberField.classNumber (TenthDiscriminant.ImaginaryQuadraticField 2)=1 :=
  TenthDiscriminant.known_nine_classNumber_one 2 (by decide)
example : NumberField.classNumber (TenthDiscriminant.ImaginaryQuadraticField 163)=1 :=
  TenthDiscriminant.known_nine_classNumber_one 163 (by decide)
