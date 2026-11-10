import TenthDiscriminant.FloorSum
import TenthDiscriminant.Phase228CombinedBasis

/-!
# Phase259 — exact horizontal mass and normalization-free scalar gate

Only existing floorSum and row-major source exponent definitions are used.
This module does not assume the production determinant normalization, nor
does it claim the 321^4 field-level theorem.
-/

namespace TenthDiscriminant.Phase259

open scoped BigOperators

/-- Subtraction-safe floor-sum identity for every positive denominator. -/
theorem floorSum_horizontal_certificate (q S : ℕ) (hq : 0 < q) :
    2 * q * floorSum S q + q * S =
      S * S + (S % q) * (q - S % q) := by
  have hs := floorSum_scaled S q
  have hscaled := congrArg (fun z : ℕ => q * z) hs
  have hdiv : S = q * (S / q) + S % q := by
    have hh := Nat.mod_add_div S q
    omega
  have hdivMul := congrArg (fun z : ℕ => q * z) hdiv
  have hdivSq := congrArg (fun z : ℕ => z * z) hdiv
  have hrem : q - S % q + S % q = q :=
    Nat.sub_add_cancel (Nat.le_of_lt (Nat.mod_lt S hq))
  have hremMul := congrArg (fun z : ℕ => (S % q) * z) hrem
  nlinarith only [hscaled, hdivMul, hdivSq, hremMul]

/-- Horizontal mass in a rectangle, using the original row-major labels. -/
theorem horizontal_rectangle_certificate (R S q : ℕ) (hq : 0 < q) :
    2 * q * (R * floorSum S q) + q * R * S =
      R * S * S + R * (S % q) * (q - S % q) := by
  calc
    2 * q * (R * floorSum S q) + q * R * S =
        R * (2 * q * floorSum S q + q * S) := by ring
    _ = R * (S * S + (S % q) * (q - S % q)) := by
      rw [floorSum_horizontal_certificate q S hq]
    _ = R * S * S + R * (S % q) * (q - S % q) := by ring

/-- Exact source-to-arithmetic bridge for the existing combined basis. -/
theorem original_row_major_horizontal_sum (R S p : ℕ) :
    (∑ i : Fin (R * S),
      TenthDiscriminant.Phase228.horizontalBasisExponent R S p i) =
        R * floorSum S (p * p) := by
  simpa only [floorSum] using
    (TenthDiscriminant.Phase228.sum_horizontalBasisExponent R S p)

/-- Exact p=3 horizontal count. -/
theorem horizontal_three (R S : ℕ) :
    18 * (R * floorSum S 9) + 9 * R * S =
      R * S * S + R * (S % 9) * (9 - S % 9) :=
  horizontal_rectangle_certificate R S 9 (by omega)

/-- Exact p=5 horizontal count. -/
theorem horizontal_five (R S : ℕ) :
    50 * (R * floorSum S 25) + 25 * R * S =
      R * S * S + R * (S % 25) * (25 - S % 25) :=
  horizontal_rectangle_certificate R S 25 (by omega)

/-- Conservative rational log-weighted horizontal mass. -/
def weightedHorizontal (R S : ℕ) : ℚ :=
  2 * ((1098 / 1000 : ℚ) * (↑(R * floorSum S 9) : ℚ) +
       (1609 / 1000 : ℚ) * (↑(R * floorSum S 25) : ℚ))

/-- Exact periodic correction, period 225. -/
def correction (S : ℕ) : ℚ :=
  (61 / 500 : ℚ) * (↑((S % 9) * (9 - S % 9)) : ℚ) +
  (1609 / 25000 : ℚ) * (↑((S % 25) * (25 - S % 25)) : ℚ)

theorem correction_nonneg (S : ℕ) : 0 ≤ correction S := by
  unfold correction
  positivity

theorem correction_periodic (S : ℕ) :
    correction (S + 225) = correction S := by
  have h9 : (S + 225) % 9 = S % 9 := by omega
  have h25 : (S + 225) % 25 = S % 25 := by omega
  simp [correction, h9, h25]

/-- Exact quadratic decomposition with periodic correction. -/
theorem weightedHorizontal_closed (R S : ℕ) :
    weightedHorizontal R S =
      (R : ℚ) *
        ((4659 / 25000 : ℚ) * (S : ℚ) ^ 2 -
         (2707 / 1000 : ℚ) * (S : ℚ) + correction S) := by
  have h9 := horizontal_three R S
  have h25 := horizontal_five R S
  have h9q' :
      (18 : ℚ) * (↑(R * floorSum S 9) : ℚ) +
          9 * (R : ℚ) * (S : ℚ) =
        (R : ℚ) * (S : ℚ) * (S : ℚ) +
          (R : ℚ) * (↑(S % 9) : ℚ) * (↑(9 - S % 9) : ℚ) := by
    exact_mod_cast h9
  have h9q :
      (18 : ℚ) * (↑(R * floorSum S 9) : ℚ) +
          9 * (R : ℚ) * (S : ℚ) =
        (R : ℚ) * (S : ℚ) * (S : ℚ) +
          (R : ℚ) * (↑((S % 9) * (9 - S % 9)) : ℚ) := by
    exact_mod_cast h9
  have h25q' :
      (50 : ℚ) * (↑(R * floorSum S 25) : ℚ) +
          25 * (R : ℚ) * (S : ℚ) =
        (R : ℚ) * (S : ℚ) * (S : ℚ) +
          (R : ℚ) * (↑(S % 25) : ℚ) * (↑(25 - S % 25) : ℚ) := by
    exact_mod_cast h25
  have h25q :
      (50 : ℚ) * (↑(R * floorSum S 25) : ℚ) +
          25 * (R : ℚ) * (S : ℚ) =
        (R : ℚ) * (S : ℚ) * (S : ℚ) +
          (R : ℚ) * (↑((S % 25) * (25 - S % 25)) : ℚ) := by
    exact_mod_cast h25
  unfold weightedHorizontal correction
  linear_combination (61 / 500 : ℚ) * h9q +
    (1609 / 25000 : ℚ) * h25q

/-- Integer-scaled weighted count without normalization. -/
theorem weightedHorizontal_scaled (R S : ℕ) :
    1000 * weightedHorizontal R S =
      2 * (1098 * (↑(R * floorSum S 9) : ℚ) +
           1609 * (↑(R * floorSum S 25) : ℚ)) := by
  unfold weightedHorizontal
  ring

theorem correction_max_witness : correction 13 = 78001 / 6250 := by
  norm_num [correction]

theorem pilot_horizontal_mass : weightedHorizontal 100 30 = 47573 / 5 := by
  have h9 : floorSum 30 9 = 36 := by decide
  have h25 : floorSum 30 25 = 5 := by decide
  norm_num [weightedHorizontal, h9, h25]

/-- The target rational horizontal contribution; D is positive below. -/
def targetHorizontal (D : ℚ) : ℚ :=
  4659 / 625000 - 36167 / (1250 * D)

/-- A cross-multiplied certificate suffices for a normalized gain.
No hypothesis N(D)=R(D)*D is introduced. -/
theorem gain_of_integer_certificate (D N W : ℚ)
    (hD : 0 < D) (hN : 0 < N)
    (hCert : N * (4659 * D - 18083500) ≤ 625000 * D * W) :
    targetHorizontal D ≤ W / N := by
  have hDne : D ≠ 0 := ne_of_gt hD
  have hNne : N ≠ 0 := ne_of_gt hN
  have hscale : 0 < (625000 : ℚ) * D * N := by positivity
  have hEq :
      ((625000 : ℚ) * D * N) * (W / N - targetHorizontal D) =
        625000 * D * W - N * (4659 * D - 18083500) := by
    unfold targetHorizontal
    field_simp
    ring
  have hnonneg :
      0 ≤ ((625000 : ℚ) * D * N) * (W / N - targetHorizontal D) := by
    rw [hEq]
    linarith
  by_contra hh
  have hneg : W / N - targetHorizontal D < 0 := by linarith
  have hprodneg :
      ((625000 : ℚ) * D * N) * (W / N - targetHorizontal D) < 0 :=
    mul_neg_of_pos_of_neg hscale hneg
  linarith

def baseline : ℚ := -3092821 / 1250000000

theorem exact_budget_321 :
    baseline + targetHorizontal ((321 : ℚ) ^ 4) =
      66095476170359899 / 13271809601250000000 := by
  norm_num [baseline, targetHorizontal]

theorem exact_safety_budget_321 :
    baseline + targetHorizontal ((321 : ℚ) ^ 4) - 1 / 250 =
      13008237765359899 / 13271809601250000000 := by
  norm_num [baseline, targetHorizontal]

/-- Abstract two-error closure, awaiting the actual same-Gram hypotheses. -/
theorem two_error_contradiction
    (m0 h0 margin gain epsB epsH : ℝ)
    (hDet : margin + gain ≤ 0)
    (hBase : m0 - epsB ≤ margin)
    (hGain : h0 - epsH ≤ gain)
    (hBudget : epsB + epsH < m0 + h0) :
    False := by
  linarith

end TenthDiscriminant.Phase259

#print axioms TenthDiscriminant.Phase259.floorSum_horizontal_certificate
#print axioms TenthDiscriminant.Phase259.original_row_major_horizontal_sum
#print axioms TenthDiscriminant.Phase259.weightedHorizontal_closed
#print axioms TenthDiscriminant.Phase259.gain_of_integer_certificate
#print axioms TenthDiscriminant.Phase259.two_error_contradiction
