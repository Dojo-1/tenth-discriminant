import TenthDiscriminant.EnderUpperB

/-!
# An upper count by disjoint inward cells

Each lattice point off both axes owns an open unit rectangle inward toward
the axes. Its physical area is `sqrt D`; the rectangles are disjoint and
remain in the same disk. Axis points supply the explicit boundary terms.
-/

namespace TenthDiscriminant
open MeasureTheory
set_option autoImplicit false
noncomputable section

def inwardLower (x : Int) : Real := if 0 < x then (x : Real) - 1 else x
def inwardUpper (x : Int) : Real := if 0 < x then x else (x : Real) + 1

theorem inward_width (x : Int) : inwardUpper x - inwardLower x = 1 := by
  unfold inwardUpper inwardLower
  split_ifs <;> ring

theorem inward_coordinate_sq_le (x : Int) (hx : x ≠ 0) (t : Real)
    (ht : inwardLower x < t ∧ t < inwardUpper x) : t ^ 2 ≤ (x : Real) ^ 2 := by
  by_cases hpos : 0 < x
  · have hxone : (1 : Real) ≤ x := by exact_mod_cast (by omega : (1 : Int) ≤ x)
    simp only [inwardLower, inwardUpper, if_pos hpos] at ht
    exact pow_le_pow_left₀ (by linarith) ht.2.le 2
  · have hxneg : (x : Real) ≤ -1 := by exact_mod_cast (by omega : x ≤ -1)
    simp only [inwardLower, inwardUpper, if_neg hpos] at ht
    have h := pow_le_pow_left₀ (by linarith : 0 ≤ -t)
      (by linarith : -t ≤ -(x : Real)) 2
    simpa only [neg_sq] using h

theorem inward_coordinate_unique (x y : Int) (hx : x ≠ 0) (hy : y ≠ 0)
    (t : Real) (htx : inwardLower x < t ∧ t < inwardUpper x)
    (hty : inwardLower y < t ∧ t < inwardUpper y) : x = y := by
  by_cases hxpos : 0 < x <;> by_cases hypos : 0 < y
  · simp only [inwardLower, inwardUpper, if_pos hxpos, if_pos hypos] at htx hty
    have hxy : x < y + 1 := by exact_mod_cast (by linarith : (x : Real) < y + 1)
    have hyx : y < x + 1 := by exact_mod_cast (by linarith : (y : Real) < x + 1)
    omega
  · have hxone : (1 : Real) ≤ x := by exact_mod_cast (by omega : (1 : Int) ≤ x)
    have hyneg : (y : Real) ≤ -1 := by exact_mod_cast (by omega : y ≤ -1)
    simp only [inwardLower, inwardUpper, if_pos hxpos, if_neg hypos] at htx hty
    linarith
  · have hyone : (1 : Real) ≤ y := by exact_mod_cast (by omega : (1 : Int) ≤ y)
    have hxneg : (x : Real) ≤ -1 := by exact_mod_cast (by omega : x ≤ -1)
    simp only [inwardLower, inwardUpper, if_neg hxpos, if_pos hypos] at htx hty
    linarith
  · simp only [inwardLower, inwardUpper, if_neg hxpos, if_neg hypos] at htx hty
    have hxy : x < y + 1 := by exact_mod_cast (by linarith : (x : Real) < y + 1)
    have hyx : y < x + 1 := by exact_mod_cast (by linarith : (y : Real) < x + 1)
    omega

def inwardCell (D : Nat) (p : Int × Int) : Set Complex :=
  Complex.measurableEquivRealProd ⁻¹'
    (Set.Ioo (inwardLower p.1) (inwardUpper p.1) ×ˢ
      Set.Ioo (Real.sqrt D * inwardLower p.2) (Real.sqrt D * inwardUpper p.2))

theorem measurableSet_inwardCell (D : Nat) (p : Int × Int) :
    MeasurableSet (inwardCell D p) :=
  (measurableSet_Ioo.prod measurableSet_Ioo).preimage
    Complex.measurableEquivRealProd.measurable

theorem mem_inwardCell_iff (D : Nat) (p : Int × Int) (z : Complex) :
    z ∈ inwardCell D p ↔
      inwardLower p.1 < z.re ∧ z.re < inwardUpper p.1 ∧
      Real.sqrt D * inwardLower p.2 < z.im ∧
        z.im < Real.sqrt D * inwardUpper p.2 := by
  simp only [inwardCell, Set.mem_preimage,
    Complex.measurableEquivRealProd_apply, Set.mem_prod, Set.mem_Ioo]
  tauto

theorem volume_inwardCell (D : Nat) (p : Int × Int) :
    volume (inwardCell D p) = ENNReal.ofReal (Real.sqrt D) := by
  rw [inwardCell,
    Complex.volume_preserving_equiv_real_prod.measure_preimage
      (MeasurableSet.prod measurableSet_Ioo measurableSet_Ioo).nullMeasurableSet,
    Measure.volume_eq_prod, Measure.prod_prod, Real.volume_Ioo, Real.volume_Ioo]
  have hy : Real.sqrt D * inwardUpper p.2 - Real.sqrt D * inwardLower p.2 =
      Real.sqrt D := by rw [← mul_sub, inward_width, mul_one]
  rw [inward_width, hy]
  simp

theorem inwardCell_im_bounds (D : Nat) (hD : 0 < D)
    (p : Int × Int) (z : Complex) (hz : z ∈ inwardCell D p) :
    inwardLower p.2 < z.im / Real.sqrt D ∧
      z.im / Real.sqrt D < inwardUpper p.2 := by
  have hs : 0 < Real.sqrt (D : Real) := Real.sqrt_pos.2 (by exact_mod_cast hD)
  have hb := (mem_inwardCell_iff D p z).mp hz
  constructor
  · apply (lt_div_iff₀ hs).2
    simpa only [mul_comm] using hb.2.2.1
  · apply (div_lt_iff₀ hs).2
    simpa only [mul_comm] using hb.2.2.2

theorem inwardCell_subset_closedBall (D rho : Nat) (hD : 0 < D)
    (p : Int × Int) (hp : p ∈ ellipsePairs D rho)
    (hx : p.1 ≠ 0) (hy : p.2 ≠ 0) :
    inwardCell D p ⊆ Metric.closedBall (0 : Complex) (rho : Real) := by
  intro z hz
  have hb := (mem_inwardCell_iff D p z).mp hz
  have hre := inward_coordinate_sq_le p.1 hx z.re ⟨hb.1, hb.2.1⟩
  have him := inward_coordinate_sq_le p.2 hy (z.im / Real.sqrt D)
    (inwardCell_im_bounds D hD p z hz)
  have hs : 0 < Real.sqrt (D : Real) := Real.sqrt_pos.2 (by exact_mod_cast hD)
  have hcancel : Real.sqrt D * (z.im / Real.sqrt D) = z.im := by field_simp
  have himsq : z.im ^ 2 ≤ (D : Real) * (p.2 : Real) ^ 2 := by
    calc
      z.im ^ 2 = (Real.sqrt D * (z.im / Real.sqrt D)) ^ 2 := by rw [hcancel]
      _ = (Real.sqrt D) ^ 2 * (z.im / Real.sqrt D) ^ 2 := by rw [mul_pow]
      _ ≤ (Real.sqrt D) ^ 2 * (p.2 : Real) ^ 2 :=
        mul_le_mul_of_nonneg_left him (sq_nonneg _)
      _ = _ := by rw [Real.sq_sqrt (by positivity : (0 : Real) ≤ D)]
  have hpNorm : (p.1 : Real) ^ 2 + (D : Real) * (p.2 : Real) ^ 2 ≤
      (rho : Real) ^ 2 := by
    exact_mod_cast (mem_ellipsePairs_iff D rho hD p.1 p.2).mp hp
  have hnorm : ‖z‖ ^ 2 ≤ (rho : Real) ^ 2 := by
    rw [Complex.sq_norm, Complex.normSq_apply]
    nlinarith
  rw [Metric.mem_closedBall, dist_zero_right]
  have hρ : (0 : Real) ≤ rho := Nat.cast_nonneg _
  nlinarith [norm_nonneg z]

theorem inwardCell_disjoint (D : Nat) (hD : 0 < D)
    (p q : Int × Int) (hx : p.1 ≠ 0) (hy : p.2 ≠ 0)
    (hqx : q.1 ≠ 0) (hqy : q.2 ≠ 0) (hpq : p ≠ q) :
    Disjoint (inwardCell D p) (inwardCell D q) := by
  apply Set.disjoint_left.2
  intro z hzp hzq
  have hp := (mem_inwardCell_iff D p z).mp hzp
  have hq := (mem_inwardCell_iff D q z).mp hzq
  have hxx := inward_coordinate_unique p.1 q.1 hx hqx z.re
    ⟨hp.1, hp.2.1⟩ ⟨hq.1, hq.2.1⟩
  have hyy := inward_coordinate_unique p.2 q.2 hy hqy (z.im / Real.sqrt D)
    (inwardCell_im_bounds D hD p z hzp) (inwardCell_im_bounds D hD q z hzq)
  exact hpq (Prod.ext hxx hyy)

def ellipseOffAxisPairs (D rho : Nat) : Finset (Int × Int) :=
  (ellipsePairs D rho).filter (fun p => p.1 ≠ 0 ∧ p.2 ≠ 0)

/-- Every off-axis point owns area `sqrt D` inside the same disk. -/
theorem ellipseOffAxis_card_area_bound (D rho : Nat) (hD : 0 < D) :
    ((ellipseOffAxisPairs D rho).card : Real) * Real.sqrt D ≤
      Real.pi * (rho : Real) ^ 2 := by
  let Q := ellipseOffAxisPairs D rho
  have hdisj : (Q : Set (Int × Int)).PairwiseDisjoint (inwardCell D) := by
    intro p hp q hq hpq
    have hp' := (Finset.mem_filter.mp hp).2
    have hq' := (Finset.mem_filter.mp hq).2
    exact inwardCell_disjoint D hD p q hp'.1 hp'.2 hq'.1 hq'.2 hpq
  have hunion : volume (⋃ p ∈ Q, inwardCell D p) =
      ∑ p ∈ Q, volume (inwardCell D p) :=
    measure_biUnion_finset hdisj (fun p _ => measurableSet_inwardCell D p)
  have hsub : (⋃ p ∈ Q, inwardCell D p) ⊆
      Metric.closedBall (0 : Complex) (rho : Real) := by
    intro z hz
    obtain ⟨p, hp, hzp⟩ := Set.mem_iUnion₂.mp hz
    have h := Finset.mem_filter.mp hp
    exact inwardCell_subset_closedBall D rho hD p h.1 h.2.1 h.2.2 hzp
  have hm : volume (⋃ p ∈ Q, inwardCell D p) ≤
      volume (Metric.closedBall (0 : Complex) (rho : Real)) := measure_mono hsub
  rw [hunion] at hm
  have hs : 0 ≤ Real.sqrt (D : Real) := Real.sqrt_nonneg _
  have hsum : (∑ p ∈ Q, volume (inwardCell D p)).toReal =
      (Q.card : Real) * Real.sqrt D := by
    simp [volume_inwardCell, ENNReal.toReal_mul, ENNReal.toReal_ofReal hs,
      nsmul_eq_mul]
  have hfinite : volume (Metric.closedBall (0 : Complex) (rho : Real)) ≠ ⊤ := by
    simp [Complex.volume_closedBall, ENNReal.mul_ne_top]
  have hdisk : (volume (Metric.closedBall (0 : Complex) (rho : Real))).toReal =
      Real.pi * (rho : Real) ^ 2 := by
    rw [Complex.volume_closedBall, ENNReal.toReal_mul, ENNReal.toReal_pow,
      ENNReal.toReal_ofReal (Nat.cast_nonneg rho)]
    simp only [ENNReal.coe_toReal, NNReal.coe_real_pi]
    ring
  have hr := ENNReal.toReal_mono hfinite hm
  rw [hsum, hdisk] at hr
  exact hr

def ellipseVerticalBound (D rho : Nat) : Nat :=
  ⌊(rho : Real) / Real.sqrt D⌋₊

theorem ellipse_pair_y_bounds (D rho : Nat) (hD : 0 < D)
    (p : Int × Int) (hp : p ∈ ellipsePairs D rho) :
    -(ellipseVerticalBound D rho : Int) ≤ p.2 ∧
      p.2 ≤ (ellipseVerticalBound D rho : Int) := by
  let z := latticePoint (D : Real) p.1 p.2
  have hz : z ∈ ellipsePoints D rho := Finset.mem_image.mpr ⟨p, hp, rfl⟩
  have hn := (Complex.abs_im_le_norm z).trans (ellipsePoint_norm_le D rho hD z hz)
  have hs : 0 < Real.sqrt (D : Real) := Real.sqrt_pos.2 (by exact_mod_cast hD)
  have hy : |(p.2 : Real)| ≤ (rho : Real) / Real.sqrt D := by
    apply (le_div_iff₀ hs).2
    simpa only [z, latticePoint, Complex.add_im, Complex.ofReal_im,
      Complex.mul_im, Complex.ofReal_re, Complex.I_re, Complex.I_im,
      mul_zero, zero_mul, add_zero, zero_add, mul_one, abs_mul,
      abs_of_pos hs] using hn
  have hyNat : p.2.natAbs ≤ ellipseVerticalBound D rho := by
    apply (Nat.le_floor_iff (by positivity : (0 : Real) ≤ (rho : Real) / Real.sqrt D)).2
    simpa only [Int.cast_natAbs, Int.cast_abs] using hy
  have hyInt : (p.2.natAbs : Int) ≤ (ellipseVerticalBound D rho : Int) := by
    exact_mod_cast hyNat
  rw [Int.natCast_natAbs] at hyInt
  exact abs_le.mp hyInt

def horizontalAxisBox (rho : Nat) : Finset (Int × Int) :=
  ((Finset.Icc (-(rho : Int)) (rho : Int)).erase 0).product {0}

def verticalAxisBox (Y : Nat) : Finset (Int × Int) :=
  ({0} : Finset Int).product (Finset.Icc (-(Y : Int)) (Y : Int))

theorem integer_axis_interval_card (N : Nat) :
    (Finset.Icc (-(N : Int)) (N : Int)).card = 2 * N + 1 := by
  rw [Int.card_Icc]
  omega

theorem horizontalAxisBox_card (rho : Nat) : (horizontalAxisBox rho).card = 2 * rho := by
  have hzero : (0 : Int) ∈ Finset.Icc (-(rho : Int)) (rho : Int) := by simp
  simp only [horizontalAxisBox, Finset.product_eq_sprod, Finset.card_product, Finset.card_singleton,
    mul_one, Finset.card_erase_of_mem hzero, integer_axis_interval_card]
  omega

theorem verticalAxisBox_card (Y : Nat) : (verticalAxisBox Y).card = 2 * Y + 1 := by
  simp only [verticalAxisBox, Finset.product_eq_sprod, Finset.card_product, Finset.card_singleton,
    one_mul, integer_axis_interval_card]

/-- The origin belongs to the vertical axis; removing it from the
horizontal box avoids double counting the boundary correction. -/
theorem ellipsePairs_card_le_offAxis_add_axes (D rho : Nat) (hD : 0 < D) :
    (ellipsePairs D rho).card ≤ (ellipseOffAxisPairs D rho).card +
      2 * rho + (2 * ellipseVerticalBound D rho + 1) := by
  let Q := ellipseOffAxisPairs D rho
  let H := horizontalAxisBox rho
  let V := verticalAxisBox (ellipseVerticalBound D rho)
  have hsub : ellipsePairs D rho ⊆ (Q ∪ H) ∪ V := by
    intro p hp
    by_cases hx : p.1 = 0
    · apply Finset.mem_union.mpr
      right
      apply Finset.mem_product.mpr
      exact ⟨by simp [hx], Finset.mem_Icc.mpr (ellipse_pair_y_bounds D rho hD p hp)⟩
    · apply Finset.mem_union.mpr
      left
      by_cases hy : p.2 = 0
      · apply Finset.mem_union.mpr
        right
        apply Finset.mem_product.mpr
        have hbox := Finset.mem_product.mp (Finset.mem_filter.mp hp).1
        exact ⟨Finset.mem_erase.mpr ⟨hx, hbox.1⟩, by simp [hy]⟩
      · exact Finset.mem_union.mpr (Or.inl (Finset.mem_filter.mpr ⟨hp, hx, hy⟩))
  have hcard := Finset.card_le_card hsub
  have houter := Finset.card_union_le (Q ∪ H) V
  have hinner := Finset.card_union_le Q H
  have ht := hcard.trans (houter.trans (Nat.add_le_add_right hinner V.card))
  simpa only [H, V, Q, horizontalAxisBox_card, verticalAxisBox_card] using ht

def ellipseUpperCount (D rho : Nat) : Real :=
  Real.pi * (rho : Real) ^ 2 / Real.sqrt D + 2 * rho +
    ((2 * ellipseVerticalBound D rho + 1 : Nat) : Real)

/-- Ender's unchanged upper point count for the actual finite ellipse. -/
theorem ellipsePairs_card_le_upper_count (D rho : Nat) (hD : 0 < D) :
    ((ellipsePairs D rho).card : Real) ≤ ellipseUpperCount D rho := by
  have hs : 0 < Real.sqrt (D : Real) := Real.sqrt_pos.2 (by exact_mod_cast hD)
  have hoff := (le_div_iff₀ hs).2 (ellipseOffAxis_card_area_bound D rho hD)
  have haxes := ellipsePairs_card_le_offAxis_add_axes D rho hD
  have hreal : ((ellipsePairs D rho).card : Real) ≤
      ((ellipseOffAxisPairs D rho).card : Real) + 2 * rho +
        ((2 * ellipseVerticalBound D rho + 1 : Nat) : Real) := by exact_mod_cast haxes
  unfold ellipseUpperCount
  linarith

/-- The line count may be padded upward, as production does by flooring
an Arb upper endpoint. Its relation to the exact floor remains explicit. -/
def ellipsePaddedUpperCount (D rho Y : Nat) : Real :=
  Real.pi * (rho : Real) ^ 2 / Real.sqrt D + 2 * rho + ((2 * Y + 1 : Nat) : Real)

/-- A strict numerical upper bound below `Y+1` suffices for safe line-count
padding; equality with an externally rounded floor is unnecessary. -/
theorem ellipseVerticalBound_le_of_ratio_lt (D rho Y : Nat)
    (hY : (rho : Real) / Real.sqrt D < (Y : Real) + 1) :
    ellipseVerticalBound D rho ≤ Y := by
  apply Nat.le_of_lt_succ
  apply (Nat.floor_lt (by positivity : (0 : Real) ≤ (rho : Real) / Real.sqrt D)).2
  exact_mod_cast hY

theorem ellipsePairs_card_le_padded_upper_count (D₁ D rho Y : Nat)
    (hD₁ : 0 < D₁) (hD : D₁ ≤ D) (hY : ellipseVerticalBound D₁ rho ≤ Y) :
    ((ellipsePairs D rho).card : Real) ≤ ellipsePaddedUpperCount D₁ rho Y := by
  have hmon : ((ellipsePairs D rho).card : Real) ≤
      ((ellipsePairs D₁ rho).card : Real) := by
    exact_mod_cast ellipsePairs_card_antitone_D D₁ D rho hD
  have hpad : ellipseUpperCount D₁ rho ≤ ellipsePaddedUpperCount D₁ rho Y := by
    unfold ellipseUpperCount ellipsePaddedUpperCount
    apply add_le_add_left
    exact_mod_cast Nat.add_le_add_right (Nat.mul_le_mul_left 2 hY) 1
  exact hmon.trans ((ellipsePairs_card_le_upper_count D₁ rho hD₁).trans hpad)

/-- Both geometric counts are now supplied by the actual ellipse: the
upper endpoint gives positivity, the lower endpoint gives production's
upper count, and class number one supplies the finite local prime mass. -/
theorem ellipse_primeMass_log_le_counted_upperB
    (D₁ D D₂ rho R S Y : Nat)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 1 ≤ R) (hS : 1 ≤ S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    (∑ p ∈ oddPrimesBelow R,
      (2 * valuationWeight R S p : Nat) * Real.log (p : Real)) ≤
      enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) := by
  exact ellipse_primeMass_log_le_upperB D D₂ rho R S
    (ellipsePaddedUpperCount D₁ rho Y) (lt_of_lt_of_le hD₁ hDlo) hDhi hR hS
    hDsq hclass hRcut hRrho hradius
    (ellipsePairs_card_le_padded_upper_count D₁ D rho Y hD₁ hDlo hY)

theorem upper_count_zero_radius_control (D : Nat) :
    ((ellipsePairs D 0).card : Real) = ellipseUpperCount D 0 := by
  norm_num [ellipsePairs, ellipseUpperCount, ellipseVerticalBound,
    Finset.filter_singleton]

theorem upper_count_unit_control :
    (5 : Real) ≤ ellipseUpperCount 1 1 := by
  simpa only [ellipsePairs_unit_control] using
    ellipsePairs_card_le_upper_count 1 1 (by decide)

theorem upper_count_nineteen_five_control :
    (21 : Real) ≤ ellipseUpperCount 19 5 := by
  simpa only [ellipsePairs_nineteen_five_control] using
    ellipsePairs_card_le_upper_count 19 5 (by decide)

theorem inward_adjacent_cells_control :
    Disjoint (inwardCell 1 (1, 1)) (inwardCell 1 (2, 1)) :=
  inwardCell_disjoint 1 (by decide) (1, 1) (2, 1)
    (by decide) (by decide) (by decide) (by decide) (by decide)

theorem inward_negative_cell_control :
    (⟨-1 / 2, -1 / 2⟩ : Complex) ∈ inwardCell 1 (-1, -1) := by
  norm_num [mem_inwardCell_iff, inwardLower, inwardUpper]

theorem inward_integer_boundary_control :
    (⟨1, 1 / 2⟩ : Complex) ∉ inwardCell 1 (1, 1) ∧
      (⟨1, 1 / 2⟩ : Complex) ∉ inwardCell 1 (2, 1) := by
  norm_num [mem_inwardCell_iff, inwardLower, inwardUpper]

/-- Counting axis points as full inward cells would put area five in a
unit disk of area less than four. The off-axis restriction is essential. -/
theorem inward_all_points_area_false :
    ¬ ((ellipsePairs 1 1).card : Real) * Real.sqrt 1 ≤ Real.pi * (1 : Real) ^ 2 := by
  rw [ellipsePairs_unit_control]
  norm_num
  linarith [Real.pi_lt_four]

theorem upper_count_without_positive_D_false :
    ¬ ((ellipsePairs 0 1).card : Real) ≤ ellipseUpperCount 0 1 := by
  have hc : (ellipsePairs 0 1).card = 9 := by decide
  norm_num [hc, ellipseUpperCount, ellipseVerticalBound]

end
end TenthDiscriminant
