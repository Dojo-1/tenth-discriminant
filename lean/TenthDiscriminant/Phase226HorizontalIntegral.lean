import TenthDiscriminant.Phase225Band
import TenthDiscriminant.JetPower

/-!
# Phase226: horizontal Frobenius squared in the ORIGINAL integral order

The inert quadratic residue calculation is moved to the original
integer-pair power, then to Zsqrtd(-D), without changing the original
sample set, row ordering, conjugation, or ordinary Z-derivative.

This certifies the universal integral W^(p*p)-W factor. The combined
rectangular two-generator unimodular matrix and its Gram determinant
factor remain SEPARATE obligations.
-/

namespace TenthDiscriminant.Phase226

open Polynomial

/-- Frobenius twice fixes every element of the actual inert quadratic
residue ring. The type is the original pair ring, NOT an abstract
substitute field. -/
theorem residue_frobenius_squared
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : QuadraticResidue D p) :
    a ^ (p * p) = a := by
  calc
    a ^ (p * p) = (a ^ p) ^ p := pow_mul a p p
    _ = a := by
      rw [Phase223.residue_frobenius_conj D p hp2 hnonsquare (a ^ p)]
      rw [Phase223.residue_frobenius_conj D p hp2 hnonsquare a]
      apply QuadraticResidue.ext <;> simp

/-- The same identity is expressed in the repository's original
two-coordinate residuePairPow, not an alternate quotient. -/
theorem residuePair_frobenius_squared
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : ZMod p × ZMod p) :
    residuePairPow D p a (p * p) = a := by
  apply QuadraticResidue.ofPair_injective D p
  rw [QuadraticResidue.ofPair_pow]
  exact residue_frobenius_squared D p hp2 hnonsquare
    (QuadraticResidue.ofPair D p a)

/-- The actual integer conjugate coordinate w=conj(z) satisfies
w^(p*p)=w modulo p in BOTH integer coordinates. -/
theorem integerPair_conjugate_frobenius_squared
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : Int × Int) :
    (p : Int) ∣ (pairPow D (pairConj a) (p * p)).1 - (pairConj a).1 ∧
    (p : Int) ∣ (pairPow D (pairConj a) (p * p)).2 - (pairConj a).2 := by
  have h : residuePair p (pairPow D (pairConj a) (p * p)) =
      residuePair p (pairConj a) := by
    rw [residuePair_pow]
    exact residuePair_frobenius_squared D p hp2 hnonsquare
      (residuePair p (pairConj a))
  constructor
  · apply (ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mp
    rw [Int.cast_sub]
    exact sub_eq_zero.mpr (congrArg Prod.fst h)
  · apply (ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mp
    rw [Int.cast_sub]
    exact sub_eq_zero.mpr (congrArg Prod.snd h)

/-- The horizontal order-zero factor is divisible by p inside the
selected INTEGRAL quadratic order, not just in a residue image. -/
theorem horizontal_zsqrtd_frobenius_squared
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : Int × Int) :
    (p : Zsqrtd (-(D : Int))) ∣
      (star (pairZsqrtdEquiv D a)) ^ (p * p) -
        star (pairZsqrtdEquiv D a) := by
  have hzero := integerPair_conjugate_frobenius_squared
    D p hp2 hnonsquare a
  apply (zsqrtd_natCast_dvd_iff (-(D : Int)) p _).2
  rw [← pairZsqrtd_conj D a,
      ← pairZsqrtd_pow D (pairConj a) (p * p)]
  simpa [pairZsqrtdEquiv] using hzero

/-- All ORIGINAL ordinary derivatives of a constant horizontal
polynomial power inherit the p^k factor; no Hasse derivatives or
factorial inversion occur. -/
theorem horizontal_constant_jet_power_dvd
    {A : Type*} [CommRing A] (B : A[X]) (z w : A)
    (p k j : Nat) (hzero : (p : A) ∣ w ^ (p * p) - w) :
    (p : A) ^ k ∣
      (derivative^[j] (B * (C (w ^ (p * p) - w)) ^ k)).eval z := by
  apply jet_power_dvd B (C (w ^ (p * p) - w)) z (p : A)
    (fun t => ?_) k j
  by_cases ht : t = 0
  · subst t
    simpa using hzero
  · rw [iterate_derivative_C (Nat.pos_of_ne_zero ht)]
    simp

/-- Same original ordinary-Z-jet carrier in the selected integer
quadratic order. The vertical Frobenius row weight is not included
here; proving additivity will use one combined source matrix. -/
theorem horizontal_original_ordinary_jet_dvd
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : Int × Int)
    (B : (Zsqrtd (-(D : Int)))[X]) (k j : Nat) :
    (p : Zsqrtd (-(D : Int))) ^ k ∣
      (derivative^[j]
        (B * (C ((star (pairZsqrtdEquiv D a)) ^ (p * p) -
          star (pairZsqrtdEquiv D a))) ^ k)).eval
        (pairZsqrtdEquiv D a) := by
  exact horizontal_constant_jet_power_dvd B
    (pairZsqrtdEquiv D a) (star (pairZsqrtdEquiv D a))
    p k j (horizontal_zsqrtd_frobenius_squared D p hp2 hnonsquare a)

/-- A small source-matched inert witness; p=3 gives W^9-W. -/
theorem original_nineteen_three_horizontal
    (a : Int × Int) :
    (3 : Zsqrtd (-(19 : Int))) ∣
      (star (pairZsqrtdEquiv 19 a)) ^ 9 -
        star (pairZsqrtdEquiv 19 a) := by
  letI : Fact (Nat.Prime 3) := ⟨by decide⟩
  simpa using horizontal_zsqrtd_frobenius_squared 19 3
    (by decide) nineteen_three_nonsquare a

/-- The p^2 identity is not universal in ramified quadratic residue
rings. The generator of F_3[t]/(t^2) gives a negative control. -/
theorem ramified_horizontal_negative_control :
    residuePairPow 3 3 (0, 1) (3 * 3) ≠
      ((0, 1) : ZMod 3 × ZMod 3) := by
  decide

end TenthDiscriminant.Phase226

#print axioms TenthDiscriminant.Phase226.residue_frobenius_squared
#print axioms TenthDiscriminant.Phase226.residuePair_frobenius_squared
#print axioms TenthDiscriminant.Phase226.integerPair_conjugate_frobenius_squared
#print axioms TenthDiscriminant.Phase226.horizontal_zsqrtd_frobenius_squared
#print axioms TenthDiscriminant.Phase226.horizontal_constant_jet_power_dvd
#print axioms TenthDiscriminant.Phase226.horizontal_original_ordinary_jet_dvd
#print axioms TenthDiscriminant.Phase226.original_nineteen_three_horizontal
#print axioms TenthDiscriminant.Phase226.ramified_horizontal_negative_control
