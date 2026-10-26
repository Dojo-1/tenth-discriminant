import TenthDiscriminant.LatticeEllipse
import Mathlib.MeasureTheory.Measure.Lebesgue.Complex
import Mathlib.MeasureTheory.Measure.Lebesgue.VolumeOfBalls

/-!
# Geometric cells for Ender's ellipse

The cells are closed rectangles in the complex plane. Their boundaries
may overlap; finite-union subadditivity, rather than disjointness, is
enough for the disk-area lower count.
-/

namespace TenthDiscriminant

open MeasureTheory

noncomputable section

/-- The width-one, height-`sqrt D` cell centered at the lattice pair. -/
def ellipseCell (D : Nat) (p : Int × Int) : Set Complex :=
  Complex.measurableEquivRealProd ⁻¹'
    (Set.Icc ((p.1 : Real) - 1 / 2) ((p.1 : Real) + 1 / 2) ×ˢ
      Set.Icc (Real.sqrt D * ((p.2 : Real) - 1 / 2))
        (Real.sqrt D * ((p.2 : Real) + 1 / 2)))

theorem mem_ellipseCell_iff (D : Nat) (p : Int × Int) (z : Complex) :
    z ∈ ellipseCell D p ↔
      (p.1 : Real) - 1 / 2 ≤ z.re ∧ z.re ≤ (p.1 : Real) + 1 / 2 ∧
      Real.sqrt D * ((p.2 : Real) - 1 / 2) ≤ z.im ∧
      z.im ≤ Real.sqrt D * ((p.2 : Real) + 1 / 2) := by
  simp only [ellipseCell, Set.mem_preimage,
    Complex.measurableEquivRealProd_apply, Set.mem_prod, Set.mem_Icc]
  tauto

/-- The exact area of each cell; boundary overlaps do not matter. -/
theorem volume_ellipseCell (D : Nat) (p : Int × Int) :
    volume (ellipseCell D p) = ENNReal.ofReal (Real.sqrt D) := by
  rw [ellipseCell,
    Complex.volume_preserving_equiv_real_prod.measure_preimage
      (MeasurableSet.prod measurableSet_Icc measurableSet_Icc).nullMeasurableSet,
    Measure.volume_eq_prod, Measure.prod_prod, Real.volume_Icc, Real.volume_Icc]
  have hfirst : ((p.1 : Real) + 1 / 2) - ((p.1 : Real) - 1 / 2) = 1 := by ring
  have hsecond : Real.sqrt D * ((p.2 : Real) + 1 / 2) -
      Real.sqrt D * ((p.2 : Real) - 1 / 2) = Real.sqrt D := by ring
  rw [hfirst, hsecond]
  simp

/-- Every real coordinate has an integer center at distance at most one half. -/
private theorem exists_half_integer_center (t : Real) :
    ∃ n : Int, (n : Real) - 1 / 2 ≤ t ∧ t ≤ (n : Real) + 1 / 2 := by
  let n : Int := ⌊t + 1 / 2⌋
  have hlo : (n : Real) ≤ t + 1 / 2 := Int.floor_le _
  have hhi : t + 1 / 2 < (n : Real) + 1 := Int.lt_floor_add_one _
  exact ⟨n, by linarith, by linarith⟩

/-- The cells cover every complex point, including ties on their boundaries. -/
theorem exists_mem_ellipseCell (D : Nat) (hD : 0 < D) (z : Complex) :
    ∃ p : Int × Int, z ∈ ellipseCell D p := by
  let s : Real := Real.sqrt D
  have hs : 0 < s := Real.sqrt_pos.2 (by exact_mod_cast hD)
  obtain ⟨x, hxlo, hxhi⟩ := exists_half_integer_center z.re
  obtain ⟨y, hylo, hyhi⟩ := exists_half_integer_center (z.im / s)
  refine ⟨(x, y), (mem_ellipseCell_iff D (x, y) z).2 ⟨hxlo, hxhi, ?_, ?_⟩⟩
  · have h := mul_le_mul_of_nonneg_left hylo hs.le
    dsimp [s] at *
    convert h using 1; field_simp
  · have h := mul_le_mul_of_nonneg_left hyhi hs.le
    dsimp [s] at *
    convert h using 1; field_simp

/-- A cell point is within the half-width plus half-height of its center. -/
theorem norm_sub_latticePoint_le_cell_radius (D : Nat) (p : Int × Int)
    (z : Complex) (hz : z ∈ ellipseCell D p) :
    ‖z - latticePoint (D : Real) p.1 p.2‖ ≤ (1 + Real.sqrt D) / 2 := by
  obtain ⟨hxlo, hxhi, hylo, hyhi⟩ := (mem_ellipseCell_iff D p z).1 hz
  have hre : |z.re - (p.1 : Real)| ≤ 1 / 2 :=
    abs_le.mpr ⟨by linarith, by linarith⟩
  have hs : 0 ≤ Real.sqrt D := Real.sqrt_nonneg _
  have him : |z.im - (p.2 : Real) * Real.sqrt D| ≤ Real.sqrt D / 2 :=
    abs_le.mpr ⟨by nlinarith [hylo], by nlinarith [hyhi]⟩
  have hnorm := Complex.norm_le_abs_re_add_abs_im
    (z - latticePoint (D : Real) p.1 p.2)
  have hre' : (z - latticePoint (D : Real) p.1 p.2).re = z.re - (p.1 : Real) := by
    simp [latticePoint]
  have him' : (z - latticePoint (D : Real) p.1 p.2).im =
      z.im - (p.2 : Real) * Real.sqrt D := by simp [latticePoint]
  rw [hre', him'] at hnorm
  linarith

/-- Every point in the smaller disk lies in a cell whose center is in the
existing finite ellipse. This includes points on the disk boundary. -/
theorem closedBall_subset_ellipseCells (D rho : Nat) (hD : 0 < D) :
    Metric.closedBall (0 : Complex)
        ((rho : Real) - (1 + Real.sqrt D) / 2) ⊆
      ⋃ p ∈ ellipsePairs D rho, ellipseCell D p := by
  intro z hz
  obtain ⟨p, hp⟩ := exists_mem_ellipseCell D hD z
  have hz' : ‖z‖ ≤ (rho : Real) - (1 + Real.sqrt D) / 2 := by
    simpa only [Metric.mem_closedBall, dist_zero_right] using hz
  have hnear := norm_sub_latticePoint_le_cell_radius D p z hp
  have hcenter : ‖latticePoint (D : Real) p.1 p.2‖ ≤ (rho : Real) := by
    have htri : ‖latticePoint (D : Real) p.1 p.2‖ ≤
        ‖z‖ + ‖z - latticePoint (D : Real) p.1 p.2‖ := by
      calc
        ‖latticePoint (D : Real) p.1 p.2‖ =
            ‖z - (z - latticePoint (D : Real) p.1 p.2)‖ := by ring
        _ ≤ _ := norm_sub_le _ _
    linarith
  have hnormsq : Complex.normSq (latticePoint (D : Real) p.1 p.2) ≤
      (rho : Real) ^ 2 := by
    rw [Complex.normSq_eq_norm_sq]
    nlinarith [norm_nonneg (latticePoint (D : Real) p.1 p.2)]
  have hpairs : p ∈ ellipsePairs D rho := by
    apply (mem_ellipsePairs_iff D rho hD p.1 p.2).2
    rw [latticePoint_normSq (D : Real) (by positivity)] at hnormsq
    exact_mod_cast hnormsq
  exact Set.mem_iUnion.2 ⟨p, Set.mem_iUnion.2 ⟨hpairs, hp⟩⟩

/-- The missing geometric input for Ender's chosen-radius count. -/
theorem ellipsePairs_cell_area_bound (D rho : Nat) (hD : 0 < D)
    (hrho : (1 + Real.sqrt D) / 2 ≤ (rho : Real)) :
    Real.pi * ((rho : Real) - (1 + Real.sqrt D) / 2) ^ 2 ≤
      ((ellipsePairs D rho).card : Real) * Real.sqrt D := by
  let t : Real := (rho : Real) - (1 + Real.sqrt D) / 2
  have ht : 0 ≤ t := by dsimp [t]; linarith
  have hcover := closedBall_subset_ellipseCells D rho hD
  have hmeasure : volume (Metric.closedBall (0 : Complex) t) ≤
      ∑ p ∈ ellipsePairs D rho, volume (ellipseCell D p) := by
    exact (measure_mono hcover).trans
      (measure_biUnion_finset_le (ellipsePairs D rho) (ellipseCell D))
  have hs : 0 ≤ Real.sqrt D := Real.sqrt_nonneg _
  have hsum : (∑ p ∈ ellipsePairs D rho, volume (ellipseCell D p)).toReal =
      ((ellipsePairs D rho).card : Real) * Real.sqrt D := by
    simp [volume_ellipseCell, ENNReal.toReal_mul, ENNReal.toReal_ofReal hs,
      nsmul_eq_mul]
  have hfinite : (∑ p ∈ ellipsePairs D rho, volume (ellipseCell D p)) ≠ ⊤ := by
    simp [volume_ellipseCell, ENNReal.mul_ne_top]
  have hdisk : (volume (Metric.closedBall (0 : Complex) t)).toReal =
      Real.pi * t ^ 2 := by
    rw [Complex.volume_closedBall, ENNReal.toReal_mul,
      ENNReal.toReal_pow, ENNReal.toReal_ofReal ht]
    simp only [ENNReal.coe_toReal, NNReal.coe_real_pi]
    ring
  have hreal := ENNReal.toReal_mono hfinite hmeasure
  rw [hdisk, hsum] at hreal
  exact hreal

/-- Ender's unchanged radius alone gives the strict point count. -/
theorem ellipsePairs_card_gt_of_ender_radius
    (D rho q : Nat) (hD : 0 < D) (hq : 0 < q)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt ((q : Real) * Real.sqrt D / Real.pi) +
        10 * Real.sqrt D ≤ (rho : Real)) :
    q < (ellipsePairs D rho).card := by
  have hsone : 1 ≤ Real.sqrt D := by
    have hDreal : (1 : Real) ≤ D := by exact_mod_cast hD
    nlinarith [Real.sq_sqrt (by positivity : (0 : Real) ≤ D),
      Real.sqrt_nonneg (D : Real)]
  have hrho : (1 + Real.sqrt D) / 2 ≤ (rho : Real) := by
    have hbeta := Real.sqrt_nonneg ((q : Real) * Real.sqrt D / Real.pi)
    nlinarith
  exact ellipsePairs_card_gt_of_ender_radius_and_area D rho q hD hq
    hradius (ellipsePairs_cell_area_bound D rho hD hrho)

/-- The chosen radius at an interval's upper endpoint gives positivity
and Hadamard for the original trace-Gram matrix at every lower `D`. -/
theorem ellipseTraceGram_det_bounds_of_ender_radius
    (D D₂ rho R S : Nat) (hD : 0 < D) (hD₂ : D ≤ D₂)
    (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    0 < (rectangularTraceGram (ellipsePoints D rho) S R S).det ∧
      (rectangularTraceGram (ellipsePoints D rho) S R S).det ≤
        Finset.univ.prod (fun i => rectangularTraceGram (ellipsePoints D rho) S R S i i) := by
  have hD₂pos : 0 < D₂ := lt_of_lt_of_le hD hD₂
  have hq : 0 < 3 * R + S := by omega
  have hcard := ellipsePairs_card_gt_of_ender_radius D₂ rho (3 * R + S)
    hD₂pos hq hradius
  exact ellipseTraceGram_det_bounds_of_ender_guard
    D D₂ rho R S hD hD₂ hR hS hcard

/-- At `D=rho=1`, the smaller disk has radius zero; the endpoint is legal. -/
theorem ellipse_cell_area_endpoint_control :
    Real.pi * ((1 : Real) - (1 + Real.sqrt 1) / 2) ^ 2 ≤
      ((ellipsePairs 1 1).card : Real) * Real.sqrt 1 := by
  norm_num

/-- A negative boundary coordinate remains in the actual finite ellipse. -/
theorem ellipse_cell_negative_boundary_control :
    ((-1 : Int), (0 : Int)) ∈ ellipsePairs 1 1 := by decide

/-- Omitting `rho ≥ delta` is false: at radius zero, squaring the negative
disk radius produces an invalid positive lower bound. -/
theorem ellipse_cell_area_without_radius_guard_false :
    ¬ Real.pi * ((0 : Real) - (1 + Real.sqrt 1) / 2) ^ 2 ≤
      ((ellipsePairs 1 0).card : Real) * Real.sqrt 1 := by
  have hcard : (ellipsePairs 1 0).card = 1 := by decide
  norm_num [hcard]
  linarith [Real.pi_gt_three]

end
end TenthDiscriminant
