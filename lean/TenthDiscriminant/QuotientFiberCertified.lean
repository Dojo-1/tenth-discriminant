import TenthDiscriminant.QuotientFiberSeed10

/-! Concrete certificate covering every seed and every admissible quotient. -/
namespace TenthDiscriminant
theorem phase36_seeds_exact :
    phase35Seeds=[3,27,35,59,75,123,131,139,147,163,179] := by decide +kernel

theorem phase36_all_fibers : phase35Seeds.all phase36Seed=true := by
  rw [phase36_seeds_exact]
  simp only [List.all_cons,List.all_nil,phase36_seed_0,phase36_seed_1,phase36_seed_2,phase36_seed_3,phase36_seed_4,phase36_seed_5,phase36_seed_6,phase36_seed_7,phase36_seed_8,phase36_seed_9,phase36_seed_10,Bool.and_self]
end TenthDiscriminant
