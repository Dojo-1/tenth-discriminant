import TenthDiscriminant.QuotientFiberField
import TenthDiscriminant.RemainingPositiveClassNumber

/-! Exact last-gap interface. The all-fiber certificate is an EXPLICIT
premise here; no global classification is asserted without supplying it. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem quotient_classNumber_one_iff_of_all_fibers
    (hcert : phase35Seeds.all phase36Seed=true)
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 ↔
      d∈([1,2,3,7,11,19,43,67,163] : List Nat) := by
  constructor
  · intro hc
    by_cases hd : d<1000000
    · exact classNumber_one_candidates_below_million d hsq hc hd
    · have hhi := imaginaryQuadratic_classNumber_one_radicand_bound d hsq hc
      exact False.elim ((quotient_classNumber_ne_one_of_all_fibers hcert d hsq (by omega) hhi) hc)
  · exact known_nine_classNumber_one d

end TenthDiscriminant
