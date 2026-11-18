import TenthDiscriminant.Euclid252Count
import TenthDiscriminant.EllipseUpperCount
import TenthDiscriminant.TightRadialSaving

/-!
# E15 - The original reduced-ellipse Gram has a uniform analytic upper

This is an exact specialization of the existing source-preserving
TightRadialSaving.normalized_integer_upper_tight theorem. E6 supplies
the count and positivity; the unchanged upper ellipse count supplies n.
No PSD determinant comparison with a different observation set, no
new prime mass, and no field cutoff are asserted here.
-/

namespace TenthDiscriminant.FirstCertificate.Tuned

set_option autoImplicit false
noncomputable section

/-- The 252 fourth-root cutoff is strong enough that the new radius
is smaller than the original row dimension and greater than 10. -/
theorem euclid_radius_guards_252 (D : Nat)
    (hD : (252 : Nat)^4 ≤ D) :
    10 ≤ euclidRadius D ∧ euclidRadius D < R D := by
  let t : Real := fourthRoot D
  have ht : (252 : Real) ≤ t := by
    dsimp [t, fourthRoot]
    apply Real.le_sqrt_of_sq_le
    apply Real.le_sqrt_of_sq_le
    exact_mod_cast (show (252 : Nat)^2^2 ≤ D by omega)
  have ht3 : (1 : Real) ≤ t^3 :=
    one_le_pow₀ (by linarith : (1 : Real) ≤ t)
  have ht3large : (252 : Real)^3 ≤ t^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have h4 : t^4 = (D : Real) := by
    simpa [t] using (fourthRoot_identities D).2.2
  have hlow : (81/200 : Real)*t^3 ≤ (euclidRadius D : Real) := by
    dsimp [t,euclidRadius]
    exact Nat.le_ceil _
  have hu : (euclidRadius D : Real) <
      (81/200 : Real)*t^3+1 := by
    dsimp [t,euclidRadius]
    exact Nat.ceil_lt_add_one (by positivity)
  have htenreal : (10 : Real) ≤ (euclidRadius D : Real) := by
    nlinarith only [ht3large, hlow]
  have hnonnegcube : (0 : Real) ≤ t^3 := by positivity
  have hgap : 0 ≤ (t-252)*t^3 :=
    mul_nonneg (by linarith) hnonnegcube
  have hrfloor : D ≤ 5*R D := by
    unfold R envelopeR
    omega
  have hrfloorReal : (D : Real) ≤ 5*(R D : Real) := by
    exact_mod_cast hrfloor
  have hbefore : 5*(euclidRadius D : Real) < (D : Real) := by
    nlinarith only [hgap,ht3,hu,h4]
  have hrlt : (euclidRadius D : Real) < (R D : Real) := by
    nlinarith only [hbefore,hrfloorReal]
  constructor
  · exact_mod_cast htenreal
  · exact_mod_cast hrlt

/-- The E6 ellipse works directly with the original integer Hadamard
source and the proven, source-compatible ellipse cardinality majorant.
The negative 23/2000 term is from the existing radial penalty, not
a fitted or newly invented scalar gain. -/
theorem euclid_normalized_upper_252 (D : Nat)
    (hD : (252 : Nat)^4 ≤ D) :
    Real.log
      ((integerRectangularTraceGram (ellipsePairs D (euclidRadius D))
        D (S D) (R D) (S D)).det : Real) /
      comparisonScale (R D) (S D) ≤
      enderUpperB (R D) (S D) (S D) (euclidRadius D)
        (ellipseUpperCount D (euclidRadius D)) /
        comparisonScale (R D) (S D) - 23/2000 := by
  have hDpos : 0 < D := by omega
  have hS100 : 100 ≤ S D := by
    unfold S R envelopeR
    omega
  have h25 : 25*S D ≤ R D := by
    unfold S R envelopeR
    omega
  have h26 : R D ≤ 26*S D := by
    unfold S R envelopeR
    omega
  obtain ⟨hrho,hrlt⟩ := euclid_radius_guards_252 D hD
  have hcard := euclid_interpolation_count_252 D hD
  have hn := ellipsePairs_card_le_upper_count D (euclidRadius D) hDpos
  have hpos : 0 < (ellipsePairs D (euclidRadius D)).card := by omega
  have hposReal :
      (0 : Real) < ((ellipsePairs D (euclidRadius D)).card : Real) := by
    exact_mod_cast hpos
  have hnpos : (0 : Real) < ellipseUpperCount D (euclidRadius D) :=
    lt_of_lt_of_le hposReal hn
  have hbound (q : Int × Int)
      (hq : q ∈ ellipsePairs D (euclidRadius D)) :
      ‖pairEval D q‖ ≤ euclidRadius D := by
    apply ellipsePoint_norm_le D (euclidRadius D) hDpos
    exact Finset.mem_image.mpr ⟨q,hq,rfl⟩
  exact TenthDiscriminant.TightRadialSaving.normalized_integer_upper_tight
    (ellipsePairs D (euclidRadius D)) D (R D) (S D)
    (euclidRadius D) (ellipseUpperCount D (euclidRadius D))
    hDpos hS100 h25 h26 hrho hrlt hcard hnpos hn hbound

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.euclid_radius_guards_252
#print axioms TenthDiscriminant.FirstCertificate.Tuned.euclid_normalized_upper_252
