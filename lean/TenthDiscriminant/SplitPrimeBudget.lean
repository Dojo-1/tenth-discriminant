import TenthDiscriminant.ClassAggregation
import TenthDiscriminant.PrimeDivisorLoss

/-! A complete choice of good primes makes the actual split-prefix count pay the weighted loss. -/
open scoped NumberField nonZeroDivisors BigOperators Classical
namespace TenthDiscriminant.SplitPrimeBudget
open ExcludedPrime ResidueMultiplicity
set_option autoImplicit false
noncomputable section

def goodPrimes (D : Nat) (P : Finset Nat) : Finset Nat :=
  P.filter (fun p => ¬ IsSquare (-(D : ZMod p)))

def splitRemainder (D : Nat) (P : Finset Nat) : Finset Nat :=
  (P\goodPrimes D P) \ ((P\goodPrimes D P).filter (fun p => p ∣ D))

def countBound (D : Nat) [Fact ((D : Int)%4=3)] (n : Nat) : Real :=
  (2*Real.pi*n/Real.sqrt D+
    4*Real.sqrt (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))*n/D)+1)/2

theorem mem_remainder_iff (D : Nat) (P : Finset Nat) (p : Nat) :
    p ∈ splitRemainder D P ↔ p ∈ P ∧ IsSquare (-(D : ZMod p)) ∧ ¬p∣D := by
  simp only [splitRemainder,goodPrimes,Finset.mem_sdiff,Finset.mem_filter]
  tauto

theorem remainder_prefix_bound (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (P : Finset Nat) (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p≠2) (n : Nat) :
    prefixCount (splitRemainder D P) n ≤ countBound D n := by
  let Q := (splitRemainder D P).filter (fun p => p≤n)
  have hQ : ∀ p ∈ Q, Admissible D p := by
    intro p hp
    have hh := (mem_remainder_iff D P p).mp (Finset.mem_filter.mp hp).1
    exact ⟨hprime p hh.1,hodd p hh.1,hh.2.2,hh.2.1⟩
  have hqn : ∀ p ∈ Q, p≤n := fun p hp => (Finset.mem_filter.mp hp).2
  change (Q.card : Real) ≤ countBound D n
  exact ClassAggregation.uniform_two_class_bound D hsq h n Q hQ hqn

theorem actual_gram_budget (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
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
  have hD : 0<D := by
    have hm := (Fact.out : (D : Int)%4=3)
    omega
  exact PrimeDivisorLoss.excluded_budget_without_divisors P (goodPrimes D P)
    D D2 rho R S L (countBound D) hD hD2 hR hS hL
    (Finset.filter_subset _ _) hprime hodd hmax
    (fun p hp => (Finset.mem_filter.mp hp).2)
    (fun n hn hnL => by
      simpa only [splitRemainder] using remainder_prefix_bound D hsq h P hprime hodd n)
    hradius

theorem empty_control (D : Nat) : goodPrimes D ∅=∅ ∧ splitRemainder D ∅=∅ := by
  simp [goodPrimes,splitRemainder]

theorem seven_eleven_control : 11 ∈ splitRemainder 7 {3,7,11} := by
  apply (mem_remainder_iff 7 {3,7,11} 11).mpr
  refine ⟨by simp,?_,by decide⟩
  exact ⟨(2 : ZMod 11),by decide⟩

theorem divisor_control (D : Nat) (P : Finset Nat) (p : Nat) (hp : p∣D) :
    p ∉ splitRemainder D P := by
  intro he
  exact ((mem_remainder_iff D P p).mp he).2.2 hp

theorem nonsquare_control (D : Nat) (P : Finset Nat) (p : Nat)
    (hp : p ∈ P) (hns : ¬ IsSquare (-(D : ZMod p))) :
    p ∈ goodPrimes D P ∧ p ∉ splitRemainder D P := by
  refine ⟨Finset.mem_filter.mpr ⟨hp,hns⟩,?_⟩
  intro he
  exact hns ((mem_remainder_iff D P p).mp he).2.1
end
end TenthDiscriminant.SplitPrimeBudget

#check TenthDiscriminant.SplitPrimeBudget.mem_remainder_iff
#check TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound
#check TenthDiscriminant.SplitPrimeBudget.actual_gram_budget
#check TenthDiscriminant.SplitPrimeBudget.empty_control
#check TenthDiscriminant.SplitPrimeBudget.seven_eleven_control
#check TenthDiscriminant.SplitPrimeBudget.divisor_control
#check TenthDiscriminant.SplitPrimeBudget.nonsquare_control
#print TenthDiscriminant.SplitPrimeBudget.goodPrimes
#print TenthDiscriminant.SplitPrimeBudget.splitRemainder
#print TenthDiscriminant.SplitPrimeBudget.countBound
#print TenthDiscriminant.ExcludedPrime.primeKernel
#print TenthDiscriminant.ExcludedPrime.kernelCost
#print axioms TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound
#print axioms TenthDiscriminant.SplitPrimeBudget.actual_gram_budget
#audit_namespace TenthDiscriminant.SplitPrimeBudget
