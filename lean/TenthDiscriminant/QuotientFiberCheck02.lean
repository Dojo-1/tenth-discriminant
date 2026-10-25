import TenthDiscriminant.QuotientFiberCheck01

namespace TenthDiscriminant
theorem phase36Entry181_checked : quotientPatternCheck 892371480 phase36Entry181=true := by decide +kernel
theorem phase36Entry191_checked : quotientPatternCheck 892371480 phase36Entry191=true := by decide +kernel
theorem phase36Entry193_checked : quotientPatternCheck 892371480 phase36Entry193=true := by decide +kernel
theorem phase36Entry197_checked : quotientPatternCheck 892371480 phase36Entry197=true := by decide +kernel
theorem phase36Entry199_checked : quotientPatternCheck 892371480 phase36Entry199=true := by decide +kernel
theorem phase36Entry211_checked : quotientPatternCheck 892371480 phase36Entry211=true := by decide +kernel
theorem phase36Entry223_checked : quotientPatternCheck 892371480 phase36Entry223=true := by decide +kernel
theorem phase36Entry227_checked : quotientPatternCheck 892371480 phase36Entry227=true := by decide +kernel
theorem phase36Entry229_checked : quotientPatternCheck 892371480 phase36Entry229=true := by decide +kernel
theorem phase36Entry233_checked : quotientPatternCheck 892371480 phase36Entry233=true := by decide +kernel
theorem phase36Entry239_checked : quotientPatternCheck 892371480 phase36Entry239=true := by decide +kernel
theorem phase36Entry241_checked : quotientPatternCheck 892371480 phase36Entry241=true := by decide +kernel
theorem phase36Entry251_checked : quotientPatternCheck 892371480 phase36Entry251=true := by decide +kernel
theorem phase36Entry257_checked : quotientPatternCheck 892371480 phase36Entry257=true := by decide +kernel
theorem phase36Entry263_checked : quotientPatternCheck 892371480 phase36Entry263=true := by decide +kernel
theorem phase36Entry269_checked : quotientPatternCheck 892371480 phase36Entry269=true := by decide +kernel

theorem phase36Chunk2_checked : quotientPatternsCheck 892371480 phase36Chunk2=true := by
  simp only [quotientPatternsCheck, phase36Chunk2, List.all_cons, List.all_nil, phase36Entry181_checked,phase36Entry191_checked,phase36Entry193_checked,phase36Entry197_checked,phase36Entry199_checked,phase36Entry211_checked,phase36Entry223_checked,phase36Entry227_checked,phase36Entry229_checked,phase36Entry233_checked,phase36Entry239_checked,phase36Entry241_checked,phase36Entry251_checked,phase36Entry257_checked,phase36Entry263_checked,phase36Entry269_checked, Bool.and_self]
end TenthDiscriminant
