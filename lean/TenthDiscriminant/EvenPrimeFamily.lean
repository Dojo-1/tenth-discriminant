import TenthDiscriminant.EvenPrimeAxis
import TenthDiscriminant.ControlledPrimeFamily
import TenthDiscriminant.EvenMaximalOrder

/-! Actual even residue kernels, four lifts and counts on one controlled family. -/
open scoped NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.EvenPrimeFamily
open Polynomial ClassFiber ResidueMultiplicity IdealCoordinates PrincipalBasis EvenControlledClass
set_option autoImplicit false
noncomputable section

def orderResidueMap (D p : Nat) [Fact p.Prime] (z : ZMod p)
    (hz : z^2=-(D : ZMod p)) : AdjoinRoot (evenOrderPoly D) →+* ZMod p :=
  AdjoinRoot.lift (Int.castRingHom (ZMod p)) z (by
    change (X^2+C (D : Int)).eval₂ (Int.castRingHom (ZMod p)) z=0
    simp only [eval₂_add,eval₂_pow,eval₂_X,eval₂_C]
    change z^2+((D : Int) : ZMod p)=0
    simpa only [Int.cast_natCast] using (eq_neg_iff_add_eq_zero.mp hz))

theorem orderResidueMap_root (D p : Nat) [Fact p.Prime] (z : ZMod p)
    (hz : z^2=-(D : ZMod p)) :
    orderResidueMap D p z hz (AdjoinRoot.root (evenOrderPoly D))=z := by
  simp [orderResidueMap,AdjoinRoot.lift_root]

def actualResidueMap (D p : Nat) [Fact (0<D)] [Fact p.Prime]
    (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (z : ZMod p) (hz : z^2=-(D : ZMod p)) : 𝓞 (EvenQuadraticField D) →+* ZMod p :=
  (orderResidueMap D p z hz).comp (evenOrderEquivRingOfIntegers D hsq hm).symm.toRingHom

theorem actualResidueMap_generator (D p : Nat) [Fact (0<D)] [Fact p.Prime]
    (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (z : ZMod p) (hz : z^2=-(D : ZMod p)) :
    actualResidueMap D p hsq hm z hz
      ((evenOrderEquivRingOfIntegers D hsq hm) (AdjoinRoot.root (evenOrderPoly D)))=z := by
  change orderResidueMap D p z hz ((evenOrderEquivRingOfIntegers D hsq hm).symm
    ((evenOrderEquivRingOfIntegers D hsq hm) (AdjoinRoot.root (evenOrderPoly D))))=z
  rw [(evenOrderEquivRingOfIntegers D hsq hm).symm_apply_apply]
  exact orderResidueMap_root D p z hz

theorem actualResidueMap_surjective (D p : Nat) [Fact (0<D)] [Fact p.Prime]
    (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (z : ZMod p) (hz : z^2=-(D : ZMod p)) :
    Function.Surjective (actualResidueMap D p hsq hm z hz) := ZMod.ringHom_surjective _

theorem actualResidueMap_norm (D p : Nat) [Fact (0<D)] [Fact p.Prime]
    (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (z : ZMod p) (hz : z^2=-(D : ZMod p)) :
    Ideal.absNorm (RingHom.ker (actualResidueMap D p hsq hm z hz))=p :=
  residueKernel_absNorm _ p _

theorem actual_residue_pair_ne (D p : Nat) [Fact p.Prime] [Fact (0<D)]
    (hDsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2) (hp2 : p≠2) (hnd : ¬ p ∣ D)
    (z : ZMod p) (hz : z^2=-(D : ZMod p)) :
    RingHom.ker (actualResidueMap D p hDsq hm z hz) ≠
      RingHom.ker (actualResidueMap D p hDsq hm (-z) (by simpa only [neg_sq] using hz)) := by
  have hD0 : (D : ZMod p) ≠ 0 := (ZMod.natCast_zmod_eq_zero_iff_dvd D p).not.mpr hnd
  have hz0 : z≠0 := by
    intro he
    have : -(D : ZMod p)=0 := by simpa [he] using hz.symm
    exact hD0 (neg_eq_zero.mp this)
  have hzn : z ≠ -z := by
    intro he
    have hs : z+z=0 := eq_neg_iff_add_eq_zero.mp he
    have hm : (2 : ZMod p)*z=0 := by simpa only [two_mul] using hs
    have h2 : (2 : ZMod p) ≠ 0 := by
      intro he2
      have hd : p ∣ 2 := (ZMod.natCast_zmod_eq_zero_iff_dvd 2 p).mp he2
      rcases (Nat.dvd_prime Nat.prime_two).mp hd with h | h
      · exact (Fact.out : p.Prime).ne_one h
      · exact hp2 h
    exact (mul_ne_zero h2 hz0) hm
  apply kernels_ne_of_value_ne _ p _ _
    ((evenOrderEquivRingOfIntegers D hDsq hm) (AdjoinRoot.root (evenOrderPoly D)))
  intro he
  have hplus := actualResidueMap_generator D p hDsq hm z hz
  have hminus := actualResidueMap_generator D p hDsq hm (-z) (by simpa only [neg_sq] using hz)
  rw [he] at hplus
  exact hzn (hplus.symm.trans hminus)

theorem fixed_family_even_four (D : Nat) [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : ClassGroup (𝓞 (EvenQuadraticField D)) →
      (Ideal (𝓞 (EvenQuadraticField D)))⁰) (hGood : FamilyGood J)
    (p : Nat) (hp : Admissible D p) :
    ∃ U : Finset (ClassGroup (𝓞 (EvenQuadraticField D)) ×
      𝓞 (EvenQuadraticField D)), U.card=4 ∧ ∀ x ∈ U, PointAt J p x := by
  letI : Fact p.Prime := ⟨hp.1⟩
  obtain ⟨z,hz⟩ := hp.2.2.2
  have hz2 : z^2=-(D : ZMod p) := by simpa only [pow_two] using hz.symm
  exact ControlledPrimeFamily.fixed_family_four_lifts _ J hGood p hp.1.pos
    (actualResidueMap D p hsq hm z hz2)
    (actualResidueMap D p hsq hm (-z) (by simpa only [neg_sq] using hz2))
    (actual_residue_pair_ne D p hsq hm hp.2.1 hp.2.2.1 z hz2)

theorem fixed_family_finite (D : Nat) [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (J : ClassGroup (𝓞 (EvenQuadraticField D)) →
      (Ideal (𝓞 (EvenQuadraticField D)))⁰) (hGood : FamilyGood J)
    (P : Finset Nat) (hP : ∀ p ∈ P, Admissible D p) :
    ∃ U : Finset (ClassGroup (𝓞 (EvenQuadraticField D)) ×
      𝓞 (EvenQuadraticField D)), U.card=4*P.card ∧
      ∀ x ∈ U, ∃ p ∈ P, PointAt J p x := by
  exact aggregate_points _ J P (fun p hp => fixed_family_even_four D hsq hm J hGood p (hP p hp))

def ClassCountData (D : Nat) [Fact (0<D)]
    (C : ClassGroup (𝓞 (EvenQuadraticField D)))
    (J : (Ideal (𝓞 (EvenQuadraticField D)))⁰) : Prop :=
  ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (EvenQuadraticField D))),
    ∃ a b c : Int, FormData D J e a b c ∧
      a≤(Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D))) : Int) ∧
      (C=1 → a=1) ∧
      ∀ (U : Finset (J : Ideal (𝓞 (EvenQuadraticField D)))) (t : Nat),
        (∀ z ∈ U, PrimeNormalized J z) →
        (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (EvenQuadraticField D))).natAbs ≤
          Ideal.absNorm (J : Ideal (𝓞 (EvenQuadraticField D)))*t) →
        (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt (4*D)+
          4*Real.sqrt (normBound (EvenQuadraticField D)*t/(4*D))+(if C=1 then 0 else 2)

theorem controlled_family (D : Nat) [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2) :
    ∃ J : ClassGroup (𝓞 (EvenQuadraticField D)) →
      (Ideal (𝓞 (EvenQuadraticField D)))⁰,
      FamilyGood J ∧ (∀ C, ClassGroup.mk0 (J C)=C ∧ ClassCountData D C (J C)) ∧
      ∀ (P : Finset Nat), (∀ p ∈ P, Admissible D p) →
        ∃ U : Finset (ClassGroup (𝓞 (EvenQuadraticField D)) ×
          𝓞 (EvenQuadraticField D)), U.card=4*P.card ∧
          ∀ x ∈ U, ∃ p ∈ P, PointAt J p x := by
  classical
  choose J hClass hBound hLift hData using
    (fun C => EvenPrimeAxis.controlled_class_prime_count D hsq hm h C)
  have hGood : FamilyGood J := by
    intro C
    exact ⟨(hClass C).trans (LeastNorm.self_inverse h C),hBound C⟩
  refine ⟨J,hGood,fun C => ⟨hClass C,hData C⟩,?_⟩
  intro P hP
  exact fixed_family_finite D hsq hm J hGood P hP

theorem empty_control (K : Type*) [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰) :
    ∃ U : Finset (ClassGroup (𝓞 K) × 𝓞 K), U.card=0 ∧
      ∀ x ∈ U, ∃ p ∈ (∅ : Finset Nat), PointAt J p x := by
  obtain ⟨U,hU,hu⟩ := aggregate_points K J ∅ (by simp)
  exact ⟨U,by simpa using hU,hu⟩

theorem zero_modulus_control (K : Type*) [Field K] [NumberField K]
    (f : 𝓞 K →+* ZMod 0) :
    Ideal.absNorm (RingHom.ker f)=0 ∧ RingHom.ker f ∉ (Ideal (𝓞 K))⁰ :=
  ClassFiber.zero_modulus_control K f

theorem characteristic_two_control :
    (1 : ZMod 2)^2=-(1 : ZMod 2) ∧ (1 : ZMod 2)= -1 := by decide

private instance onePositive : Fact (0<(1 : Nat)) := ⟨by decide⟩
private instance fivePositive : Fact (0<(5 : Nat)) := ⟨by decide⟩
private instance fivePrime : Fact (Nat.Prime 5) := ⟨by decide⟩

theorem gaussian_pair_control :
    RingHom.ker (actualResidueMap 1 5 (by norm_num) (by decide) 2 (by decide)) ≠
      RingHom.ker (actualResidueMap 1 5 (by norm_num) (by decide) (-2) (by decide)) := by
  exact actual_residue_pair_ne 1 5 (by norm_num) (by decide) (by decide) (by decide) 2 (by decide)

theorem ramified_control :
    actualResidueMap 5 5 (by exact (by norm_num : Nat.Prime 5).squarefree) (by decide) 0 (by decide) =
      actualResidueMap 5 5 (by exact (by norm_num : Nat.Prime 5).squarefree) (by decide) (-0) (by decide) := by
  simp only [neg_zero]
end
end TenthDiscriminant.EvenPrimeFamily

#check TenthDiscriminant.EvenPrimeFamily.orderResidueMap_root
#check TenthDiscriminant.EvenPrimeFamily.actualResidueMap_generator
#check TenthDiscriminant.EvenPrimeFamily.actualResidueMap_surjective
#check TenthDiscriminant.EvenPrimeFamily.actualResidueMap_norm
#check TenthDiscriminant.EvenPrimeFamily.actual_residue_pair_ne
#check TenthDiscriminant.EvenPrimeFamily.fixed_family_even_four
#check TenthDiscriminant.EvenPrimeFamily.fixed_family_finite
#check TenthDiscriminant.EvenPrimeFamily.controlled_family
#check TenthDiscriminant.EvenPrimeFamily.empty_control
#check TenthDiscriminant.EvenPrimeFamily.zero_modulus_control
#check TenthDiscriminant.EvenPrimeFamily.characteristic_two_control
#check TenthDiscriminant.EvenPrimeFamily.gaussian_pair_control
#check TenthDiscriminant.EvenPrimeFamily.ramified_control
#print TenthDiscriminant.EvenPrimeFamily.orderResidueMap
#print TenthDiscriminant.EvenPrimeFamily.actualResidueMap
#print TenthDiscriminant.EvenPrimeFamily.ClassCountData
#print axioms TenthDiscriminant.EvenPrimeFamily.controlled_family
#audit_namespace TenthDiscriminant.EvenPrimeFamily

