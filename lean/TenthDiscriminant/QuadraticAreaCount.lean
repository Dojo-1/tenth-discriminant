import TenthDiscriminant.QuadraticRowCount
import Mathlib.Analysis.SpecialFunctions.Integrals

/-! Homogeneous scaling evaluates the width integral without dividing by
the height. The zero-threshold case therefore belongs to the same proof. -/
open MeasureTheory
namespace TenthDiscriminant.QuadraticRows
set_option autoImplicit false
noncomputable section

theorem width_scaled (a D t : Real) (ha : 0 < a) (hD : 0 < D) (ht : 0 ≤ t) (u : Real) :
    width a D t (height a D t*u)=
      (Real.sqrt (4*a*t)/a)*Real.sqrt (1-u^2) := by
  have hC : 0 ≤ 4*a*t := by positivity
  have hCY : D*(height a D t)^2=4*a*t := by
    unfold height
    rw [Real.sq_sqrt (div_nonneg hC hD.le)]
    field_simp [ne_of_gt hD] <;> ring
  have he : 4*a*t-D*(height a D t*u)^2=4*a*t*(1-u^2) := by
    calc
      _ = 4*a*t-(D*(height a D t)^2)*u^2 := by ring
      _ = _ := by rw [hCY]; ring
  unfold width
  rw [he,Real.sqrt_mul hC]
  ring

theorem width_even (a D t s : Real) : width a D t (-s)=width a D t s := by
  simp [width]

theorem width_full_integral (a D t : Real) (ha : 0 < a) (hD : 0 < D) (ht : 0 ≤ t) :
    (∫ s in -height a D t..height a D t, width a D t s)=2*Real.pi*t/Real.sqrt D := by
  let Y := height a D t
  have hC : 0 ≤ 4*a*t := by positivity
  have hs : Y*(∫ u in (-1 : Real)..1, width a D t (Y*u))=
      ∫ s in -Y..Y, width a D t s := by
    simpa only [smul_eq_mul,mul_neg_one,mul_one] using
      (intervalIntegral.smul_integral_comp_mul_left (width a D t) Y (a:=(-1 : Real)) (b:=1))
  have hu : (∫ u in (-1 : Real)..1, width a D t (Y*u))=
      (Real.sqrt (4*a*t)/a)*(Real.pi/2) := by
    simp_rw [show Y=height a D t from rfl,width_scaled a D t ha hD ht]
    rw [intervalIntegral.integral_const_mul,integral_sqrt_one_sub_sq]
  have hp : Y*Real.sqrt (4*a*t)=(4*a*t)/Real.sqrt D := by
    dsimp [Y,height]
    rw [Real.sqrt_div hC,div_mul_eq_mul_div,Real.mul_self_sqrt hC]
  calc
    _ = Y*(∫ u in (-1 : Real)..1, width a D t (Y*u)) := hs.symm
    _ = Y*((Real.sqrt (4*a*t)/a)*(Real.pi/2)) := by rw [hu]
    _ = (Y*Real.sqrt (4*a*t))/a*(Real.pi/2) := by ring
    _ = ((4*a*t)/Real.sqrt D)/a*(Real.pi/2) := by rw [hp]
    _ = _ := by
      field_simp [ne_of_gt ha,ne_of_gt (Real.sqrt_pos.mpr hD)] <;> ring

theorem width_integral (a D t : Real) (ha : 0 < a) (hD : 0 < D) (ht : 0 ≤ t) :
    2*(∫ s in (0 : Real)..height a D t, width a D t s)=2*Real.pi*t/Real.sqrt D := by
  let Y := height a D t
  have hn : (∫ s in -Y..(0 : Real), width a D t s)=
      ∫ s in (0 : Real)..Y, width a D t s := by
    simpa only [neg_zero,width_even] using
      (intervalIntegral.integral_comp_neg (width a D t) (a:=(0 : Real)) (b:=Y)).symm
  have hc := width_continuous a D t
  have hadd : (∫ s in -Y..(0 : Real), width a D t s)+
      (∫ s in (0 : Real)..Y, width a D t s)=∫ s in -Y..Y, width a D t s :=
    intervalIntegral.integral_add_adjacent_intervals
      (hc.intervalIntegrable (-Y) 0) (hc.intervalIntegrable 0 Y)
  have hf := width_full_integral a D t ha hD ht
  change (∫ s in -Y..Y, width a D t s)=2*Real.pi*t/Real.sqrt D at hf
  linarith

theorem height_scale (a D t : Real) : height a D t=2*Real.sqrt (a*t/D) := by
  unfold height
  have he : 4*a*t/D=4*(a*t/D) := by ring
  rw [he,Real.sqrt_mul (by norm_num : (0 : Real) ≤ 4)]
  norm_num

theorem nonzeroBudget_eq (a D t : Real) (ha : 0 < a) (hD : 0 < D) (ht : 0 ≤ t) :
    nonzeroBudget a D t=2*Real.pi*t/Real.sqrt D+4*Real.sqrt (a*t/D) := by
  unfold nonzeroBudget
  rw [width_integral a D t ha hD ht,height_scale]
  ring

theorem off_axis_area_bound (U : Finset (Int × Int)) (a b c t : Real)
    (ha : 0 < a) (hD : 0 < 4*a*c-b^2) (ht : 0 ≤ t)
    (hQ : ∀ p ∈ U, quad a b c p ≤ t) (hy : ∀ p ∈ U, p.2 ≠ 0) :
    (U.card : Real) ≤ 2*Real.pi*t/Real.sqrt (4*a*c-b^2)+
      4*Real.sqrt (a*t/(4*a*c-b^2)) := by
  have hh := off_axis_count U a b c t ha hD ht hQ hy
  rwa [nonzeroBudget_eq a (4*a*c-b^2) t ha hD ht] at hh

theorem zero_threshold_control (a D : Real) (ha : 0 < a) (hD : 0 < D) :
    nonzeroBudget a D 0=0 := by
  rw [nonzeroBudget_eq a D 0 ha hD (le_refl 0)]
  norm_num

theorem circle_area_control : (2 : Real) ≤ Real.pi+2 := by
  have he : nonzeroBudget 1 4 1=Real.pi+2 := by
    rw [nonzeroBudget_eq 1 4 1 (by norm_num) (by norm_num) (by norm_num)]
    norm_num
  rw [← he]
  exact circle_control

theorem sheared_form_control :
    (quad 1 2 2 (-1,1)=1 ∧ quad 1 2 2 (1,-1)=1) ∧ (2 : Real) ≤ Real.pi+2 := by
  constructor
  · norm_num [quad]
  · let U : Finset (Int × Int) := {(-1,1),(1,-1)}
    have hQ : ∀ p ∈ U, quad 1 2 2 p ≤ 1 := by
      intro p hp
      simp only [U,Finset.mem_insert,Finset.mem_singleton] at hp
      rcases hp with rfl | rfl <;> norm_num [quad]
    have hy : ∀ p ∈ U, p.2 ≠ 0 := by
      intro p hp
      simp only [U,Finset.mem_insert,Finset.mem_singleton] at hp
      rcases hp with rfl | rfl <;> norm_num
    have hc := off_axis_area_bound U 1 2 2 1 (by norm_num) (by norm_num) (by norm_num) hQ hy
    convert hc using 1 <;> norm_num [U]

theorem zero_row_area_guard_control : quad 1 0 1 (0,0) ≤ 0 ∧
    ¬ (1 : Real) ≤ 2*Real.pi*0/Real.sqrt 4+4*Real.sqrt (1*0/4) := by
  norm_num [quad]

end
end TenthDiscriminant.QuadraticRows

#audit_namespace TenthDiscriminant.QuadraticRows
#print axioms TenthDiscriminant.QuadraticRows.off_axis_area_bound
