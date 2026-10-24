import TenthDiscriminant.PrimeMassAssembly
import Mathlib.Analysis.SumIntegralComparisons

/-!
# The production `upper_B` bound at integer radii

This module bounds the *actual* trace-Gram diagonal product by Ender's
unchanged upper formula on the `R>rho` branch at integer radii. It checks
the falling-factorial bound, exact rectangular sum, logarithmic integral
correction and Python's integer coefficients. The upper ellipse count,
factorial prime-mass estimate and numerical certificates remain separate.
-/

namespace TenthDiscriminant

set_option autoImplicit false

/-- Reindex the unchanged row-major Gram rows as Ender's rectangle. -/
theorem rectangular_row_sum (R S : Nat) (f : Nat → Nat → Real) :
    (∑ i : Fin (R * S), f (i.val / S) (i.val % S)) =
      ∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S, f r s := by
  have he := Fintype.sum_equiv
    (finProdFinEquiv : Fin R × Fin S ≃ Fin (R * S))
    (fun rs => f ((finProdFinEquiv rs).val / S)
      ((finProdFinEquiv rs).val % S))
    (fun i => f (i.val / S) (i.val % S)) (fun _ => rfl)
  rw [← he]
  simp only [Fintype.sum_prod_type, Finset.sum_fin_eq_sum_range]
  apply Finset.sum_congr rfl
  intro r hr
  simp only [dif_pos (Finset.mem_range.mp hr)]
  apply Finset.sum_congr rfl
  intro s hs
  simp only [dif_pos (Finset.mem_range.mp hs)]
  have hsS : s < S := Finset.mem_range.mp hs
  have hSpos : 0 < S := lt_of_le_of_lt (Nat.zero_le s) hsS
  change f ((s + S * r) / S) ((s + S * r) % S) = f r s
  rw [Nat.add_mul_div_left s r hSpos, Nat.div_eq_of_lt hsS,
    Nat.add_mul_mod_self_left, Nat.mod_eq_of_lt hsS]
  simp

/-- A radial bound on every sample gives the exact power-moment estimate;
the finite set may be empty and the exponent may be zero. -/
theorem normMoment_le_card_mul_pow (P : Finset Complex) (B : Real)
    (hbound : ∀ z ∈ P, ‖z‖ ≤ B) (k : Nat) :
    normMoment P k ≤ (P.card : Real) * B ^ (2 * k) := by
  unfold normMoment
  calc
    ∑ z ∈ P, Complex.normSq z ^ k ≤ ∑ _z ∈ P, B ^ (2 * k) := by
      apply Finset.sum_le_sum
      intro z hz
      have hsq : Complex.normSq z ≤ B ^ 2 := by
        rw [Complex.normSq_eq_norm_sq]
        exact pow_le_pow_left₀ (norm_nonneg z) (hbound z hz) 2
      calc
        Complex.normSq z ^ k ≤ (B ^ 2) ^ k :=
          pow_le_pow_left₀ (Complex.normSq_nonneg z) hsq k
        _ = B ^ (2 * k) := by rw [pow_mul]
    _ = (P.card : Real) * B ^ (2 * k) := by simp [nsmul_eq_mul]

/-- The exact ordinary-derivative diagonal is bounded termwise by the
radial moment estimate, without replacing it by a surrogate matrix. -/
theorem traceGram_diagonal_le_radial_sum (P : Finset Complex)
    (J r s : Nat) (B : Real)
    (hbound : ∀ z ∈ P, ‖z‖ ≤ B) :
    traceGramEntry P J r s r s ≤
      2 * (Finset.range J).sum (fun j =>
        if j ≤ r then (r.descFactorial j : Real) ^ 2 *
          (P.card : Real) * B ^ (2 * (r + s - j)) else 0) := by
  rw [traceGram_diagonal]
  apply mul_le_mul_of_nonneg_left ?_ (by norm_num)
  apply Finset.sum_le_sum
  intro j hj
  split_ifs with h
  · calc
      (r.descFactorial j : Real) ^ 2 * normMoment P (r + s - j) ≤
          (r.descFactorial j : Real) ^ 2 *
            ((P.card : Real) * B ^ (2 * (r + s - j))) :=
        mul_le_mul_of_nonneg_left
          (normMoment_le_card_mul_pow P B hbound _) (sq_nonneg _)
      _ = _ := by ring
  · exact le_refl _

/-- A falling-factorial derivative costs at most the radius power times
the exact `max(1,r/rho)` correction used by `upper_B`. -/
theorem radial_derivative_term_le (rho r s J j : Nat)
    (hrho : 0 < rho) (hj : j ≤ r) (hjJ : j < J) :
    (r.descFactorial j : Real) ^ 2 * (rho : Real) ^ (2 * (r + s - j)) ≤
      (rho : Real) ^ (2 * (r + s)) *
        (max 1 ((r : Real) / rho)) ^ (2 * (J - 1)) := by
  let m : Real := max 1 ((r : Real) / rho)
  have hρ : (0 : Real) < rho := by exact_mod_cast hrho
  have hm : 1 ≤ m := le_max_left _ _
  have hrm : (r : Real) ≤ (rho : Real) * m := by
    have h := le_max_right (1 : Real) ((r : Real) / rho)
    simpa only [mul_comm] using (div_le_iff₀ hρ).mp h
  have hdesc : (r.descFactorial j : Real) ≤ ((rho : Real) * m) ^ j := by
    calc
      (r.descFactorial j : Real) ≤ (r : Real) ^ j := by
        exact_mod_cast Nat.descFactorial_le_pow r j
      _ ≤ ((rho : Real) * m) ^ j :=
        pow_le_pow_left₀ (Nat.cast_nonneg _) hrm j
  have hterm : (r.descFactorial j : Real) ^ 2 *
      (rho : Real) ^ (2 * (r + s - j)) ≤
      (((rho : Real) * m) ^ j) ^ 2 *
        (rho : Real) ^ (2 * (r + s - j)) :=
    mul_le_mul_of_nonneg_right
      (pow_le_pow_left₀ (by positivity) hdesc 2) (pow_nonneg hρ.le _)
  have halg : (((rho : Real) * m) ^ j) ^ 2 *
      (rho : Real) ^ (2 * (r + s - j)) =
      (rho : Real) ^ (2 * (r + s)) * m ^ (2 * j) := by
    rw [← pow_mul, mul_pow]
    have he : 2 * j + 2 * (r + s - j) = 2 * (r + s) := by omega
    calc
      (rho : Real) ^ (j * 2) * m ^ (j * 2) *
          (rho : Real) ^ (2 * (r + s - j)) =
          (rho : Real) ^ (2 * j + 2 * (r + s - j)) * m ^ (2 * j) := by
            rw [pow_add]
            simp only [Nat.mul_comm j 2]
            ring
      _ = _ := by rw [he]
  calc
    _ ≤ (((rho : Real) * m) ^ j) ^ 2 *
          (rho : Real) ^ (2 * (r + s - j)) := hterm
    _ = (rho : Real) ^ (2 * (r + s)) * m ^ (2 * j) := halg
    _ ≤ (rho : Real) ^ (2 * (r + s)) * m ^ (2 * (J - 1)) :=
      mul_le_mul_of_nonneg_left
        (pow_le_pow_right₀ hm (by omega)) (pow_nonneg hρ.le _)

/-- Every actual diagonal entry obeys the uniform row bound from which
`upper_B` is assembled; no logarithm of zero is taken here. -/
theorem traceGram_diagonal_le_uniform (P : Finset Complex)
    (J r s rho : Nat) (hrho : 0 < rho)
    (hbound : ∀ z ∈ P, ‖z‖ ≤ (rho : Real)) :
    traceGramEntry P J r s r s ≤
      2 * (P.card : Real) * J * (rho : Real) ^ (2 * (r + s)) *
        (max 1 ((r : Real) / rho)) ^ (2 * (J - 1)) := by
  let C : Real := (P.card : Real) * (rho : Real) ^ (2 * (r + s)) *
    (max 1 ((r : Real) / rho)) ^ (2 * (J - 1))
  have hterm (j : Nat) (hj : j ∈ Finset.range J) :
      (if j ≤ r then (r.descFactorial j : Real) ^ 2 *
          normMoment P (r + s - j) else 0) ≤ C := by
    by_cases hjr : j ≤ r
    · simp only [if_pos hjr]
      have hmoment := normMoment_le_card_mul_pow P (rho : Real) hbound
        (r + s - j)
      have hrad := radial_derivative_term_le rho r s J j hrho hjr
        (Finset.mem_range.mp hj)
      calc
        (r.descFactorial j : Real) ^ 2 * normMoment P (r + s - j) ≤
            (r.descFactorial j : Real) ^ 2 *
              ((P.card : Real) * (rho : Real) ^ (2 * (r + s - j))) :=
          mul_le_mul_of_nonneg_left hmoment (sq_nonneg _)
        _ = (P.card : Real) * ((r.descFactorial j : Real) ^ 2 *
              (rho : Real) ^ (2 * (r + s - j))) := by ring
        _ ≤ C := by
          simpa only [C, mul_assoc] using
            mul_le_mul_of_nonneg_left hrad (Nat.cast_nonneg P.card)
    · simp only [if_neg hjr]
      dsimp [C]
      positivity
  have hsum : (Finset.range J).sum (fun j =>
        if j ≤ r then (r.descFactorial j : Real) ^ 2 *
          normMoment P (r + s - j) else 0) ≤ (J : Real) * C := by
    simpa [nsmul_eq_mul] using
      Finset.sum_le_card_nsmul (Finset.range J)
        (fun j => if j ≤ r then (r.descFactorial j : Real) ^ 2 *
          normMoment P (r + s - j) else 0) C hterm
  rw [traceGram_diagonal]
  calc
    _ ≤ 2 * ((J : Real) * C) :=
      mul_le_mul_of_nonneg_left hsum (by norm_num)
    _ = _ := by dsimp [C]; ring

/-- The integer-radius correction is bounded by its exact logarithmic
integral. The production `upper_B` adds a further nonnegative endpoint
term `log(R/rho)`, so this is a stronger subclaim on that branch. -/
theorem log_ratio_sum_le_integral (rho R : Nat)
    (hrho : 0 < rho) (hR : rho ≤ R) :
    (∑ r ∈ Finset.Ico rho R,
        Real.log ((r : Real) / (rho : Real))) ≤
      (R : Real) * Real.log ((R : Real) / (rho : Real)) - R + rho := by
  have hrhopos : (0 : Real) < rho := by exact_mod_cast hrho
  have hmono : MonotoneOn
      (fun x : Real => Real.log x - Real.log (rho : Real))
      (Set.Icc (rho : Real) (R : Real)) := by
    intro x hx y hy hxy
    exact sub_le_sub_right
      (Real.log_le_log (lt_of_lt_of_le hrhopos hx.1) hxy) _
  have hsum := MonotoneOn.sum_le_integral_Ico hR hmono
  have hident :
      (∑ r ∈ Finset.Ico rho R,
          Real.log ((r : Real) / (rho : Real))) =
        ∑ r ∈ Finset.Ico rho R,
          (Real.log (r : Real) - Real.log (rho : Real)) := by
    apply Finset.sum_congr rfl
    intro r hr
    have hrpos : (0 : Real) < r := by
      exact_mod_cast lt_of_lt_of_le hrho (Finset.mem_Ico.mp hr).1
    exact Real.log_div (ne_of_gt hrpos) (ne_of_gt hrhopos)
  have hint :
      (∫ x in (rho : Real)..(R : Real),
        Real.log x - Real.log (rho : Real)) =
      (R : Real) * Real.log ((R : Real) / (rho : Real)) - R + rho := by
    rw [intervalIntegral.integral_sub intervalIntegral.intervalIntegrable_log'
      (intervalIntegral.intervalIntegrable_const (Real.log (rho : Real))), integral_log,
      intervalIntegral.integral_const]
    rw [Real.log_div (by exact_mod_cast (lt_of_lt_of_le hrho hR).ne')
      (ne_of_gt hrhopos)]
    simp only [smul_eq_mul]
    ring
  rw [hident, ← hint]
  exact hsum

/-- All row indices below the integer radius contribute zero. Above it,
the exact logarithmic sum is bounded by the integral. -/
theorem log_derivative_correction_le (rho R : Nat)
    (hrho : 0 < rho) (hR : rho ≤ R) :
    (∑ r ∈ Finset.range R,
        max 0 (Real.log ((r : Real) / (rho : Real)))) ≤
      (R : Real) * Real.log ((R : Real) / (rho : Real)) - R + rho := by
  have hrhopos : (0 : Real) < rho := by exact_mod_cast hrho
  have hsplit :
      (∑ r ∈ Finset.range R,
        max 0 (Real.log ((r : Real) / (rho : Real)))) =
      ∑ r ∈ Finset.Ico rho R,
        Real.log ((r : Real) / (rho : Real)) := by
    rw [← Finset.sum_range_add_sum_Ico
      (fun r => max 0 (Real.log ((r : Real) / (rho : Real)))) hR]
    have hlow : (∑ r ∈ Finset.range rho,
        max 0 (Real.log ((r : Real) / (rho : Real)))) = 0 := by
      apply Finset.sum_eq_zero
      intro r hr
      have hrle : (r : Real) / rho ≤ 1 := by
        apply (div_le_iff₀ hrhopos).2
        simpa only [one_mul] using
          (by exact_mod_cast (Finset.mem_range.mp hr).le : (r : Real) ≤ rho)
      have hlog : Real.log ((r : Real) / rho) ≤ 0 :=
        Real.log_nonpos (div_nonneg (Nat.cast_nonneg _) hrhopos.le) hrle
      exact max_eq_left hlog
    rw [hlow, zero_add]
    apply Finset.sum_congr rfl
    intro r hr
    have hrle : 1 ≤ (r : Real) / rho := by
      apply (le_div_iff₀ hrhopos).2
      simpa only [one_mul] using
        (by exact_mod_cast (Finset.mem_Ico.mp hr).1 : (rho : Real) ≤ r)
    exact max_eq_right (Real.log_nonneg hrle)
  rw [hsplit]
  exact log_ratio_sum_le_integral rho R hrho hR

/-- The production formula's extra endpoint term is nonnegative on
the `R>rho` branch, so its stated correction follows unchanged. -/
theorem log_derivative_correction_le_upperB (rho R : Nat)
    (hrho : 0 < rho) (hR : rho < R) :
    (∑ r ∈ Finset.range R,
        max 0 (Real.log ((r : Real) / (rho : Real)))) ≤
      (R : Real) * Real.log ((R : Real) / (rho : Real)) - R + rho +
        Real.log ((R : Real) / (rho : Real)) := by
  have hbase := log_derivative_correction_le rho R hrho hR.le
  have hrhopos : (0 : Real) < rho := by exact_mod_cast hrho
  have hratio : 1 ≤ (R : Real) / rho := by
    apply (le_div_iff₀ hrhopos).2
    simpa only [one_mul] using
      (by exact_mod_cast hR.le : (rho : Real) ≤ R)
  linarith [Real.log_nonneg hratio]

theorem log_max_one_ratio (rho r : Nat) (hrho : 0 < rho) :
    Real.log (max 1 ((r : Real) / rho)) =
      max 0 (Real.log ((r : Real) / rho)) := by
  have hratio : (0 : Real) ≤ (r : Real) / rho := by positivity
  by_cases h : (r : Real) / rho ≤ 1
  · rw [max_eq_left h, Real.log_one,
      max_eq_left (Real.log_nonpos hratio h)]
  · have hge : 1 ≤ (r : Real) / rho := le_of_lt (lt_of_not_ge h)
    rw [max_eq_right hge, max_eq_right (Real.log_nonneg hge)]

/-- One positive diagonal entry has exactly the logarithmic row bound
whose rectangular sum is evaluated by the production formula. -/
theorem traceGram_log_diagonal_le (P : Finset Complex)
    (J r s rho : Nat) (n : Real) (hrho : 0 < rho) (hJ : 0 < J)
    (hnpos : 0 < n) (hn : (P.card : Real) ≤ n)
    (hbound : ∀ z ∈ P, ‖z‖ ≤ (rho : Real))
    (hpos : 0 < traceGramEntry P J r s r s) :
    Real.log (traceGramEntry P J r s r s) ≤
      Real.log (2 * n * J) + (2 * (r + s) : Nat) * Real.log (rho : Real) +
        (2 * (J - 1) : Nat) * max 0 (Real.log ((r : Real) / rho)) := by
  have hu := traceGram_diagonal_le_uniform P J r s rho hrho hbound
  have hnu : 2 * (P.card : Real) * J * (rho : Real) ^ (2 * (r + s)) *
      (max 1 ((r : Real) / rho)) ^ (2 * (J - 1)) ≤
      2 * n * J * (rho : Real) ^ (2 * (r + s)) *
        (max 1 ((r : Real) / rho)) ^ (2 * (J - 1)) := by
    gcongr
  have hlog := Real.log_le_log hpos (hu.trans hnu)
  rw [Real.log_mul (by positivity) (by positivity),
    Real.log_mul (by positivity) (by positivity),
    Real.log_pow, Real.log_pow, log_max_one_ratio rho r hrho] at hlog
  exact hlog

theorem sum_cast_range (N : Nat) :
    (∑ i ∈ Finset.range N, (i : Real)) = (N : Real) * (N - 1) / 2 := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Finset.sum_range_succ, ih]
    push_cast
    ring

/-- Evaluate the rectangular logarithmic row sum without changing the
row labels or discarding the derivative correction. -/
theorem rectangular_log_row_sum (R S J : Nat) (a b : Real) (f : Nat → Real) :
    (∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S,
      (a + (2 * (r + s) : Nat) * b + (2 * (J - 1) : Nat) * f r)) =
    (R : Real) * S * a +
      2 * b * ((S : Real) * R * (R - 1) / 2 +
        (R : Real) * S * (S - 1) / 2) +
      2 * S * ((J - 1 : Nat) : Real) * (∑ r ∈ Finset.range R, f r) := by
  have hsummand (r s : Nat) :
      a + (2 * (r + s) : Nat) * b + (2 * (J - 1) : Nat) * f r =
        a + (r : Real) * (2 * b) + (s : Real) * (2 * b) +
          f r * (2 * ((J - 1 : Nat) : Real)) := by
    push_cast
    ring
  trans ∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S,
    (a + (r : Real) * (2 * b) + (s : Real) * (2 * b) +
      f r * (2 * ((J - 1 : Nat) : Real)))
  · apply Finset.sum_congr rfl
    intro r hr
    apply Finset.sum_congr rfl
    intro s hs
    exact hsummand r s
  · simp only [Finset.sum_add_distrib,
      Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    simp only [← Finset.sum_mul, ← Finset.mul_sum, sum_cast_range]
    ring

/-- The logarithm of the original diagonal product is at most the exact
finite row sum that is bounded by `upper_B`. -/
theorem rectangularTraceGram_log_diag_le_rows (P : Finset Complex)
    (J R S rho : Nat) (n : Real) (hrho : 0 < rho) (hJ : 0 < J)
    (hnpos : 0 < n) (hn : (P.card : Real) ≤ n)
    (hbound : ∀ z ∈ P, ‖z‖ ≤ (rho : Real))
    (hpos : ∀ i : Fin (R * S), 0 < rectangularTraceGram P J R S i i) :
    Real.log (Finset.univ.prod (fun i => rectangularTraceGram P J R S i i)) ≤
      ∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S,
        (Real.log (2 * n * J) + (2 * (r + s) : Nat) * Real.log (rho : Real) +
          (2 * (J - 1) : Nat) * max 0 (Real.log ((r : Real) / rho))) := by
  rw [Real.log_prod Finset.univ _ (fun i _ => ne_of_gt (hpos i))]
  calc
    _ ≤ ∑ i : Fin (R * S),
        (Real.log (2 * n * J) +
          (2 * (i.val / S + i.val % S) : Nat) * Real.log (rho : Real) +
          (2 * (J - 1) : Nat) * max 0 (Real.log (((i.val / S : Nat) : Real) / rho))) := by
      apply Finset.sum_le_sum
      intro i hi
      exact traceGram_log_diagonal_le P J (i.val / S) (i.val % S) rho n
        hrho hJ hnpos hn hbound (hpos i)
    _ = _ := rectangular_row_sum R S (fun r s =>
      Real.log (2 * n * J) + (2 * (r + s) : Nat) * Real.log (rho : Real) +
        (2 * (J - 1) : Nat) * max 0 (Real.log ((r : Real) / rho)))

/-- The exact real expression evaluated by production `upper_B` when
`R>rho`, with the integer-radius campaign convention. -/
noncomputable def enderUpperB (R S J rho : Nat) (n : Real) : Real :=
  (R : Real) * S * Real.log (2 * n * J) +
    2 * Real.log (rho : Real) *
      ((S : Real) * R * (R - 1) / 2 + (R : Real) * S * (S - 1) / 2) +
    2 * S * ((J - 1 : Nat) : Real) *
      ((R : Real) * Real.log ((R : Real) / rho) - R + rho +
        Real.log ((R : Real) / rho))

/-- Python's two integer `//2` coefficients agree exactly with the real
triangular-number expression; no rounding is hidden in this translation. -/
theorem upperB_degree_coefficient_eq (R S : Nat) (hR : 1 ≤ R) (hS : 1 ≤ S) :
    ((S * R * (R - 1) / 2 + R * S * (S - 1) / 2 : Nat) : Real) =
      (S : Real) * R * (R - 1) / 2 + (R : Real) * S * (S - 1) / 2 := by
  have hdR : 2 ∣ S * R * (R - 1) :=
    (Nat.even_mul_pred_self R).two_dvd.trans ⟨S, by ring⟩
  have hdS : 2 ∣ R * S * (S - 1) :=
    (Nat.even_mul_pred_self S).two_dvd.trans ⟨R, by ring⟩
  rw [Nat.cast_add, Nat.cast_div hdR (by norm_num),
    Nat.cast_div hdS (by norm_num)]
  simp only [Nat.cast_mul, Nat.cast_sub hR, Nat.cast_sub hS,
    Nat.cast_one, Nat.cast_ofNat]

theorem enderUpperB_eq_production_coefficients (R S J rho : Nat) (n : Real)
    (hR : 1 ≤ R) (hS : 1 ≤ S) (hJ : 1 ≤ J) :
    enderUpperB R S J rho n =
      ((R * S : Nat) : Real) * Real.log (2 * n * J) +
      2 * Real.log (rho : Real) *
        ((S * R * (R - 1) / 2 + R * S * (S - 1) / 2 : Nat) : Real) +
      2 * S * ((J : Real) - 1) *
        ((R : Real) * Real.log ((R : Real) / rho) - R + rho +
          Real.log ((R : Real) / rho)) := by
  rw [upperB_degree_coefficient_eq R S hR hS]
  simp only [enderUpperB, Nat.cast_mul, Nat.cast_sub hJ, Nat.cast_one]

/-- The production upper expression bounds the logarithm of the actual
diagonal product once its sample-count input and diagonal positivity are
supplied. The ellipse count is a separate geometric premise. -/
theorem rectangularTraceGram_log_diag_le_upperB (P : Finset Complex)
    (J R S rho : Nat) (n : Real) (hrho : 0 < rho) (hRrho : rho < R)
    (hJ : 0 < J) (hnpos : 0 < n) (hn : (P.card : Real) ≤ n)
    (hbound : ∀ z ∈ P, ‖z‖ ≤ (rho : Real))
    (hpos : ∀ i : Fin (R * S), 0 < rectangularTraceGram P J R S i i) :
    Real.log (Finset.univ.prod (fun i => rectangularTraceGram P J R S i i)) ≤
      enderUpperB R S J rho n := by
  have hrows := rectangularTraceGram_log_diag_le_rows P J R S rho n
    hrho hJ hnpos hn hbound hpos
  rw [rectangular_log_row_sum] at hrows
  have hcorr := log_derivative_correction_le_upperB rho R hrho hRrho
  have hscaled := mul_le_mul_of_nonneg_left hcorr
    (by positivity : (0 : Real) ≤ 2 * S * ((J - 1 : Nat) : Real))
  unfold enderUpperB
  exact hrows.trans (add_le_add_left hscaled _)

/-- A positive-definite real matrix has positive diagonal entries, so
its logarithmic Hadamard product has no zero factors. -/
theorem real_posDef_diagonal_pos (N : Nat)
    (A : Matrix (Fin N) (Fin N) Real) (hA : A.PosDef) (i : Fin N) :
    0 < A i i := by
  have h := hA.2 (Pi.single i 1)
  simp_rw [Matrix.mulVec_single_one, ← Pi.single_star, star_one,
    single_dotProduct, one_mul, Matrix.transpose_apply,
    Function.ne_iff] at h
  exact h ⟨i, by simp⟩

theorem ellipsePoint_norm_le (D rho : Nat) (hD : 0 < D)
    (z : Complex) (hz : z ∈ ellipsePoints D rho) : ‖z‖ ≤ (rho : Real) := by
  obtain ⟨x, y, hxy, hsq⟩ := (mem_ellipsePoints_iff D rho hD z).mp hz
  rw [Complex.normSq_eq_norm_sq] at hsq
  have hρ : (0 : Real) ≤ rho := Nat.cast_nonneg _
  nlinarith [norm_nonneg z]

/-- Ender's checked radius supplies all diagonal positivity. Only the
upper sample-count input `n` remains a separate geometric premise. -/
theorem ellipseTraceGram_log_diag_le_upperB
    (D D₂ rho R S : Nat) (n : Real)
    (hD : 0 < D) (hD₂ : D ≤ D₂) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hRrho : rho < R)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real))
    (hn : ((ellipsePairs D rho).card : Real) ≤ n) :
    Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i)) ≤
      enderUpperB R S S rho n := by
  have hD₂pos : 0 < D₂ := lt_of_lt_of_le hD hD₂
  have hq : 0 < 3 * R + S := by omega
  have hcard₂ := ellipsePairs_card_gt_of_ender_radius D₂ rho (3 * R + S)
    hD₂pos hq hradius
  have hcard := lt_of_lt_of_le hcard₂ (ellipsePairs_card_antitone_D D D₂ rho hD₂)
  have hspos : 0 < Real.sqrt (D₂ : Real) :=
    Real.sqrt_pos.2 (by exact_mod_cast hD₂pos)
  have hβ := Real.sqrt_nonneg
    (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi)
  have hρreal : (0 : Real) < rho := by nlinarith
  have hρ : 0 < rho := by exact_mod_cast hρreal
  have hcount : 2 * (R - 1) + (S - 1) < (ellipsePoints D rho).card := by
    rw [ellipsePoints_card D rho hD]
    omega
  have hPD := rectangularTraceGram_posDef_of_point_count
    (ellipsePoints D rho) S R S hR hS le_rfl hcount
  have hnpos : 0 < n := lt_of_lt_of_le
    (by exact_mod_cast (lt_of_le_of_lt (Nat.zero_le _) hcard)) hn
  apply rectangularTraceGram_log_diag_le_upperB
    (ellipsePoints D rho) S R S rho n hρ hRrho (by omega) hnpos
  · simpa only [ellipsePoints_card D rho hD] using hn
  · exact fun z hz => ellipsePoint_norm_le D rho hD z hz
  · exact fun i => real_posDef_diagonal_pos (R * S) _ hPD i

/-- The class-number hypothesis, all odd local factors, the chosen-radius
geometry and the production upper expression now meet in one theorem.
The upper ellipse-count estimate is exposed as `hn`. -/
theorem ellipse_primeMass_log_le_upperB
    (D D₂ rho R S : Nat) (n : Real)
    (hD : 0 < D) (hD₂ : D ≤ D₂) (hR : 1 ≤ R) (hS : 1 ≤ S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real))
    (hn : ((ellipsePairs D rho).card : Real) ≤ n) :
    (∑ p ∈ oddPrimesBelow R,
      (2 * valuationWeight R S p : Nat) * Real.log (p : Real)) ≤
      enderUpperB R S S rho n := by
  exact (ellipse_allOddPrimeMass_log_le_hadamard D D₂ rho R S
    hD hD₂ hR hS hDsq hclass hRcut hradius).trans
      (ellipseTraceGram_log_diag_le_upperB D D₂ rho R S n
        hD hD₂ hR hS hRrho hradius hn)

/-- The constant row at radius one retains the factor-two normalization. -/
theorem upperB_constant_row_control :
    traceGramEntry {0} 1 0 0 0 0 = 2 := by
  norm_num [traceGramEntry, derivativeRow, Finset.sum_range_succ,
    Nat.descFactorial]

/-- Derivatives beyond the monomial degree contribute zero. -/
theorem upperB_derivative_cutoff_control :
    derivativeRow 0 3 1 (1 : Complex) = 0 := by
  norm_num [derivativeRow]

/-- The integral comparison includes the smallest legal integer radius. -/
theorem upperB_unit_radius_control :
    (∑ r ∈ Finset.range 2, max 0 (Real.log ((r : Real) / 1))) ≤
      2 * Real.log 2 - 1 := by
  have h := log_derivative_correction_le 1 2 (by decide) (by decide)
  norm_num only [Nat.cast_ofNat, div_one] at h
  simp only [div_one]
  linarith

/-- With no derivative observations, the required positive logarithm
argument cannot be supplied. -/
theorem upperB_zero_derivative_obstruction :
    ¬ 0 < traceGramEntry {0} 0 0 0 0 0 := by
  simp [traceGramEntry]

/-- An empty sample set also supplies no positive diagonal. -/
theorem upperB_empty_sample_obstruction (J r s : Nat) :
    ¬ 0 < traceGramEntry ∅ J r s r s := by
  simp [traceGramEntry]

/-- Omitting the sample-radius bound is false even in one row. -/
theorem upperB_sample_radius_guard_false :
    ¬ traceGramEntry {2} 1 1 0 1 0 ≤ 2 := by
  norm_num [traceGramEntry, derivativeRow, Finset.sum_range_succ,
    Nat.descFactorial]

/-- An understated count cannot be used as `n`: two constant observations
give diagonal four, whereas the one-observation bound would give two. -/
theorem upperB_sample_count_guard_false :
    ¬ traceGramEntry {0, 1} 1 0 0 0 0 ≤ 2 := by
  norm_num [traceGramEntry, derivativeRow, Finset.sum_range_succ,
    Nat.descFactorial]

end TenthDiscriminant
