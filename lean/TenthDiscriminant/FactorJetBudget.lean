import TenthDiscriminant.BivariateDegree
import Mathlib.Algebra.Polynomial.FieldDivision

/-! A multiplicative exceptional-set budget. Zero fibers are retained explicitly;
repeated factors are handled by factor induction, never squarefree replacement. -/
namespace TenthDiscriminant
namespace JetAssembly
open Polynomial
noncomputable section
variable {K : Type*} [Field K]

def specialize (F : Polynomial (Polynomial K)) (w : K) : Polynomial K :=
  F.map (Polynomial.evalRingHom w)

@[simp] theorem specialize_C (q : Polynomial K) (w : K) :
    specialize (Polynomial.C q) w = Polynomial.C (q.eval w) := by simp [specialize]

@[simp] theorem specialize_map_C (q : Polynomial K) (w : K) :
    specialize (q.map Polynomial.C) w = q := by
  ext i
  simp [specialize, Polynomial.coeff_map]

@[simp] theorem specialize_mul (F G : Polynomial (Polynomial K)) (w : K) :
    specialize (F*G) w = specialize F w * specialize G w := by simp [specialize]

/-- Bad means a zero fiber OR contact exceeding the actual W degree. -/
def badParameters (F : Polynomial (Polynomial K)) (s : Finset K) (z : K -> K) : Finset K := by
  classical
  exact s.filter (fun w => specialize F w = 0 ∨
    wDegree F < (specialize F w).rootMultiplicity (z w))

@[simp] theorem mem_badParameters (F : Polynomial (Polynomial K)) (s : Finset K)
    (z : K -> K) (w : K) :
    w ∈ badParameters F s z ↔ w ∈ s ∧ (specialize F w = 0 ∨
      wDegree F < (specialize F w).rootMultiplicity (z w)) := by
  classical
  exact Finset.mem_filter

/-- Injectivity prevents one root being counted under many sample names. -/
theorem root_preimage_card_le (q : Polynomial K) (hq : q ≠ 0)
    (t : Finset K) (z : K -> K) (hz : Function.Injective z)
    (hroot : ∀ w, w ∈ t -> q.IsRoot (z w)) : t.card ≤ q.natDegree := by
  classical
  have hh : (t.image z).card ≤ q.natDegree :=
    Polynomial.card_le_degree_of_subset_roots (by
      intro y hy
      obtain ⟨w, hw, rfl⟩ := Finset.mem_image.mp hy
      exact (Polynomial.mem_roots hq).mpr (hroot w hw))
  simpa only [Finset.card_image_of_injective t hz] using hh

/-- Parameter-only factors spend their ordinary W-root count. -/
theorem bad_C_card (q : Polynomial K) (hq : q ≠ 0) (s : Finset K) (z : K -> K) :
    (badParameters (Polynomial.C q) s z).card ≤ q.natDegree := by
  apply root_preimage_card_le q hq _ id Function.injective_id
  intro w hw
  have hb := (mem_badParameters _ _ _ _).mp hw
  change q.eval w = 0
  by_contra he
  have h0 : specialize (Polynomial.C q) w ≠ 0 := by
    simpa only [specialize_C, ne_eq, Polynomial.C_eq_zero] using he
  have hm : (specialize (Polynomial.C q) w).rootMultiplicity (z w) = 0 := by
    rw [specialize_C]
    apply Polynomial.rootMultiplicity_eq_zero
    simpa only [Polynomial.IsRoot, Polynomial.eval_C] using he
  rcases hb.2 with h | h
  · exact h0 h
  · rw [hm] at h
    omega

/-- Z-only factors spend their ordinary Z-root count, not a contact quotient. -/
theorem bad_map_C_card (q : Polynomial K) (hq : q ≠ 0) (s : Finset K)
    (z : K -> K) (hz : Function.Injective z) :
    (badParameters (q.map Polynomial.C) s z).card ≤ q.natDegree := by
  have hb0 : wDegree (q.map Polynomial.C) = 0 := by
    apply Nat.eq_zero_of_le_zero
    apply wDegree_le_of_coefficients
    intro i
    simp [Polynomial.coeff_map]
  apply root_preimage_card_le q hq _ z hz
  intro w hw
  have hb := (mem_badParameters _ _ _ _).mp hw
  rcases hb.2 with h | h
  · exact (hq (by simpa only [specialize_map_C] using h)).elim
  · have hm : 0 < q.rootMultiplicity (z w) := by
      simpa only [specialize_map_C, hb0] using h
    exact (Polynomial.rootMultiplicity_pos hq).mp hm

/-- A product can only be bad where at least one of its factors is bad. -/
theorem bad_mul_subset (F G : Polynomial (Polynomial K)) (hF : F ≠ 0) (hG : G ≠ 0)
    (s : Finset K) (z : K -> K) :
    badParameters (F*G) s z ⊆ badParameters F s z ∪ badParameters G s z := by
  classical
  intro w hw
  have hw' := (mem_badParameters _ _ _ _).mp hw
  by_contra hn
  have hf : ¬(specialize F w = 0 ∨ wDegree F < (specialize F w).rootMultiplicity (z w)) := by
    intro hf
    exact hn (Finset.mem_union_left _ ((mem_badParameters _ _ _ _).mpr ⟨hw'.1,hf⟩))
  have hg : ¬(specialize G w = 0 ∨ wDegree G < (specialize G w).rootMultiplicity (z w)) := by
    intro hg
    exact hn (Finset.mem_union_right _ ((mem_badParameters _ _ _ _).mpr ⟨hw'.1,hg⟩))
  have hf0 := (not_or.mp hf).1
  have hg0 := (not_or.mp hg).1
  have hfm := Nat.le_of_not_gt (not_or.mp hf).2
  have hgm := Nat.le_of_not_gt (not_or.mp hg).2
  rcases hw'.2 with h0 | hm
  · rw [specialize_mul] at h0
    exact mul_ne_zero hf0 hg0 h0
  · rw [specialize_mul, Polynomial.rootMultiplicity_mul (mul_ne_zero hf0 hg0),
      wDegree_mul F G hF hG] at hm
    omega

variable [CharZero K]

/-- Every irreducible case, including both pure-variable boundaries. -/
theorem bad_irreducible_card (F : Polynomial (Polynomial K)) (hi : Irreducible F)
    (s : Finset K) (z : K -> K) (hz : Function.Injective z) :
    (badParameters F s z).card ≤ 2*F.natDegree + wDegree F := by
  by_cases ha : F.natDegree = 0
  · have he := Polynomial.eq_C_of_natDegree_eq_zero ha
    have hq : F.coeff 0 ≠ 0 := by
      intro h
      apply hi.ne_zero
      rw [he, h, map_zero]
    have hh := bad_C_card (F.coeff 0) hq s z
    rw [he, wDegree_C]
    simpa using hh
  by_cases hb : wDegree F = 0
  · obtain ⟨q, hq⟩ := exists_constant_coefficients F hb
    have hq0 : q ≠ 0 := by intro h; apply hi.ne_zero; simp [hq,h]
    have hh := bad_map_C_card q hq0 s z hz
    have hd : F.natDegree = q.natDegree := by
      rw [hq, Polynomial.natDegree_map_eq_of_injective Polynomial.C_injective]
    rw [hq] at hh
    rw [← hq] at hh
    omega
  have hpos : 1 ≤ F.natDegree := by omega
  have hbpos : 0 < wDegree F := by omega
  have hn := irreducible_fixedDerivativeSylvester_excessive_contact_card F
    F.natDegree (wDegree F) hpos hbpos rfl hi (coefficient_natDegree_le_wDegree F)
    (badParameters F s z) z (fun w => (specialize F w).rootMultiplicity (z w))
    (fun w hw => Polynomial.pow_rootMultiplicity_dvd _ _)
    (by
      intro w hw
      rcases ((mem_badParameters _ _ _ _).mp hw).2 with h0 | hm
      · exact (irreducible_positive_specialization_ne_zero F _ hpos rfl hi w h0).elim
      · exact hm)
  omega

/-- Universal exceptional-set budget; repeated factors remain in factor induction. -/
theorem badParameters_card_le (F : Polynomial (Polynomial K)) (hF : F ≠ 0)
    (s : Finset K) (z : K -> K) (hz : Function.Injective z) :
    (badParameters F s z).card ≤ 2*F.natDegree + wDegree F := by
  classical
  revert hF
  induction F using WfDvdMonoid.induction_on_irreducible with
  | zero => intro h; exact (h rfl).elim
  | unit u hu =>
    intro h
    have hd := Polynomial.natDegree_eq_zero_of_isUnit hu
    have he := Polynomial.eq_C_of_natDegree_eq_zero hd
    have hq : u.coeff 0 ≠ 0 := by intro hq; apply h; rw [he,hq,map_zero]
    have hh := bad_C_card (u.coeff 0) hq s z
    rw [he, wDegree_C]
    simpa using hh
  | mul F H hF hi ih =>
    intro h
    calc
      (badParameters (H*F) s z).card ≤ (badParameters H s z ∪ badParameters F s z).card :=
        Finset.card_le_card (bad_mul_subset H F hi.ne_zero hF s z)
      _ ≤ (badParameters H s z).card + (badParameters F s z).card := Finset.card_union_le _ _
      _ ≤ (2*H.natDegree+wDegree H) + (2*F.natDegree+wDegree F) :=
        Nat.add_le_add (bad_irreducible_card H hi s z hz) (ih hF)
      _ = 2*(H*F).natDegree + wDegree (H*F) := by
        rw [Polynomial.natDegree_mul hi.ne_zero hF, wDegree_mul H F hi.ne_zero hF]
        omega

/-- Sampled ordinary jets separate every polynomial below this exact degree budget. -/
theorem polynomial_eq_zero_of_jet_count (F : Polynomial (Polynomial K))
    (s : Finset K) (z : K -> K) (hz : Function.Injective z) (J : Nat)
    (hJ : wDegree F < J) (hcard : 2*F.natDegree+wDegree F < s.card)
    (hjet : ∀ w, w ∈ s -> ∀ j, j < J ->
      ((Polynomial.derivative^[j]) (specialize F w)).eval (z w) = 0) : F = 0 := by
  classical
  by_contra hF
  have hsub : s ⊆ badParameters F s z := by
    intro w hw
    apply (mem_badParameters _ _ _ _).mpr
    refine ⟨hw, ?_⟩
    by_cases h0 : specialize F w = 0
    · exact Or.inl h0
    right
    apply Polynomial.lt_rootMultiplicity_of_isRoot_iterate_derivative h0
    intro j hj
    exact hjet w hw j (lt_of_le_of_lt hj hJ)
  have hh := (Finset.card_le_card hsub).trans (badParameters_card_le F hF s z hz)
  omega

end
end JetAssembly
end TenthDiscriminant
