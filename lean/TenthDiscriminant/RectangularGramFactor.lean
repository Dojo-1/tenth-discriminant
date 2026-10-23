import TenthDiscriminant.RectangularRowAction

/-!
# Assemble the actual integral Gram after the rectangular row action

The pointwise row identity is already proved. This file keeps the
original finite sample indexing while using bilinearity of the same
factor-two trace pairing to build an integral two-sided factor.
-/
namespace TenthDiscriminant

open Polynomial

/-- The original factor-two integer trace pairing expressed in the
selected quadratic-order coordinates. -/
def zsqrtdTrace (D : Nat) (v w : Zsqrtd (-(D : Int))) : Int :=
  2 * (v.re * w.re + (D : Int) * v.im * w.im)

theorem zsqrtdTrace_pair (D : Nat) (a b : Int × Int) :
    zsqrtdTrace D (pairZsqrtdEquiv D a) (pairZsqrtdEquiv D b) =
      integerPairTrace D a b := by
  rfl

private theorem zsqrtdTrace_add_left (D : Nat)
    (a b c : Zsqrtd (-(D : Int))) :
    zsqrtdTrace D (a + b) c = zsqrtdTrace D a c + zsqrtdTrace D b c := by
  simp [zsqrtdTrace]
  ring

private theorem zsqrtdTrace_add_right (D : Nat)
    (a b c : Zsqrtd (-(D : Int))) :
    zsqrtdTrace D a (b + c) = zsqrtdTrace D a b + zsqrtdTrace D a c := by
  simp [zsqrtdTrace]
  ring

private theorem zsqrtdTrace_smul_left (D : Nat) (n : Int)
    (a b : Zsqrtd (-(D : Int))) :
    zsqrtdTrace D (n • a) b = n * zsqrtdTrace D a b := by
  simp [zsqrtdTrace, zsmul_eq_mul]
  ring

private theorem zsqrtdTrace_smul_right (D : Nat) (n : Int)
    (a b : Zsqrtd (-(D : Int))) :
    zsqrtdTrace D a (n • b) = zsqrtdTrace D a b * n := by
  simp [zsqrtdTrace, zsmul_eq_mul]
  ring

private theorem zsqrtdTrace_sum_left (D : Nat) {ι : Type*}
    (s : Finset ι) (f : ι → Zsqrtd (-(D : Int)))
    (b : Zsqrtd (-(D : Int))) :
    zsqrtdTrace D (∑ x ∈ s, f x) b =
      ∑ x ∈ s, zsqrtdTrace D (f x) b := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [zsqrtdTrace]
  | @insert x s hx ih =>
      simp only [Finset.sum_insert hx, zsqrtdTrace_add_left, ih]

private theorem zsqrtdTrace_sum_right (D : Nat) {ι : Type*}
    (s : Finset ι) (f : ι → Zsqrtd (-(D : Int)))
    (a : Zsqrtd (-(D : Int))) :
    zsqrtdTrace D a (∑ x ∈ s, f x) =
      ∑ x ∈ s, zsqrtdTrace D a (f x) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [zsqrtdTrace]
  | @insert x s hx ih =>
      simp only [Finset.sum_insert hx, zsqrtdTrace_add_right, ih]

/-- An integral Gram on the original sample set and derivative orders,
written in the same selected quadratic-order coordinates. -/
def zsqrtdJetGram {n : Nat} (Q : Finset (Int × Int)) (D J : Nat)
    (V : Fin n → Int × Int → Nat → Zsqrtd (-(D : Int))) :
    Matrix (Fin n) (Fin n) Int :=
  fun i l => (Finset.range J).sum fun j =>
    Q.sum fun a => zsqrtdTrace D (V i a j) (V l a j)

/-- Original canonical integer Gram, with no change of point set,
radius, row order, derivative order or factor-two normalization. -/
theorem zsqrtdJetGram_canonical (Q : Finset (Int × Int))
    (D J R S : Nat) :
    zsqrtdJetGram Q D J (fun i a j =>
      pairZsqrtdEquiv D
        (integerDerivativeRow D (i.val / S) (i.val % S) j a)) =
      integerRectangularTraceGram Q D J R S := by
  rfl

/-- Apply the given integer matrix to each original jet column. -/
def zsqrtdJetTransform {n : Nat} (U : Matrix (Fin n) (Fin n) Int)
    {D : Nat} (V : Fin n → Int × Int → Nat → Zsqrtd (-(D : Int)))
    (i : Fin n) (a : Int × Int) (j : Nat) : Zsqrtd (-(D : Int)) :=
  ∑ h : Fin n, U i h • V h a j

private theorem zsqrtdTrace_transform {n : Nat} (D : Nat)
    (U : Matrix (Fin n) (Fin n) Int)
    (v : Fin n → Zsqrtd (-(D : Int))) (i l : Fin n) :
    zsqrtdTrace D (∑ h : Fin n, U i h • v h)
      (∑ m : Fin n, U l m • v m) =
    ∑ m : Fin n, ∑ h : Fin n,
      U i h * zsqrtdTrace D (v h) (v m) * U l m := by
  rw [zsqrtdTrace_sum_right]
  apply Finset.sum_congr rfl
  intro m hm
  rw [zsqrtdTrace_smul_right, zsqrtdTrace_sum_left, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro h hh
  rw [zsqrtdTrace_smul_left]

private theorem sum_swap_four {α β γ δ : Type*}
    (sa : Finset α) (sb : Finset β) (sc : Finset γ) (sd : Finset δ)
    (f : α → β → γ → δ → Int) :
    (∑ a ∈ sa, ∑ b ∈ sb, ∑ c ∈ sc, ∑ d ∈ sd, f a b c d) =
      ∑ c ∈ sc, ∑ d ∈ sd, ∑ b ∈ sb, ∑ a ∈ sa, f a b c d := by
  classical
  calc
    _ = ∑ a ∈ sa, ∑ c ∈ sc, ∑ b ∈ sb, ∑ d ∈ sd, f a b c d := by
      apply Finset.sum_congr rfl
      intro a ha
      rw [Finset.sum_comm]
    _ = ∑ c ∈ sc, ∑ a ∈ sa, ∑ b ∈ sb, ∑ d ∈ sd, f a b c d := by
      rw [Finset.sum_comm]
    _ = ∑ c ∈ sc, ∑ a ∈ sa, ∑ d ∈ sd, ∑ b ∈ sb, f a b c d := by
      apply Finset.sum_congr rfl
      intro c hc
      apply Finset.sum_congr rfl
      intro a ha
      rw [Finset.sum_comm]
    _ = ∑ c ∈ sc, ∑ d ∈ sd, ∑ a ∈ sa, ∑ b ∈ sb, f a b c d := by
      apply Finset.sum_congr rfl
      intro c hc
      rw [Finset.sum_comm]
    _ = ∑ c ∈ sc, ∑ d ∈ sd, ∑ b ∈ sb, ∑ a ∈ sa, f a b c d := by
      apply Finset.sum_congr rfl
      intro c hc
      apply Finset.sum_congr rfl
      intro d hd
      rw [Finset.sum_comm]

/-- Bilinearity makes the same sample-indexed Gram transform on both
sides by `U`; no residue-image set or substitute matrix is introduced. -/
theorem zsqrtdJetGram_transform {n : Nat} (Q : Finset (Int × Int))
    (D J : Nat) (U : Matrix (Fin n) (Fin n) Int)
    (V : Fin n → Int × Int → Nat → Zsqrtd (-(D : Int))) :
    zsqrtdJetGram Q D J (zsqrtdJetTransform U V) =
      U * zsqrtdJetGram Q D J V * U.transpose := by
  classical
  ext i l
  simp only [zsqrtdJetGram, zsqrtdJetTransform, Matrix.mul_apply,
    Matrix.transpose_apply]
  simp_rw [zsqrtdTrace_transform]
  simp only [Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  exact sum_swap_four Q (Finset.range J) Finset.univ Finset.univ
    (fun a j m h => U i h * zsqrtdTrace D (V h a j) (V m a j) * U l m)

/-- If every observed jet has an integral row factor, the Gram has
that factor on both sides. This includes the shared diagonal pivot. -/
theorem zsqrtdJetGram_scale {n : Nat} (Q : Finset (Int × Int))
    (D J : Nat)
    (V W : Fin n → Int × Int → Nat → Zsqrtd (-(D : Int)))
    (d : Fin n → Int)
    (hscale : ∀ i a j, a ∈ Q → j ∈ Finset.range J →
      V i a j = d i • W i a j) :
    zsqrtdJetGram Q D J V =
      Matrix.diagonal d * zsqrtdJetGram Q D J W * Matrix.diagonal d := by
  ext i l
  simp only [Matrix.mul_diagonal, Matrix.diagonal_mul, zsqrtdJetGram]
  calc
    (∑ j ∈ Finset.range J, ∑ a ∈ Q,
      zsqrtdTrace D (V i a j) (V l a j)) =
      ∑ j ∈ Finset.range J, ∑ a ∈ Q,
        d i * zsqrtdTrace D (W i a j) (W l a j) * d l := by
      apply Finset.sum_congr rfl
      intro j hj
      apply Finset.sum_congr rfl
      intro a ha
      rw [hscale i a j ha hj, hscale l a j ha hj,
        zsqrtdTrace_smul_left, zsqrtdTrace_smul_right]
      ring
    _ = d i *
        (∑ j ∈ Finset.range J, ∑ a ∈ Q,
          zsqrtdTrace D (W i a j) (W l a j)) * d l := by
      simp [Finset.mul_sum, Finset.sum_mul]

/-- The original ordered integer derivative rows, merely expressed in
the selected quadratic-order chart. -/
def rectangularCanonicalJet (D R S : Nat) :
    Fin (R * S) → Int × Int → Nat → Zsqrtd (-(D : Int)) :=
  fun i a j => pairZsqrtdEquiv D
    (integerDerivativeRow D (i.val / S) (i.val % S) j a)

/-- Choose integral quotients of the transformed *actual* jets. The
choice is possible from the checked samplewise row identity and jet
power theorem; it is not a replacement observation family. -/
noncomputable def rectangularNormalizedJet
    (D R S p : Nat) (hp : 0 < p)
    (hzero : ∀ a : Int × Int,
      (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    Fin (R * S) → Int × Int → Nat → Zsqrtd (-(D : Int)) :=
  fun i a j => Classical.choose
    (rectangularBasisMatrix_actualRow_dvd D R S p hp i a j (hzero a))

theorem rectangularTransformedJet_scale
    (D R S p : Nat) (hp : 0 < p)
    (hzero : ∀ a : Int × Int,
      (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2)
    (i : Fin (R * S)) (a : Int × Int) (j : Nat) :
    zsqrtdJetTransform (rectangularBasisMatrix R S p)
      (rectangularCanonicalJet D R S) i a j =
      ((p : Int) ^ rectangularBasisExponent R S p i) •
        rectangularNormalizedJet D R S p hp hzero i a j := by
  have h := Classical.choose_spec
    (rectangularBasisMatrix_actualRow_dvd D R S p hp i a j (hzero a))
  simpa only [zsqrtdJetTransform, rectangularCanonicalJet,
    rectangularNormalizedJet, zsmul_eq_mul, Int.cast_pow,
    Int.cast_natCast] using h

/-- Construct the previously assumed integral middle matrix for the
repository's actual rectangular Gram, under the explicit pointwise
Frobenius premise. The sum still runs over the original finite `Q`. -/
theorem rectangularTraceGram_basis_factor_of_frobenius
    (Q : Finset (Int × Int)) (D J R S p : Nat) (hp : 0 < p)
    (hzero : ∀ a : Int × Int,
      (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    ∃ K : Matrix (Fin (R * S)) (Fin (R * S)) Int,
      rectangularBasisMatrix R S p *
          integerRectangularTraceGram Q D J R S *
          (rectangularBasisMatrix R S p).transpose =
        Matrix.diagonal (fun i => (p : Int) ^
          rectangularBasisExponent R S p i) * K *
        Matrix.diagonal (fun i => (p : Int) ^
          rectangularBasisExponent R S p i) := by
  classical
  refine ⟨zsqrtdJetGram Q D J
    (rectangularNormalizedJet D R S p hp hzero), ?_⟩
  calc
    rectangularBasisMatrix R S p *
        integerRectangularTraceGram Q D J R S *
        (rectangularBasisMatrix R S p).transpose =
      zsqrtdJetGram Q D J
        (zsqrtdJetTransform (rectangularBasisMatrix R S p)
          (rectangularCanonicalJet D R S)) := by
        rw [zsqrtdJetGram_transform]
        change rectangularBasisMatrix R S p *
            integerRectangularTraceGram Q D J R S *
            (rectangularBasisMatrix R S p).transpose =
          rectangularBasisMatrix R S p *
            zsqrtdJetGram Q D J (fun i a j =>
              pairZsqrtdEquiv D
                (integerDerivativeRow D (i.val / S) (i.val % S) j a)) *
            (rectangularBasisMatrix R S p).transpose
        rw [zsqrtdJetGram_canonical]
    _ = Matrix.diagonal (fun i => (p : Int) ^
          rectangularBasisExponent R S p i) *
        zsqrtdJetGram Q D J
          (rectangularNormalizedJet D R S p hp hzero) *
        Matrix.diagonal (fun i => (p : Int) ^
          rectangularBasisExponent R S p i) := by
        apply zsqrtdJetGram_scale
        intro i a j ha hj
        exact rectangularTransformedJet_scale D R S p hp hzero i a j

/-- The general integer determinant has Ender's exact `2F(p)` factor
once the zero-order Frobenius congruence is supplied for all samples.
No irreducibility, inertness or class-number conclusion is hidden in
this theorem: proving that universal premise is a separate bridge. -/
theorem rectangularTraceGram_valuation_of_frobenius
    (Q : Finset (Int × Int)) (D J R S p : Nat) (hp : 0 < p)
    (hzero : ∀ a : Int × Int,
      (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  obtain ⟨K, hfactor⟩ :=
    rectangularTraceGram_basis_factor_of_frobenius Q D J R S p hp hzero
  exact rectangularTraceGram_valuation_of_basis_factor
    Q D J R S p (rectangularBasisMatrix R S p) K
    (rectangularBasisMatrix_det R S p hp) hfactor

end TenthDiscriminant
