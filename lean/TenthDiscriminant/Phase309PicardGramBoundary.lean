import Mathlib

/-!
Phase309: the ORIGINAL 2-source/3-observation restricted trace Gram has
a determinant that remains a *unit* at a simple split prime, even though the
O_K-linear maximal-minor ideal may represent a nontrivial Picard class.

This is an isolated polynomial reduction theorem in a residue field.
It does NOT construct a quadratic order, a Dedekind ideal, the original
full 100-row evaluation, or a number-field class-number-one proof.
The external semantic bridge is checked by Phase309 exact original-source
Python/CI controls and is a separate obligation.
-/

namespace TenthDiscriminant.Phase309

variable {F : Type*} [Field F]

/-- f(r) for the quadratic integer-ring relation omega²-omega+m=0. -/
def quadraticRelation (m r : F) : F := r*r-r+m

/--
The ordinary original integer trace Gram of rows (1,Z), restricted to
observations (0,p,omega-r), is

  [[6, 2p+1-2r], [2p+1-2r, 2(p²+f(r))]].

This is its determinant polynomial, before reduction modulo p.
-/
def restrictedTraceGramDet (p m r : F) : F :=
  6*(2*(p*p+quadraticRelation m r)) - (2*p+1-2*r)^2

/--
At a root of the quadratic integer-ring relation in a residue field,
the reduced Gram determinant equals the negative square of f'(r).
-/
theorem restrictedTraceGramDet_at_split_root
    (m r : F) (hroot : quadraticRelation m r = 0) :
    restrictedTraceGramDet (0 : F) m r = -((1-2*r)^2) := by
  simp [restrictedTraceGramDet, hroot]

/--
For a *simple* residue-field root, the reduced determinant is a unit.
Hence the restricted original trace Gram need NOT carry p-adic determinant
mass even when the original O-linear maximal-minor ideal is nonprincipal.
The latter ideal statement is an independent arithmetic premise, NOT
derived in this theorem.
-/
theorem restrictedTraceGramDet_unit_at_split_root
    (m r : F)
    (hroot : quadraticRelation m r = 0)
    (hsimple : 2*r-1 ≠ 0) :
    restrictedTraceGramDet (0 : F) m r ≠ 0 := by
  have hnonzero : (1:F)-2*r ≠ 0 := by
    intro h
    apply hsimple
    calc
      2*r-1 = -(1-2*r) := by ring
      _ = 0 := by rw [h]; ring
  rw [restrictedTraceGramDet_at_split_root m r hroot]
  simpa using (pow_ne_zero 2 hnonzero)

end TenthDiscriminant.Phase309
