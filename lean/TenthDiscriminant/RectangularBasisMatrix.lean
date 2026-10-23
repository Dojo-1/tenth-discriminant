import TenthDiscriminant.RectangularValuation
import Mathlib.LinearAlgebra.Matrix.Block

/-!
# The sample-independent rectangular basis change

The binomial coefficients here encode
`Z^(r-pk) W^s (Z^p-W)^k` in the original row-major monomial basis.
This file constructs the integer matrix and proves it is unimodular.
Its action on the existing integer derivative rows is a later bridge.
-/
namespace TenthDiscriminant

/-- Column label of the term with `t` copies of `-W` in the expansion. -/
def rectangularBasisTarget (S p r s t : Nat) : Nat :=
  (r - p * t) * S + (s + t)

/-- Coefficient of canonical column `j` in the transformed row `i`.
The matrix is defined even for empty rectangles; its determinant
theorem requires `p>0`. -/
def rectangularBasisMatrix (R S p : Nat) :
    Matrix (Fin (R * S)) (Fin (R * S)) Int :=
  fun i j =>
    let k := rectangularBasisExponent R S p i
    (Finset.range (k + 1)).sum fun t =>
      if j.val = rectangularBasisTarget S p (i.val / S) (i.val % S) t
      then (-1 : Int) ^ t * (k.choose t : Int) else 0

/-- Every active binomial term remains in the original rectangle. -/
theorem rectangularBasis_term_bounds (R S p : Nat) (hp : 0 < p)
    (i : Fin (R * S)) (t : Nat)
    (ht : t ≤ rectangularBasisExponent R S p i) :
    p * t ≤ i.val / S ∧ i.val % S + t < S := by
  have hS : 0 < S := by
    by_contra h
    have h0 : S = 0 := by omega
    have hi := i.isLt
    simp [h0] at hi
  have hs : i.val % S < S := Nat.mod_lt _ hS
  rw [rectangularBasisExponent_eq] at ht
  have htr : t ≤ (i.val / S) / p :=
    ht.trans (min_le_left _ _)
  have hts : t ≤ S - 1 - i.val % S :=
    ht.trans (min_le_right _ _)
  have hpt : t * p ≤ i.val / S :=
    (Nat.le_div_iff_mul_le hp).mp htr
  constructor
  · simpa only [Nat.mul_comm] using hpt
  · omega

private theorem rectangularBasisTarget_lt (R S p : Nat) (hp : 0 < p)
    (i : Fin (R * S)) (t : Nat) (ht0 : 0 < t)
    (ht : t ≤ rectangularBasisExponent R S p i) :
    rectangularBasisTarget S p (i.val / S) (i.val % S) t < i.val := by
  obtain ⟨hpt, hst⟩ := rectangularBasis_term_bounds R S p hp i t ht
  have hS2 : 2 ≤ S := by omega
  have hptt : t ≤ p * t := by nlinarith
  have hmul : 2 * t ≤ (p * t) * S := by
    calc
      2 * t ≤ 2 * (p * t) := Nat.mul_le_mul_left 2 hptt
      _ ≤ S * (p * t) := Nat.mul_le_mul_right (p * t) hS2
      _ = (p * t) * S := Nat.mul_comm _ _
  have hdecomp :
      (i.val / S - p * t) * S + (p * t) * S = (i.val / S) * S := by
    rw [← Nat.add_mul, Nat.sub_add_cancel hpt]
  have hindex : (i.val / S) * S + i.val % S = i.val := by
    exact Nat.div_add_mod' i.val S
  unfold rectangularBasisTarget
  omega

/-- No active expansion term is silently discarded by the finite
matrix index: its target is an actual canonical column. -/
theorem rectangularBasisTarget_in_range (R S p : Nat) (hp : 0 < p)
    (i : Fin (R * S)) (t : Nat)
    (ht : t ≤ rectangularBasisExponent R S p i) :
    rectangularBasisTarget S p (i.val / S) (i.val % S) t < R * S := by
  by_cases ht0 : t = 0
  · subst t
    simp [rectangularBasisTarget, Nat.div_add_mod', i.isLt]
  · exact (rectangularBasisTarget_lt R S p hp i t
      (Nat.pos_of_ne_zero ht0) ht).trans i.isLt

/-- The pilot row `Z³-W` really uses original columns six and one;
the highest `s` row is unchanged. -/
theorem rectangularBasisMatrix_pilot :
    rectangularBasisMatrix 4 2 3 6 6 = 1 ∧
      rectangularBasisMatrix 4 2 3 6 1 = -1 ∧
        rectangularBasisMatrix 4 2 3 7 7 = 1 := by
  decide

/-- The whole pilot row, not only selected entries: row six is
`Z³-W`, and row seven remains `Z³W`. -/
theorem rectangularBasisMatrix_pilot_rows : ∀ j : Fin 8,
    rectangularBasisMatrix 4 2 3 6 j =
      (if j = 6 then 1 else if j = 1 then -1 else 0) ∧
    rectangularBasisMatrix 4 2 3 7 j =
      (if j = 7 then 1 else 0) := by
  decide

/-- Non-leading binomial terms point to strictly earlier columns, so
the explicit integer matrix is lower triangular in row-major order. -/
theorem rectangularBasisMatrix_lowerTriangular (R S p : Nat) (hp : 0 < p) :
    (rectangularBasisMatrix R S p).BlockTriangular
      (OrderDual.toDual : Fin (R * S) → OrderDual (Fin (R * S))) := by
  intro i j hij
  have hij' : i.val < j.val := by simpa using hij
  unfold rectangularBasisMatrix
  apply Finset.sum_eq_zero
  intro t ht
  by_cases ht0 : t = 0
  · subst t
    have hindex : (i.val / S) * S + i.val % S = i.val :=
      Nat.div_add_mod' i.val S
    simp [rectangularBasisTarget, hindex, ne_of_gt hij']
  · have htbound : t ≤ rectangularBasisExponent R S p i := by
      have h := Finset.mem_range.mp ht
      omega
    have hlt := rectangularBasisTarget_lt R S p hp i t
      (Nat.pos_of_ne_zero ht0) htbound
    have hne : j.val ≠ rectangularBasisTarget S p (i.val / S) (i.val % S) t :=
      ne_of_gt (hlt.trans hij')
    simp [hne]

/-- Every leading binomial coefficient is exactly one. -/
theorem rectangularBasisMatrix_diag (R S p : Nat) (hp : 0 < p)
    (i : Fin (R * S)) : rectangularBasisMatrix R S p i i = 1 := by
  unfold rectangularBasisMatrix
  rw [Finset.sum_eq_single 0]
  · have hindex : (i.val / S) * S + i.val % S = i.val :=
      Nat.div_add_mod' i.val S
    simp [rectangularBasisTarget, hindex]
  · intro t ht ht0
    have htbound : t ≤ rectangularBasisExponent R S p i := by
      have h := Finset.mem_range.mp ht
      omega
    have hlt := rectangularBasisTarget_lt R S p hp i t
      (Nat.pos_of_ne_zero ht0) htbound
    simp [ne_of_gt hlt]
  · simp

/-- The explicit rectangular binomial change of basis has determinant
one, including the empty-grid cases. This does not yet identify its
action on the repository's derivative trace-Gram matrix. -/
theorem rectangularBasisMatrix_det (R S p : Nat) (hp : 0 < p) :
    (rectangularBasisMatrix R S p).det = 1 := by
  rw [Matrix.det_of_lowerTriangular _
    (rectangularBasisMatrix_lowerTriangular R S p hp)]
  simp [rectangularBasisMatrix_diag R S p hp]

end TenthDiscriminant
