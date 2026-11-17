import TenthDiscriminant.ThinEllipseCount
import TenthDiscriminant.ThinRadiusAnalyticGain
import TenthDiscriminant.Phase200Scalar322

/-!
# Phase342 — exact original Qthin geometry at the 307^4 threshold

This module proves candidate 307-domain geometry while keeping the
original integer pair support, ordinary-Z derivatives, floor dimensions
and the SAME original trace Gram identity. Crucially the 313-domain
guard R >= 78*(fourthRoot D)^3 is FALSE at 307^4. We derive the
weaker 76-cube bound and rho/R <= 521/76000 instead.

This module proves NO analytic Gram upper, odd-prime lower, or
actual-field discriminant theorem. The formally checked 313^4 theorem
is not modified or assumed with a weakened hypothesis.

The rational cell-area buffer is only 0.006051 at root=307, so all
ceiling and source-count arguments must be checked exactly.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- A source-exact upper envelope for the required 2R+S channels. -/
private theorem twoRplusS_le_51percent_307 (D : Nat) :
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


theorem fourthRoot_ge_307 (D : Nat) (hD : (307 : Nat)^4 <= D) :
    (307 : Real) <= fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (307 : Nat)^2^2 <= D by omega)

/-- The same original padded integer radius, at 307^4. -/
theorem rho_upper_307 (D : Nat) (hD : (307 : Nat)^4 <= D) :
    (rho D : Real) <= (521/1000 : Real)*fourthRoot D^3 := by
  have ht := fourthRoot_ge_307 D hD
  have hcube : (307 : Real)^3 <= fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (rho D : Real) <
      (13/25 : Real)*fourthRoot D^3+1 := by
    unfold rho
    exact Nat.ceil_lt_add_one (by positivity)
  nlinarith only [hcube,hceil]


/-- Exact floor remainder gives R at least 76 fourth-root cubes. -/
theorem R_ge_seventysix_cubes_307 (D : Nat) (hD : (307 : Nat)^4 ≤ D) :
    (76 : Real)*fourthRoot D^3 ≤ R D := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_307 D hD
  have hcube : (307 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hgap : (1 : Real) ≤ fourthRoot D-306 := by linarith
  have hproduct := mul_le_mul_of_nonneg_right hgap (pow_nonneg hi.1 3)
  have h3 : (3 : Real) ≤ fourthRoot D^3 := by
    nlinarith only [hcube]
  have hfloor : D ≤ 4*R D+3 := by
    unfold R envelopeR
    omega
  have hf : (D : Real) ≤ 4*(R D : Real)+3 := by
    exact_mod_cast hfloor
  rw [← hi.2.2] at hf
  nlinarith only [hf,hproduct,h3]

/-! The unchanged padded radius envelope `rho_upper_307` is proved above. -/

/-- Recover exactly the former analytic constant, without old root>=450. -/
theorem radius_over_R_307 (D : Nat) (hD : (307 : Nat)^4 ≤ D) :
    (rho D : Real)/R D ≤ 521/76000 := by
  have hR := R_ge_seventysix_cubes_307 D hD
  have hu := rho_upper_307 D hD
  have ht : (0 : Real) < fourthRoot D := by
    linarith [fourthRoot_ge_307 D hD]
  have hp : (0 : Real) < fourthRoot D^3 := pow_pos ht 3
  have hRpos : (0 : Real) < R D := by nlinarith only [hR,hp]
  apply (div_le_iff₀ hRpos).2
  nlinarith only [hR,hu]

/-- The existing eighths/ninths shrinkage still holds below 450^4. -/
theorem thin_radius_fraction_307 (D : Nat) (hD : (307 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (8/9 : Real)*(rho D : Real) := by
  have ht := fourthRoot_ge_307 D hD
  have hcube : (307 : Real)^3 ≤ fourthRoot D^3 :=
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
At fourth root 307, the rational cell-covering buffer is positive: (11/25 - 1001/1000*407/1000)*307 > 10. -/
theorem thin_chosen_radius_307 (D : Nat) (hD : (307 : Nat)^4 <= D) :
    (1001/1000 : Real) *
      Real.sqrt (((2*R D+S D : Nat) : Real)*Real.sqrt D/Real.pi) +
      10*Real.sqrt D <= (thinRadius D : Real) := by
  have ht := fourthRoot_ge_307 D hD
  have hi := fourthRoot_identities D
  have hq := twoRplusS_le_51percent_307 D
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
theorem thin_radius_interpolation_count_307 (D : Nat)
    (hD : (307 : Nat)^4 <= D) :
    2*(R D-1)+(S D-1) < (ellipsePairs D (thinRadius D)).card := by
  have hpositive : 0 < D := by omega
  have hR : 0 < R D := by
    unfold R envelopeR
    omega
  have hq : 0 < 2*R D+S D := by omega
  have hc := ellipsePairs_card_gt_of_ender_radius
    D (thinRadius D) (2*R D+S D) hpositive hq
    (thin_chosen_radius_307 D hD)
  omega

/-- Exact endpoint falsification: the old 78-cube source guard is
false at 307^4. The new 76-cube guard is compatible. -/
theorem old_seventyeight_cube_guard_fails_at_307 :
    R ((307 : Nat)^4) < 78*(307 : Nat)^3 := by
  norm_num [R, envelopeR]

theorem new_seventysix_cube_endpoint_307 :
    76*(307 : Nat)^3 ≤ R ((307 : Nat)^4) := by
  norm_num [R, envelopeR]

/-- The conservative source cell-area sufficient criterion changes
sign between 306 and 307. Both are exact integer inequalities. -/
theorem source_cell_criterion_sign_306_307 :
    32593*306 < 10000000 ∧ 10000000 ≤ 32593*307 := by
  norm_num

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.R_ge_seventysix_cubes_307
#print axioms TenthDiscriminant.FirstCertificate.Tuned.radius_over_R_307
#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_chosen_radius_307
#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_interpolation_count_307
#print axioms TenthDiscriminant.FirstCertificate.Tuned.old_seventyeight_cube_guard_fails_at_307
