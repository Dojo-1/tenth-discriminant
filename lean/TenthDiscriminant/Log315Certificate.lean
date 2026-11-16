import TenthDiscriminant.LogEnclosure

/-!
# Phase323-E: sound logarithm enclosure at the 315^4 endpoint

This is a numerical guard only. It does not assert the arithmetic lower,
analytic upper, or an actual-field discriminant theorem.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Finite odd-power-series certificate for log(315), including the
geometric upper-tail remainder. -/
theorem log_315_rational_enclosure :
    (57524/10000 : Real) ≤ Real.log 315 ∧
    Real.log 315 ≤ (5753/1000 : Real) := by
  have hc :
      checkPositiveLogBounds 5 315 8
        (57524/10000) (5753/1000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 315 8
    (57524/10000) (5753/1000) hc
  norm_num at h
  rcases h with ⟨hlo, hhi⟩
  constructor
  · linarith
  · exact hhi

private theorem log_315_power_four :
    Real.log (((315 : Nat)^4 : Nat) : Real) =
      4*Real.log (315 : Real) := by
  rw [Nat.cast_pow, Real.log_pow]
  ring

/-- Sound lower logarithm on the entire proposed 315^4 domain. -/
theorem log_floor_from_315_fourth_power (D : Nat)
    (hD : (315 : Nat)^4 ≤ D) :
    (230096/10000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((315 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((315 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [log_315_power_four] at hm
  linarith [log_315_rational_enclosure.1]

/-- Exact endpoint arithmetic. -/
theorem frontier_315_arithmetic_control :
    (315 : Nat)^4 = 9845600625 ∧
    (315 : Nat)^4 < (321 : Nat)^4 := by
  norm_num

end TenthDiscriminant

#print axioms TenthDiscriminant.log_floor_from_315_fourth_power
