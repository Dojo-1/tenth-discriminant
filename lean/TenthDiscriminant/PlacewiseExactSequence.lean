import TenthDiscriminant.PlacewiseTransport

/-!
# Phase203-A: elementwise exactness of the integral-source Gram kernel

The carrier is the SAME integer ordinary-Z-jet source already encoded in
IntegerTraceGram, transported to a SINGLE field k through the matrix
base-change theorem in Phase202. We prove the abstract kernel/radical
exactness for each such field, including characteristic 2.

No equation identifies fibres over distinct primes or with Real.
No external minor is substituted for the integer trace Gram.
The separate finrank formula remains a future Lean target.
-/

namespace TenthDiscriminant.Phase203
open Matrix
open TenthDiscriminant.Phase202
set_option autoImplicit false
noncomputable section

/-- Every vector killed by the transpose evaluation map is also
killed by the associated Gram; no nondegeneracy assumption on B. -/
theorem transpose_kernel_into_gram_kernel
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k)
    (x : Fin n → k)
    (hx : E.transpose.mulVec x = 0) :
    (E * B * E.transpose).mulVec x = 0 := by
  apply (gram_kernel_iff_restricted_radical E B x).2
  change (∃ y : Fin n → k,
      E.transpose.mulVec y = E.transpose.mulVec x) ∧
      E.mulVec (B.mulVec (E.transpose.mulVec x)) = 0
  refine ⟨⟨x, rfl⟩, ?_⟩
  simp [hx]

/-- The exact image of the Gram kernel under E transpose is precisely
the restricted pairing radical, with no hidden injectivity assumption. -/
theorem radical_iff_transpose_of_gram_kernel
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k)
    (w : Fin m → k) :
    w ∈ restrictedPairingRadical E B ↔
      ∃ x : Fin n → k,
        (E * B * E.transpose).mulVec x = 0 ∧
        E.transpose.mulVec x = w := by
  constructor
  · intro hw
    exact radical_has_kernel_preimage E B w hw
  · rintro ⟨x, hgram, himage⟩
    rw [← himage]
    exact (gram_kernel_iff_restricted_radical E B x).1 hgram

/-- The three elementwise exactness properties, separately typed.
This theorem does not claim a dependent-type short exact sequence API
or a rank identity until those objects are separately constructed. -/
theorem kernel_radical_elementwise_exact
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k) :
    (∀ x : Fin n → k,
        E.transpose.mulVec x = 0 →
        (E * B * E.transpose).mulVec x = 0) ∧
    (∀ x : Fin n → k,
        (E * B * E.transpose).mulVec x = 0 →
        E.transpose.mulVec x ∈ restrictedPairingRadical E B) ∧
    (∀ w : Fin m → k,
        w ∈ restrictedPairingRadical E B →
        ∃ x : Fin n → k,
          (E * B * E.transpose).mulVec x = 0 ∧
          E.transpose.mulVec x = w) := by
  refine ⟨?_, ?_, ?_⟩
  · intro x hx
    exact transpose_kernel_into_gram_kernel E B x hx
  · intro x hx
    exact (gram_kernel_iff_restricted_radical E B x).1 hx
  · intro w hw
    exact radical_has_kernel_preimage E B w hw

/-- Triviality of the restricted pairing radical is equivalent to
equality of the two zero-loci; it does NOT follow from evaluation
rank alone over a finite field. -/
theorem gram_kernel_no_extra_vectors_iff_radical_trivial
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k) :
    (∀ x : Fin n → k,
       (E * B * E.transpose).mulVec x = 0 →
       E.transpose.mulVec x = 0) ↔
    (∀ w : Fin m → k,
       w ∈ restrictedPairingRadical E B → w = 0) := by
  constructor
  · intro h w hw
    obtain ⟨x, hg, he⟩ := radical_has_kernel_preimage E B w hw
    calc
      w = E.transpose.mulVec x := he.symm
      _ = 0 := h x hg
  · intro h x hg
    exact h (E.transpose.mulVec x)
      ((gram_kernel_iff_restricted_radical E B x).1 hg)

/-- A reversible change of SOURCE frame leaves the restricted
observation-pairing radical exactly unchanged.  The observation module
and the channel pairing B are fixed; no p-adic or Archimedean fibres
are silently identified.  The left inverse suffices for this square
finite-dimensional frame. -/
theorem restricted_radical_unimodular_source_frame
    {k : Type*} [Field k] {n m : Nat}
    (E : Matrix (Fin n) (Fin m) k)
    (B : Matrix (Fin m) (Fin m) k)
    (U V : Matrix (Fin n) (Fin n) k)
    (hVU : V * U = 1) :
    restrictedPairingRadical (U * E) B =
      restrictedPairingRadical E B := by
  ext w
  change ((∃ x : Fin n → k,
      (U * E).transpose.mulVec x = w) ∧
      (U * E).mulVec (B.mulVec w) = 0) ↔
    ((∃ x : Fin n → k, E.transpose.mulVec x = w) ∧
      E.mulVec (B.mulVec w) = 0)
  have ht : U.transpose * V.transpose = 1 := by
    simpa only [Matrix.transpose_mul, Matrix.transpose_one] using
      congrArg (fun M => M.transpose) hVU
  constructor
  · rintro ⟨⟨x, hx⟩, hz⟩
    constructor
    · refine ⟨U.transpose.mulVec x, ?_⟩
      simpa only [Matrix.transpose_mul, Matrix.mulVec_mulVec] using hx
    · have hh := congrArg (fun z : Fin n → k => V.mulVec z) hz
      simpa only [Matrix.mulVec_mulVec, ← Matrix.mul_assoc, hVU,
        Matrix.one_mul, Matrix.mulVec_zero] using hh
  · rintro ⟨⟨x, hx⟩, hz⟩
    constructor
    · refine ⟨V.transpose.mulVec x, ?_⟩
      calc
        (U * E).transpose.mulVec (V.transpose.mulVec x) =
            E.transpose.mulVec ((U.transpose * V.transpose).mulVec x) := by
              simp only [Matrix.transpose_mul, Matrix.mulVec_mulVec]
        _ = E.transpose.mulVec x := by simp [ht]
        _ = w := hx
    · have hh := congrArg (fun z : Fin n → k => U.mulVec z) hz
      simpa only [Matrix.mulVec_mulVec, Matrix.mulVec_zero] using hh

end
end TenthDiscriminant.Phase203

#print axioms TenthDiscriminant.Phase203.transpose_kernel_into_gram_kernel
#print axioms TenthDiscriminant.Phase203.radical_iff_transpose_of_gram_kernel
#print axioms TenthDiscriminant.Phase203.kernel_radical_elementwise_exact
#print axioms TenthDiscriminant.Phase203.gram_kernel_no_extra_vectors_iff_radical_trivial

#print axioms TenthDiscriminant.Phase203.restricted_radical_unimodular_source_frame
