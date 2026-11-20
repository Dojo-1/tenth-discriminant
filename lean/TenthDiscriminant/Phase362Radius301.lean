import TenthDiscriminant.Phase361StrongerRadius301

/-!
# Phase362 — original padded ceil radius, 301^4 uniform floor guard

No new source or original Gram: rho = ceil((13/25)*t^3), R=floor(D/4).
At 301^4 the valid bound is R >= 75*t^3; the old 76*t^3
bound fails. These are analytical guard lemmas, not field claims.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

theorem rho_upper_301 (D : Nat) (hD : (301 : Nat)^4 ≤ D) :
    (rho D : Real) ≤ (521/1000 : Real)*fourthRoot D^3 := by
  have ht := fourthRoot_ge_301 D hD
  have hcube : (301 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (rho D : Real) <
      (13/25 : Real)*fourthRoot D^3+1 := by
    unfold rho
    exact Nat.ceil_lt_add_one (by positivity)
  nlinarith only [hcube,hceil]

theorem R_ge_seventyfive_cubes_301 (D : Nat)
    (hD : (301 : Nat)^4 ≤ D) :
    (75 : Real)*fourthRoot D^3 ≤ R D := by
  have hi := fourthRoot_identities D
  have ht := fourthRoot_ge_301 D hD
  have hcube : (301 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hgap : (1 : Real) ≤ fourthRoot D-300 := by linarith
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

theorem radius_over_R_301 (D : Nat) (hD : (301 : Nat)^4 ≤ D) :
    (rho D : Real)/R D ≤ 521/75000 := by
  have hR := R_ge_seventyfive_cubes_301 D hD
  have hu := rho_upper_301 D hD
  have ht : (0 : Real) < fourthRoot D := by
    linarith [fourthRoot_ge_301 D hD]
  have hp : (0 : Real) < fourthRoot D^3 := pow_pos ht 3
  have hRpos : (0 : Real) < R D := by nlinarith only [hR,hp]
  apply (div_le_iff₀ hRpos).2
  nlinarith only [hR,hu]

theorem endpoint_fraction_budget_301 :
    (521/75000 : Real)+(1/9000 : Real) < 1/100 := by
  norm_num

/-- Negative control: old 76-cube radius guard already fails at 301^4. -/
theorem original_76_cube_guard_false_at_301 :
    R ((301 : Nat)^4) < 76*(301 : Nat)^3 := by
  norm_num [R,envelopeR]

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.R_ge_seventyfive_cubes_301
#print axioms TenthDiscriminant.FirstCertificate.Tuned.radius_over_R_301
#print axioms TenthDiscriminant.FirstCertificate.Tuned.original_76_cube_guard_false_at_301
