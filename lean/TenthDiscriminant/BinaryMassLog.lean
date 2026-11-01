import TenthDiscriminant.BinaryNormalizedGain
import TenthDiscriminant.RadialCutoff

/-!
# Logarithmic binary + odd-prime mass on the SAME integer Gram

The source detector is the original ordinary-jet Gram, not the field
discriminant. The binary and odd-prime divisors are coprime. Positivity
of the actual determinant is a separate premise, provided in production
by the already checked geometry/interpolation argument.
-/
namespace TenthDiscriminant
open FirstCertificate
set_option autoImplicit false
noncomputable section

/-- The class-number-one original Gram enjoys the old odd-prime mass
PLUS the new *independently certified* binary determinant mass.
This is exactly the finite integer product, with no real approximation. -/
theorem binaryOddMass_log_le_of_det_pos
    (Q : Finset (Int × Int)) (D R S : Nat)
    (hdet : 0 < (integerRectangularTraceGram Q D S R S).det)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4))=1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    exactOddPrimeMass R S +
      (binaryNullGramExponent R S : Real)*Real.log 2 ≤
        Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  classical
  let P := oddPrimesBelow R
  let k := binaryNullGramExponent R S
  let z := (integerRectangularTraceGram Q D S R S).det
  have hz : 0 < z := hdet
  have hdiv :
      ((2^k * ∏ p ∈ P, p^(2*valuationWeight R S p) : Nat) : Int) ∣ z := by
    simpa only [P,k,z] using
      originalGram_binary_oddMass_unconditional Q D R S hsq hclass hRcut
  have hnat :
      2^k * ∏ p ∈ P, p^(2*valuationWeight R S p) ≤ z.natAbs := by
    simpa only [Int.natAbs_natCast] using
      Int.natAbs_le_of_dvd_ne_zero hdiv (ne_of_gt hz)
  have hint :
      ((2^k * ∏ p ∈ P, p^(2*valuationWeight R S p) : Nat) : Int) ≤ z := by
    have hcast :
        ((2^k * ∏ p ∈ P, p^(2*valuationWeight R S p) : Nat) : Int) ≤
          (z.natAbs : Int) := by
      exact_mod_cast hnat
    simpa only [Int.natCast_natAbs, abs_of_pos hz] using hcast
  have hreal :
      ((2^k * ∏ p ∈ P, p^(2*valuationWeight R S p) : Nat) : Real) ≤ z := by
    exact_mod_cast hint
  have hp_pos (p : Nat) (hp : p ∈ P) : (0 : Real) < p := by
    have hprime : p.Prime := (Finset.mem_filter.mp hp).2.1
    exact_mod_cast hprime.pos
  have hprod_pos : (0 : Real) <
      ∏ p ∈ P, (p : Real)^(2*valuationWeight R S p) := by
    exact Finset.prod_pos fun p hp => pow_pos (hp_pos p hp) _
  have hleft_pos :
      (0 : Real) <
        ((2^k * ∏ p ∈ P, p^(2*valuationWeight R S p) : Nat) : Real) := by
    exact_mod_cast Nat.mul_pos (pow_pos (by decide : (0 : Nat)<2) _)
      (Finset.prod_pos fun p hp =>
        pow_pos ((Finset.mem_filter.mp hp).2.1.pos) _)
  have hodd_log :
      Real.log (∏ p ∈ P, (p : Real)^(2*valuationWeight R S p)) =
        exactOddPrimeMass R S := by
    rw [Real.log_prod]
    · simp_rw [Real.log_pow]
      rfl
    · intro p hp
      exact (pow_pos (hp_pos p hp) _).ne'
  have htotal :
      Real.log ((2^k * ∏ p ∈ P, p^(2*valuationWeight R S p) : Nat) : Real) =
        (k : Real)*Real.log 2 + exactOddPrimeMass R S := by
    simp only [Nat.cast_mul, Nat.cast_pow, Nat.cast_prod]
    rw [Real.log_mul (pow_pos (by norm_num : (0 : Real)<2) _).ne'
      hprod_pos.ne', Real.log_pow, hodd_log]
  have hlog := Real.log_le_log hleft_pos hreal
  rw [htotal] at hlog
  simpa only [k,z,add_comm] using hlog

end
end TenthDiscriminant
