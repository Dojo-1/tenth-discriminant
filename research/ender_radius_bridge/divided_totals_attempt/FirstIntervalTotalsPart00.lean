import TenthDiscriminant.FirstIntervalData

namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem firstChunk00_totals :
    (firstChunk00.map (fun r => r.coefficient * r.hi)).sum = 67561225440454988426839658269495352 ∧
      (firstChunk00.map (fun r => r.weight * r.lo)).sum = 239650526867966420224193235049417986686432969 := by
  norm_num [firstChunk00, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk00_coverage : firstChunk00.map Row.p =
    (List.range' 0 132).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk01_totals :
    (firstChunk01.map (fun r => r.coefficient * r.hi)).sum = 12579661638912910081684887264340740 ∧
      (firstChunk01.map (fun r => r.weight * r.lo)).sum = 105829716620152198096538221158276777239681834 := by
  norm_num [firstChunk01, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk01_coverage : firstChunk01.map Row.p =
    (List.range' 132 180).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk02_totals :
    (firstChunk02.map (fun r => r.coefficient * r.hi)).sum = 7298105669251003309637858344651769 ∧
      (firstChunk02.map (fun r => r.weight * r.lo)).sum = 62627304352535188262422670568626295433677071 := by
  norm_num [firstChunk02, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk02_coverage : firstChunk02.map Row.p =
    (List.range' 312 192).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk03_totals :
    (firstChunk03.map (fun r => r.coefficient * r.hi)).sum = 5154644360269511318428252685383642 ∧
      (firstChunk03.map (fun r => r.weight * r.lo)).sum = 44533081700909836388108263718876106801062965 := by
  norm_num [firstChunk03, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk03_coverage : firstChunk03.map Row.p =
    (List.range' 504 216).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk04_totals :
    (firstChunk04.map (fun r => r.coefficient * r.hi)).sum = 3986235248840927489875445611316924 ∧
      (firstChunk04.map (fun r => r.weight * r.lo)).sum = 34554632241178547759827527228658389121539388 := by
  norm_num [firstChunk04, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk04_coverage : firstChunk04.map Row.p =
    (List.range' 720 222).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk05_totals :
    (firstChunk05.map (fun r => r.coefficient * r.hi)).sum = 3253071751049236310597257353539378 ∧
      (firstChunk05.map (fun r => r.weight * r.lo)).sum = 28255793273143672223190600056101826518214628 := by
  norm_num [firstChunk05, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk05_coverage : firstChunk05.map Row.p =
    (List.range' 942 222).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk06_totals :
    (firstChunk06.map (fun r => r.coefficient * r.hi)).sum = 2739413924310840739573219165977850 ∧
      (firstChunk06.map (fun r => r.weight * r.lo)).sum = 23826107508491398845750559205888229426958173 := by
  norm_num [firstChunk06, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk06_coverage : firstChunk06.map Row.p =
    (List.range' 1164 260).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk07_totals :
    (firstChunk07.map (fun r => r.coefficient * r.hi)).sum = 2365776020604245997761040502240338 ∧
      (firstChunk07.map (fun r => r.weight * r.lo)).sum = 20595906783638551377297686617252240621564521 := by
  norm_num [firstChunk07, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk07_coverage : firstChunk07.map Row.p =
    (List.range' 1424 196).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk08_totals :
    (firstChunk08.map (fun r => r.coefficient * r.hi)).sum = 2091616612276976100448183709600479 ∧
      (firstChunk08.map (fun r => r.weight * r.lo)).sum = 18221379919305146222180191021882541928366611 := by
  norm_num [firstChunk08, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk08_coverage : firstChunk08.map Row.p =
    (List.range' 1620 258).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk09_totals :
    (firstChunk09.map (fun r => r.coefficient * r.hi)).sum = 1857877549159664363932068351330033 ∧
      (firstChunk09.map (fun r => r.weight * r.lo)).sum = 16194268268327419716421198733248698937059679 := by
  norm_num [firstChunk09, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk09_coverage : firstChunk09.map Row.p =
    (List.range' 1878 252).filter (fun p => decide p.Prime) := by decide +kernel

end TenthDiscriminant.FirstCertificate
