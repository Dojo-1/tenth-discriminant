import TenthDiscriminant.Phase343Scalar307
import TenthDiscriminant.LogEnclosure

/-!
# Phase355 — scalar-only 302^4 separation, with 301^4 falsifier

The two scalar expressions are COPIED from Phase343Scalar307.
They do NOT become bounds on the original integer trace Gram merely
because they are numerically separated. Their source-validity at 302
is a separate mathematical task, and no actual field bound follows.
-/

namespace TenthDiscriminant.Phase355
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Honest rational-series enclosure for log 302, independent of floats. -/
theorem log_302_rational_enclosure :
    (571/100 : Real) ≤ Real.log 302 ∧
    Real.log 302 ≤ (572/100 : Real) := by
  have hc :
      checkPositiveLogBounds 5 302 8
        (571/100) (572/100) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 302 8
      (571/100) (572/100) hc
  norm_num at h
  rcases h with ⟨hlo, hhi⟩
  constructor
  · linarith
  · linarith

/-- A strict 302 fourth-power lower domain gives log D >= 22.840. -/
theorem log_floor_from_302_fourth_power (D : Nat)
    (hD : (302 : Nat)^4 ≤ D) :
    (22840/1000 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((302 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((302 : Nat)^4 : Nat) : Real) ≤
      (D : Real) := by exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [Nat.cast_pow, Real.log_pow] at hm
  have hlow : (571/100 : Real) ≤ Real.log (302 : Real) :=
    log_302_rational_enclosure.1
  have hscaled : (4 : Real)*(571/100 : Real) ≤
      (4 : Real)*Real.log (302 : Real) :=
    mul_le_mul_of_nonneg_left hlow (by norm_num)
  have heq : (4 : Real)*(571/100 : Real) = 22840/1000 := by
    norm_num
  rw [heq] at hscaled
  exact hscaled.trans hm

/-- The SAME real scalar expressions as Phase343/Phase348 separate
uniformly already at 302^4. This is a NUMERIC claim ONLY. -/
theorem strong_scalar_separation_302_without_mixed (D : Nat)
    (hD : (302 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D-1923/2000 <
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) := by
  have hlog := log_floor_from_302_fourth_power D hD
  have hlog2 := TenthDiscriminant.log_two_rational_control.1
  have hDint : 8318169616 ≤ D := by
    have he : (302 : Nat)^4 = 8318169616 := by norm_num
    simpa only [he] using hD
  have hDreal : (8318169616 : Real) ≤ (D : Real) :=
    by exact_mod_cast hDint
  have hDpos : (0 : Real) < D := by linarith
  have hDden : (0 : Real) < 625000*(D : Real) := by positivity
  have hDerr : (16895455 : Real)/(625000*(D : Real)) ≤ 1/100000 := by
    apply (div_le_iff₀ hDden).2
    nlinarith only [hDreal]
  have hRnat : 100000000 ≤ Tuned.R D := by
    unfold Tuned.R envelopeR
    omega
  have hRreal : (100000000 : Real) ≤ Tuned.R D :=
    by exact_mod_cast hRnat
  have hRpos : (0 : Real) < (Tuned.R D : Real) := by linarith
  have hRerr : (2 : Real)/(Tuned.R D : Real) +
      40/(Tuned.R D : Real) ≤ 1/1000000 := by
    calc
      (2 : Real)/(Tuned.R D : Real) +
        40/(Tuned.R D : Real) = 42/(Tuned.R D : Real) := by ring
      _ ≤ 1/1000000 := by
        apply (div_le_iff₀ hRpos).2
        nlinarith only [hRreal]
  linarith only [hlog,hlog2,hDerr,hRerr]

/-- If a future 302-source proof establishes BOTH bounds on the SAME g,
the resulting real interval is empty. No such source proof is claimed. -/
theorem no_scalar_overlap_302_without_mixed
    (D : Nat) (hD : (302 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-1923/2000)
    (hLower :
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) ≤ g) :
    False := by
  have hgap := strong_scalar_separation_302_without_mixed D hD
  linarith

/-- The PRE-registered 301 negative control uses the same finite
rational log series and no floating-point approximation. -/
theorem log_301_rational_enclosure :
    (5707/1000 : Real) ≤ Real.log 301 ∧
    Real.log 301 ≤ (57072/10000 : Real) := by
  have hc :
      checkPositiveLogBounds 5 301 8
        (5707/1000) (57072/10000) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 301 8
      (5707/1000) (57072/10000) hc
  norm_num at h
  rcases h with ⟨hlo, hhi⟩
  constructor
  · linarith
  · linarith

/-- Exact 301^4 source-parameter endpoint falsifies the claim that
these SAME scalar formulas are already separated there. -/
theorem original_scalar_301_not_strict :
    ¬ ((4/5 : Real)*Real.log ((301^4 : Nat) : Real)-1923/2000 <
      (999997/1000000 : Real)*Real.log ((301^4 : Nat) : Real)-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*((301^4 : Nat) : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R (301^4) : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R (301^4) : Real))) := by
  have hu : Real.log ((301^4 : Nat) : Real) ≤
      4*(57072/10000 : Real) := by
    rw [show (301^4 : Nat) = (301 : Nat)^4 by norm_num,
      Nat.cast_pow, Real.log_pow]
    nlinarith only [log_301_rational_enclosure.2]
  have h2 := TenthDiscriminant.log_two_rational_control.2
  have hposR : (0 : Real) < Tuned.R (301^4) := by
    norm_num [Tuned.R,envelopeR]
  have he1 : (0 : Real) ≤
      16895455/(625000*((301^4 : Nat) : Real)) := by positivity
  have he2 : (0 : Real) ≤
      2/(Tuned.R (301^4) : Real) := by positivity
  have he3 : (0 : Real) ≤
      40/(Tuned.R (301^4) : Real) := by positivity
  intro hbad
  linarith only [hu,h2,he1,he2,he3,hbad]

theorem conservative_margin_control :
    (0 : Real) < (318967/250000000 : Real) := by norm_num

end
end TenthDiscriminant.Phase355

#print axioms TenthDiscriminant.Phase355.log_floor_from_302_fourth_power
#print axioms TenthDiscriminant.Phase355.strong_scalar_separation_302_without_mixed
#print axioms TenthDiscriminant.Phase355.no_scalar_overlap_302_without_mixed
#print axioms TenthDiscriminant.Phase355.original_scalar_301_not_strict
