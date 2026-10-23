import TenthDiscriminant.IntegerTraceGram

/-!
# The one-factor local jet bridge

This module isolates a universal derivative fact about `Z^p-W` in the
existing integer-pair coordinates. The congruence at order zero is an
explicit premise; irreducibility and inertness are not hidden assumptions.
-/
namespace TenthDiscriminant

/-- The ordinary `Z`-jet of `Z^p-W` at `(a, conjugate a)`. -/
def frobeniusJet (D p : Nat) (a : Int × Int) (j : Nat) : Int × Int :=
  let z := integerDerivativeRow D p 0 j a
  let w := integerDerivativeRow D 0 1 j a
  (z.1 - w.1, z.2 - w.2)

/-- The zeroth jet is the coordinate form of `a^p - conjugate a`. -/
theorem frobeniusJet_zero (D p : Nat) (a : Int × Int) :
    frobeniusJet D p a 0 =
      ((pairPow D a p).1 - (pairConj a).1,
       (pairPow D a p).2 - (pairConj a).2) := by
  simp [frobeniusJet, integerDerivativeRow, pairScale, pairMul, pairPow,
    Nat.descFactorial]

private theorem descFactorial_dvd_of_pos (p j : Nat) (hj : 0 < j) :
    (p : Int) ∣ (p.descFactorial j : Int) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : j ≠ 0)
  induction k with
  | zero => simp [Nat.descFactorial]
  | succ k ih =>
      rw [Nat.descFactorial_succ]
      simp only [Nat.cast_mul]
      exact dvd_mul_of_dvd_right (ih (by omega)) _

/-- Under the explicit local Frobenius congruence, *every* ordinary
derivative jet of `Z^p-W` has both integer coordinates divisible by `p`.
The theorem is valid for any natural `p`; primality enters only when
one later proves the congruence from residue-field arithmetic. -/
theorem frobeniusJet_dvd_of_zero_congruence (D p : Nat) (a : Int × Int)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2)
    (j : Nat) :
    (p : Int) ∣ (frobeniusJet D p a j).1 ∧
      (p : Int) ∣ (frobeniusJet D p a j).2 := by
  by_cases hj0 : j = 0
  · subst j
    simpa only [frobeniusJet_zero] using hzero
  · have hj : 0 < j := Nat.pos_of_ne_zero hj0
    have hW : integerDerivativeRow D 0 1 j a = (0, 0) := by
      simp [integerDerivativeRow, Nat.not_le.mpr hj]
    by_cases hjp : j ≤ p
    · have hc := descFactorial_dvd_of_pos p j hj
      have hZ : integerDerivativeRow D p 0 j a =
          pairScale (p.descFactorial j : Int)
            (pairMul D (pairPow D a (p - j)) (pairPow D (pairConj a) 0)) := by
        simp [integerDerivativeRow, hjp]
      simp only [frobeniusJet, hZ, hW, pairScale, sub_zero]
      exact ⟨dvd_mul_of_dvd_left hc _, dvd_mul_of_dvd_left hc _⟩
    · have hZ : integerDerivativeRow D p 0 j a = (0, 0) := by
        simp [integerDerivativeRow, hjp]
      simp [frobeniusJet, hZ, hW]

/-- The congruence premise cannot be dropped: `X²+2` splits modulo `3`. -/
theorem frobeniusJet_noninert_negative_control :
    ¬ ((3 : Int) ∣ (pairPow 2 (0, 1) 3).1 - (pairConj (0, 1)).1 ∧
       (3 : Int) ∣ (pairPow 2 (0, 1) 3).2 - (pairConj (0, 1)).2) := by
  norm_num [pairPow, pairMul, pairConj]

end TenthDiscriminant
