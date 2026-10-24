import TenthDiscriminant.EvenClassNumber
import TenthDiscriminant.UniformUpperEnvelope

/-! One actual field family Q[sqrt(-d)] covers both charts. The change
theta=2*omega-1 is a field equivalence, not a redefinition of class number. -/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false
noncomputable section

abbrev ImaginaryQuadraticField (d : Nat) := EvenQuadraticField d

private theorem doubleGeneratorRelation (A : Type*) [CommRing A]
    (t c q : A) (ht : t^2-t+c=0) (hc : 4*c=q+1) : (2*t-1)^2+q=0 := by
  linear_combination 4*ht-hc

private theorem halfGeneratorRelation (A : Type*) [Field A] [CharZero A]
    (t c q : A) (ht : t^2+q=0) (hc : 4*c=q+1) :
    ((1+t)/2)^2-(1+t)/2+c=0 := by
  linear_combination ht/4+hc/4

def traceZeroToHalf (d : Nat) [Fact ((d : Int)%4=3)] [Fact (0 < d)] :
    EvenQuadraticField d →ₐ[Rat] QuadraticField (((d : Int)+1)/4) := by
  let c : Int := ((d : Int)+1)/4
  let t := AdjoinRoot.root (quadraticFieldPoly c)
  have hc : 4*(c : QuadraticField c)=(d : QuadraticField c)+1 := by
    have hi : 4*c=(d : Int)+1 := halfOrder_coefficient_identity d Fact.out
    simpa only [Int.cast_mul, Int.cast_ofNat, Int.cast_add, Int.cast_natCast, Int.cast_one]
      using congrArg (fun z : Int => (z : QuadraticField c)) hi
  have ht : t^2-t+(c : QuadraticField c)=0 := by
    have h := AdjoinRoot.eval₂_root (quadraticFieldPoly c)
    change (X^2-X+C (c : Rat)).eval₂ (AdjoinRoot.of (quadraticFieldPoly c)) t=0 at h
    rw [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C] at h
    simpa only [map_intCast] using h
  have hz : (2*t-1)^2+(d : QuadraticField c)=0 := by
    exact doubleGeneratorRelation _ _ _ _ ht hc
  let f : EvenQuadraticField d →+* QuadraticField c :=
    AdjoinRoot.lift (AdjoinRoot.of (quadraticFieldPoly c)) (2*t-1) (by
      change (X^2+C (d : Rat)).eval₂ (AdjoinRoot.of (quadraticFieldPoly c)) (2*t-1)=0
      rw [eval₂_add, eval₂_pow, eval₂_X, eval₂_C]
      simpa only [map_natCast] using hz)
  exact f.toRatAlgHom

def halfToTraceZero (d : Nat) [Fact ((d : Int)%4=3)] [Fact (0 < d)] :
    QuadraticField (((d : Int)+1)/4) →ₐ[Rat] EvenQuadraticField d := by
  let c : Int := ((d : Int)+1)/4
  let t := AdjoinRoot.root (evenFieldPoly d)
  have hc : 4*(c : EvenQuadraticField d)=(d : EvenQuadraticField d)+1 := by
    have hi : 4*c=(d : Int)+1 := halfOrder_coefficient_identity d Fact.out
    simpa only [Int.cast_mul, Int.cast_ofNat, Int.cast_add, Int.cast_natCast, Int.cast_one]
      using congrArg (fun z : Int => (z : EvenQuadraticField d)) hi
  have ht : t^2+(d : EvenQuadraticField d)=0 := by
    have h := evenField_root_sq d
    simpa [t] using (eq_neg_iff_add_eq_zero.mp h)
  have hz : ((1+t)/2)^2-(1+t)/2+(c : EvenQuadraticField d)=0 := by
    exact halfGeneratorRelation _ _ _ _ ht hc
  let f : QuadraticField c →+* EvenQuadraticField d :=
    AdjoinRoot.lift (AdjoinRoot.of (evenFieldPoly d)) ((1+t)/2) (by
      change (X^2-X+C (c : Rat)).eval₂ (AdjoinRoot.of (evenFieldPoly d)) ((1+t)/2)=0
      rw [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C]
      simpa only [map_intCast] using hz)
  exact f.toRatAlgHom

theorem traceZeroToHalf_root (d : Nat) [Fact ((d : Int)%4=3)] [Fact (0 < d)] :
    traceZeroToHalf d (AdjoinRoot.root (evenFieldPoly d))=
      2*AdjoinRoot.root (quadraticFieldPoly (((d : Int)+1)/4))-1 := by
  simp [traceZeroToHalf]

theorem halfToTraceZero_root (d : Nat) [Fact ((d : Int)%4=3)] [Fact (0 < d)] :
    halfToTraceZero d (AdjoinRoot.root (quadraticFieldPoly (((d : Int)+1)/4)))=
      (1+AdjoinRoot.root (evenFieldPoly d))/2 := by
  simp [halfToTraceZero]

def quadraticChartEquiv (d : Nat) [Fact ((d : Int)%4=3)] [Fact (0 < d)] :
    EvenQuadraticField d ≃ₐ[Rat] QuadraticField (((d : Int)+1)/4) := by
  let w := AdjoinRoot.root (quadraticFieldPoly (((d : Int)+1)/4))
  let t := AdjoinRoot.root (evenFieldPoly d)
  apply AlgEquiv.ofAlgHom (traceZeroToHalf d) (halfToTraceZero d)
  · apply AdjoinRoot.algHom_ext
    change traceZeroToHalf d (halfToTraceZero d w)=w
    have hdbl : 2*halfToTraceZero d w=1+t := by
      dsimp [w, t]
      rw [halfToTraceZero_root]
      ring
    have hm := congrArg (traceZeroToHalf d) hdbl
    simp only [map_mul, map_ofNat, map_add, map_one, t, traceZeroToHalf_root] at hm
    apply mul_left_cancel₀ (by norm_num : (2 : QuadraticField (((d : Int)+1)/4)) ≠ 0)
    exact hm.trans (by dsimp [w]; ring)
  · apply AdjoinRoot.algHom_ext
    change halfToTraceZero d (traceZeroToHalf d t)=t
    dsimp [t]
    rw [traceZeroToHalf_root]
    simp only [map_sub, map_mul, map_ofNat, map_one, halfToTraceZero_root, AlgHom.id_apply]
    ring

theorem classNumber_one_of_field_equiv (K L : Type*) [Field K] [Field L]
    [NumberField K] [NumberField L] (e : K ≃ₐ[Rat] L)
    (h : NumberField.classNumber K=1) : NumberField.classNumber L=1 := by
  letI : IsPrincipalIdealRing (NumberField.RingOfIntegers K) :=
    (NumberField.classNumber_eq_one_iff).mp h
  let f : NumberField.RingOfIntegers K ≃+* NumberField.RingOfIntegers L :=
    (e.restrictScalars Int).mapIntegralClosure.toRingEquiv
  exact NumberField.classNumber_eq_one_iff.mpr
    (IsPrincipalIdealRing.of_surjective f.toRingHom f.surjective)

theorem squarefree_mod_four_cases (d : Nat) (hsq : Squarefree d) :
    (d : Int)%4=3 ∨ ((d : Int)%4=1 ∨ (d : Int)%4=2) := by
  have h4 : ¬ 4 ∣ d := by
    intro h
    have hu : IsUnit (2 : Nat) := hsq 2 (by simpa using h)
    norm_num at hu
  omega

/-- Effective radicand bound in one actual field family, with both parity
charts supplied. This is not a finite class-number classification. -/
theorem imaginaryQuadratic_large_classNumber_ne_one (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hd : 700000000000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with hodd | heven
  · letI : Fact ((d : Int)%4=3) := ⟨hodd⟩
    intro hclass
    have hhalf := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hclass
    exact FirstCertificate.odd_large_classNumber_ne_one d hd hsq hhalf
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨heven⟩
    exact even_classNumber_ne_one d hsq (by omega)

theorem imaginaryQuadratic_classNumber_one_radicand_bound (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    d < 700000000000 := by
  by_contra h
  exact imaginaryQuadratic_large_classNumber_ne_one d hsq (by omega) hclass

/-- Conventional absolute fundamental-discriminant parameter for a
positive squarefree radicand. Its relation to NumberField.discr is not
silently used by the cutoff theorem. -/
def absoluteDiscriminantParameter (d : Nat) : Nat :=
  if (d : Int)%4=3 then d else 4*d

theorem imaginaryQuadratic_classNumber_one_parameter_bound (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    absoluteDiscriminantParameter d < 700000000000 := by
  rcases squarefree_mod_four_cases d hsq with hodd | heven
  · simpa [absoluteDiscriminantParameter, hodd] using
      imaginaryQuadratic_classNumber_one_radicand_bound d hsq hclass
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨heven⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hclass
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter, if_neg hnot]
    omega

private instance threePositiveChartFact : Fact (0 < (3 : Nat)) := ⟨by decide⟩
private instance threeOddChartFact : Fact ((((3 : Nat) : Int)%4)=3) := ⟨by decide⟩

/-- The guard counterexample is an actual algebraic integer, not merely
a formal pair with integral trace and norm. -/
theorem three_actual_half_integer_control :
    IsIntegral Int ((1+AdjoinRoot.root (evenFieldPoly 3))/2) := by
  have h := halfOrder_image_integral 3 (by decide)
    (AdjoinRoot.root (halfOrderPolynomial 3))
  rw [halfOrderToQuadraticField_root] at h
  have hm := map_isIntegral_int (halfToTraceZero 3).toRingHom h
  have hroot := halfToTraceZero_root 3
  exact hroot ▸ hm

end
end TenthDiscriminant
