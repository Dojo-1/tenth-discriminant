import TenthDiscriminant.PrimeLogConstants
import TenthDiscriminant.FirstIntervalScalars

/-! Four certified constants replace per-dimension prime-power tables.
The resulting comparison is uniform in R,S; interval/radius guards stay explicit. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

def certifiedFactorialUpper (R : Nat) : Real := triangularMass R * factorialConstantUpper

def certifiedSmallOddLower (R S : Nat) : Real :=
  ((S : Real) - 1 / 2) * triangularMass R * linearConstantLower -
    ((S : Real) - 1 / 2) * R * errorConstantUpper - squareMass R * squareConstantUpper / 2

theorem factorialSmallMass_le_certified (R : Nat) (hR : 2 ≤ R) :
    factorialSmallMass R 10000 ≤ certifiedFactorialUpper R :=
  (factorialSmallMass_le_uniform R 10000 hR).trans
    (mul_le_mul_of_nonneg_left certified_prime_log_constants.1 (triangularMass_nonneg R))

theorem certifiedSmallOddLower_le (R S : Nat) (hS : 1 ≤ S) :
    certifiedSmallOddLower R S ≤ smallOddValuationMass R S 10000 := by
  have ha : (0 : Real) ≤ (S : Real) - 1 / 2 := by
    have h : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have hb := mul_le_mul_of_nonneg_left certified_prime_log_constants.2.1
    (mul_nonneg ha (triangularMass_nonneg R))
  have he := mul_le_mul_of_nonneg_left certified_prime_log_constants.2.2.2
    (mul_nonneg ha (Nat.cast_nonneg R))
  have hc := mul_le_mul_of_nonneg_left certified_prime_log_constants.2.2.1 (squareMass_nonneg R)
  have hbound : certifiedSmallOddLower R S ≤ uniformSmallOddLower R S 7 10000 := by
    unfold certifiedSmallOddLower uniformSmallOddLower
    linarith
  exact hbound.trans (uniformSmallOddLower_le R S 7 10000 hS (by decide))

def certifiedPrimeMassLower (R S : Nat) (I : Real) : Real :=
  2 * (max (certifiedSmallOddLower R S) 0 +
    max (((S : Real) - 1 / 2) *
      (factorialLower R - certifiedFactorialUpper R - triangularMass R * I) -
        squareMass R * I / 2) 0)

theorem certifiedPrimeMassLower_le_production (R S : Nat) (I : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) :
    certifiedPrimeMassLower R S I ≤ enderPrimeMassLower R S 10000 I := by
  have hs := max_le (certifiedSmallOddLower_le R S hS) (smallOddValuationMass_nonneg R S 10000)
  have hf := factorialSmallMass_le_certified R hR
  have ha : (0 : Real) ≤ (S : Real) - 1 / 2 := by
    have h : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have ht : ((S : Real) - 1 / 2) *
      (factorialLower R - certifiedFactorialUpper R - triangularMass R * I) -
        squareMass R * I / 2 ≤ enderTailLower R S 10000 I := by
    unfold enderTailLower
    nlinarith
  have hm := max_le_max ht (le_refl (0 : Real))
  unfold certifiedPrimeMassLower enderPrimeMassLower
  linarith

theorem certifiedPrimeMassLower_antitone_tail (R S : Nat) (hS : 1 ≤ S) :
    Antitone (certifiedPrimeMassLower R S) := by
  intro I J hIJ
  have ha : (0 : Real) ≤ (S : Real) - 1 / 2 := by
    have h : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have hv := mul_nonneg ha (triangularMass_nonneg R)
  have hw := squareMass_nonneg R
  have ht : ((S : Real) - 1 / 2) *
      (factorialLower R - certifiedFactorialUpper R - triangularMass R * J) -
        squareMass R * J / 2 ≤
      ((S : Real) - 1 / 2) *
        (factorialLower R - certifiedFactorialUpper R - triangularMass R * I) -
          squareMass R * I / 2 := by nlinarith
  have hm := max_le_max ht (le_refl (0 : Real))
  unfold certifiedPrimeMassLower
  linarith

theorem ellipse_certifiedPrimeMassLower_le_counted_upperB
    (D₁ D D₂ rho R S Y : Nat)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hRS : R ≤ 10000 * S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    certifiedPrimeMassLower R S (enderTailIntegral 10000) ≤
      enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) :=
  (certifiedPrimeMassLower_le_production R S _ hR hS).trans
    (ellipse_enderPrimeMassLower_le_counted_upperB D₁ D D₂ rho R S Y 10000
      hD₁ hDlo hDhi hR hS (by decide) hRS hDsq hclass hRcut hRrho hY hradius)

/-- The tail budget depends only on P=10000, so it is reusable for all R,S. -/
theorem classNumber_ne_one_of_certified_budget_comparison
    (D₁ D D₂ rho R S Y : Nat)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hRS : R ≤ 10000 * S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real))
    (hgap : enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) <
      certifiedPrimeMassLower R S FirstEnderInterval.tailBudget) :
    NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) ≠ 1 := by
  intro hclass
  have ht := certifiedPrimeMassLower_antitone_tail R S hS FirstEnderInterval.tail_le_budget
  have hc := ellipse_certifiedPrimeMassLower_le_counted_upperB D₁ D D₂ rho R S Y
    hD₁ hDlo hDhi hR hS hRS hDsq hclass hRcut hRrho hY hradius
  exact (not_lt_of_ge (ht.trans hc)) hgap

theorem first_interval_uniform_budgets :
    certifiedFactorialUpper 175000000000 ≤ FirstEnderInterval.smallBudget ∧
      FirstEnderInterval.oddBudget ≤ certifiedSmallOddLower 175000000000 8750000000 := by
  norm_num [certifiedFactorialUpper, certifiedSmallOddLower, factorialConstantUpper,
    linearConstantLower, squareConstantUpper, errorConstantUpper, triangularMass,
    squareMass, FirstEnderInterval.smallBudget, FirstEnderInterval.oddBudget]

theorem first_interval_comparison_from_uniform_constants :
    FirstEnderInterval.upper < FirstEnderInterval.lower :=
  FirstEnderInterval.strict_comparison_of_table_budgets
    ((factorialSmallMass_le_certified _ (by decide)).trans first_interval_uniform_budgets.1)
    (first_interval_uniform_budgets.2.trans (certifiedSmallOddLower_le _ _ (by decide)))

theorem first_interval_classNumber_ne_one_from_uniform_constants (D : Nat)
    (hlo : 700000000000 ≤ D) (hhi : D ≤ 875000000000)
    [Fact ((D : Int) % 4 = 3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) ≠ 1 :=
  FirstEnderInterval.exclusion_of_strict_comparison first_interval_comparison_from_uniform_constants D hlo hhi hsq

end
end TenthDiscriminant.FirstCertificate
