import TenthDiscriminant.QuotientFiberParameters

/-! Boundary and missing-seed controls for complete quotient coverage. -/
namespace TenthDiscriminant

theorem quotient_zero_residue_control :
    (quotientInitial 0).testBit 0=false ∧
    (quotientInitial 0).testBit 1=true ∧
    (quotientWidePattern 29 3).testBit 0=false := by decide +kernel

/-- Dropping the last seed would discard a genuine member of the seed list. -/
theorem quotient_omitted_seed_control :
    179∈phase35Seeds ∧ 179∉phase35Seeds.take 10 := by decide +kernel

end TenthDiscriminant
