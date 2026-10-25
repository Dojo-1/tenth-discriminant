import TenthDiscriminant.QuotientFiberCheck11

namespace TenthDiscriminant
theorem phase36Entry1231_checked : quotientPatternCheck 892371480 phase36Entry1231=true := by decide +kernel
theorem phase36Entry1237_checked : quotientPatternCheck 892371480 phase36Entry1237=true := by decide +kernel
theorem phase36Entry1249_checked : quotientPatternCheck 892371480 phase36Entry1249=true := by decide +kernel
theorem phase36Entry1259_checked : quotientPatternCheck 892371480 phase36Entry1259=true := by decide +kernel
theorem phase36Entry1277_checked : quotientPatternCheck 892371480 phase36Entry1277=true := by decide +kernel
theorem phase36Entry1279_checked : quotientPatternCheck 892371480 phase36Entry1279=true := by decide +kernel
theorem phase36Entry1283_checked : quotientPatternCheck 892371480 phase36Entry1283=true := by decide +kernel
theorem phase36Entry1289_checked : quotientPatternCheck 892371480 phase36Entry1289=true := by decide +kernel

theorem phase36Chunk12_checked : quotientPatternsCheck 892371480 phase36Chunk12=true := by
  simp only [quotientPatternsCheck, phase36Chunk12, List.all_cons, List.all_nil, phase36Entry1231_checked,phase36Entry1237_checked,phase36Entry1249_checked,phase36Entry1259_checked,phase36Entry1277_checked,phase36Entry1279_checked,phase36Entry1283_checked,phase36Entry1289_checked, Bool.and_self]
end TenthDiscriminant
