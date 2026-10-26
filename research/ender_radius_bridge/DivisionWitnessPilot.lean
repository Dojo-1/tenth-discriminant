import TenthDiscriminant.FirstIntervalData

namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

def pilotRow : Row := firstChunk00[3]'(by decide)

theorem pilot_linear : checkFloorWitness 175000000000 pilotRow.p pilotRow.linear = true := by decide +kernel
theorem pilot_powers : checkPowerWitnesses 175000000000 pilotRow.p pilotRow.p 37 pilotRow.powers = true := by decide +kernel
theorem pilot_coefficient : pilotRow.coefficient = (pilotRow.powers.map FloorWitness.value).sum := by decide +kernel
theorem pilot_log : checkIntegerLogBounds pilotRow.p 1 pilotRow.k pilotRow.lo pilotRow.hi scale = true := by decide +kernel
theorem pilot_complete : checkRow pilotRow = true := by decide +kernel

end TenthDiscriminant.FirstCertificate
