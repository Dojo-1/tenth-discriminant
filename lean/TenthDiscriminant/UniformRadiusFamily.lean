import TenthDiscriminant.UniformLowerEnvelope
import Mathlib.Data.Complex.ExponentialBounds

/-! A new auxiliary radius family, not a modification of the frozen Ender
campaign. D-dependent lower and geometric guards are checked separately. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

def envelopeR (D : Nat) : Nat := D/4
def envelopeS (D : Nat) : Nat := envelopeR D/20
def fourthRoot (D : Nat) : Real := Real.sqrt (Real.sqrt D)
def envelopeRadius (D : Nat) : Nat := ⌈(11/20 : Real)*fourthRoot D^3⌉₊

theorem envelope_dimensions (D : Nat) (hD : 200000000000 ≤ D) :
    100000000 ≤ envelopeR D ∧ 500000 ≤ envelopeS D ∧
    envelopeR D ≤ 21*envelopeS D ∧ envelopeR D ≤ 10000*envelopeS D ∧
    (D : Real)/5 ≤ envelopeR D ∧ (envelopeR D : Real) ≤ (D : Real)/4 ∧
    (envelopeS D : Real) ≤ (envelopeR D : Real)/20 := by
  have hlo : D ≤ 5*(D/4) := by omega
  have hhi : 4*(D/4) ≤ D := by omega
  have hs : 20*((D/4)/20) ≤ D/4 := by omega
  refine ⟨by unfold envelopeR; omega, by unfold envelopeS envelopeR; omega,
    by unfold envelopeS envelopeR; omega, by unfold envelopeS envelopeR; omega, ?_, ?_, ?_⟩
  · unfold envelopeR
    have h : (D : Real) ≤ 5*(D/4 : Nat) := by exact_mod_cast hlo
    linarith
  · unfold envelopeR
    have h : 4*((D/4 : Nat) : Real) ≤ D := by exact_mod_cast hhi
    linarith
  · unfold envelopeS envelopeR
    have h : 20*(((D/4)/20 : Nat) : Real) ≤ (D/4 : Nat) := by exact_mod_cast hs
    linarith

theorem envelope_strict_inertness (D : Nat) [Fact ((D : Int)%4=3)] :
    (envelopeR D : Int) < ((D : Int)+1)/4 := by
  have hmod := Fact.out (p := (D : Int)%4=3)
  unfold envelopeR
  omega

theorem large_D_log (D : Nat) (hD : 700000000000 ≤ D) : 27 ≤ Real.log D := by
  have hmul : (4*174999999999 : Real) ≤ D := by exact_mod_cast (show 4*174999999999 ≤ D by omega)
  have h := Real.log_le_log (by norm_num : (0 : Real) < 4*174999999999) hmul
  rw [Real.log_mul (by norm_num : (4 : Real) ≠ 0) (by norm_num : (174999999999 : Real) ≠ 0)] at h
  have h4 : Real.log (4 : Real) = 2*Real.log 2 := by
    have he : (4 : Real) = 2^2 := by norm_num
    rw [he, Real.log_pow]
    norm_num
  rw [h4] at h
  linarith [Real.log_two_gt_d9, FirstEnderInterval.factorial_log_bounds.1]

theorem log_five_upper : Real.log (5 : Real) ≤ 161/100 := by
  have h := checkPositiveLogBounds_sound 8 5 2 (160/100) (161/100)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h.2

theorem log_five_lower : (1609/1000 : Real) ≤ Real.log 5 := by
  have h := checkPositiveLogBounds_sound 8 5 2 (1609/1000) (161/100)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h.1

theorem moderate_D_log (D : Nat) (hD : 200000000000 ≤ D) : 26 ≤ Real.log D := by
  have hb : (200000000000 : Real) ≤ D := by exact_mod_cast hD
  have hl := Real.log_le_log (by norm_num : (0 : Real) < 200000000000) hb
  have he : (200000000000 : Real)=2^12*5^11 := by norm_num
  rw [he, Real.log_mul (by norm_num : (2 : Real)^12 ≠ 0)
    (by norm_num : (5 : Real)^11 ≠ 0), Real.log_pow, Real.log_pow] at hl
  norm_num only [Nat.cast_ofNat] at hl
  linarith [Real.log_two_gt_d9, log_five_lower]

theorem envelope_floor_ratio (D : Nat) (hD : 1000 ≤ D) :
    249*D ≤ 1000*envelopeR D := by
  unfold envelopeR
  omega

theorem log_floor_ratio_upper : Real.log (1000/249 : Real) ≤ 140/100 := by
  have h := checkPositiveLogBounds_sound 8 (1000/249) 2 (139/100) (140/100)
    (by norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  push_cast at h
  exact h.2

theorem envelope_log_R_lower_sharp (D : Nat) (hD : 200000000000 ≤ D) :
    Real.log D-140/100 ≤ Real.log (envelopeR D) := by
  have hn := envelope_floor_ratio D (by omega)
  have hr : (249 : Real)*D ≤ 1000*envelopeR D := by exact_mod_cast hn
  have hp : (0 : Real)<D := by exact_mod_cast (show 0<D by omega)
  have hR : (D : Real)/(1000/249) ≤ envelopeR D := by
    apply (div_le_iff₀ (by norm_num : (0 : Real)<1000/249)).2
    linarith
  have hl := Real.log_le_log (div_pos hp (by norm_num)) hR
  rw [Real.log_div hp.ne' (by norm_num : (1000/249 : Real)≠0)] at hl
  linarith [log_floor_ratio_upper]

theorem envelope_floor_ratio_without_guard_rejected :
    ¬ 249*3 ≤ 1000*envelopeR 3 := by norm_num [envelopeR]

theorem envelope_log_R_lower (D : Nat) (hD : 200000000000 ≤ D) :
    Real.log D-161/100 ≤ Real.log (envelopeR D) := by
  have hdim := (envelope_dimensions D hD).2.2.2.2.1
  have hd : (0 : Real) < D := by exact_mod_cast (show 0 < D by omega)
  have hl := Real.log_le_log (div_pos hd (by norm_num)) hdim
  rw [Real.log_div hd.ne' (by norm_num : (5 : Real) ≠ 0)] at hl
  linarith [log_five_upper]

/-- One side of the proposed all-D comparison is now unconditional on
the fixed family's dimensions. This alone is not a class-number cutoff. -/
theorem envelope_normalized_lower (D : Nat) (hD : 200000000000 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5845/1000 ≤
      rawPrimeMassLower (envelopeR D) (envelopeS D) FirstEnderInterval.tailBudget /
        comparisonScale (envelopeR D) (envelopeS D) := by
  have hdim := envelope_dimensions D hD
  have hl := envelope_log_R_lower D hD
  have hu := moderate_D_log D hD
  have hlow := rawPrimeMassLower_uniform_normalized (envelopeR D) (envelopeS D)
    hdim.1 hdim.2.1 hdim.2.2.1 (by linarith)
  linarith

theorem envelope_normalized_lower_sharp (D : Nat) (hD : 200000000000 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5635/1000 ≤
      rawPrimeMassLower (envelopeR D) (envelopeS D) FirstEnderInterval.tailBudget /
        comparisonScale (envelopeR D) (envelopeS D) := by
  have hd := envelope_dimensions D hD
  have hl := envelope_log_R_lower_sharp D hD
  have hu := moderate_D_log D hD
  have hm := rawPrimeMassLower_uniform_normalized (envelopeR D) (envelopeS D)
    hd.1 hd.2.1 hd.2.2.1 (by linarith)
  linarith

theorem fourthRoot_identities (D : Nat) :
    0 ≤ fourthRoot D ∧ fourthRoot D^2=Real.sqrt D ∧ fourthRoot D^4=(D : Real) := by
  have h := Real.sq_sqrt (Real.sqrt_nonneg (D : Real))
  have hD := Real.sq_sqrt (Nat.cast_nonneg D : (0 : Real) ≤ D)
  refine ⟨Real.sqrt_nonneg _, h, ?_⟩
  change (Real.sqrt (Real.sqrt D))^4 = (D : Real)
  calc
    _ = ((Real.sqrt (Real.sqrt D))^2)^2 := by ring
    _ = (D : Real) := by rw [h, hD]

theorem fourthRoot_large (D : Nat) (hD : 200000000000 ≤ D) : 300 ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show 300^2^2 ≤ D by omega)

theorem envelope_radius_bounds (D : Nat) (hD : 200000000000 ≤ D) :
    (11/20 : Real)*fourthRoot D^3 ≤ envelopeRadius D ∧
    (envelopeRadius D : Real) ≤ (551/1000 : Real)*fourthRoot D^3 := by
  have ht := fourthRoot_large D hD
  have ht0 := (fourthRoot_identities D).1
  refine ⟨Nat.le_ceil _, ?_⟩
  have hc := Nat.ceil_lt_add_one (show 0 ≤ (11/20 : Real)*fourthRoot D^3 by positivity)
  have hcube : (300 : Real)^3 ≤ fourthRoot D^3 := pow_le_pow_left₀ (by norm_num) ht 3
  unfold envelopeRadius
  linarith

theorem envelope_radius_lt_R (D : Nat) (hD : 200000000000 ≤ D) :
    envelopeRadius D < envelopeR D := by
  have ht := fourthRoot_large D hD
  have ht0 := (fourthRoot_identities D).1
  have hp := (fourthRoot_identities D).2.2
  have hl := (envelope_dimensions D hD).2.2.2.2.1
  have hu := (envelope_radius_bounds D hD).2
  have hpos : 0 < fourthRoot D^3 := pow_pos (by linarith) 3
  have h := mul_pos hpos (show 0 < fourthRoot D/5-551/1000 by linarith)
  have hr : (envelopeRadius D : Real) < envelopeR D := by
    nlinarith only [h, hl, hu, hp]
  exact_mod_cast hr

theorem envelope_chosen_radius (D : Nat) (hD : 200000000000 ≤ D) :
    (1001/1000 : Real)*Real.sqrt
      (((3*envelopeR D+envelopeS D : Nat) : Real)*Real.sqrt D/Real.pi)+
      10*Real.sqrt D ≤ (envelopeRadius D : Real) := by
  have hd := envelope_dimensions D hD
  have ht := fourthRoot_large D hD
  have hi := fourthRoot_identities D
  have hq : ((3*envelopeR D+envelopeS D : Nat) : Real) ≤
      (61/80 : Real)*(D : Real) := by
    push_cast
    linarith [hd.2.2.2.2.2.1, hd.2.2.2.2.2.2]
  have hqm := mul_le_mul_of_nonneg_right hq (Real.sqrt_nonneg (D : Real))
  have hpow : (D : Real)*Real.sqrt D = fourthRoot D^6 := by
    rw [← hi.2.1, ← hi.2.2]
    ring
  have hinner : Real.sqrt
      (((3*envelopeR D+envelopeS D : Nat) : Real)*Real.sqrt D/Real.pi) ≤
      (51/100 : Real)*fourthRoot D^3 := by
    apply Real.sqrt_le_iff.mpr
    refine ⟨by positivity, (div_le_iff₀ Real.pi_pos).2 ?_⟩
    have hp := mul_le_mul_of_nonneg_right Real.pi_gt_three.le
      (sq_nonneg ((51/100 : Real)*fourthRoot D^3))
    have hq' : ((3*envelopeR D+envelopeS D : Nat) : Real)*Real.sqrt D ≤
        (61/80 : Real)*fourthRoot D^6 := by
      simpa only [mul_assoc, hpow] using hqm
    nlinarith only [hp, hq', pow_nonneg hi.1 6]
  have herror := mul_nonneg (sq_nonneg (fourthRoot D))
    (show 0 ≤ (11/20-1001/1000*51/100 : Real)*fourthRoot D-10 by linarith)
  have hl := (envelope_radius_bounds D hD).1
  rw [← hi.2.1] at hinner ⊢
  nlinarith only [hinner, herror, hl]

end
end TenthDiscriminant.FirstCertificate
