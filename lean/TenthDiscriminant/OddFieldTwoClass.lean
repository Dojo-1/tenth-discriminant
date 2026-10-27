import TenthDiscriminant.UniformTwoClass

/-! Isomorphisms preserve ideal classes, not only the PID case. -/
open scoped NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.OddFieldTwoClass
set_option autoImplicit false
noncomputable section
section Domains
variable {R S : Type*} [CommRing R] [IsDomain R] [IsDedekindDomain R]
  [CommRing S] [IsDomain S] [IsDedekindDomain S]

def idealMap (e : R ≃+* S) (I : (Ideal R)⁰) : (Ideal S)⁰ :=
  ⟨(I : Ideal R).map (e : R →+* S),by
    apply mem_nonZeroDivisors_iff_ne_zero.mpr
    intro hz
    have hz' : (I : Ideal R).map (e : R →+* S)=⊥ := hz
    have hh := (Ideal.map_eq_bot_iff_of_injective (f := (e : R →+* S)) e.injective).mp hz'
    exact (mem_nonZeroDivisors_iff_ne_zero.mp I.prop) hh⟩

theorem idealMap_symm (e : R ≃+* S) (I : (Ideal R)⁰) : idealMap e.symm (idealMap e I)=I := by
  apply Subtype.ext
  exact Ideal.map_of_equiv e

theorem class_relation_map (e : R ≃+* S) {I J : (Ideal R)⁰}
    (h : ClassGroup.mk0 I=ClassGroup.mk0 J) :
    ClassGroup.mk0 (idealMap e I)=ClassGroup.mk0 (idealMap e J) := by
  obtain ⟨x,y,hx,hy,hIJ⟩ := ClassGroup.mk0_eq_mk0_iff.mp h
  apply ClassGroup.mk0_eq_mk0_iff.mpr
  refine ⟨e x,e y,?_,?_,?_⟩
  · intro hh
    apply hx
    apply e.injective
    simpa only [map_zero] using hh
  · intro hh
    apply hy
    apply e.injective
    simpa only [map_zero] using hh
  · have hm := congrArg (Ideal.map (e : R →+* S)) hIJ
    change Ideal.span {e x}*(I : Ideal R).map (e : R →+* S)=
      Ideal.span {e y}*(J : Ideal R).map (e : R →+* S)
    simpa only [Ideal.map_mul,Ideal.map_span,Set.image_singleton] using hm

def classMap (e : R ≃+* S) (C : ClassGroup R) : ClassGroup S :=
  ClassGroup.mk0 (idealMap e (Function.surjInv (ClassGroup.mk0_surjective (R := R)) C))

theorem classMap_mk0 (e : R ≃+* S) (I : (Ideal R)⁰) :
    classMap e (ClassGroup.mk0 I)=ClassGroup.mk0 (idealMap e I) := by
  unfold classMap
  exact class_relation_map e (Function.surjInv_eq (ClassGroup.mk0_surjective (R := R)) (ClassGroup.mk0 I))

theorem classMap_inverse (e : R ≃+* S) (C : ClassGroup R) : classMap e.symm (classMap e C)=C := by
  obtain ⟨I,rfl⟩ := ClassGroup.mk0_surjective C
  rw [classMap_mk0,classMap_mk0,idealMap_symm]

def classEquiv (e : R ≃+* S) : ClassGroup R ≃ ClassGroup S where
  toFun := classMap e
  invFun := classMap e.symm
  left_inv := classMap_inverse e
  right_inv C := by simpa only [RingEquiv.symm_symm] using classMap_inverse e.symm C

theorem identity_class_control (C : ClassGroup R) : classMap (RingEquiv.refl R) C=C := by
  obtain ⟨I,rfl⟩ := ClassGroup.mk0_surjective C
  rw [classMap_mk0]
  have hid : idealMap (RingEquiv.refl R) I=I := by
    apply Subtype.ext
    change (I : Ideal R).map (RingHom.id R)=(I : Ideal R)
    exact (I : Ideal R).map_id
  exact congrArg (fun J : (Ideal R)⁰ => ClassGroup.mk0 J) hid
end Domains

theorem field_classNumber_eq (K L : Type*) [Field K] [Field L]
    [NumberField K] [NumberField L] (e : K ≃ₐ[Rat] L) :
    NumberField.classNumber K=NumberField.classNumber L := by
  let f : NumberField.RingOfIntegers K ≃+* NumberField.RingOfIntegers L :=
    (e.restrictScalars Int).mapIntegralClosure.toRingEquiv
  exact Fintype.card_congr (classEquiv f)

theorem canonical_odd_discriminant_bound (d : Nat) [Fact (0<d)] [Fact ((d : Int)%4=3)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)≤2) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs<2^50 := by
  have he := field_classNumber_eq (ImaginaryQuadraticField d)
    (QuadraticField (((d : Int)+1)/4)) (quadraticChartEquiv d)
  have hchart : NumberField.classNumber (QuadraticField (((d : Int)+1)/4))≤2 := by
    rw [←he]
    exact hc
  have hd : d<2^50 := by
    by_contra hn
    have hg := UniformTwoClass.odd_classNumber_gt_two d (by omega) hsq
    omega
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  simpa only [absoluteDiscriminantParameter,if_pos (Fact.out : (d : Int)%4=3)] using hd

theorem arbitrary_odd_discriminant_bound (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K≤2) (hodd : Odd (NumberField.discr K).natAbs) :
    (NumberField.discr K).natAbs<2^50 := by
  obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hdisc : (NumberField.discr K).natAbs=absoluteDiscriminantParameter d := by
    rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
    exact imaginaryQuadratic_discr_natAbs d hsq
  have hmod : (d : Int)%4=3 := by
    by_contra hnot
    have heven : (NumberField.discr K).natAbs=4*d := by
      rw [hdisc]
      simp only [absoluteDiscriminantParameter,if_neg hnot]
    obtain ⟨j,hj⟩ := hodd
    rw [heven] at hj
    omega
  letI : Fact ((d : Int)%4=3) := ⟨hmod⟩
  have he := field_classNumber_eq (ImaginaryQuadraticField d) K e
  have hcan : NumberField.classNumber (ImaginaryQuadraticField d)≤2 := by
    rw [he]
    exact hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact canonical_odd_discriminant_bound d hsq hcan

theorem class_one_control (K L : Type*) [Field K] [Field L] [NumberField K] [NumberField L]
    (e : K ≃ₐ[Rat] L) (hc : NumberField.classNumber K=1) : NumberField.classNumber L=1 := by
  rw [←field_classNumber_eq K L e]
  exact hc

theorem odd_parameter_control : absoluteDiscriminantParameter 3=3 := by
  norm_num [absoluteDiscriminantParameter]

theorem even_parameter_control : absoluteDiscriminantParameter 1=4 := by
  norm_num [absoluteDiscriminantParameter]
end
end TenthDiscriminant.OddFieldTwoClass

#check TenthDiscriminant.OddFieldTwoClass.idealMap_symm
#check TenthDiscriminant.OddFieldTwoClass.class_relation_map
#check TenthDiscriminant.OddFieldTwoClass.classMap_mk0
#check TenthDiscriminant.OddFieldTwoClass.classMap_inverse
#check TenthDiscriminant.OddFieldTwoClass.identity_class_control
#check TenthDiscriminant.OddFieldTwoClass.field_classNumber_eq
#check TenthDiscriminant.OddFieldTwoClass.canonical_odd_discriminant_bound
#check TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound
#check TenthDiscriminant.OddFieldTwoClass.class_one_control
#check TenthDiscriminant.OddFieldTwoClass.odd_parameter_control
#check TenthDiscriminant.OddFieldTwoClass.even_parameter_control
#print TenthDiscriminant.OddFieldTwoClass.idealMap
#print TenthDiscriminant.OddFieldTwoClass.classMap
#print TenthDiscriminant.OddFieldTwoClass.classEquiv
#print axioms TenthDiscriminant.OddFieldTwoClass.field_classNumber_eq
#print axioms TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound
#audit_namespace TenthDiscriminant.OddFieldTwoClass
