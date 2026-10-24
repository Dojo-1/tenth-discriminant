import TenthDiscriminant.FirstIntervalData

namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem firstChunk30_totals :
    (firstChunk30.map (fun r => r.coefficient * r.hi)).sum = 569609931004518929843598034125214 ∧
      (firstChunk30.map (fun r => r.weight * r.lo)).sum = 4979124140883301599413969128483942757044852 := by
  norm_num [firstChunk30, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk30_coverage : firstChunk30.map Row.p =
    (List.range' 7562 292).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk31_totals :
    (firstChunk31.map (fun r => r.coefficient * r.hi)).sum = 550353023885696916311547076432905 ∧
      (firstChunk31.map (fun r => r.weight * r.lo)).sum = 4810975954284157638253586210503448030151961 := by
  norm_num [firstChunk31, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk31_coverage : firstChunk31.map Row.p =
    (List.range' 7854 308).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk32_totals :
    (firstChunk32.map (fun r => r.coefficient * r.hi)).sum = 532826154133618241853300501217760 ∧
      (firstChunk32.map (fun r => r.weight * r.lo)).sum = 4657922523150120146670764289445032245606743 := by
  norm_num [firstChunk32, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk32_coverage : firstChunk32.map Row.p =
    (List.range' 8162 282).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk33_totals :
    (firstChunk33.map (fun r => r.coefficient * r.hi)).sum = 515969956497127264040163208079378 ∧
      (firstChunk33.map (fun r => r.weight * r.lo)).sum = 4510715075245721398650712221238819326651867 := by
  norm_num [firstChunk33, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk33_coverage : firstChunk33.map Row.p =
    (List.range' 8444 288).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk34_totals :
    (firstChunk34.map (fun r => r.coefficient * r.hi)).sum = 502215609571619158327754571975830 ∧
      (firstChunk34.map (fun r => r.weight * r.lo)).sum = 4390588818316968503332125679172806077831504 := by
  norm_num [firstChunk34, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk34_coverage : firstChunk34.map Row.p =
    (List.range' 8732 280).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk35_totals :
    (firstChunk35.map (fun r => r.coefficient * r.hi)).sum = 487892212895861861839193501150333 ∧
      (firstChunk35.map (fun r => r.weight * r.lo)).sum = 4265485412002492402680289131696590235929933 := by
  norm_num [firstChunk35, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk35_coverage : firstChunk35.map Row.p =
    (List.range' 9012 300).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk36_totals :
    (firstChunk36.map (fun r => r.coefficient * r.hi)).sum = 475183867142956008640671060528082 ∧
      (firstChunk36.map (fun r => r.weight * r.lo)).sum = 4154482065921899275454796277096064771260750 := by
  norm_num [firstChunk36, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk36_coverage : firstChunk36.map Row.p =
    (List.range' 9312 276).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk37_totals :
    (firstChunk37.map (fun r => r.coefficient * r.hi)).sum = 462537578112331098607343814863087 ∧
      (firstChunk37.map (fun r => r.weight * r.lo)).sum = 4044014901873015824980180025612315721035983 := by
  norm_num [firstChunk37, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk37_coverage : firstChunk37.map Row.p =
    (List.range' 9588 270).filter (fun p => decide p.Prime) := by decide +kernel

theorem firstChunk38_totals :
    (firstChunk38.map (fun r => r.coefficient * r.hi)).sum = 184731004317149428958427238636100 ∧
      (firstChunk38.map (fun r => r.weight * r.lo)).sum = 1615146865210555172653775151807395442998008 := by
  norm_num [firstChunk38, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem firstChunk38_coverage : firstChunk38.map Row.p =
    (List.range' 9858 143).filter (fun p => decide p.Prime) := by decide +kernel

end TenthDiscriminant.FirstCertificate
