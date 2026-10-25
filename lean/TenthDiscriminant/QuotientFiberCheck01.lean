import TenthDiscriminant.QuotientFiberCheck00

namespace TenthDiscriminant
theorem phase36Entry101_checked : quotientPatternCheck 892371480 phase36Entry101=true := by decide +kernel
theorem phase36Entry103_checked : quotientPatternCheck 892371480 phase36Entry103=true := by decide +kernel
theorem phase36Entry107_checked : quotientPatternCheck 892371480 phase36Entry107=true := by decide +kernel
theorem phase36Entry109_checked : quotientPatternCheck 892371480 phase36Entry109=true := by decide +kernel
theorem phase36Entry113_checked : quotientPatternCheck 892371480 phase36Entry113=true := by decide +kernel
theorem phase36Entry127_checked : quotientPatternCheck 892371480 phase36Entry127=true := by decide +kernel
theorem phase36Entry131_checked : quotientPatternCheck 892371480 phase36Entry131=true := by decide +kernel
theorem phase36Entry137_checked : quotientPatternCheck 892371480 phase36Entry137=true := by decide +kernel
theorem phase36Entry139_checked : quotientPatternCheck 892371480 phase36Entry139=true := by decide +kernel
theorem phase36Entry149_checked : quotientPatternCheck 892371480 phase36Entry149=true := by decide +kernel
theorem phase36Entry151_checked : quotientPatternCheck 892371480 phase36Entry151=true := by decide +kernel
theorem phase36Entry157_checked : quotientPatternCheck 892371480 phase36Entry157=true := by decide +kernel
theorem phase36Entry163_checked : quotientPatternCheck 892371480 phase36Entry163=true := by decide +kernel
theorem phase36Entry167_checked : quotientPatternCheck 892371480 phase36Entry167=true := by decide +kernel
theorem phase36Entry173_checked : quotientPatternCheck 892371480 phase36Entry173=true := by decide +kernel
theorem phase36Entry179_checked : quotientPatternCheck 892371480 phase36Entry179=true := by decide +kernel

theorem phase36Chunk1_checked : quotientPatternsCheck 892371480 phase36Chunk1=true := by
  simp only [quotientPatternsCheck, phase36Chunk1, List.all_cons, List.all_nil, phase36Entry101_checked,phase36Entry103_checked,phase36Entry107_checked,phase36Entry109_checked,phase36Entry113_checked,phase36Entry127_checked,phase36Entry131_checked,phase36Entry137_checked,phase36Entry139_checked,phase36Entry149_checked,phase36Entry151_checked,phase36Entry157_checked,phase36Entry163_checked,phase36Entry167_checked,phase36Entry173_checked,phase36Entry179_checked, Bool.and_self]
end TenthDiscriminant
