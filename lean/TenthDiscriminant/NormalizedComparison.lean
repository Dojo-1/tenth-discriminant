import TenthDiscriminant.UniformPrimeMassCertified

/-! Normalize both sides of the same production comparison by R^2*S.
This does not discharge geometric guards or an all-D analytic envelope. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

def comparisonScale (R S : Nat) : Real := (R : Real)^2 * S

theorem comparisonScale_pos (R S : Nat) (hR : 0 < R) (hS : 0 < S) :
    0 < comparisonScale R S := by
  unfold comparisonScale
  positivity

/-- Exact cancellation of the radius logarithm in the derivative correction.
The last term is an endpoint correction, not an asymptotic error to discard. -/
theorem upperB_normalized (R S rho : Nat) (n : Real)
    (hR : 0 < R) (hS : 1 ≤ S) (hrho : 0 < rho) :
    enderUpperB R S S rho n / comparisonScale R S =
      Real.log (2*n*S) / R + (1-(S : Real)/R)*Real.log rho +
      2*((S : Real)-1)/R*(Real.log R-1) +
      2*((S : Real)-1)/(R : Real)^2*(rho+Real.log ((R : Real)/rho)) := by
  have hr : (R : Real) ≠ 0 := by exact_mod_cast hR.ne'
  have hs : (S : Real) ≠ 0 := by exact_mod_cast (by omega : S ≠ 0)
  have hp : (rho : Real) ≠ 0 := by exact_mod_cast hrho.ne'
  unfold enderUpperB comparisonScale
  rw [Nat.cast_sub hS]
  simp only [Nat.cast_one]
  rw [Real.log_div hr hp]
  field_simp
  ring

/-- Removing clipping weakens the lower bound, irrespective of signs. -/
def rawPrimeMassLower (R S : Nat) (I : Real) : Real :=
  2*((S : Real)-1/2)*factorialLower R -
    2*((S : Real)-1/2)*triangularMass R*
      (factorialConstantUpper+I-linearConstantLower) -
    2*((S : Real)-1/2)*R*errorConstantUpper -
    squareMass R*(squareConstantUpper+I)

theorem rawPrimeMassLower_le_certified (R S : Nat) (I : Real) :
    rawPrimeMassLower R S I ≤ certifiedPrimeMassLower R S I := by
  have hs := le_max_left (certifiedSmallOddLower R S) (0 : Real)
  have ht := le_max_left (((S : Real)-1/2)*
    (factorialLower R-certifiedFactorialUpper R-triangularMass R*I)-squareMass R*I/2) (0 : Real)
  unfold certifiedPrimeMassLower
  unfold rawPrimeMassLower
  unfold certifiedSmallOddLower certifiedFactorialUpper at *
  nlinarith only [hs, ht]

/-- The full normalized algebraic lower expression; no floors are replaced
by real predecessors without the explicit R>=2 guard. -/
theorem rawPrimeMassLower_normalized (R S : Nat) (I : Real)
    (hR : 2 ≤ R) (hS : 0 < S) :
    rawPrimeMassLower R S I / comparisonScale R S =
      (1-1/(2*(S : Real)))*
        ((1-1/(R : Real))^2*(Real.log ((R : Real)-1)-3/2)+
          ((R : Real)-1/2)/(R : Real)^2) -
      (1-1/(2*(S : Real)))*(1-1/(R : Real))*
        (factorialConstantUpper+I-linearConstantLower) -
      2*(1-1/(2*(S : Real)))*errorConstantUpper/R -
      ((R : Real)-1)*(2*(R : Real)-1)/(6*(R : Real)*S)*
        (squareConstantUpper+I) := by
  have hr : (R : Real) ≠ 0 := by exact_mod_cast (by omega : R ≠ 0)
  have hs : (S : Real) ≠ 0 := by exact_mod_cast hS.ne'
  unfold rawPrimeMassLower comparisonScale factorialLower triangularMass squareMass
  rw [Nat.cast_sub (by omega : 1 ≤ R)]
  simp only [Nat.cast_one]
  field_simp
  ring

/-- The candidate affine envelopes really do separate at log D>=27.
This is a scalar lemma, not evidence that D satisfies those envelopes. -/
theorem affine_envelopes_separated (u : Real) (hu : 27 ≤ u) :
    (13/16 : Real)*u-1593/2000 < (999997/1000000 : Real)*u-5845/1000 := by
  linarith

/-- Once both envelopes and the original guards have been proved, the
comparison excludes the actual class number, with no extra analytic input. -/
theorem classNumber_ne_one_of_normalized_envelopes
    (D₁ D D₂ rho R S Y : Nat)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hRS : R ≤ 10000*S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hRcut : (R : Int) < ((D : Int)+1)/4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001/1000 : Real)*
      Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D₂/Real.pi)+
      10*Real.sqrt D₂ ≤ (rho : Real))
    (hlog : 27 ≤ Real.log D)
    (hupper : enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y)/
      comparisonScale R S ≤ (13/16 : Real)*Real.log D-1593/2000)
    (hlower : (999997/1000000 : Real)*Real.log D-5845/1000 ≤
      rawPrimeMassLower R S FirstEnderInterval.tailBudget/comparisonScale R S) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  apply classNumber_ne_one_of_certified_budget_comparison D₁ D D₂ rho R S Y
    hD₁ hDlo hDhi hR hS hRS hDsq hRcut hRrho hY hradius
  have ht := comparisonScale_pos R S (by omega) (by omega)
  have hgap := lt_of_le_of_lt hupper (affine_envelopes_separated _ hlog)
  have hraw : enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) <
      rawPrimeMassLower R S FirstEnderInterval.tailBudget :=
    (div_lt_div_iff_of_pos_right ht).mp (lt_of_lt_of_le hgap hlower)
  exact hraw.trans_le (rawPrimeMassLower_le_certified R S _)

theorem zero_comparisonScale_control (S : Nat) : comparisonScale 0 S = 0 := by
  simp [comparisonScale]

theorem zero_comparisonScale_not_positive (S : Nat) : ¬ 0 < comparisonScale 0 S := by
  simp [comparisonScale]

theorem smaller_log_threshold_rejected :
    ¬ (13/16 : Real)*26-1593/2000 < (999997/1000000 : Real)*26-5845/1000 := by
  norm_num

/-- The endpoint term cannot be dropped even when the integral is zero. -/
theorem positive_endpoint_correction_control :
    0 < (2 : Real)*(2-1)/(2 : Real)^2*(1+Real.log (2/1)) := by
  have h := Real.log_nonneg (by norm_num : (1 : Real) ≤ 2/1)
  nlinarith

theorem omitted_normalized_correction_rejected :
    ¬ enderUpperB 2 2 2 1 1 / comparisonScale 2 2 =
      Real.log (2*(1 : Real)*2)/2+(1-(2 : Real)/2)*Real.log 1+
        2*((2 : Real)-1)/2*(Real.log 2-1) := by
  rw [upperB_normalized 2 2 1 1 (by decide) (by decide) (by decide)]
  norm_num only [Nat.cast_ofNat, Nat.cast_one]
  linarith [positive_endpoint_correction_control]

end
end TenthDiscriminant.FirstCertificate
