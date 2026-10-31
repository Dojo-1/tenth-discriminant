import TenthDiscriminant.TightRadialSaving
import TenthDiscriminant.ThinEllipseCount

/-!
# Phase141: honest radius comparison for the same analytic envelope

This file isolates a production-independent identity of the existing
upper_B formula and proves a guarded lower bound for its saving when
the observation radius shrinks. It never compares determinants of
different observation matrices by equality, and leaves the original
class-number and field-discriminant theorems untouched.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

theorem thin_radius_fraction (D : Nat) (hD : 41006250000 ≤ D) :
    (thinRadius D : Real) ≤ (8/9 : Real) * rho D := by
  have ht := root_large D hD
  have hcube : (450 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hlarge := (radius_bounds D hD).1
  nlinarith only [hceil, hlarge, hcube]

theorem thin_radius_guards (D : Nat) (hD : 41006250000 ≤ D) :
    10 ≤ thinRadius D ∧ thinRadius D < rho D ∧ thinRadius D < R D := by
  have ht := root_large D hD
  have hcube : (450 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (11/25 : Real)*fourthRoot D^3 ≤ thinRadius D := by
    unfold thinRadius
    exact Nat.le_ceil _
  have h10 : (10 : Real) ≤ thinRadius D := by nlinarith only [hceil, hcube]
  have hratio := thin_radius_fraction D hD
  have hold : 0 < rho D := radius_pos D hD
  have holdReal : (0 : Real) < rho D := by exact_mod_cast hold
  have hsmall : (thinRadius D : Real) < rho D := by nlinarith only [hratio,holdReal]
  have hsmnat : thinRadius D < rho D := by exact_mod_cast hsmall
  refine ⟨by exact_mod_cast h10, hsmnat, ?_⟩
  exact lt_trans hsmnat (radius_lt_R D hD)

theorem ellipsePairs_card_mono_radius
    (D a b : Nat) (hD : 0 < D) (hab : a ≤ b) :
    (ellipsePairs D a).card ≤ (ellipsePairs D b).card := by
  apply Finset.card_le_card
  intro p hp
  have hh := (mem_ellipsePairs_iff D a hD p.1 p.2).mp hp
  have hcast : (a : Int) ≤ b := by exact_mod_cast hab
  have hz : (0 : Int) ≤ a := by positivity
  have hs : (a : Int)^2 ≤ (b : Int)^2 := by nlinarith
  exact (mem_ellipsePairs_iff D b hD p.1 p.2).mpr (hh.trans hs)

/-- Exact algebraic difference of the ALREADY certified real upper expression.
Both evaluations have the SAME rows R,S and the SAME n; this is not an
assertion that their underlying integer Gram determinants are equal. -/
theorem upperB_radius_difference (R S oldRad smallRad : Nat) (n : Real)
    (hR : 0 < R) (hS : 1 ≤ S) (hOld : 0 < oldRad) (hSmall : 0 < smallRad) :
    enderUpperB R S S oldRad n - enderUpperB R S S smallRad n =
      (S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1))*
        (Real.log (oldRad : Real)-Real.log (smallRad : Real))+
      2*(S : Real)*((S : Real)-1)*((oldRad : Real)-(smallRad : Real)) := by
  have hr : (R : Real) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hR)
  have ho : (oldRad : Real) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hOld)
  have hs : (smallRad : Real) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hSmall)
  unfold enderUpperB
  simp only [Nat.cast_sub hS, Nat.cast_one]
  rw [Real.log_div hr ho, Real.log_div hr hs]
  ring

/-- The ordinary-jet upper expression gains at least one tenth of the
entire production comparison scale whenever the integer radius contracts
by 8/9 and the existing rectangular dimension guard holds. -/
theorem upperB_tenth_saving (R S oldRad smallRad : Nat) (n : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (h25 : 25*S ≤ R)
    (hOld : 0 < oldRad) (hSmall : 0 < smallRad)
    (hratio : (smallRad : Real) ≤ (8/9 : Real)*(oldRad : Real)) :
    enderUpperB R S S smallRad n/comparisonScale R S+1/10 ≤
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
  have hfrac : (smallRad : Real)/(oldRad : Real) ≤ 8/9 :=
    (div_le_iff₀ hOldReal).2 (by linarith [hratio])
  have hlog := Real.log_le_sub_one_of_pos hfracpos
  rw [Real.log_div hSmallReal.ne' hOldReal.ne'] at hlog
  have hloggap : (1/9 : Real) ≤
      Real.log (oldRad : Real)-Real.log (smallRad : Real) := by linarith
  have hdiff : (0 : Real) ≤ (oldRad : Real)-(smallRad : Real) := by
    linarith [hratio]
  have hSminus : (0 : Real) ≤ (S : Real)-1 := by linarith
  have hnonneg : 0 ≤
      2*(S : Real)*((S : Real)-1)*((oldRad : Real)-(smallRad : Real)) := by
    positivity
  have hraw : (1/10 : Real)*comparisonScale R S ≤
      enderUpperB R S S oldRad n-enderUpperB R S S smallRad n := by
    calc
      (1/10 : Real)*comparisonScale R S =
          ((9/10 : Real)*(R : Real)^2*(S : Real))*(1/9) := by
            unfold comparisonScale
            ring
      _ ≤ ((S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1)))*(1/9) :=
        mul_le_mul_of_nonneg_right hcoefbig (by norm_num)
      _ ≤ (S : Real)*((R : Real)^2-(R : Real)*S-2*((S : Real)-1))*
          (Real.log (oldRad : Real)-Real.log (smallRad : Real)) :=
        mul_le_mul_of_nonneg_left hloggap hcoefpos
      _ ≤ _ := by linarith [hnonneg]
      _ = _ := (upperB_radius_difference R S oldRad smallRad n
        (by omega) hS hOld hSmall).symm
  have hscale : 0 < comparisonScale R S :=
    comparisonScale_pos R S (by omega) (by omega)
  have hnorm : (1/10 : Real) ≤
      (enderUpperB R S S oldRad n-enderUpperB R S S smallRad n)/
        comparisonScale R S := by
    apply (le_div_iff₀ hscale).2
    simpa only [mul_comm] using hraw
  rw [sub_div] at hnorm
  linarith

end
end TenthDiscriminant.FirstCertificate.Tuned
