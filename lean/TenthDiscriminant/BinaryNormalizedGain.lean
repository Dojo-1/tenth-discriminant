import TenthDiscriminant.BinaryNullTraceGram
import TenthDiscriminant.NormalizedComparison
import TenthDiscriminant.LogEnclosure

/-!
# A conservative uniform binary gain for the already certified radius family

The sharp paper coefficient is log(2)/4. To prove the next actual-field
endpoint we need only 1/8 on the *existing* comparisonScale R S=R^2*S.
This file deliberately keeps the simpler robust bound separate from
any unverified four-generator improvement.
-/
namespace TenthDiscriminant
open FirstCertificate
set_option autoImplicit false
noncomputable section

/-- An elementary lower bound on the sum of quotients by four.
The remainder of division by 4 is at most three. -/
theorem fourFloorSum_quadratic_lower (R : Nat) :
    R*R ≤ 8*(∑ r ∈ Finset.range R, r/4) + 7*R := by
  induction R with
  | zero => simp
  | succ R ih =>
      rw [Finset.sum_range_succ]
      have hdiv : R ≤ 4*(R/4)+3 := by omega
      nlinarith

/-- A conservative integer ratio valid already for R>=15:
the binary exponent contributes at least one fifth of R^2*S. -/
theorem binaryNullExponent_fifth_scale (R S : Nat) (hR : 15 ≤ R) :
    R*R*S ≤ 5*binaryNullGramExponent R S := by
  let A := ∑ r ∈ Finset.range R, r/4
  have hfloor : R*R ≤ 8*A+7*R :=
    fourFloorSum_quadratic_lower R
  have hlarge : 15*R ≤ R*R := by nlinarith
  have hscaled := Nat.mul_le_mul_right S hfloor
  have hlargeScaled := Nat.mul_le_mul_right S hlarge
  dsimp [A] at hscaled
  unfold binaryNullGramExponent
  nlinarith

/-- The new binary contribution alone adds at least 1/8 to the
normalized lower bound, with a finite explicit row-count guard.
The stronger exact asymptotic coefficient remains separate. -/
theorem binaryNull_normalized_gain_eighth
    (R S : Nat) (hR : 15 ≤ R) (hS : 0 < S) :
    (1/8 : Real) ≤
      (binaryNullGramExponent R S : Real)*Real.log 2 /
        comparisonScale R S := by
  have hp := comparisonScale_pos R S (by omega) hS
  have hfive := binaryNullExponent_fifth_scale R S hR
  have hreal : comparisonScale R S ≤
      5*(binaryNullGramExponent R S : Real) := by
    have hcast : (R : Real)*R*S ≤
        5*(binaryNullGramExponent R S : Real) := by
      exact_mod_cast hfive
    simpa only [comparisonScale, pow_two] using hcast
  have hlog := log_two_rational_control.1
  have hnonneg : (0 : Real) ≤ binaryNullGramExponent R S := by positivity
  have hmul := mul_nonneg hnonneg (sub_nonneg.mpr hlog)
  have hbound : (1/8 : Real)*comparisonScale R S ≤
      (binaryNullGramExponent R S : Real)*Real.log 2 := by
    nlinarith
  exact (le_div_iff₀ hp).mpr hbound

/-- The arithmetic gain is nonzero at the smallest production pilot. -/
theorem binaryNull_fifth_control :
    30*30*5 ≤ 5*binaryNullGramExponent 30 5 := by decide

end
end TenthDiscriminant
