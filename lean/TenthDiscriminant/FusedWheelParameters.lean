import TenthDiscriminant.FusedWheelCore
import TenthDiscriminant.ResidueMaskPilotData

namespace TenthDiscriminant
set_option autoImplicit false

def phase35Prefix : List (Nat×Nat) := phase34Base.take 7
def phase35Seeds : List Nat := maskWheelResidues (phase34Base.drop 7)

def phase35Leaf (k r : Nat) : Bool :=
  let d := r+892371480*k
  if 1000000≤d ∧ d<700000000000 then !maskTests d phase34Extra else true

def phase35Block (k seed : Nat) : Bool :=
  maskWheelVisit phase35Prefix 184 seed (phase35Leaf k)

end TenthDiscriminant
