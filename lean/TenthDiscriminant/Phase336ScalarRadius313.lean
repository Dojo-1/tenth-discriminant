import TenthDiscriminant.Phase332SourceGeometry313
import TenthDiscriminant.Phase332Log313Certificate
import TenthDiscriminant.Phase332StrongerRadius315

/-!
# Phase336 — 313-domain radius and scalar separation WITHOUT mixed binary mass

The 313-domain logarithmic floor, point-count geometry and positive
original Gram have already been separately established in Phase332.
At the new 313-domain floor, we:
* prove the unchanged radii obey thinRadius <= (17/20)*rho;
* use the verified Phase332 savings theorem (27/200);
* establish an unconditional REAL scalar inequality with the original
  Phase331 lower SHAPE but WITHOUT the unproved Phase332 H(Z,W) gain.

A scalar inequality does not establish its premises for a field.
No assertion of an actual 313-domain determinant upper/lower is made
in this file. No new local prime valuations or samples are used.

The next source-exact obligations are the ORIGINAL analytic upper and
arithmetic lower at D >= 313^4, on literally the same Gram determinant.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned
set_option autoImplicit false
noncomputable section

/-- The stronger 17/20 ratio already holds at D >= 313^4, with
exactly the original integer ceilings and radii. -/
theorem thin_radius_fraction_17_20_313 (D : Nat)
    (hD : (313 : Nat)^4 ≤ D) :
    (thinRadius D : Real) ≤ (17/20 : Real) * rho D := by
  have ht := fourthRoot_ge_313 D hD
  have hcube : (313 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (thinRadius D : Real) <
      (11/25 : Real)*fourthRoot D^3+1 := by
    unfold thinRadius
    exact Nat.ceil_lt_add_one (by positivity)
  have hlarge : (13/25 : Real)*fourthRoot D^3 ≤ rho D := by
    unfold rho
    exact Nat.le_ceil _
  nlinarith only [hcube,hceil,hlarge]

end
end TenthDiscriminant.FirstCertificate.Tuned

namespace TenthDiscriminant.Phase336
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- The VERIFIED 313-log floor and the VERIFIED 27/200 radius saving
provide a strict separation of two real expressions WITHOUT the
unverified mixed H determinant gain (+0.00665).

Important: this compares real formulas only. It is not a conclusion
about any source Gram until the two SAME-Gram bounds are obtained
separately for the entire 313-domain. -/
theorem strong_scalar_separation_313_without_mixed (D : Nat)
    (hD : (313 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D-1923/2000 <
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) := by
  have hlog := TenthDiscriminant.Phase332.log_floor_from_313_fourth_power D hD
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
    unfold Tuned.R envelopeR
    omega
  have hRreal : (100000000 : Real) ≤ Tuned.R D := by
    exact_mod_cast hRnat
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

/-- A source-fidelity conditional contradiction on one common REAL
value g. The hypotheses explicitly demand BOTH numerical bounds.
This intentionally does NOT claim that a Gram satisfies them at 313. -/
theorem no_scalar_overlap_313_without_mixed
    (D : Nat) (hD : (313 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-1923/2000)
    (hLower :
      (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) ≤ g) :
    False := by
  have hgap := strong_scalar_separation_313_without_mixed D hD
  linarith

end
end TenthDiscriminant.Phase336

#print axioms TenthDiscriminant.FirstCertificate.Tuned.thin_radius_fraction_17_20_313
#print axioms TenthDiscriminant.Phase336.strong_scalar_separation_313_without_mixed
#print axioms TenthDiscriminant.Phase336.no_scalar_overlap_313_without_mixed
