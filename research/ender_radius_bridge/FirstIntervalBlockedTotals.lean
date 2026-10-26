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
