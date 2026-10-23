import TenthDiscriminant.IntegerTraceGram
import Mathlib.NumberTheory.Zsqrtd.Basic

/-!
# The selected quadratic order in two coordinate charts

`(x, y)` and `⟨x, y⟩ : Zsqrtd (-(D : Int))` describe the same element of
`ℤ[√(-D)]`. This identifies the arithmetic of the existing integer-pair
construction without changing its matrix or claiming that this selected order
is always the full ring of integers.
-/
namespace TenthDiscriminant

/-- Coordinate equivalence between the verifier's pairs and the selected
quadratic order. No ring structure is added to `Int × Int`. -/
def pairZsqrtdEquiv (D : Nat) : (Int × Int) ≃ Zsqrtd (-(D : Int)) where
  toFun a := ⟨a.1, a.2⟩
  invFun z := (z.re, z.im)
  left_inv a := rfl
  right_inv z := by cases z; rfl

theorem pairZsqrtd_mul (D : Nat) (a b : Int × Int) :
    pairZsqrtdEquiv D (pairMul D a b) =
      pairZsqrtdEquiv D a * pairZsqrtdEquiv D b := by
  apply Zsqrtd.ext
  · simp [pairZsqrtdEquiv, pairMul]
    ring
  · simp [pairZsqrtdEquiv, pairMul]

theorem pairZsqrtd_conj (D : Nat) (a : Int × Int) :
    pairZsqrtdEquiv D (pairConj a) = star (pairZsqrtdEquiv D a) := by
  apply Zsqrtd.ext <;> simp [pairZsqrtdEquiv, pairConj]

theorem pairZsqrtd_scale (D : Nat) (c : Int) (a : Int × Int) :
    pairZsqrtdEquiv D (pairScale c a) =
      (c : Zsqrtd (-(D : Int))) * pairZsqrtdEquiv D a := by
  apply Zsqrtd.ext <;> simp [pairZsqrtdEquiv, pairScale]

theorem pairZsqrtd_pow (D : Nat) (a : Int × Int) (n : Nat) :
    pairZsqrtdEquiv D (pairPow D a n) = (pairZsqrtdEquiv D a) ^ n := by
  induction n with
  | zero => rfl
  | succ n ih => rw [pairPow, pairZsqrtd_mul, ih, pow_succ]

theorem pairZsqrtd_norm (D : Nat) (a : Int × Int) :
    Zsqrtd.norm (pairZsqrtdEquiv D a) =
      a.1 * a.1 + (D : Int) * a.2 * a.2 := by
  simp [Zsqrtd.norm, pairZsqrtdEquiv]

/-- The existing integer pairing is twice the real coordinate of the
quadratic-order product with conjugation. -/
theorem integerPairTrace_eq_zsqrtd_re (D : Nat) (a b : Int × Int) :
    integerPairTrace D a b =
      2 * ((pairZsqrtdEquiv D a * star (pairZsqrtdEquiv D b)).re) := by
  simp [integerPairTrace, pairZsqrtdEquiv]

end TenthDiscriminant
