import TenthDiscriminant.Phase227JointJets
import TenthDiscriminant.RectangularBasisMatrix

/-!
# Phase228: one source frame for the two noncommuting Frobenius factors

The integer matrix acts on the ORIGINAL row-major rectangle, not as a
composition of two independently truncated row maps. The term (t,u)
encodes the binomial expansion of
  Z^(r-p*k) W^(s-p*p*ell) (Z^p-W)^k (W^(p*p)-W)^ell
where k=min(r/p,S-1-s), ell=floor(s/(p*p)).

No same-Gram prime divisor follows from determinant-one alone. The
polynomial row action and both-sided Gram factor remain separate gates.
-/

namespace TenthDiscriminant.Phase228

open scoped BigOperators

/-- Number of full horizontal Frobenius blocks in the original row. -/
def horizontalBasisExponent (R S p : Nat) (i : Fin (R*S)) : Nat :=
  (i.val % S) / (p*p)

/-- The old row-major label of the (t,u) binomial term. -/
def combinedBasisTarget (S p r s t u : Nat) : Nat :=
  (r-p*t)*S + (s+t-(p*p-1)*u)

/-- The unique leading term keeps the old source label. -/
theorem combinedBasisTarget_zero (R S p : Nat) (i : Fin (R*S)) :
    combinedBasisTarget S p (i.val / S) (i.val % S) 0 0 = i.val := by
  simp [combinedBasisTarget, Nat.div_add_mod']

/-- Every non-leading term is strictly earlier in row-major order.
When t>0, the Z degree falls; otherwise u>0 lowers the W degree. -/
theorem combinedBasisTarget_lt (R S p : Nat) (hp : 2 ≤ p)
    (i : Fin (R*S)) (t u : Nat)
    (ht : t ≤ rectangularBasisExponent R S p i)
    (hu : u ≤ horizontalBasisExponent R S p i)
    (hneq : t ≠ 0 ∨ u ≠ 0) :
    combinedBasisTarget S p (i.val / S) (i.val % S) t u < i.val := by
  obtain ⟨hpt, hst⟩ := rectangularBasis_term_bounds R S p (by omega) i t ht
  have hS : 0 < S := by
    by_contra hh
    have hzero : S = 0 := by omega
    have hlt := i.isLt
    simp [hzero] at hlt
  have hdecomp : (i.val / S)*S + i.val % S = i.val :=
    Nat.div_add_mod' i.val S
  have hsmall : i.val % S + t - (p*p-1)*u < S :=
    lt_of_le_of_lt (Nat.sub_le _ _) hst
  by_cases htzero : t = 0
  · subst t
    have hu0 : u ≠ 0 := by
      rcases hneq with ht0 | hu0
      · exact False.elim (ht0 rfl)
      · exact hu0
    have hupos : 0 < u := Nat.pos_of_ne_zero hu0
    have hp2 : 0 < p*p := Nat.mul_pos (by omega) (by omega)
    have hdiv : (p*p)*u ≤ i.val % S := by
      simpa only [Nat.mul_comm] using (Nat.le_div_iff_mul_le hp2).mp hu
    have hpp : 1 < p*p := by nlinarith
    have hdpos : 0 < (p*p-1)*u :=
      Nat.mul_pos (by omega) hupos
    have hle : (p*p-1)*u ≤ i.val % S :=
      (Nat.mul_le_mul_right u (Nat.sub_le (p*p) 1)).trans hdiv
    have hspos : 0 < i.val % S := lt_of_lt_of_le hdpos hle
    have hsub : i.val % S - (p*p-1)*u < i.val % S :=
      Nat.sub_lt hspos hdpos
    simpa only [combinedBasisTarget, Nat.mul_zero, Nat.sub_zero,
        Nat.zero_add, Nat.add_zero] using
      (show (i.val / S)*S + (i.val % S - (p*p-1)*u) < i.val by omega)
  · have htpos : 0 < t := Nat.pos_of_ne_zero htzero
    have hptpos : 0 < p*t := Nat.mul_pos (by omega) htpos
    have hrd : i.val / S - p*t < i.val / S :=
      Nat.sub_lt (by omega) hptpos
    have hmul : (i.val / S - p*t + 1)*S ≤ (i.val / S)*S :=
      Nat.mul_le_mul_right S (by omega)
    have hnext : (i.val / S - p*t)*S +
        (i.val % S + t - (p*p-1)*u) <
        (i.val / S - p*t + 1)*S := by
      nlinarith
    unfold combinedBasisTarget
    omega

/-- All active terms stay in the ORIGINAL rectangular source. -/
theorem combinedBasisTarget_in_range (R S p : Nat) (hp : 2 ≤ p)
    (i : Fin (R*S)) (t u : Nat)
    (ht : t ≤ rectangularBasisExponent R S p i)
    (hu : u ≤ horizontalBasisExponent R S p i) :
    combinedBasisTarget S p (i.val / S) (i.val % S) t u < R*S := by
  by_cases h00 : t = 0 ∧ u = 0
  · rcases h00 with ⟨rfl,rfl⟩
    rw [combinedBasisTarget_zero]
    exact i.isLt
  · exact (combinedBasisTarget_lt R S p hp i t u ht hu (by omega)).trans i.isLt

/-- An active two-index term recovers the ORIGINAL row-major labels.
The residual W exponent is kept as a Nat subtraction: neither the
source nor the ordinary-jet evaluation has been replaced.  This is
the necessary label bridge before the universal polynomial action. -/
theorem combinedBasisTarget_active_labels
    (R S p : Nat) (hp : 2 ≤ p) (i : Fin (R*S))
    (t u : Nat)
    (ht : t ≤ rectangularBasisExponent R S p i)
    (hu : u ≤ horizontalBasisExponent R S p i) :
    (combinedBasisTarget S p (i.val / S) (i.val % S) t u) / S =
      i.val / S - p*t ∧
    (combinedBasisTarget S p (i.val / S) (i.val % S) t u) % S =
      i.val % S + t - (p*p-1)*u := by
  have hst := (rectangularBasis_term_bounds R S p (by omega) i t ht).2
  have hres : i.val % S + t - (p*p-1)*u < S :=
    lt_of_le_of_lt (Nat.sub_le _ _) hst
  have hS : 0 < S := by omega
  constructor
  · unfold combinedBasisTarget
    rw [Nat.mul_comm (i.val / S - p*t) S, Nat.mul_add_div hS]
    simp [Nat.div_eq_of_lt hres]
  · unfold combinedBasisTarget
    exact Nat.mul_add_mod_of_lt hres

/-- One explicit integer matrix with BOTH binomial coefficients. -/
def combinedBasisMatrix (R S p : Nat) :
    Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  fun i j =>
    let k := rectangularBasisExponent R S p i
    let ell := horizontalBasisExponent R S p i
    ∑ t ∈ Finset.range (k+1), ∑ u ∈ Finset.range (ell+1),
      if j.val = combinedBasisTarget S p (i.val / S) (i.val % S) t u
      then (-1 : Int)^(t+u) * (k.choose t : Int) * (ell.choose u : Int)
      else 0

/-- A total Fin target for the two-index expansion. Clamping is only
to make this function defined OUTSIDE the active binomial ranges; on
every active term, the original target is used without modification. -/
def combinedBasisTargetFin (R S p : Nat) (hp : 2 ≤ p)
    (i : Fin (R*S)) (t u : Nat) : Fin (R*S) :=
  ⟨combinedBasisTarget S p (i.val / S) (i.val % S)
      (min t (rectangularBasisExponent R S p i))
      (min u (horizontalBasisExponent R S p i)),
   combinedBasisTarget_in_range R S p hp i _ _
     (min_le_right _ _) (min_le_right _ _)⟩

/-- On active terms, the total target recovers BOTH original monomial
labels, before evaluation and with no assumption on the sample. -/
theorem combinedBasisTargetFin_labels
    (R S p : Nat) (hp : 2 ≤ p) (i : Fin (R*S))
    (t u : Nat)
    (ht : t ≤ rectangularBasisExponent R S p i)
    (hu : u ≤ horizontalBasisExponent R S p i) :
    (combinedBasisTargetFin R S p hp i t u).val / S =
      i.val / S - p*t ∧
    (combinedBasisTargetFin R S p hp i t u).val % S =
      i.val % S + t - (p*p-1)*u := by
  simpa only [combinedBasisTargetFin, min_eq_left ht, min_eq_left hu] using
    combinedBasisTarget_active_labels R S p hp i t u ht hu

/-- The COMBINED integral source matrix acts through the exact
two-index binomial sum on ANY additive observation family. No change
of field, derivative convention, support, or trace pairing occurs here.
In particular, this action is not the product of truncated source maps. -/
theorem combinedBasisMatrix_row_action {A : Type*} [AddCommGroup A]
    (R S p : Nat) (hp : 2 ≤ p) (i : Fin (R*S))
    (f : Fin (R*S) → A) :
    ∑ h : Fin (R*S), (combinedBasisMatrix R S p i h) • f h =
      ∑ t ∈ Finset.range (rectangularBasisExponent R S p i + 1),
        ∑ u ∈ Finset.range (horizontalBasisExponent R S p i + 1),
          ((-1 : Int)^(t+u) *
            ((rectangularBasisExponent R S p i).choose t : Int) *
            ((horizontalBasisExponent R S p i).choose u : Int)) •
            f (combinedBasisTargetFin R S p hp i t u) := by
  classical
  unfold combinedBasisMatrix
  simp_rw [Finset.sum_smul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t ht
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro u hu
  have htk : t ≤ rectangularBasisExponent R S p i := by
    have := Finset.mem_range.mp ht
    omega
  have hul : u ≤ horizontalBasisExponent R S p i := by
    have := Finset.mem_range.mp hu
    omega
  let target : Fin (R*S) :=
    ⟨combinedBasisTarget S p (i.val / S) (i.val % S) t u,
      combinedBasisTarget_in_range R S p hp i t u htk hul⟩
  have htest (h : Fin (R*S)) :
      (h.val = combinedBasisTarget S p (i.val / S)
        (i.val % S) t u) ↔ h = target := by
    constructor
    · intro heq; exact Fin.ext heq
    · intro heq; exact congrArg Fin.val heq
  simp_rw [htest]
  have hfin : combinedBasisTargetFin R S p hp i t u = target := by
    apply Fin.ext
    simp [combinedBasisTargetFin, target, min_eq_left htk, min_eq_left hul]
  simp [hfin, target]

/-- Lower triangular in the original source order. -/
theorem combinedBasisMatrix_lowerTriangular (R S p : Nat) (hp : 2 ≤ p) :
    (combinedBasisMatrix R S p).BlockTriangular
      (OrderDual.toDual : Fin (R*S) → OrderDual (Fin (R*S))) := by
  intro i j hij
  have hij' : i.val < j.val := by simpa using hij
  unfold combinedBasisMatrix
  apply Finset.sum_eq_zero
  intro t ht
  apply Finset.sum_eq_zero
  intro u hu
  have htk : t ≤ rectangularBasisExponent R S p i := by
    have h := Finset.mem_range.mp ht
    omega
  have hul : u ≤ horizontalBasisExponent R S p i := by
    have h := Finset.mem_range.mp hu
    omega
  by_cases h00 : t = 0 ∧ u = 0
  · obtain ⟨rfl,rfl⟩ := h00
    simp [combinedBasisTarget_zero R S p i, ne_of_gt hij']
  · have hlt := combinedBasisTarget_lt R S p hp i t u htk hul (by omega)
    simp [ne_of_gt (hlt.trans hij')]

/-- Each diagonal coefficient is precisely one. -/
theorem combinedBasisMatrix_diag (R S p : Nat) (hp : 2 ≤ p)
    (i : Fin (R*S)) : combinedBasisMatrix R S p i i = 1 := by
  unfold combinedBasisMatrix
  rw [Finset.sum_eq_single 0]
  · rw [Finset.sum_eq_single 0]
    · simp [combinedBasisTarget_zero R S p i]
    · intro u hu hu0
      have hul : u ≤ horizontalBasisExponent R S p i := by
        have h := Finset.mem_range.mp hu
        omega
      have hlt := combinedBasisTarget_lt R S p hp i 0 u
        (Nat.zero_le _) hul (Or.inr hu0)
      simp [ne_of_gt hlt]
    · simp
  · intro t ht ht0
    apply Finset.sum_eq_zero
    intro u hu
    have htk : t ≤ rectangularBasisExponent R S p i := by
      have h := Finset.mem_range.mp ht
      omega
    have hul : u ≤ horizontalBasisExponent R S p i := by
      have h := Finset.mem_range.mp hu
      omega
    have hlt := combinedBasisTarget_lt R S p hp i t u htk hul (Or.inl ht0)
    simp [ne_of_gt hlt]
  · simp

/-- The SINGLE combined source basis is unimodular. -/
theorem combinedBasisMatrix_det (R S p : Nat) (hp : 2 ≤ p) :
    (combinedBasisMatrix R S p).det = 1 := by
  rw [Matrix.det_of_lowerTriangular _
    (combinedBasisMatrix_lowerTriangular R S p hp)]
  simp [combinedBasisMatrix_diag R S p hp]

/-- At (r,s)=(3,9), p=3, R=4, S=11, the four old
monomial coefficients are 1,-1,-1,+1 at columns 42,34,10,2. -/
theorem combinedBasisMatrix_pilot :
    combinedBasisMatrix 4 11 3 42 42 = 1 ∧
    combinedBasisMatrix 4 11 3 42 34 = -1 ∧
    combinedBasisMatrix 4 11 3 42 10 = -1 ∧
    combinedBasisMatrix 4 11 3 42 2 = 1 := by
  decide

/-- The p=3 combined Frobenius source term preserves total-degree parity
of its ORIGINAL (Z,W) monomial labels.  The inequalities guarantee
Nat.sub does not saturate; no Gram or field claim is made here. -/
theorem combinedBasisTarget_exponents_parity_three
    (r s t u : Nat) (hr : 3*t ≤ r) (hs : 9*u ≤ s) :
    ((r - 3*t) + (s+t-8*u)) % 2 = (r+s) % 2 := by
  omega

/-- The same exact source-label parity invariant at the other
production inert prime p=5. -/
theorem combinedBasisTarget_exponents_parity_five
    (r s t u : Nat) (hr : 5*t ≤ r) (hs : 25*u ≤ s) :
    ((r - 5*t) + (s+t-24*u)) % 2 = (r+s) % 2 := by
  omega

/-- Entire original row 42, not just four sampled coefficients:
the combined (p=3, r=3, s=9) source action has exactly the
four binomial terms in the ORIGINAL 4-by-11 rectangle. -/
theorem combinedBasisMatrix_pilot_full_row :
    ∀ j : Fin 44,
      combinedBasisMatrix 4 11 3 42 j =
        (if j = 42 then (1 : Int)
         else if j = 34 then -1
         else if j = 10 then -1
         else if j = 2 then 1
         else 0) := by
  decide

/-- At p=5 the two factors (Z^5-W)(W^25-W) likewise remain
inside one original 6-by-27 source rectangle, including all
signs and both non-leading target positions. -/
theorem combinedBasisMatrix_pilot_five :
    combinedBasisMatrix 6 27 5 160 160 = 1 ∧
    combinedBasisMatrix 6 27 5 160 136 = -1 ∧
    combinedBasisMatrix 6 27 5 160 26 = -1 ∧
    combinedBasisMatrix 6 27 5 160 2 = 1 := by
  decide

end TenthDiscriminant.Phase228

#print axioms TenthDiscriminant.Phase228.combinedBasisTarget_lt
#print axioms TenthDiscriminant.Phase228.combinedBasisMatrix_lowerTriangular
#print axioms TenthDiscriminant.Phase228.combinedBasisMatrix_det
#print axioms TenthDiscriminant.Phase228.combinedBasisMatrix_pilot

#print axioms TenthDiscriminant.Phase228.combinedBasisTarget_exponents_parity_three
#print axioms TenthDiscriminant.Phase228.combinedBasisTarget_exponents_parity_five

#print axioms TenthDiscriminant.Phase228.combinedBasisMatrix_pilot_full_row
#print axioms TenthDiscriminant.Phase228.combinedBasisMatrix_pilot_five

#print axioms TenthDiscriminant.Phase228.combinedBasisTarget_active_labels

#print axioms TenthDiscriminant.Phase228.combinedBasisTargetFin_labels
#print axioms TenthDiscriminant.Phase228.combinedBasisMatrix_row_action
