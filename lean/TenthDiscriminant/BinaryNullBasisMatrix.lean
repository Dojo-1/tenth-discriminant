import TenthDiscriminant.RectangularBasisMatrix

/-!
# A unimodular binary null-polynomial row basis

The row indexed by (r,s) is Z^(r-4k) * (Z^4-Z^2)^k * W^s,
where k=floor(r/4). The coefficient at Z^r W^s is one.
All other monomials have lower Z-degree, and the W-degree stays s.

This constructs only the integral row matrix and its determinant.
Divisibility of its actual ordinary jets is a separate, typed theorem.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Number of binary null factors used by the row (r,s). -/
def binaryNullBasisExponent (R S : Nat) (i : Fin (R * S)) : Nat :=
  (i.val / S) / 4

/-- Monomial label produced by t nonleading terms in (Z^4-Z^2)^k. -/
def binaryNullBasisTarget (S r s t : Nat) : Nat :=
  (r - 2*t) * S + s

/-- Integral coefficient matrix of the source-preserving binary basis. -/
def binaryNullBasisMatrix (R S : Nat) :
    Matrix (Fin (R * S)) (Fin (R * S)) Int :=
  fun i j =>
    let k := binaryNullBasisExponent R S i
    (Finset.range (k + 1)).sum fun t =>
      if j.val = binaryNullBasisTarget S (i.val / S) (i.val % S) t
      then (-1 : Int)^t * (k.choose t : Int) else 0

private theorem binaryNullBasisTarget_lt (R S : Nat)
    (i : Fin (R * S)) (t : Nat)
    (ht0 : 0 < t) (ht : t ≤ binaryNullBasisExponent R S i) :
    binaryNullBasisTarget S (i.val / S) (i.val % S) t < i.val := by
  have hS : 0 < S := by
    by_contra hn
    have hz : S = 0 := by omega
    have hi := i.isLt
    simp [hz] at hi
  have ht4 : 4*t ≤ i.val / S := by
    dsimp [binaryNullBasisExponent] at ht
    omega
  have hlt : i.val / S - 2*t < i.val / S := by omega
  have hm : (i.val / S - 2*t)*S < (i.val / S)*S :=
    Nat.mul_lt_mul_of_pos_right hlt hS
  have hindex : (i.val / S)*S + i.val % S = i.val :=
    Nat.div_add_mod' i.val S
  unfold binaryNullBasisTarget
  omega

/-- Every term remains a real column of the original finite rectangle. -/
theorem binaryNullBasisTarget_in_range (R S : Nat)
    (i : Fin (R * S)) (t : Nat)
    (ht : t ≤ binaryNullBasisExponent R S i) :
    binaryNullBasisTarget S (i.val / S) (i.val % S) t < R*S := by
  by_cases ht0 : t = 0
  · subst t
    simp [binaryNullBasisTarget, Nat.div_add_mod', i.isLt]
  · exact (binaryNullBasisTarget_lt R S i t
      (Nat.pos_of_ne_zero ht0) ht).trans i.isLt

/-- Nonleading terms point strictly to earlier row-major columns. -/
theorem binaryNullBasisMatrix_lowerTriangular (R S : Nat) :
    (binaryNullBasisMatrix R S).BlockTriangular
      (OrderDual.toDual : Fin (R * S) → OrderDual (Fin (R * S))) := by
  intro i j hij
  have hij' : i.val < j.val := by simpa using hij
  unfold binaryNullBasisMatrix
  apply Finset.sum_eq_zero
  intro t ht
  by_cases ht0 : t = 0
  · subst t
    have hindex : (i.val / S)*S + i.val % S = i.val :=
      Nat.div_add_mod' i.val S
    simp [binaryNullBasisTarget, hindex, ne_of_gt hij']
  · have htk : t ≤ binaryNullBasisExponent R S i := by
      have h := Finset.mem_range.mp ht
      omega
    have hlt := binaryNullBasisTarget_lt R S i t
      (Nat.pos_of_ne_zero ht0) htk
    have hne : j.val ≠ binaryNullBasisTarget S (i.val / S) (i.val % S) t :=
      ne_of_gt (hlt.trans hij')
    simp [hne]

/-- Every diagonal coefficient of the explicit matrix is exactly one. -/
theorem binaryNullBasisMatrix_diag (R S : Nat) (i : Fin (R*S)) :
    binaryNullBasisMatrix R S i i = 1 := by
  unfold binaryNullBasisMatrix
  rw [Finset.sum_eq_single 0]
  · have hindex : (i.val / S)*S + i.val % S = i.val :=
      Nat.div_add_mod' i.val S
    simp [binaryNullBasisTarget, hindex]
  · intro t ht ht0
    have htk : t ≤ binaryNullBasisExponent R S i := by
      have h := Finset.mem_range.mp ht
      omega
    have hlt := binaryNullBasisTarget_lt R S i t
      (Nat.pos_of_ne_zero ht0) htk
    simp [ne_of_gt hlt]
  · simp

/-- The original integer monomial lattice is unchanged: det U=1. -/
theorem binaryNullBasisMatrix_det (R S : Nat) :
    (binaryNullBasisMatrix R S).det = 1 := by
  rw [Matrix.det_of_lowerTriangular _
    (binaryNullBasisMatrix_lowerTriangular R S)]
  simp [binaryNullBasisMatrix_diag R S]

/-- The first nontrivial row is Z^4 - Z^2 at r=4,s=0,S=2. -/
theorem binaryNullBasisMatrix_pilot :
    binaryNullBasisMatrix 5 2 8 8 = 1 ∧
    binaryNullBasisMatrix 5 2 8 4 = -1 := by
  decide

end TenthDiscriminant
