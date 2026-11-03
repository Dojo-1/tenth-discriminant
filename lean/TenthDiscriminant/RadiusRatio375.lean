import TenthDiscriminant.ThinRadiusAnalyticGain

/-!
# Phase171: recover the original radius-over-R constant below 450^4

The original definitions R = floor(D/4), rho = ceil((13/25)*D^(3/4))
and thinRadius = ceil((11/25)*D^(3/4)) are unchanged.

At the new lower domain D >= 375^4, the coarse inequality D/5 <= R
throws away more information than needed. We instead keep the exact
integer remainder 4*R >= D-3. No class-number or determinant assertion
appears in this module.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

private theorem root_ge_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    (375 : Real) ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (375 : Nat)^2^2 ≤ D by omega)

/-- Exact floor remainder gives R at least 90 fourth-root cubes. -/
theorem R_ge_ninety_cubes_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    (90 : Real)*fourthRoot D^3 ≤ R D := by
  have hi := fourthRoot_identities D
  have ht := root_ge_375 D hD
  have hcube : (375 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hgap : (15 : Real) ≤ fourthRoot D-360 := by linarith
  have hproduct := mul_le_mul_of_nonneg_right hgap (pow_nonneg hi.1 3)
  have h3 : (3 : Real) ≤ 15*fourthRoot D^3 := by
    nlinarith only [hcube]
  have hfloor : D ≤ 4*R D+3 := by
    unfold R envelopeR
    omega
  have hf : (D : Real) ≤ 4*(R D : Real)+3 := by
    exact_mod_cast hfloor
  rw [← hi.2.2] at hf
  nlinarith only [hf,hproduct,h3]

/-- The same 521/1000 rounding envelope remains valid at root 375. -/
theorem rho_upper_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    (rho D : Real) ≤ (521/1000 : Real)*fourthRoot D^3 := by
  have ht := root_ge_375 D hD
  have hcube : (375 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (rho D : Real) <
      (13/25 : Real)*fourthRoot D^3+1 := by
    unfold rho
    exact Nat.ceil_lt_add_one (by positivity)
  nlinarith only [hcube,hceil]

/-- Recover exactly the former analytic constant, without old root>=450. -/
theorem radius_over_R_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    (rho D : Real)/R D ≤ 521/90000 := by
  have hR := R_ge_ninety_cubes_375 D hD
  have hu := rho_upper_375 D hD
  have ht : (0 : Real) < fourthRoot D := by
    linarith [root_ge_375 D hD]
  have hp : (0 : Real) < fourthRoot D^3 := pow_pos ht 3
  have hRpos : (0 : Real) < R D := by nlinarith only [hR,hp]
  apply (div_le_iff₀ hRpos).2
  nlinarith only [hR,hu]

/-- The existing eighths/ninths shrinkage still holds below 450^4. -/
theorem thin_radius_fraction_375 (D : Nat) (hD : (375 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (8/9 : Real)*(rho D : Real) := by
  have ht := root_ge_375 D hD
  have hcube : (375 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hrho : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  nlinarith only [hcube,hceil,hrho]

end
end TenthDiscriminant.FirstCertificate.Tuned
