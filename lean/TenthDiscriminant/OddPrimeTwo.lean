import TenthDiscriminant.QuadraticChartEquivalence

/-! The missing modulo-eight prefilter. At prime two the half-integral
generator maps directly to zero; no division by two modulo two is used. -/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false
noncomputable section

def halfOrderResidueTwo (D : Nat) (hc : 2 ∣ ((D : Int)+1)/4) :
    AdjoinRoot (halfOrderPolynomial D) →+* ZMod 2 := by
  have hz : ((((D : Int)+1)/4 : Int) : ZMod 2)=0 :=
    (ZMod.intCast_zmod_eq_zero_iff_dvd _ 2).2 hc
  apply AdjoinRoot.lift (Int.castRingHom _) 0
  change (X^2-X+C (((D : Int)+1)/4)).eval₂ (Int.castRingHom _) (0 : ZMod 2)=0
  rw [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C]
  norm_num only [zero_pow (by decide : 2 ≠ 0), sub_self, zero_add]
  exact hz

theorem halfOrder_norm_two_of_even_coefficient (D : Nat)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : 2 ∣ ((D : Int)+1)/4)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1) :
    ∃ x y : Int, principalNorm D x y=2 := by
  let e := halfOrderEquivRingOfIntegers D hsq
  let f : NumberField.RingOfIntegers (QuadraticField (((D : Int)+1)/4)) →+* ZMod 2 :=
    (halfOrderResidueTwo D hc).comp e.symm.toRingHom
  obtain ⟨a, ha⟩ := exists_integer_of_absNorm_of_classNumber_one
    (QuadraticField (((D : Int)+1)/4)) 2 f hclass
  let w := e.symm a
  obtain ⟨x, y, hxy⟩ := halfOrder_coordinates D w
  have hn : Algebra.norm Int a=principalNorm D x y := by
    have he : e w=a := e.apply_symm_apply a
    rw [← he]
    change Algebra.norm Int (halfOrderToRingOfIntegers D w)=_
    rw [hxy]
    exact halfOrder_ringOfIntegers_norm D x y
  rw [hn] at ha
  have hp := principalNorm_nonneg D Fact.out x y
  exact ⟨x, y, by omega⟩

theorem halfOrder_norm_two_impossible_above_seven (D : Nat)
    (hmod : (D : Int)%4=3) (hD : 7 < D) (x y : Int) :
    principalNorm D x y ≠ 2 := by
  intro hn
  by_cases hy : y=0
  · subst y
    have hx : x^2=(2 : Int) := by simpa [principalNorm] using hn
    have hnat : x.natAbs^2=2 := by
      simpa only [Int.natAbs_pow] using congrArg Int.natAbs hx
    exact Nat.prime_two.not_isSquare ⟨x.natAbs, by simpa [pow_two] using hnat.symm⟩
  · exact small_norm_impossible D x y 2 hmod (by omega) hy hn (by omega)

theorem halfOrder_classNumber_one_mod_eight (D : Nat)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) (hD : 7 < D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1) :
    D%8=3 := by
  have hmod := Fact.out (p := (D : Int)%4=3)
  by_contra hnot
  have h7 : (D : Int)%8=7 := by omega
  have hc : 2 ∣ ((D : Int)+1)/4 := by omega
  obtain ⟨x, y, hn⟩ := halfOrder_norm_two_of_even_coefficient D hsq hc hclass
  exact halfOrder_norm_two_impossible_above_seven D hmod hD x y hn

/-- This is the saved sieve's prefilter, now for the single actual field
family and without a congruence assumption supplied by the caller. -/
theorem imaginaryQuadratic_classNumber_one_mod_eight (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hd : 7 < d)
    (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1) : d%8=3 := by
  rcases squarefree_mod_four_cases d hsq with hodd | heven
  · letI : Fact ((d : Int)%4=3) := ⟨hodd⟩
    have hc := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hclass
    exact halfOrder_classNumber_one_mod_eight d hsq hd hc
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨heven⟩
    exact False.elim (even_classNumber_ne_one d hsq (by omega) hclass)

theorem imaginaryQuadratic_classNumber_one_small_or_mod_eight (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    d=1 ∨ d=2 ∨ d=3 ∨ d=7 ∨ d%8=3 := by
  by_cases hd : 7 < d
  · exact Or.inr (Or.inr (Or.inr (Or.inr
      (imaginaryQuadratic_classNumber_one_mod_eight d hsq hd hclass))))
  · rcases squarefree_mod_four_cases d hsq with hodd | heven
    · omega
    · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨heven⟩
      have h := even_classNumber_one_only_one_or_two d hsq hclass
      omega

theorem seven_norm_two_exception_control : principalNorm 7 0 1=2 ∧ (7 : Nat)%8≠3 := by
  norm_num [principalNorm]

private instance twentyThreePositiveFact : Fact (0 < (23 : Nat)) := ⟨by decide⟩

theorem twentyThree_classNumber_ne_one :
    NumberField.classNumber (ImaginaryQuadraticField 23) ≠ 1 := by
  intro hc
  have h := imaginaryQuadratic_classNumber_one_mod_eight 23
    (by norm_num : Nat.Prime 23).squarefree (by decide) hc
  norm_num at h

end
end TenthDiscriminant
