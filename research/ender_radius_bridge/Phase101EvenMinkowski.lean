import TenthDiscriminant

/-! Actual even normalization and a closed weighted estimate on the original Gram. -/
open scoped NumberField nonZeroDivisors BigOperators Classical
namespace TenthDiscriminant.EvenMinkowski
open NumberField ExcludedPrime ClosedKernel Polynomial
set_option autoImplicit false
noncomputable section

def chartCost (D L : Nat) : Real := closedCost (4*D) ((4/Real.pi)*Real.sqrt D) L
def scalarCost (D L : Nat) : Real := closedCost D ((2/Real.pi)*Real.sqrt D) L

theorem field_degree (D : Nat) [Fact (0<D)] :
    Module.finrank Rat (EvenQuadraticField D)=2 := by
  simpa using Module.finrank_eq_card_basis (evenFieldBasis D)

theorem no_real_embedding (D : Nat) [Fact (0<D)] :
    ¬ Nonempty (EvenQuadraticField D →ₐ[Rat] Real) := by
  rintro ⟨f⟩
  let z := AdjoinRoot.root (evenFieldPoly D)
  have hz : z^2+(D : EvenQuadraticField D)=0 := by
    dsimp [z]
    rw [evenField_root_sq]
    simp
  have hr : (f z)^2+(D : Real)=0 := by simpa using congrArg f hz
  have hd : (0 : Real)<D := by exact_mod_cast (Fact.out : 0<D)
  nlinarith [sq_nonneg (f z)]

theorem chart_totallyComplex (D : Nat) [Fact (0<D)] :
    NumberField.IsTotallyComplex (EvenQuadraticField D) := by
  constructor
  intro w
  apply NumberField.InfinitePlace.not_isReal_iff_isComplex.mp
  intro hw
  exact no_real_embedding D ⟨(NumberField.InfinitePlace.isReal_iff.mp hw).embedding.toRatAlgHom⟩

theorem complex_places_one (D : Nat) [Fact (0<D)] :
    NumberField.InfinitePlace.nrComplexPlaces (EvenQuadraticField D)=1 := by
  letI := chart_totallyComplex D
  have hr := NumberField.IsTotallyComplex.finrank (EvenQuadraticField D)
  rw [field_degree] at hr
  omega

theorem sqrt_scale (d : Real) (hd : 0≤d) : Real.sqrt (4*d)=2*Real.sqrt d := by
  rw [Real.sqrt_mul (by norm_num : (0 : Real)≤4)]
  norm_num

theorem actual_minkowski (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2) :
    ClassFiber.normBound (EvenQuadraticField D)=(4/Real.pi)*Real.sqrt D := by
  have hd : |(NumberField.discr (EvenQuadraticField D) : Real)|=4*(D : Real) := by
    rw [even_actual_discr D hsq hm]
    push_cast
    simp
  unfold ClassFiber.normBound
  rw [field_degree,complex_places_one D,hd]
  norm_num [sqrt_scale (D : Real) (Nat.cast_nonneg D)]
  ring
  simp

theorem actual_majorant (D : Nat) [Fact (0<D)] (n : Nat) (hn : 3≤n) :
    EvenSplitPrimeBudget.countBound D n ≤
      linearSlope (4*D) (ClassFiber.normBound (EvenQuadraticField D))*n+1/2 := by
  have hd : (0 : Real)<4*D := by
    have hD : (0 : Real)<D := by exact_mod_cast (Fact.out : 0<D)
    positivity
  have hM : 0≤ClassFiber.normBound (EvenQuadraticField D) := by
    unfold ClassFiber.normBound
    positivity
  have hs := sqrt_majorant (4*(D : Real)) (ClassFiber.normBound (EvenQuadraticField D))
    (n : Real) hd hM (by exact_mod_cast hn)
  unfold EvenSplitPrimeBudget.countBound linearSlope
  simp only [div_eq_mul_inv] at hs ⊢
  nlinarith

theorem closed_count_kernel (D : Nat) [Fact (0<D)] (L : Nat) (hL : 3≤L) :
    kernelCost L primeKernel (EvenSplitPrimeBudget.countBound D) ≤
      closedCost (4*D) (ClassFiber.normBound (EvenQuadraticField D)) L := by
  let a := linearSlope (4*D) (ClassFiber.normBound (EvenQuadraticField D))
  have ha : 0≤a := by dsimp [a,linearSlope]; positivity
  calc
    _ ≤ kernelCost L primeKernel (fun n => a*n+1/2) :=
      kernel_mono L hL _ _ (fun n hn hnL => actual_majorant D n hn)
    _ = a*(Real.log 3+∑ n ∈ Finset.Ico 4 (L+1), primeKernel n)+Real.log 3/6 := by
      rw [affine_identity L hL]
      norm_num [primeKernel]
      ring
    _ ≤ a*(Real.log 3+Real.log L*(1+Real.log L))+Real.log 3/6 := by
      exact add_le_add_right (mul_le_mul_of_nonneg_left
        (add_le_add_left (prime_sum_bound L hL) _) ha) _
    _ = _ := rfl

theorem normalized_count_kernel (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2) (L : Nat) (hL : 3≤L) :
    kernelCost L primeKernel (EvenSplitPrimeBudget.countBound D) ≤ chartCost D L := by
  simpa only [actual_minkowski D hsq hm,chartCost] using closed_count_kernel D L hL

theorem normalized_actual_gram_budget (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (P : Finset Nat) (D2 rho R S L : Nat)
    (hD2 : D≤D2) (hR : 1≤R) (hS : 1≤S) (hL : 3≤L)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p≠2) (hmax : ∀ p ∈ P, p≤L)
    (hradius : (1001/1000 : Real)*
      Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
      10*Real.sqrt D2 ≤ (rho : Real)) :
    mass P R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i))+
      lossScale R S*chartCost D L+
      ((R*S*(S-1) : Nat) : Real)*Real.log (D : Real) := by
  have hb := EvenSplitPrimeBudget.actual_gram_budget D hsq hm h P D2 rho R S L
    hD2 hR hS hL hprime hodd hmax hradius
  have hk := mul_le_mul_of_nonneg_left (normalized_count_kernel D hsq hm L hL)
    (by unfold lossScale; positivity : 0≤lossScale R S)
  linarith

theorem chartCost_le_scalarCost (D L : Nat) (hD : 0<D) (hL : 3≤L) :
    chartCost D L≤scalarCost D L := by
  have hd : (0 : Real)<D := by exact_mod_cast hD
  have hs : Real.sqrt (4*(D : Real))=2*Real.sqrt D := sqrt_scale _ (by positivity)
  have harea : Real.pi/Real.sqrt (4*(D : Real))≤Real.pi/Real.sqrt D := by
    apply div_le_div_of_nonneg_left Real.pi_pos.le (Real.sqrt_pos.mpr hd)
    rw [hs]
    nlinarith [Real.sqrt_nonneg (D : Real)]
  have harg : ((4/Real.pi)*Real.sqrt D)/(3*(4*(D : Real))) ≤
      ((2/Real.pi)*Real.sqrt D)/(3*(D : Real)) := by
    have he : ((4/Real.pi)*Real.sqrt D)/(3*(4*(D : Real))) =
        (((2/Real.pi)*Real.sqrt D)/(3*(D : Real)))/2 := by
      field_simp [ne_of_gt hd,ne_of_gt Real.pi_pos]
      <;> ring
    rw [he]
    have hn : (0 : Real)≤((2/Real.pi)*Real.sqrt D)/(3*(D : Real)) := by positivity
    linarith
  have hroot := Real.sqrt_le_sqrt harg
  have hslope : linearSlope (4*D) ((4/Real.pi)*Real.sqrt D) ≤
      linearSlope D ((2/Real.pi)*Real.sqrt D) := by
    unfold linearSlope
    linarith
  have hlog : 0≤Real.log (L : Real) := Real.log_nonneg (by exact_mod_cast (by omega : 1≤L))
  have hfactor : 0≤Real.log 3+Real.log L*(1+Real.log L) := by positivity
  unfold chartCost scalarCost closedCost
  exact add_le_add_right (mul_le_mul_of_nonneg_right hslope hfactor) _

theorem scalar_actual_gram_budget (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (P : Finset Nat) (D2 rho R S L : Nat)
    (hD2 : D≤D2) (hR : 1≤R) (hS : 1≤S) (hL : 3≤L)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p≠2) (hmax : ∀ p ∈ P, p≤L)
    (hradius : (1001/1000 : Real)*
      Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
      10*Real.sqrt D2 ≤ (rho : Real)) :
    mass P R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i))+
      lossScale R S*scalarCost D L+
      ((R*S*(S-1) : Nat) : Real)*Real.log (D : Real) := by
  have hb := normalized_actual_gram_budget D hsq hm h P D2 rho R S L
    hD2 hR hS hL hprime hodd hmax hradius
  have hk := mul_le_mul_of_nonneg_left (chartCost_le_scalarCost D L Fact.out hL)
    (by unfold lossScale; positivity : 0≤lossScale R S)
  linarith

theorem gaussian_control [Fact (0<(1 : Nat))] :
    ClassFiber.normBound (EvenQuadraticField 1)=4/Real.pi := by
  simpa using actual_minkowski 1 (by simp) (by decide)

theorem two_control [Fact (0<(2 : Nat))] :
    NumberField.discr (EvenQuadraticField 2)= -8 ∧
      ClassFiber.normBound (EvenQuadraticField 2)=(4/Real.pi)*Real.sqrt 2 := by
  constructor
  · simpa using even_actual_discr 2 (by norm_num : Nat.Prime 2).squarefree (by decide)
  · exact actual_minkowski 2 (by norm_num : Nat.Prime 2).squarefree (by decide)

theorem small_domain_control : primeKernel 1<primeKernel 3 := by
  exact ExcludedPrime.small_domain_rejected

theorem axis_constant_control (L : Nat) (hL : 3≤L) :
    kernelCost L primeKernel (fun _ => (1/2 : Real))=Real.log 3/6 := by
  have he := ClosedKernel.zero_slope_control L hL (1/2)
  simp only [zero_mul,zero_add] at he
  rw [he]
  unfold primeKernel
  ring
end
end TenthDiscriminant.EvenMinkowski

#check TenthDiscriminant.EvenMinkowski.field_degree
#check TenthDiscriminant.EvenMinkowski.no_real_embedding
#check TenthDiscriminant.EvenMinkowski.chart_totallyComplex
#check TenthDiscriminant.EvenMinkowski.complex_places_one
#check TenthDiscriminant.EvenMinkowski.sqrt_scale
#check TenthDiscriminant.EvenMinkowski.actual_minkowski
#check TenthDiscriminant.EvenMinkowski.actual_majorant
#check TenthDiscriminant.EvenMinkowski.closed_count_kernel
#check TenthDiscriminant.EvenMinkowski.normalized_count_kernel
#check TenthDiscriminant.EvenMinkowski.normalized_actual_gram_budget
#check TenthDiscriminant.EvenMinkowski.chartCost_le_scalarCost
#check TenthDiscriminant.EvenMinkowski.scalar_actual_gram_budget
#check TenthDiscriminant.EvenMinkowski.gaussian_control
#check TenthDiscriminant.EvenMinkowski.two_control
#check TenthDiscriminant.EvenMinkowski.small_domain_control
#check TenthDiscriminant.EvenMinkowski.axis_constant_control
#print TenthDiscriminant.EvenMinkowski.chartCost
#print TenthDiscriminant.EvenMinkowski.scalarCost
#print axioms TenthDiscriminant.EvenMinkowski.actual_minkowski
#print axioms TenthDiscriminant.EvenMinkowski.normalized_actual_gram_budget
#print axioms TenthDiscriminant.EvenMinkowski.scalar_actual_gram_budget
#audit_namespace TenthDiscriminant.EvenMinkowski

open Lean Elab Command

elab "#phase101_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE101_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.ClassAggregation.uniform_two_class_bound,
    ``TenthDiscriminant.SplitPrimeBudget.countBound,
    ``TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound,
    ``TenthDiscriminant.SplitPrimeBudget.actual_gram_budget,
    ``TenthDiscriminant.ClosedKernel.actual_majorant,
    ``TenthDiscriminant.ClosedKernel.closed_count_kernel,
    ``TenthDiscriminant.ClosedKernel.closed_actual_gram_budget,
    ``TenthDiscriminant.OddMinkowski.actual_minkowski,
    ``TenthDiscriminant.OddMinkowski.normalized_count_kernel,
    ``TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE101_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE101_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE101_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE101_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE101_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"






#phase101_inputs TenthDiscriminant.EvenMinkowski.scalar_actual_gram_budget
