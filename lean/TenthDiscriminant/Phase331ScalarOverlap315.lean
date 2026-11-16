import TenthDiscriminant.Phase323ThinUpper315
import TenthDiscriminant.Log315Certificate

/-!
# Phase331: unconditional REAL scalar contradiction at D >= 315^4

This file is a pure scalar statement: if one SAME Gram simultaneously
satisfies the candidate full normalized lower and the previously
constructed 315-domain Hadamard upper, those inequalities conflict.

It does not assert that the full lower holds on Qthin; that proof is
separate (Phase331SameGramLower315). No classification theorem is used.
-/
namespace TenthDiscriminant.Phase331
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- The coefficient-level separation remains positive even with
coarse, transparent 315-domain denominator errors:
16895455/(625000 D) <= 1/100000 and 42/R <= 1/1000000.
The actual rational margin under these weaker errors is >0.000195.
-/
theorem strict_scalar_separation_315 (D : Nat)
    (hD : (315 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D-1853/2000 <
    (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) := by
  have hlog := TenthDiscriminant.log_floor_from_315_fourth_power D hD
  have hlog2 := TenthDiscriminant.log_two_rational_control.1
  have hd := Tuned.dimensions_315 D hD
  have hDint : 9845600625 ≤ D := by
    have he : (315 : Nat)^4 = 9845600625 := by norm_num
    simpa only [he] using hD
  have hDreal : (9845600625 : Real) ≤ (D : Real) := by
    exact_mod_cast hDint
  have hDpos : (0 : Real) < D := by linarith
  have hDden : (0 : Real) < 625000*(D : Real) := by positivity
  have hDerr : (16895455 : Real)/(625000*(D : Real)) ≤ 1/100000 := by
    apply (div_le_iff₀ hDden).2
    nlinarith only [hDreal]
  have hRreal : (100000000 : Real) ≤ (Tuned.R D : Real) := by
    exact_mod_cast hd.1
  have hRpos : (0 : Real) < (Tuned.R D : Real) := by linarith
  have hRerr : (2 : Real)/(Tuned.R D : Real) +
      40/(Tuned.R D : Real) ≤ 1/1000000 := by
    calc
      (2 : Real)/(Tuned.R D : Real) +
          40/(Tuned.R D : Real) =
          42/(Tuned.R D : Real) := by ring
      _ ≤ 1/1000000 := by
        apply (div_le_iff₀ hRpos).2
        nlinarith only [hRreal]
  linarith only [hlog,hlog2,hDerr,hRerr]

/-- If one normalized original Gram is above the source mass
and below the source Hadamard upper, there is no possible real value
for it above the 315^4 endpoint. -/
theorem no_same_gram_scalar_overlap_315
    (D : Nat) (hD : (315 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-1853/2000)
    (hLower :
      (999997/1000000 : Real)*Real.log D-57193/10000 +
        Real.log 2/4 +
        ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
        ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
        ((873747/250000000 : Real)-40/(Tuned.R D : Real)) ≤ g) : False := by
  have hsep := strict_scalar_separation_315 D hD
  linarith only [hsep,hUpper,hLower]

end
end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.no_same_gram_scalar_overlap_315
