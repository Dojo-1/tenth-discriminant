import TenthDiscriminant.Phase228CombinedBasis
import TenthDiscriminant.TunedRadiusFamily
import TenthDiscriminant.NormalizedComparison

/-!
# Phase259: exact horizontal p² mass at the original 321⁴ source dimensions

The production rectangle is R=floor(D/4), S=floor(R/25), and the
normalization is comparisonScale R S = R²*S.  The mass below is the
horizontal part of the SAME combined integral Frobenius source frame,
not a second determinant or a replacement observation family.

This file proves an arithmetic lower bound for that row mass.  It does
NOT assert that the mass is an additive increment to the pre-existing
global prime lower bound: that no-double-counting/logarithmic bridge
and the 321-domain analytic upper remain separate obligations.
-/

namespace TenthDiscriminant.Phase259
open scoped BigOperators
open TenthDiscriminant.Phase228

def floorMass (q S : Nat) : Nat :=
  ∑ s ∈ Finset.range S, s / q

/-- Elementary lower bound; no exact floor-period table is needed.
For each s, q*(s/q)+(q-1) >= s. -/
theorem floorMass_lower (q S : Nat) (hq : 0 < q) :
    S*S ≤ 2*q*floorMass q S + (2*q-1)*S := by
  have hpoint (s : Nat) : s ≤ q*(s/q)+(q-1) := by
    have hm : s % q < q := Nat.mod_lt s hq
    have hd := Nat.mod_add_div s q
    omega
  have hsum : (∑ s ∈ Finset.range S, s) ≤
      ∑ s ∈ Finset.range S, (q*(s/q)+(q-1)) := by
    exact Finset.sum_le_sum (fun s _ => hpoint s)
  have hrewrite :
      (∑ s ∈ Finset.range S, (q*(s/q)+(q-1))) =
        q*floorMass q S+(q-1)*S := by
    simp only [Finset.sum_add_distrib, Finset.sum_const,
      Finset.card_range, nsmul_eq_mul, ← Finset.mul_sum]
    unfold floorMass
    simp only [Nat.cast_id, mul_comm]
  rw [hrewrite] at hsum
  have hsumid : 2*(∑ s ∈ Finset.range S, s)+S = S*S := by
    have h := Finset.sum_range_id_mul_two S
    cases S with
    | zero => simp
    | succ s =>
      simp only [Nat.succ_sub_one] at h
      nlinarith
  have hcoef : 2*q-1 = 2*(q-1)+1 := by omega
  rw [hcoef]
  nlinarith only [hsum, hsumid]

/-- Integer-weighted p=3 and p=5 horizontal floor certificate.
1098/1000 and 1609/1000 are conservative log-prime coefficients. -/
theorem weighted_floor_lower (S : Nat) :
    116475*S*S ≤
      1250*(1098*floorMass 9 S+1609*floorMass 25 S)
        +3267275*S := by
  have h9 := floorMass_lower 9 S (by decide)
  have h25 := floorMass_lower 25 S (by decide)
  norm_num at h9 h25
  nlinarith only [h9, h25]

/-- The source normalization needs the actual remainder R % 25.
This estimate is deliberately uniform over all 25 remainders. -/
private theorem rounding_guard (D R : Nat) (hcap : D ≤ 5*R) :
    D*(3267275+4659*(R%25)) ≤ 16895455*R := by
  have hmod : R%25 < 25 := Nat.mod_lt R (by decide)
  have hcoef : 3267275+4659*(R%25) ≤ 3379091 := by omega
  calc
    D*(3267275+4659*(R%25)) ≤ D*3379091 :=
      Nat.mul_le_mul_left D hcoef
    _ = 3379091*D := by ring
    _ ≤ 3379091*(5*R) := Nat.mul_le_mul_left 3379091 hcap
    _ = 16895455*R := by ring

/-- Quotient-free certificate for the original production rectangle.
The identity R=25*S+(R%25) is essential, not an asymptotic approximation. -/
theorem horizontal_mass_core (D R S : Nat)
    (hcap : D ≤ 5*R) (hS : S = R/25) :
    4659*D*R*S ≤
      1250*D*(1098*floorMass 9 S+1609*floorMass 25 S)
        +16895455*R*S := by
  have hdiv : R = 25*S+R%25 := by
    have hd := Nat.mod_add_div R 25
    omega
  have hw := weighted_floor_lower S
  have hwD := Nat.mul_le_mul_left D hw
  have hr := rounding_guard D R hcap
  have hrS := Nat.mul_le_mul_right S hr
  calc
    4659*D*R*S =
        116475*D*S*S+4659*D*(R%25)*S := by
      calc
        4659*D*R*S = 4659*D*(25*S+R%25)*S :=
          congrArg (fun n : Nat => 4659*D*n*S) hdiv
        _ = _ := by ring
    _ ≤ 1250*D*(1098*floorMass 9 S+1609*floorMass 25 S)
          +3267275*D*S+4659*D*(R%25)*S := by
      nlinarith only [hwD]
    _ ≤ 1250*D*(1098*floorMass 9 S+1609*floorMass 25 S)
          +16895455*R*S := by
      nlinarith only [hrS]

/-- The *actual* combined source matrix horizontal row exponents,
summed over the unchanged R*S row-major source for inert 3 and 5. -/
def horizontalPrimeMass (R S : Nat) : Nat :=
    1098*(∑ i : Fin (R*S), horizontalBasisExponent R S 3 i)
      +1609*(∑ i : Fin (R*S), horizontalBasisExponent R S 5 i)

theorem horizontalPrimeMass_eq (R S : Nat) :
    horizontalPrimeMass R S =
      R*(1098*floorMass 9 S+1609*floorMass 25 S) := by
  unfold horizontalPrimeMass
  rw [sum_horizontalBasisExponent R S 3,
      sum_horizontalBasisExponent R S 5]
  simp only [show 3*3=9 by norm_num, show 5*5=25 by norm_num]
  unfold floorMass
  ring

/-- Exact integral certificate in the production R²*S normalization.
It is a statement about row exponent mass, NOT yet about log(det Gram). -/
theorem horizontal_mass_certificate (D R S : Nat)
    (hcap : D ≤ 5*R) (hS : S = R/25) :
    4659*D*(R^2*S) ≤
      1250*D*(horizontalPrimeMass R S)+16895455*(R^2*S) := by
  rw [horizontalPrimeMass_eq]
  have hc := horizontal_mass_core D R S hcap hS
  calc
    4659*D*(R^2*S) = R*(4659*D*R*S) := by ring
    _ ≤ R*(1250*D*(1098*floorMass 9 S+1609*floorMass 25 S)
            +16895455*R*S) := Nat.mul_le_mul_left R hc
    _ = 1250*D*(R*(1098*floorMass 9 S+1609*floorMass 25 S))
          +16895455*(R^2*S) := by ring

/-- The rationally weighted horizontal mass, normalized exactly as the
original trace-Gram comparison: comparisonScale R S = R²*S. -/
noncomputable def normalizedHorizontalGain (R S : Nat) : Real :=
  (horizontalPrimeMass R S : Real)/500 /
    FirstCertificate.comparisonScale R S

theorem normalizedHorizontalGain_lower
    (D R S : Nat) (hD : 0 < D) (hR : 0 < R) (hSpos : 0 < S)
    (hcap : D ≤ 5*R) (hS : S = R/25) :
    (4659/625000 : Real)-16895455/(625000*(D : Real)) ≤
      normalizedHorizontalGain R S := by
  have hcert := horizontal_mass_certificate D R S hcap hS
  have hreal :
      (4659 : Real)*(D : Real)*((R : Real)^2*(S : Real)) ≤
        1250*(D : Real)*(horizontalPrimeMass R S : Real)
          +16895455*((R : Real)^2*(S : Real)) := by
    exact_mod_cast hcert
  have hscale := FirstCertificate.comparisonScale_pos R S hR hSpos
  have hDpos : (0 : Real) < D := by exact_mod_cast hD
  unfold normalizedHorizontalGain
  apply (le_div_iff₀ hscale).2
  change ((4659/625000 : Real)-16895455/(625000*(D : Real))) *
      ((R : Real)^2*(S : Real)) ≤
        (horizontalPrimeMass R S : Real)/500
  have hrewrite :
      (4659/625000 : Real)-16895455/(625000*(D : Real)) =
        (4659*(D : Real)-16895455)/(625000*(D : Real)) := by
    field_simp [ne_of_gt hDpos]
    <;> ring
  rw [hrewrite, div_mul_eq_mul_div]
  apply (div_le_iff₀ (by positivity : (0 : Real) < 625000*(D : Real))).2
  nlinarith only [hreal]

/-- The source dimensions used by the 322 proof remain valid at 321⁴.
This is a bound on actual row mass; source-to-log-det is a separate gate. -/
theorem production_horizontal_gain_lower (D : Nat)
    (hD : (321 : Nat)^4 ≤ D) :
    (4659/625000 : Real)-16895455/(625000*(D : Real)) ≤
      normalizedHorizontalGain
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
  have hlarge : 100 ≤ D := by
    norm_num at hD
    omega
  have hDpos : 0 < D := by omega
  have hRpos : 0 < FirstCertificate.Tuned.R D := by
    change 0 < D/4
    omega
  have hSpos : 0 < FirstCertificate.Tuned.S D := by
    change 0 < (D/4)/25
    omega
  have hcap : D ≤ 5*FirstCertificate.Tuned.R D := by
    change D ≤ 5*(D/4)
    omega
  exact normalizedHorizontalGain_lower D _ _
    hDpos hRpos hSpos hcap rfl

/-- An explicit positive buffer over the previously proposed H(D).
No prime-log or baseline error term is hidden in this theorem. -/
theorem production_horizontal_gain_gt_target (D : Nat)
    (hD : (321 : Nat)^4 ≤ D) :
    (4659/625000 : Real)-36167/(1250*(D : Real)) <
      normalizedHorizontalGain
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
  have hl := production_horizontal_gain_lower D hD
  have hDpos : (0 : Real) < D := by
    have hd : 0 < D := by omega
    exact_mod_cast hd
  have hrewrite :
      (36167 : Real)/(1250*(D : Real)) =
        18083500/(625000*(D : Real)) := by
    field_simp [ne_of_gt hDpos]
    <;> ring
  have hden : (0 : Real) < 625000*(D : Real) := by positivity
  have hlt :
      (16895455 : Real)/(625000*(D : Real)) <
        18083500/(625000*(D : Real)) := by
    apply (div_lt_div_iff₀ hden hden).2
    nlinarith only [hden]
  rw [hrewrite]
  linarith

/-- Negative control: the R=D/4, S=R/25 source guards cannot be dropped. -/
theorem missing_dimension_guard_counterexample :
    ¬ (4659*(321 : Nat)^4*1 ≤
        1250*(321 : Nat)^4*
          (1098*floorMass 9 1+1609*floorMass 25 1)+16895455) := by
  norm_num [floorMass]

end TenthDiscriminant.Phase259

#print axioms TenthDiscriminant.Phase259.floorMass_lower
#print axioms TenthDiscriminant.Phase259.horizontalPrimeMass_eq
#print axioms TenthDiscriminant.Phase259.horizontal_mass_certificate
#print axioms TenthDiscriminant.Phase259.production_horizontal_gain_gt_target
#print axioms TenthDiscriminant.Phase259.missing_dimension_guard_counterexample
