import TenthDiscriminant.QuotientFiberData
import TenthDiscriminant.FusedWheelParameters

namespace TenthDiscriminant
def phase36Leaf (r : Nat) : Bool := quotientFilter r (quotientInitial r) phase36Entries == 0
def phase36Seed (seed : Nat) : Bool := maskWheelVisit phase35Prefix 184 seed phase36Leaf
end TenthDiscriminant
