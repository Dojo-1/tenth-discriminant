import TenthDiscriminant.Phase356Radius302
import TenthDiscriminant.Phase355Scalar302
import TenthDiscriminant.Phase332StrongerRadius315

/-!
# Phase361: stronger original thin/padded radius and conditional 301 scalar gap

The source and R,S,J, ordinary Z derivatives, trace and integer Gram
are NOT changed. This file proves NEW radius/scalar inputs only; a
301 original padded analytic upper, same-Gram odd/binary lower and
actual-field theorem remain separate H. The PREEXISTING Phase355 301
negative control still applies to the old -1923/2000 upper.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

theorem fourthRoot_ge_301 (D : Nat) (hD : (301 : Nat)^4 ≤ D) :
    (301 : Real) ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (301 : Nat)^2^2 ≤ D by omega)

/-- At D>=301^4 the original thin/padded CEIL radii satisfy a
strictly sharper rational envelope than 17/20. -/
theorem thin_radius_fraction_847_1000_301 (D : Nat)
    (hD : (301 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (847/1000 : Real)*(rho D : Real) := by
  have ht := fourthRoot_ge_301 D hD
  have hcube : (301 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hlarge : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  nlinarith only [hcube,hceil,hlarge]

/-- Generic stronger same-original-Ender-B radius gain:
(9/10)*(153/1000)=1377/10000. No change to the Gram. -/
theorem upperB_strong_847_1000_saving (R S oldRad smallRad : Nat) (n : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (h25 : 25*S ≤ R)
    (hOld : 0 < oldRad) (hSmall : 0 < smallRad)
    (hratio : (smallRad : Real) ≤ (847/1000 : Real)*(oldRad : Real)) :
    enderUpperB R S S smallRad n/comparisonScale R S+1377/10000 ≤
      enderUpperB R S S oldRad n/comparisonScale R S := by
  have hRreal : (2 : Real) ≤ R := by exact_mod_cast hR
  have hSreal : (1 : Real) ≤ S := by exact_mod_cast hS
  have h25real : (25 : Real)*S ≤ R := by exact_mod_cast h25
  have hmul : (0 : Real) ≤ ((R : Real)+2)*((R : Real)-25*S) :=
    mul_nonneg (by linarith) (by linarith)
  have hquad : (0 : Real) ≤ (R : Real)*((R : Real)-2) :=
    mul_nonneg (by linarith) (by linarith)
  have hcoef : (9/10 : Real)*(R : Real)^2 ≤
      (R : Real)^2-(R : Real)*S-2*((S : Real)-1) := by
    nlinarith only [hmul, hquad, hRreal, hSreal]
  have hcoefbig : (9/10 : Real)*(R : Real)^2*(S : Real) ≤
      (S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1)) := by
    nlinarith only [hcoef, hSreal]
  have hcoefpos :
      0 ≤ (S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1)) := by
    nlinarith only [hcoefbig, hSreal, sq_nonneg (R : Real)]
  have hOldReal : (0 : Real) < oldRad := by exact_mod_cast hOld
  have hSmallReal : (0 : Real) < smallRad := by exact_mod_cast hSmall
  have hfracpos : (0 : Real) < (smallRad : Real)/(oldRad : Real) :=
    div_pos hSmallReal hOldReal
  have hfrac : (smallRad : Real)/(oldRad : Real) ≤ 847/1000 :=
    (div_le_iff₀ hOldReal).2 (by linarith [hratio])
  have hlog := Real.log_le_sub_one_of_pos hfracpos
  rw [Real.log_div hSmallReal.ne' hOldReal.ne'] at hlog
  have hloggap : (153/1000 : Real) ≤
      Real.log (oldRad : Real)-Real.log (smallRad : Real) := by linarith
  have hdiff : (0 : Real) ≤ (oldRad : Real)-(smallRad : Real) := by
    linarith [hratio]
  have hSminus : (0 : Real) ≤ (S : Real)-1 := by linarith
  have hnonneg : 0 ≤
      2*(S : Real)*((S : Real)-1)*((oldRad : Real)-(smallRad : Real)) := by
    positivity
  have hraw : (1377/10000 : Real)*comparisonScale R S ≤
      enderUpperB R S S oldRad n-enderUpperB R S S smallRad n := by
    calc
      (1377/10000 : Real)*comparisonScale R S =
          ((9/10 : Real)*(R : Real)^2*(S : Real))*(153/1000) := by
            unfold comparisonScale
            ring
      _ ≤ ((S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1)))*(153/1000) :=
        mul_le_mul_of_nonneg_right hcoefbig (by norm_num)
      _ ≤ (S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1))*
          (Real.log (oldRad : Real)-Real.log (smallRad : Real)) :=
        mul_le_mul_of_nonneg_left hloggap hcoefpos
      _ ≤ _ := by linarith [hnonneg]
      _ = _ := (upperB_radius_difference R S oldRad smallRad n
        (by omega) hS hOld hSmall).symm
  have hscale : 0 < comparisonScale R S :=
    comparisonScale_pos R S (by omega) (by omega)
  have hnorm : (1377/10000 : Real) ≤
      (enderUpperB R S S oldRad n-enderUpperB R S S smallRad n)/
        comparisonScale R S := by
    apply (le_div_iff₀ hscale).2
    simpa only [mul_comm] using hraw
  rw [sub_div] at hnorm
  linarith

/-- Apply the stricter generic bound to the unchanged original
thinRadius and rho for every integer D >= 301^4. -/
theorem original_radius_saving_301 (D : Nat)
    (hD : (301 : Nat)^4 ≤ D) (n : Real) :
    enderUpperB (R D) (S D) (S D) (thinRadius D) n /
        comparisonScale (R D) (S D) + 1377/10000 ≤
      enderUpperB (R D) (S D) (S D) (rho D) n /
        comparisonScale (R D) (S D) := by
  have hR : 2 ≤ R D := by
    unfold R envelopeR
    omega
  have hS : 1 ≤ S D := by
    unfold S R envelopeR
    omega
  have h25 : 25*S D ≤ R D := by
    unfold S
    omega
  have ht : (0 : Real) < fourthRoot D := by
    linarith [fourthRoot_ge_301 D hD]
  have hcube : (0 : Real) < fourthRoot D^3 := pow_pos ht 3
  have hOldLower : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  have hSmallLower : (11/25 : Real)*fourthRoot D^3 ≤ thinRadius D := by
    unfold thinRadius
    exact Nat.le_ceil _
  have hOldReal : (0 : Real) < rho D := by
    nlinarith only [hcube,hOldLower]
  have hSmallReal : (0 : Real) < thinRadius D := by
    nlinarith only [hcube,hSmallLower]
  have hOld : 0 < rho D := by exact_mod_cast hOldReal
  have hSmall : 0 < thinRadius D := by exact_mod_cast hSmallReal
  exact upperB_strong_847_1000_saving
    (R D) (S D) (rho D) (thinRadius D) n
    hR hS h25 hOld hSmall (thin_radius_fraction_847_1000_301 D hD)

end
end TenthDiscriminant.FirstCertificate.Tuned

namespace TenthDiscriminant.Phase361
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Uniform rational-series lower log floor at root 301; inherited
log301 enclosure is checked in Phase355. -/
theorem log_floor_from_301_fourth_power (D : Nat)
    (hD : (301 : Nat)^4 ≤ D) :
    (22828/1000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((301 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((301 : Nat)^4 : Nat) : Real) ≤
      (D : Real) := by exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [Nat.cast_pow, Real.log_pow] at hm
  have hlow : (5707/1000 : Real) ≤ Real.log (301 : Real) :=
    TenthDiscriminant.Phase355.log_301_rational_enclosure.1
  have hscaled : (4 : Real)*(5707/1000 : Real) ≤
      (4 : Real)*Real.log (301 : Real) :=
    mul_le_mul_of_nonneg_left hlow (by norm_num)
  have heq : (4 : Real)*(5707/1000 : Real) = 22828/1000 := by
    norm_num
  rw [heq] at hscaled
  exact hscaled.trans hm

/-- SAME pre-existing arithmetic lower expression, but with a stronger
conditioned radius-derived analytic target -4821/5000 at 301^4. -/
theorem strong_scalar_separation_301_with_sharp_radius (D : Nat)
    (hD : (301 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D-4821/5000 <
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) := by
  have hlog := log_floor_from_301_fourth_power D hD
  have hlog2 := TenthDiscriminant.log_two_rational_control.1
  have hDint : 8208541201 ≤ D := by
    have he : (301 : Nat)^4 = 8208541201 := by norm_num
    simpa only [he] using hD
  have hDreal : (8208541201 : Real) ≤ (D : Real) :=
    by exact_mod_cast hDint
  have hDpos : (0 : Real) < D := by linarith
  have hDden : (0 : Real) < 625000*(D : Real) := by positivity
  have hDerr : (16895455 : Real)/(625000*(D : Real)) ≤ 1/100000 := by
    apply (div_le_iff₀ hDden).2
    nlinarith only [hDreal]
  have hRnat : 100000000 ≤ Tuned.R D := by
    unfold Tuned.R envelopeR
    omega
  have hRreal : (100000000 : Real) ≤ Tuned.R D :=
    by exact_mod_cast hRnat
  have hRpos : (0 : Real) < (Tuned.R D : Real) := by linarith
  have hRerr : (2 : Real)/(Tuned.R D : Real) +
      40/(Tuned.R D : Real) ≤ 1/1000000 := by
    calc
      (2 : Real)/(Tuned.R D : Real) +
        40/(Tuned.R D : Real) = 42/(Tuned.R D : Real) := by ring
      _ ≤ 1/1000000 := by
        apply (div_le_iff₀ hRpos).2
        nlinarith only [hRreal]
  linarith only [hlog,hlog2,hDerr,hRerr]

/-- Purely conditional numeric contradiction. NOT a bound on any
field or sampled Gram unless separate same-original-source inequalities
are proved at this weaker domain. -/
theorem no_scalar_overlap_301_with_sharp_radius
    (D : Nat) (hD : (301 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-4821/5000)
    (hLower :
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) ≤ g) :
    False := by
  have hgap := strong_scalar_separation_301_with_sharp_radius D hD
  linarith

end
end TenthDiscriminant.Phase361

#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_fraction_847_1000_301
#print axioms TenthDiscriminant.FirstCertificate.Tuned.upperB_strong_847_1000_saving
#print axioms TenthDiscriminant.FirstCertificate.Tuned.original_radius_saving_301
#print axioms TenthDiscriminant.Phase361.log_floor_from_301_fourth_power
#print axioms TenthDiscriminant.Phase361.strong_scalar_separation_301_with_sharp_radius
#print axioms TenthDiscriminant.Phase361.no_scalar_overlap_301_with_sharp_radius
