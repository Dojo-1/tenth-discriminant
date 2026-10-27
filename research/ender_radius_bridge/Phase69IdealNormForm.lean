import TenthDiscriminant
import Mathlib.LinearAlgebra.FreeModule.PID
import Mathlib.RingTheory.Ideal.Basis

/-! Integral coordinates for the actual normalized ideal norm.
The leading coefficient is positive, but no uniform upper bound is asserted. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.IdealNormForm
set_option autoImplicit false
noncomputable section

def integerBasis (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    Basis (Fin 2) Int (𝓞 (QuadraticField (((D : Int)+1)/4))) :=
  (halfOrderBasis D).map (halfOrderEquivRingOfIntegers D hsq).toAddEquiv.toIntLinearEquiv

def coordinates {M : Type*} [AddCommGroup M] [Module Int M]
    (e : Basis (Fin 2) Int M) (z : M) : Int × Int := (e.repr z 0,e.repr z 1)

theorem coordinates_reconstruct {M : Type*} [AddCommGroup M] [Module Int M]
    (e : Basis (Fin 2) Int M) (z : M) :
    z=(coordinates e z).1 • e 0 + (coordinates e z).2 • e 1 := by
  simpa only [coordinates,Fin.sum_univ_two] using (e.sum_repr z).symm

theorem coordinates_injective {M : Type*} [AddCommGroup M] [Module Int M]
    (e : Basis (Fin 2) Int M) : Function.Injective (coordinates e) := by
  intro z w he
  apply e.repr.injective
  ext i
  fin_cases i
  · exact congrArg Prod.fst he
  · exact congrArg Prod.snd he

theorem norm_in_integer_basis (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (x y : Int) :
    Algebra.norm Int (x • integerBasis D hsq 0 + y • integerBasis D hsq 1)=
      principalNorm (D : Int) x y := by
  simpa [integerBasis,Basis.map_apply,halfOrderBasis_zero,halfOrderBasis_one,
    Algebra.smul_def,map_add,map_mul] using halfOrder_ringOfIntegers_norm D x y

theorem norm_coordinates (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) :
    Algebra.norm Int z=principalNorm (D : Int)
      (coordinates (integerBasis D hsq) z).1 (coordinates (integerBasis D hsq) z).2 := by
  nth_rw 1 [coordinates_reconstruct (integerBasis D hsq) z]
  exact norm_in_integer_basis D hsq _ _

theorem norm_nonneg (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) : 0 ≤ Algebra.norm Int z := by
  rw [norm_coordinates D hsq]
  exact principalNorm_nonneg D Fact.out _ _

theorem norm_pos (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) (hz : z≠0) : 0 < Algebra.norm Int z :=
  lt_of_le_of_ne (norm_nonneg D hsq z) (Ne.symm (Algebra.norm_ne_zero_iff.mpr hz))

theorem exists_ideal_norm_form (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      ∃ a b c : Int, 0<a ∧ 4*a*c-b^2=(D : Int) ∧
        ∀ x y : Int, Algebra.norm Int
          ((x • e 0+y • e 1 : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) :
            𝓞 (QuadraticField (((D : Int)+1)/4))) =
          (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*
            (a*x^2+b*x*y+c*y^2) := by
  let K := QuadraticField (((D : Int)+1)/4)
  let v := integerBasis D hsq
  have hJ : (J : Ideal (𝓞 K))≠⊥ := by
    simpa only [Submodule.zero_eq_bot] using (mem_nonZeroDivisors_iff_ne_zero.mp J.prop)
  let e := Ideal.selfBasis v (J : Ideal (𝓞 K)) hJ
  let n : Int := Ideal.absNorm (J : Ideal (𝓞 K))
  have hn : 0<n := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
  let s := v.repr (e 0 : 𝓞 K) 0
  let t := v.repr (e 0 : 𝓞 K) 1
  let u := v.repr (e 1 : 𝓞 K) 0
  let w := v.repr (e 1 : 𝓞 K) 1
  let cross : Int := 2*s*u+s*w+t*u+2*(((D : Int)+1)/4)*t*w
  have hnorm (x y : Int) : Algebra.norm Int
      ((x • e 0+y • e 1 : (J : Ideal (𝓞 K))) : 𝓞 K)=
      principalNorm (D : Int) (x*s+y*u) (x*t+y*w) := by
    rw [norm_coordinates D hsq]
    simp only [coordinates,map_add,map_smul,Finsupp.add_apply,Finsupp.smul_apply,smul_eq_mul]
    rfl
  have hN0 : Algebra.norm Int (e 0 : 𝓞 K)=principalNorm (D : Int) s t := by
    simpa using hnorm 1 0
  have hN1 : Algebra.norm Int (e 1 : 𝓞 K)=principalNorm (D : Int) u w := by
    simpa using hnorm 0 1
  have hNsum : Algebra.norm Int ((e 0+e 1 : (J : Ideal (𝓞 K))) : 𝓞 K)=
      principalNorm (D : Int) (s+u) (t+w) := by simpa using hnorm 1 1
  have hd0 : n ∣ Algebra.norm Int (e 0 : 𝓞 K) := Ideal.absNorm_dvd_norm_of_mem (e 0).property
  have hd1 : n ∣ Algebra.norm Int (e 1 : 𝓞 K) := Ideal.absNorm_dvd_norm_of_mem (e 1).property
  have hds : n ∣ Algebra.norm Int ((e 0+e 1 : (J : Ideal (𝓞 K))) : 𝓞 K) :=
    Ideal.absNorm_dvd_norm_of_mem (e 0+e 1).property
  obtain ⟨a,ha⟩ := hd0
  obtain ⟨c,hc⟩ := hd1
  obtain ⟨b,hb⟩ := dvd_sub (dvd_sub hds hd0) hd1
  have hA : principalNorm (D : Int) s t=n*a := hN0.symm.trans ha
  have hC : principalNorm (D : Int) u w=n*c := hN1.symm.trans hc
  have hB : cross=n*b := by
    calc
      _ = principalNorm (D : Int) (s+u) (t+w)-principalNorm (D : Int) s t-
          principalNorm (D : Int) u w := by dsimp [cross,principalNorm]; ring
      _ = _ := by rw [← hNsum,← hN0,← hN1]; exact hb
  have hdet : (s*w-t*u).natAbs=Ideal.absNorm (J : Ideal (𝓞 K)) := by
    simpa only [Basis.det_apply,Matrix.det_fin_two,Basis.toMatrix_apply,Function.comp_apply,
      mul_comm,s,t,u,w] using Ideal.natAbs_det_basis_change v (J : Ideal (𝓞 K)) e
  have hsqdet : (s*w-t*u)^2=n^2 := by
    have he := congrArg (fun m : Nat => (m : Int)^2) hdet
    simpa only [Int.natCast_natAbs,sq_abs,n] using he
  have hraw : 4*principalNorm (D : Int) s t*principalNorm (D : Int) u w-cross^2=
      (D : Int)*(s*w-t*u)^2 := by
    have he := halfOrder_coefficient_identity D (Fact.out : (D : Int)%4=3)
    dsimp [principalNorm,cross]
    linear_combination (s*w-t*u)^2*he
  have hdisc : 4*a*c-b^2=(D : Int) := by
    rw [hA,hB,hC,hsqdet] at hraw
    apply mul_left_cancel₀ (pow_ne_zero 2 (ne_of_gt hn))
    linear_combination hraw
  have hapos : 0<a := by
    have hz : (e 0 : 𝓞 K)≠0 := by
      intro he
      exact e.ne_zero 0 (Subtype.ext he)
    have hp := norm_pos D hsq (e 0 : 𝓞 K) hz
    nlinarith [ha]
  refine ⟨e,a,b,c,hapos,hdisc,?_⟩
  intro x y
  rw [hnorm]
  calc
    _ = x^2*principalNorm (D : Int) s t+x*y*cross+y^2*principalNorm (D : Int) u w := by
      dsimp [principalNorm,cross]; ring
    _ = _ := by rw [hA,hB,hC]; ring

theorem actual_ideal_off_axis_count (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      ∃ a b c : Int, 0<a ∧ 4*a*c-b^2=(D : Int) ∧
        ∀ (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) (t : Nat),
          (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
            Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t) →
          (∀ z ∈ U, (coordinates e z).2≠0) →
          (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt D+4*Real.sqrt ((a : Real)*t/D) := by
  classical
  obtain ⟨e,a,b,c,ha,hd,hnorm⟩ := exists_ideal_norm_form D hsq J
  refine ⟨e,a,b,c,ha,hd,?_⟩
  intro U t hnormBound hy
  let V := U.image (coordinates e)
  have hcard : V.card=U.card := Finset.card_image_of_injective U (coordinates_injective e)
  have hD : 0<D := by have hm := (Fact.out : (D : Int)%4=3); omega
  have hdR : 4*(a : Real)*c-(b : Real)^2=(D : Real) := by exact_mod_cast hd
  have hQ : ∀ p ∈ V, (a : Real)*(p.1 : Real)^2+(b : Real)*(p.1 : Real)*(p.2 : Real)+
      (c : Real)*(p.2 : Real)^2 ≤ (t : Real) := by
    intro p hp
    obtain ⟨z,hz,rfl⟩ := Finset.mem_image.mp hp
    have hn := hnormBound z hz
    have hnonneg := norm_nonneg D hsq (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))
    have hni : Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) ≤
        (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*(t : Int) := by
      have hc : (((Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs : Nat) : Int) ≤
          ((Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t : Nat) : Int) := by exact_mod_cast hn
      simpa only [Int.natCast_natAbs,abs_of_nonneg hnonneg,Nat.cast_mul] using hc
    have he := hnorm (coordinates e z).1 (coordinates e z).2
    rw [← coordinates_reconstruct e z] at he
    have hN : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := by
      exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
    have hq : a*(coordinates e z).1^2+b*(coordinates e z).1*(coordinates e z).2+
        c*(coordinates e z).2^2 ≤ (t : Int) := by nlinarith [he]
    exact_mod_cast hq
  have hY : ∀ p ∈ V, p.2≠0 := by
    intro p hp
    obtain ⟨z,hz,rfl⟩ := Finset.mem_image.mp hp
    exact hy z hz
  have hbound := QuadraticRows.off_axis_area_bound V (a : Real) (b : Real) (c : Real) (t : Real)
    (by exact_mod_cast ha) (by rw [hdR]; exact_mod_cast hD) (Nat.cast_nonneg t) hQ hY
  simpa only [hcard,hdR] using hbound

private instance sevenCondition : Fact (0<4*(2 : Int)-1) := ⟨by decide⟩
private instance sevenMod : Fact (((7 : Nat) : Int)%4=3) := ⟨by decide⟩
private theorem sevenSq : Squarefree (7 : Nat) := (by norm_num : Nat.Prime 7).squarefree

theorem seven_ambient_control (x y : Int) :
    Algebra.norm Int (x • integerBasis 7 sevenSq 0+y • integerBasis 7 sevenSq 1)=x^2+x*y+2*y^2 := by
  simpa [principalNorm] using norm_in_integer_basis 7 sevenSq x y

theorem seven_shear_control (x y : Int) :
    Algebra.norm Int (x • integerBasis 7 sevenSq 0+y •
      (integerBasis 7 sevenSq 0+integerBasis 7 sevenSq 1))=x^2+3*x*y+4*y^2 := by
  have he : x • integerBasis 7 sevenSq 0+y • (integerBasis 7 sevenSq 0+integerBasis 7 sevenSq 1)=
      (x+y) • integerBasis 7 sevenSq 0+y • integerBasis 7 sevenSq 1 := by
    simp only [smul_add,add_smul]; abel
  rw [he,seven_ambient_control]; ring

theorem proper_ideal_control :
    Ideal.absNorm (Ideal.span ({(2 : 𝓞 (QuadraticField 2))} : Set (𝓞 (QuadraticField 2))))=4 := by
  rw [Ideal.absNorm_span_singleton]
  have hn := seven_ambient_control 2 0
  simpa [integerBasis,Basis.map_apply,halfOrderBasis_zero] using congrArg Int.natAbs hn

theorem proper_scalar_control (x y : Int) :
    Algebra.norm Int ((2*x) • integerBasis 7 sevenSq 0+(2*y) • integerBasis 7 sevenSq 1)=
      4*(x^2+x*y+2*y^2) := by rw [seven_ambient_control]; ring

theorem origin_guard_control :
    (Algebra.norm Int (0 : 𝓞 (QuadraticField 2))).natAbs=0 ∧
      ¬ (({(0 : Int×Int)} : Finset (Int×Int)).card : Real)≤0 := by norm_num
end
end TenthDiscriminant.IdealNormForm

#check TenthDiscriminant.IdealNormForm.exists_ideal_norm_form
#check TenthDiscriminant.IdealNormForm.actual_ideal_off_axis_count
#print axioms TenthDiscriminant.IdealNormForm.exists_ideal_norm_form
#print axioms TenthDiscriminant.IdealNormForm.actual_ideal_off_axis_count
#audit_namespace TenthDiscriminant.IdealNormForm
