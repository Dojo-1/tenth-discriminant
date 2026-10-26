import TenthDiscriminant.CentralSymmetry
import TenthDiscriminant.RectangularRowAction

/-! The same sign sectors are preserved by geometry and the odd-p
integral Frobenius basis matrix. No quantitative gain is inferred. -/
namespace TenthDiscriminant
set_option autoImplicit false

def rectangularRowParity (R S : Nat) (i : Fin (R*S)) : Nat :=
  (i.val/S+i.val%S)%2

def rectangularRowSign (R S : Nat) (i : Fin (R*S)) : Int :=
  if rectangularRowParity R S i=0 then 1 else -1

def rectangularSignMatrix (R S : Nat) : Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  Matrix.diagonal (rectangularRowSign R S)

private theorem odd_step_preserves_parity (r s p t : Nat)
    (hp : p%2=1) (hpt : p*t ≤ r) :
    (r-p*t+(s+t))%2=(r+s)%2 := by
  have hm : (p*t)%2=t%2 := by simp [Nat.mul_mod, hp]
  omega

/-- The explicit integer binomial basis matrix never crosses parity
sectors when p is odd; guarded natural subtraction is used throughout. -/
theorem rectangularBasisMatrix_eq_zero_of_parity_ne
    (R S p : Nat) (hp : 0 < p) (hodd : p%2=1)
    (i j : Fin (R*S))
    (hne : rectangularRowParity R S i ≠ rectangularRowParity R S j) :
    rectangularBasisMatrix R S p i j=0 := by
  unfold rectangularBasisMatrix
  apply Finset.sum_eq_zero
  intro t ht
  have htk : t ≤ rectangularBasisExponent R S p i := by
    have := Finset.mem_range.mp ht
    omega
  by_cases hj : j.val=rectangularBasisTarget S p (i.val/S) (i.val%S) t
  · have hfin : j=rectangularBasisTargetFin R S p hp i t := by
      apply Fin.ext
      simpa only [rectangularBasisTargetFin, min_eq_left htk] using hj
    obtain ⟨hr,hs⟩ := rectangularBasisTargetFin_labels R S p hp i t htk
    have hpar : rectangularRowParity R S j=rectangularRowParity R S i := by
      rw [hfin]
      unfold rectangularRowParity
      rw [hr,hs]
      exact odd_step_preserves_parity _ _ _ _ hodd
        (rectangularBasis_term_bounds R S p hp i t htk).1
    exact False.elim (hne hpar.symm)
  · simp [hj]

private theorem commutes_sign_of_parity_support (R S : Nat)
    (A : Matrix (Fin (R*S)) (Fin (R*S)) Int)
    (hz : ∀ i j, rectangularRowParity R S i ≠ rectangularRowParity R S j → A i j=0) :
    A * rectangularSignMatrix R S = rectangularSignMatrix R S * A := by
  classical
  unfold rectangularSignMatrix
  ext i j
  rw [Matrix.mul_diagonal, Matrix.diagonal_mul]
  by_cases h : rectangularRowParity R S i=rectangularRowParity R S j
  · have hs : rectangularRowSign R S i=rectangularRowSign R S j := by
      simp only [rectangularRowSign, h]
    rw [hs, mul_comm]
  · rw [hz i j h]
    simp

theorem rectangularBasisMatrix_commutes_sign (R S p : Nat)
    (hp : 0 < p) (hodd : p%2=1) :
    rectangularBasisMatrix R S p * rectangularSignMatrix R S =
      rectangularSignMatrix R S * rectangularBasisMatrix R S p :=
  commutes_sign_of_parity_support R S _
    (rectangularBasisMatrix_eq_zero_of_parity_ne R S p hp hodd)

theorem integerRectangularTraceGram_commutes_sign
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (hQ : ∀ a ∈ Q, -a ∈ Q) :
    integerRectangularTraceGram Q D J R S * rectangularSignMatrix R S =
      rectangularSignMatrix R S * integerRectangularTraceGram Q D J R S := by
  apply commutes_sign_of_parity_support R S
  intro i j hne
  have ho : (i.val/S+i.val%S+j.val/S+j.val%S)%2=1 := by
    unfold rectangularRowParity at hne
    omega
  exact integerTraceGramEntry_eq_zero_of_central_symmetry Q D J _ _ _ _ hQ ho

/-- The prime-two row Z^2-W mixes even and odd sectors. -/
theorem oddness_required_parity_control :
    rectangularBasisMatrix 3 2 2 4 1 = -1 ∧
    rectangularRowParity 3 2 4=0 ∧ rectangularRowParity 3 2 1=1 := by
  decide

end TenthDiscriminant
