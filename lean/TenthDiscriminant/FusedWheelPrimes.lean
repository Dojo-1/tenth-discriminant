import TenthDiscriminant.ResidueMaskBridge
import TenthDiscriminant.FusedWheelMasks

/-! Generated small primality proofs, aggregated along the exact data split. -/
namespace TenthDiscriminant

theorem phase35PrimeChunk0_checked :
    checkedOddPrimes (phase35MaskChunk0.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk0]

theorem phase35PrimeChunk1_checked :
    checkedOddPrimes (phase35MaskChunk1.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk1]

theorem phase35PrimeChunk2_checked :
    checkedOddPrimes (phase35MaskChunk2.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk2]

theorem phase35PrimeChunk3_checked :
    checkedOddPrimes (phase35MaskChunk3.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk3]

theorem phase35PrimeChunk4_checked :
    checkedOddPrimes (phase35MaskChunk4.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk4]

theorem phase35PrimeChunk5_checked :
    checkedOddPrimes (phase35MaskChunk5.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk5]

theorem phase35PrimeChunk6_checked :
    checkedOddPrimes (phase35MaskChunk6.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk6]

theorem phase35PrimeChunk7_checked :
    checkedOddPrimes (phase35MaskChunk7.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk7]

theorem phase35PrimeChunk8_checked :
    checkedOddPrimes (phase35MaskChunk8.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk8]

theorem phase35PrimeChunk9_checked :
    checkedOddPrimes (phase35MaskChunk9.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk9]

theorem phase35PrimeChunk10_checked :
    checkedOddPrimes (phase35MaskChunk10.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk10]

theorem phase35PrimeChunk11_checked :
    checkedOddPrimes (phase35MaskChunk11.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk11]

theorem phase35PrimeChunk12_checked :
    checkedOddPrimes (phase35MaskChunk12.map Prod.fst)=true := by
  norm_num [checkedOddPrimes, phase35MaskChunk12]

theorem phase35_all_primes_checked :
    checkedOddPrimes ((phase34Base++phase34Extra).map Prod.fst)=true := by
  rw [phase35_entries_split]
  simp only [List.map_append, checkedOddPrimes_append, phase35PrimeChunk0_checked, phase35PrimeChunk1_checked, phase35PrimeChunk2_checked, phase35PrimeChunk3_checked, phase35PrimeChunk4_checked, phase35PrimeChunk5_checked, phase35PrimeChunk6_checked, phase35PrimeChunk7_checked, phase35PrimeChunk8_checked, phase35PrimeChunk9_checked, phase35PrimeChunk10_checked, phase35PrimeChunk11_checked, phase35PrimeChunk12_checked, Bool.and_self]

theorem phase35_extra_primes_checked :
    checkedOddPrimes (phase34Extra.map Prod.fst)=true := by
  have h := phase35_all_primes_checked
  rw [List.map_append, checkedOddPrimes_append] at h
  exact (Bool.and_eq_true_iff.mp h).2

end TenthDiscriminant
