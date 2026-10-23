import TenthDiscriminant.InertFrobenius
import TenthDiscriminant.Arithmetic
import Mathlib.FieldTheory.KummerPolynomial

/-!
# The precise small-prime interface

The norm bound is elementary. The class-group input is isolated as
`SmallPrimeNormLifting`; no theorem in this file derives it from class
number one.
-/
namespace TenthDiscriminant

/-- The still-open global input: a residue root supplies a principal
element of norm `p` in the maximal-order coordinates. -/
def SmallPrimeNormLifting (D p : Nat) : Prop :=
  ∀ z : ZMod p, z ^ 2 = -(D : ZMod p) →
    ∃ x y : Int, principalNorm (D : Int) x y = (p : Int)

/-- A prime integer cannot be a square. -/
private theorem prime_int_not_square (p : Nat) (hp : p.Prime) (x : Int) :
    x ^ 2 ≠ (p : Int) := by
  intro hx
  have hn : x.natAbs ^ 2 = p := by
    simpa only [Int.natAbs_pow, Int.natAbs_natCast] using congrArg Int.natAbs hx
  exact hp.not_isSquare ⟨x.natAbs, by simpa [pow_two] using hn.symm⟩

/-- Strictly below Ender's norm threshold, the norm-lifting input
excludes a residue root. The boundary equality is intentionally absent. -/
theorem small_prime_no_root_of_norm_lifting (D p : Nat)
    (hD : (D : Int) % 4 = 3) (hp : p.Prime)
    (hsmall : (p : Int) < ((D : Int) + 1) / 4)
    (hlift : SmallPrimeNormLifting D p) :
    ∀ z : ZMod p, z ^ 2 ≠ -(D : ZMod p) := by
  intro z hz
  obtain ⟨x, y, hnorm⟩ := hlift z hz
  by_cases hy : y = 0
  · subst y
    have hx : x ^ 2 = (p : Int) := by simpa [principalNorm] using hnorm
    exact prime_int_not_square p hp x hx
  · exact small_norm_impossible (D : Int) x y (p : Int) hD
      (by omega) hy hnorm hsmall

/-- The local guard required by the checked integer Gram theorem. -/
theorem small_prime_nonsquare_of_norm_lifting (D p : Nat)
    (hD : (D : Int) % 4 = 3) (hp : p.Prime)
    (hsmall : (p : Int) < ((D : Int) + 1) / 4)
    (hlift : SmallPrimeNormLifting D p) :
    ¬ IsSquare (-(D : ZMod p)) := by
  rintro ⟨z, hz⟩
  exact small_prime_no_root_of_norm_lifting D p hD hp hsmall hlift z
    (by simpa [pow_two] using hz.symm)

/-- The paper's irreducible-quadratic condition and the precise Lean
local guard are equivalent (also at `p=2`). -/
theorem quadratic_irreducible_iff_nonsquare (D p : Nat) [Fact p.Prime] :
    Irreducible ((Polynomial.X : Polynomial (ZMod p)) ^ 2 +
      Polynomial.C (D : ZMod p)) ↔
      ¬ IsSquare (-(D : ZMod p)) := by
  have h := X_pow_sub_C_irreducible_iff_of_prime
    (K := ZMod p) (show Nat.Prime 2 by decide) (a := -(D : ZMod p))
  simpa only [map_neg, sub_neg_eq_add, IsSquare, pow_two, not_exists, eq_comm] using h

/-- A clean global-to-local-to-determinant interface. This is not a
class-number theorem: `hlift` must still be proved from ideal theory. -/
theorem rectangularTraceGram_valuation_of_small_prime_norm_lifting
    (Q : Finset (Int × Int)) (D J R S p : Nat) [Fact p.Prime]
    (hD : (D : Int) % 4 = 3) (hp2 : p ≠ 2)
    (hsmall : (p : Int) < ((D : Int) + 1) / 4)
    (hlift : SmallPrimeNormLifting D p) :
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  exact rectangularTraceGram_valuation_of_nonsquare Q D J R S p hp2
    (small_prime_nonsquare_of_norm_lifting D p hD Fact.out hsmall hlift)

/-- `D=15,p=3` is a strict small ramified-prime control: a residue
root exists, so the lifting premise is false. This rules out silently
dropping that global premise from the public theorem. -/
theorem fifteen_three_not_norm_lifting : ¬ SmallPrimeNormLifting 15 3 := by
  intro hlift
  have hno := small_prime_no_root_of_norm_lifting 15 3
    (by decide) (by decide) (by decide) hlift
  exact hno 0 (by decide)

/-- The already checked inert control has the paper's polynomial form. -/
theorem nineteen_three_quadratic_irreducible :
    Irreducible ((Polynomial.X : Polynomial (ZMod 3)) ^ 2 +
      Polynomial.C (19 : ZMod 3)) := by
  exact (quadratic_irreducible_iff_nonsquare 19 3).2 nineteen_three_nonsquare

end TenthDiscriminant
