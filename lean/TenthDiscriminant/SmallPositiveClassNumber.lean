import TenthDiscriminant.QuadraticDiscriminant
import Mathlib.NumberTheory.NumberField.ClassNumber
import Mathlib.Data.Real.Pi.Bounds

/-! Positive class-number statements, distinct from passing a necessary sieve.
Minkowski's existing small-discriminant criterion supplies the ideal argument. -/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

theorem quadratic_classNumber_one_of_discr_le_eight (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2) (habs : (NumberField.discr K).natAbs≤8) :
    NumberField.classNumber K=1 := by
  have hrank := NumberField.InfinitePlace.card_add_two_mul_card_eq_rank K
  rw [hdegree] at hrank
  have hcases : NumberField.InfinitePlace.nrComplexPlaces K=0 ∨
      NumberField.InfinitePlace.nrComplexPlaces K=1 := by omega
  have hi : ((NumberField.discr K).natAbs : Int)≤(8 : Int) := by exact_mod_cast habs
  rw [Int.natCast_natAbs] at hi
  have hreal : ((|NumberField.discr K| : Int) : Real)≤8 := by exact_mod_cast hi
  rw [Int.cast_abs] at hreal
  apply NumberField.classNumber_eq_one_iff.mpr
  apply RingOfIntegers.isPrincipalIdealRing_of_abs_discr_lt
  rcases hcases with h | h
  · norm_num [hdegree,h]
    linarith
  · norm_num [hdegree,h]
    nlinarith [Real.pi_gt_three]

theorem imaginaryQuadratic_finrank (d : Nat) [Fact (0 < d)] :
    Module.finrank Rat (ImaginaryQuadraticField d)=2 := by
  simpa using Module.finrank_eq_card_basis (evenFieldBasis d)

theorem imaginaryQuadratic_classNumber_one_of_parameter_le_eight (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hsmall : absoluteDiscriminantParameter d≤8) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 := by
  apply quadratic_classNumber_one_of_discr_le_eight _ (imaginaryQuadratic_finrank d)
  simpa only [imaginaryQuadratic_discr_natAbs d hsq] using hsmall

private instance positiveOneFact : Fact (0 < (1 : Nat)) := ⟨by decide⟩
private instance positiveTwoFact : Fact (0 < (2 : Nat)) := ⟨by decide⟩
private instance positiveThreeFact : Fact (0 < (3 : Nat)) := ⟨by decide⟩
private instance positiveSevenFact : Fact (0 < (7 : Nat)) := ⟨by decide⟩
private instance positiveElevenFact : Fact (0 < (11 : Nat)) := ⟨by decide⟩

theorem one_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 1)=1 :=
  imaginaryQuadratic_classNumber_one_of_parameter_le_eight 1 (by simp)
    (by norm_num [absoluteDiscriminantParameter])

theorem two_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 2)=1 :=
  imaginaryQuadratic_classNumber_one_of_parameter_le_eight 2 Nat.prime_two.squarefree
    (by norm_num [absoluteDiscriminantParameter])

theorem three_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 3)=1 :=
  imaginaryQuadratic_classNumber_one_of_parameter_le_eight 3
    (by norm_num : Nat.Prime 3).squarefree (by norm_num [absoluteDiscriminantParameter])

theorem seven_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 7)=1 :=
  imaginaryQuadratic_classNumber_one_of_parameter_le_eight 7
    (by norm_num : Nat.Prime 7).squarefree (by norm_num [absoluteDiscriminantParameter])

theorem small_positive_discriminant_controls :
    (NumberField.discr (ImaginaryQuadraticField 1)).natAbs=4 ∧
    (NumberField.discr (ImaginaryQuadraticField 2)).natAbs=8 ∧
    (NumberField.discr (ImaginaryQuadraticField 3)).natAbs=3 ∧
    (NumberField.discr (ImaginaryQuadraticField 7)).natAbs=7 := by
  rw [imaginaryQuadratic_discr_natAbs 1 (by simp),
    imaginaryQuadratic_discr_natAbs 2 Nat.prime_two.squarefree,
    imaginaryQuadratic_discr_natAbs 3 (by norm_num : Nat.Prime 3).squarefree,
    imaginaryQuadratic_discr_natAbs 7 (by norm_num : Nat.Prime 7).squarefree]
  norm_num [absoluteDiscriminantParameter]

/-- Order discriminant and field discriminant differ even for squarefree d.
The trace-zero order at d=3 is not the maximal order. -/
theorem three_order_field_discriminant_control :
    Algebra.discr Int (evenOrderBasis 3)= -12 ∧
    NumberField.discr (ImaginaryQuadraticField 3)= -3 := by
  rw [evenOrder_basis_discr, imaginaryQuadratic_discr 3 (by norm_num : Nat.Prime 3).squarefree]
  norm_num

/-- Outside this sufficient criterion, not a negative class-number claim. -/
theorem eleven_outside_small_criterion_control :
    8 < (NumberField.discr (ImaginaryQuadraticField 11)).natAbs := by
  rw [imaginaryQuadratic_discr_natAbs 11 (by norm_num : Nat.Prime 11).squarefree]
  norm_num [absoluteDiscriminantParameter]

end
end TenthDiscriminant
