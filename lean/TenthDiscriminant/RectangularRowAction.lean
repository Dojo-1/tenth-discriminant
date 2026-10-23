import TenthDiscriminant.RectangularBasisMatrix
import TenthDiscriminant.JetPower

/-!
# Acting on the original integer derivative rows

The first bridge identifies each original coordinate row with its
ordinary polynomial jet. Subsequent identities must use the explicit
binomial matrix, not an alternative matrix with the same determinant.
-/
namespace TenthDiscriminant

open Polynomial

/-- An original integer-coordinate derivative row is exactly the
ordinary polynomial jet, with the conjugate factor held constant. -/
theorem integerDerivativeRow_zsqrtd_jet (D r s j : Nat) (a : Int × Int) :
    let z := pairZsqrtdEquiv D a
    pairZsqrtdEquiv D (integerDerivativeRow D r s j a) =
      (derivative^[j] (X ^ r * C (star z) ^ s)).eval z := by
  dsimp
  rw [← map_pow, mul_comm, iterate_derivative_C_mul,
    iterate_derivative_X_pow_eq_C_mul]
  simp only [eval_mul, eval_C, eval_pow, eval_X]
  by_cases hj : j ≤ r
  · rw [integerDerivativeRow, if_pos hj, pairZsqrtd_scale,
      pairZsqrtd_mul, pairZsqrtd_pow, pairZsqrtd_pow,
      pairZsqrtd_conj]
    simp [pairZsqrtdEquiv, pairConj]
    ring
  · have hz : (r.descFactorial j : Zsqrtd (-(D : Int))) = 0 := by
      rw [Nat.descFactorial_of_lt (Nat.lt_of_not_ge hj)]
      rfl
    simp [integerDerivativeRow, hj, hz, pairZsqrtdEquiv]
    rfl

/-- The guarded binomial identity underlying the explicit rectangular
matrix. Every exponent on the right is a natural exponent because
`p*k ≤ r`; ordinary polynomial identity precedes differentiation. -/
theorem rectangular_binomial_polynomial {A : Type*} [CommRing A]
    (w : A) (r s p k : Nat) (hpk : p * k ≤ r) :
    X ^ (r - p * k) * C w ^ s * (X ^ p - C w) ^ k =
      ∑ t ∈ Finset.range (k + 1),
        (((-1 : Int) ^ t * (k.choose t : Int)) •
          (X ^ (r - p * t) * C w ^ (s + t)) : A[X]) := by
  have hb : (X ^ p - C w : A[X]) = -C w + X ^ p := by ring
  rw [hb, add_pow, mul_assoc, Finset.mul_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro t ht
  have htk : t ≤ k := by
    have := Finset.mem_range.mp ht
    omega
  have hpt : p * t ≤ p * k := Nat.mul_le_mul_left p htk
  have hmul : p * (k - t) = p * k - p * t := Nat.mul_sub_left_distrib p k t
  have hexp : r - p * k + p * (k - t) = r - p * t := by omega
  rw [zsmul_eq_mul]
  rw [neg_pow, ← pow_mul]
  have hcoef :
      (((-1 : Int) ^ t * (k.choose t : Int) : Int) : A[X]) =
        (-1 : A[X]) ^ t * (k.choose t : A[X]) := by
    norm_num
  rw [hcoef]
  calc
    X ^ (r - p * k) *
        (C w ^ s * ((-1) ^ t * C w ^ t * X ^ (p * (k - t)) *
          (k.choose t : A[X]))) =
      ((-1 : A[X]) ^ t * (k.choose t : A[X])) *
        ((X ^ (r - p * k) * X ^ (p * (k - t))) *
          (C w ^ s * C w ^ t)) := by ac_rfl
    _ = _ := by rw [← pow_add, ← pow_add, hexp]

/-- Total finite column index for a binomial term. The `min` only
defines out-of-range arguments; on the active sum range it is `t`. -/
def rectangularBasisTargetFin (R S p : Nat) (hp : 0 < p)
    (i : Fin (R * S)) (t : Nat) : Fin (R * S) :=
  ⟨rectangularBasisTarget S p (i.val / S) (i.val % S)
      (min t (rectangularBasisExponent R S p i)),
    rectangularBasisTarget_in_range R S p hp i _ (min_le_right _ _)⟩

/-- On an active term, quotient and remainder recover the intended
monomial labels, so the matrix's column is not merely in range. -/
theorem rectangularBasisTargetFin_labels (R S p : Nat) (hp : 0 < p)
    (i : Fin (R * S)) (t : Nat)
    (ht : t ≤ rectangularBasisExponent R S p i) :
    (rectangularBasisTargetFin R S p hp i t).val / S = i.val / S - p * t ∧
    (rectangularBasisTargetFin R S p hp i t).val % S = i.val % S + t := by
  have hst := (rectangularBasis_term_bounds R S p hp i t ht).2
  have hS : 0 < S := by omega
  simp only [rectangularBasisTargetFin, min_eq_left ht,
    rectangularBasisTarget]
  constructor
  · rw [Nat.mul_comm (i.val / S - p * t) S, Nat.mul_add_div hS]
    simp [Nat.div_eq_of_lt hst]
  · exact Nat.mul_add_mod_of_lt hst

/-- A matrix row acts on any abelian-group-valued column family by
the original guarded binomial sum. No sample or polynomial has been
substituted yet; this is the exact matrix rather than a surrogate. -/
theorem rectangularBasisMatrix_row_action {A : Type*} [AddCommGroup A]
    (R S p : Nat) (hp : 0 < p) (i : Fin (R * S))
    (f : Fin (R * S) → A) :
    ∑ h : Fin (R * S), (rectangularBasisMatrix R S p i h) • f h =
      ∑ t ∈ Finset.range (rectangularBasisExponent R S p i + 1),
        ((-1 : Int) ^ t *
          (rectangularBasisExponent R S p i).choose t : Int) •
          f (rectangularBasisTargetFin R S p hp i t) := by
  classical
  unfold rectangularBasisMatrix
  simp_rw [Finset.sum_smul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t ht
  have htk : t ≤ rectangularBasisExponent R S p i := by
    have := Finset.mem_range.mp ht
    omega
  let target : Fin (R * S) :=
    ⟨rectangularBasisTarget S p (i.val / S) (i.val % S) t,
      rectangularBasisTarget_in_range R S p hp i t htk⟩
  have htest (h : Fin (R * S)) :
      (h.val = rectangularBasisTarget S p (i.val / S) (i.val % S) t) ↔
        h = target := by
    constructor
    · intro heq; exact Fin.ext heq
    · intro heq; exact congrArg Fin.val heq
  simp_rw [htest]
  have hfin : rectangularBasisTargetFin R S p hp i t = target := by
    apply Fin.ext
    simp [rectangularBasisTargetFin, target, min_eq_left htk]
  simp [hfin, target]

/-- The **actual explicit integer matrix** sends the canonical
monomial-polynomial family to the proposed `Z^p-W` basis, before any
sample or derivative is taken. -/
theorem rectangularBasisMatrix_polynomial_action {A : Type*} [CommRing A]
    (R S p : Nat) (hp : 0 < p) (i : Fin (R * S)) (w : A) :
    let r := i.val / S
    let s := i.val % S
    let k := rectangularBasisExponent R S p i
    ∑ h : Fin (R * S),
      (rectangularBasisMatrix R S p i h) •
        (X ^ (h.val / S) * C w ^ (h.val % S) : A[X]) =
      X ^ (r - p * k) * C w ^ s * (X ^ p - C w) ^ k := by
  dsimp
  rw [rectangularBasisMatrix_row_action R S p hp i]
  have hpk :=
    (rectangularBasis_term_bounds R S p hp i
      (rectangularBasisExponent R S p i) le_rfl).1
  rw [rectangular_binomial_polynomial w (i.val / S) (i.val % S)
    p (rectangularBasisExponent R S p i) hpk]
  apply Finset.sum_congr rfl
  intro t ht
  have htk : t ≤ rectangularBasisExponent R S p i := by
    have := Finset.mem_range.mp ht
    omega
  obtain ⟨hr, hs⟩ := rectangularBasisTargetFin_labels R S p hp i t htk
  rw [hr, hs]

/-- The missing samplewise commuting square: matrix action on the
repository's original integer derivative rows equals the ordinary jet
of the transformed polynomial, at every original pair sample and every
derivative order. The coefficient matrix is exactly the one whose
determinant was previously checked to equal one. -/
theorem rectangularBasisMatrix_integerDerivativeRow_action
    (D R S p : Nat) (hp : 0 < p) (i : Fin (R * S))
    (a : Int × Int) (j : Nat) :
    let z := pairZsqrtdEquiv D a
    let r := i.val / S
    let s := i.val % S
    let k := rectangularBasisExponent R S p i
    ∑ h : Fin (R * S),
      (rectangularBasisMatrix R S p i h) •
        pairZsqrtdEquiv D
          (integerDerivativeRow D (h.val / S) (h.val % S) j a) =
      (derivative^[j]
        (X ^ (r - p * k) * C (star z) ^ s *
          (X ^ p - C (star z)) ^ k)).eval z := by
  dsimp
  have hpoly := rectangularBasisMatrix_polynomial_action R S p hp i
    (star (pairZsqrtdEquiv D a))
  rw [← hpoly, iterate_derivative_sum, eval_finset_sum]
  apply Finset.sum_congr rfl
  intro h hh
  rw [iterate_derivative_smul, eval_smul]
  congr 1
  exact integerDerivativeRow_zsqrtd_jet D (h.val / S) (h.val % S) j a

/-- Under the explicit local Frobenius congruence, the transformed
**actual** row—not merely a proposed polynomial—has the exact
`p^k` factor in both integer coordinates for every derivative order. -/
theorem rectangularBasisMatrix_actualRow_coordinates
    (D R S p : Nat) (hp : 0 < p) (i : Fin (R * S))
    (a : Int × Int) (j : Nat)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    let v := ∑ h : Fin (R * S),
      (rectangularBasisMatrix R S p i h) •
        pairZsqrtdEquiv D
          (integerDerivativeRow D (h.val / S) (h.val % S) j a)
    (p : Int) ^ rectangularBasisExponent R S p i ∣ v.re ∧
      (p : Int) ^ rectangularBasisExponent R S p i ∣ v.im := by
  dsimp
  rw [rectangularBasisMatrix_integerDerivativeRow_action D R S p hp i a j]
  exact rectangular_frobenius_row_jet_coordinates D p
    (i.val / S) (i.val % S) (rectangularBasisExponent R S p i)
    j a hzero

/-- The same actual-row statement as divisibility inside the selected
quadratic order, ready for constructing an integral quotient jet. -/
theorem rectangularBasisMatrix_actualRow_dvd
    (D R S p : Nat) (hp : 0 < p) (i : Fin (R * S))
    (a : Int × Int) (j : Nat)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    (p : Zsqrtd (-(D : Int))) ^ rectangularBasisExponent R S p i ∣
      ∑ h : Fin (R * S),
        (rectangularBasisMatrix R S p i h) •
          pairZsqrtdEquiv D
            (integerDerivativeRow D (h.val / S) (h.val % S) j a) := by
  have hc := rectangularBasisMatrix_actualRow_coordinates
    D R S p hp i a j hzero
  have h := (zsqrtd_natCast_dvd_iff (-(D : Int))
    (p ^ rectangularBasisExponent R S p i) _).mpr (by
      simpa only [Nat.cast_pow] using hc)
  simpa only [Nat.cast_pow] using h

end TenthDiscriminant
