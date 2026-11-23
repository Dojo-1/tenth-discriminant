import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

/-!
# Phase385: the central sign-to-real-zero implication

This file proves only the topological and algebraic bridge. The central
Epstein/Poisson identity and the exact-rational d>=200 lower bound are NOT
formalized here; factorization and sign bounds are explicit hypotheses.
-/
namespace TenthDiscriminant.Phase385
set_option autoImplicit false

/-- Strict endpoint signs force a zero strictly inside (1/2,1). -/
theorem real_zero_between_half_and_one (L : ℝ → ℝ)
    (hcont : ContinuousOn L (Set.Icc (1 / 2 : ℝ) 1))
    (hhalf : L (1 / 2) < 0) (hone : 0 < L 1) :
    ∃ β : ℝ, (1 / 2 : ℝ) < β ∧ β < 1 ∧ L β = 0 := by
  have hab : (1 / 2 : ℝ) ≤ 1 := by norm_num
  have htarget : (0 : ℝ) ∈ Set.Icc (L (1 / 2)) (L 1) :=
    ⟨le_of_lt hhalf, le_of_lt hone⟩
  obtain ⟨β, hβ, hzero⟩ := (intermediate_value_Icc hab hcont) htarget
  rcases Set.mem_Icc.mp hβ with ⟨hβlo, hβhi⟩
  have hstrictlo : (1 / 2 : ℝ) < β := by
    rcases eq_or_lt_of_le hβlo with heq | hlt
    · have hv : L (1 / 2) = 0 := by rw [heq]; exact hzero
      linarith
    · exact hlt
  have hstricthi : β < (1 : ℝ) := by
    rcases eq_or_lt_of_le hβhi with heq | hlt
    · have hv : L 1 = 0 := by rw [← heq]; exact hzero
      linarith
    · exact hlt
  exact ⟨β, hstrictlo, hstricthi, hzero⟩

/-- The Dedekind factorization is provided, not proved here.
This derives the sign of the Dirichlet factor without assuming GRH. -/
theorem positive_dedekind_half_forces_real_zero
    (L : ℝ → ℝ) (zetaHalf dedekindHalf : ℝ)
    (hzeta : zetaHalf < 0) (hDedekind : 0 < dedekindHalf)
    (hfactor : dedekindHalf = zetaHalf * L (1 / 2))
    (hone : 0 < L 1)
    (hcont : ContinuousOn L (Set.Icc (1 / 2 : ℝ) 1)) :
    ∃ β : ℝ, (1 / 2 : ℝ) < β ∧ β < 1 ∧ L β = 0 := by
  have hLhalf : L (1 / 2) < 0 := by
    by_contra hn
    have hnonneg : 0 ≤ L (1 / 2) := le_of_not_gt hn
    have hnonpos : zetaHalf * L (1 / 2) ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg (le_of_lt hzeta) hnonneg
    have hprodpos : 0 < zetaHalf * L (1 / 2) := by
      simpa [hfactor] using hDedekind
    linarith
  exact real_zero_between_half_and_one L hcont hLhalf hone

/-- A conditional bound on the *actual* absolute fundamental discriminant.
The analytic certificate is the explicitly supplied hlarge_sign hypothesis;
no theorem about number fields or analytic continuation is proved here. -/
theorem no_real_zero_excludes_d_ge_200
    (d : ℕ) (L : ℝ → ℝ) (zetaHalf dedekindHalf : ℝ)
    (hzeta : zetaHalf < 0)
    (hfactor : dedekindHalf = zetaHalf * L (1 / 2))
    (hone : 0 < L 1)
    (hcont : ContinuousOn L (Set.Icc (1 / 2 : ℝ) 1))
    (hlarge_sign : 200 ≤ d → 0 < dedekindHalf)
    (hZF : ∀ β : ℝ, (1 / 2 : ℝ) < β → β < 1 → L β ≠ 0) :
    d ≤ 199 := by
  by_contra hnot
  have hlarge : 200 ≤ d := by omega
  obtain ⟨β, hleft, hright, hzero⟩ :=
    positive_dedekind_half_forces_real_zero
      L zetaHalf dedekindHalf hzeta (hlarge_sign hlarge) hfactor hone hcont
  exact (hZF β hleft hright) hzero

end TenthDiscriminant.Phase385

#check TenthDiscriminant.Phase385.real_zero_between_half_and_one
#check TenthDiscriminant.Phase385.positive_dedekind_half_forces_real_zero
#check TenthDiscriminant.Phase385.no_real_zero_excludes_d_ge_200
#print axioms TenthDiscriminant.Phase385.positive_dedekind_half_forces_real_zero
#print axioms TenthDiscriminant.Phase385.no_real_zero_excludes_d_ge_200
