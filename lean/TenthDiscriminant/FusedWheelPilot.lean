import TenthDiscriminant.Fused35Q0S10
import TenthDiscriminant.FusedWheelBridge

namespace TenthDiscriminant
set_option autoImplicit false

theorem phase35_seeds_exact : phase35Seeds=[3, 27, 35, 59, 75, 123, 131, 139, 147, 163, 179] := by decide +kernel

theorem phase35_q0_blocks : phase35Seeds.all (phase35Block 0)=true := by
  rw [phase35_seeds_exact]
  simp only [List.all_cons, List.all_nil, phase35_block_0_0, phase35_block_0_1, phase35_block_0_2, phase35_block_0_3, phase35_block_0_4, phase35_block_0_5, phase35_block_0_6, phase35_block_0_7, phase35_block_0_8, phase35_block_0_9, phase35_block_0_10, Bool.and_self]

theorem phase35_q0_translate :
    maskTranslateClear (maskWheelResidues phase34Base)
      892371480 1000000 700000000000 0 phase34Extra=true :=
  phase35_translate_of_blocks 0 phase35_q0_blocks

end TenthDiscriminant
