import TenthDiscriminant.EvenClassAggregation
import TenthDiscriminant.SplitPrimeBudget

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

