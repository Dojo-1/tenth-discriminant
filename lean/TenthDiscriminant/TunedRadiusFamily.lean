import TenthDiscriminant.OptimizedAnalyticCutoff
import TenthDiscriminant.AspectRatioLowerEnvelope

/-! A separately guarded auxiliary family. The old families and campaign
are unchanged; this module supplies geometry and the lower budget only. -/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

def R (D : Nat) : Nat := envelopeR D
def S (D : Nat) : Nat := R D/25
def rho (D : Nat) : Nat := ⌈(13/25 : Real)*fourthRoot D^3⌉₊

theorem dimensions (D : Nat) (hD : 100000000000 ≤ D) :
    100000000 ≤ R D ∧ 500000 ≤ S D ∧ 10*R D ≤ 251*S D ∧
    R D ≤ 10000*S D ∧ (D : Real)/5 ≤ R D ∧
    (R D : Real) ≤ (D : Real)/4 ∧ (S D : Real) ≤ (R D : Real)/25 := by
  have hlo : D ≤ 5*(D/4) := by omega
  have hhi : 4*(D/4) ≤ D := by omega
  have hs : 25*((D/4)/25) ≤ D/4 := by omega
  refine ⟨by unfold R envelopeR; omega, by unfold S R envelopeR; omega,
    by unfold S R envelopeR; omega, by unfold S R envelopeR; omega, ?_, ?_, ?_⟩
  · have h : (D : Real) ≤ 5*(D/4 : Nat) := by exact_mod_cast hlo
    change (D : Real)/5 ≤ (D/4 : Nat)
    linarith
  · have h : 4*((D/4 : Nat) : Real) ≤ D := by exact_mod_cast hhi
    change ((D/4 : Nat) : Real) ≤ (D : Real)/4
    linarith
  · have h : 25*(((D/4)/25 : Nat) : Real) ≤ (D/4 : Nat) := by exact_mod_cast hs
    change (((D/4)/25 : Nat) : Real) ≤ ((D/4 : Nat) : Real)/25
    linarith

theorem strict_inertness (D : Nat) [Fact ((D : Int)%4=3)] :
    (R D : Int) < ((D : Int)+1)/4 := envelope_strict_inertness D

theorem root_large (D : Nat) (hD : 100000000000 ≤ D) : 500 ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show 500^2^2 ≤ D by omega)

theorem log_large (D : Nat) (hD : 100000000000 ≤ D) : 253/10 ≤ Real.log D := by
  have hb : (100000000000 : Real) ≤ D := by exact_mod_cast hD
  have hl := Real.log_le_log (by norm_num : (0 : Real)<100000000000) hb
  have he : (100000000000 : Real)=2^11*5^11 := by norm_num
  rw [he, Real.log_mul (by norm_num : (2 : Real)^11≠0)
    (by norm_num : (5 : Real)^11≠0), Real.log_pow, Real.log_pow] at hl
  norm_num only [Nat.cast_ofNat] at hl
  linarith [Real.log_two_gt_d9, log_five_lower]

theorem log_R_bounds (D : Nat) (hD : 100000000000 ≤ D) :
    Real.log D-140/100 ≤ Real.log (R D) ∧
    Real.log (R D) ≤ Real.log D-138/100 := by
  have hd := dimensions D hD
  have hp : (0 : Real)<D := by exact_mod_cast (show 0<D by omega)
  have hRpos : (0 : Real)<R D := by exact_mod_cast (show 0<R D by omega)
  constructor
  · have hn := envelope_floor_ratio D (by omega)
    have hr : (249 : Real)*D ≤ 1000*R D := by exact_mod_cast hn
    have hR : (D : Real)/(1000/249) ≤ R D := by
      apply (div_le_iff₀ (by norm_num : (0 : Real)<1000/249)).2
      linarith
    have hl := Real.log_le_log (div_pos hp (by norm_num)) hR
    rw [Real.log_div hp.ne' (by norm_num : (1000/249 : Real)≠0)] at hl
    linarith [log_floor_ratio_upper]
  · have hl := Real.log_le_log hRpos hd.2.2.2.2.2.1
    rw [Real.log_div hp.ne' (by norm_num : (4 : Real)≠0)] at hl
    have h4 : Real.log (4 : Real)=2*Real.log 2 := by
      have he : (4 : Real)=2^2 := by norm_num
      rw [he, Real.log_pow]
      norm_num
    rw [h4] at hl
    linarith [Real.log_two_gt_d9]

theorem normalized_lower (D : Nat) (hD : 100000000000 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5820/1000 ≤
      rawPrimeMassLower (R D) (S D) FirstEnderInterval.tailBudget/comparisonScale (R D) (S D) := by
  have hd := dimensions D hD
  have hl := (log_R_bounds D hD).1
  have hu := log_large D hD
  have hr : (10 : Real)*R D ≤ 251*S D := by exact_mod_cast hd.2.2.1
  have hratio : (R D : Real) ≤ (251/10)*S D := by linarith
  have hm := aspect_ratio_25_point_1_control (R D) (S D) hd.1 hd.2.1 hratio (by linarith)
  linarith

theorem radius_bounds (D : Nat) (hD : 100000000000 ≤ D) :
    (13/25 : Real)*fourthRoot D^3 ≤ rho D ∧
    (rho D : Real) ≤ (521/1000 : Real)*fourthRoot D^3 := by
  have ht := root_large D hD
  have ht0 := (fourthRoot_identities D).1
  refine ⟨Nat.le_ceil _, ?_⟩
  have hc := Nat.ceil_lt_add_one (show 0≤(13/25 : Real)*fourthRoot D^3 by positivity)
  have hcube : (500 : Real)^3 ≤ fourthRoot D^3 := pow_le_pow_left₀ (by norm_num) ht 3
  unfold rho
  linarith

theorem radius_pos (D : Nat) (hD : 100000000000 ≤ D) : 0<rho D := by
  have ht := root_large D hD
  have hl := (radius_bounds D hD).1
  have hp : 0<(13/25 : Real)*fourthRoot D^3 := by positivity
  have : (0 : Real)<rho D := hp.trans_le hl
  exact_mod_cast this

theorem radius_lt_R (D : Nat) (hD : 100000000000 ≤ D) : rho D<R D := by
  have ht := root_large D hD
  have ht0 := (fourthRoot_identities D).1
  have hp := (fourthRoot_identities D).2.2
  have hl := (dimensions D hD).2.2.2.2.1
  have hu := (radius_bounds D hD).2
  have hpos : 0<fourthRoot D^3 := pow_pos (by linarith) 3
  have h := mul_pos hpos (show 0<fourthRoot D/5-521/1000 by linarith)
  have hr : (rho D : Real)<R D := by nlinarith only [h,hl,hu,hp]
  exact_mod_cast hr

theorem chosen_radius (D : Nat) (hD : 100000000000 ≤ D) :
    (1001/1000 : Real)*Real.sqrt (((3*R D+S D : Nat) : Real)*Real.sqrt D/Real.pi)+
      10*Real.sqrt D ≤ (rho D : Real) := by
  have hd := dimensions D hD
  have ht := root_large D hD
  have hi := fourthRoot_identities D
  have hq : ((3*R D+S D : Nat) : Real) ≤ (19/25 : Real)*(D : Real) := by
    push_cast
    linarith [hd.2.2.2.2.2.1,hd.2.2.2.2.2.2]
  have hqm := mul_le_mul_of_nonneg_right hq (Real.sqrt_nonneg (D : Real))
  have hpow : (D : Real)*Real.sqrt D=fourthRoot D^6 := by
    rw [← hi.2.1,← hi.2.2]
    ring
  have hinner : Real.sqrt (((3*R D+S D : Nat) : Real)*Real.sqrt D/Real.pi) ≤
      (495/1000 : Real)*fourthRoot D^3 := by
    apply Real.sqrt_le_iff.mpr
    refine ⟨by positivity,(div_le_iff₀ Real.pi_pos).2 ?_⟩
    have hp := mul_le_mul_of_nonneg_right Real.pi_gt_d2.le
      (sq_nonneg ((495/1000 : Real)*fourthRoot D^3))
    have hq' : ((3*R D+S D : Nat) : Real)*Real.sqrt D ≤ (19/25 : Real)*fourthRoot D^6 := by
      simpa only [mul_assoc,hpow] using hqm
    nlinarith only [hp,hq',pow_nonneg hi.1 6]
  have herror := mul_nonneg (sq_nonneg (fourthRoot D))
    (show 0≤(13/25-1001/1000*495/1000 : Real)*fourthRoot D-10 by linarith)
  have hl := (radius_bounds D hD).1
  rw [← hi.2.1] at hinner ⊢
  nlinarith only [hinner,herror,hl]

theorem unguarded_radius_rounding_rejected :
    ¬ (rho 1 : Real) ≤ (521/1000 : Real)*fourthRoot 1^3 := by
  have hn : 1≤⌈(13/25 : Real)⌉₊ := Nat.ceil_pos.mpr (by norm_num)
  have hr : (1 : Real)≤(⌈(13/25 : Real)⌉₊ : Real) := by exact_mod_cast hn
  norm_num [rho,fourthRoot]
  linarith

theorem inclusive_inertness_endpoint_rejected : ¬ (41 : Int)<((163 : Int)+1)/4 := by
  norm_num

end
end TenthDiscriminant.FirstCertificate.Tuned
