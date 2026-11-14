import Mathlib

/-!
# Phase313: algebraic kernel for tame/wild principal units and sign parity

These are universally valid polynomial identities in a commutative ring,
and are kernel-checked by Lean. They supply the numerator and
principal-unit congruence skeleton for the normalized inert-5 Fermat
quotient and the original sign-paired Gram.

They DO NOT formalize:
* the unit group isomorphism O/25 ≃ C24 × C5²;
* ray class groups or h(K)=1;
* invertibility of the conjugate in F25, nor its quotient;
* the source-specific 40×40/100×100 Gram or any determinant valuation;
* the proposed extra tenth-discriminant theorem.
-/

namespace TenthDiscriminant.Phase313

variable {R : Type*} [CommRing R]

/-- Principal units 1+5u multiply additively to first order modulo25. -/
theorem principal_unit_product (u v : R) :
    (1 + 5*u) * (1 + 5*v) =
      1 + 5*(u+v) + 25*u*v := by
  ring

/-- The fifth power of 1+5u is congruent to 1 modulo25. The exact
integer-polynomial remainder is retained, not silently discarded. -/
theorem principal_unit_fifth_power (u : R) :
    (1+5*u)^5 =
      1+25*(u+10*u^2+50*u^3+125*u^4+125*u^5) := by
  ring

/-- If two Frobenius lifts are a+5e and b+5f, the product
defect is a twisted Leibniz term up to a multiple of25. -/
theorem two_Frobenius_lifts_product_defect (a b e f : R) :
    (a+5*e)*(b+5*f)-a*b =
      5*(e*b+a*f)+25*e*f := by
  ring

/-- Opposite sign-parity row pairings cancel on a sign-closed source. -/
theorem opposite_sign_pairing_cancel (x y : R) :
    x*y+(-x)*y=0 := by
  ring

/-- Equal sign-parity row pairings reinforce, giving twice the term. -/
theorem equal_sign_pairing_double (x y : R) :
    x*y+(-x)*(-y)=2*x*y := by
  ring

end TenthDiscriminant.Phase313
