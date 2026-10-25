import TenthDiscriminant.QuotientFiberCheck05

namespace TenthDiscriminant
theorem phase36Entry577_checked : quotientPatternCheck 892371480 phase36Entry577=true := by decide +kernel
theorem phase36Entry587_checked : quotientPatternCheck 892371480 phase36Entry587=true := by decide +kernel
theorem phase36Entry593_checked : quotientPatternCheck 892371480 phase36Entry593=true := by decide +kernel
theorem phase36Entry599_checked : quotientPatternCheck 892371480 phase36Entry599=true := by decide +kernel
theorem phase36Entry601_checked : quotientPatternCheck 892371480 phase36Entry601=true := by decide +kernel
theorem phase36Entry607_checked : quotientPatternCheck 892371480 phase36Entry607=true := by decide +kernel
theorem phase36Entry613_checked : quotientPatternCheck 892371480 phase36Entry613=true := by decide +kernel
theorem phase36Entry617_checked : quotientPatternCheck 892371480 phase36Entry617=true := by decide +kernel
theorem phase36Entry619_checked : quotientPatternCheck 892371480 phase36Entry619=true := by decide +kernel
theorem phase36Entry631_checked : quotientPatternCheck 892371480 phase36Entry631=true := by decide +kernel
theorem phase36Entry641_checked : quotientPatternCheck 892371480 phase36Entry641=true := by decide +kernel
theorem phase36Entry643_checked : quotientPatternCheck 892371480 phase36Entry643=true := by decide +kernel
theorem phase36Entry647_checked : quotientPatternCheck 892371480 phase36Entry647=true := by decide +kernel
theorem phase36Entry653_checked : quotientPatternCheck 892371480 phase36Entry653=true := by decide +kernel
theorem phase36Entry659_checked : quotientPatternCheck 892371480 phase36Entry659=true := by decide +kernel
theorem phase36Entry661_checked : quotientPatternCheck 892371480 phase36Entry661=true := by decide +kernel

theorem phase36Chunk6_checked : quotientPatternsCheck 892371480 phase36Chunk6=true := by
  simp only [quotientPatternsCheck, phase36Chunk6, List.all_cons, List.all_nil, phase36Entry577_checked,phase36Entry587_checked,phase36Entry593_checked,phase36Entry599_checked,phase36Entry601_checked,phase36Entry607_checked,phase36Entry613_checked,phase36Entry617_checked,phase36Entry619_checked,phase36Entry631_checked,phase36Entry641_checked,phase36Entry643_checked,phase36Entry647_checked,phase36Entry653_checked,phase36Entry659_checked,phase36Entry661_checked, Bool.and_self]
end TenthDiscriminant
