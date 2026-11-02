import TenthDiscriminant.BinaryNullMixedJets
import TenthDiscriminant.LocalOperators

/-!
# Phase163: true source samples for the four differential-null generators

The source sample z is ALWAYS the original x+y sqrt(-D) element and the
constant W is its conjugate. Every derivative is the original ordinary
partial derivative in Z, with W held fixed. This file only proves
source polynomial nullity and its four-factor consequence. The monic
rectangle-preserving row action and 1358 determinant exponent are separate.
-/

namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false

/-- H(Z,W)=Z^2-W^2 has an even order-zero value for every original
integer-pair sample W=conj(Z), including non-real samples. -/
theorem binaryH_sourceValue_dvd (D : Nat) (sample : Int × Int) :
    let z := pairZsqrtdEquiv D sample
    (2 : Zsqrtd (-(D : Int))) ∣ z^2 - (star z)^2 := by
  dsimp
  rw [← pairZsqrtd_conj D sample,
      ← pairZsqrtd_pow D sample 2,
      ← pairZsqrtd_pow D (pairConj sample) 2]
  apply (zsqrtd_natCast_dvd_iff (-(D : Int)) 2 _).2
  rcases sample with ⟨x,y⟩
  constructor
  · simp [pairZsqrtdEquiv, pairPow, pairMul, pairConj]
  · refine ⟨2*x*y, ?_⟩
    simp [pairZsqrtdEquiv, pairPow, pairMul, pairConj] <;> ring

/-- The positive ordinary Z derivatives of H are 2Z, 2, then zero. -/
theorem binaryH_allSourceJets_dvd (D : Nat) (sample : Int × Int)
    (j : Nat) :
    let z := pairZsqrtdEquiv D sample
    (2 : Zsqrtd (-(D : Int))) ∣
      (derivative^[j] (X^2 - C ((star z)^2) :
        (Zsqrtd (-(D : Int)))[X])).eval z := by
  dsimp
  by_cases hj : j = 0
  · subst j
    simpa using binaryH_sourceValue_dvd D sample
  · rw [iterate_derivative_sub, iterate_derivative_C
          (Nat.pos_of_ne_zero hj), sub_zero]
    exact dvd_iterate_derivative_pow X 2 _ hj

/-- F(W)=W^4-W^2 is a source-constant for partial-Z differentiation.
Conjugation preserves the integer-pair order and its binary nullity. -/
theorem binaryFW_allSourceJets_dvd (D : Nat) (sample : Int × Int)
    (j : Nat) :
    let z := pairZsqrtdEquiv D sample
    (2 : Zsqrtd (-(D : Int))) ∣
      (derivative^[j] (C ((star z)^4-(star z)^2) :
        (Zsqrtd (-(D : Int)))[X])).eval z := by
  dsimp
  by_cases hj : j = 0
  · subst j
    change (2 : Zsqrtd (-(D : Int))) ∣
      (star (pairZsqrtdEquiv D sample))^4 -
      (star (pairZsqrtdEquiv D sample))^2
    rw [← pairZsqrtd_conj D sample]
    exact binaryNull_value_dvd_zsqrtd D (pairConj sample)
  · rw [iterate_derivative_C (Nat.pos_of_ne_zero hj)]
    simp

/-- K(Z,W)=Z^2(W^2-1) is an exact source identity
F(Z) - Z^2 H(Z,W). Both terms have all jets even. -/
theorem binaryK_allSourceJets_dvd (D : Nat) (sample : Int × Int)
    (j : Nat) :
    let z := pairZsqrtdEquiv D sample
    (2 : Zsqrtd (-(D : Int))) ∣
      (derivative^[j] (X^2 * C ((star z)^2-1) :
        (Zsqrtd (-(D : Int)))[X])).eval z := by
  dsimp
  let z := pairZsqrtdEquiv D sample
  let w := star z
  have hk : (X^2 * C (w^2-1) :
      (Zsqrtd (-(D : Int)))[X]) =
      (X^4-X^2) - X^2*(X^2-C (w^2)) := by
    simp only [map_sub, map_one]
    ring
  have hH : ∀ t : Nat, (2 : Zsqrtd (-(D : Int))) ∣
      (derivative^[t] (X^2-C (w^2) :
        (Zsqrtd (-(D : Int)))[X])).eval z :=
    binaryH_allSourceJets_dvd D sample
  have hXH : (2 : Zsqrtd (-(D : Int))) ∣
      (derivative^[j] (X^2 * (X^2-C (w^2)) :
        (Zsqrtd (-(D : Int)))[X])).eval z := by
    simpa only [pow_one] using
      (jet_power_dvd (X^2)
        (X^2-C (w^2)) z (2 : Zsqrtd (-(D : Int)))
        hH 1 j)
  rw [hk, iterate_derivative_sub, eval_sub]
  exact (binaryNull_allOrdinaryJets_dvd D sample j).sub hXH

/-- Four TRUE generators from the unchanged source quadratic order.
This is an all-jets factorization, NOT yet a statement about the
original Gram; the monic integer rectangular basis must still be built. -/
theorem binaryFourSourceGenerators_jets_dvd
    (D : Nat) (sample : Int × Int)
    (B : (Zsqrtd (-(D : Int)))[X])
    (a b c d j : Nat) :
    let z := pairZsqrtdEquiv D sample
    let w := star z
    (2 : Zsqrtd (-(D : Int)))^(a+b+c+d) ∣
      (derivative^[j]
        (B * (X^4-X^2)^a * (X^2-C(w^2))^b *
          (C (w^4-w^2))^c * (X^2*C(w^2-1))^d)).eval z := by
  dsimp
  exact mixedJets_fourPowers_dvd B
    (X^4-X^2)
    (X^2-C((star (pairZsqrtdEquiv D sample))^2))
    (C((star (pairZsqrtdEquiv D sample))^4 -
       (star (pairZsqrtdEquiv D sample))^2))
    (X^2*C((star (pairZsqrtdEquiv D sample))^2-1))
    (pairZsqrtdEquiv D sample) (2 : Zsqrtd (-(D : Int)))
    a b c d j
    (binaryNull_allOrdinaryJets_dvd D sample)
    (binaryH_allSourceJets_dvd D sample)
    (binaryFW_allSourceJets_dvd D sample)
    (binaryK_allSourceJets_dvd D sample)

end TenthDiscriminant
