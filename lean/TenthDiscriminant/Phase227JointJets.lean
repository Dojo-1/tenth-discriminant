import TenthDiscriminant.Phase226HorizontalIntegral
import TenthDiscriminant.RankDivisorCompatibility

/-!
# Phase227: the TWO integral Frobenius weights on ONE original ordinary jet row

The two independent ROW OPERATORS do not commute. We do not apply them
in succession. Instead, one explicitly written source polynomial contains
both factors: (Z^p-W)^k * (W^(p*p)-W)^ell. The higher ordinary Leibniz rule
proves an additive p^(k+ell) divisor of all its original Z-jets.

The module separately checks the full labeled maximal-minor invariance
under a genuinely unimodular integral source-frame change. Neither
result asserts the combined rectangular basis has determinant one:
that finite-basis matrix and the same-original-Gram determinant theorem
remain separate obligations.
-/

namespace TenthDiscriminant.Phase227

open Polynomial
open scoped BigOperators

/-- A weighted Leibniz rule: two independently divisible jet systems
carry the SUM of their weights in a single product. We retain every
ordinary derivative, with no Hasse-derivative substitution. -/
theorem ordinary_jet_mul_additive_dvd {A : Type*} [CommRing A]
    (P Q : A[X]) (z q : A) (k ell j : Nat)
    (hP : ∀ t : Nat, q ^ k ∣ (derivative^[t] P).eval z)
    (hQ : ∀ t : Nat, q ^ ell ∣ (derivative^[t] Q).eval z) :
    q ^ (k + ell) ∣ (derivative^[j] (P * Q)).eval z := by
  rw [iterate_derivative_mul, eval_finset_sum]
  apply Finset.dvd_sum
  intro t ht
  obtain ⟨u, hu⟩ := hP (j - t)
  obtain ⟨v, hv⟩ := hQ t
  rw [eval_smul, eval_mul, nsmul_eq_mul, hu, hv, pow_add]
  refine ⟨(j.choose t : A) * (u * v), ?_⟩
  ring

/-- Two source factors whose entire ordinary jet towers are divisible
by q yield q^(k+ell). Separate q^k and q^ell certificates are NOT
simply added after taking the determinant. This is the joint witness. -/
theorem two_factor_ordinary_jet_dvd {A : Type*} [CommRing A]
    (B H G : A[X]) (z q : A) (k ell j : Nat)
    (hH : ∀ t : Nat, q ∣ (derivative^[t] H).eval z)
    (hG : ∀ t : Nat, q ∣ (derivative^[t] G).eval z) :
    q ^ (k + ell) ∣
      (derivative^[j] ((B * H ^ k) * G ^ ell)).eval z := by
  apply ordinary_jet_mul_additive_dvd (B * H ^ k) (G ^ ell) z q k ell j
  · exact jet_power_dvd B H z q hH k
  · intro t
    simpa only [one_mul] using
      (jet_power_dvd (1 : A[X]) G z q hG ell t)

/-- The combined vertical Z^p-W and horizontal W^(p*p)-W factors act
simultaneously on ONE original sample in the selected integral order.
This is genuinely additive in all ordinary derivative orders. -/
theorem combined_frobenius_ordinary_jet_dvd
    (D p : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : Int × Int)
    (B : (Zsqrtd (-(D : Int)))[X]) (k ell j : Nat) :
    let z := pairZsqrtdEquiv D a
    let w := star z
    (p : Zsqrtd (-(D : Int))) ^ (k + ell) ∣
      (derivative^[j] ((B * (X ^ p - C w) ^ k) *
        (C (w ^ (p * p) - w)) ^ ell)).eval z := by
  dsimp
  let z : Zsqrtd (-(D : Int)) := pairZsqrtdEquiv D a
  let w : Zsqrtd (-(D : Int)) := star z
  have hv : (p : Zsqrtd (-(D : Int))) ∣ z ^ p - w := by
    simpa [z, w] using pair_frobenius_congruence_zsqrtd D p a
      (integerPair_frobenius_of_nonsquare D p hp2 hnonsquare a)
  have hh : (p : Zsqrtd (-(D : Int))) ∣ w ^ (p * p) - w := by
    simpa [z, w] using
      Phase226.horizontal_zsqrtd_frobenius_squared D p hp2 hnonsquare a
  apply two_factor_ordinary_jet_dvd B (X ^ p - C w)
    (C (w ^ (p * p) - w)) z
    (p : Zsqrtd (-(D : Int))) k ell j
  · intro t
    exact frobenius_polynomial_jet_dvd z w p t hv
  · intro t
    by_cases ht : t = 0
    · subst t
      simpa using hh
    · rw [iterate_derivative_C (Nat.pos_of_ne_zero ht)]
      simp

/-- The original rectangular monomial carrier, with BOTH Frobenius
factors, is divisible by p^(k+ell) in every original ordinary jet.
Bounds that keep these rows in the original rectangle, and the
integer matrix identifying them, are separate theorems. -/
theorem combined_rectangular_row_ordinary_jet_dvd
    (D p r s k ell j : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : Int × Int) :
    let z := pairZsqrtdEquiv D a
    let w := star z
    (p : Zsqrtd (-(D : Int))) ^ (k + ell) ∣
      (derivative^[j]
        (((X ^ (r - p * k) * C w ^ (s - (p * p) * ell)) *
          (X ^ p - C w) ^ k) *
          (C (w ^ (p * p) - w)) ^ ell)).eval z := by
  dsimp
  exact combined_frobenius_ordinary_jet_dvd D p hp2 hnonsquare a
    (X ^ (r - p * k) *
      C (star (pairZsqrtdEquiv D a)) ^ (s - (p * p) * ell))
    k ell j

/-- In an integral determinant-one source frame, EVERY LABELED maximal
observation minor is preserved. This records the full Plucker data
without compressing it into a scalar determinant. -/
theorem every_labeled_maximal_minor_preserved
    {n m : Nat}
    (E : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (hU : U.det = 1)
    (cols : Fin n → Fin m) :
    (selectedColumns (U * E) cols).det =
      (selectedColumns E cols).det := by
  rw [selectedColumns_mul_left, Matrix.det_mul, hU, one_mul]

/-- An arbitrary integral change of frame scales every labeled
maximal minor by its source determinant: when that determinant is not
a unit, it is NOT a gauge transformation of the same source lattice. -/
theorem every_labeled_maximal_minor_scale
    {n m : Nat}
    (E : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (cols : Fin n → Fin m) :
    (selectedColumns (U * E) cols).det =
      U.det * (selectedColumns E cols).det := by
  rw [selectedColumns_mul_left, Matrix.det_mul]

end TenthDiscriminant.Phase227

#print axioms TenthDiscriminant.Phase227.ordinary_jet_mul_additive_dvd
#print axioms TenthDiscriminant.Phase227.two_factor_ordinary_jet_dvd
#print axioms TenthDiscriminant.Phase227.combined_frobenius_ordinary_jet_dvd
#print axioms TenthDiscriminant.Phase227.combined_rectangular_row_ordinary_jet_dvd
#print axioms TenthDiscriminant.Phase227.every_labeled_maximal_minor_preserved
#print axioms TenthDiscriminant.Phase227.every_labeled_maximal_minor_scale
