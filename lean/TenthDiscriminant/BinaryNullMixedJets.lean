import TenthDiscriminant.BinaryNullOrdinaryJets

/-!
# Phase163: a reusable four-factor ordinary-jet product principle

This is a source-independent algebraic lemma about ORDINARY derivatives.
It does not replace the original rectangular row matrix, does not claim
the Phase162 four-generator exponent 1358, and does not change the field
endpoint. It is the reusable induction bridge needed before proving the
particular F(Z), H(Z,W), F(W), K(Z,W) source generators.
-/

namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false

/-- If the j-th ordinary derivative of P has q^m and that of H has q^n,
the derivative of P*H has q^(m+n), with no factorial inversion. -/
theorem mixedJets_mul_dvd {A : Type*} [CommRing A]
    (P H : A[X]) (z q : A) (m n : Nat)
    (hP : ∀ j : Nat, q^m ∣ (derivative^[j] P).eval z)
    (hH : ∀ j : Nat, q^n ∣ (derivative^[j] H).eval z)
    (j : Nat) :
    q^(m+n) ∣ (derivative^[j] (P*H)).eval z := by
  rw [iterate_derivative_mul, eval_finset_sum]
  apply Finset.dvd_sum
  intro t ht
  obtain ⟨u, hu⟩ := hP (j-t)
  obtain ⟨v, hv⟩ := hH t
  rw [eval_smul, eval_mul, nsmul_eq_mul, hu, hv, pow_add]
  refine ⟨(j.choose t : A) * (u*v), ?_⟩
  ring

/-- Four different null polynomials contribute the SUM of their
exponents. In the future, the intended four are F(Z), H(Z,W),
F(W), K(Z,W) at W=conj(Z). The four divisibility premises MUST
be proved for each true source sample, not asserted from an unrelated
surrogate polynomial or a Hasse derivative. -/
theorem mixedJets_fourPowers_dvd {A : Type*} [CommRing A]
    (B F H L K : A[X]) (z q : A)
    (a b c d j : Nat)
    (hF : ∀ t : Nat, q ∣ (derivative^[t] F).eval z)
    (hH : ∀ t : Nat, q ∣ (derivative^[t] H).eval z)
    (hL : ∀ t : Nat, q ∣ (derivative^[t] L).eval z)
    (hK : ∀ t : Nat, q ∣ (derivative^[t] K).eval z) :
    q^(a+b+c+d) ∣
      (derivative^[j] (B*F^a*H^b*L^c*K^d)).eval z := by
  have hFa : ∀ t : Nat, q^a ∣
      (derivative^[t] (B*F^a)).eval z :=
    jet_power_dvd B F z q hF a
  have hHb : ∀ t : Nat, q^b ∣
      (derivative^[t] (H^b)).eval z := by
    intro t
    simpa only [one_mul] using
      (jet_power_dvd (1 : A[X]) H z q hH b t)
  have hLc : ∀ t : Nat, q^c ∣
      (derivative^[t] (L^c)).eval z := by
    intro t
    simpa only [one_mul] using
      (jet_power_dvd (1 : A[X]) L z q hL c t)
  have hKd : ∀ t : Nat, q^d ∣
      (derivative^[t] (K^d)).eval z := by
    intro t
    simpa only [one_mul] using
      (jet_power_dvd (1 : A[X]) K z q hK d t)
  have hFH : ∀ t : Nat, q^(a+b) ∣
      (derivative^[t] (B*F^a*H^b)).eval z :=
    fun t => mixedJets_mul_dvd (B*F^a) (H^b) z q a b hFa hHb t
  have hFHL : ∀ t : Nat, q^(a+b+c) ∣
      (derivative^[t] (B*F^a*H^b*L^c)).eval z :=
    fun t => mixedJets_mul_dvd (B*F^a*H^b) (L^c) z q
      (a+b) c hFH hLc t
  exact mixedJets_mul_dvd (B*F^a*H^b*L^c) (K^d)
    z q (a+b+c) d hFHL hKd j

/-- A source-grounded regression: the polynomial F(Z)=Z^4-Z^2
already has its all-orders null property in the selected order.
Using it repeatedly tests the four-factor composition without
claiming the distinct mixed-generator construction. -/
theorem mixedJets_fourF_source_control
    (D : Nat) (sample : Int × Int)
    (B : (Zsqrtd (-(D : Int)))[X])
    (a b c d j : Nat) :
    let z := pairZsqrtdEquiv D sample
    let F : (Zsqrtd (-(D : Int)))[X] := X^4-X^2
    (2 : Zsqrtd (-(D : Int)))^(a+b+c+d) ∣
      (derivative^[j] (B*F^a*F^b*F^c*F^d)).eval z := by
  dsimp
  exact mixedJets_fourPowers_dvd B
    (X^4-X^2) (X^4-X^2) (X^4-X^2) (X^4-X^2)
    (pairZsqrtdEquiv D sample) (2 : Zsqrtd (-(D : Int)))
    a b c d j
    (binaryNull_allOrdinaryJets_dvd D sample)
    (binaryNull_allOrdinaryJets_dvd D sample)
    (binaryNull_allOrdinaryJets_dvd D sample)
    (binaryNull_allOrdinaryJets_dvd D sample)

end TenthDiscriminant
