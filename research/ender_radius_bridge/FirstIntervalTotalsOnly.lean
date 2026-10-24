import TenthDiscriminant.FirstIntervalData
namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem isolated_budgets :
    (firstRows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧
      7995 * 10 ^ 29 * scale ≤ (firstRows.map (fun r => r.weight * r.lo)).sum := by decide +kernel

theorem isolated_coverage : firstRows.map Row.p = primeList := by decide +kernel

end TenthDiscriminant.FirstCertificate
