import TenthDiscriminant

/-! Actual labelled ideal-class slices turn four prime lifts into a prefix bound. -/
open scoped NumberField nonZeroDivisors BigOperators Classical
namespace TenthDiscriminant.EvenClassAggregation
open ClassFiber ResidueMultiplicity PrincipalBasis ClassAggregation
set_option autoImplicit false
noncomputable section

theorem prime_prefix_bound (D : Nat) [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (t : Nat) (P : Finset Nat) (hP : ∀ p ∈ P, Admissible D p) (hpt : ∀ p ∈ P, p≤t) :
    (P.card : Real) ≤ (NumberField.classNumber (EvenQuadraticField D) : Real)/4 *
      (2*Real.pi*t/Real.sqrt (4*D)+4*Real.sqrt (normBound (EvenQuadraticField D)*t/(4*D))+1) := by
  classical
  obtain ⟨J,hGood,hData,hPoints⟩ := EvenPrimeFamily.controlled_family D hsq hm h
  obtain ⟨U,hU,hu⟩ := hPoints P hP
  let A : Real := 2*Real.pi*t/Real.sqrt (4*D)
  let B : Real := 4*Real.sqrt (normBound (EvenQuadraticField D)*t/(4*D))
  let q := fun C : ClassGroup (𝓞 (EvenQuadraticField D)) =>
    ((U.filter (fun x => x.1=C)).card : Real)
  have hmem : ∀ x ∈ U, x.2 ∈ (J x.1 : Ideal (𝓞 (EvenQuadraticField D))) := by
    intro x hx
    obtain ⟨p,hp,hpoint⟩ := hu x hx
    exact hpoint.2.1
  have hrow : ∀ C, q C≤A+B+(if C=1 then 0 else 2) := by
    intro C
    obtain ⟨V,hV,hVU⟩ := actual_class_slice _ J U C hmem
    obtain ⟨e,a,b,c,hf,ha,hprin,hcount⟩ := (hData C).2
    have hprime : ∀ z ∈ V, PrimeNormalized (J C) z := by
      intro z hz
      obtain ⟨p,hp,hpoint⟩ := hu (C,(z : 𝓞 (EvenQuadraticField D))) (hVU z hz)
      exact ⟨p,(hP p hp).1,hpoint.2.2⟩
    have hnorm : ∀ z ∈ V, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
        Ideal.absNorm (J C : Ideal (𝓞 (EvenQuadraticField D)))*t := by
      intro z hz
      obtain ⟨p,hp,hpoint⟩ := hu (C,(z : 𝓞 (EvenQuadraticField D))) (hVU z hz)
      rw [hpoint.2.2]
      exact (Nat.mul_le_mul_right _ (hpt p hp)).trans_eq (Nat.mul_comm _ _)
    have hc := hcount V t hprime hnorm
    rw [hV] at hc
    exact hc
  have htotal : U.card=∑ C : ClassGroup (𝓞 (EvenQuadraticField D)),
      (U.filter (fun x => x.1=C)).card :=
    Finset.card_eq_sum_card_fiberwise (t:=Finset.univ) (f:=Prod.fst) (fun _ _ => Finset.mem_univ _)
  have htotalR : (U.card : Real)=∑ C, q C := by
    simpa only [Nat.cast_sum,q] using congrArg (fun n : Nat => (n : Real)) htotal
  have hfour : 4*(P.card : Real)≤∑ C, q C := by
    have he : 4*(P.card : Real)=∑ C, q C := calc
      _=(U.card : Real) := by exact_mod_cast hU.symm
      _=∑ C, q C := htotalR
    exact he.le
  have hcard : (Finset.univ : Finset (ClassGroup (𝓞 (EvenQuadraticField D)))).card≤2 := by
    simpa only [Finset.card_univ] using h
  have hs := two_class_accounting Finset.univ 1 (Finset.mem_univ _) hcard q
    (fun _ => B) A (P.card : Real) (fun C _ => hrow C) hfour
  have hb : (P.card : Real) ≤
      ((NumberField.classNumber (EvenQuadraticField D) : Real)*A+
       (NumberField.classNumber (EvenQuadraticField D) : Real)*B+
       (NumberField.classNumber (EvenQuadraticField D) : Real))/4 := by
    simpa only [Finset.sum_const,Finset.card_univ,nsmul_eq_mul,NumberField.classNumber] using hs
  calc
    (P.card : Real) ≤ _ := hb
    _ = (NumberField.classNumber (EvenQuadraticField D) : Real)/4*(A+B+1) := by ring

theorem uniform_two_class_bound (D : Nat) [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (t : Nat) (P : Finset Nat) (hP : ∀ p ∈ P, Admissible D p) (hpt : ∀ p ∈ P, p≤t) :
    (P.card : Real) ≤ (2*Real.pi*t/Real.sqrt (4*D)+
      4*Real.sqrt (normBound (EvenQuadraticField D)*t/(4*D))+1)/2 := by
  have hb := prime_prefix_bound D hsq hm h t P hP hpt
  have hR : (NumberField.classNumber (EvenQuadraticField D) : Real)≤2 := by exact_mod_cast h
  have hp : (0 : Real)≤2*Real.pi*t/Real.sqrt (4*D)+
      4*Real.sqrt (normBound (EvenQuadraticField D)*t/(4*D))+1 := by positivity
  calc
    (P.card : Real) ≤ _ := hb
    _ ≤ (2 : Real)/4*(2*Real.pi*t/Real.sqrt (4*D)+
      4*Real.sqrt (normBound (EvenQuadraticField D)*t/(4*D))+1) :=
      mul_le_mul_of_nonneg_right (div_le_div_of_nonneg_right hR (by norm_num)) hp
    _ = _ := by ring

theorem empty_slice_control (K : Type*) [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰) (C : ClassGroup (𝓞 K)) :
    ∃ V : Finset (J C : Ideal (𝓞 K)), V.card=0 := by
  obtain ⟨V,hV,hm⟩ := actual_class_slice K J ∅ C (by simp)
  exact ⟨V,by simpa using hV⟩

theorem absent_slice_control {α β : Type*} (U : Finset (α×β)) (C : α)
    (hC : ∀ x ∈ U, x.1≠C) : (U.filter (fun x => x.1=C)).card=0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro x hx
  exact hC x (Finset.mem_filter.mp hx).1 (Finset.mem_filter.mp hx).2

theorem label_collision_control :
    ({((0 : Fin 2),(1 : Int)),(1,1)} : Finset (Fin 2×Int)).card=2 ∧
      (({((0 : Fin 2),(1 : Int)),(1,1)} : Finset (Fin 2×Int)).image Prod.snd).card=1 := by decide

theorem axis_constant_control :
    2*((1 : Int)-1)≤1 ∧ 2*((2 : Int)-1)≤2 ∧ 3<2*((3 : Int)-1) := by norm_num
end
end TenthDiscriminant.EvenClassAggregation

#check TenthDiscriminant.EvenClassAggregation.prime_prefix_bound
#check TenthDiscriminant.EvenClassAggregation.uniform_two_class_bound
#check TenthDiscriminant.EvenClassAggregation.empty_slice_control
#check TenthDiscriminant.EvenClassAggregation.absent_slice_control
#check TenthDiscriminant.EvenClassAggregation.label_collision_control
#check TenthDiscriminant.EvenClassAggregation.axis_constant_control
#print axioms TenthDiscriminant.EvenClassAggregation.prime_prefix_bound
#print axioms TenthDiscriminant.EvenClassAggregation.uniform_two_class_bound
#audit_namespace TenthDiscriminant.EvenClassAggregation

open Lean Elab Command

elab "#phase97_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE97_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.ClassAggregation.uniform_two_class_bound]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE97_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE97_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE97_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE97_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE97_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"






#phase97_inputs TenthDiscriminant.EvenClassAggregation.uniform_two_class_bound
