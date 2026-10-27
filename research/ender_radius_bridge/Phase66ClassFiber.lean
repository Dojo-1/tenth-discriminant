import TenthDiscriminant

/-! One bounded ideal per actual ideal class serves every residue ideal in that class.
The binary-form basis and representation multiplicities are later obligations. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.ClassFiber
set_option autoImplicit false
noncomputable section

/-- The existing Mathlib Minkowski bound; no new estimate is asserted. -/
def normBound (K : Type*) [Field K] [NumberField K] : Real :=
  (4/Real.pi)^NumberField.InfinitePlace.nrComplexPlaces K *
    (((Module.finrank Rat K).factorial : Real) /
      (Module.finrank Rat K : Real)^(Module.finrank Rat K) *
      Real.sqrt |(NumberField.discr K : Real)|)

/-- A representation in the fixed ideal lattice, with exact recovery of the input ideal. -/
def NormLift {K : Type*} [Field K] [NumberField K]
    (I J : Ideal (𝓞 K)) (z : 𝓞 K) : Prop :=
  z ≠ 0 ∧ z ∈ J ∧ Ideal.span ({z} : Set (𝓞 K)) = I*J ∧
    (Algebra.norm Int z).natAbs = Ideal.absNorm I * Ideal.absNorm J ∧
    ∀ I' : Ideal (𝓞 K), I'*J = Ideal.span ({z} : Set (𝓞 K)) → I'=I

theorem lift_in_inverse_class (K : Type*) [Field K] [NumberField K]
    (I J : (Ideal (𝓞 K))⁰)
    (hc : ClassGroup.mk0 I = (ClassGroup.mk0 J)⁻¹) :
    ∃ z : 𝓞 K, NormLift (I : Ideal (𝓞 K)) (J : Ideal (𝓞 K)) z := by
  obtain ⟨z, hz, hs⟩ := ClassGroup.mk0_eq_mk0_inv_iff.mp hc
  have hspan : (I : Ideal (𝓞 K))*(J : Ideal (𝓞 K)) =
      Ideal.span ({z} : Set (𝓞 K)) := hs
  have hJ0 : (J : Ideal (𝓞 K)) ≠ 0 := mem_nonZeroDivisors_iff_ne_zero.mp J.prop
  refine ⟨z, hz, ?_, hspan.symm, ?_, ?_⟩
  · apply (Ideal.mul_le_left : (I : Ideal (𝓞 K))*(J : Ideal (𝓞 K)) ≤ J)
    rw [hspan]
    exact Ideal.subset_span (by simp)
  · rw [← Ideal.absNorm_span_singleton, ← hspan, map_mul]
  · intro I' hI'
    exact mul_right_cancel₀ hJ0 (hI'.trans hspan.symm)

/-- The ideal J is chosen before I, so the entire class has one fixed norm lattice. -/
theorem class_fiber_lifting (K : Type*) [Field K] [NumberField K]
    (C : ClassGroup (𝓞 K)) :
    ∃ J : (Ideal (𝓞 K))⁰, ClassGroup.mk0 J = C⁻¹ ∧
      (Ideal.absNorm (J : Ideal (𝓞 K)) : Real) ≤ normBound K ∧
      ∀ I : (Ideal (𝓞 K))⁰, ClassGroup.mk0 I = C →
        ∃ z : 𝓞 K, NormLift (I : Ideal (𝓞 K)) (J : Ideal (𝓞 K)) z := by
  obtain ⟨J, hJ, hb⟩ := NumberField.exists_ideal_in_class_of_norm_le C⁻¹
  refine ⟨J, hJ, hb, ?_⟩
  intro I hI
  apply lift_in_inverse_class K I J
  rw [hI, hJ, inv_inv]

/-- Actual kernel norm proves nonzeroness; it is not supplied by the caller. -/
def residueIdeal (K : Type*) [Field K] [NumberField K]
    (p : Nat) (hp : 0 < p) (f : 𝓞 K →+* ZMod p) : (Ideal (𝓞 K))⁰ :=
  ⟨RingHom.ker f, Ideal.absNorm_ne_zero_iff_mem_nonZeroDivisors.mp (by
    rw [residueKernel_absNorm K p f]
    exact ne_of_gt hp)⟩

theorem residue_class_lifting (K : Type*) [Field K] [NumberField K]
    (C : ClassGroup (𝓞 K)) :
    ∃ J : (Ideal (𝓞 K))⁰, ClassGroup.mk0 J = C⁻¹ ∧
      (Ideal.absNorm (J : Ideal (𝓞 K)) : Real) ≤ normBound K ∧
      ∀ (p : Nat) (hp : 0 < p) (f : 𝓞 K →+* ZMod p),
        ClassGroup.mk0 (residueIdeal K p hp f) = C →
        ∃ z : 𝓞 K, NormLift (RingHom.ker f) (J : Ideal (𝓞 K)) z ∧
          (Algebra.norm Int z).natAbs = p*Ideal.absNorm (J : Ideal (𝓞 K)) := by
  obtain ⟨J, hJ, hb, hall⟩ := class_fiber_lifting K C
  refine ⟨J, hJ, hb, ?_⟩
  intro p hp f hc
  obtain ⟨z, hz⟩ := hall (residueIdeal K p hp f) hc
  refine ⟨z, hz, ?_⟩
  have hn := hz.2.2.2.1
  simpa only [residueIdeal, residueKernel_absNorm K p f] using hn

theorem negation_control (K : Type*) [Field K] [NumberField K]
    (I J : Ideal (𝓞 K)) (z : 𝓞 K) (h : NormLift I J z) : NormLift I J (-z) := by
  have hn : (Algebra.norm Int (-z)).natAbs = (Algebra.norm Int z).natAbs := by
    rw [← Ideal.absNorm_span_singleton, Ideal.span_singleton_neg, Ideal.absNorm_span_singleton]
  refine ⟨neg_ne_zero.mpr h.1, J.neg_mem h.2.1, ?_, ?_, ?_⟩
  · simpa only [Ideal.span_singleton_neg] using h.2.2.1
  · rw [hn]; exact h.2.2.2.1
  · intro I' hI'
    exact h.2.2.2.2 I' (by simpa only [Ideal.span_singleton_neg] using hI')

theorem zero_ideal_guard_control :
    ¬ Function.Injective (fun I : Ideal (𝓞 Rat) => I*(0 : Ideal (𝓞 Rat))) := by
  intro h
  have he : (⊥ : Ideal (𝓞 Rat)) = ⊤ := h (by simp)
  exact bot_ne_top he

theorem zero_modulus_control (K : Type*) [Field K] [NumberField K]
    (f : 𝓞 K →+* ZMod 0) :
    Ideal.absNorm (RingHom.ker f) = 0 ∧ RingHom.ker f ∉ (Ideal (𝓞 K))⁰ := by
  constructor
  · exact residueKernel_absNorm K 0 f
  · rw [← Ideal.absNorm_ne_zero_iff_mem_nonZeroDivisors, residueKernel_absNorm K 0 f]
    simp

theorem rational_three_control :
    let f : 𝓞 Rat →+* ZMod 3 :=
      (Int.castRingHom (ZMod 3)).comp Rat.ringOfIntegersEquiv.toRingHom
    ∃ J : (Ideal (𝓞 Rat))⁰, ∃ z : 𝓞 Rat,
      NormLift (RingHom.ker f) (J : Ideal (𝓞 Rat)) z ∧
      (Algebra.norm Int z).natAbs = 3*Ideal.absNorm (J : Ideal (𝓞 Rat)) ∧
      (Ideal.absNorm (J : Ideal (𝓞 Rat)) : Real) ≤ normBound Rat := by
  dsimp only
  let f : 𝓞 Rat →+* ZMod 3 :=
    (Int.castRingHom (ZMod 3)).comp Rat.ringOfIntegersEquiv.toRingHom
  obtain ⟨J, hJ, hb, hall⟩ := residue_class_lifting Rat
    (ClassGroup.mk0 (residueIdeal Rat 3 (by norm_num) f))
  obtain ⟨z, hz, hn⟩ := hall 3 (by norm_num) f rfl
  exact ⟨J, z, hz, hn, hb⟩
end
end TenthDiscriminant.ClassFiber

#check TenthDiscriminant.ClassFiber.class_fiber_lifting
#check TenthDiscriminant.ClassFiber.residue_class_lifting
#print TenthDiscriminant.ClassFiber.NormLift
#print axioms TenthDiscriminant.ClassFiber.class_fiber_lifting
#print axioms TenthDiscriminant.ClassFiber.residue_class_lifting
#audit_namespace TenthDiscriminant.ClassFiber
