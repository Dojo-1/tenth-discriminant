import TenthDiscriminant.BinaryNullHorizontalRowAction
import TenthDiscriminant.BinaryNullBidirectionalBasisMatrix
import TenthDiscriminant.BinaryNullFourSourceJets

/-!
# Phase331 — bidirectional original-source binary polynomial bridge

This file constructs the *polynomial-level* action before asserting
any new determinant divisibility. It must preserve every original
ordinary-Z derivative row, the conjugate W coefficient, and the
integer R-by-S monomial rectangle.

The separately proved vertical and horizontal Gram divisors cannot
be multiplied to get an increased binary valuation. The only valid
route to the claimed exponent is a single combined row action with
a *simultaneous* null-polynomial factor.
-/
namespace TenthDiscriminant
open Polynomial
open scoped BigOperators
set_option autoImplicit false

/-- Actual horizontal integer basis acts on ORIGINAL polynomial
monomials with the conjugate-coordinate null factor, not a substitute
derivative in W. This holds in every commutative coefficient ring. -/
theorem binaryNullHorizontalBasisMatrix_polynomial_action
    {A : Type*} [CommRing A]
    (R S : Nat) (i : Fin (R*S)) (w : A) :
    (∑ h : Fin (R*S),
       (binaryNullHorizontalBasisMatrix R S i h) •
       (X^(h.val/S) * C w^(h.val%S) : A[X])) =
    X^(i.val/S) *
      C (w^(i.val%S - 4*binaryNullHorizontalExponent R S i) *
         (w^4-w^2)^binaryNullHorizontalExponent R S i) := by
  classical
  let ell := binaryNullHorizontalExponent R S i
  let r := i.val/S
  let s := i.val%S
  have he : 4*ell ≤ s := by
    dsimp [ell, s, binaryNullHorizontalExponent]
    omega
  rw [binaryNullHorizontalBasisMatrix_row_action]
  have hlabel :
      (∑ u ∈ Finset.range (ell+1),
        ((-1 : Int)^u * (ell.choose u : Int)) •
          (X^((binaryNullHorizontalTargetFin R S i u).val/S) *
           C w^((binaryNullHorizontalTargetFin R S i u).val%S)
             : A[X])) =
      (∑ u ∈ Finset.range (ell+1),
        ((-1 : Int)^u * (ell.choose u : Int)) •
          (X^r * C w^(s-2*u) : A[X])) := by
    apply Finset.sum_congr rfl
    intro u hu
    have hu : u ≤ ell := by
      have := Finset.mem_range.mp hu
      omega
    obtain ⟨hr,hs⟩ :=
      binaryNullHorizontalTargetFin_labels R S i u
        (by simpa only [ell] using hu)
    simp only [hr,hs,r,s]
  change (∑ u ∈ Finset.range (ell+1),
    ((-1 : Int)^u * (ell.choose u : Int)) •
      (X^((binaryNullHorizontalTargetFin R S i u).val/S) *
       C w^((binaryNullHorizontalTargetFin R S i u).val%S) : A[X])) =
    X^r * C (w^(s-4*ell)*(w^4-w^2)^ell)
  rw [hlabel]
  calc
    _ = X^r * (∑ u ∈ Finset.range (ell+1),
          ((-1 : Int)^u * (ell.choose u : Int)) •
            (C w)^(s-2*u)) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro u hu
      simp only [map_pow, zsmul_eq_mul]
      ring
    _ = X^r *
          ((C w)^(s-4*ell) *
            ((C w)^4-(C w)^2)^ell) := by
      congr 1
      simpa only [zsmul_eq_mul] using
        (binaryNullHorizontal_binomial_identity (A := A[X])
          (C w) s ell he)
    _ = _ := by simp [map_pow, map_mul, map_sub]

/-- The vertical null basis acts on a polynomial family with a fixed
arbitrary coefficient, so the horizontal factor can be pulled through
the vertical row action without any division by W or 2. -/
theorem binaryNullBasisMatrix_polynomial_with_constant
    {A : Type*} [CommRing A]
    (R S : Nat) (i : Fin (R*S)) (c : A) :
    (∑ h : Fin (R*S),
       (binaryNullBasisMatrix R S i h) •
       (X^(h.val/S) * C c : A[X])) =
      (X^(i.val/S-4*binaryNullBasisExponent R S i) *
       (X^4-X^2)^binaryNullBasisExponent R S i) * C c := by
  classical
  have hunit :=
    binaryNullBasisMatrix_polynomial_action R S i (1 : A)
  have hbare :
      (∑ h : Fin (R*S),
       (binaryNullBasisMatrix R S i h) •
          (X^(h.val/S) : A[X])) =
      X^(i.val/S-4*binaryNullBasisExponent R S i) *
       (X^4-X^2)^binaryNullBasisExponent R S i := by
    simpa only [one_pow, map_one, mul_one, one_mul] using hunit
  calc
    _ = (∑ h : Fin (R*S),
          (binaryNullBasisMatrix R S i h) •
            (X^(h.val/S) : A[X])) * C c := by
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro h hh
      simp only [zsmul_eq_mul]
      ring
    _ = _ := by rw [hbare]

end TenthDiscriminant

#print axioms TenthDiscriminant.binaryNullHorizontalBasisMatrix_polynomial_action
#print axioms TenthDiscriminant.binaryNullBasisMatrix_polynomial_with_constant
