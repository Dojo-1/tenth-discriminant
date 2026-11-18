import TenthDiscriminant.E19EuclidLogGuards300
import TenthDiscriminant.E16Dimensions300

/-!
# E20 — Original Euclid upper count and normalized log error at D>=300^4

The integer support is the E6 original ellipse, no padding/Y resampling.
To avoid needlessly sharp estimates, certify n<=16D and use
log(32 D^2) <= 5+2log D. The 1/4000 normalized budget is conservative.
-/
namespace TenthDiscriminant.E20
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Uniform logarithmic overhead bound, adapted to the E16 dimension floor.
No 307-specific theorem is silently weakened. -/
theorem euclid_log_D_over_R_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    Real.log (D : Real)/(FirstCertificate.Tuned.R D : Real) ≤
      1/9000 := by
  have hi := fourthRoot_identities D
  have ht := E18.fourthRoot_ge_300 D hD
  have hd := FirstCertificate.Tuned.dimensions_300 D hD
  have hspos : 0 < Real.sqrt (D : Real) := by
    rw [← hi.2.1]
    positivity
  have hrpos : (0 : Real) < FirstCertificate.Tuned.R D := by
    exact_mod_cast (show 0 < FirstCertificate.Tuned.R D by omega)
  have hlog := Real.log_le_sub_one_of_pos hspos
  have he : 2*Real.log (Real.sqrt D)=Real.log D := by
    have h := congrArg Real.log
      (Real.sq_sqrt (Nat.cast_nonneg D : (0 : Real) ≤ D))
    rw [Real.log_pow] at h
    simpa only [Nat.cast_ofNat] using h
  have hs : (90000 : Real) ≤ Real.sqrt D := by
    rw [← hi.2.1]
    nlinarith [sq_nonneg (fourthRoot D-300)]
  have hsq := Real.sq_sqrt (Nat.cast_nonneg D : (0 : Real) ≤ D)
  have hg := mul_nonneg hspos.le
    (show 0 ≤ Real.sqrt D-90000 by linarith)
  apply (div_le_iff₀ hrpos).2
  have hR := hd.2.2.2.2.1
  nlinarith only [hlog,he,hg,hsq,hR]

theorem euclid_log_ratio_over_R_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    Real.log ((FirstCertificate.Tuned.R D : Real) /
      FirstCertificate.Tuned.euclidRadius D) /
        FirstCertificate.Tuned.R D ≤ 1/9000 := by
  have hρpos : (0 : Real) < FirstCertificate.Tuned.euclidRadius D := by
    have hg := (FirstCertificate.Tuned.euclid_radius_guards_252 D
      (by omega : (252 : Nat)^4 ≤ D)).1
    exact_mod_cast (show 0 < FirstCertificate.Tuned.euclidRadius D by omega)
  have hrpos : (0 : Real) < FirstCertificate.Tuned.R D := by
    exact_mod_cast (show 0 < FirstCertificate.Tuned.R D by omega)
  have hR : 4*FirstCertificate.Tuned.R D ≤ D := by
    unfold FirstCertificate.Tuned.R envelopeR
    omega
  have hRreal : (FirstCertificate.Tuned.R D : Real) ≤ D := by
    have he : (4 : Real)*FirstCertificate.Tuned.R D ≤ D := by
      exact_mod_cast hR
    linarith
  have hρone : (1 : Real) ≤ FirstCertificate.Tuned.euclidRadius D := by
    exact_mod_cast (show 1 ≤ FirstCertificate.Tuned.euclidRadius D by omega)
  have hDpos : (0 : Real) < D := by
    exact_mod_cast (show 0 < D by omega)
  have hrat :
      (FirstCertificate.Tuned.R D : Real)/
      FirstCertificate.Tuned.euclidRadius D ≤ (D : Real) := by
    apply (div_le_iff₀ hρpos).2
    nlinarith only [hRreal,hρone,hDpos.le]
  have hlog := Real.log_le_log (div_pos hrpos hρpos) hrat
  have hlogD := euclid_log_D_over_R_300 D hD
  apply (div_le_iff₀ hrpos).2
  have hlogD' := (div_le_iff₀ hrpos).mp hlogD
  linarith

/-- A generous polynomial upper count with the SAME ellipse and
the source inward-cell majorant; 16D suffices for the log budget. -/
theorem euclid_ellipse_upper_count_le_16D_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    ellipseUpperCount D (FirstCertificate.Tuned.euclidRadius D) ≤
      16*(D : Real) := by
  let t : Real := fourthRoot D
  let rho : Nat := FirstCertificate.Tuned.euclidRadius D
  have ht : (300 : Real) ≤ t := E18.fourthRoot_ge_300 D hD
  have htpos : (0 : Real) < t := by linarith
  have htone : (1 : Real) ≤ t := by linarith
  have hi := fourthRoot_identities D
  have ht2 : t^2 = Real.sqrt D := by simpa [t] using hi.2.1
  have ht4 : t^4 = (D : Real) := by simpa [t] using hi.2.2
  have hsc : (0 : Real) < Real.sqrt D := by
    rw [← ht2]
    positivity
  have hrho := (E18.euclid_radius_coeff_300 D hD).2
  have hcubepos : (0 : Real) ≤ t^3 := pow_nonneg (by linarith) 3
  have hρcube : (rho : Real) ≤ t^3 := by
    dsimp [rho, t]
    nlinarith only [hrho,hcubepos]
  have hρpos : (0 : Real) ≤ rho := Nat.cast_nonneg _
  have hρsq := pow_le_pow_left₀ hρpos hρcube 2
  have hpi := mul_le_mul_of_nonneg_right Real.pi_lt_four.le
    (sq_nonneg (rho : Real))
  have hterm :
      Real.pi * (rho : Real)^2 / Real.sqrt D ≤ 4*(D : Real) := by
    apply (div_le_iff₀ hsc).2
    rw [← ht2, ← ht4]
    nlinarith only [hρsq,hpi]
  have hfloor :
      ((ellipseVerticalBound D rho : Nat) : Real) ≤
        (rho : Real) / Real.sqrt D := by
    unfold ellipseVerticalBound
    exact Nat.floor_le (by positivity)
  have hrdiv : (rho : Real)/Real.sqrt D ≤ t := by
    apply (div_le_iff₀ hsc).2
    rw [← ht2]
    nlinarith only [hρcube]
  have hY : ((ellipseVerticalBound D rho : Nat) : Real) ≤ t :=
    hfloor.trans hrdiv
  have hp3 : t^3 ≤ t^4 :=
    pow_le_pow_right₀ htone (by decide)
  have hp1 : t ≤ t^4 := by
    have hh : t^1 ≤ t^4 :=
      pow_le_pow_right₀ htone (by decide)
    simpa using hh
  have hD1 : (1 : Real) ≤ D := by
    rw [←ht4]
    have hh : (1 : Real)^4 ≤ t^4 :=
      pow_le_pow_left₀ (by norm_num) htone 4
    simpa using hh
  unfold ellipseUpperCount
  push_cast
  rw [←ht4]
  nlinarith only [hterm,hρcube,hY,hp1,hp3,hD1,ht4]

/-- The normalized count-log error <= 1/4000 with n=ellipseUpperCount.
No dependence on floating-point counts or asymptotic O-terms. -/
theorem euclid_count_log_over_R_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    Real.log (2*ellipseUpperCount D
      (FirstCertificate.Tuned.euclidRadius D) *
      FirstCertificate.Tuned.S D) /
      FirstCertificate.Tuned.R D ≤ 1/4000 := by
  let n : Real := ellipseUpperCount D (FirstCertificate.Tuned.euclidRadius D)
  have hn : n ≤ 16*(D : Real) :=
    euclid_ellipse_upper_count_le_16D_300 D hD
  have hDnat : 0 < D := by omega
  have hdp : (0 : Real) < D := by exact_mod_cast hDnat
  have hSpos : 0 < FirstCertificate.Tuned.S D := by
    unfold FirstCertificate.Tuned.S FirstCertificate.Tuned.R envelopeR
    omega
  have hs : (0 : Real) < FirstCertificate.Tuned.S D := by exact_mod_cast hSpos
  have hR : (0 : Real) < FirstCertificate.Tuned.R D := by
    exact_mod_cast (show 0 < FirstCertificate.Tuned.R D by omega)
  have hS : (FirstCertificate.Tuned.S D : Real) ≤ D := by
    have hh : FirstCertificate.Tuned.S D ≤ D := by
      unfold FirstCertificate.Tuned.S FirstCertificate.Tuned.R envelopeR
      omega
    exact_mod_cast hh
  have hnp : 0 < n := by
    dsimp [n]
    unfold ellipseUpperCount
    positivity
  have harg : 2*n*FirstCertificate.Tuned.S D ≤
      32*(D : Real)^2 := by
    have hm := mul_le_mul hn hS hs.le
      (by positivity : (0 : Real) ≤ 16*(D : Real))
    nlinarith only [hm]
  have hl := Real.log_le_log (by positivity : 0 <
    2*n*FirstCertificate.Tuned.S D) harg
  rw [Real.log_mul (by norm_num : (32 : Real) ≠ 0)
    (pow_ne_zero _ hdp.ne'),Real.log_pow] at hl
  have h32 : Real.log (32 : Real) ≤ 5 := by
    have he : (32 : Real) = 2^5 := by norm_num
    rw [he, Real.log_pow]
    norm_num only [Nat.cast_ofNat]
    linarith [Real.log_le_sub_one_of_pos (by norm_num : (0 : Real) < 2)]
  have hlog := (div_le_iff₀ hR).mp
    (euclid_log_D_over_R_300 D hD)
  have hd := FirstCertificate.Tuned.dimensions_300 D hD
  have hRl : (100000000 : Real) ≤ FirstCertificate.Tuned.R D := by
    exact_mod_cast hd.1
  apply (div_le_iff₀ hR).2
  dsimp [n] at hl ⊢
  linarith only [hl,h32,hlog,hRl]

end
end TenthDiscriminant.E20

#print axioms TenthDiscriminant.E20.euclid_log_D_over_R_300
#print axioms TenthDiscriminant.E20.euclid_ellipse_upper_count_le_16D_300
#print axioms TenthDiscriminant.E20.euclid_count_log_over_R_300
