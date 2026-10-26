import TenthDiscriminant.SmallPrimeBridge
import Mathlib.NumberTheory.NumberField.ClassNumber
import Mathlib.RingTheory.Ideal.Norm.AbsNorm

/-!
# From class number one to a principal element of prime norm

This is a general number-field statement. It does not yet construct a
residue homomorphism from a quadratic root or identify the abstract
integer norm with `principalNorm`.
-/
namespace TenthDiscriminant

open NumberField
open scoped NumberField

/-- A quotient of the integer ring onto `ZMod p` has ideal norm `p`.
Surjectivity is automatic for a ring map to `ZMod p`. The identity is
valid for any modulus; the intended application uses a prime. -/
theorem residueKernel_absNorm (K : Type*) [Field K] [NumberField K]
    (p : Nat) (f : 𝓞 K →+* ZMod p) :
    Ideal.absNorm (RingHom.ker f) = p := by
  rw [Ideal.absNorm_apply, Submodule.cardQuot_apply]
  calc
    Nat.card ((𝓞 K) ⧸ RingHom.ker f) = Nat.card (ZMod p) :=
      Nat.card_congr (RingHom.quotientKerEquivOfSurjective
        (ZMod.ringHom_surjective f)).toEquiv
    _ = p := Nat.card_zmod p

/-- Class number one makes that quotient ideal principal. The
absolute value is essential for an arbitrary number field. -/
theorem exists_integer_of_absNorm_of_classNumber_one
    (K : Type*) [Field K] [NumberField K]
    (p : Nat) (f : 𝓞 K →+* ZMod p)
    (hclass : NumberField.classNumber K = 1) :
    ∃ a : 𝓞 K, (Algebra.norm ℤ a).natAbs = p := by
  letI : IsPrincipalIdealRing (𝓞 K) :=
    (NumberField.classNumber_eq_one_iff).mp hclass
  let I : Ideal (𝓞 K) := RingHom.ker f
  let a : 𝓞 K := Submodule.IsPrincipal.generator I
  refine ⟨a, ?_⟩
  have hprincipal : Ideal.span ({a} : Set (𝓞 K)) = I :=
    Ideal.span_singleton_generator I
  calc
    (Algebra.norm ℤ a).natAbs =
        Ideal.absNorm (Ideal.span ({a} : Set (𝓞 K))) :=
      (Ideal.absNorm_span_singleton a).symm
    _ = Ideal.absNorm I := congrArg Ideal.absNorm hprincipal
    _ = p := residueKernel_absNorm K p f

/-- A small nonvacuous control: the integer ring of `ℚ` maps to
`ZMod 3`, and the theorem produces an element of norm magnitude `3`. -/
theorem rational_three_absNorm_control :
    ∃ a : 𝓞 ℚ, (Algebra.norm ℤ a).natAbs = 3 := by
  let f : 𝓞 ℚ →+* ZMod 3 :=
    (Int.castRingHom (ZMod 3)).comp Rat.ringOfIntegersEquiv.toRingHom
  exact exists_integer_of_absNorm_of_classNumber_one ℚ 3 f Rat.classNumber_eq

end TenthDiscriminant
