import TenthDiscriminant.ClosedKernel
import TenthDiscriminant.QuadraticDiscriminant

/-! The odd maximal field chart removes M(K) from the closed weighted budget. -/
open scoped NumberField nonZeroDivisors BigOperators Classical
namespace TenthDiscriminant.OddMinkowski
open NumberField ExcludedPrime ClosedKernel Polynomial
set_option autoImplicit false
noncomputable section

def chartCost (D L : Nat) : Real := closedCost D ((2/Real.pi)*Real.sqrt D) L

theorem no_real_embedding (D : Nat) [Fact ((D : Int)%4=3)] :
    ¬ Nonempty (QuadraticField (((D : Int)+1)/4) →ₐ[Rat] Real) := by
  rintro ⟨f⟩
  let c : Int := ((D : Int)+1)/4
  let z := AdjoinRoot.root (quadraticFieldPoly c)
  have hz : z^2-z+(c : QuadraticField c)=0 := by
    have he := AdjoinRoot.eval₂_root (quadraticFieldPoly c)
    change (X^2-X+C (c : Rat)).eval₂ (AdjoinRoot.of (quadraticFieldPoly c)) z=0 at he
    simpa only [eval₂_add,eval₂_sub,eval₂_pow,eval₂_X,eval₂_C] using he
  have hr : (f z)^2-f z+(c : Real)=0 := by simpa using congrArg f hz
  have hm := (Fact.out : (D : Int)%4=3)
  have hc : 4*c=(D : Int)+1 := by dsimp [c]; omega
  have hcR : 4*(c : Real)=(D : Real)+1 := by exact_mod_cast hc
  have hD : 0<D := by omega
  have hd : (0 : Real)<D := by exact_mod_cast hD
  nlinarith [sq_nonneg (2*f z-1)]

theorem chart_totallyComplex (D : Nat) [Fact ((D : Int)%4=3)] :
    NumberField.IsTotallyComplex (QuadraticField (((D : Int)+1)/4)) := by
  constructor
  intro w
  apply NumberField.InfinitePlace.not_isReal_iff_isComplex.mp
  intro hw
  exact no_real_embedding D ⟨(NumberField.InfinitePlace.isReal_iff.mp hw).embedding.toRatAlgHom⟩

theorem complex_places_one (D : Nat) [Fact ((D : Int)%4=3)] :
    NumberField.InfinitePlace.nrComplexPlaces (QuadraticField (((D : Int)+1)/4))=1 := by
  letI := chart_totallyComplex D
  have hr := NumberField.IsTotallyComplex.finrank (QuadraticField (((D : Int)+1)/4))
  rw [quadraticField_basis_dimension] at hr
  omega

theorem actual_minkowski (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))=(2/Real.pi)*Real.sqrt D := by
  have hd : |(NumberField.discr (QuadraticField (((D : Int)+1)/4)) : Real)|=(D : Real) := by
    rw [half_actual_discr D hsq]
    push_cast
    simp
  unfold ClassFiber.normBound
  rw [quadraticField_basis_dimension,complex_places_one D,hd]
  norm_num
  ring

theorem normalized_count_kernel (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (L : Nat) (hL : 3≤L) :
    kernelCost L primeKernel (SplitPrimeBudget.countBound D) ≤ chartCost D L := by
  simpa only [actual_minkowski D hsq,chartCost] using closed_count_kernel D L hL

theorem normalized_actual_gram_budget (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
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
  simpa only [actual_minkowski D hsq,chartCost] using
    closed_actual_gram_budget D hsq h P D2 rho R S L hD2 hR hS hL hprime hodd hmax hradius

local instance threeFieldFact : Fact (0<4*(1 : Int)-1) := ⟨by norm_num⟩

theorem three_control :
    ClassFiber.normBound (QuadraticField 1)=(2/Real.pi)*Real.sqrt 3 := by
  letI : Fact ((3 : Int)%4=3) := ⟨by norm_num⟩
  simpa using actual_minkowski 3 ((by norm_num : Nat.Prime 3).squarefree)

theorem seven_control :
    ClassFiber.normBound (QuadraticField 2)=(2/Real.pi)*Real.sqrt 7 := by
  letI : Fact ((7 : Int)%4=3) := ⟨by norm_num⟩
  simpa using actual_minkowski 7 ((by norm_num : Nat.Prime 7).squarefree)

theorem nonsquarefree_control : ¬ Squarefree (9 : Nat) := by
  intro h
  exact Nat.squarefree_iff_prime_squarefree.mp h 3 (by norm_num) (by norm_num)

theorem zero_guard_control : ¬ ((0 : Int)%4=3) := by norm_num
end
end TenthDiscriminant.OddMinkowski

#check TenthDiscriminant.OddMinkowski.no_real_embedding
#check TenthDiscriminant.OddMinkowski.chart_totallyComplex
#check TenthDiscriminant.OddMinkowski.complex_places_one
#check TenthDiscriminant.OddMinkowski.actual_minkowski
#check TenthDiscriminant.OddMinkowski.normalized_count_kernel
#check TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget
#check TenthDiscriminant.OddMinkowski.three_control
#check TenthDiscriminant.OddMinkowski.seven_control
#check TenthDiscriminant.OddMinkowski.nonsquarefree_control
#check TenthDiscriminant.OddMinkowski.zero_guard_control
#print TenthDiscriminant.OddMinkowski.chartCost
#print TenthDiscriminant.ClosedKernel.closedCost
#print TenthDiscriminant.ClosedKernel.linearSlope

#print axioms TenthDiscriminant.OddMinkowski.no_real_embedding
#print axioms TenthDiscriminant.OddMinkowski.complex_places_one
#print axioms TenthDiscriminant.OddMinkowski.actual_minkowski
#print axioms TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget
#audit_namespace TenthDiscriminant.OddMinkowski
