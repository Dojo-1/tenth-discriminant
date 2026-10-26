import TenthDiscriminant.FirstIntervalData
namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000
theorem normalized_coverage_pilot :
    firstChunk38.map Row.p =
      (List.range' 9858 143).filter (fun p => decide p.Prime) := by
  norm_num [firstChunk38, List.range', List.filter]
end TenthDiscriminant.FirstCertificate
