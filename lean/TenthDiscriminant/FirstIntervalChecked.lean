import TenthDiscriminant.FirstIntervalRows
import TenthDiscriminant.FirstIntervalCoverage
import TenthDiscriminant.FirstIntervalTotals
import TenthDiscriminant.FirstIntervalConclusion

/-!
# A checked class-number exclusion on one fixed Ender interval

Every numerical premise is supplied by checked finite certificates.
This is not a global cutoff or a class-number classification.
-/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem first_interval_mass_budgets :
    factorialSmallMass 175000000000 10000 ≤ FirstEnderInterval.smallBudget ∧
      FirstEnderInterval.oddBudget ≤ smallOddValuationMass 175000000000 8750000000 10000 :=
  mass_budgets_of_checked_rows firstRows first_rows_coverage
    (List.all_eq_true.mp first_rows_checked) first_rows_budgets

/-- The conservative separation is exact: the lower side exceeds the upper. -/
theorem first_interval_numeric_bounds :
    (581 * 10 ^ 31 : Real) ≤ FirstEnderInterval.lower ∧
      FirstEnderInterval.upper ≤ (572 * 10 ^ 31 : Real) :=
  ⟨FirstEnderInterval.lower_ge_budget first_interval_mass_budgets.1
      first_interval_mass_budgets.2, FirstEnderInterval.upper_le_budget⟩

theorem first_interval_strict_comparison : FirstEnderInterval.upper < FirstEnderInterval.lower := by
  have h := first_interval_numeric_bounds
  nlinarith

/-- Actual quadratic-field class number; no remaining numerical hypothesis. -/
theorem first_interval_classNumber_ne_one (D : Nat)
    (hlo : 700000000000 ≤ D) (hhi : D ≤ 875000000000)
    [Fact ((D : Int) % 4 = 3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) ≠ 1 :=
  FirstEnderInterval.exclusion_of_strict_comparison first_interval_strict_comparison D hlo hhi hsq

end
end TenthDiscriminant.FirstCertificate
