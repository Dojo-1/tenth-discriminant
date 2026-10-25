import TenthDiscriminant.QuotientFiberCheck10

namespace TenthDiscriminant
theorem phase36Entry1109_checked : quotientPatternCheck 892371480 phase36Entry1109=true := by decide +kernel
theorem phase36Entry1117_checked : quotientPatternCheck 892371480 phase36Entry1117=true := by decide +kernel
theorem phase36Entry1123_checked : quotientPatternCheck 892371480 phase36Entry1123=true := by decide +kernel
theorem phase36Entry1129_checked : quotientPatternCheck 892371480 phase36Entry1129=true := by decide +kernel
theorem phase36Entry1151_checked : quotientPatternCheck 892371480 phase36Entry1151=true := by decide +kernel
theorem phase36Entry1153_checked : quotientPatternCheck 892371480 phase36Entry1153=true := by decide +kernel
theorem phase36Entry1163_checked : quotientPatternCheck 892371480 phase36Entry1163=true := by decide +kernel
theorem phase36Entry1171_checked : quotientPatternCheck 892371480 phase36Entry1171=true := by decide +kernel
theorem phase36Entry1181_checked : quotientPatternCheck 892371480 phase36Entry1181=true := by decide +kernel
theorem phase36Entry1187_checked : quotientPatternCheck 892371480 phase36Entry1187=true := by decide +kernel
theorem phase36Entry1193_checked : quotientPatternCheck 892371480 phase36Entry1193=true := by decide +kernel
theorem phase36Entry1201_checked : quotientPatternCheck 892371480 phase36Entry1201=true := by decide +kernel
theorem phase36Entry1213_checked : quotientPatternCheck 892371480 phase36Entry1213=true := by decide +kernel
theorem phase36Entry1217_checked : quotientPatternCheck 892371480 phase36Entry1217=true := by decide +kernel
theorem phase36Entry1223_checked : quotientPatternCheck 892371480 phase36Entry1223=true := by decide +kernel
theorem phase36Entry1229_checked : quotientPatternCheck 892371480 phase36Entry1229=true := by decide +kernel

theorem phase36Chunk11_checked : quotientPatternsCheck 892371480 phase36Chunk11=true := by
  simp only [quotientPatternsCheck, phase36Chunk11, List.all_cons, List.all_nil, phase36Entry1109_checked,phase36Entry1117_checked,phase36Entry1123_checked,phase36Entry1129_checked,phase36Entry1151_checked,phase36Entry1153_checked,phase36Entry1163_checked,phase36Entry1171_checked,phase36Entry1181_checked,phase36Entry1187_checked,phase36Entry1193_checked,phase36Entry1201_checked,phase36Entry1213_checked,phase36Entry1217_checked,phase36Entry1223_checked,phase36Entry1229_checked, Bool.and_self]
end TenthDiscriminant
