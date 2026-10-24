import TenthDiscriminant.SmallPositiveClassNumber
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.RingTheory.Ideal.Norm.AbsNorm

/-! Small ideal norms, with no class-number-one hypothesis. -/
namespace TenthDiscriminant
open NumberField
open scoped NumberField nonZeroDivisors
set_option autoImplicit false
noncomputable section

theorem ideal_prime_norm_residue_map (K : Type*) [Field K] [NumberField K]
    (I : Ideal (𝓞 K)) (p : Nat) (hp : p.Prime) (hn : Ideal.absNorm I=p) :
    Nonempty ((𝓞 K) →+* ZMod p) := by
  letI : Finite ((𝓞 K) ⧸ I) := (Ideal.absNorm_ne_zero_iff I).mp (by rw [hn]; exact hp.ne_zero)
  letI := Fintype.ofFinite ((𝓞 K) ⧸ I)
  have hcard : Fintype.card ((𝓞 K) ⧸ I)=p := by
    simpa only [Ideal.absNorm_apply, Submodule.cardQuot_apply, Nat.card_eq_fintype_card] using hn
  let e := ZMod.ringEquivOfPrime ((𝓞 K) ⧸ I) hp hcard
  exact ⟨e.symm.toRingHom.comp (Ideal.Quotient.mk I)⟩

theorem quadratic_scalar_ideal_norm (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2) (p : Nat) :
    Ideal.absNorm (Ideal.span ({(p : 𝓞 K)} : Set (𝓞 K)))=p^2 := by
  have hn := Algebra.norm_algebraMap_of_basis (NumberField.RingOfIntegers.basis K) (p : Int)
  rw [← Module.finrank_eq_card_basis (NumberField.RingOfIntegers.basis K),
    NumberField.RingOfIntegers.rank, hdegree] at hn
  have hn' : Algebra.norm Int (p : 𝓞 K)=(p : Int)^2 := by simpa using hn
  rw [Ideal.absNorm_span_singleton, hn']
  rw [Int.natAbs_pow]
  rfl

theorem ideal_eq_of_le_of_equal_absNorm (K : Type*) [Field K] [NumberField K]
    (I J : Ideal (𝓞 K)) (hJI : J≤I) (hn : Ideal.absNorm I=Ideal.absNorm J)
    (hpos : 0<Ideal.absNorm I) : I=J := by
  obtain ⟨L,hL⟩ := Ideal.dvd_iff_le.mpr hJI
  have hprod : Ideal.absNorm I*Ideal.absNorm L=Ideal.absNorm I*1 := by
    rw [← map_mul, ← hL, ← hn, mul_one]
  have hLone : Ideal.absNorm L=1 := Nat.eq_of_mul_eq_mul_left hpos hprod
  have hLtop := Ideal.absNorm_eq_one_iff.mp hLone
  simpa [hLtop] using hL.symm

private theorem small_prime_square_arithmetic (n p : Nat)
    (hn : 1<n) (hn8 : n≤8) (h2 : n≠2) (h3 : n≠3) (h5 : n≠5) (h7 : n≠7)
    (hp : p.Prime) (hpn : p∣n) (hnp : n∣p^2) : n=4 ∧ p=2 := by
  have hp2 := hp.two_le
  have hp8 : p≤8 := le_trans (Nat.le_of_dvd (by omega) hpn) hn8
  interval_cases n <;> interval_cases p <;> norm_num at *

/-- The ideal (2) of norm four is allowed. Forbidding all nonunit small
ideals would incorrectly discard a legitimate principal ideal. -/
theorem quadratic_small_ideal_principal (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2)
    (hno : ∀ (J : Ideal (𝓞 K)) (p : Nat), p ∈ ([2,3,5,7] : List Nat) → Ideal.absNorm J≠p)
    (I : Ideal (𝓞 K)) (hpos : 0<Ideal.absNorm I) (hsmall : Ideal.absNorm I<9) :
    I.IsPrincipal := by
  by_cases hunit : Ideal.absNorm I=1
  · rw [Ideal.absNorm_eq_one_iff.mp hunit]
    infer_instance
  have hnotunit : ¬IsUnit I := by
    intro h
    exact hunit (by rw [Ideal.isUnit_iff.mp h, Ideal.absNorm_top])
  have hirr : Irreducible I := irreducible_iff.mpr ⟨hnotunit, by
    intro J L hfac
    by_cases hj : IsUnit J
    · exact Or.inl hj
    by_cases hl : IsUnit L
    · exact Or.inr hl
    have hprod : Ideal.absNorm J*Ideal.absNorm L=Ideal.absNorm I := by rw [← map_mul, ← hfac]
    have hjpos : 0<Ideal.absNorm J := by
      by_contra h
      have hz : Ideal.absNorm J=0 := by omega
      rw [hz,zero_mul] at hprod
      omega
    have hlpos : 0<Ideal.absNorm L := by
      by_contra h
      have hz : Ideal.absNorm L=0 := by omega
      rw [hz,mul_zero] at hprod
      omega
    have hj1 : Ideal.absNorm J≠1 := fun h => hj (Ideal.isUnit_iff.mpr (Ideal.absNorm_eq_one_iff.mp h))
    have hl1 : Ideal.absNorm L≠1 := fun h => hl (Ideal.isUnit_iff.mpr (Ideal.absNorm_eq_one_iff.mp h))
    have hj2 := hno J 2 (by simp)
    have hj3 := hno J 3 (by simp)
    have hl2 := hno L 2 (by simp)
    have hl3 := hno L 3 (by simp)
    have hj4 : 4≤Ideal.absNorm J := by omega
    have hl4 : 4≤Ideal.absNorm L := by omega
    have h16 := Nat.mul_le_mul hj4 hl4
    omega⟩
  letI : I.IsPrime := Ideal.isPrime_of_prime (UniqueFactorizationMonoid.irreducible_iff_prime.mp hirr)
  have hIbot : I≠⊥ := by
    intro h
    rw [h,Ideal.absNorm_bot] at hpos
    omega
  letI : I.IsMaximal := (inferInstance : I.IsPrime).isMaximal hIbot
  letI : Field ((𝓞 K) ⧸ I) := Ideal.Quotient.field I
  letI : Finite ((𝓞 K) ⧸ I) := (Ideal.absNorm_ne_zero_iff I).mp (by omega)
  letI := Fintype.ofFinite ((𝓞 K) ⧸ I)
  have hcard : Fintype.card ((𝓞 K) ⧸ I)=Ideal.absNorm I := by
    simp only [Ideal.absNorm_apply, Submodule.cardQuot_apply, Nat.card_eq_fintype_card]
  obtain ⟨p,hchar,_e,hp,_hpow⟩ := FiniteField.card' ((𝓞 K) ⧸ I)
  letI := hchar
  have hpzero : (p : (𝓞 K) ⧸ I)=0 := (CharP.cast_eq_zero_iff _ p p).2 dvd_rfl
  have hpn : p∣Ideal.absNorm I := (CharP.cast_eq_zero_iff ((𝓞 K) ⧸ I) p _).mp (by
    rw [← hcard]
    exact Nat.cast_card_eq_zero _)
  have hpmem : (p : 𝓞 K) ∈ I := by
    apply Ideal.Quotient.eq_zero_iff_mem.mp
    simpa only [map_natCast] using hpzero
  have hle : Ideal.span ({(p : 𝓞 K)} : Set (𝓞 K))≤I :=
    (Ideal.span_singleton_le_iff_mem I).mpr hpmem
  have hnp : Ideal.absNorm I∣p^2 := by
    simpa only [quadratic_scalar_ideal_norm K hdegree p] using Ideal.absNorm_dvd_absNorm_of_le hle
  have harith := small_prime_square_arithmetic (Ideal.absNorm I) p (by omega) (by omega)
    (hno I 2 (by simp)) (hno I 3 (by simp)) (hno I 5 (by simp)) (hno I 7 (by simp)) hp hpn hnp
  have heq : I=Ideal.span ({(p : 𝓞 K)} : Set (𝓞 K)) :=
    ideal_eq_of_le_of_equal_absNorm K _ _ hle (by
      rw [quadratic_scalar_ideal_norm K hdegree p,harith.1,harith.2]
      norm_num) hpos
  rw [heq]
  exact ⟨⟨(p : 𝓞 K),rfl⟩⟩

theorem quadratic_minkowski_bound_lt (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2) (N B : Nat)
    (hdiscr : (NumberField.discr K).natAbs≤N) (hB : 0<B) (hguard : 4*N<9*B^2) :
    (4/Real.pi)^NumberField.InfinitePlace.nrComplexPlaces K *
      (((Module.finrank Rat K).factorial : Real) /
        (Module.finrank Rat K : Real)^(Module.finrank Rat K) *
        Real.sqrt |(NumberField.discr K : Real)|) < (B : Real) := by
  have hrank := NumberField.InfinitePlace.card_add_two_mul_card_eq_rank K
  rw [hdegree] at hrank
  have hcases : NumberField.InfinitePlace.nrComplexPlaces K=0 ∨
      NumberField.InfinitePlace.nrComplexPlaces K=1 := by omega
  have hi : ((NumberField.discr K).natAbs : Int)≤(N : Int) := by exact_mod_cast hdiscr
  rw [Int.natCast_natAbs] at hi
  have hreal : ((|NumberField.discr K| : Int) : Real)≤(N : Real) := by exact_mod_cast hi
  rw [Int.cast_abs] at hreal
  have hBreal : 0<(B : Real) := by exact_mod_cast hB
  have hguardreal : 4*(N : Real)<9*(B : Real)^2 := by exact_mod_cast hguard
  let r : Real := Real.sqrt |(NumberField.discr K : Real)|
  have hr : 0≤r := Real.sqrt_nonneg _
  have hr2 : r^2=|(NumberField.discr K : Real)| := Real.sq_sqrt (abs_nonneg _)
  have hlinear : 2*r<3*(B : Real) :=
    (sq_lt_sq₀ (by positivity) (by positivity)).mp (by nlinarith)
  have hpi : 3*(B : Real)<(B : Real)*Real.pi := by
    simpa [mul_comm] using mul_lt_mul_of_pos_left Real.pi_gt_three hBreal
  have hdiv : 2*r/Real.pi<(B : Real) :=
    (div_lt_iff₀ Real.pi_pos).mpr (lt_trans hlinear hpi)
  rcases hcases with h | h
  · norm_num [hdegree,h]
    convert (show r/2<(B : Real) by linarith) using 1 <;> dsimp [r] <;> ring
  · norm_num [hdegree,h]
    convert hdiv using 1 <;> dsimp [r] <;> ring

/-- The only global input is the library's small ideal representative.
Local ideal principality is supplied explicitly, not assumed from h=1. -/
theorem quadratic_classNumber_one_of_small_ideals (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2) (N B : Nat)
    (hdiscr : (NumberField.discr K).natAbs≤N) (hB : 0<B) (hguard : 4*N<9*B^2)
    (hprincipal : ∀ I : Ideal (𝓞 K), 0<Ideal.absNorm I → Ideal.absNorm I<B → I.IsPrincipal) :
    NumberField.classNumber K=1 := by
  rw [NumberField.classNumber,Fintype.card_eq_one_iff]
  refine ⟨1,fun C => ?_⟩
  obtain ⟨I,rfl,hI⟩ := NumberField.exists_ideal_in_class_of_norm_le C
  have hbound := quadratic_minkowski_bound_lt K hdegree N B hdiscr hB hguard
  have hlt : Ideal.absNorm I.1<B := Nat.cast_lt.mp (lt_of_le_of_lt
    (by simpa only [Int.cast_abs] using hI) hbound)
  rw [ClassGroup.mk0_eq_one_iff]
  exact hprincipal I.1 (Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors I)) hlt

theorem quadratic_classNumber_one_without_norm_two (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2) (hdiscr : (NumberField.discr K).natAbs≤19)
    (hno : ∀ I : Ideal (𝓞 K), Ideal.absNorm I≠2) : NumberField.classNumber K=1 := by
  apply quadratic_classNumber_one_of_small_ideals K hdegree 19 3 hdiscr (by decide) (by decide)
  intro I hpos hsmall
  have hn : Ideal.absNorm I=1 := by have h := hno I; omega
  rw [Ideal.absNorm_eq_one_iff.mp hn]
  infer_instance

theorem quadratic_classNumber_one_without_small_prime_norms (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2) (hdiscr : (NumberField.discr K).natAbs≤163)
    (hno : ∀ (I : Ideal (𝓞 K)) (p : Nat), p ∈ ([2,3,5,7] : List Nat) → Ideal.absNorm I≠p) :
    NumberField.classNumber K=1 := by
  apply quadratic_classNumber_one_of_small_ideals K hdegree 163 9 hdiscr (by decide) (by decide)
  exact quadratic_small_ideal_principal K hdegree hno

end
end TenthDiscriminant
