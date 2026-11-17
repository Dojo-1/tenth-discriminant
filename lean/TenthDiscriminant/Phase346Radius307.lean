import TenthDiscriminant.Phase342Geometry307
import TenthDiscriminant.Phase332StrongerRadius315

/-!
# Phase346 -- exact 307-domain radius contraction on the ORIGINAL source

The Phase342 radius/R bound at 307^4 is weaker than its 313 counterpart.
Nevertheless the stronger thinRadius/rho <= 17/20 contraction survives
with the SAME ceil-defined integer radii. This specializes the already
proved abstract 27/200 Hadamard saving to the 307 domain.

This file makes NO assertion about the full 307-domain analytic Gram
upper, odd-prime arithmetic lower, or actual field discriminant.
CI / axiom checks are required before promoting these Lean declarations.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- The original thin and padded radii still satisfy the stronger
17/20 contraction for every D >= 307^4, without changing either ceiling. -/
theorem thin_radius_fraction_17_20_307 (D : Nat)
    (hD : (307 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (17/20 : Real) * (rho D : Real) := by
  have ht := fourthRoot_ge_307 D hD
  have hcube : (307 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hlarge : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  nlinarith only [hcube,hceil,hlarge]

/-- A rational budget: the weaker 307-domain rho/R ratio and the
unchanged logarithmic cost could still fit under the 1/100 envelope.
This does not itself supply the logarithmic cost theorem at 307. -/
theorem endpoint_fraction_budget_307 :
    (521/76000 : Real)+(1/9000 : Real) < 1/100 := by
  norm_num

/-- Specialize the pre-existing abstract Hadamard radius saving to
the *original* 307-domain floor dimensions and integer radii.
Only the analytic envelope is affected, not the original Gram. -/
theorem original_radius_saving_307 (D : Nat)
    (hD : (307 : Nat)^4 ≤ D) (n : Real) :
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
    linarith [fourthRoot_ge_307 D hD]
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
    hR hS h25 hOld hSmall (thin_radius_fraction_17_20_307 D hD)

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_fraction_17_20_307
#print axioms TenthDiscriminant.FirstCertificate.Tuned.endpoint_fraction_budget_307
#print axioms TenthDiscriminant.FirstCertificate.Tuned.original_radius_saving_307
