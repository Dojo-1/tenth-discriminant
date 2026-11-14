import TenthDiscriminant.Phase269Finite321Sound

/-! Serialized exact kernel evaluation for one COMPLETE CRT subtree, not a sampled residue. -/
namespace TenthDiscriminant.Phase269
set_option maxRecDepth 5000
set_option maxHeartbeats 0

theorem seed269_0 : seed269 11 = true := by decide +kernel

end TenthDiscriminant.Phase269
