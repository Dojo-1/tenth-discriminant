import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Polynomial.Eval.SMul
import Mathlib.Algebra.Polynomial.HasseDeriv
import TenthDiscriminant.QuadraticCoordinates

/-!
# Ordinary jets of a polynomial power

The sole mechanism here is the ordinary higher Leibniz rule. If every
jet of `H` at `z` is divisible by `q`, then every jet of `B * H^k` is
divisible by `q^k`. This is the product-power link required by the
rectangular `Z^p-W` construction; identifying that construction with
the existing integer-coordinate rows is a separate obligation.
-/
namespace TenthDiscriminant

open Polynomial

private theorem jet_mul_dvd {A : Type*} [CommRing A]
    (P H : A[X]) (z q : A) (m : Nat)
    (hP : ∀ j : Nat, q ^ m ∣ (derivative^[j] P).eval z)
    (hH : ∀ j : Nat, q ∣ (derivative^[j] H).eval z)
    (j : Nat) :
    q ^ (m + 1) ∣ (derivative^[j] (P * H)).eval z := by
  rw [iterate_derivative_mul, eval_finset_sum]
  apply Finset.dvd_sum
  intro t ht
  obtain ⟨u, hu⟩ := hP (j - t)
  obtain ⟨v, hv⟩ := hH t
  rw [eval_smul, eval_mul, nsmul_eq_mul, hu, hv, pow_succ]
  refine ⟨(j.choose t : A) * (u * v), ?_⟩
  ring

/-- Every ordinary jet of `B * H^k` inherits `k` factors of `q` when
every ordinary jet of `H` has one. No factorials are inverted. -/
theorem jet_power_dvd {A : Type*} [CommRing A]
    (B H : A[X]) (z q : A)
    (hH : ∀ j : Nat, q ∣ (derivative^[j] H).eval z)
    (k : Nat) : ∀ j : Nat,
    q ^ k ∣ (derivative^[j] (B * H ^ k)).eval z := by
  induction k with
  | zero => intro j; simp
  | succ k ih =>
      intro j
      simpa only [pow_succ, mul_assoc] using
        jet_mul_dvd (B * H ^ k) H z q k (fun j => ih j) hH j

/-- The local congruence at order zero and the ordinary derivative
coefficient at positive orders supply every jet of `Z^p-W`. -/
theorem frobenius_polynomial_jet_dvd {A : Type*} [CommRing A]
    (z w : A) (p j : Nat) (hzero : (p : A) ∣ z ^ p - w) :
    (p : A) ∣ (derivative^[j] (X ^ p - C w : A[X])).eval z := by
  by_cases hj : j = 0
  · subst j
    simpa using hzero
  · rw [iterate_derivative_sub, iterate_derivative_C (Nat.pos_of_ne_zero hj),
      sub_zero]
    exact dvd_iterate_derivative_pow X p z hj

/-- The proposed `Z^p-W` factor contributes one arithmetic factor per
copy, for an arbitrary polynomial prefactor. The congruence is still
an explicit premise, not a theorem about inert primes. -/
theorem frobenius_polynomial_power_dvd {A : Type*} [CommRing A]
    (B : A[X]) (z w : A) (p k j : Nat)
    (hzero : (p : A) ∣ z ^ p - w) :
    (p : A) ^ k ∣
      (derivative^[j] (B * (X ^ p - C w) ^ k)).eval z :=
  jet_power_dvd B (X ^ p - C w) z (p : A)
    (fun t => frobenius_polynomial_jet_dvd z w p t hzero) k j

/-- A rational integer divides an element of the selected quadratic
order exactly when it divides both of its integer coordinates. -/
theorem zsqrtd_natCast_dvd_iff (d : Int) (p : Nat) (v : Zsqrtd d) :
    (p : Zsqrtd d) ∣ v ↔
      (p : Int) ∣ v.re ∧ (p : Int) ∣ v.im := by
  constructor
  · rintro ⟨b, rfl⟩
    constructor
    · exact ⟨b.re, by simp⟩
    · exact ⟨b.im, by simp⟩
  · rintro ⟨⟨u, hu⟩, ⟨w, hw⟩⟩
    refine ⟨⟨u, w⟩, ?_⟩
    apply Zsqrtd.ext
    · simpa using hu
    · simpa using hw

/-- Ring divisibility by `p^k` means exactly coordinatewise integer
divisibility by `p^k`; no norm-only shortcut is used. -/
theorem zsqrtd_pow_dvd_coordinates (d : Int) (p k : Nat)
    (v : Zsqrtd d) (h : (p : Zsqrtd d) ^ k ∣ v) :
    (p : Int) ^ k ∣ v.re ∧ (p : Int) ^ k ∣ v.im := by
  have h' : ((p ^ k : Nat) : Zsqrtd d) ∣ v := by simpa using h
  simpa only [Nat.cast_pow] using
    (zsqrtd_natCast_dvd_iff d (p ^ k) v).mp h'

/-- The pair-coordinate order-zero premise of `frobeniusJet` is exactly
the divisibility premise in the selected quadratic order. -/
theorem pair_frobenius_congruence_zsqrtd (D p : Nat) (a : Int × Int)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    (p : Zsqrtd (-(D : Int))) ∣
      (pairZsqrtdEquiv D a) ^ p - star (pairZsqrtdEquiv D a) := by
  apply (zsqrtd_natCast_dvd_iff (-(D : Int)) p _).2
  rw [← pairZsqrtd_pow, ← pairZsqrtd_conj]
  simpa [pairZsqrtdEquiv] using hzero

/-- At any original integer-pair sample, every ordinary jet of the
proposed transformed row has the full `p^k` factor in the selected
quadratic order, conditional only on the explicit local congruence.
The bounds keeping this row inside a rectangular basis, and its
matrix-level identification, are separate obligations. -/
theorem rectangular_frobenius_row_jet_dvd
    (D p r s k j : Nat) (a : Int × Int)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    let z := pairZsqrtdEquiv D a
    (p : Zsqrtd (-(D : Int))) ^ k ∣
      (derivative^[j]
        ((X ^ (r - p * k) * C (star z) ^ s) *
          (X ^ p - C (star z)) ^ k)).eval z := by
  dsimp
  exact frobenius_polynomial_power_dvd
    (X ^ (r - p * k) * C (star (pairZsqrtdEquiv D a)) ^ s)
    (pairZsqrtdEquiv D a) (star (pairZsqrtdEquiv D a)) p k j
    (pair_frobenius_congruence_zsqrtd D p a hzero)

/-- The same full power appears in **both** integer coordinates of
each proposed transformed-row jet. This is stronger than a statement
only about its norm or residue determinant. -/
theorem rectangular_frobenius_row_jet_coordinates
    (D p r s k j : Nat) (a : Int × Int)
    (hzero : (p : Int) ∣ (pairPow D a p).1 - (pairConj a).1 ∧
      (p : Int) ∣ (pairPow D a p).2 - (pairConj a).2) :
    let z := pairZsqrtdEquiv D a
    let v := (derivative^[j]
      ((X ^ (r - p * k) * C (star z) ^ s) *
        (X ^ p - C (star z)) ^ k)).eval z
    (p : Int) ^ k ∣ v.re ∧ (p : Int) ^ k ∣ v.im := by
  dsimp
  exact zsqrtd_pow_dvd_coordinates (-(D : Int)) p k _
    (rectangular_frobenius_row_jet_dvd D p r s k j a hzero)

/-- The derivative convention cannot be changed silently: the third
Hasse derivative of `X³` at zero is `1`, not a multiple of `3`. -/
theorem hasse_derivative_negative_control :
    ¬ (3 : Int) ∣ ((hasseDeriv 3) (X ^ 3 : Int[X])).eval 0 := by
  have hv : ((hasseDeriv 3) (X ^ 3 : Int[X])).eval 0 = 1 := by
    rw [← coeff_zero_eq_eval_zero, hasseDeriv_coeff]
    simp
  norm_num [hv]

end TenthDiscriminant
