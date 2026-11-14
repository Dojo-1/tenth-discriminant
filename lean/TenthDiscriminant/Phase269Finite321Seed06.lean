import TenthDiscriminant.Phase269Finite321Seed05

/-! Serialized exact kernel evaluation for one COMPLETE CRT subtree, not a sampled residue. -/
namespace TenthDiscriminant.Phase269
set_option maxRecDepth 5000
set_option maxHeartbeats 0

theorem seed269_6 : seed269 123 = true := by decide +kernel

end TenthDiscriminant.Phase269
