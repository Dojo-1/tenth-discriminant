import TenthDiscriminant

/-! Fresh input closure for the aspect-ratio lemma, not a transfer of an
earlier provenance snapshot and not an external mathematical review. -/
open Lean Elab Command

elab "#aspect_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "ASPECT_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b,
    ``TenthDiscriminant.FirstCertificate.rawPrimeMassLower_uniform]
  for name in forbidden do
    if state.visited.contains name then
      throwError "ASPECT_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "ASPECT_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "ASPECT_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "ASPECT_NONSTANDARD_AXIOM {name}"
  logInfo m!"ASPECT_INPUTS_OK {target}: {count} reached; no listed cutoff, classification, finite answer or old fixed-ratio lower theorem; axioms {state.axioms}"

#check TenthDiscriminant.FirstCertificate.rawPrimeMassLower_aspect_ratio
#check TenthDiscriminant.FirstCertificate.aspect_ratio_21_control
#check TenthDiscriminant.FirstCertificate.aspect_ratio_25_point_1_control
#check TenthDiscriminant.FirstCertificate.candidate_aspect_affine_separation
#check TenthDiscriminant.FirstCertificate.candidate_aspect_log25_rejected
#check TenthDiscriminant.FirstCertificate.aspect_ratio_floor25_equality_rejected
#print axioms TenthDiscriminant.FirstCertificate.rawPrimeMassLower_aspect_ratio
#aspect_inputs TenthDiscriminant.FirstCertificate.rawPrimeMassLower_aspect_ratio
