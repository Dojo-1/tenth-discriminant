import Mathlib

/-!
# Phase209 — conditional *scalar* threshold bridge at fourth root 321

This is NOT a number-field theorem. The source-exact arithmetic column-depth
divisibility, geometry, 321-domain analytic upper and class-number transport
remain distinct prerequisites. This file proves the rational endpoint margin
and the abstract no-overlap interface only.

All constants are deliberately frozen by preregistration Issues #154–156.
-/
namespace TenthDiscriminant.Phase209Scalar321

noncomputable section

/-- Existing original thin-ellipse sufficient cell-cover has positive
rational buffer even at root 321; not by itself a point-count theorem. -/
theorem source_cell_cover_buffer_321 :
    (0 : ℚ) <
      (11/25 - (1001/1000)*(407/1000))*321 - 10 := by
  norm_num

/-- A rational specialization of the pre-existing exact ellipse-upper
formula. Turning it into an actual Q-cardinality theorem still requires
the original geometric assumptions and the corresponding Lean bridge. -/
theorem source_upper_count_ratio_321 :
    (22/7 : ℚ)*(11/25+1/(321^3))^2
      + 22/(25*321) + 3/(321^4)
      + 22/(25*321^3) + 2/(321^6) < 31/50 := by
  norm_num

/-- A fully exact rational margin at 321^4, assuming the old 322 affine
pair remains valid on the 321-domain and the *new* same-Gram derivative
depth bonus has been established. The inequality on its own proves NO
source geometry, Cauchy–Binet factorization, or field exclusion. -/
theorem rational_budget_321 :
    (1/2000 : ℚ) <
      (999997/1000000-4/5)*(4*(57714/10000))
       - 57193/10000 + 1853/2000 + 6931/40000
       + (50/(31*101))*(1098/9000+1609/25000)
       - (5/(321^4))*((2+1/9)*(11/10)+(2+1/25)*(161/100)) := by
  norm_num

/-- Abstract, same-scalar no-overlap reduction. To apply this to the
original Gram one must *separately* prove the strengthened lower bound and
the original analytic upper under hypotheses beginning at 321^4.
This theorem is not the substantive source-bound proof. -/
theorem no_scalar_overlap_321_conditional
    (u g beta : ℝ)
    (hlog : (4 * (57714/10000) : ℝ) ≤ u)
    (hupper : g ≤ (4/5 : ℝ)*u - 1853/2000)
    (hlower : (999997/1000000 : ℝ)*u - 57193/10000
      + 6931/40000 + beta ≤ g)
    (hbonus :
      (50/(31*101) : ℝ)*(1098/9000+1609/25000)
       - (5/(321^4))*((2+1/9)*(11/10)+(2+1/25)*(161/100))
      ≤ beta) : False := by
  have hfixed :
      (0 : ℝ) <
      (999997/1000000-4/5)*(4*(57714/10000))
       - 57193/10000 + 1853/2000 + 6931/40000
       + (50/(31*101))*(1098/9000+1609/25000)
       - (5/(321^4))*((2+1/9)*(11/10)+(2+1/25)*(161/100)) := by
    norm_num
  linarith

end
end TenthDiscriminant.Phase209Scalar321
