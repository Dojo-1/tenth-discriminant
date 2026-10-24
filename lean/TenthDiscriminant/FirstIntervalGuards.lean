import TenthDiscriminant.PrimeTail

/-!
# Exact guards for the first recorded Ender interval

The integer radius and vertical padding match the fixed production replay.
Rational square bounds and Mathlib's pi bounds prove the guards. The
strict lower/upper numerical comparison is deliberately not assumed true.
-/

namespace TenthDiscriminant.FirstEnderInterval
set_option autoImplicit false
noncomputable section

def sqrtD2Upper : Real := 935414346693485347 / 1000000000000
def sqrtD1Lower : Real := 836660026534075547 / 1000000000000
def sqrtInnerUpper : Real := 49831737936691424231 / 125000000000

theorem sqrt_D2_le : Real.sqrt (875000000000 : Real) ≤ sqrtD2Upper := by
  apply Real.sqrt_le_iff.mpr
  norm_num [sqrtD2Upper]

theorem le_sqrt_D1 : sqrtD1Lower ≤ Real.sqrt (700000000000 : Real) := by
  apply Real.le_sqrt_of_sq_le
  norm_num [sqrtD1Lower]

theorem sqrt_inner_le :
    Real.sqrt ((533750000000 : Real) * Real.sqrt 875000000000 / Real.pi) ≤
      sqrtInnerUpper := by
  apply Real.sqrt_le_iff.mpr
  constructor
  · norm_num [sqrtInnerUpper]
  · apply (div_le_iff₀ Real.pi_pos).mpr
    calc
      _ ≤ (533750000000 : Real) * sqrtD2Upper :=
        mul_le_mul_of_nonneg_left sqrt_D2_le (by norm_num)
      _ ≤ sqrtInnerUpper ^ 2 * (3.14159265358979323846 : Real) := by
        norm_num [sqrtD2Upper, sqrtInnerUpper]
      _ ≤ _ := mul_le_mul_of_nonneg_left Real.pi_gt_d20.le (sq_nonneg _)

theorem radius_guard :
    (1001 / 1000 : Real) *
      Real.sqrt (((3 * 175000000000 + 8750000000 : Nat) : Real) *
        Real.sqrt (875000000000 : Nat) / Real.pi) +
      10 * Real.sqrt (875000000000 : Nat) ≤ (408406701 : Nat) := by
  have hi := mul_le_mul_of_nonneg_left sqrt_inner_le (by norm_num : (0 : Real) ≤ 1001 / 1000)
  have hd := mul_le_mul_of_nonneg_left sqrt_D2_le (by norm_num : (0 : Real) ≤ 10)
  have hrat : (1001 / 1000 : Real) * sqrtInnerUpper + 10 * sqrtD2Upper ≤ 408406701 := by
    norm_num [sqrtInnerUpper, sqrtD2Upper]
  norm_num only [Nat.reduceMul, Nat.reduceAdd, Nat.cast_ofNat] at *
  linarith

theorem padding_guard : ellipseVerticalBound 700000000000 408406701 ≤ 488 := by
  have hratio : (408406701 : Real) / Real.sqrt 700000000000 < 489 := by
    apply (div_lt_iff₀ (Real.sqrt_pos.mpr (by norm_num : (0 : Real) < 700000000000))).mpr
    calc
      _ < (489 : Real) * sqrtD1Lower := by norm_num [sqrtD1Lower]
      _ ≤ (489 : Real) * Real.sqrt 700000000000 :=
        mul_le_mul_of_nonneg_left le_sqrt_D1 (by norm_num)
  apply ellipseVerticalBound_le_of_ratio_lt
  norm_num
  exact hratio

def lower : Real := enderPrimeMassLower 175000000000 8750000000 10000 (enderTailIntegral 10000)
def upper : Real :=
  enderUpperB 175000000000 8750000000 8750000000 408406701
    (ellipsePaddedUpperCount 700000000000 408406701 488)

/-- All arithmetic, radius and count guards for this interval are supplied.
The remaining numerical task is to prove `upper<lower`, not to replay Arb. -/
theorem comparison_of_classNumber_one (D : Nat)
    (hlo : 700000000000 ≤ D) (hhi : D ≤ 875000000000)
    [Fact ((D : Int) % 4 = 3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) = 1) :
    lower ≤ upper := by
  have hcut : (175000000000 : Int) < ((D : Int) + 1) / 4 := by
    have hmod : (D : Int) % 4 = 3 := Fact.out
    have hDlo : (700000000000 : Int) ≤ D := by exact_mod_cast hlo
    omega
  exact ellipse_enderPrimeMassLower_le_counted_upperB
    700000000000 D 875000000000 408406701 175000000000 8750000000 488 10000
    (by decide) hlo hhi (by decide) (by decide) (by decide) (by decide)
    hsq hclass hcut (by decide) padding_guard radius_guard

theorem exclusion_of_strict_comparison (hgap : upper < lower) (D : Nat)
    (hlo : 700000000000 ≤ D) (hhi : D ≤ 875000000000)
    [Fact ((D : Int) % 4 = 3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) ≠ 1 := by
  intro hclass
  exact (not_lt_of_ge (comparison_of_classNumber_one D hlo hhi hsq hclass)) hgap

theorem invalid_sqrt_upper_false : ¬ Real.sqrt (875000000000 : Real) ≤ 935414 := by
  rw [Real.sqrt_le_iff]
  norm_num

end
end TenthDiscriminant.FirstEnderInterval
