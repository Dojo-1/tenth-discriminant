import TenthDiscriminant.ControlledClassCount

/-! Prime-axis arithmetic on the same actual ideal bases used by the count. -/
open scoped NumberField nonZeroDivisors
open scoped Classical
namespace TenthDiscriminant.ActualPrimeAxis
open IdealCoordinates IdealBasisArithmetic PrincipalBasis
set_option autoImplicit false
noncomputable section

theorem axis_prime_iff (a p : Nat) (x : Int) (hp : p.Prime) :
    (a : Int)*x^2 = (p : Int) ↔ a=p ∧ (x=1 ∨ x= -1) := by
  constructor
  · intro hx
    have he : a*x.natAbs^2=p := by
      have hh := congrArg Int.natAbs hx
      simpa only [Int.natAbs_mul, Int.natAbs_pow, Int.natAbs_ofNat] using hh
    have hprime : (a*x.natAbs^2).Prime := he.symm ▸ hp
    rcases Nat.prime_mul_iff.mp hprime with ⟨ha, hu⟩ | ⟨hsq, ha⟩
    · have hxone : x.natAbs=1 := by simpa [Nat.pow_eq_one] using hu
      exact ⟨by simpa only [hu, mul_one] using he,
        by simpa using Int.natAbs_eq_iff.mp hxone⟩
    · exact False.elim ((Nat.Prime.not_prime_pow (by decide : 2 ≤ 2)) hsq)
  · rintro ⟨rfl, hx | hx⟩ <;> rw [hx] <;> simp

theorem actual_axis_prime (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (a b c : Int) (hf : FormData D J e a b c)
    (p : Nat) (hp : p.Prime) (z : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (hN : (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs=
      p*Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (hy : (coordinates e z).2=0) :
    a=(p : Int) ∧ ((coordinates e z).1=1 ∨ (coordinates e z).1= -1) := by
  have hb := hf.2.2 (coordinates e z).1 (coordinates e z).2
  rw [combine_coordinates _ _ e z] at hb
  simp [hy] at hb
  have hn : Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))=
      (p : Int)*(Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) := by
    have hh := congrArg (fun n : Nat => (n : Int)) hN
    simpa only [Int.natCast_natAbs,abs_of_nonneg (norm_nonneg D hsq _),Nat.cast_mul] using hh
  have hJ : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
  have hprod : (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*
      (a*(coordinates e z).1^2)=
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*(p : Int) := by
    rw [← hb,hn]
    ring
  have hx : a*(coordinates e z).1^2=(p : Int) := mul_left_cancel₀ (ne_of_gt hJ) hprod
  have hx' : (a.natAbs : Int)*(coordinates e z).1^2=(p : Int) := by
    simpa only [Int.natCast_natAbs,abs_of_pos hf.1] using hx
  have hh := (axis_prime_iff a.natAbs p (coordinates e z).1 hp).mp hx'
  refine ⟨?_,hh.2⟩
  have ha : (a.natAbs : Int)=a := by rw [Int.natCast_natAbs,abs_of_pos hf.1]
  rw [← ha,hh.1]

theorem actual_axis_card_le_two (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (a b c : Int) (hf : FormData D J e a b c)
    (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
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
    have hh := (actual_axis_prime D hsq J e a b c hf p hp z hN hy).2
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

theorem controlled_class_prime_count (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4)))) :
    ∃ J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Real) ≤
        ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) ∧
      (∀ I : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰, ClassGroup.mk0 I=C →
        ∃ z : 𝓞 (QuadraticField (((D : Int)+1)/4)), ClassFiber.NormLift I J z) ∧
      ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
        ∃ a b c : Int, FormData D J e a b c ∧
          a≤(Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) ∧
          (C=1 → a=1) ∧
          ∀ (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) (t : Nat),
            (∀ z ∈ U, PrimeNormalized J z) →
            (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
              Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t) →
            (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt D+
              4*Real.sqrt (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))*t/D)+
                (if C=1 then 0 else 2) := by
  classical
  obtain ⟨J,hJ,hB,hlift,e,a,b,c,hf,ha,haR,hrows⟩ :=
    ControlledClassCount.controlled_class_form_and_count D hsq h C
  by_cases hC : C=1
  · obtain ⟨ep,hfp,hOff,hCount⟩ := principal_class_form_and_prime_count D hsq J (hJ.trans hC)
    have hJ1 : (1 : Int)≤Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := by
      exact_mod_cast Nat.one_le_iff_ne_zero.mpr (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
    have hM : (1 : Real)≤ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) :=
      le_trans (by exact_mod_cast hJ1) hB
    refine ⟨J,hJ,hB,hlift,ep,1,1,((D : Int)+1)/4,hfp,hJ1,fun _ => rfl,?_⟩
    intro U t hprime hN
    have hc := hCount U t hprime hN
    have harg : (t : Real)/D ≤ ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))*t/D := by
      simpa only [one_mul] using div_le_div_of_nonneg_right
        (mul_le_mul_of_nonneg_right hM (Nat.cast_nonneg t)) (Nat.cast_nonneg D)
    have hs := Real.sqrt_le_sqrt harg
    rw [if_pos hC]
    linarith
  · refine ⟨J,hJ,hB,hlift,e,a,b,c,hf,ha,fun he => False.elim (hC he),?_⟩
    intro U t hprime hN
    let O := U.filter (fun z => (coordinates e z).2≠0)
    have hc := hrows O t (fun z hz => hN z (Finset.mem_filter.mp hz).1)
      (fun z hz => (Finset.mem_filter.mp hz).2)
    have hax := actual_axis_card_le_two D hsq J e a b c hf U hprime
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
  exact hp.ne_one ((axis_prime_iff 1 p x hp).mp he).1.symm

theorem zero_control (K : Type*) [Field K] [NumberField K] (J : (Ideal (𝓞 K))⁰) :
    ¬ PrimeNormalized J (0 : (J : Ideal (𝓞 K))) := zero_not_prime_normalized K J

theorem negation_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) (z : J) : coordinates e (-z)= -coordinates e z := by
  simp [coordinates]
end
end TenthDiscriminant.ActualPrimeAxis

#check TenthDiscriminant.ActualPrimeAxis.axis_prime_iff
#check TenthDiscriminant.ActualPrimeAxis.actual_axis_prime
#check TenthDiscriminant.ActualPrimeAxis.actual_axis_card_le_two
#check TenthDiscriminant.ActualPrimeAxis.controlled_class_prime_count
#check TenthDiscriminant.ActualPrimeAxis.scalar_three_control
#check TenthDiscriminant.ActualPrimeAxis.scalar_one_control
#check TenthDiscriminant.ActualPrimeAxis.zero_control
#check TenthDiscriminant.ActualPrimeAxis.negation_control
#print TenthDiscriminant.IdealCoordinates.FormData
#print TenthDiscriminant.PrincipalBasis.PrimeNormalized
#print axioms TenthDiscriminant.ActualPrimeAxis.actual_axis_card_le_two
#print axioms TenthDiscriminant.ActualPrimeAxis.controlled_class_prime_count
#audit_namespace TenthDiscriminant.ActualPrimeAxis

