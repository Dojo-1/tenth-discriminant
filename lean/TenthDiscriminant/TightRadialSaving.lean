import TenthDiscriminant.SharpRadialDetBound

/-! Phase133: same actual integer ordinary-jet Gram; only the uniform
rectangle savings change. All original arithmetic and field objects survive. -/
namespace TenthDiscriminant.TightRadialSaving
open Polynomial FirstCertificate
open scoped BigOperators ComplexConjugate Classical
set_option autoImplicit false
noncomputable section

theorem logarithm_gain_tight :
    (231/500 : Real) ≤ Real.log (100/63 : Real) := by
  have hc : checkPositiveLogBounds 4 (100/63) 0 (231/500) (47/100)=true := by
    norm_num [checkPositiveLogBounds,binaryLogLowerRat,binaryLogUpperRat,
      oddLogPrefixRat,oddLogRemainderRat,Finset.sum_range_succ]
  have h := (checkPositiveLogBounds_sound 4 (100/63) 0
    (231/500) (47/100) hc).1
  push_cast at h
  exact h

/-- Uniform across 25S ≤ R ≤ 26S. Uses an exact nonnegative factorisation
    for t=R-25S, and does NOT alter any original trace Gram observation. -/
theorem scale_gain_tight (R S : Nat)
    (hS : 100 ≤ S) (hlo : 25*S ≤ R) (hhi : R ≤ 26*S) :
    (23/2000 : Real)*(R^2*S : Nat) ≤
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*
        Real.log (100/63 : Real) := by
  have hS' : (100 : Real) ≤ S := by exact_mod_cast hS
  have hlo' : (25 : Real)*S ≤ R := by exact_mod_cast hlo
  have hhi' : (R : Real) ≤ 26*S := by exact_mod_cast hhi
  have h9 : 9*S ≤ R := by omega
  have h1 : 1 ≤ S := by omega
  rw [Nat.cast_sub h9, Nat.cast_sub h1]
  push_cast
  have hS0 : (0 : Real) ≤ S := by positivity
  have hR0 : (0 : Real) ≤ (R : Real)-9*S := by linarith
  have hSm1 : (0 : Real) ≤ (S : Real)-1 := by linarith
  have hS99 : (99/100 : Real)*S ≤ (S : Real)-1 := by linarith
  /- 676*S*(R-9*S)-17*R² =
     (S-t)*(191*S+17*t) ≥ 0 with 0≤t≤S. -/
  have hfact : (0 : Real) ≤
      (S-((R : Real)-25*S))*(191*S+17*((R : Real)-25*S)) := by
    apply mul_nonneg
    · linarith
    · nlinarith only [hlo', hS']
  have hquad : 17*(R : Real)^2 ≤ 676*((R : Real)-9*S)*S := by
    nlinarith only [hfact]
  have hsc : 17*((R : Real)^2*S) ≤
      676*((R : Real)-9*S)*S^2 := by
    have h := mul_le_mul_of_nonneg_right hquad hS0
    nlinarith only [h]
  have hsc' : (R : Real)^2*S ≤
      (676/17 : Real)*((R : Real)-9*S)*S^2 := by
    nlinarith only [hsc]
  calc
    (23/2000 : Real)*((R : Real)^2*S) ≤
        ((R : Real)^2*S)*(388773/33800000 : Real) := by
          have hc : (23/2000 : Real) ≤ 388773/33800000 := by norm_num
          nlinarith [mul_nonneg
            (show (0 : Real) ≤ (R : Real)^2*S by positivity)
            (show (0 : Real) ≤ (388773/33800000 : Real)-23/2000 by norm_num)]
    _ ≤ ((676/17 : Real)*((R : Real)-9*S)*S^2)*
        (388773/33800000 : Real) := by
      exact mul_le_mul_of_nonneg_right hsc' (by norm_num)
    _ = ((R : Real)-9*S)*S*((99/100 : Real)*S)*(231/500 : Real) := by
      ring
    _ ≤ ((R : Real)-9*S)*S*((S : Real)-1)*(231/500 : Real) := by
      gcongr
      exact mul_nonneg hR0 hS0
    _ ≤ ((R : Real)-9*S)*S*((S : Real)-1)*Real.log (100/63 : Real) := by
      exact mul_le_mul_of_nonneg_left logarithm_gain_tight
        (mul_nonneg (mul_nonneg hR0 hS0) hSm1)

theorem constant_sanity :
    (23/2000 : Real) < 388773/33800000 ∧
    (0 : Real) < 73/33800000 := by
  norm_num

/-- A stronger upper for the SAME integerRectangularTraceGram. -/
theorem normalized_integer_upper_tight
    (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hD : 0 < D) (hS : 100 ≤ S) (h25 : 25*S ≤ R) (h26 : R ≤ 26*S)
    (hrho : 10 ≤ rho) (hRrho : rho < R)
    (hcard : 2*(R-1)+(S-1) < Q.card)
    (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) :
    Real.log ((integerRectangularTraceGram Q D S R S).det : Real)/
      comparisonScale R S ≤
      enderUpperB R S S rho n/comparisonScale R S-23/2000 := by
  have hu := SharpRadialDetBound.integer_log_upper Q D R S rho n
    hD (by omega) (by omega) hrho hRrho hcard hnpos hn hbound
  have ht := comparisonScale_pos R S (by omega) (by omega)
  have hg : (23/2000 : Real)*comparisonScale R S ≤
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*
        Real.log (100/63 : Real) := by
    simpa only [comparisonScale,Nat.cast_mul,Nat.cast_pow] using
      scale_gain_tight R S hS h25 h26
  have hgn : (23/2000 : Real) ≤
      ((R-9*S : Nat)*(S : Real)*(S-1 : Nat)*
        Real.log (100/63 : Real))/comparisonScale R S := by
    apply (le_div_iff₀ ht).2
    simpa only [div_eq_mul_inv,mul_comm,one_mul] using hg
  calc
    _ ≤ (enderUpperB R S S rho n-
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*
        Real.log (100/63 : Real))/comparisonScale R S :=
      div_le_div_of_nonneg_right hu ht.le
    _ = _ := sub_div _ _ _
    _ ≤ _ := sub_le_sub_left hgn _

theorem production_normalized_upper_tight (D : Nat)
    (hD : 41006250000 ≤ D) :
    Real.log ((integerRectangularTraceGram
        (ellipsePairs D (Tuned.rho D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real)/
      comparisonScale (Tuned.R D) (Tuned.S D) ≤
        (4/5 : Real)*Real.log D-1649/2000 := by
  obtain ⟨hS,h25,h26,h10⟩ := SharpRadialDetBound.production_guards D hD
  have hd := Tuned.dimensions D hD
  have hD0 : 0 < D := by omega
  have hc := ellipsePairs_card_gt_of_ender_radius D (Tuned.rho D)
    (3*Tuned.R D+Tuned.S D) hD0 (by omega) (Tuned.chosen_radius D hD)
  have hcard : 2*(Tuned.R D-1)+(Tuned.S D-1) <
      (ellipsePairs D (Tuned.rho D)).card := by omega
  have hn := ellipsePairs_card_le_padded_upper_count D D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D)) hD0 le_rfl le_rfl
  have hnpos : 0 < ellipsePaddedUpperCount D (Tuned.rho D)
      (ellipseVerticalBound D (Tuned.rho D)) :=
    lt_of_lt_of_le
      (by exact_mod_cast
        (show 0 < (ellipsePairs D (Tuned.rho D)).card by omega)) hn
  have hbound (q : Int × Int) (hq : q ∈ ellipsePairs D (Tuned.rho D)) :
      ‖pairEval D q‖ ≤ Tuned.rho D := by
    apply ellipsePoint_norm_le D (Tuned.rho D) hD0
    exact Finset.mem_image.mpr ⟨q,hq,rfl⟩
  have hu := normalized_integer_upper_tight
    (ellipsePairs D (Tuned.rho D)) D (Tuned.R D)
    (Tuned.S D) (Tuned.rho D)
    (ellipsePaddedUpperCount D (Tuned.rho D)
      (ellipseVerticalBound D (Tuned.rho D)))
    hD0 hS h25 h26 h10
    (Tuned.radius_lt_R D hD) hcard hnpos hn hbound
  linarith [Tuned.normalized_upper D hD]

end
end TenthDiscriminant.TightRadialSaving
