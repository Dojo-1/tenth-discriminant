import TenthDiscriminant.QuotientFiberCheck07

namespace TenthDiscriminant
theorem phase36Entry787_checked : quotientPatternCheck 892371480 phase36Entry787=true := by decide +kernel
theorem phase36Entry797_checked : quotientPatternCheck 892371480 phase36Entry797=true := by decide +kernel
theorem phase36Entry809_checked : quotientPatternCheck 892371480 phase36Entry809=true := by decide +kernel
theorem phase36Entry811_checked : quotientPatternCheck 892371480 phase36Entry811=true := by decide +kernel
theorem phase36Entry821_checked : quotientPatternCheck 892371480 phase36Entry821=true := by decide +kernel
theorem phase36Entry823_checked : quotientPatternCheck 892371480 phase36Entry823=true := by decide +kernel
theorem phase36Entry827_checked : quotientPatternCheck 892371480 phase36Entry827=true := by decide +kernel
theorem phase36Entry829_checked : quotientPatternCheck 892371480 phase36Entry829=true := by decide +kernel
theorem phase36Entry839_checked : quotientPatternCheck 892371480 phase36Entry839=true := by decide +kernel
theorem phase36Entry853_checked : quotientPatternCheck 892371480 phase36Entry853=true := by decide +kernel
theorem phase36Entry857_checked : quotientPatternCheck 892371480 phase36Entry857=true := by decide +kernel
theorem phase36Entry859_checked : quotientPatternCheck 892371480 phase36Entry859=true := by decide +kernel
theorem phase36Entry863_checked : quotientPatternCheck 892371480 phase36Entry863=true := by decide +kernel
theorem phase36Entry877_checked : quotientPatternCheck 892371480 phase36Entry877=true := by decide +kernel
theorem phase36Entry881_checked : quotientPatternCheck 892371480 phase36Entry881=true := by decide +kernel
theorem phase36Entry883_checked : quotientPatternCheck 892371480 phase36Entry883=true := by decide +kernel

theorem phase36Chunk8_checked : quotientPatternsCheck 892371480 phase36Chunk8=true := by
  simp only [quotientPatternsCheck, phase36Chunk8, List.all_cons, List.all_nil, phase36Entry787_checked,phase36Entry797_checked,phase36Entry809_checked,phase36Entry811_checked,phase36Entry821_checked,phase36Entry823_checked,phase36Entry827_checked,phase36Entry829_checked,phase36Entry839_checked,phase36Entry853_checked,phase36Entry857_checked,phase36Entry859_checked,phase36Entry863_checked,phase36Entry877_checked,phase36Entry881_checked,phase36Entry883_checked, Bool.and_self]
end TenthDiscriminant
