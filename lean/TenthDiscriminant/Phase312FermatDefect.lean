import Mathlib

/-!
Phase312: universal polynomial identities underlying the inert-5
conjugate Fermat quotient epsilon(x)=(x^5-conj(x))/5.

These are exact identities in ANY commutative ring. The program-level
claim that this quotient is integral in an inert quadratic order, its
mod5 F25 semantics, the original 100-row source and class groups are
all separate statements, NOT proven by this file.
-/

namespace TenthDiscriminant.Phase312

variable {R : Type*} [CommRing R]

/-- The multiplicative defect of a fifth-power map relative to two
chosen conjugates. After division by 5 and Frobenius reduction, this
produces the twisted Leibniz rule used by the Phase312 experiment. -/
theorem fifth_defect_product
    (x y cx cy : R) :
    (x*y)^5 - cx*cy =
      (x^5-cx)*y^5 + cx*(y^5-cy) := by
  ring

/-- The additive fifth-power defect has nontrivial cross terms.
This prevents confusing the quadratic Fermat quotient with an
ordinary additive derivation. -/
theorem fifth_defect_sum
    (x y cx cy : R) :
    (x+y)^5 - (cx+cy) =
      (x^5-cx)+(y^5-cy)+
        5*(x^4*y+2*x^3*y^2+2*x^2*y^3+x*y^4) := by
  ring

/-- The actual higher Hermite source word becomes a square on the
Frobenius graph W=Z^5; differentiated jets with W held fixed are
a distinct obligation. -/
theorem hermite_restriction_square (z : R) (a : ℕ) :
    z^(45+a)*z^5 - 2*z^(26+a) + z^(2+a)
      = z^a*(z^25-z)^2 := by
  rw [pow_add, pow_add, pow_add]
  ring

end TenthDiscriminant.Phase312
