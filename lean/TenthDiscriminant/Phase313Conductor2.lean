import Mathlib

/-!
Phase313-H: exact ORIGINAL suborder/conductor-2 obstruction at D=163.

This module checks a concrete polynomial/integer counterexample:
both omega and (1+omega) lie OUTSIDE Z[sqrt(-163)]=Z+2*O_K
but their product is INSIDE, with norm 1763 = 41*43.

It does NOT formalize class number one, ray class groups, the
900-class conductor50 convolution, or any determinant valuation.
Those remain independent semantic obligations.
-/

namespace TenthDiscriminant.Phase313Conductor2

/-- An integer coordinate pair a+b*omega with omega^2=omega-41. -/
def omegaMul (x y : ℤ × ℤ) : ℤ × ℤ :=
  (x.1 * y.1 - 41 * x.2 * y.2,
   x.1 * y.2 + x.2 * y.1 + x.2 * y.2)

/-- The integral field norm from Q(sqrt(-163)). -/
def omegaNorm (z : ℤ × ℤ) : ℤ :=
  z.1 * z.1 + z.1 * z.2 + 41 * z.2 * z.2

/-- The original integer-order source is the b-even part of O_K. -/
def inOriginalOrder (z : ℤ × ℤ) : Prop :=
  z.2 % 2 = 0

/-- Two elements outside the original order can multiply into it. -/
theorem original_order_projection_not_multiplicatively_closed :
    ¬ inOriginalOrder (0, 1) ∧
    ¬ inOriginalOrder (1, 1) ∧
    inOriginalOrder (omegaMul (0, 1) (1, 1)) := by
  norm_num [inOriginalOrder, omegaMul]

/-- The exact signed product: omega*(1+omega)=2*omega-41. -/
theorem concrete_product :
    omegaMul (0, 1) (1, 1) = (-41, 2) := by
  norm_num [omegaMul]

/-- The two factor norms and the product norm. -/
theorem concrete_norms :
    omegaNorm (0, 1) = 41 ∧
    omegaNorm (1, 1) = 43 ∧
    omegaNorm (omegaMul (0, 1) (1, 1)) = 1763 ∧
    (41 : ℤ) * 43 = 1763 := by
  norm_num [omegaNorm, omegaMul]

/-- For any integer x,y, the identity x+y sqrt(-163) is represented
by (x-y)+2y omega in the maximal order. -/
theorem original_integer_to_omega (x y : ℤ) :
    inOriginalOrder (x-y, 2*y) := by
  simp [inOriginalOrder]

end TenthDiscriminant.Phase313Conductor2
