import TenthDiscriminant.BinaryNullHorizontalBasisMatrix
import TenthDiscriminant.BinaryNullRowAction

/-!
# Phase323-B: horizontal basis acts on the original ordinary-Z jets

The second monomial coordinate is the conjugate of the sample. The
horizontal matrix therefore contributes a coefficient factor
(star z)^4-(star z)^2, which is independent of the differentiated Z.
The proof keeps the original pair samples and ordinary derivative rows.
-/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false

/-- Total column of the u-th active horizontal binomial term. -/
def binaryNullHorizontalTargetFin (R S : Nat)
    (i : Fin (R*S)) (u : Nat) : Fin (R*S) :=
  ⟨binaryNullHorizontalTarget S (i.val/S) (i.val%S)
      (min u (binaryNullHorizontalExponent R S i)),
    binaryNullHorizontalTarget_in_range R S i _
      (min_le_right _ _)⟩

/-- On an active term, quotient and remainder recover the exact
horizontal monomial label. -/
theorem binaryNullHorizontalTargetFin_labels (R S : Nat)
    (i : Fin (R*S)) (u : Nat)
    (hu : u ≤ binaryNullHorizontalExponent R S i) :
    (binaryNullHorizontalTargetFin R S i u).val / S = i.val/S ∧
    (binaryNullHorizontalTargetFin R S i u).val % S = i.val%S-2*u := by
  have hS : 0 < S := by
    by_contra hn
    have hz : S = 0 := by omega
    have hi := i.isLt
    simp [hz] at hi
  have hs : i.val%S < S := Nat.mod_lt _ hS
  have hfour : 4*u ≤ i.val%S := by
    dsimp [binaryNullHorizontalExponent] at hu
    omega
  have hsmall : i.val%S-2*u < S := by omega
  simp only [binaryNullHorizontalTargetFin, min_eq_left hu,
    binaryNullHorizontalTarget]
  constructor
  · rw [Nat.mul_add_div hS]
    simp [Nat.div_eq_of_lt hsmall]
  · exact Nat.mul_add_mod_of_lt hsmall

/-- The horizontal matrix acts by its guarded binomial row sum on
arbitrary abelian-group-valued columns. -/
theorem binaryNullHorizontalBasisMatrix_row_action
    {A : Type*} [AddCommGroup A]
    (R S : Nat) (i : Fin (R*S)) (f : Fin (R*S) → A) :
    ∑ h : Fin (R*S),
      (binaryNullHorizontalBasisMatrix R S i h) • f h =
    ∑ u ∈ Finset.range (binaryNullHorizontalExponent R S i+1),
      ((-1 : Int)^u *
        (binaryNullHorizontalExponent R S i).choose u : Int) •
        f (binaryNullHorizontalTargetFin R S i u) := by
  classical
  unfold binaryNullHorizontalBasisMatrix
  simp_rw [Finset.sum_smul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro u hu
  have hubound : u ≤ binaryNullHorizontalExponent R S i := by
    have h := Finset.mem_range.mp hu
    omega
  let target : Fin (R*S) :=
    ⟨binaryNullHorizontalTarget S (i.val/S) (i.val%S) u,
      binaryNullHorizontalTarget_in_range R S i u hubound⟩
  have htest (h : Fin (R*S)) :
      (h.val = binaryNullHorizontalTarget S (i.val/S) (i.val%S) u) ↔
        h = target := by
    constructor
    · intro heq
      exact Fin.ext heq
    · intro heq
      exact congrArg Fin.val heq
  simp_rw [htest]
  have hfin : binaryNullHorizontalTargetFin R S i u = target := by
    apply Fin.ext
    simp [binaryNullHorizontalTargetFin, target, min_eq_left hubound]
  simp [hfin, target]

/-- The scalar binomial identity for the horizontal null polynomial.
It is the existing source polynomial identity evaluated at the
conjugate sample; no new polynomial convention is introduced. -/
private theorem binaryNullHorizontal_binomial_identity
    {A : Type*} [CommRing A]
    (w : A) (s ell : Nat) (hell : 4*ell ≤ s) :
    (∑ u ∈ Finset.range (ell+1),
      (((-1 : Int)^u * (ell.choose u : Int) : Int) : A) *
        w^(s-2*u)) =
      w^(s-4*ell)*(w^4-w^2)^ell := by
  have hpoly := binaryNull_binomial_polynomial w s 0 ell hell
  have heval := congrArg (Polynomial.eval w) hpoly
  simpa [eval_C, zsmul_eq_mul] using heval.symm

/-- The horizontal matrix acting on the actual integer derivative rows
is exactly multiplication by the conjugate-coordinate null factor. -/
theorem binaryNullHorizontalBasisMatrix_integerDerivativeRow_action
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    let z := pairZsqrtdEquiv D a
    let r := i.val/S
    let s := i.val%S
    let ell := binaryNullHorizontalExponent R S i
    ∑ h : Fin (R*S),
      (binaryNullHorizontalBasisMatrix R S i h) •
        pairZsqrtdEquiv D
          (integerDerivativeRow D (h.val/S) (h.val%S) j a) =
      (star z)^(s-4*ell) *
        ((star z)^4-(star z)^2)^ell *
        (derivative^[j] (X^r :
          (Zsqrtd (-(D : Int)))[X])).eval z := by
  classical
  dsimp
  let w : Zsqrtd (-(D : Int)) := star (pairZsqrtdEquiv D a)
  let B : Zsqrtd (-(D : Int)) :=
    (derivative^[j] (X^(i.val/S) :
      (Zsqrtd (-(D : Int)))[X])).eval (pairZsqrtdEquiv D a)
  have hbound :
      4*binaryNullHorizontalExponent R S i ≤ i.val%S := by
    dsimp [binaryNullHorizontalExponent]
    omega
  have hjet (v : Nat) :
      (derivative^[j] (X^(i.val/S) * C w^v)).eval
        (pairZsqrtdEquiv D a) = w^v * B := by
    rw [mul_comm, iterate_derivative_C_mul]
    simp only [eval_mul, eval_C, eval_pow]
  calc
    _ =
      ∑ u ∈ Finset.range (binaryNullHorizontalExponent R S i+1),
        ((-1 : Int)^u *
          (binaryNullHorizontalExponent R S i).choose u : Int) •
          (w^(i.val%S-2*u) * B) := by
        rw [binaryNullHorizontalBasisMatrix_row_action]
        apply Finset.sum_congr rfl
        intro u hu
        have hubound :
            u ≤ binaryNullHorizontalExponent R S i := by
          have h := Finset.mem_range.mp hu
          omega
        have hlab := binaryNullHorizontalTargetFin_labels R S i u hubound
        rw [hlab.1, hlab.2]
        rw [integerDerivativeRow_zsqrtd_jet]
        exact hjet _
    _ =
      (∑ u ∈ Finset.range (binaryNullHorizontalExponent R S i+1),
        ((-1 : Int)^u *
          (binaryNullHorizontalExponent R S i).choose u : Int) •
          w^(i.val%S-2*u)) * B := by
        rw [Finset.sum_mul]
        apply Finset.sum_congr rfl
        intro u hu
        rw [zsmul_eq_mul]
        ring
    _ =
      (w^(i.val%S-4*binaryNullHorizontalExponent R S i) *
        (w^4-w^2)^binaryNullHorizontalExponent R S i) * B := by
        rw [← binaryNullHorizontal_binomial_identity w
          (i.val%S) (binaryNullHorizontalExponent R S i) hbound]

/-- Every actual horizontal transformed jet has its full 2^ell factor.
The divisibility comes from the same parity lemma, applied to the
conjugate sample. -/
theorem binaryNullHorizontalBasisMatrix_actualRow_dvd
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    (2 : Zsqrtd (-(D : Int)))^binaryNullHorizontalExponent R S i ∣
      ∑ h : Fin (R*S),
        (binaryNullHorizontalBasisMatrix R S i h) •
          pairZsqrtdEquiv D
            (integerDerivativeRow D (h.val/S) (h.val%S) j a) := by
  rw [binaryNullHorizontalBasisMatrix_integerDerivativeRow_action]
  let z := pairZsqrtdEquiv D a
  let w := star z
  let ell := binaryNullHorizontalExponent R S i
  have hF : (2 : Zsqrtd (-(D : Int))) ∣ w^4-w^2 := by
    have h := binaryNull_value_dvd_zsqrtd D (pairConj a)
    simpa only [pairZsqrtd_conj] using h
  rcases hF with ⟨c, hc⟩
  refine ⟨w^(i.val%S-4*ell) * c^ell *
    (derivative^[j] (X^(i.val/S) :
      (Zsqrtd (-(D : Int)))[X])).eval z, ?_⟩
  rw [hc, mul_pow]
  ring

end TenthDiscriminant

#print axioms TenthDiscriminant.binaryNullHorizontalBasisMatrix_actualRow_dvd
