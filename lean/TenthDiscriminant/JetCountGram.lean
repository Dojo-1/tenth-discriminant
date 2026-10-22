import TenthDiscriminant.FactorJetBudget
import TenthDiscriminant.JetKernel

/-! Bounded-degree jet separation for the actual derivative trace-Gram matrix.
Row labels must be distinct. No independence, positivity or resultant premise
is hidden in the public point-count theorem. -/
namespace TenthDiscriminant
namespace JetAssembly
open Polynomial Matrix
open scoped ComplexConjugate
noncomputable section

/-- Conjugation preserves distinctness in both sampling coordinates. -/
theorem polynomial_eq_zero_of_conjugate_jets (F : Polynomial (Polynomial Complex))
    (P : Finset Complex) (J : Nat) (hJ : wDegree F < J)
    (hcard : 2*F.natDegree+wDegree F < P.card)
    (hjet : ∀ z, z ∈ P -> ∀ j, j < J ->
      ((Polynomial.derivative^[j]) (specialize F (conj z))).eval z = 0) : F = 0 := by
  classical
  have hc : Function.Injective (starRingEnd Complex) := by
    intro x y h
    simpa using congrArg (starRingEnd Complex) h
  apply polynomial_eq_zero_of_jet_count F (P.image (starRingEnd Complex))
    (starRingEnd Complex) hc J hJ
  · simpa only [Finset.card_image_of_injective P hc] using hcard
  · intro w hw j hj
    obtain ⟨z, hz, rfl⟩ := Finset.mem_image.mp hw
    simpa using hjet z hz j hj

/-- Assemble the original monomial row family as an actual bivariate polynomial. -/
def rowPolynomial {n : Nat} (rows : Fin n -> Nat × Nat) (c : Fin n -> Complex) :
    Polynomial (Polynomial Complex) :=
  Finset.univ.sum (fun i => Polynomial.monomial (rows i).1
    (Polynomial.monomial (rows i).2 (c i)))

theorem rowPolynomial_coeff_at {n : Nat} (rows : Fin n -> Nat × Nat)
    (hi : Function.Injective rows) (c : Fin n -> Complex) (i : Fin n) :
    ((rowPolynomial rows c).coeff (rows i).1).coeff (rows i).2 = c i := by
  classical
  simp only [rowPolynomial, Polynomial.finset_sum_coeff]
  rw [Finset.sum_eq_single i]
  · simp [Polynomial.coeff_monomial]
  · intro j hj hji
    have hn : rows j ≠ rows i := fun h => hji (hi h)
    by_cases h1 : (rows j).1 = (rows i).1
    · have h2 : (rows j).2 ≠ (rows i).2 := by
        intro h2
        exact hn (Prod.ext h1 h2)
      simp [Polynomial.coeff_monomial, h1, h2]
    · simp [Polynomial.coeff_monomial, h1]
  · intro h
    exact (h (Finset.mem_univ i)).elim

theorem rowPolynomial_natDegree_le {n : Nat} (rows : Fin n -> Nat × Nat)
    (c : Fin n -> Complex) (r : Nat) (hr : ∀ i, (rows i).1 ≤ r) :
    (rowPolynomial rows c).natDegree ≤ r := by
  apply Polynomial.natDegree_sum_le_of_forall_le
  intro i hi
  exact (Polynomial.natDegree_monomial_le _).trans (hr i)

theorem rowPolynomial_wDegree_le {n : Nat} (rows : Fin n -> Nat × Nat)
    (c : Fin n -> Complex) (s : Nat) (hs : ∀ i, (rows i).2 ≤ s) :
    wDegree (rowPolynomial rows c) ≤ s := by
  unfold wDegree rowPolynomial
  simp only [map_sum, swap_monomial_monomial]
  apply Polynomial.natDegree_sum_le_of_forall_le
  intro i hi
  exact (Polynomial.natDegree_monomial_le _).trans (hs i)

/-- The polynomial specialization is exactly the rowSection already tied to realJet. -/
theorem specialize_rowPolynomial {n : Nat} (rows : Fin n -> Nat × Nat)
    (c : Fin n -> Complex) (w : Complex) :
    specialize (rowPolynomial rows c) w = rowSection rows c w := by
  classical
  unfold specialize rowPolynomial rowSection
  rw [Polynomial.map_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [Polynomial.map_monomial]
  change Polynomial.monomial (rows i).1
    ((Polynomial.monomial (rows i).2 (c i)).eval w) = _
  rw [Polynomial.eval_monomial, Polynomial.C_mul_X_pow_eq_monomial]

/-- Point-count theorem for the SAME actual real trace-Gram matrix. -/
theorem traceGramMatrix_posDef_of_point_count {n : Nat}
    (P : Finset Complex) (J R S : Nat) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (rows : Fin n -> Nat × Nat) (hrows : Function.Injective rows)
    (hr : ∀ i, (rows i).1 < R) (hs : ∀ i, (rows i).2 < S)
    (hJ : S ≤ J) (hcard : 2*(R-1)+(S-1) < P.card) :
    (traceGramMatrix P J rows).PosDef := by
  apply (traceGramMatrix_posDef_iff P J rows).mpr
  intro x hx
  let Q := rowPolynomial rows (fun i => (x i : Complex))
  have hqR : Q.natDegree ≤ R-1 := rowPolynomial_natDegree_le rows _ (R-1)
    (fun i => by have := hr i; omega)
  have hqS : wDegree Q ≤ S-1 := rowPolynomial_wDegree_le rows _ (S-1)
    (fun i => by have := hs i; omega)
  have hQ : Q = 0 := by
    apply polynomial_eq_zero_of_conjugate_jets Q P J (by omega) (by omega)
    intro z hz j hj
    rw [show Q = rowPolynomial rows (fun i => (x i : Complex)) from rfl,
      specialize_rowPolynomial]
    have hh := hx (⟨⟨j,hj⟩,⟨z,hz⟩⟩)
    rw [realJet_eq_polynomial_jet] at hh
    exact hh
  funext i
  have hh := congrArg (fun p : Polynomial (Polynomial Complex) =>
    (p.coeff (rows i).1).coeff (rows i).2) hQ
  change ((rowPolynomial rows (fun i => (x i : Complex))).coeff (rows i).1).coeff
    (rows i).2 = ((0 : Polynomial (Polynomial Complex)).coeff (rows i).1).coeff (rows i).2 at hh
  rw [rowPolynomial_coeff_at rows hrows] at hh
  have hc : (x i : Complex) = 0 := by simpa only [Polynomial.coeff_zero] using hh
  exact_mod_cast hc

/-- No positivity hypothesis is assumed; the full point-count proof supplies it. -/
theorem traceGramMatrix_det_pos_of_point_count {n : Nat}
    (P : Finset Complex) (J R S : Nat) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (rows : Fin n -> Nat × Nat) (hrows : Function.Injective rows)
    (hr : ∀ i, (rows i).1 < R) (hs : ∀ i, (rows i).2 < S)
    (hJ : S ≤ J) (hcard : 2*(R-1)+(S-1) < P.card) :
    0 < (traceGramMatrix P J rows).det :=
  (traceGramMatrix_posDef_of_point_count P J R S hR hS rows hrows hr hs hJ hcard).det_pos

end
end JetAssembly
end TenthDiscriminant
