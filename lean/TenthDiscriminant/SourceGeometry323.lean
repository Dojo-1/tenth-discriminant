import TenthDiscriminant.ThinEllipseCount
import TenthDiscriminant.ThinRadiusAnalyticGain
import TenthDiscriminant.Phase199Scalar323

/-!
# Phase196: source-exact original thin-ellipse geometry at fourth-root 323

Only the finite-support count, integer rounding and radius/R budget are
asserted here. Same R=floor(D/4), S=floor(R/25), original ellipsePairs,
ordinary-jet support and radii. No determinant sandwich, field bound or
new number-theoretic assertion is made. Standalone research source; do not import into the production root until
this exact-head Lean build, source audit, and negative controls pass.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- A source-exact upper envelope for the required 2R+S channels. -/
private theorem twoRplusS_le_51percent (D : Nat) :
    ((2*R D+S D : Nat) : Real) <= (51/100 : Real)*(D : Real) := by
  have hR : 4*R D <= D := by
    unfold R envelopeR
    omega
  have hS : 25*S D <= R D := by
    unfold S
    omega
  have hn : 100*(2*R D+S D) <= 51*D := by omega
  have hc : ((100*(2*R D+S D) : Nat) : Real) <= ((51*D : Nat) : Real) := by
    exact_mod_cast hn
  push_cast at hc ⊢
  linarith


theorem fourthRoot_ge_323 (D : Nat) (hD : (323 : Nat)^4 <= D) :
    (323 : Real) <= fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (323 : Nat)^2^2 <= D by omega)

/-- The same original padded integer radius, at 323^4. -/
theorem rho_upper_323 (D : Nat) (hD : (323 : Nat)^4 <= D) :
    (rho D : Real) <= (521/1000 : Real)*fourthRoot D^3 := by
  have ht := fourthRoot_ge_323 D hD
  have hcube : (323 : Real)^3 <= fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (rho D : Real) <
      (13/25 : Real)*fourthRoot D^3+1 := by
    unfold rho
    exact Nat.ceil_lt_add_one (by positivity)
  nlinarith only [hcube,hceil]


/-- Exact floor remainder gives R at least 80 fourth-root cubes. -/
theorem R_ge_eighty_cubes_323 (D : Nat) (hD : (323 : Nat)^4 ≤ D) :
    (80 : Real)*fourthRoot D^3 ≤ R D := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_323 D hD
  have hcube : (323 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hgap : (3 : Real) ≤ fourthRoot D-320 := by linarith
  have hproduct := mul_le_mul_of_nonneg_right hgap (pow_nonneg hi.1 3)
  have h3 : (3 : Real) ≤ 3*fourthRoot D^3 := by
    nlinarith only [hcube]
  have hfloor : D ≤ 4*R D+3 := by
    unfold R envelopeR
    omega
  have hf : (D : Real) ≤ 4*(R D : Real)+3 := by
    exact_mod_cast hfloor
  rw [← hi.2.2] at hf
  nlinarith only [hf,hproduct,h3]

/-! The unchanged padded radius envelope `rho_upper_323` is proved above. -/

/-- Recover exactly the former analytic constant, without old root>=450. -/
theorem radius_over_R_323 (D : Nat) (hD : (323 : Nat)^4 ≤ D) :
    (rho D : Real)/R D ≤ 521/80000 := by
  have hR := R_ge_eighty_cubes_323 D hD
  have hu := rho_upper_323 D hD
  have ht : (0 : Real) < fourthRoot D := by
    linarith [fourthRoot_ge_323 D hD]
  have hp : (0 : Real) < fourthRoot D^3 := pow_pos ht 3
  have hRpos : (0 : Real) < R D := by nlinarith only [hR,hp]
  apply (div_le_iff₀ hRpos).2
  nlinarith only [hR,hu]

/-- The existing eighths/ninths shrinkage still holds below 450^4. -/
theorem thin_radius_fraction_323 (D : Nat) (hD : (323 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (8/9 : Real)*(rho D : Real) := by
  have ht := fourthRoot_ge_323 D hD
  have hcube : (323 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hrho : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  nlinarith only [hcube,hceil,hrho]

/-- The existing cell-area sufficient criterion at the smaller floor.
At fourth root 323, the rational cell-covering buffer is positive: (11/25 - 1001/1000*407/1000)*323 > 10. -/
theorem thin_chosen_radius_323 (D : Nat) (hD : (323 : Nat)^4 <= D) :
    (1001/1000 : Real) *
      Real.sqrt (((2*R D+S D : Nat) : Real)*Real.sqrt D/Real.pi) +
      10*Real.sqrt D <= (thinRadius D : Real) := by
  have ht := fourthRoot_ge_323 D hD
  have hi := fourthRoot_identities D
  have hq := twoRplusS_le_51percent D
  have hqm := mul_le_mul_of_nonneg_right hq (Real.sqrt_nonneg (D : Real))
  have hpow : (D : Real)*Real.sqrt D = fourthRoot D^6 := by
    rw [← hi.2.1, ← hi.2.2]
    ring
  have hinner : Real.sqrt
      (((2*R D+S D : Nat) : Real)*Real.sqrt D / Real.pi) <=
      (407/1000 : Real)*fourthRoot D^3 := by
    apply Real.sqrt_le_iff.mpr
    refine ⟨by positivity,(div_le_iff₀ Real.pi_pos).2 ?_⟩
    have hp := mul_le_mul_of_nonneg_right Real.pi_gt_d2.le
      (sq_nonneg ((407/1000 : Real)*fourthRoot D^3))
    have hq' : ((2*R D+S D : Nat) : Real)*Real.sqrt D <=
        (51/100 : Real)*fourthRoot D^6 := by
      simpa only [mul_assoc,hpow] using hqm
    nlinarith only [hp,hq',pow_nonneg hi.1 6]
  have herror := mul_nonneg (sq_nonneg (fourthRoot D))
    (show 0 <= (11/25-1001/1000*407/1000 : Real)*fourthRoot D-10 by
      linarith)
  have hl : (11/25 : Real)*fourthRoot D^3 <= thinRadius D := by
    unfold thinRadius
    exact Nat.le_ceil _
  rw [← hi.2.1] at hinner ⊢
  nlinarith only [hinner,herror,hl]

/-- Original-Q count, with no metric, field or prime-divisor change. -/
theorem thin_radius_interpolation_count_323 (D : Nat)
    (hD : (323 : Nat)^4 <= D) :
    2*(R D-1)+(S D-1) < (ellipsePairs D (thinRadius D)).card := by
  have hpositive : 0 < D := by omega
  have hR : 0 < R D := by
    unfold R envelopeR
    omega
  have hq : 0 < 2*R D+S D := by omega
  have hc := ellipsePairs_card_gt_of_ender_radius
    D (thinRadius D) (2*R D+S D) hpositive hq
    (thin_chosen_radius_323 D hD)
  omega

end
end TenthDiscriminant.FirstCertificate.Tuned
