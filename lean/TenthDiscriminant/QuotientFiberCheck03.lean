import TenthDiscriminant.QuotientFiberCheck02

namespace TenthDiscriminant
theorem phase36Entry271_checked : quotientPatternCheck 892371480 phase36Entry271=true := by decide +kernel
theorem phase36Entry277_checked : quotientPatternCheck 892371480 phase36Entry277=true := by decide +kernel
theorem phase36Entry281_checked : quotientPatternCheck 892371480 phase36Entry281=true := by decide +kernel
theorem phase36Entry283_checked : quotientPatternCheck 892371480 phase36Entry283=true := by decide +kernel
theorem phase36Entry293_checked : quotientPatternCheck 892371480 phase36Entry293=true := by decide +kernel
theorem phase36Entry307_checked : quotientPatternCheck 892371480 phase36Entry307=true := by decide +kernel
theorem phase36Entry311_checked : quotientPatternCheck 892371480 phase36Entry311=true := by decide +kernel
theorem phase36Entry313_checked : quotientPatternCheck 892371480 phase36Entry313=true := by decide +kernel
theorem phase36Entry317_checked : quotientPatternCheck 892371480 phase36Entry317=true := by decide +kernel
theorem phase36Entry331_checked : quotientPatternCheck 892371480 phase36Entry331=true := by decide +kernel
theorem phase36Entry337_checked : quotientPatternCheck 892371480 phase36Entry337=true := by decide +kernel
theorem phase36Entry347_checked : quotientPatternCheck 892371480 phase36Entry347=true := by decide +kernel
theorem phase36Entry349_checked : quotientPatternCheck 892371480 phase36Entry349=true := by decide +kernel
theorem phase36Entry353_checked : quotientPatternCheck 892371480 phase36Entry353=true := by decide +kernel
theorem phase36Entry359_checked : quotientPatternCheck 892371480 phase36Entry359=true := by decide +kernel
theorem phase36Entry367_checked : quotientPatternCheck 892371480 phase36Entry367=true := by decide +kernel

theorem phase36Chunk3_checked : quotientPatternsCheck 892371480 phase36Chunk3=true := by
  simp only [quotientPatternsCheck, phase36Chunk3, List.all_cons, List.all_nil, phase36Entry271_checked,phase36Entry277_checked,phase36Entry281_checked,phase36Entry283_checked,phase36Entry293_checked,phase36Entry307_checked,phase36Entry311_checked,phase36Entry313_checked,phase36Entry317_checked,phase36Entry331_checked,phase36Entry337_checked,phase36Entry347_checked,phase36Entry349_checked,phase36Entry353_checked,phase36Entry359_checked,phase36Entry367_checked, Bool.and_self]
end TenthDiscriminant
