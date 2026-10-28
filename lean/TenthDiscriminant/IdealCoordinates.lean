import TenthDiscriminant.IdealBasisArithmetic
import TenthDiscriminant.QuadraticAreaCount
import Mathlib.LinearAlgebra.FreeModule.PID

/-! The checked arbitrary-basis arithmetic is composed once with an actual ideal basis.
The same form and coordinates then serve every finite set and threshold. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.IdealCoordinates
open IdealBasisArithmetic
set_option autoImplicit false
noncomputable section

def coordinates {K : Type*} [Field K] [NumberField K] {J : Ideal (𝓞 K)}
    (e : Basis (Fin 2) Int J) (z : J) : Int×Int := (e.repr z 0,e.repr z 1)

theorem coordinates_injective (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) : Function.Injective (coordinates e) := by
  intro z w he
  apply e.repr.injective
  ext i
  fin_cases i
  · exact congrArg Prod.fst he
  · exact congrArg Prod.snd he

theorem combine_coordinates (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) (z : J) :
    combine e (coordinates e z).1 (coordinates e z).2=(z : 𝓞 K) := by
  let L : J →ₗ[Int] 𝓞 K := (Submodule.subtype J).restrictScalars Int
  have hs := congrArg L (e.sum_repr z)
  rw [Fin.sum_univ_two,map_add,map_smul,map_smul] at hs
  simpa [L,combine,coordinates,Algebra.smul_def,algebraMap_int_eq] using hs

def FormData (D : Nat) [Fact ((D : Int)%4=3)]
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (a b c : Int) : Prop :=
  0<a ∧ 4*a*c-b^2=(D : Int) ∧
    ∀ x y : Int, Algebra.norm Int (combine e x y)=
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*
        (a*x^2+b*x*y+c*y^2)

theorem actual_ideal_norm_form (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      ∃ a b c : Int, FormData D J e a b c := by
  have hJ : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))≠⊥ := by
    simpa only [Submodule.zero_eq_bot] using (mem_nonZeroDivisors_iff_ne_zero.mp J.prop)
  let e := Ideal.selfBasis (integerBasis D hsq)
    (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) hJ
  obtain ⟨a,b,c,ha,hd,hn⟩ := normalized_form_of_basis D hsq J e
  exact ⟨e,a,b,c,ha,hd,hn⟩

theorem count_for_actual_form (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (a b c : Int) (hf : FormData D J e a b c)
    (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) (t : Nat)
    (hN : ∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
      Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t)
    (hy : ∀ z ∈ U, (coordinates e z).2≠0) :
    (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt D+4*Real.sqrt ((a : Real)*t/D) := by
  classical
  let V := U.image (coordinates e)
  have hcard : V.card=U.card := Finset.card_image_of_injective U (coordinates_injective _ _ e)
  have hD : 0<D := by have hm := (Fact.out : (D : Int)%4=3); omega
  have hdR : 4*(a : Real)*c-(b : Real)^2=(D : Real) := by exact_mod_cast hf.2.1
  have hQ : ∀ p ∈ V, (a : Real)*(p.1 : Real)^2+(b : Real)*(p.1 : Real)*(p.2 : Real)+
      (c : Real)*(p.2 : Real)^2 ≤ (t : Real) := by
    intro p hp
    obtain ⟨z,hz,rfl⟩ := Finset.mem_image.mp hp
    have hn := hN z hz
    have hnn := norm_nonneg D hsq (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))
    have hi : (((Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs : Nat) : Int) ≤
        ((Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t : Nat) : Int) := by
      exact_mod_cast hn
    rw [Int.natCast_natAbs,abs_of_nonneg hnn,Nat.cast_mul] at hi
    have he := hf.2.2 (coordinates e z).1 (coordinates e z).2
    rw [combine_coordinates _ _ e z] at he
    rw [he] at hi
    have hnJ : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := by
      exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
    have hq : a*(coordinates e z).1^2+b*(coordinates e z).1*(coordinates e z).2+
        c*(coordinates e z).2^2 ≤ (t : Int) := (mul_le_mul_left hnJ).mp hi
    exact_mod_cast hq
  have hY : ∀ p ∈ V, p.2≠0 := by
    intro p hp
    obtain ⟨z,hz,rfl⟩ := Finset.mem_image.mp hp
    exact hy z hz
  have hb := QuadraticRows.off_axis_area_bound V (a : Real) (b : Real) (c : Real) (t : Real)
    (by exact_mod_cast hf.1) (by rw [hdR]; exact_mod_cast hD) (Nat.cast_nonneg t) hQ hY
  simpa only [hcard,hdR] using hb

/-- The basis and form precede every finite set and threshold. -/
theorem actual_ideal_form_and_count (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      ∃ a b c : Int, FormData D J e a b c ∧
        ∀ (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) (t : Nat),
          (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
            Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t) →
          (∀ z ∈ U, (coordinates e z).2≠0) →
          (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt D+4*Real.sqrt ((a : Real)*t/D) := by
  obtain ⟨e,a,b,c,hf⟩ := actual_ideal_norm_form D hsq J
  exact ⟨e,a,b,c,hf,fun U t hN hy => count_for_actual_form D hsq J e a b c hf U t hN hy⟩

theorem coordinate_negation_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) (z : J) : coordinates e (-z)= -coordinates e z := by
  simp [coordinates]

theorem zero_threshold_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) (U : Finset J)
    (hN : ∀ z ∈ U, (Algebra.norm Int (z : 𝓞 K)).natAbs≤0)
    (hy : ∀ z ∈ U, (coordinates e z).2≠0) : U=∅ := by
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro z hz
  have hn0 : Algebra.norm Int (z : 𝓞 K)=0 := Int.natAbs_eq_zero.mp (Nat.le_zero.mp (hN z hz))
  have hz0 : (z : 𝓞 K)=0 := Algebra.norm_eq_zero_iff.mp hn0
  have hzero : z=0 := Subtype.ext hz0
  exact hy z hz (by rw [hzero]; simp [coordinates])

theorem origin_guard_control (K : Type*) [Field K] [NumberField K] (J : Ideal (𝓞 K))
    (e : Basis (Fin 2) Int J) :
    (coordinates e 0).2=0 ∧ (Algebra.norm Int (0 : 𝓞 K)).natAbs=0 ∧
      ¬ (({(0 : J)} : Finset J).card : Real)≤0 := by simp [coordinates]

private instance sevenCondition : Fact (0<4*(2 : Int)-1) := ⟨by decide⟩
private instance sevenMod : Fact (((7 : Nat) : Int)%4=3) := ⟨by decide⟩
private theorem sevenSq : Squarefree (7 : Nat) := (by norm_num : Nat.Prime 7).squarefree

theorem proper_ideal_control :
    Ideal.absNorm (Ideal.span ({(2 : 𝓞 (QuadraticField 2))} : Set (𝓞 (QuadraticField 2))))=4 :=
  IdealBasisArithmetic.proper_ideal_control

theorem unit_ideal_empty_control :
    ∃ e : Basis (Fin 2) Int ((1 : (Ideal (𝓞 (QuadraticField 2)))⁰) : Ideal (𝓞 (QuadraticField 2))),
      ∃ a b c : Int, FormData 7 1 e a b c ∧ (0 : Real)≤0 := by
  obtain ⟨e,a,b,c,hf,hall⟩ := actual_ideal_form_and_count 7 sevenSq 1
  have hb := hall ∅ 0 (by simp) (by simp)
  exact ⟨e,a,b,c,hf,by simpa using hb⟩
end
end TenthDiscriminant.IdealCoordinates

#check TenthDiscriminant.IdealCoordinates.actual_ideal_norm_form
#check TenthDiscriminant.IdealCoordinates.actual_ideal_form_and_count
#print TenthDiscriminant.IdealCoordinates.FormData
#print axioms TenthDiscriminant.IdealCoordinates.actual_ideal_form_and_count
#audit_namespace TenthDiscriminant.IdealCoordinates
