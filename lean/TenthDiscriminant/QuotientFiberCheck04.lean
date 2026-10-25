import TenthDiscriminant.QuotientFiberCheck03

namespace TenthDiscriminant
theorem phase36Entry373_checked : quotientPatternCheck 892371480 phase36Entry373=true := by decide +kernel
theorem phase36Entry379_checked : quotientPatternCheck 892371480 phase36Entry379=true := by decide +kernel
theorem phase36Entry383_checked : quotientPatternCheck 892371480 phase36Entry383=true := by decide +kernel
theorem phase36Entry389_checked : quotientPatternCheck 892371480 phase36Entry389=true := by decide +kernel
theorem phase36Entry397_checked : quotientPatternCheck 892371480 phase36Entry397=true := by decide +kernel
theorem phase36Entry401_checked : quotientPatternCheck 892371480 phase36Entry401=true := by decide +kernel
theorem phase36Entry409_checked : quotientPatternCheck 892371480 phase36Entry409=true := by decide +kernel
theorem phase36Entry419_checked : quotientPatternCheck 892371480 phase36Entry419=true := by decide +kernel
theorem phase36Entry421_checked : quotientPatternCheck 892371480 phase36Entry421=true := by decide +kernel
theorem phase36Entry431_checked : quotientPatternCheck 892371480 phase36Entry431=true := by decide +kernel
theorem phase36Entry433_checked : quotientPatternCheck 892371480 phase36Entry433=true := by decide +kernel
theorem phase36Entry439_checked : quotientPatternCheck 892371480 phase36Entry439=true := by decide +kernel
theorem phase36Entry443_checked : quotientPatternCheck 892371480 phase36Entry443=true := by decide +kernel
theorem phase36Entry449_checked : quotientPatternCheck 892371480 phase36Entry449=true := by decide +kernel
theorem phase36Entry457_checked : quotientPatternCheck 892371480 phase36Entry457=true := by decide +kernel
theorem phase36Entry461_checked : quotientPatternCheck 892371480 phase36Entry461=true := by decide +kernel

theorem phase36Chunk4_checked : quotientPatternsCheck 892371480 phase36Chunk4=true := by
  simp only [quotientPatternsCheck, phase36Chunk4, List.all_cons, List.all_nil, phase36Entry373_checked,phase36Entry379_checked,phase36Entry383_checked,phase36Entry389_checked,phase36Entry397_checked,phase36Entry401_checked,phase36Entry409_checked,phase36Entry419_checked,phase36Entry421_checked,phase36Entry431_checked,phase36Entry433_checked,phase36Entry439_checked,phase36Entry443_checked,phase36Entry449_checked,phase36Entry457_checked,phase36Entry461_checked, Bool.and_self]
end TenthDiscriminant
