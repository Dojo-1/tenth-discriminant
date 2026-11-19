import TenthDiscriminant.E27ArithmeticNaturality

/-!
# E28: conductor-sensitive local residue transport

The source is the exact pair ring used by E24-E27. The integral order
embedding (a,b) -> (a,k*b) is injective for k>0, but its reduction at a
modulus m can lose witness information precisely when k is not a unit
modulo m. These proofs concern actual coefficient-pair source witnesses
and declared modular rings; no prime-ideal valuations or field bound
are imported.
-/

namespace TenthDiscriminant.E28
set_option autoImplicit false
noncomputable section

/-- Mod-m observations of original integral coefficient pairs. -/
def reducePair (m : Nat) (p : Int × Int) : ZMod m × ZMod m :=
  ((p.1 : ZMod m), (p.2 : ZMod m))

/-- Mod-m realization of the E24 index-k embedding. -/
def residueFrame (m k : Nat) (p : ZMod m × ZMod m) :
    ZMod m × ZMod m :=
  (p.1, (k : ZMod m) * p.2)

/-- Original quadratic pair multiplication after reducing coefficients. -/
def residueMul (m D : Nat) (a b : ZMod m × ZMod m) :
    ZMod m × ZMod m :=
  (a.1 * b.1 - (D : ZMod m) * a.2 * b.2,
   a.1 * b.2 + a.2 * b.1)

/-- Conjugation of coefficient pairs is itself a moving local observer. -/
def residueConj (m : Nat) (p : ZMod m × ZMod m) :
    ZMod m × ZMod m :=
  (p.1, -p.2)

/-- First embed the source integral witness and then reduce, or first
reduce and then move the frame: the two procedures agree exactly. -/
theorem reduction_natural (m k : Nat) (p : Int × Int) :
    reducePair m (E24.squareOrderEmbed k p) =
      residueFrame m k (reducePair m p) := by
  rcases p with ⟨a,b⟩
  apply Prod.ext
  · rfl
  · simp [reducePair, E24.squareOrderEmbed, residueFrame]

/-- The source quadratic multiplication law changes from D*k*k to D.
This is an exact ring-operations compatibility identity modulo m. -/
theorem residueFrame_mul (m D k : Nat)
    (a b : ZMod m × ZMod m) :
    residueFrame m k (residueMul m (D*k*k) a b) =
      residueMul m D (residueFrame m k a) (residueFrame m k b) := by
  apply Prod.ext <;>
    simp [residueFrame, residueMul] <;>
    push_cast <;> ring

/-- Conjugation and a change of arithmetic frame commute modulo m. -/
theorem residueFrame_conj (m k : Nat)
    (p : ZMod m × ZMod m) :
    residueFrame m k (residueConj m p) =
      residueConj m (residueFrame m k p) := by
  apply Prod.ext <;>
    simp [residueFrame, residueConj] <;> ring

/-- Local frames compose, including their original coefficient action. -/
theorem residueFrame_compose (m k l : Nat)
    (p : ZMod m × ZMod m) :
    residueFrame m k (residueFrame m l p) =
      residueFrame m (k*l) p := by
  apply Prod.ext <;>
    simp [residueFrame] <;>
    push_cast <;> ring

private theorem three_two_mod_five :
    (3 : ZMod 5) * 2 = 1 := by decide

private theorem two_three_mod_five :
    (2 : ZMod 5) * 3 = 1 := by decide

/-- Index two is exactly reversible on the original coefficient
residues modulo five; three is its inverse factor. -/
theorem mod5_left_inverse (p : ZMod 5 × ZMod 5) :
    residueFrame 5 3 (residueFrame 5 2 p) = p := by
  rcases p with ⟨a,b⟩
  apply Prod.ext
  · rfl
  · change (3 : ZMod 5) * ((2 : ZMod 5) * b) = b
    calc
      _ = ((3 : ZMod 5) * 2) * b := by ring
      _ = b := by rw [three_two_mod_five]; ring

theorem mod5_right_inverse (p : ZMod 5 × ZMod 5) :
    residueFrame 5 2 (residueFrame 5 3 p) = p := by
  rcases p with ⟨a,b⟩
  apply Prod.ext
  · rfl
  · change (2 : ZMod 5) * ((3 : ZMod 5) * b) = b
    calc
      _ = ((2 : ZMod 5) * 3) * b := by ring
      _ = b := by rw [two_three_mod_five]; ring

/-- Full bijectivity of the moving frame at the good prime 5. -/
theorem mod5_frame_bijective :
    Function.Bijective (residueFrame 5 2) := by
  constructor
  · intro a b hab
    have h := congrArg (residueFrame 5 3) hab
    simpa only [mod5_left_inverse] using h
  · intro p
    exact ⟨residueFrame 5 3 p, mod5_right_inverse p⟩

/-- At modulus two, distinct coefficient residues have identical
images. This is a direct original-source counterexample. -/
theorem mod2_collision :
    residueFrame 2 2 (0,0) = residueFrame 2 2 (0,1) ∧
      ((0,0) : ZMod 2 × ZMod 2) ≠ (0,1) := by
  constructor <;> decide

theorem mod2_frame_not_injective :
    ¬ Function.Injective (residueFrame 2 2) := by
  intro hi
  exact mod2_collision.2 (hi mod2_collision.1)

/-- The unrecoverable source coefficient is an actual nonzero
nilpotent in the mod-two source quadratic-pair ring at D=4. -/
theorem mod2_source_nilpotent :
    residueMul 2 4 (0,1) (0,1) = (0,0) ∧
      ((0,1) : ZMod 2 × ZMod 2) ≠ (0,0) := by
  constructor <;> decide

/-- The source's second coefficient is a future query that cannot
factor through this observer. Definedness is not needed for this
stronger non-factorization control. -/
theorem mod2_coefficient_not_decodable :
    ¬ ∃ decoder : (ZMod 2 × ZMod 2) → ZMod 2,
      ∀ p : ZMod 2 × ZMod 2,
        decoder (residueFrame 2 2 p) = p.2 := by
  rintro ⟨decoder,hdec⟩
  have h0 := hdec (0,0)
  have h1 := hdec (0,1)
  have heq : (0 : ZMod 2) = 1 := by
    calc
      (0 : ZMod 2) = decoder (residueFrame 2 2 (0,0)) := h0.symm
      _ = decoder (residueFrame 2 2 (0,1)) :=
        congrArg decoder mod2_collision.1
      _ = (1 : ZMod 2) := h1
  have hne : (0 : ZMod 2) ≠ 1 := by decide
  exact hne heq

/-- The two labelled residues at the two split factors of 5. -/
def splitPlus (p : ZMod 5 × ZMod 5) : ZMod 5 :=
  p.1 - 2 * p.2

def splitMinus (p : ZMod 5 × ZMod 5) : ZMod 5 :=
  p.1 + 2 * p.2

/-- Conjugation changes the prime label, rather than destroying
the prime-sensitive observation. -/
theorem mod5_prime_label_moves (p : ZMod 5 × ZMod 5) :
    splitPlus (residueConj 5 p) = splitMinus p := by
  rcases p with ⟨a,b⟩
  dsimp [splitPlus, splitMinus, residueConj]
  ring

/-- Distinct fixed-prime residues remain detectable inside
Z[2i] modulo 5 even though they coalesce under mod-two transport. -/
theorem mod5_fixed_prime_witness :
    splitPlus (residueFrame 5 2 (1,1)) ≠
      splitPlus (residueFrame 5 2 (1,4)) := by decide

end
end TenthDiscriminant.E28

#print axioms TenthDiscriminant.E28.reduction_natural
#print axioms TenthDiscriminant.E28.residueFrame_mul
#print axioms TenthDiscriminant.E28.residueFrame_compose
#print axioms TenthDiscriminant.E28.mod5_frame_bijective
#print axioms TenthDiscriminant.E28.mod2_frame_not_injective
#print axioms TenthDiscriminant.E28.mod2_source_nilpotent
#print axioms TenthDiscriminant.E28.mod2_coefficient_not_decodable
#print axioms TenthDiscriminant.E28.mod5_prime_label_moves
#print axioms TenthDiscriminant.E28.mod5_fixed_prime_witness
