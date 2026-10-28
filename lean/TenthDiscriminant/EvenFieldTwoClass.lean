import TenthDiscriminant.EvenTwoClass
import TenthDiscriminant.OddFieldTwoClass
import TenthDiscriminant.AxiomAudit

/-! The field is arbitrary; its quadratic chart is constructed inside the proof. -/
open scoped NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.EvenFieldTwoClass
set_option autoImplicit false
noncomputable section

theorem even_chart_of_even_parameter (d : Nat) (hsq : Squarefree d)
    (heven : Even (absoluteDiscriminantParameter d)) :
    (d : Int)%4=1 ∨ (d : Int)%4=2 := by
  rcases squarefree_mod_four_cases d hsq with hodd | hchart
  · have hd : Even d := by simpa only [absoluteDiscriminantParameter,if_pos hodd] using heven
    obtain ⟨k,hk⟩ := hd
    omega
  · exact hchart

theorem arbitrary_even_discriminant_bound (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K≤2) (heven : Even (NumberField.discr K).natAbs) :
    (NumberField.discr K).natAbs<2^52 := by
  obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hdisc : (NumberField.discr K).natAbs=absoluteDiscriminantParameter d := by
    rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
    exact imaginaryQuadratic_discr_natAbs d hsq
  have hm := even_chart_of_even_parameter d hsq (hdisc ▸ heven)
  have he := OddFieldTwoClass.field_classNumber_eq (ImaginaryQuadraticField d) K e
  have hcan : NumberField.classNumber (ImaginaryQuadraticField d)≤2 := by
    rw [he]
    exact hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  have hb := EvenTwoClass.even_discriminant_bound d hsq hm hcan
  simpa only [show 4*(2 : Nat)^50=2^52 by norm_num] using hb

theorem arbitrary_discriminant_bound (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K≤2) : (NumberField.discr K).natAbs<2^52 := by
  rcases Nat.even_or_odd (NumberField.discr K).natAbs with heven | hodd
  · exact arbitrary_even_discriminant_bound K hdegree hc heven
  · exact lt_trans (OddFieldTwoClass.arbitrary_odd_discriminant_bound K hdegree hc hodd)
      (by norm_num : (2 : Nat)^50<2^52)

theorem parity_refined_discriminant_bound (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K≤2) :
    (Odd (NumberField.discr K).natAbs → (NumberField.discr K).natAbs<2^50) ∧
    (Even (NumberField.discr K).natAbs → (NumberField.discr K).natAbs<2^52) := by
  exact ⟨fun hodd => OddFieldTwoClass.arbitrary_odd_discriminant_bound K hdegree hc hodd,
    fun heven => arbitrary_even_discriminant_bound K hdegree hc heven⟩

theorem classNumber_gt_two_of_large_discriminant (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hlarge : 2^52≤(NumberField.discr K).natAbs) : 2<NumberField.classNumber K := by
  by_contra hn
  have hc : NumberField.classNumber K≤2 := Nat.le_of_not_gt hn
  have hb := arbitrary_discriminant_bound K hdegree hc
  omega

theorem even_parameter_control : absoluteDiscriminantParameter 2=8 := by
  norm_num [absoluteDiscriminantParameter]

theorem odd_parameter_control : absoluteDiscriminantParameter 3=3 := by
  norm_num [absoluteDiscriminantParameter]

theorem factor_four_control : 4*(2 : Nat)^50=2^52 ∧ 4*(2 : Nat)^50≠2^50 := by
  norm_num

theorem odd_chart_exclusion_control : ¬ ((3 : Int)%4=1 ∨ (3 : Int)%4=2) := by
  decide
end
end TenthDiscriminant.EvenFieldTwoClass

#check TenthDiscriminant.EvenFieldTwoClass.even_chart_of_even_parameter
#check TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound
#check TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound
#check TenthDiscriminant.EvenFieldTwoClass.parity_refined_discriminant_bound
#check TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant
#check TenthDiscriminant.EvenFieldTwoClass.even_parameter_control
#check TenthDiscriminant.EvenFieldTwoClass.odd_parameter_control
#check TenthDiscriminant.EvenFieldTwoClass.factor_four_control
#check TenthDiscriminant.EvenFieldTwoClass.odd_chart_exclusion_control
#print axioms TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound
#print axioms TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound
#print axioms TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant
#audit_namespace TenthDiscriminant.EvenFieldTwoClass

