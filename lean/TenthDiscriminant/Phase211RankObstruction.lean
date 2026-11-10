import TenthDiscriminant.IntegerTraceGram

/-!
# Phase211 — finite ordinary-derivative budget of the actual source

Every original row has exponent r<R in Z. Its ordinary Z-jet is zero
at j>=R, independent of the integer-pair sample a, quadratic parameter
D and the W exponent s. Thus adding derivative orders j>=R yields
NO new observation columns. This is the source-specific zero-column
ingredient for the paper rank obstruction:

  rank G <= |Q| * min(J,R).
  det G > 0 => R*S <= |Q| * min(J,R).

The rank lemma itself is NOT proved here; it needs an explicit real
folded rectangular observation matrix and a matrix-rank argument.
The original thin count |Q|<=31D/50 is a separate paper inequality.
No class-number or analytic input is imported.
-/
namespace TenthDiscriminant.Phase211RankObstruction

open TenthDiscriminant

/-- Every original ordinary derivative at order >=R vanishes on EVERY
source row (r,s) of the original R-by-S polynomial rectangle. -/
theorem original_rectangular_jet_zero_of_large_depth
    (D R S : Nat) (i : Fin (R * S)) (a : Int × Int)
    (j : Nat) (hj : R ≤ j) :
    integerDerivativeRow D (i.val / S) (i.val % S) j a = (0, 0) := by
  have hS : 0 < S := by
    by_contra h
    have hzero : S = 0 := by omega
    have hi := i.isLt
    simp [hzero] at hi
  have hr : i.val / S < R := by
    apply (Nat.div_lt_iff_lt_mul hS).2
    simpa only [Nat.mul_comm] using i.isLt
  have hnot : ¬ j ≤ i.val / S := by omega
  simp only [integerDerivativeRow, if_neg hnot]

end TenthDiscriminant.Phase211RankObstruction

#print axioms TenthDiscriminant.Phase211RankObstruction.original_rectangular_jet_zero_of_large_depth
