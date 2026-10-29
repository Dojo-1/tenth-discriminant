import TenthDiscriminant

/-! The actual radial matrices form an additive integer action on observations. -/
namespace TenthDiscriminant.Phase127RadialAction
open Polynomial Matrix
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

private theorem polynomial_composition {A : Type*} [CommRing A]
    (R S : Nat) (a b : Int) (i : Fin (R*S)) (w : A) :
    ∑ h : Fin (R*S), RadialOperator.matrix R S a i h •
      RadialOperator.polynomial b w (h.val/S) (h.val%S) =
      RadialOperator.polynomial (a+b) w (i.val/S) (i.val%S) := by
  rw [RadialOperator.row_action]
  let r := i.val/S
  let s := i.val%S
  let m := min r s
  have hmr : m ≤ r := min_le_left _ _
  have hms : m ≤ s := min_le_right _ _
  have term (t : Nat) (ht : t ≤ m) :
      RadialOperator.polynomial b w
        ((RadialOperator.targetFin R S i t).val/S)
        ((RadialOperator.targetFin R S i t).val%S) =
      X^(r-m)*C w^(s-m)*(X*C w-C (b : A))^(m-t) := by
    obtain ⟨hr,hs⟩ := RadialOperator.targetFin_labels R S i t ht
    rw [hr,hs]
    change RadialOperator.polynomial b w (r-t) (s-t) = _
    have hm : min (r-t) (s-t)=m-t := by dsimp [m]; omega
    have hr' : r-t-(m-t)=r-m := by omega
    have hs' : s-t-(m-t)=s-m := by omega
    unfold RadialOperator.polynomial
    rw [hm,hr',hs']
  change (∑ t ∈ Finset.range (m+1),
    ((-a)^t*(m.choose t : Int)) •
      RadialOperator.polynomial b w
        ((RadialOperator.targetFin R S i t).val/S)
        ((RadialOperator.targetFin R S i t).val%S)) =
      RadialOperator.polynomial (a+b) w r s
  have hrad : (-C (a : A))+(X*C w-C (b : A)) =
      X*C w-C ((a+b : Int) : A) := by push_cast; ring
  calc
    _ = ∑ t ∈ Finset.range (m+1),
        ((-a)^t*(m.choose t : Int)) •
          (X^(r-m)*C w^(s-m)*(X*C w-C (b : A))^(m-t)) := by
      apply Finset.sum_congr rfl
      intro t ht
      rw [term t (by have := Finset.mem_range.mp ht; omega)]
    _ = X^(r-m)*C w^(s-m)*((-C (a : A))+(X*C w-C (b : A)))^m := by
      rw [add_pow,Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro t ht
      rw [zsmul_eq_mul]
      have hc : (((-a)^t*(m.choose t : Int) : Int) : A[X]) =
          (-C (a : A))^t*(m.choose t : A[X]) := by simp
      rw [hc]
      ring
    _ = _ := by rw [hrad]; rfl

private theorem row_coeff (R S : Nat) (v : Fin (R*S) → Int) (i : Fin (R*S)) :
    ((∑ h : Fin (R*S), v h •
      (X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) : Polynomial (Polynomial Int))).coeff
        (i.val/S)).coeff (i.val%S) = v i := by
  have mono (h : Fin (R*S)) :
      ((X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) :
        Polynomial (Polynomial Int)).coeff (i.val/S)).coeff (i.val%S) =
        if h=i then 1 else 0 := by
    rw [← map_pow,mul_comm,Polynomial.coeff_C_mul_X_pow]
    by_cases hr : i.val/S=h.val/S
    · rw [if_pos hr,Polynomial.coeff_X_pow]
      by_cases hs : i.val%S=h.val%S
      · have he : h=i := by
          apply Fin.ext
          calc
            h.val = (h.val/S)*S+h.val%S := (Nat.div_add_mod' _ _).symm
            _ = (i.val/S)*S+i.val%S := by rw [← hr,← hs]
            _ = i.val := Nat.div_add_mod' _ _
        simp [hs,he]
      · have he : h≠i := by intro he; subst h; exact hs rfl
        simp [hs,he]
    · have he : h≠i := by intro he; subst h; exact hr rfl
      simp [hr,he]
  simp only [Polynomial.finset_sum_coeff,Polynomial.coeff_smul]
  simp_rw [mono]
  simp

theorem matrix_zero (R S : Nat) : RadialOperator.matrix R S 0=1 := by
  ext i j
  unfold RadialOperator.matrix
  rw [Finset.sum_eq_single 0]
  · simp [RadialOperator.target,Nat.div_add_mod',Matrix.one_apply,Fin.ext_iff,eq_comm]
  · intro t ht ht0
    simp [ht0]
  · simp

theorem matrix_add (R S : Nat) (a b : Int) :
    RadialOperator.matrix R S a*RadialOperator.matrix R S b =
      RadialOperator.matrix R S (a+b) := by
  ext i j
  have hp :
      (∑ h : Fin (R*S), (RadialOperator.matrix R S a*RadialOperator.matrix R S b) i h •
        (X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) : Polynomial (Polynomial Int))) =
      ∑ h : Fin (R*S), RadialOperator.matrix R S (a+b) i h •
        (X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) : Polynomial (Polynomial Int)) := by
    simp only [Matrix.mul_apply,Finset.sum_smul,mul_smul]
    rw [Finset.sum_comm]
    simp_rw [← Finset.smul_sum]
    simp_rw [RadialOperator.polynomial_action]
    rw [polynomial_composition,RadialOperator.polynomial_action]
  have hc := congrArg (fun P : Polynomial (Polynomial Int) =>
    (P.coeff (j.val/S)).coeff (j.val%S)) hp
  simpa only [row_coeff] using hc

theorem matrix_neg (R S : Nat) (a : Int) :
    RadialOperator.matrix R S a*RadialOperator.matrix R S (-a)=1 ∧
      RadialOperator.matrix R S (-a)*RadialOperator.matrix R S a=1 := by
  constructor
  · rw [matrix_add,add_neg_cancel,matrix_zero]
  · rw [matrix_add,neg_add_cancel,matrix_zero]

theorem matrix_commute (R S : Nat) (a b : Int) :
    RadialOperator.matrix R S a*RadialOperator.matrix R S b =
      RadialOperator.matrix R S b*RadialOperator.matrix R S a := by
  rw [matrix_add,matrix_add,Int.add_comm a b]

theorem transform_add (D R S : Nat) (a b : Int)
    (V : Fin (R*S) → Int × Int → Nat → Zsqrtd (-(D : Int))) :
    zsqrtdJetTransform (RadialOperator.matrix R S a)
      (zsqrtdJetTransform (RadialOperator.matrix R S b) V) =
      zsqrtdJetTransform (RadialOperator.matrix R S (a+b)) V := by
  funext i q j
  unfold zsqrtdJetTransform
  rw [← matrix_add]
  simp only [Matrix.mul_apply,Finset.sum_smul,mul_smul,Finset.smul_sum]
  rw [Finset.sum_comm]

theorem gram_add (Q : Finset (Int × Int)) (D J R S : Nat) (a b : Int) :
    RadialOperator.matrix R S a*RadialOperator.gram Q D J R S b*
      (RadialOperator.matrix R S a).transpose =
      RadialOperator.gram Q D J R S (a+b) := by
  rw [RadialOperator.gram_congruence,RadialOperator.gram_congruence,← matrix_add]
  simp only [Matrix.transpose_mul,Matrix.mul_assoc]

theorem nonmultiplicative_control :
    ((RadialOperator.polynomial 3 (1 : Int) 1 0)*
      (RadialOperator.polynomial 3 (1 : Int) 0 1)).eval 0=0 ∧
      (RadialOperator.polynomial 3 (1 : Int) 1 1).eval 0 = -3 := by
  exact ⟨RadialOperator.origin_and_ring_controls.2.2,
    RadialOperator.origin_and_ring_controls.2.1⟩

end
end TenthDiscriminant.Phase127RadialAction

#audit_namespace TenthDiscriminant.Phase127RadialAction

open Lean Elab Command
elab "#phase127_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE127_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  unless state.visited.contains ``TenthDiscriminant.RadialOperator.matrix do
    throwError "PHASE127_ACTUAL_MATRIX_MISSING {target}"
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
    ``TenthDiscriminant.ClassAggregation.uniform_two_class_bound,
    ``TenthDiscriminant.SplitPrimeBudget.countBound,
    ``TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound,
    ``TenthDiscriminant.SplitPrimeBudget.actual_gram_budget,
    ``TenthDiscriminant.ClosedKernel.actual_majorant,
    ``TenthDiscriminant.ClosedKernel.closed_count_kernel,
    ``TenthDiscriminant.ClosedKernel.closed_actual_gram_budget,
    ``TenthDiscriminant.OddMinkowski.actual_minkowski,
    ``TenthDiscriminant.OddMinkowski.normalized_count_kernel,
    ``TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget,
    ``TenthDiscriminant.EvenTwoClass.even_classNumber_gt_two,
    ``TenthDiscriminant.EvenTwoClass.even_radicand_bound,
    ``TenthDiscriminant.EvenTwoClass.even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.parity_refined_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant,
    ``TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_cast,
    ``TenthDiscriminant.CoordinateTranslation.shifted_posDef,
    ``TenthDiscriminant.CoordinateTranslation.shifted_valuation,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE127_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE127_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE127_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE127_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE127_INPUTS_OK {target}: {count} reached;70forbidden roots excluded;axioms {state.axioms}"

#phase127_inputs TenthDiscriminant.Phase127RadialAction.matrix_add
#phase127_inputs TenthDiscriminant.Phase127RadialAction.transform_add
#phase127_inputs TenthDiscriminant.Phase127RadialAction.gram_add
