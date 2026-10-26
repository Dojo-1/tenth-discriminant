import TenthDiscriminant.QuotientFiberCheck06

namespace TenthDiscriminant
theorem phase36Entry673_checked : quotientPatternCheck 892371480 phase36Entry673=true := by decide +kernel
theorem phase36Entry677_checked : quotientPatternCheck 892371480 phase36Entry677=true := by decide +kernel
theorem phase36Entry683_checked : quotientPatternCheck 892371480 phase36Entry683=true := by decide +kernel
theorem phase36Entry691_checked : quotientPatternCheck 892371480 phase36Entry691=true := by decide +kernel
theorem phase36Entry701_checked : quotientPatternCheck 892371480 phase36Entry701=true := by decide +kernel
theorem phase36Entry709_checked : quotientPatternCheck 892371480 phase36Entry709=true := by decide +kernel
theorem phase36Entry719_checked : quotientPatternCheck 892371480 phase36Entry719=true := by decide +kernel
theorem phase36Entry727_checked : quotientPatternCheck 892371480 phase36Entry727=true := by decide +kernel
theorem phase36Entry733_checked : quotientPatternCheck 892371480 phase36Entry733=true := by decide +kernel
theorem phase36Entry739_checked : quotientPatternCheck 892371480 phase36Entry739=true := by decide +kernel
theorem phase36Entry743_checked : quotientPatternCheck 892371480 phase36Entry743=true := by decide +kernel
theorem phase36Entry751_checked : quotientPatternCheck 892371480 phase36Entry751=true := by decide +kernel
theorem phase36Entry757_checked : quotientPatternCheck 892371480 phase36Entry757=true := by decide +kernel
theorem phase36Entry761_checked : quotientPatternCheck 892371480 phase36Entry761=true := by decide +kernel
theorem phase36Entry769_checked : quotientPatternCheck 892371480 phase36Entry769=true := by decide +kernel
theorem phase36Entry773_checked : quotientPatternCheck 892371480 phase36Entry773=true := by decide +kernel

theorem phase36Chunk7_checked : quotientPatternsCheck 892371480 phase36Chunk7=true := by
  simp only [quotientPatternsCheck, phase36Chunk7, List.all_cons, List.all_nil, phase36Entry673_checked,phase36Entry677_checked,phase36Entry683_checked,phase36Entry691_checked,phase36Entry701_checked,phase36Entry709_checked,phase36Entry719_checked,phase36Entry727_checked,phase36Entry733_checked,phase36Entry739_checked,phase36Entry743_checked,phase36Entry751_checked,phase36Entry757_checked,phase36Entry761_checked,phase36Entry769_checked,phase36Entry773_checked, Bool.and_self]
end TenthDiscriminant
