import TenthDiscriminant.E29LocalUnitAndKernel

/-!
# E30: finite adic persistence vs. disappearance of source ambiguity

The scalar |ker(k mod p^n)| is not a persistent witness. With k=2
and n=1,2,3,4, every finite-level kernel has cardinality two, but
reduction of a kernel witness at level n+1 lands at zero at level n.

These are exact finite original-residue observations, rather than a
formal Lean construction of Z_2 or an arbitrary inverse limit.
The corresponding missing odd target (cokernel control) persists.
-/

namespace TenthDiscriminant.E30
set_option autoImplicit false

/-- Explicit observation-clock reductions between consecutive powers
of two. These are actual coefficient residue maps, not an arbitrary
transport of representatives. -/
def reduce4to2 (x : ZMod 4) : ZMod 2 := (x.val : ZMod 2)
def reduce8to4 (x : ZMod 8) : ZMod 4 := (x.val : ZMod 4)
def reduce16to8 (x : ZMod 16) : ZMod 8 := (x.val : ZMod 8)

/-- At every tested depth there are exactly two locally ambiguous
source coefficients for multiplication by 2. -/
theorem kernel_size_mod2 :
    (Finset.univ.filter (fun x : ZMod 2 =>
      (2 : ZMod 2) * x = 0)).card = 2 := by decide

theorem kernel_size_mod4 :
    (Finset.univ.filter (fun x : ZMod 4 =>
      (2 : ZMod 4) * x = 0)).card = 2 := by decide

theorem kernel_size_mod8 :
    (Finset.univ.filter (fun x : ZMod 8 =>
      (2 : ZMod 8) * x = 0)).card = 2 := by decide

theorem kernel_size_mod16 :
    (Finset.univ.filter (fun x : ZMod 16 =>
      (2 : ZMod 16) * x = 0)).card = 2 := by decide

/-- Yet every mod-4 ambiguity projects to zero at mod 2. -/
theorem mod4_kernel_projects_zero (x : ZMod 4)
    (hx : (2 : ZMod 4) * x = 0) :
    reduce4to2 x = 0 := by
  -- Exact finite arithmetic, quantifying over all four residues.
  have h : ∀ y : ZMod 4,
      (2 : ZMod 4) * y = 0 → (y.val : ZMod 2) = 0 := by decide
  exact h x hx

theorem mod8_kernel_projects_zero (x : ZMod 8)
    (hx : (2 : ZMod 8) * x = 0) :
    reduce8to4 x = 0 := by
  have h : ∀ y : ZMod 8,
      (2 : ZMod 8) * y = 0 → (y.val : ZMod 4) = 0 := by decide
  exact h x hx

theorem mod16_kernel_projects_zero (x : ZMod 16)
    (hx : (2 : ZMod 16) * x = 0) :
    reduce16to8 x = 0 := by
  have h : ∀ y : ZMod 16,
      (2 : ZMod 16) * y = 0 → (y.val : ZMod 8) = 0 := by decide
  exact h x hx

/-- Contrary to a naive kernel-cardinality argument, a nonzero
mod-2 ambiguity CANNOT be extended to a coherent mod-4 source kernel. -/
theorem no_nonzero_source_kernel_lift_from_two :
    ¬ ∃ x : ZMod 4,
      (2 : ZMod 4) * x = 0 ∧ reduce4to2 x = 1 := by
  rintro ⟨x,hx,h1⟩
  have hz := mod4_kernel_projects_zero x hx
  have hne : (0 : ZMod 2) ≠ 1 := by decide
  exact hne (hz.symm.trans h1)

/-- More generally, any explicitly compatible mod-2 kernel
observation inherited from a mod-4 kernel is necessarily zero. -/
theorem coherent_two_level_kernel_is_zero (x2 : ZMod 2) (x4 : ZMod 4)
    (h4 : (2 : ZMod 4) * x4 = 0)
    (hcompat : reduce4to2 x4 = x2) :
    x2 = 0 := by
  rw [← hcompat]
  exact mod4_kernel_projects_zero x4 h4

theorem coherent_three_level_kernel_is_zero_at_four
    (x4 : ZMod 4) (x8 : ZMod 8)
    (h8 : (2 : ZMod 8) * x8 = 0)
    (hcompat : reduce8to4 x8 = x4) :
    x4 = 0 := by
  rw [← hcompat]
  exact mod8_kernel_projects_zero x8 h8

/-- The missing target witness 1 survives at each observation depth:
multiplication by 2 is not surjective. This is a cokernel signal,
not a persistent nonzero source-kernel element. -/
theorem odd_target_missing_mod2 :
    ¬ ∃ x : ZMod 2, (2 : ZMod 2) * x = 1 := by decide

theorem odd_target_missing_mod4 :
    ¬ ∃ x : ZMod 4, (2 : ZMod 4) * x = 1 := by decide

theorem odd_target_missing_mod8 :
    ¬ ∃ x : ZMod 8, (2 : ZMod 8) * x = 1 := by decide

theorem odd_target_missing_mod16 :
    ¬ ∃ x : ZMod 16, (2 : ZMod 16) * x = 1 := by decide

/-- The unavailable target witness 1 is itself compatible under
observation-clock reduction. -/
theorem target_one_compatible_4to2 : reduce4to2 1 = 1 := by decide
theorem target_one_compatible_8to4 : reduce8to4 1 = 1 := by decide
theorem target_one_compatible_16to8 : reduce16to8 1 = 1 := by decide

end TenthDiscriminant.E30

#print axioms TenthDiscriminant.E30.kernel_size_mod2
#print axioms TenthDiscriminant.E30.kernel_size_mod4
#print axioms TenthDiscriminant.E30.kernel_size_mod8
#print axioms TenthDiscriminant.E30.kernel_size_mod16
#print axioms TenthDiscriminant.E30.mod4_kernel_projects_zero
#print axioms TenthDiscriminant.E30.no_nonzero_source_kernel_lift_from_two
#print axioms TenthDiscriminant.E30.coherent_three_level_kernel_is_zero_at_four
#print axioms TenthDiscriminant.E30.odd_target_missing_mod16
