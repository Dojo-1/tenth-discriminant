import TenthDiscriminant.EuclidCellBridge
import TenthDiscriminant.TunedRadiusFamily

/-!
# E6: Uniform original-ellipse count at fourth-root 252

Only the original quadratic lattice, rectangular rows, and ordinary-Z jets.
This file does not change the field bound, infer an arithmetic lower, or
assume that a finite-search radius works uniformly.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- Rational candidate radius; the original finite quadratic lattice is unchanged. -/
def euclidRadius (D : Nat) : Nat :=
  ⌈(81/200 : Real) * fourthRoot D ^ 3⌉₊

private theorem fourthRoot_ge_252 (D : Nat) (hD : (252 : Nat)^4 ≤ D) :
    (252 : Real) ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (252 : Nat)^2^2 ≤ D by omega)

/-- An exact rational lower buffer for the *existing* closed cell cover.
The coarser L1 radius (1+sqrt D)/2 is sufficient; no new metric axiom. -/
private theorem euclid_radius_buffer_252 (D : Nat)
    (hD : (252 : Nat)^4 ≤ D) :
    (403015/1000000 : Real) * fourthRoot D ^ 3 +
        (1 + Real.sqrt D) / 2 ≤ (euclidRadius D : Real) := by
  let t : Real := fourthRoot D
  have ht : (252 : Real) ≤ t := by
    dsimp [t]
    exact fourthRoot_ge_252 D hD
  have hi := fourthRoot_identities D
  have ht2 : t^2 = Real.sqrt D := by simpa [t] using hi.2.1
  have ht3 : (252 : Real)^3 ≤ t^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hstretch : (0 : Real) ≤ (t - 252) * t^2 :=
    mul_nonneg (by linarith) (sq_nonneg t)
  have hr : (81/200 : Real) * t^3 ≤ (euclidRadius D : Real) := by
    dsimp [t, euclidRadius]
    exact Nat.le_ceil _
  rw [← ht2]
  nlinarith only [ht3, hstretch, hr]

private theorem twoRplusS_le_51percent (D : Nat) :
    ((2*R D+S D : Nat) : Real) ≤ (51/100 : Real)*(D : Real) := by
  have hn : 100*(2*R D+S D) ≤ 51*D := by
    unfold S R envelopeR
    omega
  have hc : ((100*(2*R D+S D) : Nat) : Real) ≤
      ((51*D : Nat) : Real) := by exact_mod_cast hn
  push_cast at hc ⊢
  linarith

/-- Exact rational preflight, checked by the normalization tactic. -/
theorem euclid_252_rational_margin :
    (51/100 : Real) < (157/50 : Real) * (403015/1000000 : Real)^2 := by
  norm_num

/-- Universal point-count theorem for the original integer ellipse.
No squarefree or class-number assumption enters this geometric statement. -/
theorem euclid_radius_count_252 (D : Nat) (hD : (252 : Nat)^4 ≤ D) :
    2*R D+S D < (ellipsePairs D (euclidRadius D)).card := by
  let t : Real := fourthRoot D
  have ht : (252 : Real) ≤ t := by
    dsimp [t]
    exact fourthRoot_ge_252 D hD
  have htpos : (0 : Real) < t := by linarith
  have hi := fourthRoot_identities D
  have ht2 : t^2 = Real.sqrt D := by simpa [t] using hi.2.1
  have ht4 : t^4 = (D : Real) := by simpa [t] using hi.2.2
  have hscale : (D : Real) * Real.sqrt D = t^6 := by
    rw [← ht2, ← ht4]
    ring
  have hDpos : 0 < D := by omega
  have hbuffer := euclid_radius_buffer_252 D hD
  let a : Real := (403015/1000000 : Real) * t^3
  let b : Real := (euclidRadius D : Real) - (1 + Real.sqrt D)/2
  have ha : 0 < a := by
    dsimp [a]
    exact mul_pos (by norm_num) (pow_pos htpos 3)
  have hab : a ≤ b := by
    dsimp [a, b, t]
    linarith only [hbuffer]
  have hbnonneg : 0 ≤ b := le_trans (le_of_lt ha) hab
  have hrho : (1 + Real.sqrt D)/2 ≤ (euclidRadius D : Real) := by
    dsimp [b] at hbnonneg
    linarith
  have hsqprod : 0 ≤ (b-a)*(b+a) :=
    mul_nonneg (sub_nonneg.mpr hab) (by linarith)
  have hsq : a^2 ≤ b^2 := by nlinarith only [hsqprod]
  have hcoef : (51/100 : Real) <
      Real.pi * (403015/1000000 : Real)^2 := by
    have hpi : (157/50 : Real) < Real.pi := by
      convert Real.pi_gt_d2 using 1 <;> norm_num
    exact (euclid_252_rational_margin).trans
      (mul_lt_mul_of_pos_right hpi (by norm_num))
  have hcoefprod : (51/100 : Real)*t^6 <
      (Real.pi * (403015/1000000 : Real)^2)*t^6 :=
    mul_lt_mul_of_pos_right hcoef (pow_pos htpos 6)
  have hqprod := mul_le_mul_of_nonneg_right (twoRplusS_le_51percent D)
    (Real.sqrt_nonneg (D : Real))
  have hsqScaled : Real.pi * a^2 ≤ Real.pi * b^2 :=
    mul_le_mul_of_nonneg_left hsq Real.pi_pos.le
  have hstrict : ((2*R D+S D : Nat) : Real)*Real.sqrt D <
      Real.pi * ((euclidRadius D : Real)-(1+Real.sqrt D)/2)^2 := by
    calc
      ((2*R D+S D : Nat) : Real)*Real.sqrt D ≤
          (51/100 : Real) * (D : Real) * Real.sqrt D := hqprod
      _ = (51/100 : Real) * t^6 := by rw [mul_assoc, hscale]
      _ < (Real.pi * (403015/1000000 : Real)^2)*t^6 := hcoefprod
      _ = Real.pi * a^2 := by dsimp [a]; ring
      _ ≤ Real.pi * b^2 := hsqScaled
      _ = Real.pi * ((euclidRadius D : Real)-(1+Real.sqrt D)/2)^2 := rfl
  exact TenthDiscriminant.ellipse_card_gt_of_strict_cell_area
    D (euclidRadius D) (2*R D+S D) hDpos hrho hstrict

/-- The production interpolation count guard is weaker than 2R+S. -/
theorem euclid_interpolation_count_252 (D : Nat)
    (hD : (252 : Nat)^4 ≤ D) :
    2*(R D-1)+(S D-1) < (ellipsePairs D (euclidRadius D)).card := by
  have hc := euclid_radius_count_252 D hD
  omega

/-- Positive definite ORIGINAL real trace Gram, with J=S ordinary-Z jets. -/
theorem euclid_original_gram_posDef_252 (D : Nat)
    (hD : (252 : Nat)^4 ≤ D) :
    (rectangularTraceGram (ellipsePoints D (euclidRadius D))
        (S D) (R D) (S D)).PosDef := by
  have hp : 0 < D := by omega
  have hR : 1 ≤ R D := by unfold R envelopeR; omega
  have hS : 1 ≤ S D := by unfold S R envelopeR; omega
  apply rectangularTraceGram_posDef_of_point_count
    (ellipsePoints D (euclidRadius D)) (S D) (R D) (S D)
    hR hS le_rfl
  rw [ellipsePoints_card D (euclidRadius D) hp]
  exact euclid_interpolation_count_252 D hD

/-- ORIGINAL integer Gram determinant is positive on the certified ellipse.
This is the exact source type needed for the odd/binary arithmetic bridge. -/
theorem euclid_original_integer_gram_det_pos_252 (D : Nat)
    (hD : (252 : Nat)^4 ≤ D) :
    0 < (integerRectangularTraceGram (ellipsePairs D (euclidRadius D))
      D (S D) (R D) (S D)).det := by
  exact ellipseIntegerTraceGram_det_pos_of_count
    D (euclidRadius D) (S D) (R D) (S D)
    (by omega)
    (by unfold R envelopeR; omega)
    (by unfold S R envelopeR; omega)
    le_rfl
    (euclid_interpolation_count_252 D hD)

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.euclid_radius_count_252
#print axioms TenthDiscriminant.FirstCertificate.Tuned.euclid_interpolation_count_252
#print axioms TenthDiscriminant.FirstCertificate.Tuned.euclid_original_gram_posDef_252
#print axioms TenthDiscriminant.FirstCertificate.Tuned.euclid_original_integer_gram_det_pos_252
