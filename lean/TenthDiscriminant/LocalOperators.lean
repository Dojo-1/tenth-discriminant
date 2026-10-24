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

/-- Coordinatewise and discriminant congruences modulo `p` are preserved
by multiplication in the selected quadratic order. -/
theorem pairMul_congruence (D₁ D₂ p : Nat) (a₁ a₂ b₁ b₂ : Int × Int)
    (hD : (p : Int) ∣ (D₁ : Int) - (D₂ : Int))
    (ha : (p : Int) ∣ a₁.1 - a₂.1 ∧ (p : Int) ∣ a₁.2 - a₂.2)
    (hb : (p : Int) ∣ b₁.1 - b₂.1 ∧ (p : Int) ∣ b₁.2 - b₂.2) :
    (p : Int) ∣ (pairMul D₁ a₁ b₁).1 - (pairMul D₂ a₂ b₂).1 ∧
    (p : Int) ∣ (pairMul D₁ a₁ b₁).2 - (pairMul D₂ a₂ b₂).2 := by
  rcases hD with ⟨kD, hkD⟩
  rcases ha with ⟨⟨ka1, hka1⟩, ⟨ka2, hka2⟩⟩
  rcases hb with ⟨⟨kb1, hkb1⟩, ⟨kb2, hkb2⟩⟩
  have hD_eq : (D₁ : Int) = (D₂ : Int) + (p : Int) * kD := by omega
  have ha1_eq : a₁.1 = a₂.1 + (p : Int) * ka1 := by omega
  have ha2_eq : a₁.2 = a₂.2 + (p : Int) * ka2 := by omega
  have hb1_eq : b₁.1 = b₂.1 + (p : Int) * kb1 := by omega
  have hb2_eq : b₁.2 = b₂.2 + (p : Int) * kb2 := by omega
  constructor
  · simp only [pairMul]
    rw [hD_eq, ha1_eq, ha2_eq, hb1_eq, hb2_eq]
    refine ⟨ka1 * b₂.1 + a₂.1 * kb1 + (p : Int) * ka1 * kb1 -
      (kD * a₂.2 * b₂.2 + (D₂ : Int) * ka2 * b₂.2 + (D₂ : Int) * a₂.2 * kb2 +
        (p : Int) * kD * ka2 * b₂.2 + (p : Int) * kD * a₂.2 * kb2 +
        (D₂ : Int) * (p : Int) * ka2 * kb2 +
        (p : Int) ^ 2 * kD * ka2 * kb2), ?_⟩
    ring
  · simp only [pairMul]
    rw [ha1_eq, ha2_eq, hb1_eq, hb2_eq]
    refine ⟨ka1 * b₂.2 + a₂.1 * kb2 + (p : Int) * ka1 * kb2 +
      (ka2 * b₂.1 + a₂.2 * kb1 + (p : Int) * ka2 * kb1), ?_⟩
    ring

/-- Natural powers in the selected quadratic order respect congruence of
both the discriminant parameter `D` and the sample `a` modulo `p`. -/
theorem pairPow_congruence (D₁ D₂ p n : Nat) (a b : Int × Int)
    (hD : (p : Int) ∣ (D₁ : Int) - (D₂ : Int))
    (hab : (p : Int) ∣ a.1 - b.1 ∧ (p : Int) ∣ a.2 - b.2) :
    (p : Int) ∣ (pairPow D₁ a n).1 - (pairPow D₂ b n).1 ∧
    (p : Int) ∣ (pairPow D₁ a n).2 - (pairPow D₂ b n).2 := by
  induction n with
  | zero =>
      simp [pairPow]
  | succ n ih =>
      simp only [pairPow]
      exact pairMul_congruence D₁ D₂ p (pairPow D₁ a n) (pairPow D₂ b n) a b hD ih hab

/-- Residue-fiber transport operator `T`: replacing `D₁, a` by `D₂, b` within
the same residue fiber modulo `p` preserves the explicit order-zero Frobenius
congruence. This explores a local residue fiber without claiming global
class-number invariance. -/
theorem frobenius_congruence_of_mod_eq (D₁ D₂ p : Nat) (a b : Int × Int)
    (hD : (p : Int) ∣ (D₁ : Int) - (D₂ : Int))
    (hab : (p : Int) ∣ a.1 - b.1 ∧ (p : Int) ∣ a.2 - b.2)
    (hzero : (p : Int) ∣ (pairPow D₁ a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D₁ a p).2 - (pairConj a).2) :
    (p : Int) ∣ (pairPow D₂ b p).1 - (pairConj b).1 ∧
    (p : Int) ∣ (pairPow D₂ b p).2 - (pairConj b).2 := by
  have hpow := pairPow_congruence D₁ D₂ p p a b hD hab
  rcases hpow with ⟨⟨kp1, hkp1⟩, ⟨kp2, hkp2⟩⟩
  rcases hab with ⟨⟨kab1, hkab1⟩, ⟨kab2, hkab2⟩⟩
  rcases hzero with ⟨⟨kz1, hkz1⟩, ⟨kz2, hkz2⟩⟩
  constructor
  · simp only [pairConj] at hkz1 ⊢
    have h1 : (pairPow D₂ b p).1 = (pairPow D₁ a p).1 - (p : Int) * kp1 := by omega
    have h2 : b.1 = a.1 - (p : Int) * kab1 := by omega
    have h3 : (pairPow D₁ a p).1 = a.1 + (p : Int) * kz1 := by omega
    rw [h1, h2, h3]
    refine ⟨kz1 - kp1 + kab1, ?_⟩
    ring
  · simp only [pairConj] at hkz2 ⊢
    have h1 : (pairPow D₂ b p).2 = (pairPow D₁ a p).2 - (p : Int) * kp2 := by omega
    have h2 : b.2 = a.2 - (p : Int) * kab2 := by omega
    have h3 : (pairPow D₁ a p).2 = -a.2 + (p : Int) * kz2 := by omega
    rw [h1, h2, h3]
    refine ⟨kz2 - kp2 - kab2, ?_⟩
    ring

/-- Composing residue-fiber transport with the all-order one-factor jet
theorem transfers every ordinary derivative jet across the residue fiber. -/
theorem frobeniusJet_of_mod_eq_dvd (D₁ D₂ p : Nat) (a b : Int × Int)
    (hD : (p : Int) ∣ (D₁ : Int) - (D₂ : Int))
    (hab : (p : Int) ∣ a.1 - b.1 ∧ (p : Int) ∣ a.2 - b.2)
    (hzero : (p : Int) ∣ (pairPow D₁ a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D₁ a p).2 - (pairConj a).2)
    (j : Nat) :
    (p : Int) ∣ (frobeniusJet D₂ p b j).1 ∧
      (p : Int) ∣ (frobeniusJet D₂ p b j).2 :=
  frobeniusJet_dvd_of_zero_congruence D₂ p b
    (frobenius_congruence_of_mod_eq D₁ D₂ p a b hD hab hzero) j

/-- Composing residue-fiber transport with the ordinary-jet power theorem
transfers `p^k` coordinate divisibility of `Z^(r-pk) W^s (Z^p-W)^k` across
congruent `(D, a)` pairs modulo `p`. -/
theorem rectangular_frobenius_row_jet_of_mod_eq
    (D₁ D₂ p r s k j : Nat) (a b : Int × Int)
    (hD : (p : Int) ∣ (D₁ : Int) - (D₂ : Int))
    (hab : (p : Int) ∣ a.1 - b.1 ∧ (p : Int) ∣ a.2 - b.2)
    (hzero : (p : Int) ∣ (pairPow D₁ a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D₁ a p).2 - (pairConj a).2) :
    let z := pairZsqrtdEquiv D₂ b
    let P : Polynomial (Zsqrtd (-(D₂ : Int))) :=
      Polynomial.X ^ (r - p * k) * Polynomial.C (star z) ^ s *
        (Polynomial.X ^ p - Polynomial.C (star z)) ^ k
    (p : Int) ^ k ∣ ((Polynomial.derivative^[j] P).eval z).re ∧
      (p : Int) ^ k ∣ ((Polynomial.derivative^[j] P).eval z).im :=
  rectangular_frobenius_row_jet_coordinates D₂ p r s k j b
    (frobenius_congruence_of_mod_eq D₁ D₂ p a b hD hab hzero)

/-- Pilot check: transporting `(D₁=1, a=(0,1))` across the modulo-`3` fiber
to `(D₂=19, b=(3,-2))` preserves the order-zero Frobenius congruence. -/
theorem frobenius_congruence_residue_transport_pilot :
    (3 : Int) ∣ (pairPow 19 (3, -2) 3).1 - (pairConj (3, -2)).1 ∧
    (3 : Int) ∣ (pairPow 19 (3, -2) 3).2 - (pairConj (3, -2)).2 := by
  apply frobenius_congruence_of_mod_eq 1 19 3 (0, 1) (3, -2)
  · decide
  · decide
  · decide

end TenthDiscriminant
