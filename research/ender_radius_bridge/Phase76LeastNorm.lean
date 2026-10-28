import TenthDiscriminant
import Mathlib.Data.Int.GCD
import Mathlib.Data.Nat.Find
import Mathlib.GroupTheory.OrderOfElement

/-! Least actual norm makes primitivity independent of the chosen basis. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.LeastNorm
open IdealBasisArithmetic
set_option autoImplicit false
noncomputable section

theorem norm_zsmul (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (d : Int) (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) :
    Algebra.norm Int (d • z)=d^2*Algebra.norm Int z := by
  rw [norm_coordinates D hsq,norm_coordinates D hsq z]
  simp only [map_smul,Finsupp.smul_apply,smul_eq_mul,principalNorm]
  ring

theorem primitive_of_minimal (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))
    (z : J) (hz : z≠0)
    (hmin : ∀ w : J, w≠0 →
      (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
      (Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs)
    (e : Basis (Fin 2) Int J) : Int.gcd (e.repr z 0) (e.repr z 1)=1 := by
  let m := e.repr z 0
  let n := e.repr z 1
  have hg : 0<Int.gcd m n := by
    by_contra hh
    have hh := Int.gcd_eq_zero_iff.mp (Nat.eq_zero_of_not_pos hh)
    apply hz
    apply e.repr.injective
    ext i
    fin_cases i
    · simpa [m] using hh.1
    · simpa [n] using hh.2
  obtain ⟨d,u,v,hd,huv,hm,hn⟩ := Int.exists_gcd_one' hg
  let w : J := u • e 0+v • e 1
  have hzw : z=(d : Int) • w := by
    calc
      z=m • e 0+n • e 1 := by
        symm
        simpa only [m,n,Fin.sum_univ_two] using e.sum_repr z
      _=(d : Int) • w := by
        rw [hm,hn]
        simp [w,smul_add,mul_smul,smul_smul,mul_comm]
  have hw : w≠0 := by
    intro hw
    rw [hw,smul_zero] at hzw
    exact hz hzw
  have hwcoe : (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))≠0 := by
    intro he
    exact hw (Subtype.ext he)
  have hp : 0<(Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs :=
    Int.natAbs_pos.mpr (Algebra.norm_ne_zero_iff.mpr hwcoe)
  let L := (Submodule.subtype J).restrictScalars Int
  have hcoe : (((d : Int) • w : J) : 𝓞 (QuadraticField (((D : Int)+1)/4)))=
      (d : Int) • (w : 𝓞 (QuadraticField (((D : Int)+1)/4))) := L.map_smul (d : Int) w
  have hscale : (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs=
      d^2*(Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs := by
    rw [hzw,hcoe,norm_zsmul D hsq]
    simp [Int.natAbs_mul,Int.natAbs_pow]
  have hle : d^2*(Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
      1*(Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs := by
    rw [one_mul,← hscale]
    exact hmin w hw
  have hd2 : d^2≤1 := Nat.le_of_mul_le_mul_right hle hp
  have hd1 : d=1 := by nlinarith
  change Int.gcd m n=1
  rw [hm,hn,hd1]
  simpa using huv

theorem least_primitive_vector (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) (z0 : J) (hz0 : z0≠0) :
    ∃ z : J, z≠0 ∧
      (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
        (Algebra.norm Int (z0 : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ∧
      (∀ w : J, w≠0 →
        (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
        (Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs) ∧
      ∀ e : Basis (Fin 2) Int J, Int.gcd (e.repr z 0) (e.repr z 1)=1 := by
  classical
  let P : Nat → Prop := fun n => ∃ z : J, z≠0 ∧
    (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs=n
  have hex : ∃ n, P n := ⟨_,z0,hz0,rfl⟩
  obtain ⟨z,hz,hn⟩ := Nat.find_spec hex
  have hmin : ∀ w : J, w≠0 →
      (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
      (Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs := by
    intro w hw
    rw [hn]
    exact Nat.find_min' hex ⟨w,hw,rfl⟩
  exact ⟨z,hz,hmin z0 hz0,hmin,fun e => primitive_of_minimal D hsq J z hz hmin e⟩

theorem self_inverse {G : Type*} [Group G] [Fintype G] (h : Fintype.card G≤2) (g : G) :
    g=g⁻¹ := by
  have hp : 0<Fintype.card G := Fintype.card_pos
  have hh : Fintype.card G=1 ∨ Fintype.card G=2 := by omega
  have hg : g^Fintype.card G=1 := pow_card_eq_one
  apply eq_inv_iff_mul_eq_one.mpr
  rcases hh with hh | hh
  · rw [hh,pow_one] at hg; simp [hg]
  · simpa only [hh,pow_two] using hg

theorem bounded_class_least_primitive (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4)))) :
    ∃ J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Real) ≤
        ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) ∧
      ∃ z : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))), z≠0 ∧
        (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
          Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))^2 ∧
        (∀ w : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))), w≠0 →
          (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
          (Algebra.norm Int (w : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs) ∧
        ∀ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
          Int.gcd (e.repr z 0) (e.repr z 1)=1 := by
  obtain ⟨J,hJ,hb⟩ := NumberField.exists_ideal_in_class_of_norm_le C
  obtain ⟨v,hv⟩ := ClassFiber.lift_in_inverse_class _ J J (self_inverse h (ClassGroup.mk0 J))
  let z0 : (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) := ⟨v,hv.2.1⟩
  have hz0 : z0≠0 := fun he => hv.1 (congrArg Subtype.val he)
  obtain ⟨z,hz,hzN,hmin,hprim⟩ := least_primitive_vector D hsq J z0 hz0
  have h0 : (Algebra.norm Int (z0 : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs=
      Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))^2 := by
    simpa only [z0,pow_two] using hv.2.2.2.1
  exact ⟨J,hJ,hb,z,hz,hzN.trans_eq h0,hmin,hprim⟩

theorem zero_control (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) : Algebra.norm Int ((0 : Int) • z)=0 := by
  rw [norm_zsmul D hsq]; ring

theorem neg_two_control (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (z : 𝓞 (QuadraticField (((D : Int)+1)/4))) :
    Algebra.norm Int ((-2 : Int) • z)=4*Algebra.norm Int z := by
  rw [norm_zsmul D hsq]; ring

theorem nonprimitive_control : Int.gcd (4 : Int) 6=2 ∧
    (4 : Int)^2+6^2=52 ∧ (2 : Int)^2+3^2=13 ∧ (13 : Int)<52 := by norm_num

private instance sevenMod : Fact (((7 : Nat) : Int)%4=3) := ⟨by decide⟩
private instance sevenCondition : Fact (0<4*(2 : Int)-1) := ⟨by decide⟩

theorem unit_control (e : Basis (Fin 2) Int (1 : Ideal (𝓞 (QuadraticField 2)))) :
    let z : (1 : Ideal (𝓞 (QuadraticField 2))) := ⟨1,by simp⟩
    Int.gcd (e.repr z 0) (e.repr z 1)=1 := by
  let z : (1 : Ideal (𝓞 (QuadraticField 2))) := ⟨1,by simp⟩
  apply primitive_of_minimal 7 (by exact (by norm_num : Nat.Prime 7).squarefree) 1 z
    (by intro he; have hh := congrArg Subtype.val he; exact one_ne_zero hh) ?_ e
  intro w hw
  have hwcoe : w.val≠0 := fun he => hw (Subtype.ext he)
  have hp : 0<(Algebra.norm Int w.val).natAbs :=
    Int.natAbs_pos.mpr (Algebra.norm_ne_zero_iff.mpr hwcoe)
  change (Algebra.norm Int (1 : 𝓞 (QuadraticField 2))).natAbs ≤ (Algebra.norm Int w.val).natAbs
  simpa only [map_one,Int.natAbs_one] using hp
end
end TenthDiscriminant.LeastNorm

#check TenthDiscriminant.LeastNorm.norm_zsmul
#check TenthDiscriminant.LeastNorm.primitive_of_minimal
#check TenthDiscriminant.LeastNorm.least_primitive_vector
#check TenthDiscriminant.LeastNorm.self_inverse
#check TenthDiscriminant.LeastNorm.bounded_class_least_primitive
#check TenthDiscriminant.LeastNorm.zero_control
#check TenthDiscriminant.LeastNorm.neg_two_control
#check TenthDiscriminant.LeastNorm.nonprimitive_control
#check TenthDiscriminant.LeastNorm.unit_control
#print axioms TenthDiscriminant.LeastNorm.norm_zsmul
#print axioms TenthDiscriminant.LeastNorm.primitive_of_minimal
#print axioms TenthDiscriminant.LeastNorm.bounded_class_least_primitive
#audit_namespace TenthDiscriminant.LeastNorm
