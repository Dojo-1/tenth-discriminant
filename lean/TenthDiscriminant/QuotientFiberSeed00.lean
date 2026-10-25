import TenthDiscriminant.QuotientFiberParameters

/-! Complete original-interval fiber check; serialized imports bound memory.
Phase36 accepted seeds0..9; separately registered Phase37 accepted seed10. -/
namespace TenthDiscriminant
theorem phase36_seed_0 : phase36Seed 3=true := by decide +kernel
end TenthDiscriminant
