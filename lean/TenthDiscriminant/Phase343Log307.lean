import TenthDiscriminant.LogEnclosure

/-!
# Phase343 — a sound 307^4 logarithmic floor

An exact finite-series rational enclosure of log(307), and monotone
transport to log D for the hypothetical 307-domain proof programme.

This is only a NUMERIC guard: no source Gram, prime product, or field
theorem is concluded. The existing verified field theorem is unchanged.
-/
namespace TenthDiscriminant.Phase343
set_option autoImplicit false

theorem log_307_rational_enclosure :
    (5726/1000 : Real) ≤ Real.log 307 ∧
    Real.log 307 ≤ (5728/1000 : Real) := by
  have hc :
      checkPositiveLogBounds 5 307 8
        (5726/1000) (5728/1000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 307 8
      (5726/1000) (5728/1000) hc
  norm_num at h
  rcases h with ⟨hlo, hhi⟩
  constructor
  · linarith
  · linarith

theorem log_floor_from_307_fourth_power (D : Nat)
    (hD : (307 : Nat)^4 ≤ D) :
    (22904/1000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((307 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((307 : Nat)^4 : Nat) : Real) ≤
      (D : Real) := by exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [Nat.cast_pow, Real.log_pow] at hm
  have hlow : (5726/1000 : Real) ≤ Real.log (307 : Real) :=
    log_307_rational_enclosure.1
  have hscaled : (4 : Real)*(5726/1000 : Real) ≤
      (4 : Real)*Real.log (307 : Real) :=
    mul_le_mul_of_nonneg_left hlow (by norm_num)
  have heq : (4 : Real)*(5726/1000 : Real) = 22904/1000 := by
    norm_num
  rw [heq] at hscaled
  exact hscaled.trans hm

theorem fourth_power_307_control :
    (307 : Nat)^4 = 8882874001 ∧
    8882874001 < (315 : Nat)^4 := by norm_num

end TenthDiscriminant.Phase343

#print axioms TenthDiscriminant.Phase343.log_floor_from_307_fourth_power
