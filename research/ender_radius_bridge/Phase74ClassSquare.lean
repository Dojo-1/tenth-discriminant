import TenthDiscriminant
import Mathlib.GroupTheory.OrderOfElement

/-! Class-group inversion supplies a controlled vector, before any basis choice. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.ClassSquare
set_option autoImplicit false
noncomputable section

theorem self_inverse_of_card_le_two {G : Type*} [Group G] [Fintype G]
    (h : Fintype.card G ≤ 2) (g : G) : g = g⁻¹ := by
  have hp : 0 < Fintype.card G := Fintype.card_pos
  have he : Fintype.card G = 1 ∨ Fintype.card G = 2 := by omega
  have hg : g ^ Fintype.card G = 1 := pow_card_eq_one
  apply eq_inv_iff_mul_eq_one.mpr
  rcases he with he | he
  · rw [he, pow_one] at hg
    simp [hg]
  · simpa only [he, pow_two] using hg

theorem class_self_inverse (K : Type*) [Field K] [NumberField K]
    (h : NumberField.classNumber K ≤ 2) (C : ClassGroup (𝓞 K)) : C = C⁻¹ := by
  exact self_inverse_of_card_le_two h C

theorem ideal_square_vector (K : Type*) [Field K] [NumberField K]
    (h : NumberField.classNumber K ≤ 2) (J : (Ideal (𝓞 K))⁰) :
    ∃ z : 𝓞 K, ClassFiber.NormLift (J : Ideal (𝓞 K)) (J : Ideal (𝓞 K)) z := by
  exact ClassFiber.lift_in_inverse_class K J J (class_self_inverse K h (ClassGroup.mk0 J))

/-- The ideal is fixed for the whole class; its square produces a controlled vector. -/
theorem bounded_class_vector (K : Type*) [Field K] [NumberField K]
    (h : NumberField.classNumber K ≤ 2) (C : ClassGroup (𝓞 K)) :
    ∃ J : (Ideal (𝓞 K))⁰, ClassGroup.mk0 J = C ∧
      (Ideal.absNorm (J : Ideal (𝓞 K)) : Real) ≤ ClassFiber.normBound K ∧
      ∃ z : 𝓞 K, ClassFiber.NormLift (J : Ideal (𝓞 K)) (J : Ideal (𝓞 K)) z ∧
        (Algebra.norm Int z).natAbs = Ideal.absNorm (J : Ideal (𝓞 K)) ^ 2 := by
  obtain ⟨J, hJ, hb⟩ := NumberField.exists_ideal_in_class_of_norm_le C
  obtain ⟨z, hz⟩ := ideal_square_vector K h J
  exact ⟨J, hJ, hb, z, hz, by simpa only [pow_two] using hz.2.2.2.1⟩

theorem identity_control {G : Type*} [Group G] : (1 : G) = (1 : G)⁻¹ := by simp

theorem order_three_control : (1 : ZMod 3) ≠ -(1 : ZMod 3) := by decide

theorem zero_vector_control (K : Type*) [Field K] [NumberField K]
    (J : (Ideal (𝓞 K))⁰) :
    (Algebra.norm Int (0 : 𝓞 K)).natAbs ≠ Ideal.absNorm (J : Ideal (𝓞 K)) ^ 2 := by
  have hn : Ideal.absNorm (J : Ideal (𝓞 K)) ≠ 0 :=
    Ideal.absNorm_ne_zero_iff_mem_nonZeroDivisors.mpr J.prop
  simpa using (pow_ne_zero 2 hn).symm

theorem rational_control :
    ∃ J : (Ideal (𝓞 Rat))⁰, ClassGroup.mk0 J = 1 ∧
      (Ideal.absNorm (J : Ideal (𝓞 Rat)) : Real) ≤ ClassFiber.normBound Rat ∧
      ∃ z : 𝓞 Rat, ClassFiber.NormLift (J : Ideal (𝓞 Rat)) (J : Ideal (𝓞 Rat)) z ∧
        (Algebra.norm Int z).natAbs = Ideal.absNorm (J : Ideal (𝓞 Rat)) ^ 2 := by
  exact bounded_class_vector Rat (by rw [Rat.classNumber_eq]; decide) 1
end
end TenthDiscriminant.ClassSquare

#check TenthDiscriminant.ClassSquare.self_inverse_of_card_le_two
#check TenthDiscriminant.ClassSquare.class_self_inverse
#check TenthDiscriminant.ClassSquare.ideal_square_vector
#check TenthDiscriminant.ClassSquare.bounded_class_vector
#check TenthDiscriminant.ClassSquare.identity_control
#check TenthDiscriminant.ClassSquare.order_three_control
#check TenthDiscriminant.ClassSquare.zero_vector_control
#check TenthDiscriminant.ClassSquare.rational_control
#print TenthDiscriminant.ClassFiber.NormLift
#print TenthDiscriminant.ClassFiber.normBound
#print axioms TenthDiscriminant.ClassSquare.self_inverse_of_card_le_two
#print axioms TenthDiscriminant.ClassSquare.bounded_class_vector
#audit_namespace TenthDiscriminant.ClassSquare
