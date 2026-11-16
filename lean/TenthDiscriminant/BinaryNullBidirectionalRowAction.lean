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


/-- The two real integer basis changes compose to a SINGLE
ordinary-Z polynomial on the original rectangle. Crucially, the
horizontal coefficient depends only on the W exponent, which stays
unchanged under the vertical row change. No division by 2 or W is used. -/
theorem binaryNullBidirectionalBasisMatrix_polynomial_action
    {A : Type*} [CommRing A]
    (R S : Nat) (i : Fin (R*S)) (w : A) :
    (∑ h : Fin (R*S),
       (binaryNullBidirectionalBasisMatrix R S i h) •
         (X^(h.val/S) * C w^(h.val%S) : A[X])) =
      (X^(i.val/S-4*binaryNullBasisExponent R S i) *
       (X^4-X^2)^binaryNullBasisExponent R S i) *
       C (w^(i.val%S - 4*binaryNullHorizontalExponent R S i) *
         (w^4-w^2)^binaryNullHorizontalExponent R S i) := by
  classical
  let c : Fin (R*S) → A := fun h =>
    w^(h.val%S-4*binaryNullHorizontalExponent R S h) *
      (w^4-w^2)^binaryNullHorizontalExponent R S h
  let monom : Fin (R*S) → A[X] := fun h =>
    X^(h.val/S) * C w^(h.val%S)
  have hhorizontal (h : Fin (R*S)) :
      (∑ k : Fin (R*S),
        (binaryNullHorizontalBasisMatrix R S h k) • monom k) =
      X^(h.val/S) * C (c h) := by
    simpa only [monom, c] using
      binaryNullHorizontalBasisMatrix_polynomial_action R S h w
  have hcomposition :
    (∑ h : Fin (R*S),
       (binaryNullBidirectionalBasisMatrix R S i h) • monom h) =
    (∑ t : Fin (R*S),
       (binaryNullBasisMatrix R S i t) •
         (∑ h : Fin (R*S),
             (binaryNullHorizontalBasisMatrix R S t h) • monom h)) := by
    unfold binaryNullBidirectionalBasisMatrix
    calc
      _ = ∑ h : Fin (R*S), ∑ t : Fin (R*S),
          (binaryNullBasisMatrix R S i t) •
            ((binaryNullHorizontalBasisMatrix R S t h) • monom h) := by
          simp only [Matrix.mul_apply, Finset.sum_smul, mul_smul]
      _ = ∑ t : Fin (R*S), ∑ h : Fin (R*S),
          (binaryNullBasisMatrix R S i t) •
            ((binaryNullHorizontalBasisMatrix R S t h) • monom h) := by
          rw [Finset.sum_comm]
      _ = _ := by simp only [Finset.smul_sum]
  have hconstant :
    (∑ t : Fin (R*S),
       (binaryNullBasisMatrix R S i t) •
         (X^(t.val/S) * C (c t))) =
    (∑ t : Fin (R*S),
       (binaryNullBasisMatrix R S i t) •
         (X^(t.val/S) * C (c i))) := by
    rw [binaryNullBasisMatrix_row_action,
      binaryNullBasisMatrix_row_action]
    apply Finset.sum_congr rfl
    intro t ht
    have hbound : t ≤ binaryNullBasisExponent R S i := by
      have := Finset.mem_range.mp ht
      omega
    have hs := (binaryNullBasisTargetFin_labels R S i t hbound).2
    have hc : c (binaryNullBasisTargetFin R S i t) = c i := by
      simp only [c, binaryNullHorizontalExponent, hs]
    rw [hc]
  change (∑ h : Fin (R*S),
      (binaryNullBidirectionalBasisMatrix R S i h) • monom h) =
    (X^(i.val/S-4*binaryNullBasisExponent R S i) *
       (X^4-X^2)^binaryNullBasisExponent R S i) * C (c i)
  calc
    _ = ∑ t : Fin (R*S),
        (binaryNullBasisMatrix R S i t) •
         (∑ h : Fin (R*S),
            (binaryNullHorizontalBasisMatrix R S t h) • monom h) :=
      hcomposition
    _ = ∑ t : Fin (R*S),
        (binaryNullBasisMatrix R S i t) •
          (X^(t.val/S) * C (c t)) := by
        apply Finset.sum_congr rfl
        intro t ht
        rw [hhorizontal]
    _ = ∑ t : Fin (R*S),
        (binaryNullBasisMatrix R S i t) •
          (X^(t.val/S) * C (c i)) := hconstant
    _ = _ := binaryNullBasisMatrix_polynomial_with_constant R S i (c i)


/-- The composite explicit unimodular matrix acts on each ACTUAL
original ordinary-Z derivative row as the derivative of the compact
two-null polynomial. The conjugate W is a fixed coefficient.
Every original observation pair and every j is preserved. -/
theorem binaryNullBidirectionalBasisMatrix_integerDerivativeRow_action
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    let z := pairZsqrtdEquiv D a
    let w := star z
    let k := binaryNullBasisExponent R S i
    let ell := binaryNullHorizontalExponent R S i
    (∑ h : Fin (R*S),
       (binaryNullBidirectionalBasisMatrix R S i h) •
         pairZsqrtdEquiv D
           (integerDerivativeRow D (h.val/S) (h.val%S) j a)) =
    (derivative^[j] (
       (X^(i.val/S-4*k) * (X^4-X^2)^k) *
       C (w^(i.val%S-4*ell)*(w^4-w^2)^ell)
         : (Zsqrtd (-(D : Int)))[X])).eval z := by
  dsimp
  have hpoly := binaryNullBidirectionalBasisMatrix_polynomial_action
    R S i (star (pairZsqrtdEquiv D a))
  rw [← hpoly, iterate_derivative_sum, eval_finset_sum]
  apply Finset.sum_congr rfl
  intro h hh
  rw [iterate_derivative_smul, eval_smul]
  congr 1
  exact integerDerivativeRow_zsqrtd_jet D (h.val/S) (h.val%S) j a

/-- This is the TRUE source-specific simultaneous 2^(k+ell) divisor
of one transformed row, not a product of separate determinant claims.
It uses the existing all-orders F(Z) null-jet theorem and the true
W=conj(Z) null-value theorem, without differentiation in W. -/
theorem binaryNullBidirectionalBasisMatrix_actualRow_dvd
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    (2 : Zsqrtd (-(D : Int)))^
      binaryNullBidirectionalExponent R S i ∣
    ∑ h : Fin (R*S),
      (binaryNullBidirectionalBasisMatrix R S i h) •
        pairZsqrtdEquiv D
          (integerDerivativeRow D (h.val/S) (h.val%S) j a) := by
  rw [binaryNullBidirectionalBasisMatrix_integerDerivativeRow_action]
  let z : Zsqrtd (-(D : Int)) := pairZsqrtdEquiv D a
  let w : Zsqrtd (-(D : Int)) := star z
  let r := i.val/S
  let s := i.val%S
  let k := binaryNullBasisExponent R S i
  let ell := binaryNullHorizontalExponent R S i
  let P : (Zsqrtd (-(D : Int)))[X] :=
    X^(r-4*k)*(X^4-X^2)^k
  have hZ : (2 : Zsqrtd (-(D : Int)))^k ∣
       (derivative^[j] P).eval z := by
    exact binaryNull_power_allOrdinaryJets_dvd D a
      (X^(r-4*k)) k j
  have hW : (2 : Zsqrtd (-(D : Int))) ∣ w^4-w^2 := by
    have h := binaryNull_value_dvd_zsqrtd D (pairConj a)
    simpa only [w, z, pairZsqrtd_conj] using h
  rcases hZ with ⟨u,hu⟩
  rcases hW with ⟨v,hv⟩
  have hconst : (derivative^[j]
      (P * C (w^(s-4*ell)*(w^4-w^2)^ell))).eval z =
      w^(s-4*ell)*(w^4-w^2)^ell *
        (derivative^[j] P).eval z := by
    rw [mul_comm, iterate_derivative_C_mul]
    simp [eval_mul, eval_C]
  change (2 : Zsqrtd (-(D : Int)))^(k+ell) ∣
    (derivative^[j] (P * C
      (w^(s-4*ell)*(w^4-w^2)^ell))).eval z
  rw [hconst, hv, mul_pow, hu]
  refine ⟨w^(s-4*ell)*v^ell*u, ?_⟩
  ring

end TenthDiscriminant

#print axioms TenthDiscriminant.binaryNullHorizontalBasisMatrix_polynomial_action
#print axioms TenthDiscriminant.binaryNullBasisMatrix_polynomial_with_constant

#print axioms TenthDiscriminant.binaryNullBidirectionalBasisMatrix_polynomial_action

#print axioms TenthDiscriminant.binaryNullBidirectionalBasisMatrix_integerDerivativeRow_action
#print axioms TenthDiscriminant.binaryNullBidirectionalBasisMatrix_actualRow_dvd
