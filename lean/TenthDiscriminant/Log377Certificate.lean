import TenthDiscriminant.LogEnclosure

/-!
# Phase169 — exact rational logarithm certificate at the 377^4 frontier

The old geometric proof uses 24 ≤ log D for D ≥ 450^4.
At the proposed lower anchor 377^4 this inequality is FALSE.
Rather than reusing it, certify a weaker TRUE lower bracket by the
already proved positive-rational logarithm enclosure checker.

No other large-D geometric, prime-tail, field or analytic statement
is weakened or assumed in this file. This is NOT a discriminant bound.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- A rational interval derived by a SOUND finite checker. The checker
uses the odd-log power series WITH its upper-tail remainder, rather than
uncertified decimal approximations. -/
theorem log_377_rational_enclosure :
    (593 / 100 : Real) ≤ Real.log 377 ∧
    Real.log 377 ≤ (594 / 100 : Real) := by
  have hc :
      checkPositiveLogBounds 5 377 8 (593 / 100) (594 / 100) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 377 8 (593 / 100) (594 / 100) hc
  norm_num at h
  constructor
  · exact h.1
  · calc
      Real.log 377 ≤ (297 / 50 : Real) := h.2
      _ = (594 / 100 : Real) := by norm_num

private theorem log_377_power_four :
    Real.log (((377 : Nat) ^ 4 : Nat) : Real) =
      4 * Real.log (377 : Real) := by
  rw [Nat.cast_pow, Real.log_pow]
  ring

/-- Replacement for the false 24 <= log D premise at the NEW anchor.
This establishes only a numerical LOG guard, not the rest of the
production geometric hypotheses below the proven 450^4 floor. -/
theorem log_large_from_377_fourth_power (D : Nat)
    (hD : (377 : Nat) ^ 4 ≤ D) :
    (237 / 10 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((377 : Nat) ^ 4 : Nat) : Real) := by norm_num
  have hDreal : (((377 : Nat) ^ 4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [log_377_power_four] at hm
  linarith [log_377_rational_enclosure.1]

/-- A regression that KILLS blind reuse of the current 24-log proof at
D = 377^4. It is an exact result using an upper log certificate. -/
theorem log_twenty_four_false_at_377_fourth_power :
    ¬ ((24 : Real) ≤ Real.log (((377 : Nat) ^ 4 : Nat) : Real)) := by
  intro h
  rw [log_377_power_four] at h
  linarith [log_377_rational_enclosure.2]

/-- The proposed lower anchor is exactly 20,200,652,641; it is
strictly smaller than the already proved 450^4 cutoff. -/
theorem frontier_arithmetic_controls :
    (377 : Nat)^4 = 20200652641 ∧ (377 : Nat)^4 < (450 : Nat)^4 := by
  norm_num

end TenthDiscriminant
