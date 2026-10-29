import TenthDiscriminant

/-! Structural interface: transport the existing canonical classification. -/
namespace TenthDiscriminant.Phase126Classification
set_option autoImplicit false
noncomputable section

/-- Classification up to rational algebra equivalence, without a supplied generator. -/
theorem field_classNumber_one_iff
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) :
    NumberField.classNumber K=1 ↔
      ∃ d : Nat, 0<d ∧ Squarefree d ∧
        d∈([1,2,3,7,11,19,43,67,163] : List Nat) ∧
        Nonempty (ImaginaryQuadraticField d ≃ₐ[Rat] K) := by
  constructor
  · intro hc
    obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
    letI : Fact (0<d) := ⟨hd⟩
    let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
    have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
    exact ⟨d,hd,hsq,(imaginaryQuadratic_classNumber_one_iff d hsq).mp hcan,⟨e⟩⟩
  · rintro ⟨d,hd,hsq,hmem,⟨e⟩⟩
    letI : Fact (0<d) := ⟨hd⟩
    exact classNumber_one_of_field_equiv (ImaginaryQuadraticField d) K e
      ((imaginaryQuadratic_classNumber_one_iff d hsq).mpr hmem)

/-- Actual signed field discriminants; membership is necessary, not an asserted iff. -/
theorem field_classNumber_one_discriminant_mem
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) (hc : NumberField.classNumber K=1) :
    NumberField.discr K ∈ ([-4,-8,-3,-7,-11,-19,-43,-67,-163] : List Int) := by
  obtain ⟨d,hd,hsq,hmem,⟨e⟩⟩ := (field_classNumber_one_iff K hdegree).mp hc
  letI : Fact (0<d) := ⟨hd⟩
  have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_mem d hsq hcan

end
end TenthDiscriminant.Phase126Classification

#audit_namespace TenthDiscriminant.Phase126Classification

open Lean Elab Command
elab "#phase126_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE126_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let required : Array Name := #[
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff,
    ``TenthDiscriminant.exists_squarefree_root_of_totallyComplex_degree_two,
    ``TenthDiscriminant.imaginaryQuadraticEquivOfRoot,
    ``TenthDiscriminant.classNumber_one_of_field_equiv]
  for name in required do
    unless state.visited.contains name do
      throwError "PHASE126_REQUIRED_INPUT_MISSING {target}: {name}"
  let forbidden : Array Name := #[
    ``TenthDiscriminant.RadialCutoff.odd_large_classNumber_ne_one_48b,
    ``TenthDiscriminant.RadialCutoff.imaginaryQuadratic_large_classNumber_ne_one_48b,
    ``TenthDiscriminant.RadialCutoff.imaginaryQuadratic_classNumber_one_discriminant_bound_48b,
    ``TenthDiscriminant.RadialCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_48b,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE126_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE126_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE126_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE126_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE126_INPUTS_OK {target}: {count} reached;4required/8forbidden;axioms {state.axioms}"

#phase126_inputs TenthDiscriminant.Phase126Classification.field_classNumber_one_iff
#phase126_inputs TenthDiscriminant.Phase126Classification.field_classNumber_one_discriminant_mem
