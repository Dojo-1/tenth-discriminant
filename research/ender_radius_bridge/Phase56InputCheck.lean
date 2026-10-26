import TenthDiscriminant

/-! Fresh Phase56 exact cutoff signatures, inputs and controls.
No earlier provenance inventory is transferred to these new roots. -/
open Lean Elab Command

elab "#tuned_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "TUNED_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
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
  logInfo m!"TUNED_INPUTS_OK {target}: {count} reached; none of25 listed old-cutoff/classification/finite-answer/fixed-ratio inputs; axioms {state.axioms}"



#check TenthDiscriminant.FirstCertificate.recovery_log_controls
#check TenthDiscriminant.FirstCertificate.strong_recovered_scale_gain
#check TenthDiscriminant.FirstCertificate.strong_gain_missing_S_guard_rejected
#check TenthDiscriminant.FirstCertificate.Tuned.log_large_geometry
#check TenthDiscriminant.FirstCertificate.Tuned.log_large_50b
#check TenthDiscriminant.FirstCertificate.Tuned.fifty_endpoint_identity
#check TenthDiscriminant.FirstCertificate.Tuned.fifty_log246_rejected
#check TenthDiscriminant.FirstCertificate.Tuned.unguarded_radius_rounding_rejected
#check TenthDiscriminant.FirstCertificate.Tuned.inclusive_inertness_endpoint_rejected
#check TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b
#print axioms TenthDiscriminant.FirstCertificate.strong_recovered_scale_gain
#print axioms TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b
#tuned_inputs TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b
#tuned_inputs TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_50b
#tuned_inputs TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b
example : (450 : Nat)^4=41006250000 := by norm_num
example (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2) (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 50000000000 :=
  TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b K hdegree hc
