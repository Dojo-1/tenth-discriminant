import TenthDiscriminant.LogEnclosure

/-!
# Phase182: exact rational log bracket at the 375^4 candidate

This guards the logarithmic part only, without assuming an improved
geometric count, arithmetic lower, or actual-field theorem.
The independent rational checker includes the logarithm remainder.
-/
namespace TenthDiscriminant
set_option autoImplicit false

theorem log_375_rational_enclosure :
    (5926 / 1000 : Real) ≤ Real.log 375 ∧
    Real.log 375 ≤ (5927 / 1000 : Real) := by
  have hc :
      checkPositiveLogBounds 5 375 8 (5926 / 1000) (5927 / 1000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 375 8
    (5926 / 1000) (5927 / 1000) hc
  norm_num at h
  constructor
  · linarith [h.1]
  · exact h.2

private theorem log_375_power_four :
    Real.log (((375 : Nat) ^ 4 : Nat) : Real) =
      4 * Real.log (375 : Real) := by
  rw [Nat.cast_pow, Real.log_pow]
  ring

theorem log_large_from_375_fourth_power (D : Nat)
    (hD : (375 : Nat) ^ 4 ≤ D) :
    (237 / 10 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((375 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((375 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [log_375_power_four] at hm
  linarith [log_375_rational_enclosure.1]

/-- A fixed false-premise control: log(375^4) remains below 24. -/
theorem log_twenty_four_false_at_375_fourth_power :
    ¬ ((24 : Real) ≤ Real.log (((375 : Nat)^4 : Nat) : Real)) := by
  intro h
  rw [log_375_power_four] at h
  linarith [log_375_rational_enclosure.2]

theorem frontier_375_arithmetic_controls :
    (375 : Nat)^4 = 19775390625 ∧
    (375 : Nat)^4 < (377 : Nat)^4 := by
  norm_num

end TenthDiscriminant
