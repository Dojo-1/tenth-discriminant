import Mathlib

/-!
# Phase315: second p-adic wild-log correction at conductor 125

For the normalized quadratic Frobenius defect, multiplication
has the twisted law d(xy)=d(x)+d(y)+5*d(x)*d(y) modulo25.
The correction L(d)=d-15*d^2 is additive modulo25.

This file proves the exact Z-polynomial remainder before reducing
to ZMod 25, which prevents a hidden cancellation assumption.

This does NOT formalize O_K, F25 Frobenius/conjugation, the ray125
unit group, its global class group, the Lean original 40-row source,
or any determinant valuation. Those are separate obligations.
-/

namespace TenthDiscriminant.Phase315

variable {R : Type*} [CommRing R]

def twistedDefectProduct (a b : R) : R :=
  a+b+5*a*b

def correctedWildLog (x : R) : R :=
  x-15*x^2

/-- The exact integer-coefficient correction, before reducing mod25. -/
theorem correctedWildLog_exact_remainder (a b : R) :
    correctedWildLog (twistedDefectProduct a b) =
      correctedWildLog a + correctedWildLog b
        - 25*(a*b + 6*a^2*b + 6*a*b^2 + 15*a^2*b^2) := by
  unfold correctedWildLog twistedDefectProduct
  ring

/-- Since the exact remainder is 25 times a polynomial, the
corrected second-depth wild coordinate is additive mod25. -/
theorem correctedWildLog_additive_mod25 (a b : ZMod 25) :
    correctedWildLog (twistedDefectProduct a b) =
      correctedWildLog a + correctedWildLog b := by
  rw [correctedWildLog_exact_remainder]
  norm_num

end TenthDiscriminant.Phase315
