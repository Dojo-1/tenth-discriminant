import Mathlib

/-!
Phase310 — an exact symbolic split-conjugate trace identity.

For a quadratic maximal order O=Z[omega], omega²-omega+m=0,
a simple split residue prime has roots r and 1-r. The original
Hermitian trace of (a+b omega)*(c+d conjugate(omega)) reduces to
the *cross-pairing* of the two embeddings, not the same-side
Euclidean pairing.

This kernel-checks ONLY the universal commutative-ring polynomial
identity, NOT the full original 100×1052 source/observation claims,
Picard classes or a tenth-discriminant field theorem.
-/

namespace TenthDiscriminant.Phase310

variable {F : Type*} [CommRing F]

def traceForm (m a b c d : F) : F :=
  2*a*c + a*d + b*c + 2*m*b*d

def conjugateCross (r a b c d : F) : F :=
  (a+b*r)*(c+d*(1-r)) + (a+b*(1-r))*(c+d*r)

theorem traceForm_eq_cross_at_root
    (m r a b c d : F)
    (hroot : r*r-r+m=0) :
    traceForm m a b c d = conjugateCross r a b c d := by
  have hm : r*(1-r)=m := by
    linear_combination -hroot
  unfold traceForm conjugateCross
  calc
    2*a*c + a*d + b*c + 2*m*b*d =
      2*a*c + a*d + b*c + 2*(r*(1-r))*b*d := by rw [hm]
    _ = (a+b*r)*(c+d*(1-r)) + (a+b*(1-r))*(c+d*r) := by ring

end TenthDiscriminant.Phase310
