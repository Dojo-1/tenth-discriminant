import TenthDiscriminant.FirstIntervalData

/-! Phase-25 full-table proof attempt; no interval claim until accepted and audited. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem firstChunk00_checked : firstChunk00.all checkRow = true := by decide +kernel

theorem firstChunk01_checked : firstChunk01.all checkRow = true := by decide +kernel

theorem firstChunk02_checked : firstChunk02.all checkRow = true := by decide +kernel

theorem firstChunk03_checked : firstChunk03.all checkRow = true := by decide +kernel

theorem firstChunk04_checked : firstChunk04.all checkRow = true := by decide +kernel

theorem firstChunk05_checked : firstChunk05.all checkRow = true := by decide +kernel

theorem firstChunk06_checked : firstChunk06.all checkRow = true := by decide +kernel

theorem firstChunk07_checked : firstChunk07.all checkRow = true := by decide +kernel

theorem firstChunk08_checked : firstChunk08.all checkRow = true := by decide +kernel

theorem firstChunk09_checked : firstChunk09.all checkRow = true := by decide +kernel

theorem firstChunk10_checked : firstChunk10.all checkRow = true := by decide +kernel

theorem firstChunk11_checked : firstChunk11.all checkRow = true := by decide +kernel

theorem firstChunk12_checked : firstChunk12.all checkRow = true := by decide +kernel

theorem firstChunk13_checked : firstChunk13.all checkRow = true := by decide +kernel

theorem firstChunk14_checked : firstChunk14.all checkRow = true := by decide +kernel

theorem firstChunk15_checked : firstChunk15.all checkRow = true := by decide +kernel

theorem firstChunk16_checked : firstChunk16.all checkRow = true := by decide +kernel

theorem firstChunk17_checked : firstChunk17.all checkRow = true := by decide +kernel

theorem firstChunk18_checked : firstChunk18.all checkRow = true := by decide +kernel

theorem firstChunk19_checked : firstChunk19.all checkRow = true := by decide +kernel

theorem firstChunk20_checked : firstChunk20.all checkRow = true := by decide +kernel

theorem firstChunk21_checked : firstChunk21.all checkRow = true := by decide +kernel

theorem firstChunk22_checked : firstChunk22.all checkRow = true := by decide +kernel

theorem firstChunk23_checked : firstChunk23.all checkRow = true := by decide +kernel

theorem firstChunk24_checked : firstChunk24.all checkRow = true := by decide +kernel

theorem firstChunk25_checked : firstChunk25.all checkRow = true := by decide +kernel

theorem firstChunk26_checked : firstChunk26.all checkRow = true := by decide +kernel

theorem firstChunk27_checked : firstChunk27.all checkRow = true := by decide +kernel

theorem firstChunk28_checked : firstChunk28.all checkRow = true := by decide +kernel

theorem firstChunk29_checked : firstChunk29.all checkRow = true := by decide +kernel

theorem firstChunk30_checked : firstChunk30.all checkRow = true := by decide +kernel

theorem firstChunk31_checked : firstChunk31.all checkRow = true := by decide +kernel

theorem firstChunk32_checked : firstChunk32.all checkRow = true := by decide +kernel

theorem firstChunk33_checked : firstChunk33.all checkRow = true := by decide +kernel

theorem firstChunk34_checked : firstChunk34.all checkRow = true := by decide +kernel

theorem firstChunk35_checked : firstChunk35.all checkRow = true := by decide +kernel

theorem firstChunk36_checked : firstChunk36.all checkRow = true := by decide +kernel

theorem firstChunk37_checked : firstChunk37.all checkRow = true := by decide +kernel

theorem firstChunk38_checked : firstChunk38.all checkRow = true := by decide +kernel

theorem first_rows_checked : firstRows.all checkRow = true := by
  rw [firstRows, List.all_flatten]
  apply List.all_eq_true.mpr
  intro chunk hmem
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
  rcases hmem with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact firstChunk00_checked
  · exact firstChunk01_checked
  · exact firstChunk02_checked
  · exact firstChunk03_checked
  · exact firstChunk04_checked
  · exact firstChunk05_checked
  · exact firstChunk06_checked
  · exact firstChunk07_checked
  · exact firstChunk08_checked
  · exact firstChunk09_checked
  · exact firstChunk10_checked
  · exact firstChunk11_checked
  · exact firstChunk12_checked
  · exact firstChunk13_checked
  · exact firstChunk14_checked
  · exact firstChunk15_checked
  · exact firstChunk16_checked
  · exact firstChunk17_checked
  · exact firstChunk18_checked
  · exact firstChunk19_checked
  · exact firstChunk20_checked
  · exact firstChunk21_checked
  · exact firstChunk22_checked
  · exact firstChunk23_checked
  · exact firstChunk24_checked
  · exact firstChunk25_checked
  · exact firstChunk26_checked
  · exact firstChunk27_checked
  · exact firstChunk28_checked
  · exact firstChunk29_checked
  · exact firstChunk30_checked
  · exact firstChunk31_checked
  · exact firstChunk32_checked
  · exact firstChunk33_checked
  · exact firstChunk34_checked
  · exact firstChunk35_checked
  · exact firstChunk36_checked
  · exact firstChunk37_checked
  · exact firstChunk38_checked

end TenthDiscriminant.FirstCertificate
