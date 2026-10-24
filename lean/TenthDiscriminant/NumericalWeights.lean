import TenthDiscriminant.PrimeMassLower

/-!
# Efficient finite weights for numerical certificates

The global staircase inequality is a lower bound even after saturation;
the exact polynomial identity requires the stronger quotient guard.
-/

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

theorem sum_min_ge_polynomial (S k : Nat) :
    ((S : Real) - 1 / 2) * k - (k : Real) ^ 2 / 2 ≤
      ((∑ t ∈ Finset.range S, min k t : Nat) : Real) := by
  by_cases hk : k ≤ S
  · have h := sum_min_identity S k hk
    have hr : 2 * ((∑ t ∈ Finset.range S, min k t : Nat) : Real) +
        (k : Real) * (k + 1) = 2 * S * k := by exact_mod_cast h
    nlinarith
  · have heq : (∑ t ∈ Finset.range S, min k t) = ∑ t ∈ Finset.range S, t := by
      apply Finset.sum_congr rfl
      intro t ht
      exact min_eq_right (by have h := Finset.mem_range.mp ht; omega)
    have hnat : 2 * (∑ t ∈ Finset.range S, t) + S = S ^ 2 := by
      have h := Finset.sum_range_id_mul_two S
      cases S with
      | zero => simp
      | succ s => simp only [Nat.succ_sub_one] at h; nlinarith
    have hr : 2 * ((∑ t ∈ Finset.range S, t : Nat) : Real) + S = (S : Real) ^ 2 := by
      exact_mod_cast hnat
    have hks : (S : Real) ≤ k := by exact_mod_cast (by omega : S ≤ k)
    have hprod := mul_nonneg (sub_nonneg.mpr hks)
      (show (0 : Real) ≤ (k : Real) - S + 1 by linarith)
    rw [heq]
    nlinarith

theorem valuationWeight_ge_polynomial (R S p : Nat) :
    ((S : Real) - 1 / 2) * floorSum R p - (floorSquareSum R p : Real) / 2 ≤
      (valuationWeight R S p : Real) := by
  have hrows : (∑ r ∈ Finset.range R,
      (((S : Real) - 1 / 2) * ((r / p : Nat) : Real) - ((r / p : Nat) : Real) ^ 2 / 2)) ≤
      ∑ r ∈ Finset.range R, ((∑ t ∈ Finset.range S, min (r / p) t : Nat) : Real) :=
    Finset.sum_le_sum (fun r hr => sum_min_ge_polynomial S (r / p))
  simpa only [valuationWeight, floorSum, floorSquareSum, Nat.cast_sum,
    Nat.cast_pow, Finset.sum_sub_distrib, Finset.sum_div, ← Finset.mul_sum] using hrows

theorem valuationWeight_ge_floor_bound (R S p : Nat) :
    ((S : Real) - 1 / 2) * floorSum R p - squareMass R / (2 * (p : Real) ^ 2) ≤
      (valuationWeight R S p : Real) := by
  have h := valuationWeight_ge_polynomial R S p
  have hq := floorSquareSum_le_squareMass_div R p
  have hdiv : squareMass R / (2 * (p : Real) ^ 2) = (squareMass R / (p : Real) ^ 2) / 2 := by
    ring
  rw [hdiv]
  linarith

def floorSumClosed (R q : Nat) : Nat := q * (R / q) * (R / q - 1) / 2 + (R / q) * (R % q)

def checkValuationLower (R S p w : Nat) : Bool :=
  decide (w = 0 ∨ (w : Rat) ≤ ((S : Rat) - 1 / 2) * floorSumClosed R p -
    ((R * (R - 1) * (2 * R - 1) / 6 : Nat) : Rat) / (2 * (p : Rat) ^ 2))

theorem checkValuationLower_sound (R S p w : Nat)
    (hc : checkValuationLower R S p w = true) : (w : Real) ≤ valuationWeight R S p := by
  have h := of_decide_eq_true hc
  rcases h with hz | hw
  · subst w
    exact_mod_cast Nat.zero_le (valuationWeight R S p)
  · have hr : (w : Real) ≤ ((S : Real) - 1 / 2) * floorSum R p -
        squareMass R / (2 * (p : Real) ^ 2) := by
      rw [squareMass_eq_production, floorSum_closed]
      change (w : Real) ≤ ((S : Real) - 1 / 2) * floorSumClosed R p -
        ((R * (R - 1) * (2 * R - 1) / 6 : Nat) : Real) / (2 * (p : Real) ^ 2)
      have hcast : ((w : Rat) : Real) ≤
          ((((S : Rat) - 1 / 2) * (floorSumClosed R p : Rat) -
            ((R * (R - 1) * (2 * R - 1) / 6 : Nat) : Rat) /
              (2 * (p : Rat) ^ 2) : Rat) : Real) := by exact_mod_cast hw
      push_cast at hcast
      exact hcast
    exact hr.trans (valuationWeight_ge_floor_bound R S p)

def checkIntegerValuationLower (R S p w : Nat) : Bool := decide (
  w = 0 ∨ 2 * p ^ 2 * w + R * (R - 1) * (2 * R - 1) / 6 ≤
    (2 * S - 1) * floorSumClosed R p * p ^ 2)

theorem checkIntegerValuationLower_sound (R S p w : Nat) (hS : 1 ≤ S) (hp : 0 < p)
    (hc : checkIntegerValuationLower R S p w = true) : (w : Real) ≤ valuationWeight R S p := by
  rcases of_decide_eq_true hc with hz | hw
  · subst w
    exact_mod_cast Nat.zero_le (valuationWeight R S p)
  · have htwo : 1 ≤ 2 * S := by omega
    have hr : ((2 * p ^ 2 * w + R * (R - 1) * (2 * R - 1) / 6 : Nat) : Real) ≤
        (((2 * S - 1) * floorSumClosed R p * p ^ 2 : Nat) : Real) := by exact_mod_cast hw
    push_cast [Nat.cast_sub htwo] at hr
    have hfloor : floorSumClosed R p = floorSum R p := (floorSum_closed R p).symm
    rw [← squareMass_eq_production R, hfloor] at hr
    have hppos : (0 : Real) < p := by exact_mod_cast hp
    have hden : (0 : Real) < 2 * (p : Real) ^ 2 := by positivity
    have hbound : (w : Real) ≤ ((S : Real) - 1 / 2) * floorSum R p -
        squareMass R / (2 * (p : Real) ^ 2) := by
      apply (le_sub_iff_add_le).mpr
      apply (mul_le_mul_right hden).mp
      have hcancel : squareMass R / (2 * (p : Real) ^ 2) * (2 * (p : Real) ^ 2) =
          squareMass R := div_mul_cancel₀ _ (ne_of_gt hden)
      nlinarith
    exact hbound.trans (valuationWeight_ge_floor_bound R S p)

def factorialCoefficient (R p K : Nat) : Nat :=
  ∑ j ∈ Finset.Ico 1 K, floorSumClosed R (p ^ j)

theorem factorialPowerSum_eq_coefficient (R p K : Nat)
    (hKR : K ≤ R) (hp : 1 ≤ p) (hpow : R ≤ p ^ K) :
    factorialPowerSum R p = factorialCoefficient R p K := by
  rw [factorialPowerSum_eq_unfiltered]
  unfold factorialCoefficient
  have hsub : Finset.Ico 1 K ⊆ Finset.Ico 1 R := Finset.Ico_subset_Ico le_rfl hKR
  have heq : (∑ j ∈ Finset.Ico 1 K, floorSum R (p ^ j)) =
      ∑ j ∈ Finset.Ico 1 R, floorSum R (p ^ j) := by
    apply Finset.sum_subset hsub
    intro j hj hjnot
    have hKj : K ≤ j := by
      have hjone := (Finset.mem_Ico.mp hj).1
      by_contra h
      exact hjnot (Finset.mem_Ico.mpr ⟨hjone, by omega⟩)
    exact floorSum_eq_zero_of_le R (p ^ j)
      (hpow.trans (Nat.pow_le_pow_right (by omega : 0 < p) hKj))
  rw [← heq]
  apply Finset.sum_congr rfl
  intro j hj
  exact floorSum_closed R (p ^ j)

theorem first_factorial_coefficient (p : Nat) (hp : 2 ≤ p) :
    factorialPowerSum 175000000000 p = factorialCoefficient 175000000000 p 38 := by
  apply factorialPowerSum_eq_coefficient _ _ _ (by decide) (by omega)
  exact (show 175000000000 ≤ 2 ^ 38 by decide).trans (Nat.pow_le_pow_left hp 38)

theorem saturated_polynomial_not_identity_control :
    (valuationWeight 8 2 2 : Real) ≠
      ((2 : Real) - 1 / 2) * floorSum 8 2 - (floorSquareSum 8 2 : Real) / 2 :=
  weight_without_quotient_guard_false

theorem global_polynomial_lower_control :
    ((2 : Real) - 1 / 2) * floorSum 8 2 - (floorSquareSum 8 2 : Real) / 2 ≤
      (valuationWeight 8 2 2 : Real) := valuationWeight_ge_polynomial 8 2 2

end
end TenthDiscriminant
