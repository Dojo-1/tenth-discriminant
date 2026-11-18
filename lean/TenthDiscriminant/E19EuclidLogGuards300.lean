import TenthDiscriminant.E18EuclidGuards300
import TenthDiscriminant.LogEnclosure

/-!
# E19 — Two uniform logarithmic guards on the original reduced ellipse

The source rho=ceil(81/200*t^3), t=D^(1/4) is unchanged.
The logarithm of the rho coefficient is certified by the existing
finite odd-log series with an explicit remainder, not a decimal guess.
The R/rho upper log uses log(x)<=x-1 at x=50/81.
-/
namespace TenthDiscriminant.E19
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem log_203_over_500_upper :
    Real.log (203/500 : Real) ≤ -(22/25 : Real) := by
  have hc :
      checkPositiveLogBounds 5 (500/203) 1
        (22/25) 1 = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ]
  have hlo := (checkPositiveLogBounds_sound 5 (500/203) 1
    (22/25) 1 hc).1
  have hrecip : (203/500 : Real) = (500/203 : Real)⁻¹ := by
    norm_num
  rw [hrecip,Real.log_inv]
  linarith

/-- Identity for logarithms of the positive fourth-root parameter. -/
theorem log_fourthRoot (D : Nat) :
    (4 : Real)*Real.log (fourthRoot D) =
      Real.log (D : Real) := by
  have hi := fourthRoot_identities D
  have h := congrArg Real.log hi.2.2
  rw [Real.log_pow] at h
  simpa only [Nat.cast_ofNat] using h

/-- Exact E17 log(radius) guard for all real fourth-root values >=300. -/
theorem euclid_log_radius_upper_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    Real.log (FirstCertificate.Tuned.euclidRadius D : Real) ≤
      (3/4 : Real)*Real.log (D : Real)-22/25 := by
  have ht := E18.fourthRoot_ge_300 D hD
  have htpos : (0 : Real) < fourthRoot D := by linarith
  have hρ : (0 : Real) < FirstCertificate.Tuned.euclidRadius D := by
    have hg := (FirstCertificate.Tuned.euclid_radius_guards_252 D
      (by omega : (252 : Nat)^4 ≤ D)).1
    exact_mod_cast (show 0 < FirstCertificate.Tuned.euclidRadius D by omega)
  have hu := (E18.euclid_radius_coeff_300 D hD).2
  have hlog := Real.log_le_log hρ hu
  rw [Real.log_mul (by norm_num : (203/500 : Real) ≠ 0)
    (pow_ne_zero _ htpos.ne'),Real.log_pow] at hlog
  have hroot := log_fourthRoot D
  linarith [log_203_over_500_upper]

/-- The R/rho upper guard uses only source R<=D/4 and rho>=.405 t^3.
The coefficient 31/81 comes from exact log x <= x-1 at x=50/81. -/
theorem euclid_log_R_over_radius_upper_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    Real.log ((FirstCertificate.Tuned.R D : Real)/
      FirstCertificate.Tuned.euclidRadius D) ≤
      (1/4 : Real)*Real.log (D : Real)-31/81 := by
  let t : Real := fourthRoot D
  have ht : (300 : Real) ≤ t := E18.fourthRoot_ge_300 D hD
  have htpos : (0 : Real) < t := by linarith
  have hρ : (0 : Real) < FirstCertificate.Tuned.euclidRadius D := by
    have hr := (FirstCertificate.Tuned.euclid_radius_guards_252 D
      (by omega : (252 : Nat)^4 ≤ D)).1
    exact_mod_cast (show 0 < FirstCertificate.Tuned.euclidRadius D by omega)
  have hRpos : (0 : Real) < FirstCertificate.Tuned.R D := by
    exact_mod_cast (show 0 < FirstCertificate.Tuned.R D by
      unfold FirstCertificate.Tuned.R envelopeR
      omega)
  have hRfloor : 4*FirstCertificate.Tuned.R D ≤ D := by
    unfold FirstCertificate.Tuned.R envelopeR
    omega
  have hRreal : (FirstCertificate.Tuned.R D : Real) ≤
      (D : Real)/4 := by
    have h := (show (4*FirstCertificate.Tuned.R D : Nat) ≤ D from hRfloor)
    have h' : (4 : Real)*FirstCertificate.Tuned.R D ≤ D := by
      exact_mod_cast h
    linarith
  have hlow := (E18.euclid_radius_coeff_300 D hD).1
  have hmul := mul_le_mul_of_nonneg_left hlow
    (show (0 : Real) ≤ (50/81 : Real)*t by positivity)
  have hRproduct : (FirstCertificate.Tuned.R D : Real) ≤
      (50/81 : Real)*t*FirstCertificate.Tuned.euclidRadius D := by
    have h4 : t^4 = (D : Real) := by
      simpa only [t] using (fourthRoot_identities D).2.2
    rw [←h4] at hRreal
    dsimp [t] at hmul ⊢
    nlinarith only [hRreal,hmul]
  have hratio :
      (FirstCertificate.Tuned.R D : Real)/
        FirstCertificate.Tuned.euclidRadius D ≤ (50/81 : Real)*t :=
    (div_le_iff₀ hρ).2 hRproduct
  have hlog := Real.log_le_log (div_pos hRpos hρ) hratio
  rw [Real.log_mul (by norm_num : (50/81 : Real) ≠ 0) htpos.ne'] at hlog
  have hcoef := Real.log_le_sub_one_of_pos
    (by norm_num : (0 : Real) < 50/81)
  have hroot := log_fourthRoot D
  dsimp [t] at hlog ⊢
  linarith

end
end TenthDiscriminant.E19

#print axioms TenthDiscriminant.E19.log_203_over_500_upper
#print axioms TenthDiscriminant.E19.euclid_log_radius_upper_300
#print axioms TenthDiscriminant.E19.euclid_log_R_over_radius_upper_300
