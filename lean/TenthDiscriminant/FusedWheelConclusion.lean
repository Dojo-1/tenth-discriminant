import TenthDiscriminant.FusedWheelFieldBridge
import TenthDiscriminant.FusedWheelPilot
import TenthDiscriminant.RemainingPositiveClassNumber

/-! One COMPLETE sampled translate extends the bounded iff. The untested
remaining quotient indices are not supplied by these declarations. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem phase35_first_period_classNumber_ne_one (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hlo : 1000000≤d) (hhi : d<892371480) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  apply phase35_classNumber_ne_one_of_translate 0 phase35_q0_translate d hsq hlo
    (by omega)
  exact Nat.div_eq_of_lt hhi

theorem classNumber_one_iff_below_first_period (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hhi : d<892371480) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 ↔
      d∈([1,2,3,7,11,19,43,67,163] : List Nat) := by
  constructor
  · intro hc
    by_cases hd : d<1000000
    · exact classNumber_one_candidates_below_million d hsq hc hd
    · exact False.elim ((phase35_first_period_classNumber_ne_one d hsq (by omega) hhi) hc)
  · exact known_nine_classNumber_one d

end TenthDiscriminant
