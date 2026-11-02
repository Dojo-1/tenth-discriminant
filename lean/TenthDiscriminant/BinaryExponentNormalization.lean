import TenthDiscriminant.BinaryThinGramBridge
import TenthDiscriminant.FloorSum

/-!
# Phase165 — exact, representation-independent binary exponent normalization

Human claim: for every natural R,S, if t=R mod 4, then
  4 * Lambda1(R,S) = S * (R^2 + t*(4-t)).
In particular S*R^2 <= 4*Lambda1; the normalized 2-adic contribution
is at least (log 2)/4 whenever R and S are positive.

This file is algebra about the ALREADY source-checked univariate
Gram exponent. It introduces no new derivative, node, weight or field
assumption. It is NOT a new field-discriminant theorem.
-/

namespace TenthDiscriminant
set_option autoImplicit false

/-- Exact closed expression for the existing exponent. The remainder
t = R % 4 is kept visible instead of silently bounding it away. -/
theorem binaryNullGramExponent_four_scaled (R S : Nat) :
    4 * binaryNullGramExponent R S =
      S * (R^2 + (R%4)*(4 - R%4)) := by
  have hF := floorSum_scaled R 4
  have hr : R = 4*(R/4) + R%4 := by omega
  have hrem : R%4 <= 4 := by omega
  have htail : (R%4)*(4-R%4)+(R%4)^2 = 4*(R%4) := by
    calc
      (R%4)*(4-R%4)+(R%4)^2 =
          (R%4)*((4-R%4)+(R%4)) := by ring
      _ = (R%4)*4 := by rw [Nat.sub_add_cancel hrem]
      _ = 4*(R%4) := by ring
  have hpolynomial :
      4*(4*(R/4)+R%4)+8*floorSum R 4 =
        (4*(R/4)+R%4)^2+(R%4)*(4-R%4) := by
    nlinarith [hF, htail]
  have hbase : 4*R+8*floorSum R 4 =
      R^2 + (R%4)*(4-R%4) := by
    have hr4 : 4*R = 4*(4*(R/4)+R%4) :=
      congrArg (fun n : Nat => 4*n) hr
    calc
      4*R+8*floorSum R 4 =
          4*(4*(R/4)+R%4)+8*floorSum R 4 := by rw [hr4]
      _ = (4*(R/4)+R%4)^2+(R%4)*(4-R%4) := hpolynomial
      _ = R^2+(R%4)*(4-R%4) := by rw [← hr]
  calc
    4*binaryNullGramExponent R S =
        S*(4*R+8*floorSum R 4) := by
          dsimp [binaryNullGramExponent, floorSum]
          ring
    _ = S*(R^2+(R%4)*(4-R%4)) := by rw [hbase]

/-- The exact exponent automatically contains a quarter of R^2*S.
There are NO asymptotic or real-valued approximations in this theorem. -/
theorem binaryNullGramExponent_quarter_lower (R S : Nat) :
    S * R^2 <= 4 * binaryNullGramExponent R S := by
  rw [binaryNullGramExponent_four_scaled]
  exact Nat.mul_le_mul_left S (Nat.le_add_right _ _)

/-- The verified rational/logarithm machinery is reusable; this
inequality merely transports the integer exponent estimate across a
nonnegative multiplication by log 2, without dividing by R^2*S. -/
theorem binaryNullGramExponent_log_two_lower (R S : Nat) :
    ((S*R^2 : Nat) : Real) * Real.log 2 <=
      ((4*binaryNullGramExponent R S : Nat) : Real) * Real.log 2 := by
  have hnat := binaryNullGramExponent_quarter_lower R S
  have hreal : ((S*R^2 : Nat) : Real) <=
      ((4*binaryNullGramExponent R S : Nat) : Real) := by
    exact_mod_cast hnat
  exact mul_le_mul_of_nonneg_right hreal (le_of_lt (Real.log_pos (by norm_num)))

/-- Source-config regression: Lambda1(30,5)=1130, while the remainder
t=2 contributes a positive exact finite correction. -/
theorem binaryNullGramExponent_30_5_scaled_control :
    4*binaryNullGramExponent 30 5 = 5*(30^2+2*(4-2)) := by
  norm_num [binaryNullGramExponent_30_5]

end TenthDiscriminant
