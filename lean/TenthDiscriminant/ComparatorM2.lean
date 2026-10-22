import TenthDiscriminant.GramMatrix

/-! Targeted historical M2 follow-up. For P={0,1,2}, R=S=1, J=4,
n=3,L=3,M=1 satisfy the old sufficient guard. The actual matrix is [6].
This does not retroactively change the old uncaught-mutation record. -/
namespace TenthDiscriminant
noncomputable section

theorem comparatorR1_hadamard_equality :
    (traceGramMatrix {0,1,2} 4 (fun _ : Fin 1 => (0,0))).det = 6 := by
  norm_num [Matrix.det_unique, traceGramMatrix, traceGramEntry, derivativeRow,
    Finset.sum_range_succ, Nat.descFactorial]

theorem comparatorR1_M2_rejected :
    (6 : Rat) > 6 / 1000000 := by norm_num

end
end TenthDiscriminant
