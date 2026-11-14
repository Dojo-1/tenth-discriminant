import TenthDiscriminant.Phase269Finite321Seed03

/-! Serialized exact kernel evaluation for one COMPLETE CRT subtree, not a sampled residue. -/
namespace TenthDiscriminant.Phase269
set_option maxRecDepth 5000
set_option maxHeartbeats 0

theorem seed269_4 : seed269 99 = true := by decide +kernel

end TenthDiscriminant.Phase269
