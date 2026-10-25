import TenthDiscriminant.QuotientFiberCheck08

namespace TenthDiscriminant
theorem phase36Entry887_checked : quotientPatternCheck 892371480 phase36Entry887=true := by decide +kernel
theorem phase36Entry907_checked : quotientPatternCheck 892371480 phase36Entry907=true := by decide +kernel
theorem phase36Entry911_checked : quotientPatternCheck 892371480 phase36Entry911=true := by decide +kernel
theorem phase36Entry919_checked : quotientPatternCheck 892371480 phase36Entry919=true := by decide +kernel
theorem phase36Entry929_checked : quotientPatternCheck 892371480 phase36Entry929=true := by decide +kernel
theorem phase36Entry937_checked : quotientPatternCheck 892371480 phase36Entry937=true := by decide +kernel
theorem phase36Entry941_checked : quotientPatternCheck 892371480 phase36Entry941=true := by decide +kernel
theorem phase36Entry947_checked : quotientPatternCheck 892371480 phase36Entry947=true := by decide +kernel
theorem phase36Entry953_checked : quotientPatternCheck 892371480 phase36Entry953=true := by decide +kernel
theorem phase36Entry967_checked : quotientPatternCheck 892371480 phase36Entry967=true := by decide +kernel
theorem phase36Entry971_checked : quotientPatternCheck 892371480 phase36Entry971=true := by decide +kernel
theorem phase36Entry977_checked : quotientPatternCheck 892371480 phase36Entry977=true := by decide +kernel
theorem phase36Entry983_checked : quotientPatternCheck 892371480 phase36Entry983=true := by decide +kernel
theorem phase36Entry991_checked : quotientPatternCheck 892371480 phase36Entry991=true := by decide +kernel
theorem phase36Entry997_checked : quotientPatternCheck 892371480 phase36Entry997=true := by decide +kernel
theorem phase36Entry1009_checked : quotientPatternCheck 892371480 phase36Entry1009=true := by decide +kernel

theorem phase36Chunk9_checked : quotientPatternsCheck 892371480 phase36Chunk9=true := by
  simp only [quotientPatternsCheck, phase36Chunk9, List.all_cons, List.all_nil, phase36Entry887_checked,phase36Entry907_checked,phase36Entry911_checked,phase36Entry919_checked,phase36Entry929_checked,phase36Entry937_checked,phase36Entry941_checked,phase36Entry947_checked,phase36Entry953_checked,phase36Entry967_checked,phase36Entry971_checked,phase36Entry977_checked,phase36Entry983_checked,phase36Entry991_checked,phase36Entry997_checked,phase36Entry1009_checked, Bool.and_self]
end TenthDiscriminant
