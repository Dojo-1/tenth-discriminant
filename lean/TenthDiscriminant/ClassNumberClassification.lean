import TenthDiscriminant.QuotientFiberClassification
import TenthDiscriminant.QuotientFiberCertified

/-! Class number one for the canonical actual field Q(sqrt(-d)).
No finite-range, sieve-certificate or numerical hypothesis remains.
This does not assert a representation theorem for arbitrary field types. -/
namespace TenthDiscriminant
set_option autoImplicit false

/-- The nine positive squarefree radicands, with both directions proved. -/
theorem imaginaryQuadratic_classNumber_one_iff (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 ↔
      d∈([1,2,3,7,11,19,43,67,163] : List Nat) :=
  quotient_classNumber_one_iff_of_all_fibers phase36_all_fibers d hsq

/-- Necessary signed discriminants, using the actual maximal integer ring. -/
theorem imaginaryQuadratic_classNumber_one_discriminant_mem (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    NumberField.discr (ImaginaryQuadraticField d) ∈
      ([-4,-8,-3,-7,-11,-19,-43,-67,-163] : List Int) := by
  have hd := (imaginaryQuadratic_classNumber_one_iff d hsq).mp hc
  simp only [List.mem_cons,List.not_mem_nil,or_false] at hd
  rcases hd with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    rw [imaginaryQuadratic_discr _ hsq] <;> norm_num

end TenthDiscriminant
