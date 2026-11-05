import TenthDiscriminant.InertFrobenius

/-!
# Phase223: source-coordinate Frobenius horizontal relation

The Frobenius input is the existing integer-pair / quadratic residue
bridge, not an auxiliary quadratic extension. This is the exact
quadratic factor underlying the finite-band annihilator. It is only the
local factor, not yet the full product over ellipse support.
-/

namespace TenthDiscriminant.Phase223

/-- For the original quadratic residue coordinates the p-power map
conjugates the imaginary coordinate under the exact inert guard. -/
theorem residue_frobenius_conj
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : QuadraticResidue D p) :
    a ^ p = ⟨a.re, -a.im⟩ := by
  have h := residuePair_pow_conj_of_nonsquare D p hp2 hnonsquare
    (a.re, a.im)
  calc
    a ^ p = (QuadraticResidue.ofPair D p (a.re, a.im)) ^ p := rfl
    _ = QuadraticResidue.ofPair D p
        (residuePairPow D p (a.re, a.im) p) :=
      (QuadraticResidue.ofPair_pow D p (a.re, a.im) p).symm
    _ = QuadraticResidue.ofPair D p
        (residuePairConj (a.re, a.im)) := congrArg (QuadraticResidue.ofPair D p) h
    _ = ⟨a.re, -a.im⟩ := rfl

/-- The exact horizontal quadratic factor, independent of coordinates
chosen to present the integer sample. For a conjugate sample with
imaginary integer coefficient y, this is the b=|y| band factor. -/
theorem residue_horizontal_quadratic_factor
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : QuadraticResidue D p) :
    (a ^ p - a) ^ 2 +
      QuadraticResidue.scalar D p (4 * (D : ZMod p) * a.im ^ 2) = 0 := by
  rw [residue_frobenius_conj D p hp2 hnonsquare a]
  apply QuadraticResidue.ext
  · simp [QuadraticResidue.scalar, sub_eq_add_neg, pow_two]
    ring
  · simp [QuadraticResidue.scalar, sub_eq_add_neg, pow_two]

end TenthDiscriminant.Phase223

#print axioms TenthDiscriminant.Phase223.residue_frobenius_conj
#print axioms TenthDiscriminant.Phase223.residue_horizontal_quadratic_factor
