import Mathlib

/-!
# E9 - Horizontal ordinary-jet obstruction polynomial

This certifies the polynomial/IVT lemma, NOT the 12x12 determinant identity.
CAS checks derive det(E(x)) = -1024*x^4*(x-2)^4*horizontalObstruction(x)
for the original ordinary-Z feature matrix at D=1,R=6,S=J=2 and
q=(0,1),(2,1),(x,1). Source-matrix equality is an unproved bridge in Lean.
No integer-grid singularity or field-discriminant improvement is claimed.
-/
namespace TenthDiscriminant.E9

noncomputable def horizontalObstruction (x : Real) : Real :=
  3*x^8-24*x^7-40*x^6+576*x^5-2448*x^4+5504*x^3-
  12288*x^2+15360*x-13312

noncomputable def determinantFactor (x : Real) : Real :=
  -1024*x^4*(x-2)^4*horizontalObstruction x

theorem determinantFactor_endpoint_values :
    determinantFactor 7 = 3063195031680000 ∧
    determinantFactor 8 = -2733042309267456 := by
  norm_num [determinantFactor, horizontalObstruction]

theorem horizontalObstruction_endpoint_signs :
    horizontalObstruction 7 < 0 ∧
    0 < horizontalObstruction 8 := by
  norm_num [horizontalObstruction]

private theorem obstruction_continuous : Continuous horizontalObstruction := by
  unfold horizontalObstruction
  fun_prop

/-- A real, not generally integer, root in (7,8). -/
theorem horizontalObstruction_has_root :
    ∃ x : Real, 7 < x ∧ x < 8 ∧ horizontalObstruction x = 0 := by
  have hneg := horizontalObstruction_endpoint_signs.1
  have hpos := horizontalObstruction_endpoint_signs.2
  have hmem : (0 : Real) ∈
      Set.Icc (horizontalObstruction 7) (horizontalObstruction 8) :=
    ⟨le_of_lt hneg, le_of_lt hpos⟩
  obtain ⟨x, hx, hf⟩ := Set.mem_image.mp
    (intermediate_value_Icc (by norm_num : (7 : Real) ≤ 8)
       obstruction_continuous.continuousOn hmem)
  rcases Set.mem_Icc.mp hx with ⟨hxl, hxr⟩
  have hl : (7 : Real) < x := by
    by_contra hn
    have heq : x = 7 := le_antisymm (le_of_not_gt hn) hxl
    subst x
    linarith
  have hr : x < (8 : Real) := by
    by_contra hn
    have heq : x = 8 := le_antisymm hxr (le_of_not_gt hn)
    subst x
    linarith
  exact ⟨x, hl, hr, hf⟩

/-- The integer polynomial corresponding to the source-matched obstruction. -/
def horizontalObstructionInt (x : Int) : Int :=
  3*x^8-24*x^7-40*x^6+576*x^5-2448*x^4+5504*x^3-
  12288*x^2+15360*x-13312

/-- The five residue values modulo five are 3,1,3,4,4. -/
private theorem obstruction_mod_five_nonzero (x : ZMod 5) :
    3*x^8-24*x^7-40*x^6+576*x^5-2448*x^4+5504*x^3-
    12288*x^2+15360*x-13312 ≠ 0 := by
  fin_cases x <;> decide

/-- No integer abscissa can be a root of the residual polynomial.
The continuous obstruction still has a noninteger real root. -/
theorem horizontalObstructionInt_ne_zero (x : Int) :
    horizontalObstructionInt x ≠ 0 := by
  intro hzero
  have hcast : (horizontalObstructionInt x : ZMod 5) = 0 := by
    exact_mod_cast hzero
  have hbad :
      3*(x : ZMod 5)^8-24*(x : ZMod 5)^7-40*(x : ZMod 5)^6+
      576*(x : ZMod 5)^5-2448*(x : ZMod 5)^4+
      5504*(x : ZMod 5)^3-12288*(x : ZMod 5)^2+
      15360*(x : ZMod 5)-13312 = 0 := by
    simpa [horizontalObstructionInt] using hcast
  exact obstruction_mod_five_nonzero (x : ZMod 5) hbad


end TenthDiscriminant.E9

#print axioms TenthDiscriminant.E9.horizontalObstruction_has_root
#print axioms TenthDiscriminant.E9.determinantFactor_endpoint_values
#print axioms TenthDiscriminant.E9.horizontalObstructionInt_ne_zero
