import TenthDiscriminant.LogEnclosure

/-!
Phase332: sound finite-series logarithm floor at the possible
313^4 field threshold. This is an analytic *numeric guard* only.

The source Gram mixed H(Z,W) row action, 313-domain geometry
and full field theorem remain open. No external Heegner classification.
-/
namespace TenthDiscriminant.Phase332
set_option autoImplicit false

theorem log_313_rational_enclosure :
    (5746/1000 : Real) ≤ Real.log 313 ∧
    Real.log 313 ≤ (5747/1000 : Real) := by
  have hc :
      checkPositiveLogBounds 5 313 8
        (5746/1000) (5747/1000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 313 8
      (5746/1000) (5747/1000) hc
  norm_num at h
  exact h

theorem log_floor_from_313_fourth_power (D : Nat)
    (hD : (313 : Nat)^4 ≤ D) :
    (22984/1000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((313 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((313 : Nat)^4 : Nat) : Real) ≤
      (D : Real) := by exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [Nat.cast_pow, Real.log_pow] at hm
  linarith [log_313_rational_enclosure.1]

theorem fourth_power_313_control :
    (313 : Nat)^4 = 9597924961 ∧
    9597924961 < (315 : Nat)^4 := by norm_num

end TenthDiscriminant.Phase332

#print axioms TenthDiscriminant.Phase332.log_floor_from_313_fourth_power
