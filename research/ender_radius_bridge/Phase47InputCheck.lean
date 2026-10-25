import TenthDiscriminant

/-! Fresh operator/normalization and abstract-field cutoff input checks. -/
open Lean Elab Command

elab "#operator_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "OPERATOR_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let base : Array Name := #[
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
  let normalization := target==``TenthDiscriminant.exists_squarefree_root_of_totallyComplex_degree_two ||
    target==``TenthDiscriminant.imaginaryQuadratic_isTotallyComplex
  let extra : Array Name := #[
    ``NumberField.classNumber,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b,
    ``TenthDiscriminant.classNumber_one_radicand_bound_of_quadratic_root,
    ``TenthDiscriminant.classNumber_one_discriminant_bound_of_quadratic_root,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound]
  let forbidden := if normalization then base++extra else base
  for name in forbidden do
    if state.visited.contains name then
      throwError "OPERATOR_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "OPERATOR_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "OPERATOR_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "OPERATOR_NONSTANDARD_AXIOM {name}"
  logInfo m!"OPERATOR_INPUTS_OK {target}: {count} reached; none of{forbidden.size} named forbidden inputs; axioms {state.axioms}"

#check TenthDiscriminant.quadratic_nonidentity_aut_eq
#check TenthDiscriminant.exists_conjugation_operator
#check TenthDiscriminant.antiInvariantProjection_anti
#check TenthDiscriminant.antiInvariantProjection_idempotent
#check TenthDiscriminant.exists_squarefree_root_of_totallyComplex_degree_two
#check TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound
#print axioms TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound
#operator_inputs TenthDiscriminant.exists_squarefree_root_of_totallyComplex_degree_two
#operator_inputs TenthDiscriminant.imaginaryQuadratic_isTotallyComplex
#operator_inputs TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound

namespace Phase47Controls
open TenthDiscriminant
private instance onePositive : Fact (0 < (1 : Nat)) := ⟨by decide⟩
private instance twoPositive : Fact (0 < (2 : Nat)) := ⟨by decide⟩
private instance nineteenPositive : Fact (0 < (19 : Nat)) := ⟨by decide⟩

example : (NumberField.discr (ImaginaryQuadraticField 1)).natAbs < 100000000000 := by
  letI := imaginaryQuadratic_isTotallyComplex 1
  exact totallyComplex_degree_two_classNumber_one_discriminant_bound _
    (imaginaryQuadratic_finrank 1) (known_nine_classNumber_one 1 (by decide))

example : (NumberField.discr (ImaginaryQuadraticField 2)).natAbs < 100000000000 := by
  letI := imaginaryQuadratic_isTotallyComplex 2
  exact totallyComplex_degree_two_classNumber_one_discriminant_bound _
    (imaginaryQuadratic_finrank 2) (known_nine_classNumber_one 2 (by decide))

example : (NumberField.discr (ImaginaryQuadraticField 19)).natAbs < 100000000000 := by
  letI := imaginaryQuadratic_isTotallyComplex 19
  exact totallyComplex_degree_two_classNumber_one_discriminant_bound _
    (imaginaryQuadratic_finrank 19) (known_nine_classNumber_one 19 (by decide))

end Phase47Controls
