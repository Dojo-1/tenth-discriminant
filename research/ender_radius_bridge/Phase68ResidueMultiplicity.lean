import TenthDiscriminant

/-! Actual residue pairs give four class-labelled norm representatives.
The labels retain distinct ideal lattices; no binary-form coordinates are assumed. -/
open scoped NumberField nonZeroDivisors
namespace TenthDiscriminant.ResidueMultiplicity
open ClassFiber
set_option autoImplicit false
noncomputable section

def FamilyGood {K : Type*} [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰) : Prop :=
  ∀ C, ClassGroup.mk0 (J C) = C⁻¹ ∧
    (Ideal.absNorm (J C : Ideal (𝓞 K)) : Real) ≤ normBound K

def PointAt {K : Type*} [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰) (p : Nat)
    (x : ClassGroup (𝓞 K) × 𝓞 K) : Prop :=
  x.2 ≠ 0 ∧ x.2 ∈ (J x.1 : Ideal (𝓞 K)) ∧
    (Algebra.norm Int x.2).natAbs = p*Ideal.absNorm (J x.1 : Ideal (𝓞 K))

theorem tagged_lifts_ne (K : Type*) [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰)
    (I I' : Ideal (𝓞 K)) (C C' : ClassGroup (𝓞 K)) (z w : 𝓞 K)
    (hz : NormLift I (J C : Ideal (𝓞 K)) z)
    (hw : NormLift I' (J C' : Ideal (𝓞 K)) w) (hne : I ≠ I') :
    (C,z) ≠ (C',w) := by
  intro he
  have hC : C=C' := congrArg Prod.fst he
  have hzw : z=w := congrArg Prod.snd he
  subst C'
  have hI : I'=I := hz.2.2.2.2 I' (by rw [← hw.2.2.1, ← hzw])
  exact hne hI.symm

/-- One family is chosen before all residue maps and all positive moduli. -/
theorem class_family_four_lifts (K : Type*) [Field K] [NumberField K] :
    ∃ J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰, FamilyGood J ∧
      ∀ (p : Nat) (hp : 0 < p) (f g : 𝓞 K →+* ZMod p),
        RingHom.ker f ≠ RingHom.ker g →
        ∃ U : Finset (ClassGroup (𝓞 K) × 𝓞 K), U.card=4 ∧
          ∀ x ∈ U, PointAt J p x := by
  classical
  choose J hclass hbound hall using (fun C : ClassGroup (𝓞 K) => residue_class_lifting K C)
  refine ⟨J, fun C => ⟨hclass C,hbound C⟩, ?_⟩
  intro p hp f g hne
  let C := ClassGroup.mk0 (residueIdeal K p hp f)
  let C' := ClassGroup.mk0 (residueIdeal K p hp g)
  obtain ⟨z,hz,hnz⟩ := hall C p hp f rfl
  obtain ⟨w,hw,hnw⟩ := hall C' p hp g rfl
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
    simpa only [residueKernel_absNorm K p f] using hzn.2.2.2.1
  have hpnw : (Algebra.norm Int (-w)).natAbs=p*Ideal.absNorm (J C' : Ideal (𝓞 K)) := by
    simpa only [residueKernel_absNorm K p g] using hwn.2.2.2.1
  refine ⟨U,hc,?_⟩
  intro x hx
  simp only [U, Finset.mem_insert, Finset.mem_singleton] at hx
  rcases hx with rfl | rfl | rfl | rfl
  · exact ⟨hz.1,hz.2.1,hnz⟩
  · exact ⟨hzn.1,hzn.2.1,hpnz⟩
  · exact ⟨hw.1,hw.2.1,hnw⟩
  · exact ⟨hwn.1,hwn.2.1,hpnw⟩

theorem kernels_ne_of_value_ne (K : Type*) [Field K] [NumberField K]
    (p : Nat) [Fact p.Prime] (f g : 𝓞 K →+* ZMod p) (w : 𝓞 K)
    (hval : f w ≠ g w) : RingHom.ker f ≠ RingHom.ker g := by
  let a : 𝓞 K := w - ((f w).val : 𝓞 K)
  have hf : f a=0 := by simp [a]
  have hg : g a≠0 := by
    simp only [a, map_sub, map_natCast, ZMod.natCast_zmod_val]
    exact sub_ne_zero.mpr hval.symm
  intro he
  have hm : a ∈ RingHom.ker f := hf
  have hmg : a ∈ RingHom.ker g := he ▸ hm
  exact hg hmg

def actualResidueMap (D p : Nat) [Fact p.Prime] [Fact ((D : Int)%4=3)]
    (hDsq : Squarefree D) (hp2 : p≠2) (z : ZMod p) (hz : z^2=-(D : ZMod p)) :
    𝓞 (QuadraticField (((D : Int)+1)/4)) →+* ZMod p :=
  (halfOrderResidueMap D p Fact.out hp2 z hz).comp
    (halfOrderEquivRingOfIntegers D hDsq).symm.toRingHom

theorem actualResidueMap_generator (D p : Nat) [Fact p.Prime] [Fact ((D : Int)%4=3)]
    (hDsq : Squarefree D) (hp2 : p≠2) (z : ZMod p) (hz : z^2=-(D : ZMod p)) :
    2*actualResidueMap D p hDsq hp2 z hz
      ((halfOrderEquivRingOfIntegers D hDsq) (AdjoinRoot.root (halfOrderPolynomial D)))-1=z := by
  change 2*halfOrderResidueMap D p Fact.out hp2 z hz
    ((halfOrderEquivRingOfIntegers D hDsq).symm
      ((halfOrderEquivRingOfIntegers D hDsq) (AdjoinRoot.root (halfOrderPolynomial D))))-1=z
  rw [(halfOrderEquivRingOfIntegers D hDsq).symm_apply_apply]
  exact halfOrderResidueMap_root_twice_sub_one D p Fact.out hp2 z hz

theorem actual_residue_pair_ne (D p : Nat) [Fact p.Prime] [Fact ((D : Int)%4=3)]
    (hDsq : Squarefree D) (hp2 : p≠2) (hnd : ¬ p ∣ D)
    (z : ZMod p) (hz : z^2=-(D : ZMod p)) :
    RingHom.ker (actualResidueMap D p hDsq hp2 z hz) ≠
      RingHom.ker (actualResidueMap D p hDsq hp2 (-z) (by simpa only [neg_sq] using hz)) := by
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
    ((halfOrderEquivRingOfIntegers D hDsq) (AdjoinRoot.root (halfOrderPolynomial D)))
  intro he
  have hplus := actualResidueMap_generator D p hDsq hp2 z hz
  have hminus := actualResidueMap_generator D p hDsq hp2 (-z) (by simpa only [neg_sq] using hz)
  rw [he] at hplus
  exact hzn (hplus.symm.trans hminus)

def Admissible (D p : Nat) : Prop :=
  p.Prime ∧ p≠2 ∧ ¬p∣D ∧ IsSquare (-(D : ZMod p))

theorem odd_square_family (D : Nat) [Fact ((D : Int)%4=3)] (hDsq : Squarefree D) :
    ∃ J : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) →
        (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      FamilyGood J ∧ ∀ p, Admissible D p →
        ∃ U : Finset (ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) ×
          𝓞 (QuadraticField (((D : Int)+1)/4))), U.card=4 ∧ ∀ x ∈ U, PointAt J p x := by
  obtain ⟨J,hJ,hall⟩ := class_family_four_lifts (QuadraticField (((D : Int)+1)/4))
  refine ⟨J,hJ,?_⟩
  intro p hp
  letI : Fact p.Prime := ⟨hp.1⟩
  obtain ⟨z,hz⟩ := hp.2.2.2
  have hz2 : z^2=-(D : ZMod p) := by simpa only [pow_two] using hz.symm
  exact hall p hp.1.pos (actualResidueMap D p hDsq hp.2.1 z hz2)
    (actualResidueMap D p hDsq hp.2.1 (-z) (by simpa only [neg_sq] using hz2))
    (actual_residue_pair_ne D p hDsq hp.2.1 hp.2.2.1 z hz2)

/-- Different primes cannot share a labelled norm representative. -/
theorem aggregate_points (K : Type*) [Field K] [NumberField K]
    (J : ClassGroup (𝓞 K) → (Ideal (𝓞 K))⁰) (P : Finset Nat)
    (hall : ∀ p ∈ P, ∃ V : Finset (ClassGroup (𝓞 K) × 𝓞 K),
      V.card=4 ∧ ∀ x ∈ V, PointAt J p x) :
    ∃ U : Finset (ClassGroup (𝓞 K) × 𝓞 K), U.card=4*P.card ∧
      ∀ x ∈ U, ∃ p ∈ P, PointAt J p x := by
  classical
  revert hall
  refine Finset.induction_on P ?_ ?_
  · intro hall
    exact ⟨∅,by simp,by simp⟩
  · intro p P hp ih hall
    obtain ⟨V,hV,hVp⟩ := ih (fun q hq => hall q (Finset.mem_insert_of_mem hq))
    obtain ⟨W,hW,hWp⟩ := hall p (Finset.mem_insert_self p P)
    have hd : Disjoint W V := by
      apply Finset.disjoint_left.mpr
      intro x hxW hxV
      obtain ⟨q,hq,hqx⟩ := hVp x hxV
      have hpx := hWp x hxW
      have hN : 0 < Ideal.absNorm (J x.1 : Ideal (𝓞 K)) :=
        Nat.pos_of_ne_zero (Ideal.absNorm_ne_zero_of_nonZeroDivisors (J x.1))
      have he : p=q := by nlinarith [hpx.2.2,hqx.2.2]
      exact hp (he.symm ▸ hq)
    refine ⟨W ∪ V,?_,?_⟩
    · rw [Finset.card_union_of_disjoint hd,hW,hV,Finset.card_insert_of_not_mem hp]
      ring
    · intro x hx
      rcases Finset.mem_union.mp hx with hx | hx
      · exact ⟨p,Finset.mem_insert_self p P,hWp x hx⟩
      · obtain ⟨q,hq,hqx⟩ := hVp x hx
        exact ⟨q,Finset.mem_insert_of_mem hq,hqx⟩

theorem finite_odd_square_representations (D : Nat) [Fact ((D : Int)%4=3)]
    (hDsq : Squarefree D) (P : Finset Nat) (hP : ∀ p ∈ P, Admissible D p) :
    ∃ J : ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) →
        (Ideal (𝓞 (QuadraticField (((D : Int)+1)/4))))⁰,
      FamilyGood J ∧ ∃ U : Finset (ClassGroup (𝓞 (QuadraticField (((D : Int)+1)/4))) ×
          𝓞 (QuadraticField (((D : Int)+1)/4))),
        U.card=4*P.card ∧ ∀ x ∈ U, ∃ p ∈ P, PointAt J p x := by
  obtain ⟨J,hJ,hall⟩ := odd_square_family D hDsq
  obtain ⟨U,hU,hu⟩ := aggregate_points _ J P (fun p hp => hall p (hP p hp))
  exact ⟨J,hJ,U,hU,hu⟩

private instance sevenFieldCondition : Fact (0 < 4*(2 : Int)-1) := ⟨by decide⟩

theorem seven_eleven_control :
    ∃ J : ClassGroup (𝓞 (QuadraticField 2)) → (Ideal (𝓞 (QuadraticField 2)))⁰,
      ∃ U : Finset (ClassGroup (𝓞 (QuadraticField 2)) × 𝓞 (QuadraticField 2)),
        U.card=4 ∧ ∀ x ∈ U, PointAt J 11 x := by
  letI : Fact (((7 : Nat) : Int)%4=3) := ⟨by decide⟩
  have hs : Squarefree (7 : Nat) := (by norm_num : Nat.Prime 7).squarefree
  have hp : Admissible 7 11 := ⟨by norm_num,by decide,by decide,⟨2,by decide⟩⟩
  obtain ⟨J,hJ,U,hU,hu⟩ := finite_odd_square_representations 7 hs {11}
    (by intro p hp'; simpa only [Finset.mem_singleton.mp hp'] using hp)
  refine ⟨J,U,by simpa using hU,?_⟩
  intro x hx
  obtain ⟨p,hp',hpx⟩ := hu x hx
  simpa only [Finset.mem_singleton.mp hp'] using hpx

theorem empty_control :
    ∃ J : ClassGroup (𝓞 Rat) → (Ideal (𝓞 Rat))⁰,
      ∃ U : Finset (ClassGroup (𝓞 Rat) × 𝓞 Rat), U.card=0 := by
  obtain ⟨J,hJ,hall⟩ := class_family_four_lifts Rat
  obtain ⟨U,hU,hu⟩ := aggregate_points Rat J ∅ (by simp)
  exact ⟨J,U,by simpa using hU⟩

theorem ramified_root_control :
    letI : Fact (((15 : Nat) : Int)%4=3) := ⟨by decide⟩
    actualResidueMap 15 3 fifteen_squarefree (by decide) 0 (by decide) =
      actualResidueMap 15 3 fifteen_squarefree (by decide) (-0) (by decide) := by
  simp

theorem characteristic_two_control :
    (1 : ZMod 2)^2=-(7 : ZMod 2) ∧ (1 : ZMod 2)= -1 := by decide
end
end TenthDiscriminant.ResidueMultiplicity

#check TenthDiscriminant.ResidueMultiplicity.class_family_four_lifts
#check TenthDiscriminant.ResidueMultiplicity.finite_odd_square_representations
#print TenthDiscriminant.ResidueMultiplicity.FamilyGood
#print TenthDiscriminant.ResidueMultiplicity.Admissible
#print TenthDiscriminant.ResidueMultiplicity.PointAt
#print axioms TenthDiscriminant.ResidueMultiplicity.class_family_four_lifts
#print axioms TenthDiscriminant.ResidueMultiplicity.finite_odd_square_representations
#audit_namespace TenthDiscriminant.ResidueMultiplicity
