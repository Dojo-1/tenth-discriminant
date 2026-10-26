import TenthDiscriminant.QuotientFiberData

namespace TenthDiscriminant
theorem phase36Entry29_checked : quotientPatternCheck 892371480 phase36Entry29=true := by decide +kernel
theorem phase36Entry31_checked : quotientPatternCheck 892371480 phase36Entry31=true := by decide +kernel
theorem phase36Entry37_checked : quotientPatternCheck 892371480 phase36Entry37=true := by decide +kernel
theorem phase36Entry41_checked : quotientPatternCheck 892371480 phase36Entry41=true := by decide +kernel
theorem phase36Entry43_checked : quotientPatternCheck 892371480 phase36Entry43=true := by decide +kernel
theorem phase36Entry47_checked : quotientPatternCheck 892371480 phase36Entry47=true := by decide +kernel
theorem phase36Entry53_checked : quotientPatternCheck 892371480 phase36Entry53=true := by decide +kernel
theorem phase36Entry59_checked : quotientPatternCheck 892371480 phase36Entry59=true := by decide +kernel
theorem phase36Entry61_checked : quotientPatternCheck 892371480 phase36Entry61=true := by decide +kernel
theorem phase36Entry67_checked : quotientPatternCheck 892371480 phase36Entry67=true := by decide +kernel
theorem phase36Entry71_checked : quotientPatternCheck 892371480 phase36Entry71=true := by decide +kernel
theorem phase36Entry73_checked : quotientPatternCheck 892371480 phase36Entry73=true := by decide +kernel
theorem phase36Entry79_checked : quotientPatternCheck 892371480 phase36Entry79=true := by decide +kernel
theorem phase36Entry83_checked : quotientPatternCheck 892371480 phase36Entry83=true := by decide +kernel
theorem phase36Entry89_checked : quotientPatternCheck 892371480 phase36Entry89=true := by decide +kernel
theorem phase36Entry97_checked : quotientPatternCheck 892371480 phase36Entry97=true := by decide +kernel

theorem phase36Chunk0_checked : quotientPatternsCheck 892371480 phase36Chunk0=true := by
  simp only [quotientPatternsCheck, phase36Chunk0, List.all_cons, List.all_nil, phase36Entry29_checked,phase36Entry31_checked,phase36Entry37_checked,phase36Entry41_checked,phase36Entry43_checked,phase36Entry47_checked,phase36Entry53_checked,phase36Entry59_checked,phase36Entry61_checked,phase36Entry67_checked,phase36Entry71_checked,phase36Entry73_checked,phase36Entry79_checked,phase36Entry83_checked,phase36Entry89_checked,phase36Entry97_checked, Bool.and_self]
end TenthDiscriminant
