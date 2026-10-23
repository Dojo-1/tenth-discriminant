import TenthDiscriminant.JetPower
import TenthDiscriminant.FrobeniusJet

/-!
# Conjugation as an operator on valid local samples

Validity here is the explicit coordinatewise congruence used by the
ordinary-jet theorem, not a global class-number assertion.
-/
namespace TenthDiscriminant

/-- Conjugation is an involution on the verifier's exact integer pairs. -/
theorem pairConj_involutive (a : Int × Int) :
    pairConj (pairConj a) = a := by
  cases a
  simp [pairConj]

/-- Conjugation respects multiplication in the selected quadratic order. -/
theorem pairConj_mul (D : Nat) (a b : Int × Int) :
    pairConj (pairMul D a b) = pairMul D (pairConj a) (pairConj b) := by
  apply Prod.ext
  · simp [pairConj, pairMul]
  · simp [pairConj, pairMul]
    ring

/-- It therefore commutes with every natural power. -/
theorem pairPow_conj (D n : Nat) (a : Int × Int) :
    pairPow D (pairConj a) n = pairConj (pairPow D a n) := by
  induction n with
  | zero => rfl
  | succ n ih =>
      rw [pairPow, ih, pairPow, pairConj_mul]

/-- The local Frobenius premise is closed under exact conjugation.
This creates another valid sample, not another global discriminant. -/
theorem frobenius_congruence_conj (D p : Nat) (a : Int × Int)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    (p : Int) ∣ (pairPow D (pairConj a) p).1 -
      (pairConj (pairConj a)).1 ∧
    (p : Int) ∣ (pairPow D (pairConj a) p).2 -
      (pairConj (pairConj a)).2 := by
  rw [pairPow_conj, pairConj_involutive]
  constructor
  · simpa only [pairConj] using hzero.1
  · have h := dvd_neg.mpr hzero.2
    convert h using 1
    simp only [pairConj]
    ring

/-- Composing conjugation with the existing jet theorem gives every
ordinary derivative jet at the reflected sample, not just order zero. -/
theorem frobeniusJet_conj_dvd (D p : Nat) (a : Int × Int)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2)
    (j : Nat) :
    (p : Int) ∣ (frobeniusJet D p (pairConj a) j).1 ∧
      (p : Int) ∣ (frobeniusJet D p (pairConj a) j).2 :=
  frobeniusJet_dvd_of_zero_congruence D p (pairConj a)
    (frobenius_congruence_conj D p a hzero) j

/-- A non-real pilot sample is valid at `D=19,p=3`; conjugation gives
the opposite non-real sample, rather than only a vacuous real case. -/
theorem frobenius_congruence_conj_pilot :
    (3 : Int) ∣ (pairPow 19 (pairConj (0, 1)) 3).1 -
      (pairConj (pairConj (0, 1))).1 ∧
    (3 : Int) ∣ (pairPow 19 (pairConj (0, 1)) 3).2 -
      (pairConj (pairConj (0, 1))).2 := by
  apply frobenius_congruence_conj
  norm_num [pairPow, pairMul, pairConj]

end TenthDiscriminant
