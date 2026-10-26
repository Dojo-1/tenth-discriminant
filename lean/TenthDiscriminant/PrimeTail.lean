import TenthDiscriminant.PrimeMassLower

/-!
# Ender's reciprocal-prime tail by a finite potential drop

The integer comparison is independent of primality. Summing a positive
potential drop telescopes; primes form a subset of the integer interval.
No infinite sum or prime-distribution input is used.
-/

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

def tailPotential (x : Real) : Real :=
  Real.log (x + 1) / x + Real.log (x + 1) - Real.log x

theorem tailPotential_hasDerivAt (x : Real) (hx : 0 < x) :
    HasDerivAt tailPotential (-Real.log (x + 1) / x ^ 2) x := by
  have hxne := ne_of_gt hx
  have hxone : x + 1 ≠ 0 := by positivity
  have hlog := ((hasDerivAt_id x).add_const 1).log hxone
  have h := (((hlog.div (hasDerivAt_id x) hxne).add hlog).sub
    (Real.hasDerivAt_log hxne))
  convert h using 1
  simp only [id_eq]
  field_simp [hxne, hxone]
  ring

theorem tailPotential_pos (x : Real) (hx : 0 < x) : 0 < tailPotential x := by
  have hlog : 0 < Real.log (x + 1) := Real.log_pos (by linarith)
  have hinc : Real.log x ≤ Real.log (x + 1) := Real.log_le_log hx (by linarith)
  have hdiv := div_pos hlog hx
  unfold tailPotential
  linarith

theorem tailPotential_eq_enderTailIntegral (P : Nat) (hP : 1 ≤ P) :
    tailPotential (P : Real) = enderTailIntegral P := by
  have hp : (0 : Real) < P := by exact_mod_cast (by omega : 0 < P)
  have hratio : 1 + 1 / (P : Real) = ((P : Real) + 1) / P := by
    field_simp
  unfold tailPotential enderTailIntegral
  rw [hratio, Real.log_div (by positivity) (ne_of_gt hp)]
  ring

/-- A monotone comparison primitive on one unit interval. Its derivative
is nonnegative because `x+1>=m` throughout `[m-1,m]`. -/
theorem tail_unit_step (m : Real) (hm : 1 < m) :
    Real.log m / (m * (m - 1)) ≤ tailPotential (m - 1) - tailPotential m := by
  let g : Real → Real := fun x => -tailPotential x + Real.log m / x
  have hderiv : ∀ x : Real, 0 < x →
      HasDerivAt g ((Real.log (x + 1) - Real.log m) / x ^ 2) x := by
    intro x hx
    have h := (tailPotential_hasDerivAt x hx).neg.add
      ((hasDerivAt_const x (Real.log m)).div (hasDerivAt_id x) (ne_of_gt hx))
    convert h using 1
    simp only [id_eq]
    field_simp [ne_of_gt hx]
    ring
  have hmono : MonotoneOn g (Set.Icc (m - 1) m) := by
    apply monotoneOn_of_hasDerivWithinAt_nonneg (convex_Icc (m - 1) m)
    · intro x hx
      exact (hderiv x (by linarith [hx.1])).continuousAt.continuousWithinAt
    · intro x hx
      have hxi : x ∈ Set.Icc (m - 1) m := interior_subset hx
      exact (hderiv x (by linarith [hxi.1])).hasDerivWithinAt
    · intro x hx
      have hxi : x ∈ Set.Icc (m - 1) m := interior_subset hx
      exact div_nonneg (sub_nonneg.mpr
        (Real.log_le_log (by linarith : 0 < m) (by linarith [hxi.1]))) (sq_nonneg x)
  have hends := hmono
    (show m - 1 ∈ Set.Icc (m - 1) m by constructor <;> linarith)
    (show m ∈ Set.Icc (m - 1) m by constructor <;> linarith) (by linarith)
  have hid : Real.log m / (m - 1) - Real.log m / m = Real.log m / (m * (m - 1)) := by
    field_simp [ne_of_gt (by linarith : 0 < m), ne_of_gt (by linarith : 0 < m - 1)]
    ring
  dsimp [g] at hends
  linarith

theorem integer_reciprocal_tail_le (P R : Nat) (hP : 1 ≤ P) :
    (∑ m ∈ Finset.Ico (P + 1) (R + 1),
      Real.log (m : Real) / ((m : Real) * ((m : Real) - 1))) ≤ tailPotential P := by
  by_cases hPR : P ≤ R
  · have hshift := Finset.sum_Ico_add'
      (fun m : Nat => Real.log (m : Real) / ((m : Real) * ((m : Real) - 1))) P R 1
    rw [← hshift]
    have hsteps : (∑ n ∈ Finset.Ico P R,
        Real.log ((n + 1 : Nat) : Real) /
          (((n + 1 : Nat) : Real) * (((n + 1 : Nat) : Real) - 1))) ≤
        ∑ n ∈ Finset.Ico P R, (tailPotential (n : Real) - tailPotential ((n + 1 : Nat) : Real)) := by
      apply Finset.sum_le_sum
      intro n hn
      have hnP := (Finset.mem_Ico.mp hn).1
      have hnreal : (1 : Real) < ((n + 1 : Nat) : Real) := by exact_mod_cast (by omega : 1 < n + 1)
      simpa only [Nat.cast_add, Nat.cast_one, add_sub_cancel_right] using
        tail_unit_step (((n + 1 : Nat) : Real)) hnreal
    have htel := Finset.sum_Ico_sub (f := fun n : Nat => tailPotential (n : Real)) hPR
    have hdrop : (∑ n ∈ Finset.Ico P R,
        (tailPotential (n : Real) - tailPotential ((n + 1 : Nat) : Real))) =
        tailPotential P - tailPotential R := by
      calc
        _ = -(∑ n ∈ Finset.Ico P R,
          (tailPotential ((n + 1 : Nat) : Real) - tailPotential (n : Real))) := by
          rw [← Finset.sum_neg_distrib]
          apply Finset.sum_congr rfl
          intro n hn
          ring
        _ = _ := by rw [htel]; ring
    rw [hdrop] at hsteps
    have hRpos : (0 : Real) < R := by exact_mod_cast (by omega : 0 < R)
    linarith [tailPotential_pos R hRpos]
  · have hempty : Finset.Ico (P + 1) (R + 1) = ∅ := Finset.Ico_eq_empty (by omega)
    rw [hempty, Finset.sum_empty]
    exact (tailPotential_pos P (by exact_mod_cast (by omega : 0 < P))).le

/-- The exact production tail constant bounds the actual finite prime
sum for every row bound R. Only its inclusion in the integer interval is used. -/
theorem largeReciprocalTail_le_enderTailIntegral (R P : Nat) (hP : 2 ≤ P) :
    largeReciprocalTail R P ≤ enderTailIntegral P := by
  have hsub : largeFactorialPrimes R P ⊆ Finset.Ico (P + 1) (R + 1) := by
    intro p hp
    have hpP := (Finset.mem_filter.mp hp).2
    have hpR := Finset.mem_range.mp (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).1
    exact Finset.mem_Ico.mpr ⟨by omega, by omega⟩
  have hsum : largeReciprocalTail R P ≤
      ∑ m ∈ Finset.Ico (P + 1) (R + 1),
        Real.log (m : Real) / ((m : Real) * ((m : Real) - 1)) := by
    apply Finset.sum_le_sum_of_subset_of_nonneg hsub
    intro m hm hmnot
    have hmP := (Finset.mem_Ico.mp hm).1
    have hmreal : (1 : Real) < m := by exact_mod_cast (by omega : 1 < m)
    exact div_nonneg (Real.log_nonneg hmreal.le)
      (mul_nonneg (by linarith) (sub_nonneg.mpr hmreal.le))
  rw [← tailPotential_eq_enderTailIntegral P (by omega)]
  exact hsum.trans (integer_reciprocal_tail_le P R (by omega))

theorem enderPrimeMassLower_le_exact_production (R S P : Nat)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hP : 2 ≤ P) (hRS : R ≤ P * S) :
    enderPrimeMassLower R S P (enderTailIntegral P) ≤ exactOddPrimeMass R S :=
  enderPrimeMassLower_le_exact_of_tail R S P (enderTailIntegral P) hR hS hP hRS
    (largeReciprocalTail_le_enderTailIntegral R P hP)

/-- Both mathematical production expressions now apply to the same Gram,
with the analytic tail discharged. Numerical enclosure checking is separate. -/
theorem ellipse_enderPrimeMassLower_le_counted_upperB
    (D₁ D D₂ rho R S Y P : Nat)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hP : 2 ≤ P) (hRS : R ≤ P * S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    enderPrimeMassLower R S P (enderTailIntegral P) ≤
      enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) := by
  exact ellipse_enderPrimeMassLower_le_upperB D₁ D D₂ rho R S Y P
    (enderTailIntegral P) hD₁ hDlo hDhi hR hS hP hRS hDsq hclass hRcut hRrho hY hradius
    (largeReciprocalTail_le_enderTailIntegral R P hP)

/-- A strict numerical comparison would now exclude class number one.
Its truth is still an explicit premise, not supplied by recorded Arb output. -/
theorem classNumber_ne_one_of_ender_comparison
    (D₁ D D₂ rho R S Y P : Nat)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hP : 2 ≤ P) (hRS : R ≤ P * S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real))
    (hgap : enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) <
      enderPrimeMassLower R S P (enderTailIntegral P)) :
    NumberField.classNumber (QuadraticField (((D : Int) + 1) / 4)) ≠ 1 := by
  intro hclass
  have h := ellipse_enderPrimeMassLower_le_counted_upperB D₁ D D₂ rho R S Y P
    hD₁ hDlo hDhi hR hS hP hRS hDsq hclass hRcut hRrho hY hradius
  exact (not_lt_of_ge h) hgap

theorem tail_step_two_control :
    Real.log 2 / 2 ≤ tailPotential 1 - tailPotential 2 := by
  have h := tail_unit_step 2 (by norm_num)
  norm_num at h
  exact h

theorem reciprocal_tail_empty_control (R P : Nat) (hRP : R ≤ P) :
    largeReciprocalTail R P = 0 := by
  unfold largeReciprocalTail
  apply Finset.sum_eq_zero
  intro p hp
  have hpP := (Finset.mem_filter.mp hp).2
  have hpR := Finset.mem_range.mp (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).1
  omega

theorem reciprocal_tail_two_control (R : Nat) :
    largeReciprocalTail R 2 ≤ enderTailIntegral 2 :=
  largeReciprocalTail_le_enderTailIntegral R 2 (by decide)

theorem tail_prime_at_boundary_control : 3 ∉ largeFactorialPrimes 5 3 := by decide

theorem reciprocal_tail_nonempty_control :
    largeReciprocalTail 4 2 = Real.log 3 / 6 := by
  have hs : largeFactorialPrimes 4 2 = {3} := by decide
  norm_num [largeReciprocalTail, hs]

theorem reciprocal_tail_zero_bound_false : ¬ largeReciprocalTail 4 2 ≤ 0 := by
  rw [reciprocal_tail_nonempty_control]
  exact not_le_of_gt (div_pos (Real.log_pos (by norm_num)) (by norm_num))

theorem enderTailIntegral_pos (P : Nat) (hP : 1 ≤ P) : 0 < enderTailIntegral P := by
  rw [← tailPotential_eq_enderTailIntegral P hP]
  exact tailPotential_pos P (by exact_mod_cast (by omega : 0 < P))

theorem tailPotential_at_zero_positive_false : ¬ 0 < tailPotential 0 := by
  norm_num [tailPotential]

end
end TenthDiscriminant
