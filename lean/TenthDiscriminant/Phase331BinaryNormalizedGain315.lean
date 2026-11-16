import TenthDiscriminant.Phase331JointBinaryOddLog315
import TenthDiscriminant.LogEnclosure

/-!
Phase331: transport the PROVED joint binary row exponent to the
original R^2*S normalization. The estimate has a visible -2/R
rounding loss. No second binary divisor or changed Gram occurs.
-/
namespace TenthDiscriminant.Phase331
open TenthDiscriminant
open TenthDiscriminant.Phase259
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false

/-- Elementary integer floor budget for S=floor(R/25). The underlying
floorMass_lower 4 S is already proved in Phase259, and no
asymptotic floor is silently substituted. -/
theorem horizontal_binary_floor_budget (R S : Nat)
    (hS : S = R/25) :
    R*S ≤ 200*floorMass 4 S+200*S := by
  have hf := floorMass_lower 4 S (by decide)
  norm_num at hf
  have hdiv : R = 25*S+R%25 := by
    rw [hS]
    omega
  have hrem : R%25 < 25 := Nat.mod_lt R (by decide)
  have hR : R ≤ 25*S+24 := by omega
  have hRS := Nat.mul_le_mul_right S hR
  nlinarith only [hf,hRS]

/-- Exact normalized additional vertical-plus-horizontal BINARY row
gain beyond the OLD vertical exponent, including the floor error.
The only analytic input is the existing certified lower log2 bound
and the elementary log2 <= 1. -/
theorem normalized_new_horizontal_binary_gain (R S : Nat)
    (hR : 0 < R) (hS : 0 < S) (hfloor : S = R/25) :
    (6931/1000000 : Real)-2/(R : Real) ≤
      ((2*R*floorMass 4 S : Nat) : Real)*Real.log 2/
        comparisonScale R S := by
  have hr : (0 : Real) < R := by exact_mod_cast hR
  have hs : (0 : Real) < S := by exact_mod_cast hS
  have hNat := horizontal_binary_floor_budget R S hfloor
  have hf : (R : Real)*(S : Real) ≤
      200*(floorMass 4 S : Real)+200*S := by
    exact_mod_cast hNat
  have hratio : (1/100 : Real)-2/(R : Real) ≤
      (2 : Real)*(floorMass 4 S : Real)/(R*S) := by
    apply (le_div_iff₀ (mul_pos hr hs)).2
    calc
      ((1/100 : Real)-2/(R : Real))*(R*S) =
          (R*S)/100-2*S := by
        field_simp
        <;> ring
      _ ≤ 2*(floorMass 4 S : Real) := by linarith [hf]
  have hlo := TenthDiscriminant.log_two_rational_control.1
  have hhi : Real.log (2 : Real) ≤ 1 := by
    have h := Real.log_le_sub_one_of_pos
      (by norm_num : (0 : Real) < 2)
    linarith
  have hp : (0 : Real) ≤ Real.log 2 :=
    Real.log_nonneg (by norm_num)
  have hbase : (6931/1000000 : Real) ≤
      (1/100 : Real)*Real.log 2 := by linarith [hlo]
  have herror : -(2/(R : Real)) ≤
      -(2/(R : Real))*Real.log 2 := by
    have hmul := mul_le_mul_of_nonneg_left hhi
      (show (0 : Real) ≤ 2/(R : Real) by positivity)
    linarith
  have hterm : (6931/1000000 : Real)-2/(R : Real) ≤
      ((1/100 : Real)-2/(R : Real))*Real.log 2 := by
    nlinarith only [hbase,herror]
  calc
    _ ≤ ((1/100 : Real)-2/(R : Real))*Real.log 2 := hterm
    _ ≤ ((2 : Real)*(floorMass 4 S : Real)/(R*S))*Real.log 2 :=
      mul_le_mul_of_nonneg_right hratio hp
    _ = ((2*R*floorMass 4 S : Nat) : Real)*Real.log 2/
        comparisonScale R S := by
          unfold comparisonScale
          push_cast
          field_simp
          ring

end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.normalized_new_horizontal_binary_gain
