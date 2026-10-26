import TenthDiscriminant.QuotientFiberCheck09

namespace TenthDiscriminant
theorem phase36Entry1013_checked : quotientPatternCheck 892371480 phase36Entry1013=true := by decide +kernel
theorem phase36Entry1019_checked : quotientPatternCheck 892371480 phase36Entry1019=true := by decide +kernel
theorem phase36Entry1021_checked : quotientPatternCheck 892371480 phase36Entry1021=true := by decide +kernel
theorem phase36Entry1031_checked : quotientPatternCheck 892371480 phase36Entry1031=true := by decide +kernel
theorem phase36Entry1033_checked : quotientPatternCheck 892371480 phase36Entry1033=true := by decide +kernel
theorem phase36Entry1039_checked : quotientPatternCheck 892371480 phase36Entry1039=true := by decide +kernel
theorem phase36Entry1049_checked : quotientPatternCheck 892371480 phase36Entry1049=true := by decide +kernel
theorem phase36Entry1051_checked : quotientPatternCheck 892371480 phase36Entry1051=true := by decide +kernel
theorem phase36Entry1061_checked : quotientPatternCheck 892371480 phase36Entry1061=true := by decide +kernel
theorem phase36Entry1063_checked : quotientPatternCheck 892371480 phase36Entry1063=true := by decide +kernel
theorem phase36Entry1069_checked : quotientPatternCheck 892371480 phase36Entry1069=true := by decide +kernel
theorem phase36Entry1087_checked : quotientPatternCheck 892371480 phase36Entry1087=true := by decide +kernel
theorem phase36Entry1091_checked : quotientPatternCheck 892371480 phase36Entry1091=true := by decide +kernel
theorem phase36Entry1093_checked : quotientPatternCheck 892371480 phase36Entry1093=true := by decide +kernel
theorem phase36Entry1097_checked : quotientPatternCheck 892371480 phase36Entry1097=true := by decide +kernel
theorem phase36Entry1103_checked : quotientPatternCheck 892371480 phase36Entry1103=true := by decide +kernel

theorem phase36Chunk10_checked : quotientPatternsCheck 892371480 phase36Chunk10=true := by
  simp only [quotientPatternsCheck, phase36Chunk10, List.all_cons, List.all_nil, phase36Entry1013_checked,phase36Entry1019_checked,phase36Entry1021_checked,phase36Entry1031_checked,phase36Entry1033_checked,phase36Entry1039_checked,phase36Entry1049_checked,phase36Entry1051_checked,phase36Entry1061_checked,phase36Entry1063_checked,phase36Entry1069_checked,phase36Entry1087_checked,phase36Entry1091_checked,phase36Entry1093_checked,phase36Entry1097_checked,phase36Entry1103_checked, Bool.and_self]
end TenthDiscriminant
