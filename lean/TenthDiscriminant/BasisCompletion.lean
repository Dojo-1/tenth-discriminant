import TenthDiscriminant.IdealCoordinates
import TenthDiscriminant.AxiomAudit
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.Data.Int.GCD

/-! An existing Mathlib lattice automorphism completes a primitive element. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.BasisCompletion
open IdealBasisArithmetic IdealCoordinates
set_option autoImplicit false
noncomputable section

theorem primitive_completion {M : Type*} [AddCommGroup M] [Module Int M]
    (e : Basis (Fin 2) Int M) (z : M)
    (hg : Int.gcd (e.repr z 0) (e.repr z 1)=1) :
    ∃ e' : Basis (Fin 2) Int M, e' 0=z := by
  let u := e.repr z 0
  let v := e.repr z 1
  let A := Int.gcdA u v
  let B := Int.gcdB u v
  change Int.gcd u v=1 at hg
  have hbez : u*A+v*B=1 := by
    simpa only [hg] using (Int.gcd_eq_gcd_ab u v).symm
  let T : Matrix (Fin 2) (Fin 2) Int := !![u,-B;v,A]
  have hdet : T.det=1 := by
    rw [Matrix.det_fin_two]
    change u*A-(-B)*v=1
    nlinarith [hbez]
  have hu : IsUnit T.det := by rw [hdet]; exact isUnit_one
  let L := Matrix.toLinearEquiv e T hu
  refine ⟨e.map L,?_⟩
  change Matrix.toLin e e T (e 0)=z
  rw [Matrix.toLin_self,Fin.sum_univ_two]
  simpa [T,u,v,Fin.sum_univ_two,int_smul_eq_zsmul] using e.sum_repr z

theorem actual_form_of_primitive_bound (D : Nat) [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (z : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (hg : Int.gcd (e.repr z 0) (e.repr z 1)=1)
    (hzN : (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
      Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))^2) :
    ∃ e' : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      e' 0=z ∧ ∃ a b c : Int, FormData D J e' a b c ∧
        a ≤ (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) := by
  obtain ⟨e',he⟩ := primitive_completion e z hg
  obtain ⟨a,b,c,ha,hd,hform⟩ := normalized_form_of_basis D hsq J e'
  have hf : FormData D J e' a b c := ⟨ha,hd,hform⟩
  have hN : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_iff_mem_nonZeroDivisors.mpr J.prop)
  have hb : ((Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs : Int) ≤
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)^2 := by
    exact_mod_cast hzN
  rw [Int.natCast_natAbs] at hb
  have hzle := (le_abs_self (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4))))).trans hb
  have hnorm : Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))=
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int)*a := by
    simpa [combine,he] using hform 1 0
  have haN : a≤(Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) := by
    apply (mul_le_mul_left hN).mp
    simpa only [hnorm,pow_two] using hzle
  exact ⟨e',he,a,b,c,hf,haN⟩

theorem two_three_control :
    ∃ e : Basis (Fin 2) Int (Fin 2 → Int), e 0=![2,3] := by
  apply primitive_completion (Pi.basisFun Int (Fin 2)) ![2,3]
  norm_num

theorem zero_guard {M : Type*} [AddCommGroup M] [Module Int M]
    (e : Basis (Fin 2) Int M) : ¬ Int.gcd (e.repr (0 : M) 0) (e.repr (0 : M) 1)=1 := by
  simp

theorem nonprimitive_guard : ¬ Int.gcd (4 : Int) 6=1 := by norm_num

theorem first_vector_control {M : Type*} [AddCommGroup M] [Module Int M]
    (e : Basis (Fin 2) Int M) :
    Int.gcd (e.repr (e 0) 0) (e.repr (e 0) 1)=1 ∧
      ∃ e' : Basis (Fin 2) Int M, e' 0=e 0 := by
  have hg : Int.gcd (e.repr (e 0) 0) (e.repr (e 0) 1)=1 := by simp
  exact ⟨hg,primitive_completion e (e 0) hg⟩
end
end TenthDiscriminant.BasisCompletion

#check TenthDiscriminant.BasisCompletion.primitive_completion
#check TenthDiscriminant.BasisCompletion.actual_form_of_primitive_bound
#check TenthDiscriminant.BasisCompletion.two_three_control
#check TenthDiscriminant.BasisCompletion.zero_guard
#check TenthDiscriminant.BasisCompletion.nonprimitive_guard
#check TenthDiscriminant.BasisCompletion.first_vector_control
#print TenthDiscriminant.IdealCoordinates.FormData
#print axioms TenthDiscriminant.BasisCompletion.primitive_completion
#print axioms TenthDiscriminant.BasisCompletion.actual_form_of_primitive_bound
#audit_namespace TenthDiscriminant.BasisCompletion
