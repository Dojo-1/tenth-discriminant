import TenthDiscriminant.IntegerTraceGram

/-! The two sign-character sectors of the original ordinary-jet Gram.
No variable swap, replacement minor or strict determinant saving is used. -/
namespace TenthDiscriminant
open scoped ComplexConjugate
set_option autoImplicit false
noncomputable section

private theorem derivativeRow_neg (r s j : Nat) (z : Complex) :
    derivativeRow r s j (-z) =
      (-1 : Complex) ^ (r-j+s) * derivativeRow r s j z := by
  by_cases hj : j ≤ r
  · simp only [derivativeRow, if_pos hj, map_neg]
    rw [neg_pow z (r-j), neg_pow (conj z) s, pow_add]
    ring
  · simp [derivativeRow, hj]

private theorem jet_pairing_neg (r s t u j : Nat) (z : Complex)
    (hodd : (r+s+t+u)%2=1) :
    derivativeRow r s j (-z) * conj (derivativeRow t u j (-z)) =
      -(derivativeRow r s j z * conj (derivativeRow t u j z)) := by
  by_cases hr : j ≤ r
  · by_cases ht : j ≤ t
    · have he : (r-j+s+(t-j+u))%2=1 := by omega
      have hp : (-1 : Complex)^(r-j+s+(t-j+u)) = -1 :=
        (Nat.odd_iff.mpr he).neg_one_pow
      rw [derivativeRow_neg, derivativeRow_neg, map_mul, map_pow]
      simp only [map_neg, map_one]
      calc
        _ = (-1 : Complex)^(r-j+s+(t-j+u)) *
            (derivativeRow r s j z * conj (derivativeRow t u j z)) := by
              rw [pow_add]
              ring
        _ = _ := by rw [hp]; ring
    · simp [derivativeRow, ht]
  · simp [derivativeRow, hr]

private theorem pairEval_neg (D : Nat) (a : Int × Int) :
    pairEval D (-a) = -pairEval D a := by
  apply Complex.ext <;> simp [pairEval, latticePoint]

private theorem integer_pairing_neg (D r s t u j : Nat) (a : Int × Int)
    (hodd : (r+s+t+u)%2=1) :
    integerPairTrace D (integerDerivativeRow D r s j (-a))
      (integerDerivativeRow D t u j (-a)) =
    -integerPairTrace D (integerDerivativeRow D r s j a)
      (integerDerivativeRow D t u j a) := by
  apply (Int.cast_injective (α := Real))
  push_cast
  rw [integerPairTrace_cast, integerPairTrace_cast]
  simp only [integerDerivativeRow_eval, pairEval_neg]
  rw [jet_pairing_neg r s t u j _ hodd]
  simp <;> ring

/-- Opposite total-degree parity sectors are orthogonal on a centrally
symmetric sample set, retaining every ordinary derivative and factor two. -/
theorem integerTraceGramEntry_eq_zero_of_central_symmetry
    (Q : Finset (Int × Int)) (D J r s t u : Nat)
    (hQ : ∀ a ∈ Q, -a ∈ Q) (hodd : (r+s+t+u)%2=1) :
    integerTraceGramEntry Q D J r s t u = 0 := by
  classical
  unfold integerTraceGramEntry
  apply Finset.sum_eq_zero
  intro j hj
  let f := fun a => integerPairTrace D (integerDerivativeRow D r s j a)
    (integerDerivativeRow D t u j a)
  have hs : (∑ a ∈ Q, f (-a)) = ∑ a ∈ Q, f a := by
    apply Finset.sum_bij (fun a _ => -a)
    · exact fun a ha => hQ a ha
    · intro a ha b hb hab
      exact neg_injective hab
    · intro b hb
      exact ⟨-b, hQ b hb, neg_neg b⟩
    · intro a ha
      rfl
  have hn : (∑ a ∈ Q, f (-a)) = -(∑ a ∈ Q, f a) := by
    rw [← Finset.sum_neg_distrib]
    apply Finset.sum_congr rfl
    intro a ha
    exact integer_pairing_neg D r s t u j a hodd
  dsimp [f] at hs hn
  omega

theorem ellipsePairs_central_symmetry (D rho : Nat) (hD : 0 < D)
    (a : Int × Int) (ha : a ∈ ellipsePairs D rho) :
    -a ∈ ellipsePairs D rho := by
  rw [mem_ellipsePairs_iff D rho hD] at ha ⊢
  simpa using ha

theorem ellipseTraceGramEntry_eq_zero_of_odd_degree
    (D rho J r s t u : Nat) (hD : 0 < D) (hodd : (r+s+t+u)%2=1) :
    integerTraceGramEntry (ellipsePairs D rho) D J r s t u = 0 :=
  integerTraceGramEntry_eq_zero_of_central_symmetry _ _ _ _ _ _ _
    (ellipsePairs_central_symmetry D rho hD) hodd

/-- Without sample symmetry the opposite-parity entry can be nonzero. -/
theorem central_symmetry_required_control :
    integerTraceGramEntry {(1,0)} 1 1 0 0 1 0 = 2 := by
  norm_num [integerTraceGramEntry, integerDerivativeRow, integerPairTrace,
    pairScale, pairMul, pairPow, pairConj, Nat.descFactorial]

end
end TenthDiscriminant
