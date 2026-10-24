import TenthDiscriminant.EvenMaximalOrder
import TenthDiscriminant.PrincipalIdealBridge

/-! Prime two excludes all but radicands 1,2 in the even fundamental chart.
No analytic cutoff, odd-case classification or Heegner method is used. -/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false
noncomputable section

def evenOrderResidueTwo (d : Nat) : AdjoinRoot (evenOrderPoly d) →+* ZMod 2 := by
  have hroot : (d : ZMod 2)^2+(d : ZMod 2)=0 := by
    generalize (d : ZMod 2)=z
    fin_cases z <;> decide
  apply AdjoinRoot.lift (Int.castRingHom _) (d : ZMod 2)
  simpa [evenOrderPoly] using hroot

theorem even_classNumber_one_norm_two (d : Nat)
    [Fact ((d : Int)%4=1 ∨ (d : Int)%4=2)] (hsq : Squarefree d)
    (hclass : NumberField.classNumber (EvenQuadraticField d)=1) :
    ∃ x y : Int, x^2+(d : Int)*y^2=2 := by
  let e := evenOrderEquivRingOfIntegers d hsq Fact.out
  let f : NumberField.RingOfIntegers (EvenQuadraticField d) →+* ZMod 2 :=
    (evenOrderResidueTwo d).comp e.symm.toRingHom
  obtain ⟨a, ha⟩ := exists_integer_of_absNorm_of_classNumber_one (EvenQuadraticField d) 2 f hclass
  let w := e.symm a
  obtain ⟨x, y, hxy⟩ := evenOrder_coordinates d w
  have hanorm : Algebra.norm Int a=x^2+(d : Int)*y^2 := by
    have he : e w=a := e.apply_symm_apply a
    rw [← he]
    change Algebra.norm Int (evenOrderToRingOfIntegers d w)=_
    rw [hxy]
    exact evenOrder_ringOfIntegers_norm d x y
  rw [hanorm] at ha
  have hnonneg := evenChart_norm_nonneg d x y
  exact ⟨x, y, by omega⟩

theorem even_classNumber_ne_one (d : Nat)
    [Fact ((d : Int)%4=1 ∨ (d : Int)%4=2)] (hsq : Squarefree d) (hd : 2 < d) :
    NumberField.classNumber (EvenQuadraticField d) ≠ 1 := by
  intro hclass
  obtain ⟨x, y, hxy⟩ := even_classNumber_one_norm_two d hsq hclass
  exact evenChart_no_norm_two d hd x y hxy

theorem even_classNumber_one_only_one_or_two (d : Nat)
    [Fact ((d : Int)%4=1 ∨ (d : Int)%4=2)] (hsq : Squarefree d)
    (hclass : NumberField.classNumber (EvenQuadraticField d)=1) : d=1 ∨ d=2 := by
  have hmod := Fact.out (p := (d : Int)%4=1 ∨ (d : Int)%4=2)
  have hle : d ≤ 2 := by
    by_contra h
    exact even_classNumber_ne_one d hsq (by omega) hclass
  omega

private instance fiveEvenModFact : Fact (((5 : Nat) : Int)%4=1 ∨ ((5 : Nat) : Int)%4=2) := ⟨by decide⟩

theorem five_even_classNumber_ne_one : NumberField.classNumber (EvenQuadraticField 5) ≠ 1 := by
  exact even_classNumber_ne_one 5 (by norm_num : Nat.Prime 5).squarefree (by decide)

end
end TenthDiscriminant
