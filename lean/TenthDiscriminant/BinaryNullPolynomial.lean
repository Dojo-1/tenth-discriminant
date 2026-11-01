import TenthDiscriminant.IntegerTraceGram

/-!
# A quadratic-order null polynomial at the binary prime

For every integer-pair point z = x + y * sqrt(-D), the coordinates of
F(z) = z^4 - z^2 are even. This is a source-level lemma, NOT yet
a proof of the determinant floor involving powers of F and all jets.

The rectangular ordinary-jet convention and 2,2D trace metric are unchanged.
-/
namespace TenthDiscriminant
set_option autoImplicit false

private theorem two_dvd_consecutive (a : Int) :
    (2 : Int) ∣ a * (a - 1) := by
  have h : a % 2 = 0 ∨ a % 2 = 1 := by omega
  rcases h with hzero | hone
  · refine ⟨(a / 2) * (a - 1), ?_⟩
    have ha : a = 2 * (a / 2) := by omega
    calc
      a * (a - 1) = (2 * (a / 2)) * (a - 1) := by rw [← ha]
      _ = 2 * ((a / 2) * (a - 1)) := by ring
  · refine ⟨a * ((a - 1) / 2), ?_⟩
    have ha : a - 1 = 2 * ((a - 1) / 2) := by omega
    calc
      a * (a - 1) = a * (2 * ((a - 1) / 2)) := by rw [← ha]
      _ = 2 * (a * ((a - 1) / 2)) := by ring

/-- Every integer quadratic-order point makes z^4-z^2 even in BOTH
coordinates. No inertness, positivity or field-class assumption is used. -/
theorem binaryNullPower_even (D : Nat) (q : Int × Int) :
    (2 : Int) ∣ (pairPow D q 4).1 - (pairPow D q 2).1 ∧
    (2 : Int) ∣ (pairPow D q 4).2 - (pairPow D q 2).2 := by
  rcases q with ⟨x, y⟩
  let a : Int := x * x - (D : Int) * y * y
  let b : Int := 2 * x * y
  have hreal :
      (pairPow D (x, y) 4).1 - (pairPow D (x, y) 2).1 =
        a * (a - 1) - (D : Int) * b * b := by
    simp [a, b, pairPow, pairMul] <;> ring
  have him :
      (pairPow D (x, y) 4).2 - (pairPow D (x, y) 2).2 =
        b * (2 * a - 1) := by
    simp [a, b, pairPow, pairMul] <;> ring
  have hb : (2 : Int) ∣ b := by
    refine ⟨x * y, ?_⟩
    dsimp [b]
    ring
  have hterm : (2 : Int) ∣ (D : Int) * b * b := by
    rcases hb with ⟨c, hc⟩
    refine ⟨(D : Int) * c * b, ?_⟩
    rw [hc]
    ring
  constructor
  · rw [hreal]
    exact (two_dvd_consecutive a).sub hterm
  · rw [him]
    rcases hb with ⟨c, hc⟩
    refine ⟨c * (2 * a - 1), ?_⟩
    rw [hc]
    ring

/-- The tempting quadratic replacement z^2-z does NOT vanish modulo two:
the imaginary coordinate at z=sqrt(-3) is odd. -/
theorem binaryNullDegreeTwo_negative_control :
    ¬ (2 : Int) ∣ (pairPow 3 (0, 1) 2).2 - (0 : Int) - 1 := by
  norm_num [pairPow, pairMul]

/-- The paper-level proposed Gram valuation exponent. The link from this
number to the original transformed ordinary jets is a separate proof task. -/
def binaryNullGramExponent (R S : Nat) : Nat :=
  R * S + 2 * S * ∑ r ∈ Finset.range R, r / 4

theorem binaryNullGramExponent_30_5 :
    binaryNullGramExponent 30 5 = 1130 := by decide

theorem binaryNullGramExponent_8_4 :
    binaryNullGramExponent 8 4 = 64 := by decide

end TenthDiscriminant
