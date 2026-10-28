import TenthDiscriminant

/-! The actual even prime count pays the weighted loss on the original Gram. -/
open scoped NumberField nonZeroDivisors BigOperators Classical
namespace TenthDiscriminant.EvenSplitPrimeBudget
open ExcludedPrime ResidueMultiplicity SplitPrimeBudget
set_option autoImplicit false
noncomputable section

def countBound (D : Nat) [Fact (0<D)] (n : Nat) : Real :=
  (2*Real.pi*n/Real.sqrt (4*D)+
    4*Real.sqrt (ClassFiber.normBound (EvenQuadraticField D)*n/(4*D))+1)/2

theorem remainder_prefix_bound (D : Nat) [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (P : Finset Nat) (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p≠2) (n : Nat) :
    prefixCount (splitRemainder D P) n ≤ countBound D n := by
  let Q := (splitRemainder D P).filter (fun p => p≤n)
  have hQ : ∀ p ∈ Q, Admissible D p := by
    intro p hp
    have hh := (mem_remainder_iff D P p).mp (Finset.mem_filter.mp hp).1
    exact ⟨hprime p hh.1,hodd p hh.1,hh.2.2,hh.2.1⟩
  have hqn : ∀ p ∈ Q, p≤n := fun p hp => (Finset.mem_filter.mp hp).2
  change (Q.card : Real) ≤ countBound D n
  exact EvenClassAggregation.uniform_two_class_bound D hsq hm h n Q hQ hqn

theorem actual_gram_budget (D : Nat) [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (P : Finset Nat) (D2 rho R S L : Nat)
    (hD2 : D≤D2) (hR : 1≤R) (hS : 1≤S) (hL : 3≤L)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p≠2) (hmax : ∀ p ∈ P, p≤L)
    (hradius : (1001/1000 : Real)*
      Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
      10*Real.sqrt D2 ≤ (rho : Real)) :
    mass P R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i))+
      lossScale R S*kernelCost L primeKernel (countBound D)+
      ((R*S*(S-1) : Nat) : Real)*Real.log (D : Real) := by
  have hD : 0<D := Fact.out
  exact PrimeDivisorLoss.excluded_budget_without_divisors P (goodPrimes D P)
    D D2 rho R S L (countBound D) hD hD2 hR hS hL
    (Finset.filter_subset _ _) hprime hodd hmax
    (fun p hp => (Finset.mem_filter.mp hp).2)
    (fun n hn hnL => by
      simpa only [splitRemainder] using remainder_prefix_bound D hsq hm h P hprime hodd n)
    hradius

theorem empty_control (D : Nat) : goodPrimes D ∅=∅ ∧ splitRemainder D ∅=∅ := by
  exact SplitPrimeBudget.empty_control D

theorem gaussian_split_control : 5 ∈ splitRemainder 1 {3,5} := by
  apply (mem_remainder_iff 1 {3,5} 5).mpr
  exact ⟨by simp, ⟨(2 : ZMod 5),by decide⟩,by decide⟩

theorem parameter_divisor_control : 5 ∉ splitRemainder 5 {3,5} := by
  exact SplitPrimeBudget.divisor_control 5 {3,5} 5 (by decide)

theorem prime_two_control : IsSquare (-(1 : ZMod 2)) ∧ ¬ Admissible 1 2 := by
  constructor
  · exact ⟨(1 : ZMod 2),by decide⟩
  · intro h
    exact h.2.1 rfl

theorem one_column_control (R p : Nat) : valuationWeight R 1 p = 0 := by
  exact PrimeDivisorLoss.one_column_control R p
end
end TenthDiscriminant.EvenSplitPrimeBudget

#check TenthDiscriminant.EvenSplitPrimeBudget.remainder_prefix_bound
#check TenthDiscriminant.EvenSplitPrimeBudget.actual_gram_budget
#check TenthDiscriminant.EvenSplitPrimeBudget.empty_control
#check TenthDiscriminant.EvenSplitPrimeBudget.gaussian_split_control
#check TenthDiscriminant.EvenSplitPrimeBudget.parameter_divisor_control
#check TenthDiscriminant.EvenSplitPrimeBudget.prime_two_control
#check TenthDiscriminant.EvenSplitPrimeBudget.one_column_control
#print TenthDiscriminant.EvenSplitPrimeBudget.countBound
#print axioms TenthDiscriminant.EvenSplitPrimeBudget.remainder_prefix_bound
#print axioms TenthDiscriminant.EvenSplitPrimeBudget.actual_gram_budget
#audit_namespace TenthDiscriminant.EvenSplitPrimeBudget

open Lean Elab Command

elab "#phase99_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE99_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.SplitPrimeBudget.actual_gram_budget]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE99_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE99_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE99_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE99_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE99_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"






#phase99_inputs TenthDiscriminant.EvenSplitPrimeBudget.actual_gram_budget
