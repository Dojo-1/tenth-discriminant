import TenthDiscriminant.ClassFiber
import TenthDiscriminant.ClassNumberInertBridge
import TenthDiscriminant.AxiomAudit

/-! Small arbitrary-basis arithmetic, separated from chosen Smith bases.
This helper does not construct a basis or compose a geometric point count. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.IdealBasisArithmetic
set_option autoImplicit false
noncomputable section

def integerBasis (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    Basis (Fin 2) Int (𝓞 (QuadraticField (((D : Int)+1)/4))) :=
  (halfOrderBasis D).map (halfOrderEquivRingOfIntegers D hsq).toAddEquiv.toIntLinearEquiv

def combine {K : Type*} [Field K] [NumberField K] {J : Ideal (𝓞 K)}
    (e : Basis (Fin 2) Int J) (x y : Int) : 𝓞 K :=
  (x : 𝓞 K)*(e 0 : 𝓞 K)+(y : 𝓞 K)*(e 1 : 𝓞 K)

def cross (D : Nat) (s t u v : Int) : Int :=
  2*s*u+s*v+t*u+2*(((D : Int)+1)/4)*t*v

theorem norm_in_integer_basis (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (x y : Int) :
    Algebra.norm Int (x • integerBasis D hsq 0+y • integerBasis D hsq 1)=
      principalNorm (D : Int) x y := by
  simpa [integerBasis,Basis.map_apply,halfOrderBasis_zero,halfOrderBasis_one,
    Algebra.smul_def,map_add,map_mul] using halfOrder_ringOfIntegers_norm D x y

theorem norm_coordinates (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) :
    Algebra.norm Int z=principalNorm (D : Int)
      ((integerBasis D hsq).repr z 0) ((integerBasis D hsq).repr z 1) := by
  let e := integerBasis D hsq
  have he : (e.repr z 0) • e 0+(e.repr z 1) • e 1=z := by
    simpa only [Fin.sum_univ_two] using e.sum_repr z
  exact (congrArg (Algebra.norm Int) he).symm.trans (norm_in_integer_basis D hsq _ _)

theorem norm_nonneg (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) : 0≤Algebra.norm Int z := by
  rw [norm_coordinates D hsq]
  exact principalNorm_nonneg D Fact.out _ _

theorem norm_pos (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) (hz : z≠0) : 0<Algebra.norm Int z :=
  lt_of_le_of_ne (norm_nonneg D hsq z) (Ne.symm (Algebra.norm_ne_zero_iff.mpr hz))

/-- No chosen basis is unfolded in this two-by-two determinant calculation. -/
theorem ideal_basis_index (K : Type*) [Field K] [NumberField K]
    (v : Basis (Fin 2) Int (𝓞 K)) (J : Ideal (𝓞 K)) (e : Basis (Fin 2) Int J) :
    ((v.repr (e 0 : 𝓞 K) 0)*(v.repr (e 1 : 𝓞 K) 1)-
      (v.repr (e 1 : 𝓞 K) 0)*(v.repr (e 0 : 𝓞 K) 1)).natAbs=Ideal.absNorm J := by
  have h := Ideal.natAbs_det_basis_change v J e
  rw [Basis.det_apply,Matrix.det_fin_two] at h
  exact h

theorem repr_combine (K : Type*) [Field K] [NumberField K]
    (v : Basis (Fin 2) Int (𝓞 K)) (J : Ideal (𝓞 K)) (e : Basis (Fin 2) Int J)
    (x y : Int) (i : Fin 2) :
    v.repr (combine e x y) i=x*v.repr (e 0 : 𝓞 K) i+y*v.repr (e 1 : 𝓞 K) i := by
  have he : combine e x y=x • (e 0 : 𝓞 K)+y • (e 1 : 𝓞 K) := by
    simp [combine,Algebra.smul_def,algebraMap_int_eq]
  rw [he,map_add,map_smul,map_smul]
  simp only [Finsupp.add_apply,Finsupp.smul_apply,smul_eq_mul]

theorem principal_transform (D : Nat) (s t u v x y : Int) :
    principalNorm (D : Int) (x*s+y*u) (x*t+y*v)=
      x^2*principalNorm (D : Int) s t+x*y*cross D s t u v+
        y^2*principalNorm (D : Int) u v := by
  unfold principalNorm cross
  ring

theorem principal_discriminant (D : Nat) [Fact ((D : Int)%4=3)] (s t u v : Int) :
    4*principalNorm (D : Int) s t*principalNorm (D : Int) u v-(cross D s t u v)^2=
      (D : Int)*(s*v-u*t)^2 := by
  have h := halfOrder_coefficient_identity D (Fact.out : (D : Int)%4=3)
  unfold principalNorm cross
  linear_combination (s*v-u*t)^2*h

theorem normalized_form_of_basis (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) :
    ∃ a b c : Int, 0<a ∧ 4*a*c-b^2=(D : Int) ∧
      ∀ x y : Int, Algebra.norm Int (combine e x y)=
        (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*
          (a*x^2+b*x*y+c*y^2) := by
  let K := QuadraticField (((D : Int)+1)/4)
  let v := integerBasis D hsq
  let n : Int := Ideal.absNorm (J : Ideal (𝓞 K))
  have hn : 0<n := by
    dsimp [n]
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
  let s := v.repr (e 0 : 𝓞 K) 0
  let t := v.repr (e 0 : 𝓞 K) 1
  let u := v.repr (e 1 : 𝓞 K) 0
  let w := v.repr (e 1 : 𝓞 K) 1
  have hnorm (x y : Int) : Algebra.norm Int (combine e x y)=
      principalNorm (D : Int) (x*s+y*u) (x*t+y*w) := by
    rw [norm_coordinates D hsq]
    rw [repr_combine K v (J : Ideal (𝓞 K)) e x y 0,
      repr_combine K v (J : Ideal (𝓞 K)) e x y 1]
  have hN0 : Algebra.norm Int (e 0 : 𝓞 K)=principalNorm (D : Int) s t := by
    simpa only [combine,Int.cast_one,Int.cast_zero,one_mul,zero_mul,add_zero,
      zero_add,mul_zero,mul_one] using hnorm 1 0
  have hN1 : Algebra.norm Int (e 1 : 𝓞 K)=principalNorm (D : Int) u w := by
    simpa only [combine,Int.cast_one,Int.cast_zero,one_mul,zero_mul,add_zero,
      zero_add,mul_zero,mul_one] using hnorm 0 1
  have hNs : Algebra.norm Int ((e 0 : 𝓞 K)+(e 1 : 𝓞 K))=
      principalNorm (D : Int) (s+u) (t+w) := by
    simpa only [combine,Int.cast_one,one_mul,mul_one] using hnorm 1 1
  have hd0 : n∣Algebra.norm Int (e 0 : 𝓞 K) := Ideal.absNorm_dvd_norm_of_mem (e 0).property
  have hd1 : n∣Algebra.norm Int (e 1 : 𝓞 K) := Ideal.absNorm_dvd_norm_of_mem (e 1).property
  have hds : n∣Algebra.norm Int ((e 0 : 𝓞 K)+(e 1 : 𝓞 K)) :=
    Ideal.absNorm_dvd_norm_of_mem (e 0+e 1).property
  have hdB := dvd_sub (dvd_sub hds hd0) hd1
  obtain ⟨a,ha⟩ := hd0
  obtain ⟨c,hc⟩ := hd1
  obtain ⟨b,hb⟩ := hdB
  have hA : principalNorm (D : Int) s t=n*a := hN0.symm.trans ha
  have hC : principalNorm (D : Int) u w=n*c := hN1.symm.trans hc
  have hB : cross D s t u w=n*b := by
    calc
      _ = principalNorm (D : Int) (s+u) (t+w)-principalNorm (D : Int) s t-
          principalNorm (D : Int) u w := by unfold cross principalNorm; ring
      _ = _ := by rw [← hNs,← hN0,← hN1]; exact hb
  have hindex := ideal_basis_index K v (J : Ideal (𝓞 K)) e
  change (s*w-u*t).natAbs=Ideal.absNorm (J : Ideal (𝓞 K)) at hindex
  have hdet2 : (s*w-u*t)^2=n^2 := by
    have hh : |s*w-u*t|^2=n^2 := by
      simpa only [Int.natCast_natAbs,n] using
        congrArg (fun m : Nat => (m : Int)^2) hindex
    exact (sq_abs (s*w-u*t)).symm.trans hh
  have hraw := principal_discriminant D s t u w
  rw [hA,hB,hC,hdet2] at hraw
  have hdisc : 4*a*c-b^2=(D : Int) := by
    apply mul_left_cancel₀ (pow_ne_zero 2 (ne_of_gt hn))
    linear_combination hraw
  have hz : (e 0 : 𝓞 K)≠0 := by
    intro he
    exact e.ne_zero 0 (Subtype.ext he)
  have hp := norm_pos D hsq (e 0 : 𝓞 K) hz
  have hapos : 0<a := by nlinarith [ha]
  refine ⟨a,b,c,hapos,hdisc,?_⟩
  intro x y
  rw [hnorm,principal_transform,hA,hB,hC]
  ring

private instance sevenCondition : Fact (0<4*(2 : Int)-1) := ⟨by decide⟩
private instance sevenMod : Fact (((7 : Nat) : Int)%4=3) := ⟨by decide⟩
private theorem sevenSq : Squarefree (7 : Nat) := (by norm_num : Nat.Prime 7).squarefree

theorem seven_ambient_control (x y : Int) :
    Algebra.norm Int (x • integerBasis 7 sevenSq 0+y • integerBasis 7 sevenSq 1)=x^2+x*y+2*y^2 := by
  simpa [principalNorm] using norm_in_integer_basis 7 sevenSq x y

theorem seven_shear_control (x y : Int) :
    Algebra.norm Int (x • integerBasis 7 sevenSq 0+y •
      (integerBasis 7 sevenSq 0+integerBasis 7 sevenSq 1))=x^2+3*x*y+4*y^2 ∧
      4*(1 : Int)*4-3^2=7 := by
  constructor
  · have he : x • integerBasis 7 sevenSq 0+y • (integerBasis 7 sevenSq 0+integerBasis 7 sevenSq 1)=
        (x+y) • integerBasis 7 sevenSq 0+y • integerBasis 7 sevenSq 1 := by
      simp only [smul_add,add_smul]; abel
    rw [he,seven_ambient_control]; ring
  · norm_num

theorem proper_ideal_control :
    Ideal.absNorm (Ideal.span ({(2 : 𝓞 (QuadraticField 2))} : Set (𝓞 (QuadraticField 2))))=4 := by
  rw [Ideal.absNorm_span_singleton]
  have hn := seven_ambient_control 2 0
  simpa [integerBasis,Basis.map_apply,halfOrderBasis_zero] using congrArg Int.natAbs hn

theorem proper_scalar_control (x y : Int) :
    Algebra.norm Int ((2*x) • integerBasis 7 sevenSq 0+(2*y) • integerBasis 7 sevenSq 1)=
      4*(x^2+x*y+2*y^2) := by rw [seven_ambient_control]; ring

theorem positivity_guard_control :
    4*(-1 : Int)*(-2)-1^2=7 ∧ (-1 : Int)*1^2+1*1*0+(-2)*0^2<0 := by norm_num
end
end TenthDiscriminant.IdealBasisArithmetic

#check TenthDiscriminant.IdealBasisArithmetic.normalized_form_of_basis
#print TenthDiscriminant.IdealBasisArithmetic.combine
#print axioms TenthDiscriminant.IdealBasisArithmetic.normalized_form_of_basis
#audit_namespace TenthDiscriminant.IdealBasisArithmetic
