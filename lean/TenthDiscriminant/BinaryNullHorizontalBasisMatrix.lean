import TenthDiscriminant.BinaryNullBasisMatrix

/-!
# Phase323-A: horizontal binary-null basis on the original rectangle

This is the conjugate-coordinate companion to BinaryNullBasisMatrix.
It acts on the second monomial label while preserving the first label.
The row indexed by (r,s) is

  Z^r W^(s-4*l) (W^4-W^2)^l,  l=floor(s/4).

Every active term remains in the original R-by-S rectangle. Nonleading
terms strictly lower the row-major index, and the diagonal is one.
This file proves only the horizontal integer basis and its determinant;
the actual-jet and Gram-divisibility bridge is a separate module.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Number of conjugate-coordinate null factors in row i=(r,s). -/
def binaryNullHorizontalExponent (R S : Nat) (i : Fin (R*S)) : Nat :=
  (i.val % S) / 4

/-- Row-major target of the u-th nonleading term of (W^4-W^2)^ell. -/
def binaryNullHorizontalTarget (S r s u : Nat) : Nat :=
  r*S + (s - 2*u)

/-- Integral coefficient matrix for the horizontal binary-null basis. -/
def binaryNullHorizontalBasisMatrix (R S : Nat) :
    Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  fun i j =>
    let ell := binaryNullHorizontalExponent R S i
    (Finset.range (ell+1)).sum fun u =>
      if j.val = binaryNullHorizontalTarget S (i.val/S) (i.val%S) u
      then (-1 : Int)^u * (ell.choose u : Int) else 0

private theorem binaryNullHorizontalTarget_lt (R S : Nat)
    (i : Fin (R*S)) (u : Nat)
    (hu0 : 0 < u)
    (hu : u ≤ binaryNullHorizontalExponent R S i) :
    binaryNullHorizontalTarget S (i.val/S) (i.val%S) u < i.val := by
  have hS : 0 < S := by
    by_contra hn
    have hz : S = 0 := by omega
    have hi := i.isLt
    simp [hz] at hi
  have hfour : 4*u ≤ i.val%S := by
    dsimp [binaryNullHorizontalExponent] at hu
    omega
  have hindex : (i.val/S)*S + i.val%S = i.val :=
    Nat.div_add_mod' i.val S
  unfold binaryNullHorizontalTarget
  omega

/-- Every active horizontal term is an actual column of the original
finite rectangle; no truncation or new monomial label is introduced. -/
theorem binaryNullHorizontalTarget_in_range (R S : Nat)
    (i : Fin (R*S)) (u : Nat)
    (hu : u ≤ binaryNullHorizontalExponent R S i) :
    binaryNullHorizontalTarget S (i.val/S) (i.val%S) u < R*S := by
  by_cases hu0 : u = 0
  · subst u
    simp [binaryNullHorizontalTarget, Nat.div_add_mod', i.isLt]
  · exact (binaryNullHorizontalTarget_lt R S i u
      (Nat.pos_of_ne_zero hu0) hu).trans i.isLt

/-- Nonleading horizontal terms point strictly to earlier row-major
columns. -/
theorem binaryNullHorizontalBasisMatrix_lowerTriangular (R S : Nat) :
    (binaryNullHorizontalBasisMatrix R S).BlockTriangular
      (OrderDual.toDual : Fin (R*S) → OrderDual (Fin (R*S))) := by
  intro i j hij
  have hij' : i.val < j.val := by simpa using hij
  unfold binaryNullHorizontalBasisMatrix
  apply Finset.sum_eq_zero
  intro u hu
  by_cases hu0 : u = 0
  · subst u
    have hindex : (i.val/S)*S + i.val%S = i.val :=
      Nat.div_add_mod' i.val S
    simp [binaryNullHorizontalTarget, hindex, ne_of_gt hij']
  · have hubound : u ≤ binaryNullHorizontalExponent R S i := by
      have h := Finset.mem_range.mp hu
      omega
    have hlt := binaryNullHorizontalTarget_lt R S i u
      (Nat.pos_of_ne_zero hu0) hubound
    have hne : j.val ≠ binaryNullHorizontalTarget S (i.val/S) (i.val%S) u :=
      ne_of_gt (hlt.trans hij')
    simp [hne]

/-- Every diagonal coefficient is exactly one. -/
theorem binaryNullHorizontalBasisMatrix_diag (R S : Nat)
    (i : Fin (R*S)) :
    binaryNullHorizontalBasisMatrix R S i i = 1 := by
  unfold binaryNullHorizontalBasisMatrix
  rw [Finset.sum_eq_single 0]
  · have hindex : (i.val/S)*S + i.val%S = i.val :=
      Nat.div_add_mod' i.val S
    simp [binaryNullHorizontalTarget, hindex]
  · intro u hu hu0
    have hubound : u ≤ binaryNullHorizontalExponent R S i := by
      have h := Finset.mem_range.mp hu
      omega
    have hlt := binaryNullHorizontalTarget_lt R S i u
      (Nat.pos_of_ne_zero hu0) hubound
    simp [ne_of_gt hlt]
  · simp

/-- The horizontal change of basis is unimodular, including empty
rectangles. -/
theorem binaryNullHorizontalBasisMatrix_det (R S : Nat) :
    (binaryNullHorizontalBasisMatrix R S).det = 1 := by
  rw [Matrix.det_of_lowerTriangular _
    (binaryNullHorizontalBasisMatrix_lowerTriangular R S)]
  simp [binaryNullHorizontalBasisMatrix_diag]

/-- First nontrivial horizontal row: W^4-W^2 in the original columns. -/
theorem binaryNullHorizontalBasisMatrix_pilot :
    binaryNullHorizontalBasisMatrix 2 5 4 4 = 1 ∧
    binaryNullHorizontalBasisMatrix 2 5 4 2 = -1 := by
  decide

end TenthDiscriminant

#print axioms TenthDiscriminant.binaryNullHorizontalBasisMatrix_det
