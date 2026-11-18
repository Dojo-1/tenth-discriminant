import TenthDiscriminant.E16Integrated300
import TenthDiscriminant.NormalizedComparison

/-!
# E17a — Exact normalized original Ender upper and a guard-based envelope

The theorem is a real algebraic consequence of the EXACT source
enderUpperB formula, with every guard named. It does not assume
the eight guards hold for all D>=300^4, and it does not change Q,
the integer Gram, the original ordinary-Z derivative, or the prime
divisor. The next proof task is the uniform guard derivation.
-/
namespace TenthDiscriminant.E17
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem enderUpperB_expanded (R S rho : Nat) (n : Real)
    (hR : 0 < R) (hS : 1 ≤ S) (hrho : 0 < rho) :
    enderUpperB R S S rho n / comparisonScale R S =
      Real.log (2*n*S) / R +
      (1 + (S : Real)/(R : Real) - 2/(R : Real))*Real.log rho +
      2*((S : Real)-1)/(R : Real) *
        (Real.log ((R : Real)/rho) -1 +
          (rho : Real)/(R : Real) +
          Real.log ((R : Real)/rho)/(R : Real)) := by
  have h := upperB_normalized R S rho n hR hS hrho
  rw [h]
  have hRr : (R : Real) ≠ 0 := by exact_mod_cast hR.ne'
  have hRho : (rho : Real) ≠ 0 := by exact_mod_cast hrho.ne'
  rw [Real.log_div hRr hRho]
  field_simp
  ring

/-- The eight scalar guards are explicit hypotheses. Every coefficient
bound is inferred with its sign condition; there is no reverse
inequality or appeal to sampled numerical values. -/
theorem enderUpperB_affine_from_guards
    (D R S rho : Nat) (n : Real)
    (hR : 100000000 ≤ R) (hS : 1 ≤ S) (hrho : 0 < rho)
    (hSr : (S : Real)/(R : Real) ≤ 1/25)
    (hlogrho0 : 0 ≤ Real.log (rho : Real))
    (hlogrho : Real.log (rho : Real) ≤
      (3/4 : Real)*Real.log (D : Real) - 22/25)
    (hlogratio1 : 1 ≤ Real.log ((R : Real)/(rho : Real)))
    (hlogratio : Real.log ((R : Real)/(rho : Real)) ≤
      (1/4 : Real)*Real.log (D : Real) - 31/81)
    (hratio : (rho : Real)/(R : Real) ≤ 1/100)
    (hlogratioR : Real.log ((R : Real)/(rho : Real))/
      (R : Real) ≤ 1/9000)
    (hlogn : Real.log (2*n*S)/(R : Real) ≤ 1/4000) :
    enderUpperB R S S rho n / comparisonScale R S - 23/2000 ≤
      (4/5 : Real)*Real.log (D : Real) - 8393693/8100000 := by
  have hr : (0 : Real) < R := by
    exact_mod_cast (show 0 < R by omega)
  have hs : (1 : Real) ≤ S := by exact_mod_cast hS
  let A : Real := 1+(S : Real)/R-2/R
  let B : Real := 2*((S : Real)-1)/R
  let C : Real := Real.log ((R : Real)/rho)-1+
    (rho : Real)/R+Real.log ((R : Real)/rho)/R
  have hA : A ≤ 26/25 := by
    dsimp [A]
    have ht : (0 : Real) ≤ 2/(R : Real) := by positivity
    linarith only [hSr, ht]
  have hB : B ≤ 2/25 := by
    dsimp [B]
    have hSr' : (S : Real) ≤ (1/25 : Real)*(R : Real) :=
      (div_le_iff₀ hr).mp hSr
    apply (div_le_iff₀ hr).2
    linarith only [hSr']
  have hC0 : 0 ≤ C := by
    dsimp [C]
    have hρ : (0 : Real) ≤ (rho : Real)/R := by positivity
    have hlogr : 0 ≤ Real.log ((R : Real)/(rho : Real))/R := by
      positivity
    linarith only [hlogratio1,hρ,hlogr]
  have hC :
      C ≤ (1/4 : Real)*Real.log (D : Real)-31/81-1+
        1/100+1/9000 := by
    dsimp [C]
    linarith only [hlogratio,hratio,hlogratioR]
  have hAlog : A*Real.log (rho : Real) ≤
      (26/25 : Real)*Real.log rho :=
    mul_le_mul_of_nonneg_right hA hlogrho0
  have hAlog' :
      (26/25 : Real)*Real.log rho ≤
      (26/25 : Real)*((3/4 : Real)*Real.log (D : Real)-22/25) :=
    mul_le_mul_of_nonneg_left hlogrho (by norm_num)
  have hBC : B*C ≤ (2/25 : Real)*C :=
    mul_le_mul_of_nonneg_right hB hC0
  have hBC' :
      (2/25 : Real)*C ≤
      (2/25 : Real)*((1/4 : Real)*Real.log (D : Real)-
        31/81-1+1/100+1/9000) :=
    mul_le_mul_of_nonneg_left hC (by norm_num)
  have heq :
      enderUpperB R S S rho n / comparisonScale R S-23/2000 =
        Real.log (2*n*S)/R + A*Real.log rho + B*C - 23/2000 := by
    rw [enderUpperB_expanded R S rho n (by omega) hS hrho]
  calc
    _ = Real.log (2*n*S)/R + A*Real.log rho+B*C-23/2000 := heq
    _ ≤ 1/4000 + (26/25 : Real)*
          ((3/4 : Real)*Real.log (D : Real)-22/25) +
          (2/25 : Real)*((1/4 : Real)*Real.log (D : Real)-
              31/81-1+1/100+1/9000)-23/2000 := by
            linarith only [hlogn,hAlog,hAlog',hBC,hBC']
    _ = (4/5 : Real)*Real.log (D : Real)-8393693/8100000 := by ring

/-- The conservative affine majorant has an exact strictly positive
margin, rather than a decimal-fitted threshold. -/
theorem enderUpperB_affine_margin (u : Real) :
    (4/5 : Real)*u-8393693/8100000 <
      (4/5 : Real)*u-103/100 := by
  linarith

end
end TenthDiscriminant.E17

#print axioms TenthDiscriminant.E17.enderUpperB_expanded
#print axioms TenthDiscriminant.E17.enderUpperB_affine_from_guards
#print axioms TenthDiscriminant.E17.enderUpperB_affine_margin
