import TenthDiscriminant.PrimeMassAssembly
import TenthDiscriminant.InertFrobenius
import TenthDiscriminant.ThinUpper322
import TenthDiscriminant.SourcePositivity322

/-!
# Phase210 — a class-number-free, SAME-GRAM finite inert-prime budget

This does not assert a Landau-Siegel-zero exclusion. The assumptions
on P are *only* distinctness (Finset), prime, oddness and nonsquareness
of -D modulo p. Class number one is not used anywhere in this file.

The exact source object throughout is
integerRectangularTraceGram (ellipsePairs D (Tuned.thinRadius D))
  D (Tuned.S D) (Tuned.R D) (Tuned.S D).
The analytic input is ThinUpper322.thin_production_normalized_upper_322
with the explicit hypotheses D >= 322^4; the geometric positivity
input is Tuned.thin_original_gram_pos_322.

The generic product assembly comes from the existing verified
PrimeMassAssembly.primePowerProduct_le_det. The logarithms require the
positive original integer determinant, not an abstract comparison.
-/
namespace TenthDiscriminant.Phase210FiniteInertBudget

open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- ANY finite collection of distinct odd inert primes forces the
sum of its existing full 2F(p) valuations below the logarithm of the
SAME positive integer trace Gram. There is NO class-number hypothesis. -/
theorem finite_inert_mass_le_original_log
    (P : Finset Nat) (D rho J R S : Nat)
    (hpositive : 0 <
      (integerRectangularTraceGram (ellipsePairs D rho) D J R S).det)
    (hprime : ∀ p ∈ P, p.Prime)
    (hodd : ∀ p ∈ P, p ≠ 2)
    (hinert : ∀ p ∈ P, ¬ IsSquare (-(D : ZMod p))) :
    (∑ p ∈ P, ((2 * valuationWeight R S p : Nat) : Real) *
      Real.log (p : Real)) ≤
    Real.log ((integerRectangularTraceGram (ellipsePairs D rho)
      D J R S).det : Real) := by
  classical
  let e : Nat → Nat := fun p => 2 * valuationWeight R S p
  have hlocal : ∀ p ∈ P, (p : Int) ^ e p ∣
      (integerRectangularTraceGram (ellipsePairs D rho) D J R S).det := by
    intro p hp
    letI : Fact p.Prime := ⟨hprime p hp⟩
    exact rectangularTraceGram_valuation_of_nonsquare
      (ellipsePairs D rho) D J R S p (hodd p hp) (hinert p hp)
  have hle := primePowerProduct_le_det P e
    (integerRectangularTraceGram (ellipsePairs D rho) D J R S).det
    hpositive hprime hlocal
  have hleInt :
      ((∏ p ∈ P, p ^ e p : Nat) : Int) ≤
        (integerRectangularTraceGram (ellipsePairs D rho) D J R S).det := by
    have hcast :
        ((∏ p ∈ P, p ^ e p : Nat) : Int) ≤
          (((integerRectangularTraceGram (ellipsePairs D rho)
              D J R S).det).natAbs : Int) := by
      exact_mod_cast hle
    simpa only [Int.natCast_natAbs, abs_of_pos hpositive] using hcast
  have hleReal :
      ((∏ p ∈ P, p ^ e p : Nat) : Real) ≤
      ((integerRectangularTraceGram (ellipsePairs D rho)
        D J R S).det : Real) := by
    exact_mod_cast hleInt
  have hp_pos : ∀ p ∈ P, (0 : Real) < p := by
    intro p hp
    exact_mod_cast (hprime p hp).pos
  have hprod_pos_nat :
      0 < (∏ p ∈ P, p ^ e p : Nat) := by
    exact Finset.prod_pos (fun p hp => pow_pos (hprime p hp).pos _)
  have hprod_pos :
      (0 : Real) < ((∏ p ∈ P, p ^ e p : Nat) : Real) := by
    exact_mod_cast hprod_pos_nat
  have hlog := Real.log_le_log hprod_pos hleReal
  have hmass :
      Real.log ((∏ p ∈ P, p ^ e p : Nat) : Real) =
        ∑ p ∈ P, ((e p : Nat) : Real) * Real.log (p : Real) := by
    simp only [Nat.cast_prod, Nat.cast_pow]
    rw [Real.log_prod]
    · simp_rw [Real.log_pow]
    · intro p hp
      exact ne_of_gt (pow_pos (hp_pos p hp) _)
  rw [hmass] at hlog
  simpa only [e] using hlog

/-- With the analytic upper EXPLICITLY ASSUMED as hupper, the class-
number-free mass bound is a formal implication for the original Qthin.
The hypothesis is exactly the accepted same-Gram logarithmic upper. -/
theorem thin_inert_mass_budget_of_analytic_upper_322
    (D : Nat) (hD : (322 : Nat)^4 ≤ D) (P : Finset Nat)
    (hprime : ∀ p ∈ P, p.Prime)
    (hodd : ∀ p ∈ P, p ≠ 2)
    (hinert : ∀ p ∈ P, ¬ IsSquare (-(D : ZMod p)))
    (hpositive : 0 < (integerRectangularTraceGram
      (ellipsePairs D (Tuned.thinRadius D)) D (Tuned.S D)
      (Tuned.R D) (Tuned.S D)).det)
    (hupper :
       Real.log ((integerRectangularTraceGram
           (ellipsePairs D (Tuned.thinRadius D)) D (Tuned.S D)
           (Tuned.R D) (Tuned.S D)).det : Real) /
         comparisonScale (Tuned.R D) (Tuned.S D) ≤
           (4/5 : Real) * Real.log D - 1853/2000) :
    (∑ p ∈ P,
      ((2 * valuationWeight (Tuned.R D) (Tuned.S D) p : Nat) : Real) *
        Real.log (p : Real)) /
       comparisonScale (Tuned.R D) (Tuned.S D) ≤
      (4/5 : Real) * Real.log D - 1853/2000 := by
  have hdim := Tuned.dimensions_322 D hD
  have hscale := comparisonScale_pos
    (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hmass := finite_inert_mass_le_original_log
    P D (Tuned.thinRadius D) (Tuned.S D)
    (Tuned.R D) (Tuned.S D)
    hpositive hprime hodd hinert
  exact (div_le_div_of_nonneg_right hmass hscale.le).trans hupper

/-- Source-checked closed corollary: at >=322^4 the actual thin
original Gram is positive and obeys the required analytic upper.
Only odd-prime inertness is assumed for the chosen finite set P. -/
theorem thin_inert_mass_budget_322
    (D : Nat) (hD : (322 : Nat)^4 ≤ D) (P : Finset Nat)
    (hprime : ∀ p ∈ P, p.Prime)
    (hodd : ∀ p ∈ P, p ≠ 2)
    (hinert : ∀ p ∈ P, ¬ IsSquare (-(D : ZMod p))) :
    (∑ p ∈ P,
      ((2 * valuationWeight (Tuned.R D) (Tuned.S D) p : Nat) : Real) *
        Real.log (p : Real)) /
      comparisonScale (Tuned.R D) (Tuned.S D) ≤
      (4/5 : Real) * Real.log D - 1853/2000 := by
  exact thin_inert_mass_budget_of_analytic_upper_322
    D hD P hprime hodd hinert
    (Tuned.thin_original_gram_pos_322 D hD)
    (ThinUpper322.thin_production_normalized_upper_322 D hD)

/-- Empty prime sets contribute zero, not an illicit inert factor.
This is a regression for the finite-prime quantifier. -/
theorem thin_inert_empty_sum_control (D : Nat) :
    (∑ p ∈ (∅ : Finset Nat),
      ((2 * valuationWeight (Tuned.R D) (Tuned.S D) p : Nat) : Real) *
        Real.log (p : Real)) = 0 := by simp

end
end TenthDiscriminant.Phase210FiniteInertBudget

#print axioms TenthDiscriminant.Phase210FiniteInertBudget.finite_inert_mass_le_original_log
#print axioms TenthDiscriminant.Phase210FiniteInertBudget.thin_inert_mass_budget_of_analytic_upper_322
#print axioms TenthDiscriminant.Phase210FiniteInertBudget.thin_inert_mass_budget_322
#print axioms TenthDiscriminant.Phase210FiniteInertBudget.thin_inert_empty_sum_control

-- Explicitly print the complete theorem signature in CI for Phase211's
-- external hypothesis inventory; the theorem's proof remains unchanged.
#check TenthDiscriminant.Phase210FiniteInertBudget.finite_inert_mass_le_original_log
