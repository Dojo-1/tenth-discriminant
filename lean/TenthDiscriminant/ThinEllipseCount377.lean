import TenthDiscriminant.ThinEllipseCount

/-!
# Phase170 -- the original thin-ellipse interpolation count at 377^4

The support remains ellipsePairs D (thinRadius D) and the sufficient
interpolation guard remains 2*(R-1)+(S-1) < card Q.

A local candidate. This file has NOT been compiled against pinned Lean.
It neither assumes class number one nor proves a discriminant cutoff.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- Only the 377 fourth-root bound, not the old 450-root assumption. -/
theorem fourthRoot_ge_377 (D : Nat) (hD : (377 : Nat)^4 <= D) :
    (377 : Real) <= fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (377 : Nat)^2^2 <= D by omega)

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
  push_cast at hc
  linarith

/-- The existing cell-area sufficient criterion at the smaller floor.
At fourth root 377, the rounding remainder is 23299/1000000 > 0. -/
theorem thin_chosen_radius_377 (D : Nat) (hD : (377 : Nat)^4 <= D) :
    (1001/1000 : Real) *
      Real.sqrt (((2*R D+S D : Nat) : Real)*Real.sqrt D/Real.pi) +
      10*Real.sqrt D <= (thinRadius D : Real) := by
  have ht := fourthRoot_ge_377 D hD
  have hi := fourthRoot_identities D
  have hq := twoRplusS_le_51percent D
  have hqm := mul_le_mul_of_nonneg_right hq (Real.sqrt_nonneg (D : Real))
  have hpow : (D : Real)*Real.sqrt D = fourthRoot D^6 := by
    rw [← hi.2.1, ← hi.2.2]
    ring
  have hinner : Real.sqrt
      (((2*R D+S D : Nat) : Real)*Real.sqrt D / Real.pi) <=
      (413/1000 : Real)*fourthRoot D^3 := by
    apply Real.sqrt_le_iff.mpr
    refine ⟨by positivity,(div_le_iff₀ Real.pi_pos).2 ?_⟩
    have hp := mul_le_mul_of_nonneg_right Real.pi_gt_d2.le
      (sq_nonneg ((413/1000 : Real)*fourthRoot D^3))
    have hq' : ((2*R D+S D : Nat) : Real)*Real.sqrt D <=
        (51/100 : Real)*fourthRoot D^6 := by
      simpa only [mul_assoc,hpow] using hqm
    nlinarith only [hp,hq',pow_nonneg hi.1 6]
  have herror := mul_nonneg (sq_nonneg (fourthRoot D))
    (show 0 <= (11/25-1001/1000*413/1000 : Real)*fourthRoot D-10 by
      linarith)
  have hl : (11/25 : Real)*fourthRoot D^3 <= thinRadius D := by
    unfold thinRadius
    exact Nat.le_ceil _
  rw [← hi.2.1] at hinner ⊢
  nlinarith only [hinner,herror,hl]

/-- Original-Q count, with no metric, field or prime-divisor change. -/
theorem thin_radius_interpolation_count_377 (D : Nat)
    (hD : (377 : Nat)^4 <= D) :
    2*(R D-1)+(S D-1) < (ellipsePairs D (thinRadius D)).card := by
  have hpositive : 0 < D := by omega
  have hR : 0 < R D := by
    unfold R envelopeR
    omega
  have hq : 0 < 2*R D+S D := by omega
  have hc := ellipsePairs_card_gt_of_ender_radius
    D (thinRadius D) (2*R D+S D) hpositive hq
    (thin_chosen_radius_377 D hD)
  omega

end
end TenthDiscriminant.FirstCertificate.Tuned
