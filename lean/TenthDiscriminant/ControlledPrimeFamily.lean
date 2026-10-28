import TenthDiscriminant.ActualPrimeAxis
import TenthDiscriminant.ResidueMultiplicity

/-! Controlled counts and four prime lifts now refer to the same specified ideal family. -/
open scoped NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.ControlledPrimeFamily
open ClassFiber ResidueMultiplicity IdealCoordinates PrincipalBasis
set_option autoImplicit false
noncomputable section

theorem fixed_family_four_lifts (K : Type*) [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰) (hGood : FamilyGood J)
    (p : Nat) (hp : 0<p) (f g : 𝓞 K →+* ZMod p) (hne : RingHom.ker f≠RingHom.ker g) :
    ∃ U : Finset (ClassGroup (𝓞 K) × 𝓞 K), U.card=4 ∧ ∀ x ∈ U, PointAt J p x := by
  classical
  have hall : ∀ C : ClassGroup (𝓞 K), ∀ I : (Ideal (𝓞 K))⁰, ClassGroup.mk0 I=C →
      ∃ z : 𝓞 K, NormLift I (J C) z := by
    intro C I hI
    apply lift_in_inverse_class K I (J C)
    rw [hI,(hGood C).1,inv_inv]
  let C := ClassGroup.mk0 (residueIdeal K p hp f)
  let C' := ClassGroup.mk0 (residueIdeal K p hp g)
  obtain ⟨z,hz⟩ := hall C (residueIdeal K p hp f) rfl
  obtain ⟨w,hw⟩ := hall C' (residueIdeal K p hp g) rfl
  have hnz : (Algebra.norm Int z).natAbs=p*Ideal.absNorm (J C : Ideal (𝓞 K)) := by
    simpa only [residueIdeal,residueKernel_absNorm K p f] using hz.2.2.2.1
  have hnw : (Algebra.norm Int w).natAbs=p*Ideal.absNorm (J C' : Ideal (𝓞 K)) := by
    simpa only [residueIdeal,residueKernel_absNorm K p g] using hw.2.2.2.1
  have hzn := negation_control K _ _ z hz
  have hwn := negation_control K _ _ w hw
  have ha : (C,z) ≠ (C,-z) := by
    intro he
    exact hz.1 (CharZero.eq_neg_self_iff.mp (congrArg Prod.snd he))
  have hb : (C',w) ≠ (C',-w) := by
    intro he
    exact hw.1 (CharZero.eq_neg_self_iff.mp (congrArg Prod.snd he))
  have hab := tagged_lifts_ne K J _ _ C C' z w hz hw hne
  have habn := tagged_lifts_ne K J _ _ C C' z (-w) hz hwn hne
  have hanb := tagged_lifts_ne K J _ _ C C' (-z) w hzn hw hne
  have hanbn := tagged_lifts_ne K J _ _ C C' (-z) (-w) hzn hwn hne
  let U : Finset (ClassGroup (𝓞 K) × 𝓞 K) := {(C,z),(C,-z),(C',w),(C',-w)}
  have hc : U.card=4 := by
    simp [U, Finset.card_insert_of_not_mem, ha, hb, hab, habn, hanb, hanbn]
  have hpnz : (Algebra.norm Int (-z)).natAbs=p*Ideal.absNorm (J C : Ideal (𝓞 K)) := by
    simpa only [residueIdeal,residueKernel_absNorm K p f] using hzn.2.2.2.1
  have hpnw : (Algebra.norm Int (-w)).natAbs=p*Ideal.absNorm (J C' : Ideal (𝓞 K)) := by
    simpa only [residueIdeal,residueKernel_absNorm K p g] using hwn.2.2.2.1
  refine ⟨U,hc,?_⟩
  intro x hx
  simp only [U, Finset.mem_insert, Finset.mem_singleton] at hx
  rcases hx with rfl | rfl | rfl | rfl
  · exact ⟨hz.1,hz.2.1,hnz⟩
  · exact ⟨hzn.1,hzn.2.1,hpnz⟩
  · exact ⟨hw.1,hw.2.1,hnw⟩
  · exact ⟨hwn.1,hwn.2.1,hpnw⟩

theorem fixed_family_odd_four (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) →
      (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) (hGood : FamilyGood J)
    (p : Nat) (hp : Admissible D p) :
    ∃ U : Finset (ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) ×
      𝓞 (QuadraticField (((D : Int)+1)/4))), U.card=4 ∧ ∀ x ∈ U, PointAt J p x := by
  letI : Fact p.Prime := ⟨hp.1⟩
  obtain ⟨z,hz⟩ := hp.2.2.2
  have hz2 : z^2=-(D : ZMod p) := by simpa only [pow_two] using hz.symm
  exact fixed_family_four_lifts _ J hGood p hp.1.pos
    (actualResidueMap D p hsq hp.2.1 z hz2)
    (actualResidueMap D p hsq hp.2.1 (-z) (by simpa only [neg_sq] using hz2))
    (actual_residue_pair_ne D p hsq hp.2.1 hp.2.2.1 z hz2)

theorem fixed_family_finite (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (J : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) →
      (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) (hGood : FamilyGood J)
    (P : Finset Nat) (hP : ∀ p ∈ P, Admissible D p) :
    ∃ U : Finset (ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) ×
      𝓞 (QuadraticField (((D : Int)+1)/4))), U.card=4*P.card ∧
      ∀ x ∈ U, ∃ p ∈ P, PointAt J p x := by
  exact aggregate_points _ J P (fun p hp => fixed_family_odd_four D hsq J hGood p (hP p hp))

def ClassCountData (D : Nat) [Fact ((D : Int)%4=3)]
    (C : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))))
    (J : (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰) : Prop :=
  ∃ e : Basis (Fin 2) Int (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))),
    ∃ a b c : Int, FormData D J e a b c ∧
      a≤(Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4)))) : Int) ∧
      (C=1 → a=1) ∧
      ∀ (U : Finset (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))) (t : Nat),
        (∀ z ∈ U, PrimeNormalized J z) →
        (∀ z ∈ U, (Algebra.norm Int (z : 𝓞 (QuadraticField (((D : Int)+1)/4)))).natAbs ≤
          Ideal.absNorm (J : Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))*t) →
        (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt D+
          4*Real.sqrt (normBound (QuadraticField (((D : Int)+1)/4))*t/D)+(if C=1 then 0 else 2)

theorem controlled_family (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2) :
    ∃ J : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) →
      (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      FamilyGood J ∧ (∀ C, ClassGroup.mk0 (J C)=C ∧ ClassCountData D C (J C)) ∧
      ∀ (P : Finset Nat), (∀ p ∈ P, Admissible D p) →
        ∃ U : Finset (ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) ×
          𝓞 (QuadraticField (((D : Int)+1)/4))), U.card=4*P.card ∧
          ∀ x ∈ U, ∃ p ∈ P, PointAt J p x := by
  classical
  choose J hClass hBound hLift hData using
    (fun C => ActualPrimeAxis.controlled_class_prime_count D hsq h C)
  have hGood : FamilyGood J := by
    intro C
    exact ⟨(hClass C).trans (LeastNorm.self_inverse h C),hBound C⟩
  refine ⟨J,hGood,fun C => ⟨hClass C,hData C⟩,?_⟩
  intro P hP
  exact fixed_family_finite D hsq J hGood P hP

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
    (1 : ZMod 2)^2=-(7 : ZMod 2) ∧ (1 : ZMod 2)= -1 := ResidueMultiplicity.characteristic_two_control

theorem ramified_control :
    letI : Fact (((15 : Nat) : Int)%4=3) := ⟨by decide⟩
    actualResidueMap 15 3 fifteen_squarefree (by decide) 0 (by decide) =
      actualResidueMap 15 3 fifteen_squarefree (by decide) (-0) (by decide) :=
  ResidueMultiplicity.ramified_root_control
end
end TenthDiscriminant.ControlledPrimeFamily

#check TenthDiscriminant.ControlledPrimeFamily.fixed_family_four_lifts
#check TenthDiscriminant.ControlledPrimeFamily.fixed_family_odd_four
#check TenthDiscriminant.ControlledPrimeFamily.fixed_family_finite
#check TenthDiscriminant.ControlledPrimeFamily.controlled_family
#check TenthDiscriminant.ControlledPrimeFamily.empty_control
#check TenthDiscriminant.ControlledPrimeFamily.zero_modulus_control
#check TenthDiscriminant.ControlledPrimeFamily.characteristic_two_control
#check TenthDiscriminant.ControlledPrimeFamily.ramified_control
#print TenthDiscriminant.ControlledPrimeFamily.ClassCountData
#print TenthDiscriminant.ResidueMultiplicity.FamilyGood
#print TenthDiscriminant.ResidueMultiplicity.PointAt
#print TenthDiscriminant.ResidueMultiplicity.Admissible
#print axioms TenthDiscriminant.ControlledPrimeFamily.fixed_family_four_lifts
#print axioms TenthDiscriminant.ControlledPrimeFamily.controlled_family
#audit_namespace TenthDiscriminant.ControlledPrimeFamily
