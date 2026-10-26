import TenthDiscriminant.FirstIntervalData
namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem block_pilot_totals :
    (firstChunk00.map (fun r => r.coefficient * r.hi)).sum = 67561225440454988426839658269495352 ∧
      (firstChunk00.map (fun r => r.weight * r.lo)).sum = 239650526867966420224193235049417986686432969 := by
  norm_num [firstChunk00, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem block_pilot_coverage : firstChunk00.map Row.p =
    (List.range' 0 132).filter (fun p => decide p.Prime) := by decide +kernel

end TenthDiscriminant.FirstCertificate
