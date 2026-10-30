import TenthDiscriminant.ClassNumberClassification
import TenthDiscriminant.ImaginaryQuadraticRepresentation

/-! Structural interface: transport the existing canonical classification. -/
namespace TenthDiscriminant.FieldClassification
set_option autoImplicit false
noncomputable section

/-- Classification up to rational algebra equivalence, without a supplied generator. -/
theorem field_classNumber_one_iff
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) :
    NumberField.classNumber K=1 ↔
      ∃ d : Nat, 0<d ∧ Squarefree d ∧
        d∈([1,2,3,7,11,19,43,67,163] : List Nat) ∧
        Nonempty (ImaginaryQuadraticField d ≃ₐ[Rat] K) := by
  constructor
  · intro hc
    obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
    letI : Fact (0<d) := ⟨hd⟩
    let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
    have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
    exact ⟨d,hd,hsq,(imaginaryQuadratic_classNumber_one_iff d hsq).mp hcan,⟨e⟩⟩
  · rintro ⟨d,hd,hsq,hmem,⟨e⟩⟩
    letI : Fact (0<d) := ⟨hd⟩
    exact classNumber_one_of_field_equiv (ImaginaryQuadraticField d) K e
      ((imaginaryQuadratic_classNumber_one_iff d hsq).mpr hmem)

/-- Actual signed field discriminants; membership is necessary, not an asserted iff. -/
theorem field_classNumber_one_discriminant_mem
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) (hc : NumberField.classNumber K=1) :
    NumberField.discr K ∈ ([-4,-8,-3,-7,-11,-19,-43,-67,-163] : List Int) := by
  obtain ⟨d,hd,hsq,hmem,⟨e⟩⟩ := (field_classNumber_one_iff K hdegree).mp hc
  letI : Fact (0<d) := ⟨hd⟩
  have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_mem d hsq hcan

end
end TenthDiscriminant.FieldClassification
