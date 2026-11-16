import Mathlib

/-!
# Phase323: exact rational 315^4 scalar target

This module intentionally proves only an arithmetic inequality in Q.
It does not assert the binary bi-jet determinant divisor, the extended
prime log-mass bound, source positivity, analytic Hadamard majorant, or
any class-number-one field theorem. Those are separate proof gates.

The coefficient 873747/250000000 is the conservative ten-prime gain
from Phase323FinitePrimeCertificate; the 6931/1000000 term is the
proposed horizontal binary gain. The error -450/R uses the exact
endpoint R=floor(315^4/4). Never infer this extra gain from two
independent binary divisibility statements.
-/
namespace TenthDiscriminant.Phase323
set_option autoImplicit false

def scalarGap315 : Rat :=
    (999997/1000000-4/5)*(230096/10000)
    -57193/10000 +1853/2000 +6931/40000
    +4659/625000 -16895455/(625000*9845600625)
    +6931/1000000 +873747/250000000
    -450/2461400156

theorem endpoint315_floors :
    (315 : Nat)^4 = 9845600625 ∧
    (315 : Nat)^4 / 4 = 2461400156 := by
  norm_num

/-- Exact arithmetic value of the conditional scalar margin; no
floating-point evaluation and no mathematical hypotheses are hidden. -/
theorem scalarGap315_exact :
    scalarGap315 =
      2498202070590058939787/12116981457144348750000000 := by
  norm_num [scalarGap315]

/-- Explicit rational separation target, conditional on transporting
every source estimate to this discriminant domain and same Gram. -/
theorem scalarGap315_gt_one_in_five_thousand :
    (1/5000 : Rat) < scalarGap315 := by
  rw [scalarGap315_exact]
  norm_num

end TenthDiscriminant.Phase323

#print axioms TenthDiscriminant.Phase323.scalarGap315_gt_one_in_five_thousand
