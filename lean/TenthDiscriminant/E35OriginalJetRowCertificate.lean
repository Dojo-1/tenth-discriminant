import TenthDiscriminant.E34OriginalGramPrimeFactor

/-!
# E35 — Original ordinary-jet row certificate implies true Gram factor

E34 uses entrywise divisibility conditions on the original entire
two-row integerRectangularTraceGram. This module discharges those
conditions directly from the ORIGINAL integerDerivativeRow values at
EVERY sampled point and EVERY ordinary derivative index.

No ambient conductor-kernel substitution is allowed.
The price is an explicit strong source hypothesis:
all real/imag coefficients of the second ORIGINAL jet row are
divisible by p at all (j,q) in the finite original sample support.

This provides a source-to-entry-to-determinant factor bridge
for exactly two rectangular rows. It is NOT the full multirow
thin-ellipse prime-mass proof and does not sharpen 307^4.
-/

namespace TenthDiscriminant.E35
set_option autoImplicit false
noncomputable section

/-- The original integer trace pairing is symmetric in its two source
jets: this uses the SAME positive trace metric 2*(ac+D*bd). -/
private theorem pair_trace_symm (D : Nat) (a b : Int × Int) :
    integerPairTrace D a b = integerPairTrace D b a := by
  simp [integerPairTrace]
  ring

/-- A p-divisible ORIGINAL second jet is p-divisible in its positive
integer trace pairing with every other original jet. -/
private theorem trace_dvd_right
    (D : Nat) (p : Int) (a b : Int × Int)
    (hb1 : p ∣ b.1) (hb2 : p ∣ b.2) :
    p ∣ integerPairTrace D a b := by
  rcases hb1 with ⟨u,hu⟩
  rcases hb2 with ⟨v,hv⟩
  refine ⟨2*(a.1*u + (D : Int)*a.2*v), ?_⟩
  dsimp [integerPairTrace]
  rw [hu,hv]
  ring

/-- If BOTH original jets are p-divisible in each integer
coefficient, their trace pairing has a genuine p² factor. -/
private theorem trace_dvd_both_sq
    (D : Nat) (p : Int) (a b : Int × Int)
    (ha1 : p ∣ a.1) (ha2 : p ∣ a.2)
    (hb1 : p ∣ b.1) (hb2 : p ∣ b.2) :
    p*p ∣ integerPairTrace D a b := by
  rcases ha1 with ⟨u,hu⟩
  rcases ha2 with ⟨v,hv⟩
  rcases hb1 with ⟨w,hw⟩
  rcases hb2 with ⟨z,hz⟩
  refine ⟨2*(u*w + (D : Int)*v*z), ?_⟩
  dsimp [integerPairTrace]
  rw [hu,hv,hw,hz]
  ring

private theorem entry_trace_symm
    (Q : Finset (Int × Int)) (D J r s t u : Nat) :
    integerTraceGramEntry Q D J r s t u =
      integerTraceGramEntry Q D J t u r s := by
  unfold integerTraceGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  apply Finset.sum_congr rfl
  intro q hq
  exact pair_trace_symm D
    (integerDerivativeRow D r s j q)
    (integerDerivativeRow D t u j q)

/-- Every ORIGINAL ordinary jet of the second rectangular row
belongs to p times the original integral coefficient lattice. -/
def SecondRowJetDivisible
    (Q : Finset (Int × Int)) (D J : Nat) (p : Int) : Prop :=
  ∀ j ∈ Finset.range J, ∀ q ∈ Q,
    p ∣ (integerDerivativeRow D 1 0 j q).1 ∧
    p ∣ (integerDerivativeRow D 1 0 j q).2

private theorem entry_01_divides
    (Q : Finset (Int × Int)) (D J : Nat) (p : Int)
    (h : SecondRowJetDivisible Q D J p) :
    p ∣ integerTraceGramEntry Q D J 0 0 1 0 := by
  unfold integerTraceGramEntry
  apply Finset.dvd_sum
  intro j hj
  apply Finset.dvd_sum
  intro q hq
  have hqj := h j hj q hq
  exact trace_dvd_right D p
    (integerDerivativeRow D 0 0 j q)
    (integerDerivativeRow D 1 0 j q)
    hqj.1 hqj.2

private theorem entry_10_divides
    (Q : Finset (Int × Int)) (D J : Nat) (p : Int)
    (h : SecondRowJetDivisible Q D J p) :
    p ∣ integerTraceGramEntry Q D J 1 0 0 0 := by
  rw [entry_trace_symm]
  exact entry_01_divides Q D J p h

private theorem entry_11_sq_divides
    (Q : Finset (Int × Int)) (D J : Nat) (p : Int)
    (h : SecondRowJetDivisible Q D J p) :
    p*p ∣ integerTraceGramEntry Q D J 1 0 1 0 := by
  unfold integerTraceGramEntry
  apply Finset.dvd_sum
  intro j hj
  apply Finset.dvd_sum
  intro q hq
  have hqj := h j hj q hq
  exact trace_dvd_both_sq D p
    (integerDerivativeRow D 1 0 j q)
    (integerDerivativeRow D 1 0 j q)
    hqj.1 hqj.2 hqj.1 hqj.2

/-- UNIVERSAL two-row *original-jet* source certificate.
The source premise is about every actual ordinary derivative point,
not a conductor frame, heuristic kernel, local ideal, or selected minor. -/
theorem original_two_row_jet_factor
    (Q : Finset (Int × Int)) (D J : Nat) (p : Int)
    (h : SecondRowJetDivisible Q D J p) :
    p*p ∣ (integerRectangularTraceGram Q D J 2 1).det := by
  have h01 : p ∣ (integerRectangularTraceGram Q D J 2 1) 0 1 := by
    change p ∣ integerTraceGramEntry Q D J 0 0 1 0
    exact entry_01_divides Q D J p h
  have h10 : p ∣ (integerRectangularTraceGram Q D J 2 1) 1 0 := by
    change p ∣ integerTraceGramEntry Q D J 1 0 0 0
    exact entry_10_divides Q D J p h
  have h11 : p*p ∣ (integerRectangularTraceGram Q D J 2 1) 1 1 := by
    change p*p ∣ integerTraceGramEntry Q D J 1 0 1 0
    exact entry_11_sq_divides Q D J p h
  exact E34.original_two_row_gram_prime_factor Q D J p h01 h10 h11

/-- The positive E34 original source Q_five ACTUALLY satisfies every
jet-wise hypothesis at D=25, J=1, without any modified sampling. -/
theorem qfive_original_jet_row_is_divisible :
    SecondRowJetDivisible E34.realFiveSource 25 1 5 := by
  intro j hj q hq
  have hj0 : j = 0 := by
    have hh := Finset.mem_range.mp hj
    omega
  subst j
  have hqcases : q = (0,0) ∨ q = (5,0) := by
    simpa [E34.realFiveSource] using hq
  rcases hqcases with heq | heq
  · subst q
    decide
  · subst q
    decide

/-- Instantiate source-jet, source-entry, then actual-det factoring. -/
theorem qfive_jet_certificate_for_gram_factor :
    ((5 : Int)*5) ∣
      (integerRectangularTraceGram E34.realFiveSource 25 1 2 1).det := by
  exact original_two_row_jet_factor E34.realFiveSource 25 1 5
    qfive_original_jet_row_is_divisible

/-- Matched negative source Q_unit fails the needed actual source
ordinary-jet premise; an ambient conductor kernel cannot rescue it. -/
theorem qunit_fails_jet_row_certificate :
    ¬ SecondRowJetDivisible E31.realSource 25 1 5 := by
  intro h
  have hj : 0 ∈ Finset.range 1 := by decide
  have hq : (1,0) ∈ E31.realSource := by decide
  have hbad := (h 0 hj (1,0) hq).1
  have hnot :
      ¬ ((5 : Int) ∣ (integerDerivativeRow 25 1 0 0 (1,0)).1) := by
    decide
  exact hnot hbad

end
end TenthDiscriminant.E35

#print axioms TenthDiscriminant.E35.original_two_row_jet_factor
#print axioms TenthDiscriminant.E35.qfive_original_jet_row_is_divisible
#print axioms TenthDiscriminant.E35.qfive_jet_certificate_for_gram_factor
#print axioms TenthDiscriminant.E35.qunit_fails_jet_row_certificate
