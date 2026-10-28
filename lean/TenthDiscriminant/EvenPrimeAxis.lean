import TenthDiscriminant.EvenControlledClass
import TenthDiscriminant.ActualPrimeAxis
import TenthDiscriminant.PrincipalBasis

/-! The even principal axis is empty; other classes pay two across ALL primes. -/
open scoped NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.EvenPrimeAxis
open IdealCoordinates IdealBasisArithmetic PrincipalBasis EvenIdealCount EvenControlledClass
set_option autoImplicit false
noncomputable section

theorem principal_form_of_class (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰)
    (hclass : ClassGroup.mk0 J=1) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))),
      FormData D J e 1 0 (D : Int) := by
  let K := EvenQuadraticField D
  letI : (J : Ideal (𝓞 K)).IsPrincipal := (ClassGroup.mk0_eq_one_iff J.prop).mp hclass
  let g : 𝓞 K := Submodule.IsPrincipal.generator (J : Ideal (𝓞 K))
  have hspan : Ideal.span ({g} : Set (𝓞 K))=(J : Ideal (𝓞 K)) :=
    Ideal.span_singleton_generator (J : Ideal (𝓞 K))
  have hJ : (J : Ideal (𝓞 K))≠⊥ := by
    simpa only [Submodule.zero_eq_bot] using (mem_nonZeroDivisors_iff_ne_zero.mp J.prop)
  have hg : g≠0 := by
    intro he
    have hb : Ideal.span ({g} : Set (𝓞 K))=⊥ := by simp [he]
    exact hJ (hspan.symm.trans hb)
  obtain ⟨e,he⟩ := scaled_basis K (integerBasis D hsq hm) (J : Ideal (𝓞 K)) g hg hspan
  have hnat : (Algebra.norm Int g).natAbs=Ideal.absNorm (J : Ideal (𝓞 K)) := by
    rw [← Ideal.absNorm_span_singleton,hspan]
  have hNg : Algebra.norm Int g=(Ideal.absNorm (J : Ideal (𝓞 K)) : Int) := by
    have hh : |Algebra.norm Int g|=(Ideal.absNorm (J : Ideal (𝓞 K)) : Int) := by
      simpa only [Int.natCast_natAbs] using congrArg (fun n : Nat => (n : Int)) hnat
    exact (abs_of_pos (norm_pos D hsq hm g hg)).symm.trans hh
  have hcombine (x y : Int) : combine e x y=
      g*(x • integerBasis D hsq hm 0+y • integerBasis D hsq hm 1) := by
    unfold combine
    rw [he 0,he 1]
    simp [Algebra.smul_def,algebraMap_int_eq]
    ring
  refine ⟨e,by norm_num,?_,?_⟩
  · ring
  · intro x y
    rw [hcombine,map_mul,hNg,EvenIdealCount.norm_in_integer_basis]
    simp [EvenIdealCount.normQ]

theorem prime_axis_nonzero (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))))
    (hf : FormData D J e 1 0 (D : Int)) (p : Nat) (hp : p.Prime)
    (z : (J : Ideal (𝓞 (EvenQuadraticField D))))
    (hN : (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs=
      p*Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))) :
    (coordinates e z).2≠0 := by
  intro hy
  have hbase := hf.2.2 (coordinates e z).1 (coordinates e z).2
  rw [combine_coordinates _ _ e z] at hbase
  simp [hy] at hbase
  have hni : Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))=
      (p : Int)*(Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) := by
    have hh := congrArg (fun n : Nat => (n : Int)) hN
    simpa only [Int.natCast_natAbs,abs_of_nonneg (norm_nonneg D hsq hm _),Nat.cast_mul] using hh
  have hn : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
  have hprod : (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int)*
      (coordinates e z).1^2=
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int)*(p : Int) := by
    rw [← hbase,hni]
    ring
  have hx : (coordinates e z).1^2=(p : Int) := mul_left_cancel₀ (ne_of_gt hn) hprod
  have hxNat : (coordinates e z).1.natAbs^2=p := by
    have hh := congrArg Int.natAbs hx
    simpa only [Int.natAbs_pow,Int.natAbs_ofNat] using hh
  have hpow : ((coordinates e z).1.natAbs^2).Prime := hxNat.symm ▸ hp
  exact (Nat.Prime.not_prime_pow (by decide : 2≤2)) hpow

theorem principal_class_form_and_prime_count (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰) (hclass : ClassGroup.mk0 J=1) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))),
      FormData D J e 1 0 (D : Int) ∧
        (∀ (p : Nat), p.Prime → ∀ z : (J : Ideal (𝓞 (EvenQuadraticField D))),
          (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs=
            p*Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) →
          (coordinates e z).2≠0) ∧
        ∀ (U : Finset (J : Ideal (𝓞 (EvenQuadraticField D)))) (t : Nat),
          (∀ z ∈ U, PrimeNormalized J z) →
          (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
            Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))*t) →
          (U.card : Real)≤2*Real.pi*t/Real.sqrt (4*D)+4*Real.sqrt ((t : Real)/(4*D)) := by
  obtain ⟨e,hf⟩ := principal_form_of_class D hsq hm J hclass
  refine ⟨e,hf,fun p hp z hN => prime_axis_nonzero D hsq hm J e hf p hp z hN,?_⟩
  intro U t hprime hN
  have hy : ∀ z ∈ U, (coordinates e z).2≠0 := by
    intro z hz
    obtain ⟨p,hp,hn⟩ := hprime z hz
    exact prime_axis_nonzero D hsq hm J e hf p hp z hn
  have hb := count_for_actual_form D hsq hm J e 1 0 (D : Int) hf U t hN hy
  simpa only [Int.cast_one,one_mul] using hb

theorem actual_axis_prime (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))))
    (a b c : Int) (hf : FormData D J e a b c)
    (p : Nat) (hp : p.Prime) (z : (J : Ideal (𝓞 (EvenQuadraticField D))))
    (hN : (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs=
      p*Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))))
    (hy : (coordinates e z).2=0) :
    a=(p : Int) ∧ ((coordinates e z).1=1 ∨ (coordinates e z).1= -1) := by
  have hb := hf.2.2 (coordinates e z).1 (coordinates e z).2
  rw [combine_coordinates _ _ e z] at hb
  simp [hy] at hb
  have hn : Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))=
      (p : Int)*(Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) := by
    have hh := congrArg (fun n : Nat => (n : Int)) hN
    simpa only [Int.natCast_natAbs,abs_of_nonneg (norm_nonneg D hsq hm _),Nat.cast_mul] using hh
  have hJ : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
  have hprod : (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int)*
      (a*(coordinates e z).1^2)=
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int)*(p : Int) := by
    rw [← hb,hn]
    ring
  have hx : a*(coordinates e z).1^2=(p : Int) := mul_left_cancel₀ (ne_of_gt hJ) hprod
  have hx' : (a.natAbs : Int)*(coordinates e z).1^2=(p : Int) := by
    simpa only [Int.natCast_natAbs,abs_of_pos hf.1] using hx
  have hh := (ActualPrimeAxis.axis_prime_iff a.natAbs p (coordinates e z).1 hp).mp hx'
  refine ⟨?_,hh.2⟩
  have ha : (a.natAbs : Int)=a := by rw [Int.natCast_natAbs,abs_of_pos hf.1]
  rw [← ha,hh.1]

theorem actual_axis_card_le_two (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))))
    (a b c : Int) (hf : FormData D J e a b c)
    (U : Finset (J : Ideal (𝓞 (EvenQuadraticField D))))
    (hprime : ∀ z ∈ U, PrimeNormalized J z) :
    (U.filter (fun z => (coordinates e z).2=0)).card≤2 := by
  classical
  let A := U.filter (fun z => (coordinates e z).2=0)
  have hs : A.image (coordinates e) ⊆ ({(1,0),(-1,0)} : Finset (Int×Int)) := by
    intro q hq
    obtain ⟨z,hz,rfl⟩ := Finset.mem_image.mp hq
    have hzU := (Finset.mem_filter.mp hz).1
    have hy := (Finset.mem_filter.mp hz).2
    obtain ⟨p,hp,hN⟩ := hprime z hzU
    have hh := (actual_axis_prime D hsq hm J e a b c hf p hp z hN hy).2
    rcases hh with hh | hh
    · have he : coordinates e z=(1,0) := Prod.ext hh hy
      simp [he]
    · have he : coordinates e z=(-1,0) := Prod.ext hh hy
      simp [he]
  have hc : (A.image (coordinates e)).card=A.card :=
    Finset.card_image_of_injective A (coordinates_injective _ _ e)
  have hle := (Finset.card_le_card hs).trans (by norm_num : ({(1,0),(-1,0)} : Finset (Int×Int)).card≤2)
  rw [hc] at hle
  exact hle

theorem controlled_class_prime_count (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (C : ClassGroup (𝓞 (EvenQuadraticField D))) :
    ∃ J : (Ideal (𝓞 (EvenQuadraticField D)))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Real) ≤
        ClassFiber.normBound (EvenQuadraticField D) ∧
      (∀ I : (Ideal (𝓞 (EvenQuadraticField D)))⁰, ClassGroup.mk0 I=C →
        ∃ z : 𝓞 (EvenQuadraticField D), ClassFiber.NormLift I J z) ∧
      ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))),
        ∃ a b c : Int, FormData D J e a b c ∧
          a≤(Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) ∧
          (C=1 → a=1) ∧
          ∀ (U : Finset (J : Ideal (𝓞 (EvenQuadraticField D)))) (t : Nat),
            (∀ z ∈ U, PrimeNormalized J z) →
            (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
              Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))*t) →
            (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt (4*D)+
              4*Real.sqrt (ClassFiber.normBound (EvenQuadraticField D)*t/(4*D))+
                (if C=1 then 0 else 2) := by
  classical
  obtain ⟨J,hJ,hB,hlift,e,a,b,c,hf,ha,haR,hrows⟩ :=
    EvenControlledClass.controlled_class_form_and_count D hsq hm h C
  by_cases hC : C=1
  · obtain ⟨ep,hfp,hOff,hCount⟩ := principal_class_form_and_prime_count D hsq hm J (hJ.trans hC)
    have hJ1 : (1 : Int)≤Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) := by
      exact_mod_cast Nat.one_le_iff_ne_zero.mpr (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
    have hM : (1 : Real)≤ClassFiber.normBound (EvenQuadraticField D) :=
      le_trans (by exact_mod_cast hJ1) hB
    refine ⟨J,hJ,hB,hlift,ep,1,0,(D : Int),hfp,hJ1,fun _ => rfl,?_⟩
    intro U t hprime hN
    have hc := hCount U t hprime hN
    have harg : (t : Real)/(4*D) ≤ ClassFiber.normBound (EvenQuadraticField D)*t/(4*D) := by
      simpa only [one_mul] using div_le_div_of_nonneg_right
        (mul_le_mul_of_nonneg_right hM (Nat.cast_nonneg t)) (by positivity)
    have hs := Real.sqrt_le_sqrt harg
    rw [if_pos hC]
    linarith
  · refine ⟨J,hJ,hB,hlift,e,a,b,c,hf,ha,fun he => False.elim (hC he),?_⟩
    intro U t hprime hN
    let O := U.filter (fun z => (coordinates e z).2≠0)
    have hc := hrows O t (fun z hz => hN z (Finset.mem_filter.mp hz).1)
      (fun z hz => (Finset.mem_filter.mp hz).2)
    have hax := actual_axis_card_le_two D hsq hm J e a b c hf U hprime
    have haxR : ((U.filter (fun z => (coordinates e z).2=0)).card : Real)≤2 := by exact_mod_cast hax
    have hsplit : (U.card : Real)=(O.card : Real)+
        ((U.filter (fun z => (coordinates e z).2=0)).card : Real) := by
      have hh := Finset.filter_card_add_filter_neg_card_eq_card (s:=U) (fun z => (coordinates e z).2≠0)
      have he : O.card+(U.filter (fun z => (coordinates e z).2=0)).card=U.card := by
        simpa only [not_not] using hh
      exact_mod_cast he.symm
    rw [if_neg hC]
    linarith

theorem scalar_three_control :
    (3 : Int)*1^2=3 ∧ (3 : Int)*(-1)^2=3 ∧ Nat.Prime 3 := by norm_num

theorem scalar_one_control (p : Nat) (hp : p.Prime) (x : Int) :
    ¬ (1 : Int)*x^2=(p : Int) := by
  intro he
  exact hp.ne_one ((ActualPrimeAxis.axis_prime_iff 1 p x hp).mp he).1.symm

theorem zero_control (K : Type*) [Field K] [NumberField K] (J : (Ideal (𝓞 K))⁰) :
    ¬ PrimeNormalized J (0 : (J : Ideal (𝓞 K))) := zero_not_prime_normalized K J

theorem negation_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) (z : J) : coordinates e (-z)= -coordinates e z := by
  simp [coordinates]
private instance gaussianPositive : Fact (0<(1 : Nat)) := ⟨by decide⟩

theorem gaussian_unit_control :
    ∃ e : Basis (Fin 2) Int ((1 : (Ideal (𝓞 (EvenQuadraticField 1)))⁰) : Ideal (𝓞 (EvenQuadraticField 1))),
      FormData 1 1 e 1 0 1 := by
  simpa using principal_form_of_class 1 (by norm_num) (by decide) 1 (map_one ClassGroup.mk0)
end
end TenthDiscriminant.EvenPrimeAxis

#check TenthDiscriminant.EvenPrimeAxis.principal_form_of_class
#check TenthDiscriminant.EvenPrimeAxis.prime_axis_nonzero
#check TenthDiscriminant.EvenPrimeAxis.principal_class_form_and_prime_count
#check TenthDiscriminant.EvenPrimeAxis.actual_axis_prime
#check TenthDiscriminant.EvenPrimeAxis.actual_axis_card_le_two
#check TenthDiscriminant.EvenPrimeAxis.controlled_class_prime_count
#check TenthDiscriminant.EvenPrimeAxis.scalar_three_control
#check TenthDiscriminant.EvenPrimeAxis.scalar_one_control
#check TenthDiscriminant.EvenPrimeAxis.zero_control
#check TenthDiscriminant.EvenPrimeAxis.negation_control
#check TenthDiscriminant.EvenPrimeAxis.gaussian_unit_control
#print TenthDiscriminant.EvenControlledClass.FormData
#print TenthDiscriminant.PrincipalBasis.PrimeNormalized
#print axioms TenthDiscriminant.EvenPrimeAxis.controlled_class_prime_count
#audit_namespace TenthDiscriminant.EvenPrimeAxis

