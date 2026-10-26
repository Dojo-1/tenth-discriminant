import TenthDiscriminant.FirstIntervalData

namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem firstChunk10_totals :
    (firstChunk10.map (fun r => r.coefficient * r.hi)).sum = 1677870334517081197174776954567288 ∧
      (firstChunk10.map (fun r => r.weight * r.lo)).sum = 14631438822491711992790264975214510045196726 := by
  norm_num [firstChunk10, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk10_coverage : firstChunk10.map Row.p =
    (List.range' 2130 248).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk11_totals :
    (firstChunk11.map (fun r => r.coefficient * r.hi)).sum = 1531601603426514284138916141682120 ∧
      (firstChunk11.map (fun r => r.weight * r.lo)).sum = 13360463021365323819431641959063490851110891 := by
  norm_num [firstChunk11, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk11_coverage : firstChunk11.map Row.p =
    (List.range' 2378 280).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk12_totals :
    (firstChunk12.map (fun r => r.coefficient * r.hi)).sum = 1410787103995001323609611487309722 ∧
      (firstChunk12.map (fun r => r.weight * r.lo)).sum = 12309989705068867993585851913455314249813099 := by
  norm_num [firstChunk12, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk12_coverage : firstChunk12.map Row.p =
    (List.range' 2658 204).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk13_totals :
    (firstChunk13.map (fun r => r.coefficient * r.hi)).sum = 1303654315784172841345615208195966 ∧
      (firstChunk13.map (fun r => r.weight * r.lo)).sum = 11377926159210626232896145681650273051650736 := by
  norm_num [firstChunk13, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk13_coverage : firstChunk13.map Row.p =
    (List.range' 2862 306).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk14_totals :
    (firstChunk14.map (fun r => r.coefficient * r.hi)).sum = 1206070096465781590434452825814928 ∧
      (firstChunk14.map (fun r => r.weight * r.lo)).sum = 10528528393862356338836347844012918667184695 := by
  norm_num [firstChunk14, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk14_coverage : firstChunk14.map Row.p =
    (List.range' 3168 246).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk15_totals :
    (firstChunk15.map (fun r => r.coefficient * r.hi)).sum = 1129174977444969793446178482061796 ∧
      (firstChunk15.map (fun r => r.weight * r.lo)).sum = 9858930675210400822431174171901069633421770 := by
  norm_num [firstChunk15, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk15_coverage : firstChunk15.map Row.p =
    (List.range' 3414 258).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk16_totals :
    (firstChunk16.map (fun r => r.coefficient * r.hi)).sum = 1063147873941474584888611830569192 ∧
      (firstChunk16.map (fun r => r.weight * r.lo)).sum = 9283772978464240424043100864161592618646160 := by
  norm_num [firstChunk16, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk16_coverage : firstChunk16.map Row.p =
    (List.range' 3672 252).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk17_totals :
    (firstChunk17.map (fun r => r.coefficient * r.hi)).sum = 1002236244679638772939942959226860 ∧
      (firstChunk17.map (fun r => r.weight * r.lo)).sum = 8753020414372088123133702269876082343819706 := by
  norm_num [firstChunk17, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk17_coverage : firstChunk17.map Row.p =
    (List.range' 3924 288).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk18_totals :
    (firstChunk18.map (fun r => r.coefficient * r.hi)).sum = 946664096300881870644076229638049 ∧
      (firstChunk18.map (fun r => r.weight * r.lo)).sum = 8268662319998266956738999993427137129982917 := by
  norm_num [firstChunk18, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk18_coverage : firstChunk18.map Row.p =
    (List.range' 4212 270).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk19_totals :
    (firstChunk19.map (fun r => r.coefficient * r.hi)).sum = 896023108588271943149100844409665 ∧
      (firstChunk19.map (fun r => r.weight * r.lo)).sum = 7827176639408184912559852854552873895989190 := by
  norm_num [firstChunk19, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk19_coverage : firstChunk19.map Row.p =
    (List.range' 4482 270).filter (fun p => decide p.Prime) := by decide +kernel

end TenthDiscriminant.FirstCertificate
