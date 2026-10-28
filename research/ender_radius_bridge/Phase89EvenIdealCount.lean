import TenthDiscriminant

/-! The even maximal lattice has discriminant magnitude4d, not d. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.EvenIdealCount
open IdealBasisArithmetic IdealCoordinates
set_option autoImplicit false
noncomputable section

def integerBasis (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2) :
    Basis (Fin 2) Int (𝓞 (EvenQuadraticField d)) :=
  (evenOrderBasis d).map (evenOrderEquivRingOfIntegers d hsq hm).toAddEquiv.toIntLinearEquiv

def normQ (d : Nat) (x y : Int) : Int := x^2+(d : Int)*y^2

def cross (d : Nat) (s t u v : Int) : Int := 2*s*u+2*(d : Int)*t*v

theorem norm_in_integer_basis (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2) (x y : Int) :
    Algebra.norm Int (x • integerBasis d hsq hm 0+y • integerBasis d hsq hm 1)=normQ d x y := by
  simpa [integerBasis,Basis.map_apply,evenOrderBasis_zero,evenOrderBasis_one,
    Algebra.smul_def,map_add,map_mul,normQ] using evenOrder_ringOfIntegers_norm d x y

theorem norm_coordinates (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2) (z : 𝓞 (EvenQuadraticField d)) :
    Algebra.norm Int z=normQ d ((integerBasis d hsq hm).repr z 0)
      ((integerBasis d hsq hm).repr z 1) := by
  let e := integerBasis d hsq hm
  have he : (e.repr z 0) • e 0+(e.repr z 1) • e 1=z := by
    simpa only [Fin.sum_univ_two] using e.sum_repr z
  exact (congrArg (Algebra.norm Int) he).symm.trans (norm_in_integer_basis d hsq hm _ _)

theorem norm_nonneg (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2) (z : 𝓞 (EvenQuadraticField d)) :
    0≤Algebra.norm Int z := by
  rw [norm_coordinates d hsq hm]
  unfold normQ
  positivity

theorem norm_pos (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2) (z : 𝓞 (EvenQuadraticField d))
    (hz : z≠0) : 0<Algebra.norm Int z :=
  lt_of_le_of_ne (norm_nonneg d hsq hm z) (Ne.symm (Algebra.norm_ne_zero_iff.mpr hz))

theorem principal_transform (d : Nat) (s t u v x y : Int) :
    normQ d (x*s+y*u) (x*t+y*v)=
      x^2*normQ d s t+x*y*cross d s t u v+y^2*normQ d u v := by
  unfold normQ cross
  ring

theorem principal_discriminant (d : Nat) (s t u v : Int) :
    4*normQ d s t*normQ d u v-(cross d s t u v)^2=
      4*(d : Int)*(s*v-u*t)^2 := by
  unfold normQ cross
  ring

theorem normalized_form_of_basis (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField d)))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField d)))) :
    ∃ a b c : Int, 0<a ∧ 4*a*c-b^2=4*(d : Int) ∧
      ∀ x y : Int, Algebra.norm Int (combine e x y)=
        (Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField d))) : Int)*
          (a*x^2+b*x*y+c*y^2) := by
  let K := EvenQuadraticField d
  let v := integerBasis d hsq hm
  let n : Int := Ideal.absNorm (J : Ideal (𝓞 K))
  have hn : 0<n := by
    dsimp [n]
    exact_mod_cast Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors J)
  let s := v.repr (e 0 : 𝓞 K) 0
  let t := v.repr (e 0 : 𝓞 K) 1
  let u := v.repr (e 1 : 𝓞 K) 0
  let w := v.repr (e 1 : 𝓞 K) 1
  have hnorm (x y : Int) : Algebra.norm Int (combine e x y)=
      normQ d (x*s+y*u) (x*t+y*w) := by
    rw [norm_coordinates d hsq hm]
    rw [repr_combine K v (J : Ideal (𝓞 K)) e x y 0,
      repr_combine K v (J : Ideal (𝓞 K)) e x y 1]
  have hN0 : Algebra.norm Int (e 0 : 𝓞 K)=normQ d s t := by
    simpa only [combine,Int.cast_one,Int.cast_zero,one_mul,zero_mul,add_zero,
      zero_add,mul_zero,mul_one] using hnorm 1 0
  have hN1 : Algebra.norm Int (e 1 : 𝓞 K)=normQ d u w := by
    simpa only [combine,Int.cast_one,Int.cast_zero,one_mul,zero_mul,add_zero,
      zero_add,mul_zero,mul_one] using hnorm 0 1
  have hNs : Algebra.norm Int ((e 0 : 𝓞 K)+(e 1 : 𝓞 K))=
      normQ d (s+u) (t+w) := by
    simpa only [combine,Int.cast_one,one_mul,mul_one] using hnorm 1 1
  have hd0 : n∣Algebra.norm Int (e 0 : 𝓞 K) := Ideal.absNorm_dvd_norm_of_mem (e 0).property
  have hd1 : n∣Algebra.norm Int (e 1 : 𝓞 K) := Ideal.absNorm_dvd_norm_of_mem (e 1).property
  have hds : n∣Algebra.norm Int ((e 0 : 𝓞 K)+(e 1 : 𝓞 K)) :=
    Ideal.absNorm_dvd_norm_of_mem (e 0+e 1).property
  have hdB := dvd_sub (dvd_sub hds hd0) hd1
  obtain ⟨a,ha⟩ := hd0
  obtain ⟨c,hc⟩ := hd1
  obtain ⟨b,hb⟩ := hdB
  have hA : normQ d s t=n*a := hN0.symm.trans ha
  have hC : normQ d u w=n*c := hN1.symm.trans hc
  have hB : cross d s t u w=n*b := by
    calc
      _ = normQ d (s+u) (t+w)-normQ d s t-
          normQ d u w := by unfold cross normQ; ring
      _ = _ := by rw [← hNs,← hN0,← hN1]; exact hb
  have hindex := ideal_basis_index K v (J : Ideal (𝓞 K)) e
  change (s*w-u*t).natAbs=Ideal.absNorm (J : Ideal (𝓞 K)) at hindex
  have hdet2 : (s*w-u*t)^2=n^2 := by
    have hh : |s*w-u*t|^2=n^2 := by
      simpa only [Int.natCast_natAbs,n] using
        congrArg (fun m : Nat => (m : Int)^2) hindex
    exact (sq_abs (s*w-u*t)).symm.trans hh
  have hraw := principal_discriminant d s t u w
  rw [hA,hB,hC,hdet2] at hraw
  have hdisc : 4*a*c-b^2=4*(d : Int) := by
    apply mul_left_cancel₀ (pow_ne_zero 2 (ne_of_gt hn))
    linear_combination hraw
  have hz : (e 0 : 𝓞 K)≠0 := by
    intro he
    exact e.ne_zero 0 (Subtype.ext he)
  have hp := norm_pos d hsq hm (e 0 : 𝓞 K) hz
  have hapos : 0<a := by nlinarith [ha]
  refine ⟨a,b,c,hapos,hdisc,?_⟩
  intro x y
  rw [hnorm,principal_transform,hA,hB,hC]
  ring

theorem actual_ideal_norm_form (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField d)))⁰) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField d))),
      ∃ a b c : Int, (0<a ∧ 4*a*c-b^2=4*(d : Int) ∧
      ∀ x y : Int, Algebra.norm Int (combine e x y)=
        (Ideal.absNorm (J : (Ideal (𝓞 (EvenQuadraticField d)))) : Int)*(a*x^2+b*x*y+c*y^2)) := by
  have hJ : (J : Ideal (𝓞 (EvenQuadraticField d)))≠⊥ := by
    simpa only [Submodule.zero_eq_bot] using (mem_nonZeroDivisors_iff_ne_zero.mp J.prop)
  let e := Ideal.selfBasis (integerBasis d hsq hm)
    (J : Ideal (𝓞 (EvenQuadraticField d))) hJ
  obtain ⟨a,b,c,ha,hd,hn⟩ := normalized_form_of_basis d hsq hm J e
  exact ⟨e,a,b,c,ha,hd,hn⟩

theorem count_for_actual_form (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField d)))⁰)
    (e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField d))))
    (a b c : Int) (hf : (0<a ∧ 4*a*c-b^2=4*(d : Int) ∧
      ∀ x y : Int, Algebra.norm Int (combine e x y)=
        (Ideal.absNorm (J : (Ideal (𝓞 (EvenQuadraticField d)))) : Int)*(a*x^2+b*x*y+c*y^2)))
    (U : Finset (J : Ideal (𝓞 (EvenQuadraticField d)))) (t : Nat)
    (hN : ∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField d))).natAbs ≤
      Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField d)))*t)
    (hy : ∀ z ∈ U, (coordinates e z).2≠0) :
    (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt (4*d)+4*Real.sqrt ((a : Real)*t/(4*d)) := by
  classical
  let V := U.image (coordinates e)
  have hcard : V.card=U.card := Finset.card_image_of_injective U (coordinates_injective _ _ e)
  have hD : 0<4*d := by have hd := (Fact.out : 0<d); omega
  have hdR : 4*(a : Real)*c-(b : Real)^2=((4*d : Nat) : Real) := by exact_mod_cast hf.2.1
  have hQ : ∀ p ∈ V, (a : Real)*(p.1 : Real)^2+(b : Real)*(p.1 : Real)*(p.2 : Real)+
      (c : Real)*(p.2 : Real)^2 ≤ (t : Real) := by
    intro p hp
    obtain ⟨z,hz,rfl⟩ := Finset.mem_image.mp hp
    have hn := hN z hz
    have hnn := norm_nonneg d hsq hm (z : 𝓞 (EvenQuadraticField d))
    have hi : (((Algebra.norm Int (z : 𝓞 (EvenQuadraticField d))).natAbs : Nat) : Int) ≤
        ((Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField d)))*t : Nat) : Int) := by
      exact_mod_cast hn
    rw [Int.natCast_natAbs,abs_of_nonneg hnn,Nat.cast_mul] at hi
    have he := hf.2.2 (coordinates e z).1 (coordinates e z).2
    rw [combine_coordinates _ _ e z] at he
    rw [he] at hi
    have hnJ : (0 : Int)<Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField d))) := by
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
  simpa only [hcard,hdR,Nat.cast_mul,Nat.cast_ofNat] using hb

/-- The basis and form precede every finite set and threshold. -/
theorem actual_ideal_form_and_count (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hm : (d : Int)%4=1 ∨ (d : Int)%4=2)
    (J : (Ideal (𝓞 (EvenQuadraticField d)))⁰) :
    ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField d))),
      ∃ a b c : Int, (0<a ∧ 4*a*c-b^2=4*(d : Int) ∧
      ∀ x y : Int, Algebra.norm Int (combine e x y)=
        (Ideal.absNorm (J : (Ideal (𝓞 (EvenQuadraticField d)))) : Int)*(a*x^2+b*x*y+c*y^2)) ∧
        ∀ (U : Finset (J : Ideal (𝓞 (EvenQuadraticField d)))) (t : Nat),
          (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField d))).natAbs ≤
            Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField d)))*t) →
          (∀ z ∈ U, (coordinates e z).2≠0) →
          (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt (4*d)+4*Real.sqrt ((a : Real)*t/(4*d)) := by
  obtain ⟨e,a,b,c,hf⟩ := actual_ideal_norm_form d hsq hm J
  exact ⟨e,a,b,c,hf,fun U t hN hy => count_for_actual_form d hsq hm J e a b c hf U t hN hy⟩

private instance onePositive : Fact (0<(1 : Nat)) := ⟨by decide⟩
private instance twoPositive : Fact (0<(2 : Nat)) := ⟨by decide⟩
private theorem oneSq : Squarefree (1 : Nat) := by norm_num
private theorem twoSq : Squarefree (2 : Nat) := (by norm_num : Nat.Prime 2).squarefree

theorem gaussian_control (x y : Int) :
    Algebra.norm Int (x • integerBasis 1 oneSq (by decide) 0+
      y • integerBasis 1 oneSq (by decide) 1)=x^2+y^2 := by
  simpa [normQ] using norm_in_integer_basis 1 oneSq (by decide) x y

theorem two_shear_control (x y : Int) :
    Algebra.norm Int (x • integerBasis 2 twoSq (by decide) 0+
      y • (integerBasis 2 twoSq (by decide) 0+integerBasis 2 twoSq (by decide) 1))=
      x^2+2*x*y+3*y^2 ∧ 4*(1 : Int)*3-2^2=8 := by
  constructor
  · have he : x • integerBasis 2 twoSq (by decide) 0+
        y • (integerBasis 2 twoSq (by decide) 0+integerBasis 2 twoSq (by decide) 1)=
        (x+y) • integerBasis 2 twoSq (by decide) 0+y • integerBasis 2 twoSq (by decide) 1 := by
      simp only [smul_add,add_smul]; abel
    rw [he,norm_in_integer_basis]
    unfold normQ
    ring
  · norm_num

theorem actual_discriminant_control :
    NumberField.discr (EvenQuadraticField 2)= -8 ∧
      (NumberField.discr (EvenQuadraticField 2)).natAbs≠2 := by
  have he := even_actual_discr 2 twoSq (by decide)
  norm_num at he ⊢
  exact ⟨he,by rw [he]; norm_num⟩

theorem zero_threshold_control (d : Nat) [Fact (0<d)]
    (J : Ideal (𝓞 (EvenQuadraticField d))) (e : Basis (Fin 2) Int J) (U : Finset J)
    (hN : ∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField d))).natAbs≤0)
    (hy : ∀ z ∈ U, (coordinates e z).2≠0) : U=∅ :=
  IdealCoordinates.zero_threshold_control _ J e U hN hy
end
end TenthDiscriminant.EvenIdealCount

#check TenthDiscriminant.EvenIdealCount.norm_in_integer_basis
#check TenthDiscriminant.EvenIdealCount.norm_coordinates
#check TenthDiscriminant.EvenIdealCount.norm_nonneg
#check TenthDiscriminant.EvenIdealCount.norm_pos
#check TenthDiscriminant.EvenIdealCount.principal_transform
#check TenthDiscriminant.EvenIdealCount.principal_discriminant
#check TenthDiscriminant.EvenIdealCount.normalized_form_of_basis
#check TenthDiscriminant.EvenIdealCount.actual_ideal_norm_form
#check TenthDiscriminant.EvenIdealCount.count_for_actual_form
#check TenthDiscriminant.EvenIdealCount.actual_ideal_form_and_count
#check TenthDiscriminant.EvenIdealCount.gaussian_control
#check TenthDiscriminant.EvenIdealCount.two_shear_control
#check TenthDiscriminant.EvenIdealCount.actual_discriminant_control
#check TenthDiscriminant.EvenIdealCount.zero_threshold_control
#print TenthDiscriminant.EvenIdealCount.integerBasis
#print TenthDiscriminant.EvenIdealCount.normQ
#print TenthDiscriminant.EvenIdealCount.cross
#print axioms TenthDiscriminant.EvenIdealCount.actual_ideal_form_and_count
#audit_namespace TenthDiscriminant.EvenIdealCount

open Lean Elab Command

elab "#phase89_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE89_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE89_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE89_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE89_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE89_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE89_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"






#phase89_inputs TenthDiscriminant.EvenIdealCount.actual_ideal_form_and_count
