import TenthDiscriminant.Phase269Finite321Seed01

/-! Serialized exact kernel evaluation for one COMPLETE CRT subtree, not a sampled residue. -/
namespace TenthDiscriminant.Phase269
set_option maxRecDepth 5000
set_option maxHeartbeats 0

theorem seed269_2 : seed269 43 = true := by decide +kernel

end TenthDiscriminant.Phase269
