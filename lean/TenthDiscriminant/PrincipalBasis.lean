import TenthDiscriminant.IdealCoordinates
import TenthDiscriminant.AxiomAudit
import Mathlib.RingTheory.Ideal.Basis

/-! Calibrate a particular identity-class ideal, without a class-number-one hypothesis.
Multiplication by its generator cancels out of the normalized norm form. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.PrincipalBasis
open IdealBasisArithmetic IdealCoordinates
set_option autoImplicit false
noncomputable section

def PrimeNormalized {K : Type*} [Field K] [NumberField K]
    (J : (Ideal (𝓞 K))⁰) (z : (J : Ideal (𝓞 K))) : Prop :=
  ∃ p : Nat, p.Prime ∧ (Algebra.norm Int (z : 𝓞 K)).natAbs=
    p*Ideal.absNorm (J : Ideal (𝓞 K))

theorem scaled_basis (K : Type*) [Field K] [NumberField K]
    (v : Basis (Fin 2) Int (𝓞 K)) (J : Ideal (𝓞 K)) (g : 𝓞 K)
    (hg : g≠0) (hspan : Ideal.span ({g} : Set (𝓞 K))=J) :
    ∃ e : Basis (Fin 2) Int J, ∀ i, (e i : 𝓞 K)=g*v i := by
  let L := (LinearEquiv.ofEq (Ideal.span ({g} : Set (𝓞 K))) J hspan).restrictScalars Int
  refine ⟨(Ideal.basisSpanSingleton v hg).map L,?_⟩
  intro i
  rw [Basis.map_apply]
  change ((LinearEquiv.ofEq (Ideal.span ({g} : Set (𝓞 K))) J hspan)
    ((Ideal.basisSpanSingleton v hg) i) : 𝓞 K)=g*v i
  rw [LinearEquiv.coe_ofEq_apply]
  exact Ideal.basisSpanSingleton_apply v hg i

theorem principal_form_of_class (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (hclass : ClassGroup.mk0 J=1) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      FormData D J e 1 1 (((D : Int)+1)/4) := by
  let K := QuadraticField (((D : Int)+1)/4)
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
  obtain ⟨e,he⟩ := scaled_basis K (integerBasis D hsq) (J : Ideal (𝓞 K)) g hg hspan
  have hnat : (Algebra.norm Int g).natAbs=Ideal.absNorm (J : Ideal (𝓞 K)) := by
    rw [← Ideal.absNorm_span_singleton,hspan]
  have hNg : Algebra.norm Int g=(Ideal.absNorm (J : Ideal (𝓞 K)) : Int) := by
    have hh : |Algebra.norm Int g|=(Ideal.absNorm (J : Ideal (𝓞 K)) : Int) := by
      simpa only [Int.natCast_natAbs] using congrArg (fun n : Nat => (n : Int)) hnat
    exact (abs_of_pos (norm_pos D hsq g hg)).symm.trans hh
  have hcombine (x y : Int) : combine e x y=
      g*(x • integerBasis D hsq 0+y • integerBasis D hsq 1) := by
    unfold combine
    rw [he 0,he 1]
    simp [Algebra.smul_def,algebraMap_int_eq]
    ring
  refine ⟨e,by norm_num,?_,?_⟩
  · have hh := halfOrder_coefficient_identity D (Fact.out : (D : Int)%4=3)
    nlinarith
  · intro x y
    rw [hcombine,map_mul,hNg,norm_in_integer_basis]
    simp [principalNorm]

theorem prime_axis_nonzero (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (hf : FormData D J e 1 1 (((D : Int)+1)/4)) (p : Nat) (hp : p.Prime)
    (z : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (hN : (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs=
      p*Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) :
    (coordinates e z).2≠0 := by
  intro hy
  have hbase := hf.2.2 (coordinates e z).1 (coordinates e z).2
  rw [combine_coordinates _ _ e z] at hbase
  simp [hy] at hbase
  have hni : Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))=
      (p : Int)*(Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) := by
    have hh := congrArg (fun n : Nat => (n : Int)) hN
    simpa only [Int.natCast_natAbs,abs_of_nonneg (norm_nonneg D hsq _),Nat.cast_mul] using hh
  have hn : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
  have hprod : (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*
      (coordinates e z).1^2=
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*(p : Int) := by
    rw [← hbase,hni]
    ring
  have hx : (coordinates e z).1^2=(p : Int) := mul_left_cancel₀ (ne_of_gt hn) hprod
  have hxNat : (coordinates e z).1.natAbs^2=p := by
    have hh := congrArg Int.natAbs hx
    simpa only [Int.natAbs_pow,Int.natAbs_ofNat] using hh
  have hpow : ((coordinates e z).1.natAbs^2).Prime := hxNat.symm ▸ hp
  exact (Nat.Prime.not_prime_pow (by decide : 2≤2)) hpow

theorem principal_class_form_and_prime_count (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) (hclass : ClassGroup.mk0 J=1) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      FormData D J e 1 1 (((D : Int)+1)/4) ∧
        (∀ (p : Nat), p.Prime → ∀ z : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
          (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs=
            p*Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) →
          (coordinates e z).2≠0) ∧
        ∀ (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) (t : Nat),
          (∀ z ∈ U, PrimeNormalized J z) →
          (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
            Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t) →
          (U.card : Real)≤2*Real.pi*t/Real.sqrt D+4*Real.sqrt ((t : Real)/D) := by
  obtain ⟨e,hf⟩ := principal_form_of_class D hsq J hclass
  refine ⟨e,hf,fun p hp z hN => prime_axis_nonzero D hsq J e hf p hp z hN,?_⟩
  intro U t hprime hN
  have hy : ∀ z ∈ U, (coordinates e z).2≠0 := by
    intro z hz
    obtain ⟨p,hp,hn⟩ := hprime z hz
    exact prime_axis_nonzero D hsq J e hf p hp z hn
  have hb := count_for_actual_form D hsq J e 1 1 (((D : Int)+1)/4) hf U t hN hy
  simpa only [Int.cast_one,one_mul] using hb

theorem zero_not_prime_normalized (K : Type*) [Field K] [NumberField K]
    (J : (Ideal (𝓞 K))⁰) : ¬ PrimeNormalized J (0 : (J : Ideal (𝓞 K))) := by
  rintro ⟨p,hp,hn⟩
  have hpos : 0<p*Ideal.absNorm (J : Ideal (𝓞 K)) :=
    Nat.mul_pos hp.pos (Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J))
  have he : 0=p*Ideal.absNorm (J : Ideal (𝓞 K)) := by simpa using hn
  exact (ne_of_gt hpos) he.symm

private instance sevenCondition : Fact (0<4*(2 : Int)-1) := ⟨by decide⟩
private instance sevenMod : Fact (((7 : Nat) : Int)%4=3) := ⟨by decide⟩
private theorem sevenSq : Squarefree (7 : Nat) := (by norm_num : Nat.Prime 7).squarefree

theorem unit_ideal_control :
    ∃ e : Basis (Fin 2) Int ((1 : (Ideal (𝓞 (QuadraticField 2)))⁰) : Ideal (𝓞 (QuadraticField 2))),
      FormData 7 1 e 1 1 2 := by
  simpa using principal_form_of_class 7 sevenSq 1 (map_one ClassGroup.mk0)

def twoIdeal : (Ideal (𝓞 (QuadraticField 2)))⁰ :=
  ⟨Ideal.span ({2} : Set (𝓞 (QuadraticField 2))),
    Ideal.absNorm_ne_zero_iff_mem_nonZeroDivisors.mp (by
      rw [IdealBasisArithmetic.proper_ideal_control]; decide)⟩

theorem proper_ideal_control :
    Ideal.absNorm (twoIdeal : Ideal (𝓞 (QuadraticField 2)))=4 ∧
      ∃ e : Basis (Fin 2) Int (twoIdeal : Ideal (𝓞 (QuadraticField 2))), FormData 7 twoIdeal e 1 1 2 := by
  have hc : ClassGroup.mk0 twoIdeal=1 :=
    (ClassGroup.mk0_eq_one_iff twoIdeal.prop).mpr (by exact ⟨⟨(2 : 𝓞 (QuadraticField 2)),rfl⟩⟩)
  exact ⟨IdealBasisArithmetic.proper_ideal_control,by simpa using principal_form_of_class 7 sevenSq twoIdeal hc⟩

theorem uncalibrated_axis_control :
    (3 : Int)*1^2+1*1*0+1001*0^2=3 ∧
      (3 : Int)*(-1)^2+1*(-1)*0+1001*0^2=3 ∧ Nat.Prime 3 := by norm_num
end
end TenthDiscriminant.PrincipalBasis

#check TenthDiscriminant.PrincipalBasis.principal_class_form_and_prime_count
#print TenthDiscriminant.IdealCoordinates.FormData
#print TenthDiscriminant.PrincipalBasis.PrimeNormalized
#print axioms TenthDiscriminant.PrincipalBasis.principal_class_form_and_prime_count
#audit_namespace TenthDiscriminant.PrincipalBasis
