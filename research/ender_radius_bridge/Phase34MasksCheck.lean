import TenthDiscriminant.ResidueMaskPilotData

namespace TenthDiscriminant
example : ((phase34Base++phase34Extra).all (fun e =>
    negativeSquareMask e.1 == e.2))=true := by decide +kernel
example : phase34Extra.length=200 ∧ phase34Extra.getLast?=some (1289,negativeSquareMask 1289) := by
  decide +kernel
example : maskWheelMod phase34Base=892371480 := by decide +kernel
example : 700000000000/892371480+1=785 := by decide +kernel
end TenthDiscriminant
