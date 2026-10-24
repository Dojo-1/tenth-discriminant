import TenthDiscriminant.FirstIntervalScalars
import TenthDiscriminant.NumericalCertificate

/-! Sound conclusion from complete, checked prime-table evidence.
This module does not assume that any generated table passes its checks. -/

namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem strict_comparison_of_checked_rows (rows : List Row)
    (hcover : rows.map Row.p = primeList) (hrows : ∀ r ∈ rows, checkRow r = true)
    (hbudgets : (rows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧
      7995 * 10 ^ 29 * scale ≤ (rows.map (fun r => r.weight * r.lo)).sum) :
    FirstEnderInterval.upper < FirstEnderInterval.lower := by
  have hm := table_mass_bounds rows hcover hrows
  have hscale : (0 : Real) < (scale : Real) := by norm_num [scale]
  have hsmall : (((rows.map (fun r => r.coefficient * r.hi)).sum : Nat) : Real) / scale ≤
      FirstEnderInterval.smallBudget := by
    apply (div_le_iff₀ hscale).mpr
    unfold FirstEnderInterval.smallBudget
    exact_mod_cast hbudgets.1
  have hodd : FirstEnderInterval.oddBudget ≤
      (((rows.map (fun r => r.weight * r.lo)).sum : Nat) : Real) / scale := by
    apply (le_div_iff₀ hscale).mpr
    unfold FirstEnderInterval.oddBudget
    exact_mod_cast hbudgets.2
  exact FirstEnderInterval.strict_comparison_of_table_budgets (hm.1.trans hsmall) (hodd.trans hm.2)

theorem exclusion_of_checked_rows (rows : List Row)
    (hcover : rows.map Row.p = primeList) (hrows : ∀ r ∈ rows, checkRow r = true)
    (hbudgets : (rows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧
      7995 * 10 ^ 29 * scale ≤ (rows.map (fun r => r.weight * r.lo)).sum)
    (D : Nat) (hlo : 700000000000 ≤ D) (hhi : D ≤ 875000000000)
    [Fact ((D : Int) % 4 = 3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) ≠ 1 :=
  FirstEnderInterval.exclusion_of_strict_comparison
    (strict_comparison_of_checked_rows rows hcover hrows hbudgets) D hlo hhi hsq

end
end TenthDiscriminant.FirstCertificate
