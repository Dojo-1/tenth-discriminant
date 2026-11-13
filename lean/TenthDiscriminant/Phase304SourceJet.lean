import Mathlib

/-!
Phase304 formal source kernel, not a new class-number-one field theorem.

The integer identity transports the hermitian trace pairing of the
quadratic order with omega^2 = omega - m under
(x,y) |-> (x-y, 2*y), where D=4*m-1.

The two ZMod5 equalities encode the value and first ordinary Z-jet
of (Z^5-W)*Z^k under the F25 conjugation relation W=Z^5.
They concern source evaluation, NOT a field-class-number implication.
-/

namespace TenthDiscriminant.Phase304

theorem trace_conductor_two
    (m x y u v : ℤ) :
    2 * (x - y) * (u - v)
      + (x - y) * (2 * v)
      + (2 * y) * (u - v)
      + (2 * m) * (2 * y) * (2 * v)
      = 2 * x * u + 2 * (4 * m - 1) * y * v := by
  ring

theorem inert_frobenius_value
    (z w : ZMod 5) (hw : w = z ^ 5) (k : ℕ) :
    z ^ (k + 5) - z ^ k * w = 0 := by
  rw [hw, pow_add]
  ring

theorem inert_frobenius_ordinary_jet_one_base
    (z : ZMod 5) :
    (5 : ZMod 5) * z ^ 4 = 0 := by
  norm_num

theorem inert_frobenius_ordinary_jet_one
    (z w : ZMod 5) (hw : w = z ^ 5) (k : ℕ) :
    ((k + 6 : ℕ) : ZMod 5) * z ^ (k + 5)
      - ((k + 1 : ℕ) : ZMod 5) * z ^ k * w = 0 := by
  have hc :
      ((k + 6 : ℕ) : ZMod 5) =
        ((k + 1 : ℕ) : ZMod 5) := by
    have hn : k + 6 = (k + 1) + 5 := by omega
    rw [hn, Nat.cast_add]
    norm_num
  rw [hc, hw, pow_add]
  ring

end TenthDiscriminant.Phase304
