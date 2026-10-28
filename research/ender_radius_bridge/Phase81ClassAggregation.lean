import TenthDiscriminant
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-! Actual ideal slices preserve labelled point cardinality before summing class bounds. -/
open scoped NumberField nonZeroDivisors BigOperators Classical
namespace TenthDiscriminant.ClassAggregation
open ClassFiber ResidueMultiplicity ControlledPrimeFamily PrincipalBasis
set_option autoImplicit false
noncomputable section

theorem two_class_accounting {ι : Type} [DecidableEq ι]
    (I : Finset ι) (j : ι) (hj : j ∈ I) (hI : I.card ≤ 2)
    (q beta : ι → Real) (A N : Real)
    (hrows : ∀ i ∈ I, q i ≤ A+beta i+(if i=j then 0 else 2))
    (hfour : 4*N ≤ ∑ i ∈ I, q i) :
    N ≤ ((I.card : Real)*A + (∑ i ∈ I, beta i) + I.card)/4 := by
  have hzero : (∑ i ∈ I, if i=j then (0 : Real) else 2) = 2*(I.card : Real)-2 := by
    calc
      _ = ∑ i ∈ I, (2-(if i=j then (2 : Real) else 0)) := by
        apply Finset.sum_congr rfl
        intro i hi
        split_ifs <;> norm_num
      _ = _ := by rw [Finset.sum_sub_distrib]; simp [hj]; ring
  have hsum : (∑ i ∈ I, q i) ≤
      (I.card : Real)*A + (∑ i ∈ I, beta i) + 2*(I.card : Real)-2 := by
    calc
      _ ≤ ∑ i ∈ I, (A+beta i+(if i=j then 0 else 2)) :=
        Finset.sum_le_sum hrows
      _ = _ := by rw [Finset.sum_add_distrib, Finset.sum_add_distrib, hzero]; simp; ring
  have hc : (I.card : Real) ≤ 2 := by exact_mod_cast hI
  linarith

theorem actual_class_slice (K : Type*) [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰)
    (U : Finset (ClassGroup (𝓞 K) × 𝓞 K)) (C : ClassGroup (𝓞 K))
    (hmem : ∀ x ∈ U, x.2 ∈ (J x.1 : Ideal (𝓞 K))) :
    ∃ V : Finset (J C : Ideal (𝓞 K)), V.card=(U.filter (fun x => x.1=C)).card ∧
      ∀ z ∈ V, (C,(z : 𝓞 K)) ∈ U := by
  classical
  let R := U.filter (fun x => x.1=C)
  let T := R.image Prod.snd
  have hi : Set.InjOn Prod.snd (R : Set (ClassGroup (𝓞 K) × 𝓞 K)) := by
    intro x hx y hy hxy
    apply Prod.ext
    · exact (Finset.mem_filter.mp hx).2.trans (Finset.mem_filter.mp hy).2.symm
    · exact hxy
  have hc : T.card=R.card := Finset.card_image_of_injOn hi
  have hT : ∀ z ∈ T, z ∈ (J C : Ideal (𝓞 K)) := by
    intro z hz
    obtain ⟨x,hx,he⟩ := Finset.mem_image.mp hz
    have hxC := (Finset.mem_filter.mp hx).2
    have hm := hmem x (Finset.mem_filter.mp hx).1
    simpa only [hxC,he] using hm
  let F : {z : 𝓞 K // z ∈ T} ↪ (J C : Ideal (𝓞 K)) :=
    ⟨fun z => ⟨z.val,hT z.val z.prop⟩,by
      intro z w he
      apply Subtype.ext
      exact congrArg (fun x : (J C : Ideal (𝓞 K)) => (x : 𝓞 K)) he⟩
  let V := T.attach.map F
  refine ⟨V,?_,?_⟩
  · calc
      V.card=T.card := by simp only [V,Finset.card_map,Finset.card_attach]
      _=R.card := hc
  · intro z hz
    obtain ⟨q,hq,he⟩ := Finset.mem_map.mp hz
    have hzT : (z : 𝓞 K) ∈ T := by
      rw [← he]
      exact q.prop
    obtain ⟨x,hx,hxz⟩ := Finset.mem_image.mp hzT
    have hxC := (Finset.mem_filter.mp hx).2
    have hepair : (C,(z : 𝓞 K))=x := Prod.ext hxC.symm hxz.symm
    rw [hepair]
    exact (Finset.mem_filter.mp hx).1

theorem prime_prefix_bound (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (t : Nat) (P : Finset Nat) (hP : ∀ p ∈ P, Admissible D p) (hpt : ∀ p ∈ P, p≤t) :
    (P.card : Real) ≤ (NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) : Real)/4 *
      (2*Real.pi*t/Real.sqrt D+4*Real.sqrt (normBound (QuadraticField (((D : Int)+1)/4))*t/D)+1) := by
  classical
  obtain ⟨J,hGood,hData,hPoints⟩ := controlled_family D hsq h
  obtain ⟨U,hU,hu⟩ := hPoints P hP
  let A : Real := 2*Real.pi*t/Real.sqrt D
  let B : Real := 4*Real.sqrt (normBound (QuadraticField (((D : Int)+1)/4))*t/D)
  let q := fun C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) =>
    ((U.filter (fun x => x.1=C)).card : Real)
  have hmem : ∀ x ∈ U, x.2 ∈ (J x.1 : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := by
    intro x hx
    obtain ⟨p,hp,hpoint⟩ := hu x hx
    exact hpoint.2.1
  have hrow : ∀ C, q C≤A+B+(if C=1 then 0 else 2) := by
    intro C
    obtain ⟨V,hV,hVU⟩ := actual_class_slice _ J U C hmem
    obtain ⟨e,a,b,c,hf,ha,hprin,hcount⟩ := (hData C).2
    have hprime : ∀ z ∈ V, PrimeNormalized (J C) z := by
      intro z hz
      obtain ⟨p,hp,hpoint⟩ := hu (C,(z : 𝓞 (QuadraticField (((D : Int)+1)/4)))) (hVU z hz)
      exact ⟨p,(hP p hp).1,hpoint.2.2⟩
    have hnorm : ∀ z ∈ V, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
        Ideal.absNorm (J C : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t := by
      intro z hz
      obtain ⟨p,hp,hpoint⟩ := hu (C,(z : 𝓞 (QuadraticField (((D : Int)+1)/4)))) (hVU z hz)
      rw [hpoint.2.2]
      exact (Nat.mul_le_mul_right _ (hpt p hp)).trans_eq (Nat.mul_comm _ _)
    have hc := hcount V t hprime hnorm
    rw [hV] at hc
    exact hc
  have htotal : U.card=∑ C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))),
      (U.filter (fun x => x.1=C)).card :=
    Finset.card_eq_sum_card_fiberwise (t:=Finset.univ) (f:=Prod.fst) (fun _ _ => Finset.mem_univ _)
  have htotalR : (U.card : Real)=∑ C, q C := by
    simpa only [Nat.cast_sum,q] using congrArg (fun n : Nat => (n : Real)) htotal
  have hfour : 4*(P.card : Real)≤∑ C, q C := by
    have he : 4*(P.card : Real)=∑ C, q C := calc
      _=(U.card : Real) := by exact_mod_cast hU.symm
      _=∑ C, q C := htotalR
    exact he.le
  have hcard : (Finset.univ : Finset (ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))))).card≤2 := by
    simpa only [Finset.card_univ] using h
  have hs := two_class_accounting Finset.univ 1 (Finset.mem_univ _) hcard q
    (fun _ => B) A (P.card : Real) (fun C _ => hrow C) hfour
  have hb : (P.card : Real) ≤
      ((NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) : Real)*A+
       (NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) : Real)*B+
       (NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) : Real))/4 := by
    simpa only [Finset.sum_const,Finset.card_univ,nsmul_eq_mul,NumberField.classNumber] using hs
  calc
    (P.card : Real) ≤ _ := hb
    _ = (NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) : Real)/4*(A+B+1) := by ring

theorem uniform_two_class_bound (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (t : Nat) (P : Finset Nat) (hP : ∀ p ∈ P, Admissible D p) (hpt : ∀ p ∈ P, p≤t) :
    (P.card : Real) ≤ (2*Real.pi*t/Real.sqrt D+
      4*Real.sqrt (normBound (QuadraticField (((D : Int)+1)/4))*t/D)+1)/2 := by
  have hb := prime_prefix_bound D hsq h t P hP hpt
  have hR : (NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) : Real)≤2 := by exact_mod_cast h
  have hp : (0 : Real)≤2*Real.pi*t/Real.sqrt D+
      4*Real.sqrt (normBound (QuadraticField (((D : Int)+1)/4))*t/D)+1 := by positivity
  calc
    (P.card : Real) ≤ _ := hb
    _ ≤ (2 : Real)/4*(2*Real.pi*t/Real.sqrt D+
      4*Real.sqrt (normBound (QuadraticField (((D : Int)+1)/4))*t/D)+1) :=
      mul_le_mul_of_nonneg_right (div_le_div_of_nonneg_right hR (by norm_num)) hp
    _ = _ := by ring

theorem empty_slice_control (K : Type*) [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰) (C : ClassGroup (𝓞 K)) :
    ∃ V : Finset (J C : Ideal (𝓞 K)), V.card=0 := by
  obtain ⟨V,hV,hm⟩ := actual_class_slice K J ∅ C (by simp)
  exact ⟨V,by simpa using hV⟩

theorem absent_slice_control {α β : Type*} (U : Finset (α×β)) (C : α)
    (hC : ∀ x ∈ U, x.1≠C) : (U.filter (fun x => x.1=C)).card=0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro x hx
  exact hC x (Finset.mem_filter.mp hx).1 (Finset.mem_filter.mp hx).2

theorem label_collision_control :
    ({((0 : Fin 2),(1 : Int)),(1,1)} : Finset (Fin 2×Int)).card=2 ∧
      (({((0 : Fin 2),(1 : Int)),(1,1)} : Finset (Fin 2×Int)).image Prod.snd).card=1 := by decide

theorem axis_constant_control :
    2*((1 : Int)-1)≤1 ∧ 2*((2 : Int)-1)≤2 ∧ 3<2*((3 : Int)-1) := by norm_num
end
end TenthDiscriminant.ClassAggregation

#check TenthDiscriminant.ClassAggregation.two_class_accounting
#check TenthDiscriminant.ClassAggregation.actual_class_slice
#check TenthDiscriminant.ClassAggregation.prime_prefix_bound
#check TenthDiscriminant.ClassAggregation.uniform_two_class_bound
#check TenthDiscriminant.ClassAggregation.empty_slice_control
#check TenthDiscriminant.ClassAggregation.absent_slice_control
#check TenthDiscriminant.ClassAggregation.label_collision_control
#check TenthDiscriminant.ClassAggregation.axis_constant_control
#print TenthDiscriminant.ControlledPrimeFamily.ClassCountData
#print TenthDiscriminant.ResidueMultiplicity.PointAt
#print axioms TenthDiscriminant.ClassAggregation.actual_class_slice
#print axioms TenthDiscriminant.ClassAggregation.prime_prefix_bound
#print axioms TenthDiscriminant.ClassAggregation.uniform_two_class_bound
#audit_namespace TenthDiscriminant.ClassAggregation

