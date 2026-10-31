import TenthDiscriminant.TunedRadiusFamily
import TenthDiscriminant.EllipseCellArea

/-!
# Phase140: a thinner certified interpolation ellipse

The old production radius was chosen to guarantee the stronger 3R+S
point count, while the ORIGINAL interpolation theorem actually requires
only 2*(R-1)+(S-1) points. This module explores that slack on the SAME
quadratic integer lattice. It does not alter a prime factor, analytic
upper bound, class-number-one bridge or field discriminant theorem.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- A geometric candidate independent of the old production radius. -/
def thinRadius (D : Nat) : Nat :=
  ⌈(11/25 : Real) * fourthRoot D ^ 3⌉₊

/-- The smaller 0.44 D^(3/4) radius still obeys the existing, fully
proved cell-area point-count criterion when the target is 2R+S. -/
theorem thin_chosen_radius (D : Nat) (hD : 41006250000 ≤ D) :
    (1001/1000 : Real) *
        Real.sqrt (((2*R D+S D : Nat) : Real) * Real.sqrt D / Real.pi) +
      10*Real.sqrt D ≤ (thinRadius D : Real) := by
  have hd := dimensions D hD
  have ht := root_large D hD
  have hi := fourthRoot_identities D
  have hq : ((2*R D+S D : Nat) : Real) ≤ (51/100 : Real)*(D : Real) := by
    push_cast
    linarith [hd.2.2.2.2.2.1,hd.2.2.2.2.2.2]
  have hqm := mul_le_mul_of_nonneg_right hq (Real.sqrt_nonneg (D : Real))
  have hpow : (D : Real)*Real.sqrt D = fourthRoot D^6 := by
    rw [← hi.2.1, ← hi.2.2]
    ring
  have hinner :
      Real.sqrt (((2*R D+S D : Nat) : Real)*Real.sqrt D/Real.pi) ≤
      (413/1000 : Real)*fourthRoot D^3 := by
    apply Real.sqrt_le_iff.mpr
    refine ⟨by positivity,(div_le_iff₀ Real.pi_pos).2 ?_⟩
    have hp := mul_le_mul_of_nonneg_right Real.pi_gt_d2.le
      (sq_nonneg ((413/1000 : Real)*fourthRoot D^3))
    have hq' :
        ((2*R D+S D : Nat) : Real)*Real.sqrt D ≤
          (51/100 : Real)*fourthRoot D^6 := by
      simpa only [mul_assoc,hpow] using hqm
    nlinarith only [hp,hq',pow_nonneg hi.1 6]
  have herror := mul_nonneg (sq_nonneg (fourthRoot D))
    (show 0 ≤ (11/25-1001/1000*413/1000 : Real)*fourthRoot D-10 by linarith)
  have hl : (11/25 : Real)*fourthRoot D^3 ≤ thinRadius D := by
    unfold thinRadius
    exact Nat.le_ceil _
  rw [← hi.2.1] at hinner ⊢
  nlinarith only [hinner,herror,hl]

/-- No squarefree or class-number assumption is needed for the geometric
count: the thinner ellipse still satisfies the SAME interpolation guard. -/
theorem thin_radius_interpolation_count (D : Nat) (hD : 41006250000 ≤ D) :
    2*(R D-1)+(S D-1) <
      (ellipsePairs D (thinRadius D)).card := by
  have hd := dimensions D hD
  have hpositive : 0 < D := by omega
  have hq : 0 < 2*R D+S D := by omega
  have hc := ellipsePairs_card_gt_of_ender_radius
    D (thinRadius D) (2*R D+S D) hpositive hq
    (thin_chosen_radius D hD)
  omega

/-- A narrower integer radius without reworking its point count can fail
the sufficient interpolation guard. -/
theorem toy_radius_four_loses_count :
    ¬ 2*(8-1)+(4-1) < (ellipsePairs 19 4).card := by
  decide

end
end TenthDiscriminant.FirstCertificate.Tuned
