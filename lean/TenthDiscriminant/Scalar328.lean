import TenthDiscriminant.LogEnclosure

/-!
# Phase191: exact scalar preflight at fourth-root 328 with only original source-prime gain

These proofs concern exact rational logarithm enclosures and the affine
strict separator ALONE. No determinant lower/upper theorem, interpolation
count, class-number bridge or field cutoff is asserted here. The source
of Real.log 2 is the existing sound odd-series checker. The strengthened
-57321/10000 is conditional on Phase190's original-prime +0.0879 proof;
this file only certifies the scalar non-overlap.
-/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

theorem log_328_rational_enclosure :
    (5793 / 1000 : Real) ≤ Real.log 328 ∧
    Real.log 328 ≤ (5794 / 1000 : Real) := by
  have hc :
      checkPositiveLogBounds 5 328 8 (5793 / 1000) (5794 / 1000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 328 8
    (5793 / 1000) (5794 / 1000) hc
  norm_num at h
  constructor
  · linarith [h.1]
  · exact h.2

private theorem log_328_power_four :
    Real.log (((328 : Nat) ^ 4 : Nat) : Real) =
      4 * Real.log (328 : Real) := by
  rw [Nat.cast_pow, Real.log_pow]
  ring

theorem log_floor_from_328_fourth_power (D : Nat)
    (hD : (328 : Nat) ^ 4 ≤ D) :
    (23172 / 1000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((328 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((328 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [log_328_power_four] at hm
  linarith [log_328_rational_enclosure.1]

/-- The actual strict contradiction, without the old optional +0.098. -/
theorem strict_affine_separator_328 (u : Real)
    (hu : (23172 / 1000 : Real) ≤ u) :
    (4/5 : Real)*u-1849/2000 <
      (999997/1000000 : Real)*u-57321/10000+Real.log 2/4 := by
  have hlog2 := log_two_rational_control.1
  linarith

/-- An abstract overlap contradiction, not a construction of the Gram bound. -/
theorem no_abstract_scalar_overlap_328
    (D : Nat) (hD : (328 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-1849/2000)
    (hLower : (999997/1000000 : Real)*Real.log D-57321/10000+
      Real.log 2/4 ≤ g) : False := by
  have hu := log_floor_from_328_fourth_power D hD
  have hgap := strict_affine_separator_328 (Real.log D) hu
  linarith

/-- Falsifier: the former extra 0.098 gap is absent at the 328 floor. -/
theorem extra_098_gap_false_at_328 :
    ¬ ((4/5 : Real)*(23172/1000)-1849/2000+98/1000 <
      (999997/1000000 : Real)*(23172/1000)-57321/10000+Real.log 2/4) := by
  intro h
  have h2 := log_two_rational_control.2
  linarith

/-- Falsifier: the same scalar envelopes do not separate at log D = 23.16. -/
theorem scalar_strict_gap_false_at_23_point_16 :
    ¬ ((4/5 : Real)*(579/25)-1849/2000 <
      (999997/1000000 : Real)*(579/25)-57321/10000+Real.log 2/4) := by
  intro h
  have h2 := log_two_rational_control.2
  linarith

theorem fourth_power_328_control :
    (328 : Nat)^4 = 11574317056 ∧
    (327 : Nat)^4 < (328 : Nat)^4 := by
  norm_num

end
end TenthDiscriminant
