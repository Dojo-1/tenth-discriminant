import TenthDiscriminant.EvenQuadraticField

/-! Identify Z[sqrt(-d)] with the actual maximal integer ring in the
squarefree d=1,2 modulo 4 cases. No principal-ideal premise is used here. -/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false
noncomputable section

def evenOrderToField (d : Nat) : AdjoinRoot (evenOrderPoly d) →+* EvenQuadraticField d := by
  let t : EvenQuadraticField d := AdjoinRoot.root (evenFieldPoly d)
  have ht : t^2+(d : EvenQuadraticField d)=0 := by
    have h := AdjoinRoot.eval₂_root (evenFieldPoly d)
    change (X^2+C (d : Rat)).eval₂ (AdjoinRoot.of (evenFieldPoly d)) t=0 at h
    simpa only [eval₂_add, eval₂_pow, eval₂_X, eval₂_C] using h
  apply AdjoinRoot.lift (Int.castRingHom _) t
  change (X^2+C (d : Int)).eval₂ (Int.castRingHom _) t=0
  simpa only [eval₂_add, eval₂_pow, eval₂_X, eval₂_C, Int.cast_natCast] using ht

theorem evenOrderToField_injective (d : Nat) : Function.Injective (evenOrderToField d) := by
  let f := evenOrderToField d
  apply (injective_iff_map_eq_zero f).2
  intro z hz
  obtain ⟨x, y, hxy⟩ := evenOrder_coordinates d z
  have hfield : AdjoinRoot.of (evenFieldPoly d) (x : Rat)+
      AdjoinRoot.of (evenFieldPoly d) (y : Rat)*AdjoinRoot.root (evenFieldPoly d)=0 := by
    rw [hxy] at hz
    simpa [f, evenOrderToField] using hz
  have hxq : (x : Rat)=0 := by
    have h := congrArg (fun w : EvenQuadraticField d => (evenFieldBasis d).repr w 0) hfield
    dsimp only at h
    rw [evenFieldBasis_repr] at h
    simpa using h
  have hyq : (y : Rat)=0 := by
    have h := congrArg (fun w : EvenQuadraticField d => (evenFieldBasis d).repr w 1) hfield
    dsimp only at h
    rw [evenFieldBasis_repr] at h
    simpa using h
  have hx : x=0 := by exact_mod_cast hxq
  have hy : y=0 := by exact_mod_cast hyq
  simp [hxy, hx, hy]

theorem evenOrder_image_integral (d : Nat) (z : AdjoinRoot (evenOrderPoly d)) :
    IsIntegral Int (evenOrderToField d z) := by
  obtain ⟨x, y, hxy⟩ := evenOrder_coordinates d z
  have hroot : IsIntegral Int (AdjoinRoot.root (evenOrderPoly d)) :=
    AdjoinRoot.isIntegral_root' (evenOrder_monic d)
  have hz : IsIntegral Int z := by
    rw [hxy]
    have hx : IsIntegral Int (AdjoinRoot.of (evenOrderPoly d) x) := isIntegral_algebraMap
    have hy : IsIntegral Int (AdjoinRoot.of (evenOrderPoly d) y) := isIntegral_algebraMap
    exact hx.add (hy.mul hroot)
  exact map_isIntegral_int (evenOrderToField d) hz

def evenOrderToRingOfIntegers (d : Nat) [Fact (0 < d)] :
    AdjoinRoot (evenOrderPoly d) →+* NumberField.RingOfIntegers (EvenQuadraticField d) := by
  let f := evenOrderToField d
  refine {
    toFun := fun z => ⟨f z, evenOrder_image_integral d z⟩
    map_one' := ?_
    map_mul' := ?_
    map_zero' := ?_
    map_add' := ?_
  }
  · apply Subtype.ext
    exact f.map_one
  · intro x y
    apply Subtype.ext
    exact f.map_mul x y
  · apply Subtype.ext
    exact f.map_zero
  · intro x y
    apply Subtype.ext
    exact f.map_add x y

theorem evenOrderToRingOfIntegers_injective (d : Nat) [Fact (0 < d)] :
    Function.Injective (evenOrderToRingOfIntegers d) := by
  intro x y hxy
  apply evenOrderToField_injective d
  exact congrArg Subtype.val hxy

theorem evenOrderToRingOfIntegers_surjective (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hmod : (d : Int)%4=1 ∨ (d : Int)%4=2) :
    Function.Surjective (evenOrderToRingOfIntegers d) := by
  intro w
  obtain ⟨x, y, hxy⟩ := evenField_integral_coordinates d hsq hmod w.1 w.2
  refine ⟨AdjoinRoot.of (evenOrderPoly d) x+
    AdjoinRoot.of (evenOrderPoly d) y*AdjoinRoot.root (evenOrderPoly d), ?_⟩
  apply Subtype.ext
  simpa [evenOrderToRingOfIntegers, evenOrderToField] using hxy.symm

def evenOrderEquivRingOfIntegers (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hmod : (d : Int)%4=1 ∨ (d : Int)%4=2) :
    AdjoinRoot (evenOrderPoly d) ≃+* NumberField.RingOfIntegers (EvenQuadraticField d) :=
  RingEquiv.ofBijective (evenOrderToRingOfIntegers d)
    ⟨evenOrderToRingOfIntegers_injective d, evenOrderToRingOfIntegers_surjective d hsq hmod⟩

theorem evenOrder_ringOfIntegers_norm (d : Nat) [Fact (0 < d)] (x y : Int) :
    Algebra.norm Int (evenOrderToRingOfIntegers d (AdjoinRoot.of (evenOrderPoly d) x+
      AdjoinRoot.of (evenOrderPoly d) y*AdjoinRoot.root (evenOrderPoly d))) =
      x^2+(d : Int)*y^2 := by
  have hn := Algebra.coe_norm_int (evenOrderToRingOfIntegers d
    (AdjoinRoot.of (evenOrderPoly d) x+
      AdjoinRoot.of (evenOrderPoly d) y*AdjoinRoot.root (evenOrderPoly d)))
  have hn' : ((Algebra.norm Int (evenOrderToRingOfIntegers d
    (AdjoinRoot.of (evenOrderPoly d) x+
      AdjoinRoot.of (evenOrderPoly d) y*AdjoinRoot.root (evenOrderPoly d))) : Int) : Rat) =
      (x : Rat)^2+(d : Rat)*(y : Rat)^2 := by
    rw [hn]
    simpa [evenOrderToRingOfIntegers, evenOrderToField] using evenField_norm d (x : Rat) (y : Rat)
  exact_mod_cast hn'

end
end TenthDiscriminant
