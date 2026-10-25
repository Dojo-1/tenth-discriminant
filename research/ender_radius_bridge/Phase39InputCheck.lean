import TenthDiscriminant

/-! A new cutoff needs its own input check; the frozen Phase38 snapshot is
not automatically transferred to these changed mathematical sources. -/
open Lean Elab Command

elab "#analytic_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "ANALYTIC_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound]
  for name in forbidden do
    if state.visited.contains name then
      throwError "ANALYTIC_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "ANALYTIC_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "ANALYTIC_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "ANALYTIC_NONSTANDARD_AXIOM {name}"
  logInfo m!"ANALYTIC_INPUTS_OK {target}: {count} reached; no listed classification, certificate or old cutoff input; axioms {state.axioms}"

#check TenthDiscriminant.FirstCertificate.sharp_affine_envelopes_separated
#check TenthDiscriminant.FirstCertificate.sharp_affine_log25_rejected
#check TenthDiscriminant.FirstCertificate.envelope_floor_ratio
#check TenthDiscriminant.FirstCertificate.envelope_floor_ratio_without_guard_rejected
#check TenthDiscriminant.FirstCertificate.smaller_log_threshold_rejected
#check TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one
#check TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff
#check TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b
#check TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b
#print axioms TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b
#analytic_inputs TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one_200b
#analytic_inputs TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b
#analytic_inputs TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b
