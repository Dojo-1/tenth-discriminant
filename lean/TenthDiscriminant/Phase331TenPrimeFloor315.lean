import TenthDiscriminant.Phase323OddPrimeProduct
import TenthDiscriminant.Phase323FinitePrimeCertificate
import TenthDiscriminant.Phase259Horizontal321

/-!
Phase331: integer-only floor-mass budget for the TEN new horizontal
odd primes (7,11,13,17,19,23,29,31,37,41).

The arithmetic coefficient 873747/250000000 of the proposed 315^4
scalar gap is recovered using a *finite integer certificate* with
no floating-point approximations and no new prime-distribution law.

This file does not prove the analytic logarithmic lower or field
theorem; its sum-of-floors inequality is the necessary number-theoretic
rounding bridge to the existing original-jet p^2 divisors.
-/
namespace TenthDiscriminant.Phase331
open scoped BigOperators
open TenthDiscriminant.Phase259
open TenthDiscriminant.Phase323
set_option autoImplicit false

def tenPrimeReciprocalWeight (p : Nat) : Nat :=
  if p = 7 then 2040 else
  if p = 11 then 826 else
  if p = 13 then 591 else
  if p = 17 then 346 else
  if p = 19 then 277 else
  if p = 23 then 189 else
  if p = 29 then 118 else
  if p = 31 then 104 else
  if p = 37 then 73 else
  if p = 41 then 59 else 0

/-- Each weight is a floor to denominator 100000. -/
theorem tenPrimeReciprocalWeight_square_le (p : Nat)
    (hp : p ∈ oddHorizontalPrimes) :
    tenPrimeReciprocalWeight p * (p*p) ≤ 100000 := by
  norm_num [oddHorizontalPrimes] at hp
  rcases hp with rfl | rfl | rfl | rfl | rfl |
    rfl | rfl | rfl | rfl | rfl
  all_goals norm_num [tenPrimeReciprocalWeight]

theorem tenPrimeReciprocalWeight_sum :
    (∑ p ∈ oddHorizontalPrimes,
      tenPrimeReciprocalWeight p) = 4623 := by
  norm_num [oddHorizontalPrimes, tenPrimeReciprocalWeight]

/-- Each individual p^2 floor mass, weighted by the exact certified
reciprocal-square numerator, covers a fixed quadratic part. -/
theorem tenPrimeWeightedFloorPoint (p S : Nat)
    (hp : p ∈ oddHorizontalPrimes) :
    tenPrimeReciprocalWeight p * (S*S) ≤
      200000*floorMass (p*p) S + 200000*S := by
  let w := tenPrimeReciprocalWeight p
  let F := floorMass (p*p) S
  have hsq : w*(p*p) ≤ 100000 := by
    exact tenPrimeReciprocalWeight_square_le p hp
  have hF : S*S ≤ 2*(p*p)*F+(2*(p*p)-1)*S := by
    exact floorMass_lower (p*p) S (by
      have h := oddHorizontalPrime_ge_seven p hp
      positivity)
  have hsub : (2*(p*p)-1)*S ≤ 2*(p*p)*S :=
    Nat.mul_le_mul_right S (Nat.sub_le _ _)
  have hsimple : S*S ≤ 2*(p*p)*F+2*(p*p)*S :=
    hF.trans (add_le_add_left hsub _)
  have hweightF := Nat.mul_le_mul_right F hsq
  have hweightS := Nat.mul_le_mul_right S hsq
  calc
    w*(S*S) ≤ w*(2*(p*p)*F+2*(p*p)*S) :=
      Nat.mul_le_mul_left w hsimple
    _ = 2*(w*(p*p)*F)+2*(w*(p*p)*S) := by ring
    _ ≤ 2*(100000*F)+2*(100000*S) :=
      add_le_add (Nat.mul_le_mul_left 2 hweightF)
        (Nat.mul_le_mul_left 2 hweightS)
    _ = _ := by ring

/-- The entire selected ten-prime floor mass is covered by ONE
integer inequality; the coefficient 4623 is the exact finite
reciprocal-square certificate, not an asymptotic estimate. -/
theorem tenPrimeFloorMassCore (S : Nat) :
    4623*S*S ≤
      200000*(∑ p ∈ oddHorizontalPrimes,
        floorMass (p*p) S) + 2000000*S := by
  have hsum : (∑ p ∈ oddHorizontalPrimes,
      tenPrimeReciprocalWeight p*(S*S)) ≤
      ∑ p ∈ oddHorizontalPrimes,
        (200000*floorMass (p*p) S+200000*S) :=
    Finset.sum_le_sum
      (fun p hp => tenPrimeWeightedFloorPoint p S hp)
  have hcard : oddHorizontalPrimes.card = 10 := by
    norm_num [oddHorizontalPrimes]
  have hmass :
      (∑ p ∈ oddHorizontalPrimes, tenPrimeReciprocalWeight p)*(S*S) ≤
      200000*(∑ p ∈ oddHorizontalPrimes, floorMass (p*p) S)+
        200000*(oddHorizontalPrimes.card*S) := by
    calc
      _ = ∑ p ∈ oddHorizontalPrimes,
            tenPrimeReciprocalWeight p*(S*S) := by rw [Finset.sum_mul]
      _ ≤ ∑ p ∈ oddHorizontalPrimes,
            (200000*floorMass (p*p) S+200000*S) := hsum
      _ = _ := by
        rw [Finset.sum_add_distrib]
        simp only [← Finset.mul_sum, Finset.sum_const, nsmul_eq_mul]
        ac_rfl
  rw [tenPrimeReciprocalWeight_sum, hcard] at hmass
  nlinarith only [hmass]

/-- With the *actual* S=floor(R/25) the 10-prime gain pays the
rational coefficient 873747 and a conservative rounding budget of
40/R. Written as a polynomial inequality, so no logarithms,
division or floating casts hide in this theorem. -/
theorem tenPrimeHorizontalRoundingBudget (R S : Nat)
    (hS : S = R/25) :
    873747*R*S ≤
      945000000*(∑ p ∈ oddHorizontalPrimes,
        floorMass (p*p) S) + 10000000000*S := by
  have hcore := tenPrimeFloorMassCore S
  have hdiv : R = 25*S+R%25 := by
    rw [hS]
    omega
  have hrem : R%25 < 25 := Nat.mod_lt R (by decide)
  have hR : R ≤ 25*S+24 := by omega
  have hRS := Nat.mul_le_mul_right S hR
  nlinarith only [hcore,hRS]

end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.tenPrimeHorizontalRoundingBudget
