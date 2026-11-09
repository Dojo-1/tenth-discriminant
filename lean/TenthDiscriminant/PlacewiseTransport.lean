import TenthDiscriminant.IntegerTraceGram

/-!
# Phase202: source-typed place-wise transport and restricted-pairing kernel

Do NOT identify a finite residue fibre with the Archimedean fibre.
The common datum is an integral ordinary-Z-jet observation source.

No class-number assumption, external selected minor, change of support,
or stronger discriminant bound enters these elementary algebraic lemmas.
The full dimension/rank formula is a separate formalization target.
-/

namespace TenthDiscriminant.Phase202
open Matrix
set_option autoImplicit false
noncomputable section

/-- The two integral observation channels of the original derivative row. -/
def sourceChannel (v : Int × Int) (c : Fin 2) : Int :=
  if c = 0 then v.1 else v.2

/-- Preserve the original trace weights 2 and 2D, even at p=2. -/
def sourceChannelWeight (D : Nat) (c : Fin 2) : Int :=
  if c = 0 then 2 else 2 * (D : Int)

/-- The actual original trace pairing splits into two typed channels.
This is not a change of derivative convention or lattice. -/
theorem original_trace_is_channel_pairing
    (D : Nat) (a b : Int × Int) :
    integerPairTrace D a b =
      ∑ c : Fin 2,
        sourceChannel a c * sourceChannelWeight D c * sourceChannel b c := by
  simp [integerPairTrace, sourceChannel, sourceChannelWeight, Fin.sum_univ_two] <;>
    ring

/-- The original finite jet Gram entry is exactly a sum of its two
integral channels with unchanged J, Q, derivative and row order. -/
theorem original_gram_entry_is_channel_sum
    (Q : Finset (Int × Int)) (D J r s t u : Nat) :
    integerTraceGramEntry Q D J r s t u =
      (Finset.range J).sum (fun j => Q.sum (fun p =>
        ∑ c : Fin 2,
          sourceChannel (integerDerivativeRow D r s j p) c *
          sourceChannelWeight D c *
          sourceChannel (integerDerivativeRow D t u j p) c)) := by
  simp only [integerTraceGramEntry, original_trace_is_channel_pairing]

/-- Ring base change is a separate map out of one integral source,
NOT an isomorphism across residue characteristics or places. -/
theorem integral_gram_basechange
    {n m : Nat} {T : Type*} [CommRing T]
    (E : Matrix (Fin n) (Fin m) Int)
    (B : Matrix (Fin m) (Fin m) Int)
    (f : Int →+* T) :
    (E * B * E.transpose).map f =
      E.map f * B.map f * (E.map f).transpose := by
  simp only [Matrix.map_mul, Matrix.transpose_map]

/-- Restricted radical: image of E^T annihilated under the B pairing.
The ambient form B is allowed to be degenerate in any characteristic. -/
def restrictedPairingRadical
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k) : Set (Fin m → k) :=
  {w | (∃ x : Fin n → k, E.transpose.mulVec x = w) ∧
       E.mulVec (B.mulVec w) = 0}

/-- Gram kernel maps exactly into the typed restricted pairing radical.
The kernel of E^T remains visible and is not silently collapsed. -/
theorem gram_kernel_iff_restricted_radical
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k)
    (x : Fin n → k) :
    (E * B * E.transpose).mulVec x = 0 ↔
      E.transpose.mulVec x ∈ restrictedPairingRadical E B := by
  change (E * B * E.transpose).mulVec x = 0 ↔
    (∃ y : Fin n → k, E.transpose.mulVec y = E.transpose.mulVec x) ∧
      E.mulVec (B.mulVec (E.transpose.mulVec x)) = 0
  constructor
  · intro h
    refine ⟨⟨x, rfl⟩, ?_⟩
    simpa only [Matrix.mulVec_mulVec, Matrix.mul_assoc] using h
  · rintro ⟨_, h⟩
    simpa only [Matrix.mulVec_mulVec, Matrix.mul_assoc] using h

/-- Surjectivity half of the kernel-radical exact sequence. -/
theorem radical_has_kernel_preimage
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k)
    (w : Fin m → k)
    (hw : w ∈ restrictedPairingRadical E B) :
    ∃ x : Fin n → k,
      (E * B * E.transpose).mulVec x = 0 ∧
      E.transpose.mulVec x = w := by
  rcases hw with ⟨⟨x, hx⟩, hzero⟩
  refine ⟨x, ?_, hx⟩
  rw [← hx] at hzero
  simpa only [Matrix.mulVec_mulVec, Matrix.mul_assoc] using hzero

end
end TenthDiscriminant.Phase202

#print axioms TenthDiscriminant.Phase202.integral_gram_basechange
#print axioms TenthDiscriminant.Phase202.gram_kernel_iff_restricted_radical
#print axioms TenthDiscriminant.Phase202.radical_has_kernel_preimage
