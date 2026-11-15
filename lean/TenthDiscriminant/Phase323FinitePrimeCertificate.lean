import TenthDiscriminant.Phase200Scalar322

/-!
# Phase323-C: exact finite ten-prime horizontal certificate

This module contains only finite rational/logarithm controls. It does
not assume a prime-distribution theorem, an Euler product, or a global
character-sum estimate. The floor-sum transport to the original Gram
is a separate theorem.
-/
namespace TenthDiscriminant.Phase323
set_option autoImplicit false

/-- Ten explicit odd primes used by the horizontal p^2 Frobenius factors. -/
def oddHorizontalPrimes : Finset Nat :=
  {7,11,13,17,19,23,29,31,37,41}

/-- The elementary inequality log(7/5) >= 2/7, obtained from
log(x) <= x-1 at x=5/7 and log(x^-1)=-log(x). -/
theorem log_seven_over_five_lower :
    (2/7 : Real) ≤ Real.log (7/5 : Real) := by
  have h := Real.log_le_sub_one_of_pos
    (by norm_num : (0 : Real) < (5/7 : Real))
  have heq : (5/7 : Real) = (7/5 : Real)⁻¹ := by norm_num
  rw [heq, Real.log_inv] at h
  norm_num at h
  linarith

/-- A deliberately conservative rational lower bound for log 7. -/
theorem log_seven_lower_189 :
    (189/100 : Real) ≤ Real.log 7 := by
  have h5 := TenthDiscriminant.log_five_lower_1609
  have h75 := log_seven_over_five_lower
  have hmul : (5 : Real) * (7/5 : Real) = 7 := by norm_num
  have hlog : Real.log 7 =
      Real.log 5 + Real.log (7/5 : Real) := by
    calc
      Real.log 7 = Real.log ((5 : Real)*(7/5 : Real)) := by rw [hmul]
      _ = Real.log 5 + Real.log (7/5 : Real) :=
        Real.log_mul (by norm_num) (by norm_num)
  norm_num at h5
  linarith

/-- Every selected prime is at least seven. -/
theorem oddHorizontalPrime_ge_seven (p : Nat)
    (hp : p ∈ oddHorizontalPrimes) : 7 ≤ p := by
  norm_num [oddHorizontalPrimes] at hp
  omega

/-- Every selected prime has the same certified logarithm lower bound. -/
theorem oddHorizontalPrime_log_lower (p : Nat)
    (hp : p ∈ oddHorizontalPrimes) :
    (189/100 : Real) ≤ Real.log p := by
  have hp7 := oddHorizontalPrime_ge_seven p hp
  have hpReal : (7 : Real) ≤ (p : Real) := by exact_mod_cast hp7
  have hlog := Real.log_le_log (by norm_num : (0 : Real) < 7) hpReal
  exact log_seven_lower_189.trans hlog

/-- Exact reciprocal-square lower certificate. The ten numerators
2040,826,591,346,277,189,118,104,73,59 all have denominator 100000. -/
theorem reciprocal_square_sum_lower :
    (4623/100000 : Real) ≤
      ∑ p ∈ oddHorizontalPrimes, 1/(p : Real)^2 := by
  norm_num [oddHorizontalPrimes]

/-- Exact sum of the deliberately conservative finite-prime error
coefficients. -/
theorem sum_two_p_minus_one :
    (∑ p ∈ oddHorizontalPrimes, (2*p-1)) = 446 := by
  norm_num [oddHorizontalPrimes]

/-- Rational horizontal coefficient before the finite R-rounding loss. -/
theorem finite_odd_horizontal_gain_lower :
    (873747/250000000 : Real) ≤
      (189/2500 : Real) *
        (∑ p ∈ oddHorizontalPrimes, 1/(p : Real)^2) := by
  have h := reciprocal_square_sum_lower
  norm_num at h ⊢
  nlinarith

end TenthDiscriminant.Phase323

#print axioms TenthDiscriminant.Phase323.finite_odd_horizontal_gain_lower
