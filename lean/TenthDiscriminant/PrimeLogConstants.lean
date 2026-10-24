import TenthDiscriminant.PrimeLogConstantData
import TenthDiscriminant.FirstIntervalRows
import TenthDiscriminant.FirstIntervalCoverage

namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem constantChunk00_checked :
    checkConstantRows firstChunk00 constantChunk00 = true := by decide +kernel

theorem constantChunk00_totals :
    (constantChunk00.map ConstantRow.a).sum = 4412161665974 ∧
    (constantChunk00.map ConstantRow.b).sum = 2629402162866 ∧
    (constantChunk00.map ConstantRow.c).sum = 126113524727 ∧
    (constantChunk00.map ConstantRow.e).sum = 113387991469524 := by
  norm_num [constantChunk00, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk01_checked :
    checkConstantRows firstChunk01 constantChunk01 = true := by decide +kernel

theorem constantChunk01_totals :
    (constantChunk01.map ConstantRow.a).sum = 821528927737 ∧
    (constantChunk01.map ConstantRow.b).sum = 817379703579 ∧
    (constantChunk01.map ConstantRow.c).sum = 4127039424 ∧
    (constantChunk01.map ConstantRow.e).sum = 171702463889016 := by
  norm_num [constantChunk01, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk02_checked :
    checkConstantRows firstChunk02 constantChunk02 = true := by decide +kernel

theorem constantChunk02_totals :
    (constantChunk02.map ConstantRow.a).sum = 476610986881 ∧
    (constantChunk02.map ConstantRow.b).sum = 475409797774 ∧
    (constantChunk02.map ConstantRow.c).sum = 1198102547 ∧
    (constantChunk02.map ConstantRow.e).sum = 192283381593108 := by
  norm_num [constantChunk02, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk03_checked :
    checkConstantRows firstChunk03 constantChunk03 = true := by decide +kernel

theorem constantChunk03_totals :
    (constantChunk03.map ConstantRow.a).sum = 336629840331 ∧
    (constantChunk03.map ConstantRow.b).sum = 336074080221 ∧
    (constantChunk03.map ConstantRow.c).sum = 554833817 ∧
    (constantChunk03.map ConstantRow.e).sum = 205387705059880 := by
  norm_num [constantChunk03, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk04_checked :
    checkConstantRows firstChunk04 constantChunk04 = true := by decide +kernel

theorem constantChunk04_totals :
    (constantChunk04.map ConstantRow.a).sum = 260325571449 ∧
    (constantChunk04.map ConstantRow.b).sum = 260008915742 ∧
    (constantChunk04.map ConstantRow.c).sum = 316267863 ∧
    (constantChunk04.map ConstantRow.e).sum = 215038525705943 := by
  norm_num [constantChunk04, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk05_checked :
    checkConstantRows firstChunk05 constantChunk05 = true := by decide +kernel

theorem constantChunk05_totals :
    (constantChunk05.map ConstantRow.a).sum = 212445506128 ∧
    (constantChunk05.map ConstantRow.b).sum = 212242277250 ∧
    (constantChunk05.map ConstantRow.c).sum = 203033492 ∧
    (constantChunk05.map ConstantRow.e).sum = 222612969996169 := by
  norm_num [constantChunk05, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk06_checked :
    checkConstantRows firstChunk06 constantChunk06 = true := by decide +kernel

theorem constantChunk06_totals :
    (constantChunk06.map ConstantRow.a).sum = 178900505207 ∧
    (constantChunk06.map ConstantRow.b).sum = 178760453347 ∧
    (constantChunk06.map ConstantRow.c).sum = 139941634 ∧
    (constantChunk06.map ConstantRow.e).sum = 229008514457117 := by
  norm_num [constantChunk06, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk07_checked :
    checkConstantRows firstChunk07 constantChunk07 = true := by decide +kernel

theorem constantChunk07_totals :
    (constantChunk07.map ConstantRow.a).sum = 154499662562 ∧
    (constantChunk07.map ConstantRow.b).sum = 154397742042 ∧
    (constantChunk07.map ConstantRow.c).sum = 101852945 ∧
    (constantChunk07.map ConstantRow.e).sum = 234431318734059 := by
  norm_num [constantChunk07, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk08_checked :
    checkConstantRows firstChunk08 constantChunk08 = true := by decide +kernel

theorem constantChunk08_totals :
    (constantChunk08.map ConstantRow.a).sum = 136595374726 ∧
    (constantChunk08.map ConstantRow.b).sum = 136517196192 ∧
    (constantChunk08.map ConstantRow.c).sum = 78133505 ∧
    (constantChunk08.map ConstantRow.e).sum = 238989954780555 := by
  norm_num [constantChunk08, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk09_checked :
    checkConstantRows firstChunk09 constantChunk09 = true := by decide +kernel

theorem constantChunk09_totals :
    (constantChunk09.map ConstantRow.a).sum = 121330782911 ∧
    (constantChunk09.map ConstantRow.b).sum = 121270242564 ∧
    (constantChunk09.map ConstantRow.c).sum = 60509910 ∧
    (constantChunk09.map ConstantRow.e).sum = 243350449387553 := by
  norm_num [constantChunk09, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk10_checked :
    checkConstantRows firstChunk10 constantChunk10 = true := by decide +kernel

theorem constantChunk10_totals :
    (constantChunk10.map ConstantRow.a).sum = 109575209766 ∧
    (constantChunk10.map ConstantRow.b).sum = 109526586524 ∧
    (constantChunk10.map ConstantRow.c).sum = 48601465 ∧
    (constantChunk10.map ConstantRow.e).sum = 247096744722944 := by
  norm_num [constantChunk10, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk11_checked :
    checkConstantRows firstChunk11 constantChunk11 = true := by decide +kernel

theorem constantChunk11_totals :
    (constantChunk11.map ConstantRow.a).sum = 100022966150 ∧
    (constantChunk11.map ConstantRow.b).sum = 99982988250 ∧
    (constantChunk11.map ConstantRow.c).sum = 39961742 ∧
    (constantChunk11.map ConstantRow.e).sum = 250445832943791 := by
  norm_num [constantChunk11, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk12_checked :
    checkConstantRows firstChunk12 constantChunk12 = true := by decide +kernel

theorem constantChunk12_totals :
    (constantChunk12.map ConstantRow.a).sum = 92133039702 ∧
    (constantChunk12.map ConstantRow.b).sum = 92099542408 ∧
    (constantChunk12.map ConstantRow.c).sum = 33484961 ∧
    (constantChunk12.map ConstantRow.e).sum = 253447492317158 := by
  norm_num [constantChunk12, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk13_checked :
    checkConstantRows firstChunk13 constantChunk13 = true := by decide +kernel

theorem constantChunk13_totals :
    (constantChunk13.map ConstantRow.a).sum = 85136612757 ∧
    (constantChunk13.map ConstantRow.b).sum = 85108324545 ∧
    (constantChunk13.map ConstantRow.c).sum = 28278669 ∧
    (constantChunk13.map ConstantRow.e).sum = 256339864613222 := by
  norm_num [constantChunk13, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk14_checked :
    checkConstantRows firstChunk14 constantChunk14 = true := by decide +kernel

theorem constantChunk14_totals :
    (constantChunk14.map ConstantRow.a).sum = 78763765808 ∧
    (constantChunk14.map ConstantRow.b).sum = 78739825340 ∧
    (constantChunk14.map ConstantRow.c).sum = 23933061 ∧
    (constantChunk14.map ConstantRow.e).sum = 259177545703040 := by
  norm_num [constantChunk14, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk15_checked :
    checkConstantRows firstChunk15 constantChunk15 = true := by decide +kernel

theorem constantChunk15_totals :
    (constantChunk15.map ConstantRow.a).sum = 73742043791 ∧
    (constantChunk15.map ConstantRow.b).sum = 73721253435 ∧
    (constantChunk15.map ConstantRow.c).sum = 20784371 ∧
    (constantChunk15.map ConstantRow.e).sum = 261578641404581 := by
  norm_num [constantChunk15, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk16_checked :
    checkConstantRows firstChunk16 constantChunk16 = true := by decide +kernel

theorem constantChunk16_totals :
    (constantChunk16.map ConstantRow.a).sum = 69430069708 ∧
    (constantChunk16.map ConstantRow.b).sum = 69411791395 ∧
    (constantChunk16.map ConstantRow.c).sum = 18273386 ∧
    (constantChunk16.map ConstantRow.e).sum = 263774546665067 := by
  norm_num [constantChunk16, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk17_checked :
    checkConstantRows firstChunk17 constantChunk17 = true := by decide +kernel

theorem constantChunk17_totals :
    (constantChunk17.map ConstantRow.a).sum = 65452167368 ∧
    (constantChunk17.map ConstantRow.b).sum = 65436055062 ∧
    (constantChunk17.map ConstantRow.c).sum = 16108227 ∧
    (constantChunk17.map ConstantRow.e).sum = 265920797062451 := by
  norm_num [constantChunk17, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk18_checked :
    checkConstantRows firstChunk18 constantChunk18 = true := by decide +kernel

theorem constantChunk18_totals :
    (constantChunk18.map ConstantRow.a).sum = 61822965918 ∧
    (constantChunk18.map ConstantRow.b).sum = 61808702110 ∧
    (constantChunk18.map ConstantRow.c).sum = 14260405 ∧
    (constantChunk18.map ConstantRow.e).sum = 267994049041971 := by
  norm_num [constantChunk18, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk19_checked :
    checkConstantRows firstChunk19 constantChunk19 = true := by decide +kernel

theorem constantChunk19_totals :
    (constantChunk19.map ConstantRow.a).sum = 58515799348 ∧
    (constantChunk19.map ConstantRow.b).sum = 58503115985 ∧
    (constantChunk19.map ConstantRow.c).sum = 12680510 ∧
    (constantChunk19.map ConstantRow.e).sum = 269989355731797 := by
  norm_num [constantChunk19, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk20_checked :
    checkConstantRows firstChunk20 constantChunk20 = true := by decide +kernel

theorem constantChunk20_totals :
    (constantChunk20.map ConstantRow.a).sum = 55525040262 ∧
    (constantChunk20.map ConstantRow.b).sum = 55513700338 ∧
    (constantChunk20.map ConstantRow.c).sum = 11337515 ∧
    (constantChunk20.map ConstantRow.e).sum = 271892184496390 := by
  norm_num [constantChunk20, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk21_checked :
    checkConstantRows firstChunk21 constantChunk21 = true := by decide +kernel

theorem constantChunk21_totals :
    (constantChunk21.map ConstantRow.a).sum = 52981308737 ∧
    (constantChunk21.map ConstantRow.b).sum = 52971047807 ∧
    (constantChunk21.map ConstantRow.c).sum = 10258850 ∧
    (constantChunk21.map ConstantRow.e).sum = 273592280568830 := by
  norm_num [constantChunk21, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk22_checked :
    checkConstantRows firstChunk22 constantChunk22 = true := by decide +kernel

theorem constantChunk22_totals :
    (constantChunk22.map ConstantRow.a).sum = 50492490956 ∧
    (constantChunk22.map ConstantRow.b).sum = 50483231350 ∧
    (constantChunk22.map ConstantRow.c).sum = 9257821 ∧
    (constantChunk22.map ConstantRow.e).sum = 275333096528975 := by
  norm_num [constantChunk22, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk23_checked :
    checkConstantRows firstChunk23 constantChunk23 = true := by decide +kernel

theorem constantChunk23_totals :
    (constantChunk23.map ConstantRow.a).sum = 48396438909 ∧
    (constantChunk23.map ConstantRow.b).sum = 48387979051 ∧
    (constantChunk23.map ConstantRow.c).sum = 8458294 ∧
    (constantChunk23.map ConstantRow.e).sum = 276867632379671 := by
  norm_num [constantChunk23, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk24_checked :
    checkConstantRows firstChunk24 constantChunk24 = true := by decide +kernel

theorem constantChunk24_totals :
    (constantChunk24.map ConstantRow.a).sum = 46457232377 ∧
    (constantChunk24.map ConstantRow.b).sum = 46449477812 ∧
    (constantChunk24.map ConstantRow.c).sum = 7753189 ∧
    (constantChunk24.map ConstantRow.e).sum = 278347273313375 := by
  norm_num [constantChunk24, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk25_checked :
    checkConstantRows firstChunk25 constantChunk25 = true := by decide +kernel

theorem constantChunk25_totals :
    (constantChunk25.map ConstantRow.a).sum = 44618009890 ∧
    (constantChunk25.map ConstantRow.b).sum = 44610895229 ∧
    (constantChunk25.map ConstantRow.c).sum = 7113449 ∧
    (constantChunk25.map ConstantRow.e).sum = 279805403050201 := by
  norm_num [constantChunk25, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk26_checked :
    checkConstantRows firstChunk26 constantChunk26 = true := by decide +kernel

theorem constantChunk26_totals :
    (constantChunk26.map ConstantRow.a).sum = 42893068966 ∧
    (constantChunk26.map ConstantRow.b).sum = 42886526553 ∧
    (constantChunk26.map ConstantRow.c).sum = 6541335 ∧
    (constantChunk26.map ConstantRow.e).sum = 281230321749147 := by
  norm_num [constantChunk26, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk27_checked :
    checkConstantRows firstChunk27 constantChunk27 = true := by decide +kernel

theorem constantChunk27_totals :
    (constantChunk27.map ConstantRow.a).sum = 41310550018 ∧
    (constantChunk27.map ConstantRow.b).sum = 41304510896 ∧
    (constantChunk27.map ConstantRow.c).sum = 6038170 ∧
    (constantChunk27.map ConstantRow.e).sum = 282586271464294 := by
  norm_num [constantChunk27, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk28_checked :
    checkConstantRows firstChunk28 constantChunk28 = true := by decide +kernel

theorem constantChunk28_totals :
    (constantChunk28.map ConstantRow.a).sum = 39883749655 ∧
    (constantChunk28.map ConstantRow.b).sum = 39878145473 ∧
    (constantChunk28.map ConstantRow.c).sum = 5603322 ∧
    (constantChunk28.map ConstantRow.e).sum = 283854424936620 := by
  norm_num [constantChunk28, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk29_checked :
    checkConstantRows firstChunk29 constantChunk29 = true := by decide +kernel

theorem constantChunk29_totals :
    (constantChunk29.map ConstantRow.a).sum = 38353032141 ∧
    (constantChunk29.map ConstantRow.b).sum = 38347875564 ∧
    (constantChunk29.map ConstantRow.c).sum = 5155816 ∧
    (constantChunk29.map ConstantRow.e).sum = 285264954692152 := by
  norm_num [constantChunk29, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk30_checked :
    checkConstantRows firstChunk30 constantChunk30 = true := by decide +kernel

theorem constantChunk30_totals :
    (constantChunk30.map ConstantRow.a).sum = 37199019818 ∧
    (constantChunk30.map ConstantRow.b).sum = 37194187623 ∧
    (constantChunk30.map ConstantRow.c).sum = 4831503 ∧
    (constantChunk30.map ConstantRow.e).sum = 286365337455253 := by
  norm_num [constantChunk30, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk31_checked :
    checkConstantRows firstChunk31 constantChunk31 = true := by decide +kernel

theorem constantChunk31_totals :
    (constantChunk31.map ConstantRow.a).sum = 35941425831 ∧
    (constantChunk31.map ConstantRow.b).sum = 35936934185 ∧
    (constantChunk31.map ConstantRow.c).sum = 4491019 ∧
    (constantChunk31.map ConstantRow.e).sum = 287603978998643 := by
  norm_num [constantChunk31, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk32_checked :
    checkConstantRows firstChunk32 constantChunk32 = true := by decide +kernel

theorem constantChunk32_totals :
    (constantChunk32.map ConstantRow.a).sum = 34796813886 ∧
    (constantChunk32.map ConstantRow.b).sum = 34792620852 ∧
    (constantChunk32.map ConstantRow.c).sum = 4192465 ∧
    (constantChunk32.map ConstantRow.e).sum = 288768440451109 := by
  norm_num [constantChunk32, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk33_checked :
    checkConstantRows firstChunk33 constantChunk33 = true := by decide +kernel

theorem constantChunk33_totals :
    (constantChunk33.map ConstantRow.a).sum = 33696000945 ∧
    (constantChunk33.map ConstantRow.b).sum = 33692084709 ∧
    (constantChunk33.map ConstantRow.c).sum = 3915721 ∧
    (constantChunk33.map ConstantRow.e).sum = 289924753711694 := by
  norm_num [constantChunk33, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk34_checked :
    checkConstantRows firstChunk34 constantChunk34 = true := by decide +kernel

theorem constantChunk34_totals :
    (constantChunk34.map ConstantRow.a).sum = 32797757851 ∧
    (constantChunk34.map ConstantRow.b).sum = 32794059991 ∧
    (constantChunk34.map ConstantRow.c).sum = 3697381 ∧
    (constantChunk34.map ConstantRow.e).sum = 290896345989142 := by
  norm_num [constantChunk34, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk35_checked :
    checkConstantRows firstChunk35 constantChunk35 = true := by decide +kernel

theorem constantChunk35_totals :
    (constantChunk35.map ConstantRow.a).sum = 31862352332 ∧
    (constantChunk35.map ConstantRow.b).sum = 31858874826 ∧
    (constantChunk35.map ConstantRow.c).sum = 3477058 ∧
    (constantChunk35.map ConstantRow.e).sum = 291936273104921 := by
  norm_num [constantChunk35, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk36_checked :
    checkConstantRows firstChunk36 constantChunk36 = true := by decide +kernel

theorem constantChunk36_totals :
    (constantChunk36.map ConstantRow.a).sum = 31032419525 ∧
    (constantChunk36.map ConstantRow.b).sum = 31029131576 ∧
    (constantChunk36.map ConstantRow.c).sum = 3287538 ∧
    (constantChunk36.map ConstantRow.e).sum = 292884122848948 := by
  norm_num [constantChunk36, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk37_checked :
    checkConstantRows firstChunk37 constantChunk37 = true := by decide +kernel

theorem constantChunk37_totals :
    (constantChunk37.map ConstantRow.a).sum = 30206539409 ∧
    (constantChunk37.map ConstantRow.b).sum = 30203434373 ∧
    (constantChunk37.map ConstantRow.c).sum = 3104653 ∧
    (constantChunk37.map ConstantRow.e).sum = 293852945207125 := by
  norm_num [constantChunk37, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constantChunk38_checked :
    checkConstantRows firstChunk38 constantChunk38 = true := by decide +kernel

theorem constantChunk38_totals :
    (constantChunk38.map ConstantRow.a).sum = 12064067086 ∧
    (constantChunk38.map ConstantRow.b).sum = 12062850521 ∧
    (constantChunk38.map ConstantRow.c).sum = 1216417 ∧
    (constantChunk38.map ConstantRow.e).sum = 119625995731617 := by
  norm_num [constantChunk38, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]

theorem constant_rows_related :
    List.Forall₂ (fun r t => checkConstantRow r t = true) firstRows constantRows := by
  apply List.rel_flatten
  exact
    .cons (checkConstantRows_sound _ _ constantChunk00_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk01_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk02_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk03_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk04_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk05_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk06_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk07_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk08_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk09_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk10_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk11_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk12_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk13_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk14_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk15_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk16_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk17_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk18_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk19_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk20_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk21_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk22_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk23_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk24_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk25_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk26_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk27_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk28_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk29_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk30_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk31_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk32_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk33_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk34_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk35_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk36_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk37_checked) (
    .cons (checkConstantRows_sound _ _ constantChunk38_checked) (
    .nil)))))))))))))))))))))))))))))))))))))))

theorem constant_units_totals :
    (constantRows.map ConstantRow.a).sum = 8646130782816 ∧
    (constantRows.map ConstantRow.b).sum = 6856198325360 ∧
    (constantRows.map ConstantRow.c).sum = 133259338177 ∧
    (constantRows.map ConstantRow.e).sum = 9892590181957053 := by
  constructor
  · simp only [constantRows, List.map_flatten, List.sum_flatten, List.map_map,
      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, constantChunk00_totals.1, constantChunk01_totals.1, constantChunk02_totals.1, constantChunk03_totals.1, constantChunk04_totals.1, constantChunk05_totals.1, constantChunk06_totals.1, constantChunk07_totals.1, constantChunk08_totals.1, constantChunk09_totals.1, constantChunk10_totals.1, constantChunk11_totals.1, constantChunk12_totals.1, constantChunk13_totals.1, constantChunk14_totals.1, constantChunk15_totals.1, constantChunk16_totals.1, constantChunk17_totals.1, constantChunk18_totals.1, constantChunk19_totals.1, constantChunk20_totals.1, constantChunk21_totals.1, constantChunk22_totals.1, constantChunk23_totals.1, constantChunk24_totals.1, constantChunk25_totals.1, constantChunk26_totals.1, constantChunk27_totals.1, constantChunk28_totals.1, constantChunk29_totals.1, constantChunk30_totals.1, constantChunk31_totals.1, constantChunk32_totals.1, constantChunk33_totals.1, constantChunk34_totals.1, constantChunk35_totals.1, constantChunk36_totals.1, constantChunk37_totals.1, constantChunk38_totals.1]
    norm_num
  constructor
  · simp only [constantRows, List.map_flatten, List.sum_flatten, List.map_map,
      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, constantChunk00_totals.2.1, constantChunk01_totals.2.1, constantChunk02_totals.2.1, constantChunk03_totals.2.1, constantChunk04_totals.2.1, constantChunk05_totals.2.1, constantChunk06_totals.2.1, constantChunk07_totals.2.1, constantChunk08_totals.2.1, constantChunk09_totals.2.1, constantChunk10_totals.2.1, constantChunk11_totals.2.1, constantChunk12_totals.2.1, constantChunk13_totals.2.1, constantChunk14_totals.2.1, constantChunk15_totals.2.1, constantChunk16_totals.2.1, constantChunk17_totals.2.1, constantChunk18_totals.2.1, constantChunk19_totals.2.1, constantChunk20_totals.2.1, constantChunk21_totals.2.1, constantChunk22_totals.2.1, constantChunk23_totals.2.1, constantChunk24_totals.2.1, constantChunk25_totals.2.1, constantChunk26_totals.2.1, constantChunk27_totals.2.1, constantChunk28_totals.2.1, constantChunk29_totals.2.1, constantChunk30_totals.2.1, constantChunk31_totals.2.1, constantChunk32_totals.2.1, constantChunk33_totals.2.1, constantChunk34_totals.2.1, constantChunk35_totals.2.1, constantChunk36_totals.2.1, constantChunk37_totals.2.1, constantChunk38_totals.2.1]
    norm_num
  constructor
  · simp only [constantRows, List.map_flatten, List.sum_flatten, List.map_map,
      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, constantChunk00_totals.2.2.1, constantChunk01_totals.2.2.1, constantChunk02_totals.2.2.1, constantChunk03_totals.2.2.1, constantChunk04_totals.2.2.1, constantChunk05_totals.2.2.1, constantChunk06_totals.2.2.1, constantChunk07_totals.2.2.1, constantChunk08_totals.2.2.1, constantChunk09_totals.2.2.1, constantChunk10_totals.2.2.1, constantChunk11_totals.2.2.1, constantChunk12_totals.2.2.1, constantChunk13_totals.2.2.1, constantChunk14_totals.2.2.1, constantChunk15_totals.2.2.1, constantChunk16_totals.2.2.1, constantChunk17_totals.2.2.1, constantChunk18_totals.2.2.1, constantChunk19_totals.2.2.1, constantChunk20_totals.2.2.1, constantChunk21_totals.2.2.1, constantChunk22_totals.2.2.1, constantChunk23_totals.2.2.1, constantChunk24_totals.2.2.1, constantChunk25_totals.2.2.1, constantChunk26_totals.2.2.1, constantChunk27_totals.2.2.1, constantChunk28_totals.2.2.1, constantChunk29_totals.2.2.1, constantChunk30_totals.2.2.1, constantChunk31_totals.2.2.1, constantChunk32_totals.2.2.1, constantChunk33_totals.2.2.1, constantChunk34_totals.2.2.1, constantChunk35_totals.2.2.1, constantChunk36_totals.2.2.1, constantChunk37_totals.2.2.1, constantChunk38_totals.2.2.1]
    norm_num
  simp only [constantRows, List.map_flatten, List.sum_flatten, List.map_map,
      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, constantChunk00_totals.2.2.2, constantChunk01_totals.2.2.2, constantChunk02_totals.2.2.2, constantChunk03_totals.2.2.2, constantChunk04_totals.2.2.2, constantChunk05_totals.2.2.2, constantChunk06_totals.2.2.2, constantChunk07_totals.2.2.2, constantChunk08_totals.2.2.2, constantChunk09_totals.2.2.2, constantChunk10_totals.2.2.2, constantChunk11_totals.2.2.2, constantChunk12_totals.2.2.2, constantChunk13_totals.2.2.2, constantChunk14_totals.2.2.2, constantChunk15_totals.2.2.2, constantChunk16_totals.2.2.2, constantChunk17_totals.2.2.2, constantChunk18_totals.2.2.2, constantChunk19_totals.2.2.2, constantChunk20_totals.2.2.2, constantChunk21_totals.2.2.2, constantChunk22_totals.2.2.2, constantChunk23_totals.2.2.2, constantChunk24_totals.2.2.2, constantChunk25_totals.2.2.2, constantChunk26_totals.2.2.2, constantChunk27_totals.2.2.2, constantChunk28_totals.2.2.2, constantChunk29_totals.2.2.2, constantChunk30_totals.2.2.2, constantChunk31_totals.2.2.2, constantChunk32_totals.2.2.2, constantChunk33_totals.2.2.2, constantChunk34_totals.2.2.2, constantChunk35_totals.2.2.2, constantChunk36_totals.2.2.2, constantChunk37_totals.2.2.2, constantChunk38_totals.2.2.2]
  norm_num

noncomputable section

def factorialConstantUpper : Real := 8646130782816 / 1000000000000
def linearConstantLower : Real := 6856198325360 / 1000000000000
def squareConstantUpper : Real := 133259338177 / 1000000000000
def errorConstantUpper : Real := 9892590181957053 / 1000000000000

theorem certified_prime_log_constants :
    primeLogFactorialConstant 10000 ≤ factorialConstantUpper ∧
      linearConstantLower ≤ primeLogLinearConstant 7 10000 ∧
      primeLogSquareConstant 7 10000 ≤ squareConstantUpper ∧
      primeLogErrorConstant 7 10000 ≤ errorConstantUpper := by
  have h := four_prime_log_bounds firstRows constantRows first_rows_coverage
    (List.all_eq_true.mp first_rows_checked) constant_rows_related
  simpa only [constant_units_totals.1, constant_units_totals.2.1,
    constant_units_totals.2.2.1, constant_units_totals.2.2.2, scale,
    Nat.cast_ofNat, factorialConstantUpper, linearConstantLower,
    squareConstantUpper, errorConstantUpper] using h

theorem constant_upper_rounding_down_rejected :
    checkConstantRow (firstChunk00[0]'(by decide))
      { constantChunk00[0]'(by decide) with a := (constantChunk00[0]'(by decide)).a - 1 } = false := by decide +kernel

theorem constant_lower_rounding_up_rejected :
    checkConstantRow (firstChunk00[3]'(by decide))
      { constantChunk00[3]'(by decide) with b := (constantChunk00[3]'(by decide)).b + 1 } = false := by decide +kernel

end
end TenthDiscriminant.FirstCertificate
