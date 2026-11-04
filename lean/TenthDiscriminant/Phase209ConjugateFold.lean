import TenthDiscriminant.IntegerTraceGram

/-!
Phase209 — exact algebraic local identity behind conjugate folding.

These are ABOUT the repository's original integerPairTrace, pairConj
and original integer-pair coordinate metric. They do not assert a
row-transformed whole-Gram equality or establish derivative-order
divisibility. Such a full source-indexed Gram bridge is still required.
-/
namespace TenthDiscriminant.Phase209ConjugateFold

open TenthDiscriminant

/-- The original trace pairing is preserved under conjugating BOTH
integer-pair entries, with no change in metric. -/
theorem original_trace_conjugate (D : Nat) (a b : Int × Int) :
    integerPairTrace D (pairConj a) (pairConj b) =
      integerPairTrace D a b := by
  simp only [integerPairTrace, pairConj]
  ring

/-- An exact nonreal conjugate pair of observations has ONE effective
real coordinate of weight 4 and ONE imaginary coordinate of weight 4D.
This is an integral identity with NO square-root or division factors. -/
theorem original_trace_pair_fold (D : Nat) (a b : Int × Int) :
    integerPairTrace D a b +
      integerPairTrace D (pairConj a) (pairConj b) =
      4 * a.1 * b.1 + (4*(D : Int)) * a.2 * b.2 := by
  simp only [integerPairTrace, pairConj]
  ring

/-- At a real sample the source imaginary coordinate is zero, leaving
the unchanged original metric weight 2 (not 4). -/
theorem original_trace_real_sample (D : Nat) (x y : Int) :
    integerPairTrace D (x, 0) (y, 0) = 2*x*y := by
  simp [integerPairTrace]

end TenthDiscriminant.Phase209ConjugateFold

#print axioms TenthDiscriminant.Phase209ConjugateFold.original_trace_pair_fold
