import TenthDiscriminant.SourceGeometry328
import TenthDiscriminant.Scalar328
import TenthDiscriminant.LogEnclosure

/-!
# Phase196A — independently check the 327 scalar floor and sharper radius logarithm

This is a source-preserving *preflight*, not a same-Gram upper/lower
inequality and NOT an actual-field cutoff at 327^4.

No change to Qthin, the integer ordinary-Z jets, the trace weights, R, S,
or the original source radius rho. The 328 field theorem remains unchanged.
The only new analytic ingredient is keeping another digit from the existing
rho <= 521/1000 * D^(3/4) bound.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

theorem fourthRoot_ge_327 (D : Nat) (hD : (327 : Nat)^4 <= D) :
    (327 : Real) <= fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (327 : Nat)^2^2 <= D by omega)

/-- The same original padded integer radius, at 327^4. -/
theorem rho_upper_327 (D : Nat) (hD : (327 : Nat)^4 <= D) :
    (rho D : Real) <= (521/1000 : Real)*fourthRoot D^3 := by
  have ht := fourthRoot_ge_327 D hD
  have hcube : (327 : Real)^3 <= fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (rho D : Real) <
      (13/25 : Real)*fourthRoot D^3+1 := by
    unfold rho
    exact Nat.ceil_lt_add_one (by positivity)
  nlinarith only [hcube,hceil]

/-- A sound log2 bracket and log(1+x)<=x improve -0.650 to -0.651
without a new approximation or altered radius. -/
theorem log_521_over_1000_le_neg_651 :
    Real.log (521/1000 : Real) <= -651/1000 := by
  have he : (521/500 : Real) = 2*(521/1000) := by norm_num
  have h := Real.log_le_sub_one_of_pos
    (by norm_num : (0 : Real) < 521/500)
  rw [he, Real.log_mul
    (by norm_num : (2 : Real) ≠ 0)
    (by norm_num : (521/1000 : Real) ≠ 0)] at h
  have h2 := TenthDiscriminant.log_two_rational_control.1
  linarith

/-- Sharpen the real upper log on the *same* old rho at the 327 floor.
This alone says nothing about the normalized Hadamard upper or a field. -/
theorem log_radius_upper_327_sharp (D : Nat)
    (hD : (327 : Nat)^4 <= D) :
    Real.log (rho D) <= (3/4 : Real)*Real.log D-651/1000 := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_327 D hD
  have htpos : 0 < fourthRoot D := by linarith
  have hrpos : (0 : Real) < rho D := by
    have hlow : (13/25 : Real)*fourthRoot D^3 <= rho D := by
      unfold rho
      exact Nat.le_ceil _
    nlinarith only [hlow, pow_pos htpos 3]
  have hlog := Real.log_le_log hrpos (rho_upper_327 D hD)
  rw [Real.log_mul (by norm_num : (521/1000 : Real) ≠ 0)
      (pow_ne_zero _ htpos.ne'),Real.log_pow] at hlog
  have hroot : 4*Real.log (fourthRoot D) = Real.log D := by
    have h := congrArg Real.log hi.2.2
    rw [Real.log_pow] at h
    simpa only [Nat.cast_ofNat] using h
  norm_num only [Nat.cast_ofNat] at hlog
  linarith [log_521_over_1000_le_neg_651]

end
end TenthDiscriminant.FirstCertificate.Tuned

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

/-- N=5, x=327=2^8(327/256), z=(327-256)/(327+256)=71/583.
The remainder is bounded by the existing sound finite-series checker. -/
theorem log_327_rational_enclosure :
    (57899/10000 : Real) <= Real.log 327 ∧
    Real.log 327 <= (579/100 : Real) := by
  have hc :
      checkPositiveLogBounds 5 327 8 (57899/10000) (579/100) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 327 8
    (57899/10000) (579/100) hc
  norm_num at h
  constructor
  · linarith [h.1]
  · linarith [h.2]

private theorem log_327_power_four :
    Real.log (((327 : Nat)^4 : Nat) : Real) =
      4*Real.log (327 : Real) := by
  rw [Nat.cast_pow,Real.log_pow]
  ring

theorem log_floor_from_327_fourth_power (D : Nat)
    (hD : (327 : Nat)^4 <= D) :
    (231596/10000 : Real) <= Real.log (D : Real) := by
  have hsmall : (0 : Real) < (((327 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((327 : Nat)^4 : Nat) : Real) <= (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [log_327_power_four] at hm
  linarith [log_327_rational_enclosure.1]

/-- Exact conditional scalar separator. Neither determinant inequality
is asserted by this lemma. -/
theorem strict_affine_separator_327 (u : Real)
    (hu : (231596/10000 : Real) <= u) :
    (4/5 : Real)*u-1851/2000 <
      (999997/1000000 : Real)*u-57305/10000+Real.log 2/4 := by
  have h2 := log_two_rational_control.1
  linarith

/-- The actual positive *rational* separation used by the scalar step. -/
theorem exact_327_scalar_margin :
    (999997/1000000-4/5 : Real)*(231596/10000)
      -57305/10000+1851/2000+6931/40000 =
        (313803/2500000000 : Real) ∧
      (0 : Real) < 313803/2500000000 := by
  norm_num

/-- Falsifier: the same affine envelopes do not separate at log D=23.15. -/
theorem smaller_327_log_floor_rejected :
    ¬ ((4/5 : Real)*(463/20)-1851/2000 <
      (999997/1000000 : Real)*(463/20)-57305/10000+Real.log 2/4) := by
  intro h
  have h2 := log_two_rational_control.2
  linarith

theorem fourth_power_327_control :
    (327 : Nat)^4 = 11433811041 ∧
    (327 : Nat)^4 < (328 : Nat)^4 := by
  norm_num

end
end TenthDiscriminant
