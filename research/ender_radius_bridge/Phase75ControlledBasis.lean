import TenthDiscriminant
import Mathlib.Data.Int.GCD
import Mathlib.GroupTheory.OrderOfElement

/-! Primitive division and a Bezout inverse control an actual ideal basis. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.ControlledBasis
open IdealBasisArithmetic IdealCoordinates
set_option autoImplicit false
noncomputable section

def bezoutEquiv (u v A B : Int) (h : u*A+v*B=1) :
    (Fin 2 → Int) ≃ₗ[Int] (Fin 2 → Int) where
  toFun x := ![u*x 0-B*x 1,v*x 0+A*x 1]
  invFun y := ![A*y 0+B*y 1,-v*y 0+u*y 1]
  left_inv x := by
    ext i
    fin_cases i
    · change A*(u*x 0-B*x 1)+B*(v*x 0+A*x 1)=x 0
      calc
        _=(u*A+v*B)*x 0 := by ring
        _=x 0 := by rw [h]; ring
    · change -v*(u*x 0-B*x 1)+u*(v*x 0+A*x 1)=x 1
      calc
        _=(u*A+v*B)*x 1 := by ring
        _=x 1 := by rw [h]; ring
  right_inv x := by
    ext i
    fin_cases i
    · change u*(A*x 0+B*x 1)-B*(-v*x 0+u*x 1)=x 0
      calc
        _=(u*A+v*B)*x 0 := by ring
        _=x 0 := by rw [h]; ring
    · change v*(A*x 0+B*x 1)+A*(-v*x 0+u*x 1)=x 1
      calc
        _=(u*A+v*B)*x 1 := by ring
        _=x 1 := by rw [h]; ring
  map_add' x y := by ext i; fin_cases i <;> simp <;> ring
  map_smul' c x := by ext i; fin_cases i <;> simp <;> ring

theorem primitive_basis {M : Type*} [AddCommGroup M] [Module Int M]
    (e : Basis (Fin 2) Int M) (u v : Int) (hg : Int.gcd u v=1) :
    ∃ e' : Basis (Fin 2) Int M, e' 0=u • e 0+v • e 1 := by
  let A := Int.gcdA u v
  let B := Int.gcdB u v
  have h : u*A+v*B=1 := by
    simpa only [hg,Int.cast_one] using (Int.gcd_eq_gcd_ab u v).symm
  let T := bezoutEquiv u v A B h
  let e' := e.map ((e.equivFun.trans T).trans e.equivFun.symm)
  refine ⟨e',?_⟩
  simp [e',T,Basis.map_apply,LinearEquiv.trans_apply,
    Basis.equivFun_symm_apply,Fin.sum_univ_two,bezoutEquiv,Basis.equivFun_apply]

theorem quadratic_scaling (a b c u v d : Int) :
    a*(u*d)^2+b*(u*d)*(v*d)+c*(v*d)^2=
      d^2*(a*u^2+b*u*v+c*v^2) := by ring

theorem controlled_basis_of_norm_square (D : Nat) [Fact ((D : Int)%4=3)]
    (hsq : Squarefree D)
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))
    (hz : z≠0) (hzJ : z ∈ (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))))
    (hzN : (Algebra.norm Int z).natAbs =
      Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))^2) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
      ∃ a b c : Int, FormData D J e a b c ∧
        a ≤ (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) := by
  classical
  obtain ⟨e,a,b,c,hf⟩ := actual_ideal_norm_form D hsq J
  let zz : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := ⟨z,hzJ⟩
  let m := e.repr zz 0
  let n := e.repr zz 1
  have hg : 0 < Int.gcd m n := by
    by_contra hh
    have hh := Int.gcd_eq_zero_iff.mp (Nat.eq_zero_of_not_pos hh)
    have he : zz=0 := by
      apply e.repr.injective
      ext i
      fin_cases i
      · simpa [m] using hh.1
      · simpa [n] using hh.2
    exact hz (congrArg Subtype.val he)
  obtain ⟨d,u,v,hd,huv,hm,hn⟩ := Int.exists_gcd_one' hg
  obtain ⟨e',he0⟩ := primitive_basis e u v huv
  obtain ⟨a',b',c',hf'⟩ := normalized_form_of_basis D hsq J e'
  let N := Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))
  have hN : (0 : Int)<N := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_iff_mem_nonZeroDivisors.mpr J.prop)
  have hzNorm : Algebra.norm Int z=(N : Int)^2 := by
    calc
      _=|(Algebra.norm Int z)| := (abs_of_pos (norm_pos D hsq z hz)).symm
      _=((Algebra.norm Int z).natAbs : Int) := Int.natCast_natAbs.symm
      _=(N : Int)^2 := by exact_mod_cast hzN
  have hcoord : combine e m n=z := combine_coordinates _ _ e zz
  have hq : a*m^2+b*m*n+c*n^2=(N : Int) := by
    apply mul_left_cancel₀ (ne_of_gt hN)
    calc
      _=Algebra.norm Int z := by rw [← hcoord]; exact (hf.2.2 m n).symm
      _=(N : Int)*(N : Int) := by rw [hzNorm]; ring
  have hw : combine e u v=(e' 0 : 𝓞 (QuadraticField (((D : Int)+1)/4))) := by
    rw [he0]
    simp [combine,Algebra.smul_def,algebraMap_int_eq]
  have heNorm : Algebra.norm Int (e' 0 : 𝓞 (QuadraticField (((D : Int)+1)/4)))=(N : Int)*a' := by
    simpa [combine] using hf'.2.2 1 0
  have ha' : a'=a*u^2+b*u*v+c*v^2 := by
    apply mul_left_cancel₀ (ne_of_gt hN)
    calc
      _=Algebra.norm Int (e' 0 : 𝓞 (QuadraticField (((D : Int)+1)/4))) := heNorm.symm
      _=(N : Int)*(a*u^2+b*u*v+c*v^2) := by rw [← hw]; exact hf.2.2 u v
  have heq : (N : Int)=(d : Int)^2*a' := by
    rw [ha',← quadratic_scaling a b c u v d,← hm,← hn]
    exact hq.symm
  have hd1 : (1 : Int)≤d := by exact_mod_cast hd
  have hd2 : (1 : Int)≤(d : Int)^2 := by nlinarith
  refine ⟨e',a',b',c',hf',?_⟩
  change a'≤(N : Int)
  rw [heq]
  exact le_mul_of_one_le_left (le_of_lt hf'.1) hd2

theorem controlled_class_basis (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) ≤ 2)
    (C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4)))) :
    ∃ J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Real) ≤
        ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) ∧
      ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
        ∃ a b c : Int, FormData D J e a b c ∧
          a ≤ (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) := by
  obtain ⟨J,hJ,hb⟩ := NumberField.exists_ideal_in_class_of_norm_le C
  have hc : ClassGroup.mk0 J=(ClassGroup.mk0 J)⁻¹ := by
    have hp : 0 < NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) := Fintype.card_pos
    have hh : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1 ∨
        NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=2 := by omega
    have hg : (ClassGroup.mk0 J)^NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1 := pow_card_eq_one
    apply eq_inv_iff_mul_eq_one.mpr
    rcases hh with hh | hh
    · rw [hh,pow_one] at hg; simp [hg]
    · simpa only [hh,pow_two] using hg
  obtain ⟨z,hz⟩ := ClassFiber.lift_in_inverse_class _ J J hc
  have hzN : (Algebra.norm Int z).natAbs=Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))^2 := by
    simpa only [pow_two] using hz.2.2.2.1
  exact ⟨J,hJ,hb,controlled_basis_of_norm_square D hsq J z hz.1 hz.2.1 hzN⟩

theorem primitive_control : Int.gcd (2 : Int) 3=1 ∧ (2 : Int)*(-1)+3*1=1 := by norm_num

theorem division_control : (4 : Int)=2*2 ∧ (6 : Int)=3*2 ∧ Int.gcd (2 : Int) 3=1 := by norm_num

private instance sevenMod : Fact (((7 : Nat) : Int)%4=3) := ⟨by decide⟩
private instance sevenCondition : Fact (0<4*(2 : Int)-1) := ⟨by decide⟩

theorem unit_ideal_control :
    ∃ e : Basis (Fin 2) Int ((1 : (Ideal (𝓞 (QuadraticField 2)))⁰) : Ideal (𝓞 (QuadraticField 2))),
      ∃ a b c : Int, FormData 7 1 e a b c ∧ a≤1 := by
  simpa using controlled_basis_of_norm_square 7 (by norm_num : Squarefree (7 : Nat)) 1
    (1 : 𝓞 (QuadraticField 2)) one_ne_zero (by simp) (by simp)

theorem shear_control (k : Int) : principalNorm 7 1 k=1+k+2*k^2 := by
  simp [principalNorm]
end
end TenthDiscriminant.ControlledBasis

#check TenthDiscriminant.ControlledBasis.primitive_basis
#check TenthDiscriminant.ControlledBasis.quadratic_scaling
#check TenthDiscriminant.ControlledBasis.controlled_basis_of_norm_square
#check TenthDiscriminant.ControlledBasis.controlled_class_basis
#check TenthDiscriminant.ControlledBasis.primitive_control
#check TenthDiscriminant.ControlledBasis.division_control
#check TenthDiscriminant.ControlledBasis.unit_ideal_control
#check TenthDiscriminant.ControlledBasis.shear_control
#print TenthDiscriminant.ControlledBasis.bezoutEquiv
#print TenthDiscriminant.IdealCoordinates.FormData
#print TenthDiscriminant.ClassFiber.normBound
#print axioms TenthDiscriminant.ControlledBasis.controlled_basis_of_norm_square
#print axioms TenthDiscriminant.ControlledBasis.controlled_class_basis
#audit_namespace TenthDiscriminant.ControlledBasis
