import TenthDiscriminant.FirstIntervalGuards
import TenthDiscriminant.LogEnclosure

/-! Exact scalar enclosures for the fixed first interval. The complete
prime-table budgets remain explicit inputs until separately kernel-checked. -/

namespace TenthDiscriminant.FirstEnderInterval
set_option autoImplicit false
set_option maxRecDepth 10000
set_option maxHeartbeats 2000000
noncomputable section

theorem factorial_log_bounds :
    (25888051773431 / 1000000000000 : Real) ≤ Real.log 174999999999 ∧
      Real.log 174999999999 ≤ (25888051811352 / 1000000000000 : Real) := by
  have h := checkPositiveLogBounds_sound 8 174999999999 37
    (25888051773431 / 1000000000000) (25888051811352 / 1000000000000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h

theorem tail_prime_log_bounds :
    (9210440353824 / 1000000000000 : Real) ≤ Real.log 10001 ∧
      Real.log 10001 ≤ (9210440367148 / 1000000000000 : Real) := by
  have h := checkPositiveLogBounds_sound 8 10001 13
    (9210440353824 / 1000000000000) (9210440367148 / 1000000000000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h

theorem tail_ratio_log_bounds :
    (99995000 / 1000000000000 : Real) ≤ Real.log (10001 / 10000) ∧
      Real.log (10001 / 10000) ≤ (99995001 / 1000000000000 : Real) := by
  have h := checkPositiveLogBounds_sound 8 (10001 / 10000) 0
    (99995000 / 1000000000000) (99995001 / 1000000000000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h

def countArgumentUpper : Real := 11183983326123142744759381338636483725 / 1019074331953807

theorem count_log_bounds :
    (50749874876081 / 1000000000000 : Real) ≤ Real.log countArgumentUpper ∧
      Real.log countArgumentUpper ≤ (50749874950898 / 1000000000000 : Real) := by
  have h := checkPositiveLogBounds_sound 8
    (11183983326123142744759381338636483725 / 1019074331953807) 73
    (50749874876081 / 1000000000000) (50749874950898 / 1000000000000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h

theorem radius_log_bounds :
    (19827774023725 / 1000000000000 : Real) ≤ Real.log 408406701 ∧
      Real.log 408406701 ≤ (19827774052423 / 1000000000000 : Real) := by
  have h := checkPositiveLogBounds_sound 8 408406701 28
    (19827774023725 / 1000000000000) (19827774052423 / 1000000000000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h

theorem radius_ratio_log_bounds :
    (6060277750714 / 1000000000000 : Real) ≤ Real.log (175000000000 / 408406701) ∧
      Real.log (175000000000 / 408406701) ≤ (6060277758922 / 1000000000000 : Real) := by
  have h := checkPositiveLogBounds_sound 8 (175000000000 / 408406701) 8
    (6060277750714 / 1000000000000) (6060277758922 / 1000000000000)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h

theorem count_log_argument_le :
    2 * ellipsePaddedUpperCount 700000000000 408406701 488 * 8750000000 ≤ countArgumentUpper := by
  have hlpos : (0 : Real) < sqrtD1Lower := by norm_num [sqrtD1Lower]
  have hnum : (0 : Real) ≤ Real.pi * (408406701 : Real) ^ 2 := by positivity
  have hd := div_le_div_of_nonneg_left hnum hlpos le_sqrt_D1
  have hn := div_le_div_of_nonneg_right
    (mul_le_mul_of_nonneg_right Real.pi_lt_d20.le (sq_nonneg (408406701 : Real))) hlpos.le
  have hcount : ellipsePaddedUpperCount 700000000000 408406701 488 ≤
      (3.14159265358979323847 : Real) * 408406701 ^ 2 / sqrtD1Lower + 2 * 408406701 + 977 := by
    unfold ellipsePaddedUpperCount
    norm_num only [Nat.reduceMul, Nat.reduceAdd, Nat.cast_ofNat]
    linarith
  have hs := mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hcount
    (by norm_num : (0 : Real) ≤ 2)) (by norm_num : (0 : Real) ≤ 8750000000)
  have heq : 2 * ((3.14159265358979323847 : Real) * 408406701 ^ 2 / sqrtD1Lower +
      2 * 408406701 + 977) * 8750000000 = countArgumentUpper := by
    norm_num [sqrtD1Lower, countArgumentUpper]
  rw [heq] at hs
  exact hs

theorem upper_le_budget : upper ≤ (572 * 10 ^ 31 : Real) := by
  have hnpos : (0 : Real) < 2 * ellipsePaddedUpperCount 700000000000 408406701 488 * 8750000000 := by
    unfold ellipsePaddedUpperCount
    positivity
  have hn := (Real.log_le_log hnpos count_log_argument_le).trans count_log_bounds.2
  have hr := radius_log_bounds.2
  have hratio := radius_ratio_log_bounds.2
  unfold upper enderUpperB
  norm_num only [Nat.cast_ofNat, Nat.reduceSub]
  nlinarith

def smallBudget : Real := 1324 * 10 ^ 20
def oddBudget : Real := 7995 * 10 ^ 29
def factorialBudget : Real :=
  (174999999999 : Real) ^ 2 / 2 * (25888051773431 / 1000000000000) -
    3 * 174999999999 ^ 2 / 4 + 174999999999 / 2 + 1 / 4
def tailBudget : Real := (9210440367148 / 1000000000000 : Real) / 10000 + 99995001 / 1000000000000
def tailLowerBudget : Real := ((8750000000 : Real) - 1 / 2) *
  (factorialBudget - smallBudget - triangularMass 175000000000 * tailBudget) -
    squareMass 175000000000 * tailBudget / 2

theorem factorialBudget_le : factorialBudget ≤ factorialLower 175000000000 := by
  have h := factorial_log_bounds.1
  unfold factorialBudget factorialLower
  norm_num only [Nat.reduceSub, Nat.cast_ofNat]
  nlinarith

theorem tail_le_budget : enderTailIntegral 10000 ≤ tailBudget := by
  have hp := tail_prime_log_bounds.2
  have hr := tail_ratio_log_bounds.2
  unfold enderTailIntegral tailBudget
  norm_num only [Nat.cast_ofNat]
  linarith

theorem lower_ge_budget
    (hsmall : factorialSmallMass 175000000000 10000 ≤ smallBudget)
    (hodd : oddBudget ≤ smallOddValuationMass 175000000000 8750000000 10000) :
    (581 * 10 ^ 31 : Real) ≤ lower := by
  have hfac := factorialBudget_le
  have hI := tail_le_budget
  have htail : tailLowerBudget ≤ enderTailLower 175000000000 8750000000 10000 (enderTailIntegral 10000) := by
    unfold tailLowerBudget enderTailLower triangularMass squareMass
    norm_num only [Nat.cast_ofNat]
    nlinarith
  have hclip := le_max_left (enderTailLower 175000000000 8750000000 10000 (enderTailIntegral 10000)) 0
  have hsum : 2 * (oddBudget + tailLowerBudget) ≤ lower := by
    unfold lower enderPrimeMassLower
    nlinarith
  have hrat : (581 * 10 ^ 31 : Real) ≤ 2 * (oddBudget + tailLowerBudget) := by
    norm_num [oddBudget, tailLowerBudget, factorialBudget, smallBudget, tailBudget,
      triangularMass, squareMass]
  exact hrat.trans hsum

theorem strict_comparison_of_table_budgets
    (hsmall : factorialSmallMass 175000000000 10000 ≤ smallBudget)
    (hodd : oddBudget ≤ smallOddValuationMass 175000000000 8750000000 10000) : upper < lower := by
  have hu := upper_le_budget
  have hl := lower_ge_budget hsmall hodd
  nlinarith

end
end TenthDiscriminant.FirstEnderInterval
