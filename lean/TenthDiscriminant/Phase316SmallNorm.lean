import Mathlib

/-!
# Phase316: strict small-norm rigidity in the quadratic maximal order

For omega²-omega+m=0, the norm of a+b*omega is
a²+ab+mb² and the discriminant is -(4m-1).

The elementary completed-square identity implies:
if m>=1 and Norm(a+b*omega)<m, then b=0, so the element is
a rational integer and its norm is a².

This is a general quantified norm-form theorem, with NO class-number
assumption. To conclude that every ideal of norm n<m is a rational
square ideal, one separately assumes the field's ideal class group
is trivial. This module does NOT formalize that ideal-class bridge,
any ray class structure, or the original Gram determinant.
-/

namespace TenthDiscriminant.Phase316

def omegaNorm (m a b : ℤ) : ℤ :=
  a*a+a*b+m*b*b

theorem four_omegaNorm (m a b : ℤ) :
    4*omegaNorm m a b = (2*a+b)^2+(4*m-1)*b^2 := by
  unfold omegaNorm
  ring

/-- Any element with norm below m must be an integer. -/
theorem small_norm_rational
    (m a b : ℤ) (hm : 1 ≤ m)
    (hsmall : omegaNorm m a b < m) : b = 0 := by
  by_contra hb
  have hb2 : 1 ≤ b ^ 2 := by
    have hbne : b ^ 2 ≠ 0 := pow_ne_zero 2 hb
    have hbnn : 0 ≤ b ^ 2 := sq_nonneg b
    omega
  have hdnn : 0 ≤ 4*m-1 := by omega
  have hsqnn : 0 ≤ (2*a+b)^2 := sq_nonneg _
  have hprod : 0 ≤ (4*m-1)*(b^2-1) :=
    mul_nonneg hdnn (by omega)
  have hfour := four_omegaNorm m a b
  have hsmall_int : omegaNorm m a b ≤ m-1 := by omega
  nlinarith

/-- Hence every represented positive n < m is an integer square. -/
theorem small_norm_is_square
    (m a b : ℤ) (hm : 1 ≤ m)
    (hsmall : omegaNorm m a b < m) :
    omegaNorm m a b = a^2 := by
  have hb : b=0 := small_norm_rational m a b hm hsmall
  subst b
  unfold omegaNorm
  ring

end TenthDiscriminant.Phase316
