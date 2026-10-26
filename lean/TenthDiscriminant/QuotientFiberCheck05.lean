import TenthDiscriminant.QuotientFiberCheck04

namespace TenthDiscriminant
theorem phase36Entry463_checked : quotientPatternCheck 892371480 phase36Entry463=true := by decide +kernel
theorem phase36Entry467_checked : quotientPatternCheck 892371480 phase36Entry467=true := by decide +kernel
theorem phase36Entry479_checked : quotientPatternCheck 892371480 phase36Entry479=true := by decide +kernel
theorem phase36Entry487_checked : quotientPatternCheck 892371480 phase36Entry487=true := by decide +kernel
theorem phase36Entry491_checked : quotientPatternCheck 892371480 phase36Entry491=true := by decide +kernel
theorem phase36Entry499_checked : quotientPatternCheck 892371480 phase36Entry499=true := by decide +kernel
theorem phase36Entry503_checked : quotientPatternCheck 892371480 phase36Entry503=true := by decide +kernel
theorem phase36Entry509_checked : quotientPatternCheck 892371480 phase36Entry509=true := by decide +kernel
theorem phase36Entry521_checked : quotientPatternCheck 892371480 phase36Entry521=true := by decide +kernel
theorem phase36Entry523_checked : quotientPatternCheck 892371480 phase36Entry523=true := by decide +kernel
theorem phase36Entry541_checked : quotientPatternCheck 892371480 phase36Entry541=true := by decide +kernel
theorem phase36Entry547_checked : quotientPatternCheck 892371480 phase36Entry547=true := by decide +kernel
theorem phase36Entry557_checked : quotientPatternCheck 892371480 phase36Entry557=true := by decide +kernel
theorem phase36Entry563_checked : quotientPatternCheck 892371480 phase36Entry563=true := by decide +kernel
theorem phase36Entry569_checked : quotientPatternCheck 892371480 phase36Entry569=true := by decide +kernel
theorem phase36Entry571_checked : quotientPatternCheck 892371480 phase36Entry571=true := by decide +kernel

theorem phase36Chunk5_checked : quotientPatternsCheck 892371480 phase36Chunk5=true := by
  simp only [quotientPatternsCheck, phase36Chunk5, List.all_cons, List.all_nil, phase36Entry463_checked,phase36Entry467_checked,phase36Entry479_checked,phase36Entry487_checked,phase36Entry491_checked,phase36Entry499_checked,phase36Entry503_checked,phase36Entry509_checked,phase36Entry521_checked,phase36Entry523_checked,phase36Entry541_checked,phase36Entry547_checked,phase36Entry557_checked,phase36Entry563_checked,phase36Entry569_checked,phase36Entry571_checked, Bool.and_self]
end TenthDiscriminant
