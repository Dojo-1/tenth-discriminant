import TenthDiscriminant.QuotientFiberCheck12
import TenthDiscriminant.QuotientFiberBridge

namespace TenthDiscriminant
theorem phase36_entries_split : phase36Entries=phase36Chunk0++phase36Chunk1++phase36Chunk2++phase36Chunk3++phase36Chunk4++phase36Chunk5++phase36Chunk6++phase36Chunk7++phase36Chunk8++phase36Chunk9++phase36Chunk10++phase36Chunk11++phase36Chunk12 := by rfl
theorem phase36_patterns_checked : quotientPatternsCheck 892371480 phase36Entries=true := by
  rw [phase36_entries_split]
  simp only [quotientPatternsCheck_append, phase36Chunk0_checked,phase36Chunk1_checked,phase36Chunk2_checked,phase36Chunk3_checked,phase36Chunk4_checked,phase36Chunk5_checked,phase36Chunk6_checked,phase36Chunk7_checked,phase36Chunk8_checked,phase36Chunk9_checked,phase36Chunk10_checked,phase36Chunk11_checked,phase36Chunk12_checked, Bool.and_self]
end TenthDiscriminant
