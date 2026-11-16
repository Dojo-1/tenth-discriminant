import TenthDiscriminant.Phase331TenPrimeFloor315
import TenthDiscriminant.NormalizedComparison

/-!
Phase331: exact REAL normalization of the ten-prime integer-only
floor certificate. Only the source R=floor(D/4), S=floor(R/25)
relation and positivity of dimensions are needed.

The coefficient 189/100 is the already-verified UNIFORM lower
bound for log p, p in the ten-prime set (Phase323); this theorem
does not yet compare the ten-prime sum to the whole jointOddMass.
No new integer matrix or Hadamard upper is introduced here.
-/
namespace TenthDiscriminant.Phase331
open scoped BigOperators
open TenthDiscriminant.Phase259
open TenthDiscriminant.FirstCertificate
open TenthDiscriminant.Phase323
set_option autoImplicit false

/-- One exact rational normalization of ten selected p^2 horizontal
row weights, with conservative -40/R error. The binary and 3/5
factors do not occur in this inequality. -/
theorem normalized_ten_prime_horizontal_gain
    (R S : Nat) (hR : 0 < R) (hS : 0 < S)
    (hfloor : S = R/25) :
    (873747/250000000 : Real)-40/(R : Real) ≤
      (((2*R*(∑ p ∈ oddHorizontalPrimes,
         floorMass (p*p) S) : Nat) : Real) *
        (189/100 : Real)) / comparisonScale R S := by
  let F := ∑ p ∈ oddHorizontalPrimes, floorMass (p*p) S
  have hn := tenPrimeHorizontalRoundingBudget R S hfloor
  have hnR : (873747 : Real)*R*S ≤
      945000000*(F : Real)+10000000000*S := by
    exact_mod_cast hn
  have hr : (0 : Real) < R := by exact_mod_cast hR
  have hs : (0 : Real) < S := by exact_mod_cast hS
  have hmul := mul_le_mul_of_nonneg_right hnR
    (show (0 : Real) ≤ R by positivity)
  have hp : (0 : Real) < comparisonScale R S :=
    comparisonScale_pos R S hR hS
  apply (le_div_iff₀ hp).2
  have heq :
      ((873747/250000000 : Real)-40/(R : Real))*
          comparisonScale R S =
      ((873747 : Real)*R*S-10000000000*S)*R/250000000 := by
    unfold comparisonScale
    field_simp
    ring
  rw [heq]
  have hreal :
      (((2*R*F : Nat) : Real)*(189/100 : Real)) =
        (945000000 : Real)*R*F/250000000 := by
    push_cast
    ring
  change
    ((873747/250000000 : Real)-40/(R : Real))*
       comparisonScale R S ≤
       (((2*R*F : Nat) : Real)*(189/100 : Real)) at *
  rw [heq, hreal]
  nlinarith only [hmul]

end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.normalized_ten_prime_horizontal_gain
