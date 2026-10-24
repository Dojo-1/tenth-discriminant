import TenthDiscriminant.FirstIntervalData
namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
theorem probe_prime_9973 : Nat.Prime 9973 := by norm_num
theorem probe_composite_9979 : ¬ Nat.Prime 9979 := by norm_num
end TenthDiscriminant.FirstCertificate
