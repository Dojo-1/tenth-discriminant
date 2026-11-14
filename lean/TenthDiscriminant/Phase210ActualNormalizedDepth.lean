import TenthDiscriminant.RectangularGramFactor
import TenthDiscriminant.Phase210SharpOrdinaryJet

/-!
# Phase210: first quantified depth boundary on the ACTUAL normalized jets

This does NOT construct a second observation model. Every theorem refers
to the existing `rectangularNormalizedJet` of RectangularGramFactor.
The only uniform conclusion proved here is the zero-depth regime j < p^2.
The nontrivial regime j >= p^2 remains an OPEN formal proof obligation;
the source-exact sharp (p=3, j=9) witness lives in
Phase210SharpOrdinaryJet.lean and has its own axiom audit.

A full source theorem requires the integral Taylor-flow statement for
Phase209DeltaCarrier.delta and cancellation of the existing p^k row
factor exactly once. Neither is assumed or smuggled in here.
-/
namespace TenthDiscriminant.Phase210ActualNormalizedDepth

open TenthDiscriminant

/-- Finite form of E_p(j)=sum_{m>=2} floor(j/p^m).  The upper cutoff j+1
is harmless for p>=2, because p^m>j whenever m>j. -/
def taylorDepth (p j : Nat) : Nat :=
  ∑ m ∈ Finset.Ico 2 (j + 1), j / p ^ m

/-- The first nonzero possible Taylor depth is j=p^2. -/
theorem taylorDepth_zero_below_square (p j : Nat)
    (hp : 2 ≤ p) (hj : j < p ^ 2) :
    taylorDepth p j = 0 := by
  unfold taylorDepth
  apply Finset.sum_eq_zero
  intro m hm
  have h2 : 2 ≤ m := (Finset.mem_Ico.mp hm).1
  have hpow : p ^ 2 ≤ p ^ m :=
    pow_le_pow_right₀ (by omega : 1 ≤ p) h2
  exact Nat.div_eq_of_lt (lt_of_lt_of_le hj hpow)

/-- Exact regression: p=3, j=9 is the first nonzero grade, E_3(9)=1.
The stronger source-exact jet witness is audited separately. -/
theorem taylorDepth_three_nine : taylorDepth 3 9 = 1 := by
  decide

/-- The zero-grade part of the user-requested source theorem, quantified
over ALL rows, actual integer-pair samples and ordinary jet depths.
No alternate or abstract matrix is introduced. -/
theorem actual_normalized_jet_depth_below_square
    (D R S p : Nat) (hp : 2 ≤ p)
    (hzero : ∀ a : Int × Int,
      (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2)
    (i : Fin (R * S)) (a : Int × Int) (j : Nat)
    (hj : j < p ^ 2) :
    (p : Int) ^ taylorDepth p j ∣
      (rectangularNormalizedJet D R S p (by omega : 0 < p) hzero i a j).re ∧
    (p : Int) ^ taylorDepth p j ∣
      (rectangularNormalizedJet D R S p (by omega : 0 < p) hzero i a j).im := by
  rw [taylorDepth_zero_below_square p j hp hj]
  simp

end TenthDiscriminant.Phase210ActualNormalizedDepth

#print axioms TenthDiscriminant.Phase210ActualNormalizedDepth.taylorDepth_zero_below_square
#print axioms TenthDiscriminant.Phase210ActualNormalizedDepth.taylorDepth_three_nine
#print axioms TenthDiscriminant.Phase210ActualNormalizedDepth.actual_normalized_jet_depth_below_square
