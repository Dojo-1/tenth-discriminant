import TenthDiscriminant.BinaryNullBasisMatrix
import TenthDiscriminant.BinaryNullOrdinaryJets
import TenthDiscriminant.RectangularRowAction

/-!
# Action of the binary-null basis on the ACTUAL original ordinary jets

For every original sample q and jet order j, the explicit unimodular
integer basis matrix must act on integerDerivativeRow, not on a
surrogate polynomial. This is the typed bridge to the existing
zsqrtdJetGram_transform/scale and integer determinant factor.
-/
namespace TenthDiscriminant

open Polynomial

/-- The exact target column for a valid binomial term. -/
def binaryNullBasisTargetFin (R S : Nat)
    (i : Fin (R*S)) (t : Nat) : Fin (R*S) :=
  ⟨binaryNullBasisTarget S (i.val/S) (i.val%S)
      (min t (binaryNullBasisExponent R S i)),
    binaryNullBasisTarget_in_range R S i _
      (min_le_right _ _)⟩

/-- No truncation of original monomial labels occurs. -/
theorem binaryNullBasisTargetFin_labels
    (R S : Nat) (i : Fin (R*S)) (t : Nat)
    (ht : t ≤ binaryNullBasisExponent R S i) :
    (binaryNullBasisTargetFin R S i t).val / S =
      i.val / S - 2*t ∧
    (binaryNullBasisTargetFin R S i t).val % S =
      i.val % S := by
  have hS : 0 < S := by
    by_contra hn
    have hz : S = 0 := by omega
    have hi := i.isLt
    simp [hz] at hi
  have hs : i.val % S < S := Nat.mod_lt _ hS
  have hr : 4*t ≤ i.val/S := by
    dsimp [binaryNullBasisExponent] at ht
    omega
  simp only [binaryNullBasisTargetFin, min_eq_left ht,
    binaryNullBasisTarget]
  constructor
  · rw [Nat.mul_comm (i.val/S-2*t) S, Nat.mul_add_div hS]
    simp [Nat.div_eq_of_lt hs]
  · exact Nat.mul_add_mod_of_lt hs

/-- The exact integer matrix acts by its original binomial row expansion. -/
theorem binaryNullBasisMatrix_row_action {A : Type*} [AddCommGroup A]
    (R S : Nat) (i : Fin (R*S)) (f : Fin (R*S) → A) :
    ∑ h : Fin (R*S), (binaryNullBasisMatrix R S i h) • f h =
      ∑ t ∈ Finset.range (binaryNullBasisExponent R S i + 1),
        ((-1 : Int)^t *
          (binaryNullBasisExponent R S i).choose t : Int) •
          f (binaryNullBasisTargetFin R S i t) := by
  classical
  unfold binaryNullBasisMatrix
  simp_rw [Finset.sum_smul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t ht
  have htk : t ≤ binaryNullBasisExponent R S i := by
    have h := Finset.mem_range.mp ht
    omega
  let target : Fin (R*S) :=
    ⟨binaryNullBasisTarget S (i.val/S) (i.val%S) t,
      binaryNullBasisTarget_in_range R S i t htk⟩
  have htest (h : Fin (R*S)) :
      (h.val = binaryNullBasisTarget S (i.val/S) (i.val%S) t) ↔
        h = target := by
    constructor
    · intro heq; exact Fin.ext heq
    · intro heq; exact congrArg Fin.val heq
  simp_rw [htest]
  have hfin : binaryNullBasisTargetFin R S i t = target := by
    apply Fin.ext
    simp [binaryNullBasisTargetFin, target, min_eq_left htk]
  simp [hfin, target]

/-- Binomial polynomial equality BEFORE differentiation, with each
nonleading term at the identical original monomial label. -/
theorem binaryNull_binomial_polynomial {A : Type*} [CommRing A]
    (w : A) (r s k : Nat) (hk : 4*k ≤ r) :
    X^(r-4*k) * C w^s * (X^4-X^2)^k =
      ∑ t ∈ Finset.range (k+1),
        (((-1 : Int)^t * (k.choose t : Int)) •
          (X^(r-2*t) * C w^s) : A[X]) := by
  have hb : (X^4-X^2 : A[X]) = -X^2 + X^4 := by ring
  rw [hb, add_pow, mul_assoc, Finset.mul_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro t ht
  have htk : t ≤ k := by
    have h := Finset.mem_range.mp ht
    omega
  have he : r-4*k + 2*t + 4*(k-t) = r-2*t := by omega
  rw [zsmul_eq_mul]
  rw [neg_pow, ← pow_mul, ← pow_mul]
  have hcoef :
      ((((-1 : Int)^t * (k.choose t : Int) : Int) : A[X])) =
        (-1 : A[X])^t * (k.choose t : A[X]) := by
    norm_num
  rw [hcoef]
  calc
    X^(r-4*k) *
        (C w^s * ((-1 : A[X])^t * X^(2*t) *
          X^(4*(k-t)) * (k.choose t : A[X]))) =
      ((-1 : A[X])^t * (k.choose t : A[X])) *
        ((X^(r-4*k) * X^(2*t) * X^(4*(k-t))) * C w^s) := by ac_rfl
    _ = _ := by rw [←pow_add, ←pow_add, he]

/-- The explicit integer basis matrix acts on original polynomial
monomials as the binary-null power with NO altered observation. -/
theorem binaryNullBasisMatrix_polynomial_action {A : Type*} [CommRing A]
    (R S : Nat) (i : Fin (R*S)) (w : A) :
    let r := i.val/S
    let s := i.val%S
    let k := binaryNullBasisExponent R S i
    ∑ h : Fin (R*S),
      (binaryNullBasisMatrix R S i h) •
        (X^(h.val/S) * C w^(h.val%S) : A[X]) =
      X^(r-4*k) * C w^s * (X^4-X^2)^k := by
  dsimp
  rw [binaryNullBasisMatrix_row_action R S i]
  have hk : 4*binaryNullBasisExponent R S i ≤ i.val/S := by
    simp [binaryNullBasisExponent]
    omega
  rw [binaryNull_binomial_polynomial w (i.val/S) (i.val%S)
    (binaryNullBasisExponent R S i) hk]
  apply Finset.sum_congr rfl
  intro t ht
  have htk : t ≤ binaryNullBasisExponent R S i := by
    have h := Finset.mem_range.mp ht
    omega
  obtain ⟨hr,hs⟩ := binaryNullBasisTargetFin_labels R S i t htk
  rw [hr,hs]

/-- Every original integer ordinary-jet row is transported to the
binary-null polynomial jet by the SAME explicit integer matrix. -/
theorem binaryNullBasisMatrix_integerDerivativeRow_action
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    let z := pairZsqrtdEquiv D a
    let r := i.val/S
    let s := i.val%S
    let k := binaryNullBasisExponent R S i
    ∑ h : Fin (R*S),
      (binaryNullBasisMatrix R S i h) •
        pairZsqrtdEquiv D
          (integerDerivativeRow D (h.val/S) (h.val%S) j a) =
      (derivative^[j]
        (X^(r-4*k) * C (star z)^s * (X^4-X^2)^k)).eval z := by
  dsimp
  have hpoly := binaryNullBasisMatrix_polynomial_action R S i
    (star (pairZsqrtdEquiv D a))
  rw [← hpoly, iterate_derivative_sum, eval_finset_sum]
  apply Finset.sum_congr rfl
  intro h hh
  rw [iterate_derivative_smul, eval_smul]
  congr 1
  exact integerDerivativeRow_zsqrtd_jet D (h.val/S) (h.val%S) j a

/-- The source row identity and the already checked all-orders
binary-null jet theorem provide full 2^k divisibility of each channel. -/
theorem binaryNullBasisMatrix_actualRow_dvd
    (D R S : Nat) (i : Fin (R*S))
    (a : Int × Int) (j : Nat) :
    (2 : Zsqrtd (-(D : Int)))^binaryNullBasisExponent R S i ∣
      ∑ h : Fin (R*S),
        (binaryNullBasisMatrix R S i h) •
          pairZsqrtdEquiv D
            (integerDerivativeRow D (h.val/S) (h.val%S) j a) := by
  rw [binaryNullBasisMatrix_integerDerivativeRow_action D R S i a j]
  exact binaryNull_power_allOrdinaryJets_dvd D a
    (X^(i.val/S-4*binaryNullBasisExponent R S i) *
      C (star (pairZsqrtdEquiv D a))^(i.val%S))
    (binaryNullBasisExponent R S i) j

end TenthDiscriminant
