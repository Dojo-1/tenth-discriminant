import TenthDiscriminant.NumericalWeights
import TenthDiscriminant.PrimeTail

/-!
# Prime-mass bounds uniform in the rectangle dimensions

The four prime-log sums depend on the fixed prime cutoffs, not on R or S.
All estimates concern the original production weights and actual-Gram chain.
-/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

theorem cast_div_ge_sub_one (r p : Nat) (hp : 0 < p) :
    (r : Real) / p - 1 ≤ ((r / p : Nat) : Real) := by
  have hdiv : ((p * (r / p) + r % p : Nat) : Real) = r := by
    exact_mod_cast Nat.div_add_mod r p
  push_cast at hdiv
  have hmod : ((r % p : Nat) : Real) < p := by exact_mod_cast Nat.mod_lt r hp
  have hpos : (0 : Real) < p := by exact_mod_cast hp
  apply (sub_le_iff_le_add).mpr
  apply (div_le_iff₀ hpos).mpr
  nlinarith

theorem floorSum_ge_triangularMass_div_sub (R p : Nat) (hp : 0 < p) :
    triangularMass R / p - R ≤ (floorSum R p : Real) := by
  calc
    _ = ∑ r ∈ Finset.range R, ((r : Real) / p - 1) := by
      rw [Finset.sum_sub_distrib, ← Finset.sum_div, sum_range_real_eq_triangularMass]
      simp
    _ ≤ ∑ r ∈ Finset.range R, (((r / p : Nat) : Real)) :=
      Finset.sum_le_sum (fun r hr => cast_div_ge_sub_one r p hp)
    _ = _ := by simp [floorSum]

theorem factorialPowerSum_le_triangularMass_div_sub_one (R p : Nat)
    (hR : 2 ≤ R) (hp : 2 ≤ p) :
    (factorialPowerSum R p : Real) ≤ triangularMass R / ((p : Real) - 1) := by
  have hh := factorialHigherWeight_le R p hR hp
  have hf := floorSum_le_triangularMass_div R p
  have hp0 : (0 : Real) < p := by exact_mod_cast (by omega : 0 < p)
  have hp1 : (0 : Real) < (p : Real) - 1 := by
    have h : (2 : Real) ≤ p := by exact_mod_cast hp
    linarith
  have heq : triangularMass R / p + triangularMass R / ((p : Real) * (p - 1)) =
      triangularMass R / ((p : Real) - 1) := by
    field_simp [ne_of_gt hp0, ne_of_gt hp1]
    ring
  linarith

def uniformValuationLower (R S p : Nat) : Real :=
  ((S : Real) - 1 / 2) * (triangularMass R / p - R) - squareMass R / (2 * (p : Real) ^ 2)

theorem uniformValuationLower_le (R S p : Nat) (hS : 1 ≤ S) (hp : 0 < p) :
    uniformValuationLower R S p ≤ (valuationWeight R S p : Real) := by
  have hcoeff : (0 : Real) ≤ (S : Real) - 1 / 2 := by
    have h : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have hf := mul_le_mul_of_nonneg_left (floorSum_ge_triangularMass_div_sub R p hp) hcoeff
  have hw := valuationWeight_ge_floor_bound R S p
  unfold uniformValuationLower
  linarith

def retainedSmallPrimes (Q P : Nat) : Finset Nat :=
  (productionSmallPrimes P).filter (fun p => Q ≤ p)

def primeLogFactorialConstant (P : Nat) : Real :=
  ∑ p ∈ productionSmallPrimes P, Real.log p / ((p : Real) - 1)

def primeLogLinearConstant (Q P : Nat) : Real :=
  ∑ p ∈ retainedSmallPrimes Q P, Real.log p / (p : Real)

def primeLogSquareConstant (Q P : Nat) : Real :=
  ∑ p ∈ retainedSmallPrimes Q P, Real.log p / (p : Real) ^ 2

def primeLogErrorConstant (Q P : Nat) : Real :=
  ∑ p ∈ retainedSmallPrimes Q P, Real.log p

def uniformSmallOddLower (R S Q P : Nat) : Real :=
  ((S : Real) - 1 / 2) * triangularMass R * primeLogLinearConstant Q P -
    ((S : Real) - 1 / 2) * R * primeLogErrorConstant Q P -
      squareMass R * primeLogSquareConstant Q P / 2

theorem factorialSmallMass_le_uniform (R P : Nat) (hR : 2 ≤ R) :
    factorialSmallMass R P ≤ triangularMass R * primeLogFactorialConstant P := by
  rw [factorialSmallMass_eq_padded]
  unfold primeLogFactorialConstant
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro p hp
  have hprime := (Finset.mem_filter.mp hp).2
  have hlog := Real.log_nonneg (show (1 : Real) ≤ p by exact_mod_cast hprime.one_le)
  have h := mul_le_mul_of_nonneg_right
    (factorialPowerSum_le_triangularMass_div_sub_one R p hR hprime.two_le) hlog
  convert h using 1 <;> ring

theorem uniformSmallOddLower_le (R S Q P : Nat) (hS : 1 ≤ S) (hQ : 3 ≤ Q) :
    uniformSmallOddLower R S Q P ≤ smallOddValuationMass R S P := by
  have hsub : retainedSmallPrimes Q P ⊆ (productionSmallPrimes P).filter (fun p => p ≠ 2) := by
    intro p hp
    rcases Finset.mem_filter.mp hp with ⟨hprime, hqp⟩
    exact Finset.mem_filter.mpr ⟨hprime, by omega⟩
  have hsum : uniformSmallOddLower R S Q P =
      ∑ p ∈ retainedSmallPrimes Q P, uniformValuationLower R S p * Real.log p := by
    unfold uniformSmallOddLower primeLogLinearConstant primeLogSquareConstant primeLogErrorConstant
    rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, Finset.sum_div,
      ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro p hp
    unfold uniformValuationLower
    ring
  rw [hsum, smallOddValuationMass_eq_padded]
  apply le_trans (Finset.sum_le_sum (s := retainedSmallPrimes Q P) ?_)
  · apply Finset.sum_le_sum_of_subset_of_nonneg hsub
    intro p hp hpnot
    have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).2
    exact mul_nonneg (by positivity)
      (Real.log_nonneg (show (1 : Real) ≤ p by exact_mod_cast hprime.one_le))
  · intro p hp
    have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).2
    exact mul_le_mul_of_nonneg_right (uniformValuationLower_le R S p hS hprime.pos)
      (Real.log_nonneg (show (1 : Real) ≤ p by exact_mod_cast hprime.one_le))

def uniformPrimeMassLower (R S Q P : Nat) (I : Real) : Real :=
  2 * (max (uniformSmallOddLower R S Q P) 0 +
    max (((S : Real) - 1 / 2) *
      (factorialLower R - triangularMass R * primeLogFactorialConstant P - triangularMass R * I) -
        squareMass R * I / 2) 0)

theorem smallOddValuationMass_nonneg (R S P : Nat) : 0 ≤ smallOddValuationMass R S P := by
  unfold smallOddValuationMass
  apply Finset.sum_nonneg
  intro p hp
  have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).1).2
  exact mul_nonneg (by positivity)
    (Real.log_nonneg (show (1 : Real) ≤ p by exact_mod_cast hprime.one_le))

theorem uniformPrimeMassLower_le_production (R S Q P : Nat) (I : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hQ : 3 ≤ Q) :
    uniformPrimeMassLower R S Q P I ≤ enderPrimeMassLower R S P I := by
  have hsmall := uniformSmallOddLower_le R S Q P hS hQ
  have hsmall0 := smallOddValuationMass_nonneg R S P
  have hfac := factorialSmallMass_le_uniform R P hR
  have hc : (0 : Real) ≤ (S : Real) - 1 / 2 := by
    have h : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have htail : ((S : Real) - 1 / 2) *
      (factorialLower R - triangularMass R * primeLogFactorialConstant P - triangularMass R * I) -
        squareMass R * I / 2 ≤ enderTailLower R S P I := by
    unfold enderTailLower
    nlinarith
  have hs := max_le hsmall hsmall0
  have ht := max_le_max htail (le_refl (0 : Real))
  unfold uniformPrimeMassLower enderPrimeMassLower
  linarith

theorem uniform_missing_S_guard_false : ¬ uniformValuationLower 1 0 7 ≤ valuationWeight 1 0 7 := by
  norm_num [uniformValuationLower, triangularMass, squareMass, valuationWeight]

theorem uniform_missing_floor_error_false : ¬
    (((2 : Real) - 1 / 2) * (triangularMass 2 / 7) - squareMass 2 / (2 * 7 ^ 2)) ≤
      valuationWeight 2 2 7 := by
  norm_num [triangularMass, squareMass, valuationWeight, Finset.sum_range_succ]

theorem uniform_missing_quadratic_loss_false : ¬
    (((2 : Real) - 1 / 2) * (triangularMass 30 / 7 - 30)) ≤
      valuationWeight 30 2 7 := by
  norm_num [triangularMass, valuationWeight, Finset.sum_range_succ]

theorem uniform_retaining_two_false : ¬
    uniformSmallOddLower 20 20 2 2 ≤ smallOddValuationMass 20 20 2 := by
  rw [smallOddValuationMass_eq_padded]
  have he : (productionSmallPrimes 2).filter (fun p => p ≠ 2) = ∅ := by decide
  rw [he, Finset.sum_empty]
  have ht : retainedSmallPrimes 2 2 = {2} := by decide
  have hv : uniformSmallOddLower 20 20 2 2 = (4615 / 4 : Real) * Real.log 2 := by
    norm_num [uniformSmallOddLower, primeLogLinearConstant, primeLogSquareConstant,
      primeLogErrorConstant, ht, triangularMass, squareMass]
    ring
  rw [hv]
  exact not_le_of_gt (mul_pos (by norm_num) (Real.log_pos (by norm_num)))

/-- The uniform envelope still bounds the same chosen-radius actual Gram. -/
theorem ellipse_uniformPrimeMassLower_le_counted_upperB
    (D₁ D D₂ rho R S Y Q P : Nat)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hQ : 3 ≤ Q) (hP : 2 ≤ P) (hRS : R ≤ P * S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    uniformPrimeMassLower R S Q P (enderTailIntegral P) ≤
      enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) :=
  (uniformPrimeMassLower_le_production R S Q P _ hR hS hQ).trans
    (ellipse_enderPrimeMassLower_le_counted_upperB D₁ D D₂ rho R S Y P
      hD₁ hDlo hDhi hR hS hP hRS hDsq hclass hRcut hRrho hY hradius)

end
end TenthDiscriminant
