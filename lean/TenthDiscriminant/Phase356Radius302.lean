import TenthDiscriminant.Phase342Geometry307
import TenthDiscriminant.Phase332StrongerRadius315

/-!
# Phase356: 302-root source-exact radius repair

The previous uniform 307 proof used R >= 76*t^3. At t=302 this
fails even on the original perfect fourth-power source parameter.
We do NOT transplant that false lemma. Instead we prove R >= 75*t^3,
a correspondingly weaker rho/R budget, and the same strong 17/20
thin-vs-padded contraction on the unchanged ceil-defined radii.

No determinant estimate, odd-prime lower, class number, or field bound
is asserted here.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

theorem fourthRoot_ge_302 (D : Nat) (hD : (302 : Nat)^4 ≤ D) :
    (302 : Real) ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (302 : Nat)^2^2 ≤ D by omega)

/-- Keep the ORIGINAL padded ceil-radius envelope, without floats. -/
theorem rho_upper_302 (D : Nat) (hD : (302 : Nat)^4 ≤ D) :
    (rho D : Real) ≤ (521/1000 : Real)*fourthRoot D^3 := by
  have ht := fourthRoot_ge_302 D hD
  have hcube : (302 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (rho D : Real) <
      (13/25 : Real)*fourthRoot D^3+1 := by
    unfold rho
    exact Nat.ceil_lt_add_one (by positivity)
  nlinarith only [hcube,hceil]

/-- Floor-exact 75-cube bound valid uniformly for every integer D>=302^4.
The old 76-cube guard is FALSE at the 302^4 endpoint. -/
theorem R_ge_seventyfive_cubes_302 (D : Nat)
    (hD : (302 : Nat)^4 ≤ D) :
    (75 : Real)*fourthRoot D^3 ≤ R D := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_302 D hD
  have hcube : (302 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hgap : (2 : Real) ≤ fourthRoot D-300 := by linarith
  have hproduct := mul_le_mul_of_nonneg_right hgap (pow_nonneg hi.1 3)
  have h3 : (3 : Real) ≤ 2*fourthRoot D^3 := by
    nlinarith only [hcube]
  have hfloor : D ≤ 4*R D+3 := by
    unfold R envelopeR
    omega
  have hf : (D : Real) ≤ 4*(R D : Real)+3 := by
    exact_mod_cast hfloor
  rw [← hi.2.2] at hf
  nlinarith only [hf,hproduct,h3]

/-- Entire original padded radius divided by the original row count. -/
theorem radius_over_R_302 (D : Nat) (hD : (302 : Nat)^4 ≤ D) :
    (rho D : Real)/R D ≤ 521/75000 := by
  have hR := R_ge_seventyfive_cubes_302 D hD
  have hu := rho_upper_302 D hD
  have ht : (0 : Real) < fourthRoot D := by
    linarith [fourthRoot_ge_302 D hD]
  have hp : (0 : Real) < fourthRoot D^3 := pow_pos ht 3
  have hRpos : (0 : Real) < R D := by nlinarith only [hR,hp]
  apply (div_le_iff₀ hRpos).2
  nlinarith only [hR,hu]

/-- Numerically generous endpoint error budget at 302. -/
theorem endpoint_fraction_budget_302 :
    (521/75000 : Real)+(1/9000 : Real) < 1/100 := by
  norm_num

/-- The precise ORIGINAL thin and padded integer-ceil radii still
satisfy the stronger 17/20 contraction uniformly at 302. -/
theorem thin_radius_fraction_17_20_302 (D : Nat)
    (hD : (302 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (17/20 : Real)*(rho D : Real) := by
  have ht := fourthRoot_ge_302 D hD
  have hcube : (302 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hlarge : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  nlinarith only [hcube,hceil,hlarge]

/-- Source-exact abstract normalized radius saving survives at 302.
This still requires separate SAME-GRAM Hadamard and scalar upper. -/
theorem original_radius_saving_302 (D : Nat)
    (hD : (302 : Nat)^4 ≤ D) (n : Real) :
    enderUpperB (R D) (S D) (S D) (thinRadius D) n /
        comparisonScale (R D) (S D) + 27/200 ≤
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
    linarith [fourthRoot_ge_302 D hD]
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
  exact upperB_strong_17_20_saving
    (R D) (S D) (rho D) (thinRadius D) n
    hR hS h25 hOld hSmall (thin_radius_fraction_17_20_302 D hD)

/-- FALSIFIER: the old 307-domain 76-cube inequality is not valid
on the actual 302^4 parameter, even before arbitrary D rounding. -/
theorem original_76_cube_guard_false_at_302 :
    R ((302 : Nat)^4) < 76*(302 : Nat)^3 := by
  norm_num [R,envelopeR]

/-- The weakened 75-cube endpoint has positive exact slack. -/
theorem original_75_cube_guard_true_at_302 :
    75*(302 : Nat)^3 ≤ R ((302 : Nat)^4) := by
  norm_num [R,envelopeR]

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.R_ge_seventyfive_cubes_302
#print axioms TenthDiscriminant.FirstCertificate.Tuned.radius_over_R_302
#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_fraction_17_20_302
#print axioms TenthDiscriminant.FirstCertificate.Tuned.original_radius_saving_302
#print axioms TenthDiscriminant.FirstCertificate.Tuned.original_76_cube_guard_false_at_302
