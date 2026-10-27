import TenthDiscriminant.LeastNorm
import TenthDiscriminant.BasisCompletion
import TenthDiscriminant.PrincipalBasis

/-! One bounded actual ideal and controlled basis serve each entire ideal class. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.ControlledClassCount
open IdealCoordinates
set_option autoImplicit false
noncomputable section

theorem controlled_class_basis (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4)))) :
    ∃ J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Real) ≤
        ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) ∧
      ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
        ∃ a b c : Int, FormData D J e a b c ∧
          a ≤ (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) := by
  obtain ⟨J,hJ,hB,z,hz,hzN,hmin,hprim⟩ := LeastNorm.bounded_class_least_primitive D hsq h C
  obtain ⟨e,a0,b0,c0,hf0⟩ := actual_ideal_norm_form D hsq J
  obtain ⟨e',he,a,b,c,hf,ha⟩ := BasisCompletion.actual_form_of_primitive_bound D hsq J e z (hprim e) hzN
  exact ⟨J,hJ,hB,e',a,b,c,hf,ha⟩

theorem controlled_class_form_and_count (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4)))) :
    ∃ J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Real) ≤
        ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) ∧
      (∀ I : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰, ClassGroup.mk0 I=C →
        ∃ z : 𝓞 (QuadraticField (((D : Int)+1)/4)), ClassFiber.NormLift I J z) ∧
      ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
        ∃ a b c : Int, FormData D J e a b c ∧
          a ≤ (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) ∧
          (a : Real) ≤ ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) ∧
          ∀ (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) (t : Nat),
            (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
              Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t) →
            (∀ z ∈ U, (coordinates e z).2≠0) →
            (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt D+
              4*Real.sqrt (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))*t/D) := by
  obtain ⟨J,hJ,hB,e,a,b,c,hf,ha⟩ := controlled_class_basis D hsq h C
  have hlift : ∀ I : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      ClassGroup.mk0 I=C → ∃ z : 𝓞 (QuadraticField (((D : Int)+1)/4)), ClassFiber.NormLift I J z := by
    intro I hI
    apply ClassFiber.lift_in_inverse_class _ I J
    rw [hI,hJ]
    exact LeastNorm.self_inverse h C
  have haR : (a : Real)≤ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) :=
    le_trans (by exact_mod_cast ha) hB
  refine ⟨J,hJ,hB,hlift,e,a,b,c,hf,ha,haR,?_⟩
  intro U t hN hy
  have hc := count_for_actual_form D hsq J e a b c hf U t hN hy
  have harg : (a : Real)*t/D ≤ ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))*t/D :=
    div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_right haR (Nat.cast_nonneg t)) (Nat.cast_nonneg D)
  have hs := Real.sqrt_le_sqrt harg
  linarith

theorem coordinate_negation_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) (z : J) : coordinates e (-z)= -coordinates e z :=
  IdealCoordinates.coordinate_negation_control K J e z

theorem zero_threshold_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) (U : Finset J)
    (hN : ∀ z ∈ U, (Algebra.norm Int (z : 𝓞 K)).natAbs≤0)
    (hy : ∀ z ∈ U, (coordinates e z).2≠0) : U=∅ :=
  IdealCoordinates.zero_threshold_control K J e U hN hy

theorem origin_guard_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) :
    (coordinates e 0).2=0 ∧ (Algebra.norm Int (0 : 𝓞 K)).natAbs=0 ∧
      ¬ (({(0 : J)} : Finset J).card : Real)≤0 := IdealCoordinates.origin_guard_control K J e

theorem identity_lift_control (K : Type*) [Field K] [NumberField K]
    (I J : (Ideal (𝓞 K))⁰) (hI : ClassGroup.mk0 I=1) (hJ : ClassGroup.mk0 J=1) :
    ∃ z : 𝓞 K, ClassFiber.NormLift I J z := by
  apply ClassFiber.lift_in_inverse_class K I J
  rw [hI,hJ,inv_one]
end
end TenthDiscriminant.ControlledClassCount

#check TenthDiscriminant.ControlledClassCount.controlled_class_basis
#check TenthDiscriminant.ControlledClassCount.controlled_class_form_and_count
#check TenthDiscriminant.ControlledClassCount.coordinate_negation_control
#check TenthDiscriminant.ControlledClassCount.zero_threshold_control
#check TenthDiscriminant.ControlledClassCount.origin_guard_control
#check TenthDiscriminant.ControlledClassCount.identity_lift_control
#print TenthDiscriminant.IdealCoordinates.FormData
#print TenthDiscriminant.ClassFiber.normBound
#print axioms TenthDiscriminant.ControlledClassCount.controlled_class_basis
#print axioms TenthDiscriminant.ControlledClassCount.controlled_class_form_and_count
#audit_namespace TenthDiscriminant.ControlledClassCount
