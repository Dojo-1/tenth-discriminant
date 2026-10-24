import TenthDiscriminant.SmallIdealClassNumber
import TenthDiscriminant.MillionSieve

/-! The remaining five positive class-number proofs. Local polynomial
checks supply ideal obstructions; Minkowski supplies a global representative. -/
namespace TenthDiscriminant
open NumberField
open scoped NumberField
set_option autoImplicit false
noncomputable section

theorem halfOrder_no_prime_norm (d : Nat) [Fact ((d : Int)%4=3)] (hsq : Squarefree d)
    (p : Nat) (hp : p.Prime)
    (hroot : ∀ z : ZMod p, z^2-z+((((d : Int)+1)/4 : Int) : ZMod p)≠0)
    (I : Ideal (𝓞 (QuadraticField (((d : Int)+1)/4)))) : Ideal.absNorm I≠p := by
  intro hn
  obtain ⟨f⟩ := ideal_prime_norm_residue_map (QuadraticField (((d : Int)+1)/4)) I p hp hn
  let e := halfOrderEquivRingOfIntegers d hsq
  let z : ZMod p := f (e (AdjoinRoot.root (halfOrderPolynomial d)))
  have hrel : z^2=z-((((d : Int)+1)/4 : Int) : ZMod p) := by
    have h := congrArg (fun a => f (e a)) (halfOrder_root_sq d)
    simpa [z] using h
  exact hroot z (by linear_combination hrel)

theorem halfOrder_positive_lower_tier (d : Nat) [Fact (0 < d)] [Fact ((d : Int)%4=3)]
    (hsq : Squarefree d) (hsmall : d≤19)
    (hroot : ∀ z : ZMod 2, z^2-z+((((d : Int)+1)/4 : Int) : ZMod 2)≠0) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 := by
  have hd : (NumberField.discr (QuadraticField (((d : Int)+1)/4))).natAbs≤19 := by
    rw [half_actual_discr d hsq]
    simpa using hsmall
  have hc := quadratic_classNumber_one_without_norm_two (QuadraticField (((d : Int)+1)/4))
    (quadraticField_basis_dimension _) hd (halfOrder_no_prime_norm d hsq 2 Nat.prime_two hroot)
  exact classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d).symm hc

theorem halfOrder_positive_upper_tier (d : Nat) [Fact (0 < d)] [Fact ((d : Int)%4=3)]
    (hsq : Squarefree d) (hsmall : d≤163)
    (hroots : ∀ p ∈ ([2,3,5,7] : List Nat),
      ∀ z : ZMod p, z^2-z+((((d : Int)+1)/4 : Int) : ZMod p)≠0) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 := by
  have hd : (NumberField.discr (QuadraticField (((d : Int)+1)/4))).natAbs≤163 := by
    rw [half_actual_discr d hsq]
    simpa using hsmall
  have hno : ∀ (I : Ideal (𝓞 (QuadraticField (((d : Int)+1)/4)))) (p : Nat),
      p ∈ ([2,3,5,7] : List Nat) → Ideal.absNorm I≠p := by
    intro I p hp
    have hprime : p.Prime := by
      have hm := hp
      simp only [List.mem_cons,List.not_mem_nil,or_false] at hm
      rcases hm with rfl | rfl | rfl | rfl <;> norm_num
    exact halfOrder_no_prime_norm d hsq p hprime (hroots p hp) I
  have hc := quadratic_classNumber_one_without_small_prime_norms
    (QuadraticField (((d : Int)+1)/4)) (quadraticField_basis_dimension _) hd hno
  exact classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d).symm hc

private instance positiveEleven : Fact (0 < (11 : Nat)) := ⟨by decide⟩
private instance oddEleven : Fact (((11 : Nat) : Int)%4=3) := ⟨by decide⟩
private instance positiveNineteen : Fact (0 < (19 : Nat)) := ⟨by decide⟩
private instance oddNineteen : Fact (((19 : Nat) : Int)%4=3) := ⟨by decide⟩
private instance positiveFortyThree : Fact (0 < (43 : Nat)) := ⟨by decide⟩
private instance oddFortyThree : Fact (((43 : Nat) : Int)%4=3) := ⟨by decide⟩
private instance positiveSixtySeven : Fact (0 < (67 : Nat)) := ⟨by decide⟩
private instance oddSixtySeven : Fact (((67 : Nat) : Int)%4=3) := ⟨by decide⟩
private instance positiveOneSixtyThree : Fact (0 < (163 : Nat)) := ⟨by decide⟩
private instance oddOneSixtyThree : Fact (((163 : Nat) : Int)%4=3) := ⟨by decide⟩
private instance positiveTwentyThree : Fact (0 < (23 : Nat)) := ⟨by decide⟩

theorem eleven_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 11)=1 :=
  halfOrder_positive_lower_tier 11 (by norm_num : Nat.Prime 11).squarefree
    (by decide) (by decide +kernel)

theorem nineteen_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 19)=1 :=
  halfOrder_positive_lower_tier 19 (by norm_num : Nat.Prime 19).squarefree
    (by decide) (by decide +kernel)

theorem fortyThree_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 43)=1 := by
  apply halfOrder_positive_upper_tier 43 (by norm_num : Nat.Prime 43).squarefree (by decide)
  intro p hp
  simp only [List.mem_cons,List.not_mem_nil,or_false] at hp
  rcases hp with rfl | rfl | rfl | rfl <;> decide +kernel

theorem sixtySeven_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 67)=1 := by
  apply halfOrder_positive_upper_tier 67 (by norm_num : Nat.Prime 67).squarefree (by decide)
  intro p hp
  simp only [List.mem_cons,List.not_mem_nil,or_false] at hp
  rcases hp with rfl | rfl | rfl | rfl <;> decide +kernel

theorem oneSixtyThree_classNumber_one : NumberField.classNumber (ImaginaryQuadraticField 163)=1 := by
  apply halfOrder_positive_upper_tier 163 (by norm_num : Nat.Prime 163).squarefree (by decide)
  intro p hp
  simp only [List.mem_cons,List.not_mem_nil,or_false] at hp
  rcases hp with rfl | rfl | rfl | rfl <;> decide +kernel

theorem known_nine_classNumber_one (d : Nat) [Fact (0 < d)]
    (hd : d ∈ ([1,2,3,7,11,19,43,67,163] : List Nat)) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 := by
  simp only [List.mem_cons,List.not_mem_nil,or_false] at hd
  rcases hd with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact one_classNumber_one
  · exact two_classNumber_one
  · exact three_classNumber_one
  · exact seven_classNumber_one
  · exact eleven_classNumber_one
  · exact nineteen_classNumber_one
  · exact fortyThree_classNumber_one
  · exact sixtySeven_classNumber_one
  · exact oneSixtyThree_classNumber_one

/-- Both directions, but only below the explicitly checked finite endpoint. -/
theorem classNumber_one_iff_below_million (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hhi : d<1000000) :
    NumberField.classNumber (ImaginaryQuadraticField d)=1 ↔
      d ∈ ([1,2,3,7,11,19,43,67,163] : List Nat) :=
  ⟨fun hc => classNumber_one_candidates_below_million d hsq hc hhi,
    known_nine_classNumber_one d⟩

theorem principal_two_norm_four_control (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K=2) :
    Ideal.absNorm (Ideal.span ({(2 : 𝓞 K)} : Set (𝓞 K)))=4 := by
  simpa using quadratic_scalar_ideal_norm K hdegree 2

theorem eleven_root_mod_three_control :
    (0 : ZMod 3)^2-0+((((11 : Int)+1)/4 : Int) : ZMod 3)=0 := by decide +kernel

theorem twentyThree_root_mod_two_control :
    (0 : ZMod 2)^2-0+((((23 : Int)+1)/4 : Int) : ZMod 2)=0 := by decide +kernel

theorem discriminant_bound_alone_insufficient_control :
    (NumberField.discr (ImaginaryQuadraticField 23)).natAbs≤163 ∧
      NumberField.classNumber (ImaginaryQuadraticField 23)≠1 := by
  constructor
  · rw [imaginaryQuadratic_discr_natAbs 23 (by norm_num : Nat.Prime 23).squarefree]
    norm_num [absoluteDiscriminantParameter]
  · exact twentyThree_classNumber_ne_one

end
end TenthDiscriminant
