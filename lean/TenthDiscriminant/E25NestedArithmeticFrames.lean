import TenthDiscriminant.E24ArithmeticFrame

/-!
# E25: nested integral frames and a typed partial inverse

The embeddings compose exactly. Their inverse is PARTIAL on the target
lattice: an odd-coordinate target is None, not a fabricated witness.
The two-step original integer Gram remains source-locked throughout.
-/
namespace TenthDiscriminant.E25
set_option autoImplicit false
noncomputable section

theorem squareOrderEmbed_compose (k l : Nat) (p : Int × Int) :
    E24.squareOrderEmbed k (E24.squareOrderEmbed l p) =
      E24.squareOrderEmbed (k*l) p := by
  apply Prod.ext <;> simp [E24.squareOrderEmbed] <;> ring

/-- Two nested arithmetic frames preserve every original derivative row
and trace-Gram entry through the source-matched supports. -/
theorem two_stage_originalGram (Q : Finset (Int × Int))
    (D k l J R S : Nat) (hk : 0 < k) (hl : 0 < l) :
    integerRectangularTraceGram
      ((Q.image (E24.squareOrderEmbed l)).image
        (E24.squareOrderEmbed k)) D J R S =
    integerRectangularTraceGram Q ((D*k*k)*l*l) J R S := by
  calc
    _ = integerRectangularTraceGram
        (Q.image (E24.squareOrderEmbed l)) (D*k*k) J R S :=
      E24.squareOrderEmbed_originalGram
        (Q.image (E24.squareOrderEmbed l)) D k J R S hk
    _ = integerRectangularTraceGram
        Q ((D*k*k)*l*l) J R S :=
      E24.squareOrderEmbed_originalGram Q (D*k*k) l J R S hl

/-- The k=2 integer embedding has an exact inverse on its image only. -/
def recoverEven (p : Int × Int) : Option (Int × Int) :=
  if p.2 % 2 = 0 then some (p.1,p.2/2) else none

theorem recoverEven_after_embedding (p : Int × Int) :
    recoverEven (E24.squareOrderEmbed 2 p) = some p := by
  cases p with
  | mk x y =>
      have hmod : (2*y : Int) % 2 = 0 := by omega
      have hquot : (2*y : Int) / 2 = y := by omega
      simp [recoverEven,E24.squareOrderEmbed,hmod,hquot]

theorem recoverEven_odd_target :
    recoverEven (0,1) = none := by
  norm_num [recoverEven]

theorem recoverEven_even_target :
    recoverEven (0,0) = some (0,0) := by
  norm_num [recoverEven]

theorem recoverEven_not_total :
    ¬ ∀ p : Int × Int, ∃ q, recoverEven p = some q := by
  intro h
  obtain ⟨q,hq⟩ := h (0,1)
  rw [recoverEven_odd_target] at hq
  cases hq

/-- Observing x alone cannot reconstruct the future partial arithmetic
reverse transition; the definedness remainder is a typed obstruction. -/
theorem future_reverse_not_decodable_from_first_coordinate :
    ¬ ∃ f : Int → Option (Int × Int),
        ∀ p : Int × Int, f p.1 = recoverEven p := by
  rintro ⟨f,hf⟩
  have h0 := hf (0,0)
  have h1 := hf (0,1)
  have hsame : recoverEven (0,0) = recoverEven (0,1) :=
    h0.symm.trans h1
  rw [recoverEven_even_target, recoverEven_odd_target] at hsame
  cases hsame

theorem same_first_coordinate_different_definedness :
    ((0,0) : Int × Int).1 = ((0,1) : Int × Int).1 ∧
      recoverEven (0,0) ≠ recoverEven (0,1) := by
  constructor
  · rfl
  · rw [recoverEven_even_target, recoverEven_odd_target]
    decide

end
end TenthDiscriminant.E25

#print axioms TenthDiscriminant.E25.squareOrderEmbed_compose
#print axioms TenthDiscriminant.E25.two_stage_originalGram
#print axioms TenthDiscriminant.E25.recoverEven_after_embedding
#print axioms TenthDiscriminant.E25.recoverEven_not_total
#print axioms TenthDiscriminant.E25.future_reverse_not_decodable_from_first_coordinate
