import Mathlib

/-!
# Phase317: exact norm-(D+1) nonrational integer generator fibre

Put D=4m-1 with m>=2, and consider original integer-order
norm N(x+y*sqrt(-D))=x*x + D*y*y.
If N=D+1=4m and y !=0, then x*x=y*y=1.
Thus the only nonrational integer solutions are (±1,±1).

When m is a square, two ADDITIONAL rational solutions are
x=±2*sqrt(m), y=0. These are directly constructed below.

This module neither asserts that m is prime from class number one,
nor formalizes ideal class groups, ray classes, Gram matrices or
any uniform determinant bound. Those are separate bridge obligations.
-/

namespace TenthDiscriminant.Phase317

def originalNorm (m x y : ℤ) : ℤ :=
  x*x + (4*m-1)*y*y

theorem four_nonscalar_witnesses (m : ℤ) :
    originalNorm m 1 1 = 4*m ∧
    originalNorm m (-1) 1 = 4*m ∧
    originalNorm m 1 (-1) = 4*m ∧
    originalNorm m (-1) (-1) = 4*m := by
  simp [originalNorm]
  ring

/-- An arbitrary nonrational solution at norm 4m has x²=y²=1. -/
theorem nonrational_norm_four_m_exact
    (m x y : ℤ) (hm : 2 ≤ m)
    (hy : y ≠ 0)
    (h : originalNorm m x y = 4*m) :
    x*x=1 ∧ y*y=1 := by
  unfold originalNorm at h
  have hD : 0 ≤ 4*m-1 := by omega
  have hx2 : 0 ≤ x*x := mul_self_nonneg x
  have hylo : -1 ≤ y := by
    by_contra hn
    have hneg : y ≤ -2 := by omega
    have hge4 : 4 ≤ y*y := by
      nlinarith [mul_nonneg (by omega : 0 ≤ -y-2)
        (by omega : 0 ≤ -y+2)]
    have hprod : 0 ≤ (4*m-1)*(y*y-4) :=
      mul_nonneg hD (by omega)
    nlinarith
  have hyhi : y ≤ 1 := by
    by_contra hn
    have hpos : 2 ≤ y := by omega
    have hge4 : 4 ≤ y*y := by
      nlinarith [mul_nonneg (by omega : 0 ≤ y-2)
        (by omega : 0 ≤ y+2)]
    have hprod : 0 ≤ (4*m-1)*(y*y-4) :=
      mul_nonneg hD (by omega)
    nlinarith
  have hcase : y=-1 ∨ y=0 ∨ y=1 := by omega
  have hy2 : y*y=1 := by
    rcases hcase with hneg | hzero | hpos
    · rw [hneg]; norm_num
    · exact False.elim (hy hzero)
    · rw [hpos]; norm_num
  constructor
  · nlinarith [h,hy2]
  · exact hy2

/-- A square m yields two extra rational generators, which is why
the no-rational-square hypothesis cannot be omitted in any count. -/
theorem rational_extra_witness (m t : ℤ) (h : t*t=m) :
    originalNorm m (2*t) 0 = 4*m ∧
    originalNorm m (-2*t) 0 = 4*m := by
  constructor <;> simp [originalNorm] <;> nlinarith [h]

end TenthDiscriminant.Phase317
