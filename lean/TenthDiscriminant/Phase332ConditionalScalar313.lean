import TenthDiscriminant.Phase332Log313Certificate
import TenthDiscriminant.Phase323ThinUpper315

/-!
Phase332 conditional *scalar* 313^4 separation.

This theorem establishes a positive real-number interval separation
at D >= 313^4 *IF* the original-Gram arithmetic lower includes the
additional mixed binary horizontal gain 665/100000 - 2/R, and the
original 315-domain source/analytic hypotheses have been genuinely
re-established at 313.

NOT a determinant divisibility theorem.
NOT an original-Q Hadamard theorem at 313.
NOT a class-number-one or number-field discriminant theorem.
-/
namespace TenthDiscriminant.Phase332
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Conservative pointwise no-overlap. The extra +0.00665 comes from
the proposed guarded H(Z,W) source polynomial, but its universal
determinant proof is still explicitly separate. -/
theorem conditional_strict_scalar_separation_313 (D : Nat)
    (hD : (313 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D-1853/2000 <
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) +
      ((665/100000 : Real)-2/(Tuned.R D : Real)) := by
  have hlog := log_floor_from_313_fourth_power D hD
  have hlog2 := TenthDiscriminant.log_two_rational_control.1
  have hDint : 9597924961 ≤ D := by
    have he : (313 : Nat)^4 = 9597924961 := by norm_num
    simpa only [he] using hD
  have hDreal : (9597924961 : Real) ≤ (D : Real) :=
    by exact_mod_cast hDint
  have hDpos : (0 : Real) < D := by linarith
  have hDden : (0 : Real) < 625000*(D : Real) := by positivity
  have hDerr : (16895455 : Real)/(625000*(D : Real)) ≤ 1/100000 := by
    apply (div_le_iff₀ hDden).2
    nlinarith only [hDreal]
  have hRnat : 100000000 ≤ Tuned.R D := by
    unfold Tuned.R Tuned.envelopeR
    omega
  have hRreal : (100000000 : Real) ≤ Tuned.R D := by
    exact_mod_cast hRnat
  have hRpos : (0 : Real) < (Tuned.R D : Real) := by linarith
  have hRerr : (2 : Real)/(Tuned.R D : Real) +
      40/(Tuned.R D : Real) +
      2/(Tuned.R D : Real) ≤ 1/1000000 := by
    calc
      (2 : Real)/(Tuned.R D : Real) +
        40/(Tuned.R D : Real) +
        2/(Tuned.R D : Real) =
          44/(Tuned.R D : Real) := by ring
      _ ≤ 1/1000000 := by
        apply (div_le_iff₀ hRpos).2
        nlinarith only [hRreal]
  linarith only [hlog,hlog2,hDerr,hRerr]

end
end TenthDiscriminant.Phase332

#print axioms TenthDiscriminant.Phase332.conditional_strict_scalar_separation_313
