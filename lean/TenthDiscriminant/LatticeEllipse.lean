import TenthDiscriminant.Interpolation

/-!
# The integer ellipse as an input to interpolation

This module constructs the full finite ellipse used in the informal Ender
argument. The analytic estimate that its cardinality is large enough remains
a separate obligation.
-/
namespace TenthDiscriminant

/-- Integer pairs in the full ellipse of integer radius `rho`. -/
def ellipsePairs (D rho : Nat) : Finset (Int × Int) :=
  ((Finset.Icc (-(rho : Int)) (rho : Int)).product
    (Finset.Icc (-(rho : Int)) (rho : Int))).filter
      (fun p => p.1 ^ 2 + (D : Int) * p.2 ^ 2 ≤ (rho : Int) ^ 2)

/-- A boundary control: origin and the four unit-axis points are all retained. -/
theorem ellipsePairs_unit_control : (ellipsePairs 1 1).card = 5 := by decide

/-- A bounded exact control with a nontrivial vertical slice of the ellipse. -/
theorem ellipsePairs_nineteen_five_control : (ellipsePairs 19 5).card = 21 := by decide

noncomputable section

/-- The finite point set supplied to the unchanged trace-Gram matrix. -/
def ellipsePoints (D rho : Nat) : Finset Complex :=
  (ellipsePairs D rho).image (fun p => latticePoint (D : Real) p.1 p.2)

private theorem ellipse_coordinate_bounds (D rho : Nat) (hD : 0 < D)
    (x y : Int) (h : x ^ 2 + (D : Int) * y ^ 2 ≤ (rho : Int) ^ 2) :
    -(rho : Int) ≤ x ∧ x ≤ (rho : Int) ∧
      -(rho : Int) ≤ y ∧ y ≤ (rho : Int) := by
  have hD' : (1 : Int) ≤ D := by exact_mod_cast hD
  have hr : (0 : Int) ≤ rho := by exact_mod_cast Nat.zero_le rho
  have hy2 : (0 : Int) ≤ y ^ 2 := sq_nonneg y
  have hprod : 0 ≤ ((D : Int) - 1) * y ^ 2 :=
    mul_nonneg (by omega) hy2
  constructor
  · nlinarith [sq_nonneg (x + (rho : Int))]
  constructor
  · nlinarith [sq_nonneg (x - (rho : Int))]
  constructor
  · nlinarith [sq_nonneg (y + (rho : Int))]
  · nlinarith [sq_nonneg (y - (rho : Int))]

/-- The bounding box loses no lattice point when `D` is positive. -/
theorem mem_ellipsePairs_iff (D rho : Nat) (hD : 0 < D) (x y : Int) :
    (x, y) ∈ ellipsePairs D rho ↔
      x ^ 2 + (D : Int) * y ^ 2 ≤ (rho : Int) ^ 2 := by
  simp only [ellipsePairs, Finset.mem_filter, Prod.fst, Prod.snd]
  constructor
  · exact fun h => h.2
  · intro h
    obtain ⟨hx₁, hx₂, hy₁, hy₂⟩ := ellipse_coordinate_bounds D rho hD x y h
    exact ⟨Finset.mem_product.mpr
      ⟨Finset.mem_Icc.mpr ⟨hx₁, hx₂⟩, Finset.mem_Icc.mpr ⟨hy₁, hy₂⟩⟩, h⟩

/-- At fixed radius, increasing `D` can only remove lattice points. -/
theorem ellipsePairs_antitone_D (D₁ D₂ rho : Nat) (hD : D₁ ≤ D₂) :
    ellipsePairs D₂ rho ⊆ ellipsePairs D₁ rho := by
  intro p hp
  simp only [ellipsePairs, Finset.mem_filter] at hp ⊢
  refine ⟨hp.1, ?_⟩
  have hD' : (D₁ : Int) ≤ D₂ := by exact_mod_cast hD
  have hy : (0 : Int) ≤ p.2 ^ 2 := sq_nonneg p.2
  have hprod : 0 ≤ ((D₂ : Int) - D₁) * p.2 ^ 2 :=
    mul_nonneg (by omega) hy
  nlinarith [hp.2]

theorem ellipsePairs_card_antitone_D (D₁ D₂ rho : Nat) (hD : D₁ ≤ D₂) :
    (ellipsePairs D₂ rho).card ≤ (ellipsePairs D₁ rho).card :=
  Finset.card_le_card (ellipsePairs_antitone_D D₁ D₂ rho hD)

/-- Ender's radius turns the cell-area estimate into the strict rank count.
The area estimate is deliberately an explicit hypothesis, not a checked theorem. -/
theorem ellipsePairs_card_gt_of_ender_radius_and_area
    (D rho q : Nat) (hD : 0 < D) (hq : 0 < q)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt ((q : Real) * Real.sqrt D / Real.pi) +
        10 * Real.sqrt D ≤ (rho : Real))
    (harea : Real.pi * ((rho : Real) - (1 + Real.sqrt D) / 2) ^ 2 ≤
        ((ellipsePairs D rho).card : Real) * Real.sqrt D) :
    q < (ellipsePairs D rho).card := by
  let s : Real := Real.sqrt D
  let beta : Real := Real.sqrt ((q : Real) * s / Real.pi)
  let delta : Real := (1 + s) / 2
  have hs : 0 < s := Real.sqrt_pos.2 (by exact_mod_cast hD)
  have hsone : 1 ≤ s := by
    have : (1 : Real) ≤ D := by exact_mod_cast hD
    nlinarith [Real.sq_sqrt (by positivity : (0 : Real) ≤ D)]
  have hpi : 0 < Real.pi := Real.pi_pos
  have harg : 0 < (q : Real) * s / Real.pi := by positivity
  have hbeta : 0 < beta := Real.sqrt_pos.2 harg
  have hbeta2 : Real.pi * beta ^ 2 = (q : Real) * s := by
    dsimp [beta]
    rw [Real.sq_sqrt (le_of_lt harg)]
    field_simp
  have hdelta : delta ≤ s := by dsimp [delta]; linarith
  have hdiff : beta < (rho : Real) - delta := by
    dsimp [delta] at hdelta ⊢
    dsimp [beta, s] at hradius ⊢
    nlinarith [Real.sqrt_nonneg ((q : Real) * Real.sqrt D / Real.pi)]
  have hsquare : beta ^ 2 < ((rho : Real) - delta) ^ 2 := by
    nlinarith [mul_pos (sub_pos.mpr hdiff)
      (by linarith : 0 < (rho : Real) - delta + beta)]
  have hreal : (q : Real) * s < ((ellipsePairs D rho).card : Real) * s := by
    calc
      (q : Real) * s = Real.pi * beta ^ 2 := hbeta2.symm
      _ < Real.pi * ((rho : Real) - delta) ^ 2 := by nlinarith
      _ ≤ ((ellipsePairs D rho).card : Real) * s := harea
  have : (q : Real) < ((ellipsePairs D rho).card : Real) :=
    (mul_lt_mul_right hs).mp hreal
  exact_mod_cast this

/-- Positive `D` keeps distinct integer coordinate pairs distinct in `ℂ`. -/
theorem latticePoint_injective (D : Nat) (hD : 0 < D) :
    Function.Injective (fun p : Int × Int => latticePoint (D : Real) p.1 p.2) := by
  intro p q hpq
  have hsqrt : 0 < Real.sqrt (D : Real) :=
    Real.sqrt_pos.2 (by exact_mod_cast hD)
  have hre : (p.1 : Real) = (q.1 : Real) := by
    have := congrArg Complex.re hpq
    simpa [latticePoint] using this
  have him : (p.2 : Real) * Real.sqrt (D : Real) =
      (q.2 : Real) * Real.sqrt (D : Real) := by
    have := congrArg Complex.im hpq
    simpa [latticePoint] using this
  have hx : p.1 = q.1 := by exact_mod_cast hre
  have hy : p.2 = q.2 := by
    have : (p.2 : Real) = (q.2 : Real) :=
      mul_right_cancel₀ (ne_of_gt hsqrt) him
    exact_mod_cast this
  exact Prod.ext hx hy

theorem ellipsePoints_card (D rho : Nat) (hD : 0 < D) :
    (ellipsePoints D rho).card = (ellipsePairs D rho).card := by
  exact Finset.card_image_of_injective _ (latticePoint_injective D hD)

/-- The image is exactly the lattice ellipse, including boundary and origin. -/
theorem mem_ellipsePoints_iff (D rho : Nat) (hD : 0 < D) (z : Complex) :
    z ∈ ellipsePoints D rho ↔
      ∃ x y : Int, z = latticePoint (D : Real) x y ∧
        Complex.normSq z ≤ (rho : Real) ^ 2 := by
  constructor
  · intro hz
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hz
    refine ⟨p.1, p.2, rfl, ?_⟩
    rw [latticePoint_normSq (D : Real) (by positivity)]
    have h := (mem_ellipsePairs_iff D rho hD p.1 p.2).mp hp
    exact_mod_cast h
  · rintro ⟨x, y, rfl, hz⟩
    apply Finset.mem_image.mpr
    refine ⟨(x, y), ?_, rfl⟩
    apply (mem_ellipsePairs_iff D rho hD x y).mpr
    rw [latticePoint_normSq (D : Real) (by positivity)] at hz
    exact_mod_cast hz

/-- A count for the actual ellipse supplies the existing Gram theorem. -/
theorem ellipseTraceGram_det_bounds (D rho J R S : Nat) (hD : 0 < D)
    (hR : 1 ≤ R) (hS : 1 ≤ S) (hJ : S ≤ J)
    (hcard : 2 * (R - 1) + (S - 1) < (ellipsePairs D rho).card) :
    0 < (rectangularTraceGram (ellipsePoints D rho) J R S).det ∧
      (rectangularTraceGram (ellipsePoints D rho) J R S).det ≤
        Finset.univ.prod (fun i => rectangularTraceGram (ellipsePoints D rho) J R S i i) := by
  apply rectangularTraceGram_det_bounds (ellipsePoints D rho) J R S hR hS hJ
  rwa [ellipsePoints_card D rho hD]

/-- A count certified at an interval's upper endpoint works throughout it. -/
theorem ellipseTraceGram_det_bounds_of_upper_endpoint
    (D D₂ rho J R S : Nat) (hD : 0 < D) (hD₂ : D ≤ D₂)
    (hR : 1 ≤ R) (hS : 1 ≤ S) (hJ : S ≤ J)
    (hcard : 2 * (R - 1) + (S - 1) < (ellipsePairs D₂ rho).card) :
    0 < (rectangularTraceGram (ellipsePoints D rho) J R S).det ∧
      (rectangularTraceGram (ellipsePoints D rho) J R S).det ≤
        Finset.univ.prod (fun i => rectangularTraceGram (ellipsePoints D rho) J R S i i) := by
  apply ellipseTraceGram_det_bounds D rho J R S hD hR hS hJ
  exact lt_of_lt_of_le hcard (ellipsePairs_card_antitone_D D D₂ rho hD₂)

/-- Ender's stronger `3R+S` guard at `J=S`, checked at the upper endpoint. -/
theorem ellipseTraceGram_det_bounds_of_ender_guard
    (D D₂ rho R S : Nat) (hD : 0 < D) (hD₂ : D ≤ D₂)
    (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hcard : 3 * R + S < (ellipsePairs D₂ rho).card) :
    0 < (rectangularTraceGram (ellipsePoints D rho) S R S).det ∧
      (rectangularTraceGram (ellipsePoints D rho) S R S).det ≤
        Finset.univ.prod (fun i => rectangularTraceGram (ellipsePoints D rho) S R S i i) := by
  apply ellipseTraceGram_det_bounds_of_upper_endpoint D D₂ rho S R S
    hD hD₂ hR hS le_rfl
  omega

/-- Conditional geometric-to-Gram bridge at the upper endpoint of an
Ender interval. The only unproved premise here is the stated cell area bound. -/
theorem ellipseTraceGram_det_bounds_of_ender_radius_and_area
    (D D₂ rho R S : Nat) (hD : 0 < D) (hD₂ : D ≤ D₂)
    (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real))
    (harea : Real.pi * ((rho : Real) - (1 + Real.sqrt D₂) / 2) ^ 2 ≤
        ((ellipsePairs D₂ rho).card : Real) * Real.sqrt D₂) :
    0 < (rectangularTraceGram (ellipsePoints D rho) S R S).det ∧
      (rectangularTraceGram (ellipsePoints D rho) S R S).det ≤
        Finset.univ.prod (fun i => rectangularTraceGram (ellipsePoints D rho) S R S i i) := by
  have hD₂pos : 0 < D₂ := lt_of_lt_of_le hD hD₂
  have hq : 0 < 3 * R + S := by omega
  have hcard := ellipsePairs_card_gt_of_ender_radius_and_area
    D₂ rho (3 * R + S) hD₂pos hq hradius harea
  exact ellipseTraceGram_det_bounds_of_ender_guard
    D D₂ rho R S hD hD₂ hR hS hcard

end
end TenthDiscriminant
