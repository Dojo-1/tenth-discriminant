import TenthDiscriminant.Phase323ThinUpper315
import TenthDiscriminant.SourceGeometry315
import TenthDiscriminant.ThinRadiusAnalyticGain

/-!
# Phase332: a sharper SAME-source Hadamard radius estimate

Use the existing thin ellipse, integer ordinary-Z jets, original trace
metric, same rectangular dimensions, and the same padded *count*
majorant. No second source determinant; no new arithmetic valuation.
The 315-domain bound is targeted first, before trying a smaller floor.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- The original integer-ceiling radii are already within 17/20. -/
theorem thin_radius_fraction_17_20_315 (D : Nat)
    (hD : (315 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (17/20 : Real) * rho D := by
  have ht := fourthRoot_ge_315 D hD
  have hcube : (315 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hlarge : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  nlinarith only [hcube,hceil,hlarge]

theorem upperB_strong_17_20_saving (R S oldRad smallRad : Nat) (n : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (h25 : 25*S ≤ R)
    (hOld : 0 < oldRad) (hSmall : 0 < smallRad)
    (hratio : (smallRad : Real) ≤ (17/20 : Real)*(oldRad : Real)) :
    enderUpperB R S S smallRad n/comparisonScale R S+27/200 ≤
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
  have hfrac : (smallRad : Real)/(oldRad : Real) ≤ 17/20 :=
    (div_le_iff₀ hOldReal).2 (by linarith [hratio])
  have hlog := Real.log_le_sub_one_of_pos hfracpos
  rw [Real.log_div hSmallReal.ne' hOldReal.ne'] at hlog
  have hloggap : (3/20 : Real) ≤
      Real.log (oldRad : Real)-Real.log (smallRad : Real) := by linarith
  have hdiff : (0 : Real) ≤ (oldRad : Real)-(smallRad : Real) := by
    linarith [hratio]
  have hSminus : (0 : Real) ≤ (S : Real)-1 := by linarith
  have hnonneg : 0 ≤
      2*(S : Real)*((S : Real)-1)*((oldRad : Real)-(smallRad : Real)) := by
    positivity
  have hraw : (27/200 : Real)*comparisonScale R S ≤
      enderUpperB R S S oldRad n-enderUpperB R S S smallRad n := by
    calc
      (27/200 : Real)*comparisonScale R S =
          ((9/10 : Real)*(R : Real)^2*(S : Real))*(3/20) := by
            unfold comparisonScale
            ring
      _ ≤ ((S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1)))*(3/20) :=
        mul_le_mul_of_nonneg_right hcoefbig (by norm_num)
      _ ≤ (S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1))*
          (Real.log (oldRad : Real)-Real.log (smallRad : Real)) :=
        mul_le_mul_of_nonneg_left hloggap hcoefpos
      _ ≤ _ := by linarith [hnonneg]
      _ = _ := (upperB_radius_difference R S oldRad smallRad n
        (by omega) hS hOld hSmall).symm
  have hscale : 0 < comparisonScale R S :=
    comparisonScale_pos R S (by omega) (by omega)
  have hnorm : (27/200 : Real) ≤
      (enderUpperB R S S oldRad n-enderUpperB R S S smallRad n)/
        comparisonScale R S := by
    apply (le_div_iff₀ hscale).2
    simpa only [mul_comm] using hraw
  rw [sub_div] at hnorm
  linarith


end
end TenthDiscriminant.FirstCertificate.Tuned

namespace TenthDiscriminant.Phase332
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

private def oldCountUpper (D : Nat) : Real :=
  ellipsePaddedUpperCount D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D))

/-- Same ORIGINAL Qthin, ordinary-jet trace Gram and row normalization,
with the old node-count majorant only as the n input to the original
Hadamard upper. No obsolete 450^4 premise is called. -/
theorem thin_production_normalized_upper_stronger_315 (D : Nat)
    (hD : (315 : Nat)^4 ≤ D) :
    Real.log ((integerRectangularTraceGram
      (ellipsePairs D (Tuned.thinRadius D)) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
      comparisonScale (Tuned.R D) (Tuned.S D) ≤
      (4/5 : Real)*Real.log D-1923/2000 := by
  have hd := Tuned.dimensions_315 D hD
  have hS : 100 ≤ Tuned.S D := by omega
  have h25 : 25*Tuned.S D ≤ Tuned.R D := by
    unfold Tuned.S
    omega
  have h26 : Tuned.R D ≤ 26*Tuned.S D := by
    unfold Tuned.S
    omega
  have hD0 : 0 < D := by omega
  have hcard := Tuned.thin_radius_interpolation_count_315 D hD
  obtain ⟨h10, hsmaller, hRrho⟩ := Tuned.thin_radius_guards_315 D hD
  have hn : ((ellipsePairs D (Tuned.thinRadius D)).card : Real) ≤
      oldCountUpper D := by
    exact Tuned.thin_card_le_old_padded_majorant_315 D hD
  have hnpos : (0 : Real) < oldCountUpper D := by
    exact Tuned.old_padded_majorant_pos_315 D hD
  have hbound (q : Int × Int)
      (hq : q ∈ ellipsePairs D (Tuned.thinRadius D)) :
      ‖pairEval D q‖ ≤ Tuned.thinRadius D := by
    apply ellipsePoint_norm_le D (Tuned.thinRadius D) hD0
    exact Finset.mem_image.mpr ⟨q,hq,rfl⟩
  have hupper := TightRadialSaving.normalized_integer_upper_tight
    (ellipsePairs D (Tuned.thinRadius D)) D
    (Tuned.R D) (Tuned.S D) (Tuned.thinRadius D)
    (oldCountUpper D)
    hD0 hS h25 h26 h10 hRrho hcard hnpos hn hbound
  have hsave := Tuned.upperB_strong_17_20_saving
    (Tuned.R D) (Tuned.S D) (Tuned.rho D)
    (Tuned.thinRadius D) (oldCountUpper D)
    (by omega) (by omega) h25
    (Tuned.radius_pos_315 D hD) (by omega)
    (Tuned.thin_radius_fraction_17_20_315 D hD)
  have hold := Tuned.normalized_upper_315 D hD
  dsimp only [oldCountUpper] at hupper hsave hn hnpos
  linarith


end
end TenthDiscriminant.Phase332

#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_fraction_17_20_315
#print axioms TenthDiscriminant.FirstCertificate.Tuned.upperB_strong_17_20_saving
#print axioms TenthDiscriminant.Phase332.thin_production_normalized_upper_stronger_315
