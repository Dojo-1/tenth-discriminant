import TenthDiscriminant.RectangularGramFactor
import TenthDiscriminant.QuadraticResidueRing
import Mathlib.NumberTheory.LegendreSymbol.Basic

/-!
# The residue generator under an inert quadratic local condition

This is a bounded bridge from a nonsquare parameter to the actual
pair-residue power operation. It does not yet assert Freshman's dream
for arbitrary pairs.
-/
namespace TenthDiscriminant

private theorem residueGenerator_even_odd (D p n : Nat) :
    residuePairPow D p (0, 1) (2 * n) = ((-(D : ZMod p)) ^ n, 0) ∧
    residuePairPow D p (0, 1) (2 * n + 1) = (0, (-(D : ZMod p)) ^ n) := by
  induction n with
  | zero =>
      simp [residuePairPow, residuePairMul]
  | succ n ih =>
      obtain ⟨_, hodd⟩ := ih
      have heven' : residuePairPow D p (0, 1) (2 * (n + 1)) =
          ((-(D : ZMod p)) ^ (n + 1), 0) := by
        rw [show 2 * (n + 1) = (2 * n + 1) + 1 by omega,
          residuePairPow, hodd]
        simp [residuePairMul, pow_succ]
        ring
      constructor
      · exact heven'
      · rw [residuePairPow]
        rw [heven']
        simp [residuePairMul]

/-- Euler's criterion makes the generator `t²=-D` conjugate under
the `p`-power map. This is the actual residue pair power, not a
separate quotient-field model. -/
theorem residueGenerator_pow_prime (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p))) :
    residuePairPow D p (0, 1) p = (0, -1) := by
  have hodd : p % 2 = 1 := (Nat.Prime.eq_two_or_odd (Fact.out : p.Prime)).resolve_left hp2
  have hnonzero : (-(D : ZMod p)) ≠ 0 := by
    intro hz
    apply hnonsquare
    rw [hz]
    exact ⟨0, by simp⟩
  have hpow : (-(D : ZMod p)) ^ (p / 2) = -1 := by
    rcases ZMod.pow_div_two_eq_neg_one_or_one p hnonzero with hone | hneg
    · exact False.elim (hnonsquare ((ZMod.euler_criterion p hnonzero).2 hone))
    · exact hneg
  have hp : p = 2 * (p / 2) + 1 := by omega
  calc
    residuePairPow D p (0, 1) p =
        residuePairPow D p (0, 1) (2 * (p / 2) + 1) :=
      congrArg (residuePairPow D p (0, 1)) hp
    _ = (0, -1) := by rw [(residueGenerator_even_odd D p (p / 2)).2, hpow]

private theorem quadraticResidue_charP (D p : Nat) [Fact p.Prime] :
    CharP (QuadraticResidue D p) p := by
  letI : Nontrivial (QuadraticResidue D p) :=
    ⟨⟨0, 1, by
      intro h
      exact (zero_ne_one : (0 : ZMod p) ≠ 1) (congrArg QuadraticResidue.re h)⟩⟩
  exact CharP.of_ringHom_of_ne_zero (QuadraticResidue.scalar D p) p
    (Fact.out : p.Prime).ne_zero

/-- In characteristic `p`, the generator identity extends to every
pair by Freshman's dream. The ring chart is exactly the old pair
multiplication and power, so this is not a new observation family. -/
theorem residuePair_pow_conj_of_nonsquare (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : ZMod p × ZMod p) :
    residuePairPow D p a p = residuePairConj a := by
  letI : CharP (QuadraticResidue D p) p := quadraticResidue_charP D p
  let t := QuadraticResidue.generator D p
  have ht : t ^ p = -t := by
    have h := congrArg (QuadraticResidue.ofPair D p)
      (residueGenerator_pow_prime D p hp2 hnonsquare)
    rw [QuadraticResidue.ofPair_pow] at h
    calc
      t ^ p = QuadraticResidue.ofPair D p (0, -1) := h
      _ = -t := by ext <;> simp [t, QuadraticResidue.ofPair,
        QuadraticResidue.generator]
  have hscalar (x : ZMod p) :
      (QuadraticResidue.scalar D p x) ^ p = QuadraticResidue.scalar D p x := by
    rw [← map_pow, ZMod.pow_card]
  apply QuadraticResidue.ofPair_injective D p
  calc
    QuadraticResidue.ofPair D p (residuePairPow D p a p) =
        (QuadraticResidue.ofPair D p a) ^ p :=
      QuadraticResidue.ofPair_pow D p a p
    _ = QuadraticResidue.scalar D p a.1 -
        QuadraticResidue.scalar D p a.2 * t := by
      conv_lhs => rw [QuadraticResidue.decompose D p (QuadraticResidue.ofPair D p a)]
      rw [add_pow_char, mul_pow, hscalar, hscalar, ht]
      simp only [QuadraticResidue.ofPair]
      ring
    _ = QuadraticResidue.ofPair D p (residuePairConj a) := by
      simpa only [t] using (QuadraticResidue.ofPair_conj D p a).symm

/-- The precise universal premise required by Phase 7 follows from
quadratic nonsquareness in the selected residue order. -/
theorem integerPair_frobenius_of_nonsquare (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : Int × Int) :
    (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
    (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2 := by
  have h : residuePair p (pairPow D a p) = residuePair p (pairConj a) := by
    rw [residuePair_pow, residuePair_conj]
    exact residuePair_pow_conj_of_nonsquare D p hp2 hnonsquare (residuePair p a)
  constructor
  · apply (ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mp
    rw [Int.cast_sub]
    exact sub_eq_zero.mpr (congrArg Prod.fst h)
  · apply (ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mp
    rw [Int.cast_sub]
    exact sub_eq_zero.mpr (congrArg Prod.snd h)

/-- Ender's exact determinant exponent for the existing integer
rectangular Gram, under the explicit nonsquare local condition. -/
theorem rectangularTraceGram_valuation_of_nonsquare
    (Q : Finset (Int × Int)) (D J R S p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p))) :
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  apply rectangularTraceGram_valuation_of_frobenius Q D J R S p
    (Fact.out : p.Prime).pos
  intro a
  exact integerPair_frobenius_of_nonsquare D p hp2 hnonsquare a

/-- The fixed inert example satisfies the new generic local guard. -/
theorem nineteen_three_nonsquare : ¬ IsSquare (-(19 : ZMod 3)) := by
  decide

/-- The old noninert falsifier fails exactly this guard. -/
theorem two_three_square : IsSquare (-(2 : ZMod 3)) := by
  refine ⟨1, ?_⟩
  decide

/-- Nonsquareness of `-D` modulo `p` depends only on the residue class of `D`
modulo `p`. -/
theorem nonsquare_of_mod_eq (D₁ D₂ p : Nat)
    (hD : (D₁ : ZMod p) = (D₂ : ZMod p))
    (hnonsquare : ¬ IsSquare (-(D₁ : ZMod p))) :
    ¬ IsSquare (-(D₂ : ZMod p)) := by
  rwa [← hD]

/-- Residue-fiber transport for the exact integer Gram valuation: if `D₁` and
`D₂` have the same residue modulo an odd prime `p`, nonsquareness of `-D₁`
yields the full `p^(2F(p))` determinant factor for `D₂`. -/
theorem rectangularTraceGram_valuation_of_mod_eq_nonsquare
    (Q : Finset (Int × Int)) (D₁ D₂ J R S p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hD : (D₁ : ZMod p) = (D₂ : ZMod p))
    (hnonsquare : ¬ IsSquare (-(D₁ : ZMod p))) :
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (integerRectangularTraceGram Q D₂ J R S).det :=
  rectangularTraceGram_valuation_of_nonsquare Q D₂ J R S p hp2
    (nonsquare_of_mod_eq D₁ D₂ p hD hnonsquare)

/-- Index-2 norm embedding: the norm `(pairMul D (x, y) (pairConj (x, y))).1 = x^2 + D * y^2`
in the selected order `ℤ[√(-D)]` equals `principalNorm D (x - y) (2 * y)` in the
maximal-order principal form whenever `D ≡ 3 (mod 4)`. -/
theorem selectedOrderNorm_eq_principalNorm (D : Nat) (x y : Int)
    (hD : (D : Int) % 4 = 3) :
    (pairMul D (x, y) (pairConj (x, y))).1 =
      principalNorm (D : Int) (x - y) (2 * y) := by
  have h4 := principalNorm_four (D : Int) (x - y) (2 * y) hD
  have hpair : (pairMul D (x, y) (pairConj (x, y))).1 = x ^ 2 + (D : Int) * y ^ 2 := by
    simp [pairMul, pairConj]
    ring
  rw [hpair]
  have hring : 4 * (x ^ 2 + (D : Int) * y ^ 2) =
      (2 * (x - y) + 2 * y) ^ 2 + (D : Int) * (2 * y) ^ 2 := by ring
  omega

/-- Local norm obstruction under nonsquareness: if `-D` is nonsquare in `ZMod p`,
then any residue pair `(u, v)` with `u^2 + D * v^2 = 0` in `ZMod p` has `u = 0`
and `v = 0`. -/
theorem norm_eq_zero_iff_of_nonsquare (D p : Nat) [Fact p.Prime]
    (hnonsquare : ¬ IsSquare (-(D : ZMod p))) (u v : ZMod p)
    (hnorm : u ^ 2 + (D : ZMod p) * v ^ 2 = 0) :
    u = 0 ∧ v = 0 := by
  have hv : v = 0 := by
    by_contra hv0
    apply hnonsquare
    refine ⟨u * v⁻¹, ?_⟩
    have h1 : u ^ 2 = -(D : ZMod p) * v ^ 2 := by
      linear_combination hnorm
    have h2 : (u * v⁻¹) * (u * v⁻¹) = u ^ 2 * (v ^ 2)⁻¹ := by ring
    rw [h2, h1, mul_assoc, mul_inv_cancel₀ (pow_ne_zero 2 hv0), mul_one]
  subst hv
  simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, mul_zero,
    add_zero, sq_eq_zero_iff] at hnorm
  exact ⟨hnorm, rfl⟩

/-- If `-D` is nonsquare modulo a prime `p` and `D ≡ 3 (mod 4)`, then `p` can
only divide `4 * principalNorm D x y` when `p` divides both `2 * x + y` and `y`. -/
theorem dvd_four_mul_principalNorm_of_nonsquare (D p : Nat) [Fact p.Prime]
    (hnonsquare : ¬ IsSquare (-(D : ZMod p))) (x y : Int)
    (hD : (D : Int) % 4 = 3)
    (hdvd : (p : Int) ∣ 4 * principalNorm (D : Int) x y) :
    (p : Int) ∣ 2 * x + y ∧ (p : Int) ∣ y := by
  rw [principalNorm_four (D : Int) x y hD] at hdvd
  have hz : (((2 * x + y) ^ 2 + (D : Int) * y ^ 2 : Int) : ZMod p) = 0 :=
    (ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mpr hdvd
  have hz' : ((2 * x + y : Int) : ZMod p) ^ 2 +
      (D : ZMod p) * ((y : Int) : ZMod p) ^ 2 = 0 := by
    simpa only [Int.cast_add, Int.cast_mul, Int.cast_pow, Int.cast_natCast] using hz
  obtain ⟨hu, hv⟩ := norm_eq_zero_iff_of_nonsquare D p hnonsquare
    ((2 * x + y : Int) : ZMod p) ((y : Int) : ZMod p) hz'
  exact ⟨(ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mp hu,
    (ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mp hv⟩

end TenthDiscriminant
