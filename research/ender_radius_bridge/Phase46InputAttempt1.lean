import TenthDiscriminant

/-! Fresh constructor/actual-field signatures and proof-input checks. -/
open Lean Elab Command

elab "#generator_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "GENERATOR_ROOT_MISSING {target}"
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
      throwError "GENERATOR_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "GENERATOR_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "GENERATOR_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "GENERATOR_NONSTANDARD_AXIOM {name}"
  logInfo m!"GENERATOR_INPUTS_OK {target}: {count} reached; none of16 listed forbidden inputs; axioms {state.axioms}"

#check TenthDiscriminant.imaginaryQuadraticEquivOfRoot
#check TenthDiscriminant.imaginaryQuadraticEquivOfRoot_root
#check TenthDiscriminant.imaginaryQuadratic_degree_of_equiv
#check TenthDiscriminant.classNumber_one_radicand_bound_of_quadratic_root
#check TenthDiscriminant.classNumber_one_discriminant_bound_of_quadratic_root
#print axioms TenthDiscriminant.classNumber_one_discriminant_bound_of_quadratic_root
#generator_inputs TenthDiscriminant.classNumber_one_radicand_bound_of_quadratic_root
#generator_inputs TenthDiscriminant.classNumber_one_discriminant_bound_of_quadratic_root

namespace Phase46Controls
open TenthDiscriminant Polynomial
private instance : Fact (0 < (19 : Nat)) := ⟨by decide⟩
private instance : Fact (0 < 4 * (5 : Int) - 1) := ⟨by decide⟩
private instance : Fact (0 < (1 : Nat)) := ⟨by decide⟩

def negativeRoot : ImaginaryQuadraticField 19 := -AdjoinRoot.root (evenFieldPoly 19)

theorem negativeRoot_relation : negativeRoot^2 + (19 : ImaginaryQuadraticField 19) = 0 := by
  have h := evenField_root_sq 19
  simpa [negativeRoot, neg_sq] using (eq_neg_iff_add_eq_zero.mp h)

example : imaginaryQuadraticEquivOfRoot 19 (ImaginaryQuadraticField 19)
    negativeRoot negativeRoot_relation (imaginaryQuadratic_finrank 19)
    (AdjoinRoot.root (evenFieldPoly 19)) = negativeRoot :=
  imaginaryQuadraticEquivOfRoot_root _ _ _ _ _

def halfRoot : QuadraticField 5 := 2*AdjoinRoot.root (quadraticFieldPoly 5)-1

theorem halfRoot_relation : halfRoot^2 + (19 : QuadraticField 5) = 0 := by
  have h := AdjoinRoot.eval₂_root (quadraticFieldPoly 5)
  change (X^2-X+C (5 : Rat)).eval₂ (AdjoinRoot.of (quadraticFieldPoly 5))
    (AdjoinRoot.root (quadraticFieldPoly 5))=0 at h
  simp only [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C, map_ofNat] at h
  dsimp [halfRoot]
  linear_combination 4*h

example : imaginaryQuadraticEquivOfRoot 19 (QuadraticField 5)
    halfRoot halfRoot_relation (quadraticField_basis_dimension 5)
    (AdjoinRoot.root (evenFieldPoly 19)) = halfRoot :=
  imaginaryQuadraticEquivOfRoot_root _ _ _ _ _

def scaledRoot : ImaginaryQuadraticField 1 :=
  1000000*AdjoinRoot.root (evenFieldPoly 1)

theorem scaledRoot_relation :
    scaledRoot^2 + (1000000000000 : ImaginaryQuadraticField 1) = 0 := by
  have h : (AdjoinRoot.root (evenFieldPoly 1))^2 = (-1 : ImaginaryQuadraticField 1) := by
    simpa using evenField_root_sq 1
  dsimp [scaledRoot]
  rw [mul_pow, h]
  norm_num

theorem nonsquarefree_rescaling_rejects_unguarded_bound :
    ∃ a : ImaginaryQuadraticField 1,
      a^2+(1000000000000 : ImaginaryQuadraticField 1)=0 ∧
      Module.finrank Rat (ImaginaryQuadraticField 1)=2 ∧
      NumberField.classNumber (ImaginaryQuadraticField 1)=1 ∧
      ¬ Squarefree (1000000000000 : Nat) ∧ ¬ (1000000000000 : Nat)<100000000000 := by
  refine ⟨scaledRoot,scaledRoot_relation,imaginaryQuadratic_finrank 1,
    known_nine_classNumber_one 1 (by decide),?_,by norm_num⟩
  intro hs
  have h2 := hs 2 (by norm_num : (2 : Nat)*2 ∣ 1000000000000)
  norm_num at h2

end Phase46Controls
