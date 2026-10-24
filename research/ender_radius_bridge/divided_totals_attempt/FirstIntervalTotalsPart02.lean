import TenthDiscriminant.FirstIntervalData

namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem firstChunk20_totals :
    (firstChunk20.map (fun r => r.coefficient * r.hi)).sum = 850227111316045708233530622336748 ∧
      (firstChunk20.map (fun r => r.weight * r.lo)).sum = 7427841254456241386074299948182848636502360 := by
  norm_num [firstChunk20, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk20_coverage : firstChunk20.map Row.p =
    (List.range' 4752 260).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk21_totals :
    (firstChunk21.map (fun r => r.coefficient * r.hi)).sum = 811276221592627141455505016975759 ∧
      (firstChunk21.map (fun r => r.weight * r.lo)).sum = 7088129035671811067027149812253869974367977 := by
  norm_num [firstChunk21, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk21_coverage : firstChunk21.map Row.p =
    (List.range' 5012 298).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk22_totals :
    (firstChunk22.map (fun r => r.coefficient * r.hi)).sum = 773166196784320555761804755738917 ∧
      (firstChunk22.map (fun r => r.weight * r.lo)).sum = 6755694652938764740401587550164873601510909 := by
  norm_num [firstChunk22, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk22_coverage : firstChunk22.map Row.p =
    (List.range' 5310 264).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk23_totals :
    (firstChunk23.map (fun r => r.coefficient * r.hi)).sum = 741070399472647105133750095731105 ∧
      (firstChunk23.map (fun r => r.weight * r.lo)).sum = 6475677739629609346943364778172346266969384 := by
  norm_num [firstChunk23, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk23_coverage : firstChunk23.map Row.p =
    (List.range' 5574 276).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk24_totals :
    (firstChunk24.map (fun r => r.coefficient * r.hi)).sum = 711376301954346706766920844535310 ∧
      (firstChunk24.map (fun r => r.weight * r.lo)).sum = 6216578683170144117183975498854052546659457 := by
  norm_num [firstChunk24, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk24_coverage : firstChunk24.map Row.p =
    (List.range' 5850 284).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk25_totals :
    (firstChunk25.map (fun r => r.coefficient * r.hi)).sum = 683213209862809227698074453292156 ∧
      (firstChunk25.map (fun r => r.weight * r.lo)).sum = 5970808778870185877333745313329560468857866 := by
  norm_num [firstChunk25, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk25_coverage : firstChunk25.map Row.p =
    (List.range' 6134 246).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk26_totals :
    (firstChunk26.map (fun r => r.coefficient * r.hi)).sum = 656800053768479415398302699383409 ∧
      (firstChunk26.map (fun r => r.weight * r.lo)).sum = 5740281347923066187212773788376773771490513 := by
  norm_num [firstChunk26, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk26_coverage : firstChunk26.map Row.p =
    (List.range' 6380 322).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk27_totals :
    (firstChunk27.map (fun r => r.coefficient * r.hi)).sum = 632567733944238960602794460307178 ∧
      (firstChunk27.map (fun r => r.weight * r.lo)).sum = 5528765408954364874543715472289956198013751 := by
  norm_num [firstChunk27, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk27_coverage : firstChunk27.map Row.p =
    (List.range' 6702 270).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk28_totals :
    (firstChunk28.map (fun r => r.coefficient * r.hi)).sum = 610719854577816850342577953539371 ∧
      (firstChunk28.map (fun r => r.weight * r.lo)).sum = 5338043146123370655726909503599407967063785 := by
  norm_num [firstChunk28, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk28_coverage : firstChunk28.map Row.p =
    (List.range' 6972 282).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk29_totals :
    (firstChunk29.map (fun r => r.coefficient * r.hi)).sum = 587280743915250339109244403392396 ∧
      (firstChunk29.map (fun r => r.weight * r.lo)).sum = 5133410610554469398748822370837646988493888 := by
  norm_num [firstChunk29, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk29_coverage : firstChunk29.map Row.p =
    (List.range' 7254 308).filter (fun p => decide p.Prime) := by decide +kernel

end TenthDiscriminant.FirstCertificate
