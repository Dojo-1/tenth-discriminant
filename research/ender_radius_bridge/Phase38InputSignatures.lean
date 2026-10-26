import TenthDiscriminant

/-! Inspect the actual generic inputs found in the single frozen inventory.
This does not repeat the provenance traversal or change any theorem. -/
#check NumberField.classNumber
#check NumberField.classNumber.eq_1
#check NumberField.classNumber_eq_one_iff
#check NumberField.RingOfIntegers.instFintypeClassGroup
#check NumberField.exists_ideal_in_class_of_norm_le
#check RingOfIntegers.isPrincipalIdealRing_of_abs_discr_lt
#check NumberField.exists_ne_zero_mem_ideal_of_norm_le_mul_sqrt_discr
#check ClassGroup.fintypeOfAdmissibleOfFinite
#check ClassGroup.fintypeOfAdmissibleOfAlgebraic
#check card_classGroup_eq_one_iff
#check IsPrincipalIdealRing.of_surjective
