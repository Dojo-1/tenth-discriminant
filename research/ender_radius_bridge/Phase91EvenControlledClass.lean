import TenthDiscriminant

/-! One controlled even ideal lattice serves each complete actual ideal class. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.EvenControlledClass
open IdealBasisArithmetic IdealCoordinates EvenIdealCount
set_option autoImplicit false
noncomputable section

def FormData (D : Nat) [Fact (0<D)]
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D)))) (a b c : Int) : Prop :=
  0<a ∧ 4*a*c-b^2=4*(D : Int) ∧
    ∀ x y : Int, Algebra.norm Int (combine e x y)=
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int)*(a*x^2+b*x*y+c*y^2)

theorem norm_zsmul (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (d : Int) (z : 𝓞 (EvenQuadraticField D)) :
    Algebra.norm Int (d • z)=d^2*Algebra.norm Int z := by
  rw [norm_coordinates D hsq hm,norm_coordinates D hsq hm z]
  simp only [map_smul,Finsupp.smul_apply,smul_eq_mul,EvenIdealCount.normQ]
  ring

theorem primitive_of_minimal (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : Ideal (𝓞 (EvenQuadraticField D)))
    (z : J) (hz : z≠0)
    (hmin : ∀ w : J, w≠0 →
      (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
      (Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs)
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
  obtain ⟨d,u,v,hd,huv,hmul,hn⟩ := Int.exists_gcd_one' hg
  let w : J := u • e 0+v • e 1
  have hzw : z=(d : Int) • w := by
    calc
      z=m • e 0+n • e 1 := by
        symm
        simpa only [m,n,Fin.sum_univ_two] using e.sum_repr z
      _=(d : Int) • w := by
        rw [hmul,hn]
        simp [w,smul_add,mul_smul,smul_smul,mul_comm]
  have hw : w≠0 := by
    intro hw
    rw [hw,smul_zero] at hzw
    exact hz hzw
  have hwcoe : (w : 𝓞 (EvenQuadraticField D))≠0 := by
    intro he
    exact hw (Subtype.ext he)
  have hp : 0<(Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs :=
    Int.natAbs_pos.mpr (Algebra.norm_ne_zero_iff.mpr hwcoe)
  let L := (Submodule.subtype J).restrictScalars Int
  have hcoe : (((d : Int) • w : J) : 𝓞 (EvenQuadraticField D))=
      (d : Int) • (w : 𝓞 (EvenQuadraticField D)) := L.map_smul (d : Int) w
  have hscale : (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs=
      d^2*(Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs := by
    rw [hzw,hcoe,norm_zsmul D hsq hm]
    simp [Int.natAbs_mul,Int.natAbs_pow]
  have hle : d^2*(Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs ≤
      1*(Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs := by
    rw [one_mul,← hscale]
    exact hmin w hw
  have hd2 : d^2≤1 := Nat.le_of_mul_le_mul_right hle hp
  have hd1 : d=1 := by nlinarith
  change Int.gcd m n=1
  rw [hmul,hn,hd1]
  simpa using huv

theorem least_primitive_vector (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : Ideal (𝓞 (EvenQuadraticField D))) (z0 : J) (hz0 : z0≠0) :
    ∃ z : J, z≠0 ∧
      (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
        (Algebra.norm Int (z0 : 𝓞 (EvenQuadraticField D))).natAbs ∧
      (∀ w : J, w≠0 →
        (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
        (Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs) ∧
      ∀ e : Basis (Fin 2) Int J, Int.gcd (e.repr z 0) (e.repr z 1)=1 := by
  classical
  let P : Nat → Prop := fun n => ∃ z : J, z≠0 ∧
    (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs=n
  have hex : ∃ n, P n := ⟨_,z0,hz0,rfl⟩
  obtain ⟨z,hz,hn⟩ := Nat.find_spec hex
  have hmin : ∀ w : J, w≠0 →
      (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
      (Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs := by
    intro w hw
    rw [hn]
    exact Nat.find_min' hex ⟨w,hw,rfl⟩
  exact ⟨z,hz,hmin z0 hz0,hmin,fun e => primitive_of_minimal D hsq hm J z hz hmin e⟩

theorem bounded_class_least_primitive (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (C : ClassGroup (𝓞 (EvenQuadraticField D))) :
    ∃ J : (Ideal (𝓞 (EvenQuadraticField D)))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Real) ≤
        ClassFiber.normBound (EvenQuadraticField D) ∧
      ∃ z : (J : Ideal (𝓞 (EvenQuadraticField D))), z≠0 ∧
        (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
          Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))^2 ∧
        (∀ w : (J : Ideal (𝓞 (EvenQuadraticField D))), w≠0 →
          (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
          (Algebra.norm Int (w : 𝓞 (EvenQuadraticField D))).natAbs) ∧
        ∀ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))),
          Int.gcd (e.repr z 0) (e.repr z 1)=1 := by
  obtain ⟨J,hJ,hb⟩ := NumberField.exists_ideal_in_class_of_norm_le C
  obtain ⟨v,hv⟩ := ClassFiber.lift_in_inverse_class _ J J (LeastNorm.self_inverse h (ClassGroup.mk0 J))
  let z0 : (J : Ideal (𝓞 (EvenQuadraticField D))) := ⟨v,hv.2.1⟩
  have hz0 : z0≠0 := fun he => hv.1 (congrArg Subtype.val he)
  obtain ⟨z,hz,hzN,hmin,hprim⟩ := least_primitive_vector D hsq hm J z0 hz0
  have h0 : (Algebra.norm Int (z0 : 𝓞 (EvenQuadraticField D))).natAbs=
      Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))^2 := by
    simpa only [z0,pow_two] using hv.2.2.2.1
  exact ⟨J,hJ,hb,z,hz,hzN.trans_eq h0,hmin,hprim⟩

theorem actual_form_of_primitive_bound (D : Nat) [Fact (0<D)]
    (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))))
    (z : (J : Ideal (𝓞 (EvenQuadraticField D))))
    (hg : Int.gcd (e.repr z 0) (e.repr z 1)=1)
    (hzN : (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
      Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))^2) :
    ∃ e' : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))),
      e' 0=z ∧ ∃ a b c : Int, FormData D J e' a b c ∧
        a ≤ (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) := by
  obtain ⟨e',he⟩ := BasisCompletion.primitive_completion e z hg
  obtain ⟨a,b,c,ha,hd,hform⟩ := normalized_form_of_basis D hsq hm J e'
  have hf : FormData D J e' a b c := ⟨ha,hd,hform⟩
  have hN : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) := by
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_iff_mem_nonZeroDivisors.mpr J.prop)
  have hb : ((Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs : Int) ≤
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int)^2 := by
    exact_mod_cast hzN
  rw [Int.natCast_natAbs] at hb
  have hzle := (le_abs_self (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D)))).trans hb
  have hnorm : Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))=
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int)*a := by
    simpa [combine,he] using hform 1 0
  have haN : a≤(Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) := by
    apply (mul_le_mul_left hN).mp
    simpa only [hnorm,pow_two] using hzle
  exact ⟨e',he,a,b,c,hf,haN⟩

theorem controlled_class_basis (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2)
    (C : ClassGroup (𝓞 (EvenQuadraticField D))) :
    ∃ J : (Ideal (𝓞 (EvenQuadraticField D)))⁰,
      ClassGroup.mk0 J=C ∧
      (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Real) ≤
        ClassFiber.normBound (EvenQuadraticField D) ∧
      ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))),
        ∃ a b c : Int, FormData D J e a b c ∧
          a ≤ (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) := by
  obtain ⟨J,hJ,hB,z,hz,hzN,hmin,hprim⟩ := bounded_class_least_primitive D hsq hm h C
  obtain ⟨e,a0,b0,c0,hf0⟩ := actual_ideal_norm_form D hsq hm J
  obtain ⟨e',he,a,b,c,hf,ha⟩ := actual_form_of_primitive_bound D hsq hm J e z (hprim e) hzN
  exact ⟨J,hJ,hB,e',a,b,c,hf,ha⟩

theorem controlled_class_form_and_count (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
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
          a ≤ (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) ∧
          (a : Real) ≤ ClassFiber.normBound (EvenQuadraticField D) ∧
          ∀ (U : Finset (J : Ideal (𝓞 (EvenQuadraticField D)))) (t : Nat),
            (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
              Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))*t) →
            (∀ z ∈ U, (coordinates e z).2≠0) →
            (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt (4*D)+
              4*Real.sqrt (ClassFiber.normBound (EvenQuadraticField D)*t/(4*D)) := by
  obtain ⟨J,hJ,hB,e,a,b,c,hf,ha⟩ := controlled_class_basis D hsq hm h C
  have hlift : ∀ I : (Ideal (𝓞 (EvenQuadraticField D)))⁰,
      ClassGroup.mk0 I=C → ∃ z : 𝓞 (EvenQuadraticField D), ClassFiber.NormLift I J z := by
    intro I hI
    apply ClassFiber.lift_in_inverse_class _ I J
    rw [hI,hJ]
    exact LeastNorm.self_inverse h C
  have haR : (a : Real)≤ClassFiber.normBound (EvenQuadraticField D) :=
    le_trans (by exact_mod_cast ha) hB
  refine ⟨J,hJ,hB,hlift,e,a,b,c,hf,ha,haR,?_⟩
  intro U t hN hy
  have hc := count_for_actual_form D hsq hm J e a b c hf U t hN hy
  have harg : (a : Real)*t/(4*D) ≤ ClassFiber.normBound (EvenQuadraticField D)*t/(4*D) :=
    div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_right haR (Nat.cast_nonneg t)) (by positivity)
  have hs := Real.sqrt_le_sqrt harg
  linarith

theorem zero_control (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (z : 𝓞 (EvenQuadraticField D)) : Algebra.norm Int ((0 : Int) • z)=0 := by
  rw [norm_zsmul D hsq hm]; ring

theorem neg_two_control (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (z : 𝓞 (EvenQuadraticField D)) :
    Algebra.norm Int ((-2 : Int) • z)=4*Algebra.norm Int z := by
  rw [norm_zsmul D hsq hm]; ring

theorem nonprimitive_control : Int.gcd (4 : Int) 6=2 ∧
    (4 : Int)^2+6^2=52 ∧ (2 : Int)^2+3^2=13 ∧ (13 : Int)<52 := by norm_num

private instance gaussianPositive : Fact (0<(1 : Nat)) := ⟨by decide⟩

theorem unit_control (e : Basis (Fin 2) Int (1 : Ideal (𝓞 (EvenQuadraticField 1)))) :
    let z : (1 : Ideal (𝓞 (EvenQuadraticField 1))) := ⟨1,by simp⟩
    Int.gcd (e.repr z 0) (e.repr z 1)=1 := by
  let z : (1 : Ideal (𝓞 (EvenQuadraticField 1))) := ⟨1,by simp⟩
  apply primitive_of_minimal 1 (by norm_num) (by decide) 1 z
    (by intro he; have hh := congrArg Subtype.val he; exact one_ne_zero hh) ?_ e
  intro w hw
  have hwcoe : w.val≠0 := fun he => hw (Subtype.ext he)
  have hp : 0<(Algebra.norm Int w.val).natAbs :=
    Int.natAbs_pos.mpr (Algebra.norm_ne_zero_iff.mpr hwcoe)
  change (Algebra.norm Int (1 : 𝓞 (EvenQuadraticField 1))).natAbs ≤ (Algebra.norm Int w.val).natAbs
  simpa only [map_one,Int.natAbs_one] using hp
end
end TenthDiscriminant.EvenControlledClass

#check TenthDiscriminant.EvenControlledClass.norm_zsmul
#check TenthDiscriminant.EvenControlledClass.primitive_of_minimal
#check TenthDiscriminant.EvenControlledClass.least_primitive_vector
#check TenthDiscriminant.EvenControlledClass.bounded_class_least_primitive
#check TenthDiscriminant.EvenControlledClass.actual_form_of_primitive_bound
#check TenthDiscriminant.EvenControlledClass.controlled_class_basis
#check TenthDiscriminant.EvenControlledClass.controlled_class_form_and_count
#check TenthDiscriminant.EvenControlledClass.zero_control
#check TenthDiscriminant.EvenControlledClass.neg_two_control
#check TenthDiscriminant.EvenControlledClass.nonprimitive_control
#check TenthDiscriminant.EvenControlledClass.unit_control
#print TenthDiscriminant.EvenControlledClass.FormData
#print axioms TenthDiscriminant.EvenControlledClass.controlled_class_form_and_count
#audit_namespace TenthDiscriminant.EvenControlledClass

open Lean Elab Command

elab "#phase91_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE91_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
    ``TenthDiscriminant.ellipse_primeMass_product_dvd,
    ``TenthDiscriminant.ellipse_primeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_log_le_hadamard,
    ``TenthDiscriminant.smallPrimeNormLifting_of_classNumber_one,
    ``TenthDiscriminant.smallPrime_nonsquare_of_classNumber_one,
    ``TenthDiscriminant.rectangularTraceGram_valuation_of_classNumber_one,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b,

    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff,
    ``TenthDiscriminant.known_nine_classNumber_one,
    ``TenthDiscriminant.phase36_all_fibers,
    ``TenthDiscriminant.classNumber_one_candidates_below_million,
    ``TenthDiscriminant.classNumber_one_iff_below_million,
    ``TenthDiscriminant.phase35_q0_translate,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_parameter_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b,
    ``TenthDiscriminant.FirstCertificate.rawPrimeMassLower_uniform,
    ``TenthDiscriminant.classNumber_one_of_field_equiv,
    ``TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two,
    ``TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound,
    ``TenthDiscriminant.ControlledClassCount.controlled_class_form_and_count]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE91_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE91_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE91_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE91_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE91_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"






#phase91_inputs TenthDiscriminant.EvenControlledClass.controlled_class_form_and_count
