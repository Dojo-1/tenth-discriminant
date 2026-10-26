import TenthDiscriminant.FirstIntervalTotalsPart00
import TenthDiscriminant.FirstIntervalTotalsPart01
import TenthDiscriminant.FirstIntervalTotalsPart02
import TenthDiscriminant.FirstIntervalTotalsPart03

namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem first_range_split : List.range 10001 = [List.range' 0 132, List.range' 132 180, List.range' 312 192, List.range' 504 216, List.range' 720 222, List.range' 942 222, List.range' 1164 260, List.range' 1424 196, List.range' 1620 258, List.range' 1878 252, List.range' 2130 248, List.range' 2378 280, List.range' 2658 204, List.range' 2862 306, List.range' 3168 246, List.range' 3414 258, List.range' 3672 252, List.range' 3924 288, List.range' 4212 270, List.range' 4482 270, List.range' 4752 260, List.range' 5012 298, List.range' 5310 264, List.range' 5574 276, List.range' 5850 284, List.range' 6134 246, List.range' 6380 322, List.range' 6702 270, List.range' 6972 282, List.range' 7254 308, List.range' 7562 292, List.range' 7854 308, List.range' 8162 282, List.range' 8444 288, List.range' 8732 280, List.range' 9012 300, List.range' 9312 276, List.range' 9588 270, List.range' 9858 143].flatten := by
  rw [List.range_eq_range']
  simp only [List.flatten_cons, List.flatten_nil, List.append_nil]
  rw [List.range'_append_1 (s := 9588) (m := 270) (n := 143)]
  rw [List.range'_append_1 (s := 9312) (m := 276) (n := 413)]
  rw [List.range'_append_1 (s := 9012) (m := 300) (n := 689)]
  rw [List.range'_append_1 (s := 8732) (m := 280) (n := 989)]
  rw [List.range'_append_1 (s := 8444) (m := 288) (n := 1269)]
  rw [List.range'_append_1 (s := 8162) (m := 282) (n := 1557)]
  rw [List.range'_append_1 (s := 7854) (m := 308) (n := 1839)]
  rw [List.range'_append_1 (s := 7562) (m := 292) (n := 2147)]
  rw [List.range'_append_1 (s := 7254) (m := 308) (n := 2439)]
  rw [List.range'_append_1 (s := 6972) (m := 282) (n := 2747)]
  rw [List.range'_append_1 (s := 6702) (m := 270) (n := 3029)]
  rw [List.range'_append_1 (s := 6380) (m := 322) (n := 3299)]
  rw [List.range'_append_1 (s := 6134) (m := 246) (n := 3621)]
  rw [List.range'_append_1 (s := 5850) (m := 284) (n := 3867)]
  rw [List.range'_append_1 (s := 5574) (m := 276) (n := 4151)]
  rw [List.range'_append_1 (s := 5310) (m := 264) (n := 4427)]
  rw [List.range'_append_1 (s := 5012) (m := 298) (n := 4691)]
  rw [List.range'_append_1 (s := 4752) (m := 260) (n := 4989)]
  rw [List.range'_append_1 (s := 4482) (m := 270) (n := 5249)]
  rw [List.range'_append_1 (s := 4212) (m := 270) (n := 5519)]
  rw [List.range'_append_1 (s := 3924) (m := 288) (n := 5789)]
  rw [List.range'_append_1 (s := 3672) (m := 252) (n := 6077)]
  rw [List.range'_append_1 (s := 3414) (m := 258) (n := 6329)]
  rw [List.range'_append_1 (s := 3168) (m := 246) (n := 6587)]
  rw [List.range'_append_1 (s := 2862) (m := 306) (n := 6833)]
  rw [List.range'_append_1 (s := 2658) (m := 204) (n := 7139)]
  rw [List.range'_append_1 (s := 2378) (m := 280) (n := 7343)]
  rw [List.range'_append_1 (s := 2130) (m := 248) (n := 7623)]
  rw [List.range'_append_1 (s := 1878) (m := 252) (n := 7871)]
  rw [List.range'_append_1 (s := 1620) (m := 258) (n := 8123)]
  rw [List.range'_append_1 (s := 1424) (m := 196) (n := 8381)]
  rw [List.range'_append_1 (s := 1164) (m := 260) (n := 8577)]
  rw [List.range'_append_1 (s := 942) (m := 222) (n := 8837)]
  rw [List.range'_append_1 (s := 720) (m := 222) (n := 9059)]
  rw [List.range'_append_1 (s := 504) (m := 216) (n := 9281)]
  rw [List.range'_append_1 (s := 312) (m := 192) (n := 9497)]
  rw [List.range'_append_1 (s := 132) (m := 180) (n := 9689)]
  rw [List.range'_append_1 (s := 0) (m := 132) (n := 9869)]

theorem first_rows_coverage : firstRows.map Row.p = primeList := by
  unfold primeList
  rw [first_range_split, List.filter_flatten, firstRows, List.map_flatten]
  simp only [List.map_cons, List.map_nil, firstChunk00_coverage, firstChunk01_coverage, firstChunk02_coverage, firstChunk03_coverage, firstChunk04_coverage, firstChunk05_coverage, firstChunk06_coverage, firstChunk07_coverage, firstChunk08_coverage, firstChunk09_coverage, firstChunk10_coverage, firstChunk11_coverage, firstChunk12_coverage, firstChunk13_coverage, firstChunk14_coverage, firstChunk15_coverage, firstChunk16_coverage, firstChunk17_coverage, firstChunk18_coverage, firstChunk19_coverage, firstChunk20_coverage, firstChunk21_coverage, firstChunk22_coverage, firstChunk23_coverage, firstChunk24_coverage, firstChunk25_coverage, firstChunk26_coverage, firstChunk27_coverage, firstChunk28_coverage, firstChunk29_coverage, firstChunk30_coverage, firstChunk31_coverage, firstChunk32_coverage, firstChunk33_coverage, firstChunk34_coverage, firstChunk35_coverage, firstChunk36_coverage, firstChunk37_coverage, firstChunk38_coverage]

theorem first_rows_unit_sums :
    (firstRows.map (fun r => r.coefficient * r.hi)).sum = 132393875135023553259473658533593129 ∧
      (firstRows.map (fun r => r.weight * r.lo)).sum = 799592313080280706345663778036662106229815220 := by
  constructor
  · simp only [firstRows, List.map_flatten, List.sum_flatten, List.map_map,
      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, firstChunk00_totals.1, firstChunk01_totals.1, firstChunk02_totals.1, firstChunk03_totals.1, firstChunk04_totals.1, firstChunk05_totals.1, firstChunk06_totals.1, firstChunk07_totals.1, firstChunk08_totals.1, firstChunk09_totals.1, firstChunk10_totals.1, firstChunk11_totals.1, firstChunk12_totals.1, firstChunk13_totals.1, firstChunk14_totals.1, firstChunk15_totals.1, firstChunk16_totals.1, firstChunk17_totals.1, firstChunk18_totals.1, firstChunk19_totals.1, firstChunk20_totals.1, firstChunk21_totals.1, firstChunk22_totals.1, firstChunk23_totals.1, firstChunk24_totals.1, firstChunk25_totals.1, firstChunk26_totals.1, firstChunk27_totals.1, firstChunk28_totals.1, firstChunk29_totals.1, firstChunk30_totals.1, firstChunk31_totals.1, firstChunk32_totals.1, firstChunk33_totals.1, firstChunk34_totals.1, firstChunk35_totals.1, firstChunk36_totals.1, firstChunk37_totals.1, firstChunk38_totals.1]
    norm_num
  · simp only [firstRows, List.map_flatten, List.sum_flatten, List.map_map,
      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, firstChunk00_totals.2, firstChunk01_totals.2, firstChunk02_totals.2, firstChunk03_totals.2, firstChunk04_totals.2, firstChunk05_totals.2, firstChunk06_totals.2, firstChunk07_totals.2, firstChunk08_totals.2, firstChunk09_totals.2, firstChunk10_totals.2, firstChunk11_totals.2, firstChunk12_totals.2, firstChunk13_totals.2, firstChunk14_totals.2, firstChunk15_totals.2, firstChunk16_totals.2, firstChunk17_totals.2, firstChunk18_totals.2, firstChunk19_totals.2, firstChunk20_totals.2, firstChunk21_totals.2, firstChunk22_totals.2, firstChunk23_totals.2, firstChunk24_totals.2, firstChunk25_totals.2, firstChunk26_totals.2, firstChunk27_totals.2, firstChunk28_totals.2, firstChunk29_totals.2, firstChunk30_totals.2, firstChunk31_totals.2, firstChunk32_totals.2, firstChunk33_totals.2, firstChunk34_totals.2, firstChunk35_totals.2, firstChunk36_totals.2, firstChunk37_totals.2, firstChunk38_totals.2]
    norm_num

theorem first_rows_budgets :
    (firstRows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧
      7995 * 10 ^ 29 * scale ≤ (firstRows.map (fun r => r.weight * r.lo)).sum := by
  rw [first_rows_unit_sums.1, first_rows_unit_sums.2]
  decide +kernel

end TenthDiscriminant.FirstCertificate
