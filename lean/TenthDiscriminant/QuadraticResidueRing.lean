import TenthDiscriminant.ResidueTraceGram

/-!
# A ring chart for the existing two residue coordinates

This local chart packages the repository's `residuePairMul` as a
commutative ring, so characteristic-`p` identities apply without
changing the underlying pair or the integer Gram.
-/
namespace TenthDiscriminant

structure QuadraticResidue (D p : Nat) where
  re : ZMod p
  im : ZMod p
deriving DecidableEq

namespace QuadraticResidue

@[ext] theorem ext {D p : Nat} {a b : QuadraticResidue D p}
    (hre : a.re = b.re) (him : a.im = b.im) : a = b := by
  cases a with
  | mk ar ai =>
    cases b with
    | mk br bi =>
      cases hre
      cases him
      rfl

instance (D p : Nat) : Zero (QuadraticResidue D p) := ⟨⟨0, 0⟩⟩
instance (D p : Nat) : One (QuadraticResidue D p) := ⟨⟨1, 0⟩⟩
instance (D p : Nat) : Add (QuadraticResidue D p) :=
  ⟨fun a b => ⟨a.re + b.re, a.im + b.im⟩⟩
instance (D p : Nat) : Neg (QuadraticResidue D p) :=
  ⟨fun a => ⟨-a.re, -a.im⟩⟩
instance (D p : Nat) : Mul (QuadraticResidue D p) :=
  ⟨fun a b => ⟨a.re * b.re - (D : ZMod p) * a.im * b.im,
    a.re * b.im + a.im * b.re⟩⟩

@[simp] theorem zero_re (D p : Nat) : (0 : QuadraticResidue D p).re = 0 := rfl
@[simp] theorem zero_im (D p : Nat) : (0 : QuadraticResidue D p).im = 0 := rfl
@[simp] theorem one_re (D p : Nat) : (1 : QuadraticResidue D p).re = 1 := rfl
@[simp] theorem one_im (D p : Nat) : (1 : QuadraticResidue D p).im = 0 := rfl
@[simp] theorem add_re {D p : Nat} (a b : QuadraticResidue D p) :
    (a + b).re = a.re + b.re := rfl
@[simp] theorem add_im {D p : Nat} (a b : QuadraticResidue D p) :
    (a + b).im = a.im + b.im := rfl
@[simp] theorem neg_re {D p : Nat} (a : QuadraticResidue D p) :
    (-a).re = -a.re := rfl
@[simp] theorem neg_im {D p : Nat} (a : QuadraticResidue D p) :
    (-a).im = -a.im := rfl
@[simp] theorem mul_re {D p : Nat} (a b : QuadraticResidue D p) :
    (a * b).re = a.re * b.re - (D : ZMod p) * a.im * b.im := rfl
@[simp] theorem mul_im {D p : Nat} (a b : QuadraticResidue D p) :
    (a * b).im = a.re * b.im + a.im * b.re := rfl

instance (D p : Nat) : CommRing (QuadraticResidue D p) :=
  CommRing.ofMinimalAxioms
    (by intros; ext <;> simp [add_assoc])
    (by intros; ext <;> simp)
    (by intros; ext <;> simp)
    (by intros; ext <;> simp <;> ring)
    (by intros; ext <;> simp <;> ring)
    (by intros; ext <;> simp)
    (by intros; ext <;> simp <;> ring)

/-- The exact coordinate chart, with no quotienting of samples. -/
def ofPair (D p : Nat) (a : ZMod p × ZMod p) : QuadraticResidue D p :=
  ⟨a.1, a.2⟩

theorem ofPair_injective (D p : Nat) : Function.Injective (ofPair D p) := by
  intro a b h
  exact Prod.ext (congrArg re h) (congrArg im h)

theorem ofPair_mul (D p : Nat) (a b : ZMod p × ZMod p) :
    ofPair D p (residuePairMul D p a b) = ofPair D p a * ofPair D p b := rfl

theorem ofPair_pow (D p : Nat) (a : ZMod p × ZMod p) (n : Nat) :
    ofPair D p (residuePairPow D p a n) = (ofPair D p a) ^ n := by
  induction n with
  | zero => rfl
  | succ n ih => rw [residuePairPow, ofPair_mul, ih, pow_succ]

/-- The scalar copy of `ZMod p` and its quadratic generator. -/
def scalar (D p : Nat) : ZMod p →+* QuadraticResidue D p where
  toFun x := ⟨x, 0⟩
  map_one' := rfl
  map_mul' := by intros; ext <;> simp
  map_zero' := rfl
  map_add' := by intros; ext <;> simp

def generator (D p : Nat) : QuadraticResidue D p := ⟨0, 1⟩

theorem decompose (D p : Nat) (a : QuadraticResidue D p) :
    a = scalar D p a.re + scalar D p a.im * generator D p := by
  ext <;> simp [scalar, generator]

theorem ofPair_conj (D p : Nat) (a : ZMod p × ZMod p) :
    ofPair D p (residuePairConj a) =
      scalar D p a.1 - scalar D p a.2 * generator D p := by
  ext <;> simp [ofPair, residuePairConj, scalar, generator, sub_eq_add_neg]

end QuadraticResidue
end TenthDiscriminant
