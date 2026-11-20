import TenthDiscriminant.E29LocalUnitAndKernel

/-!
# E30 — Finite source-exact kernel transition controls

The original quadratic order coefficient map (x,y)->(x,2*y)
has a mod-2^n lostFiber at every finite n>=1. Crucially, a kernel
element at depth n+1 REDUCES TO ZERO at depth n, although each
finite kernel is nontrivial. This is the essential guard against
identifying a persistent scalar cardinality with a persistent
inverse-limit witness.

This file proves exact finite integer-remainder statements for the
moduli 2,4,8,16,32 and their predecessor maps. It does NOT prove
an infinite inverse-limit theorem, a p-adic ring API, any actual
prime-ideal valuation, or a new field-discriminant bound.
-/

namespace TenthDiscriminant.E30
set_option autoImplicit false

/-- Any mod-4 kernel witness reduces to zero mod 2. -/
theorem mod4_kernel_reduces_zero_mod2
    (a : Int) (ha : (2*a) % 4 = 0) :
    a % 2 = 0 := by omega

/-- Any mod-8 kernel witness reduces to zero mod 4. -/
theorem mod8_kernel_reduces_zero_mod4
    (a : Int) (ha : (2*a) % 8 = 0) :
    a % 4 = 0 := by omega

/-- Any mod-16 kernel witness reduces to zero mod 8. -/
theorem mod16_kernel_reduces_zero_mod8
    (a : Int) (ha : (2*a) % 16 = 0) :
    a % 8 = 0 := by omega

/-- Any mod-32 kernel witness reduces to zero mod 16. -/
theorem mod32_kernel_reduces_zero_mod16
    (a : Int) (ha : (2*a) % 32 = 0) :
    a % 16 = 0 := by omega

/-- The nonzero kernel at level 1 disappears under reduction to the
trivial zero level. The subsequent tests give the genuine tower. -/
theorem mod4_nonzero_kernel_generator_reduces_zero :
    ((2*2 : Int) % 4 = 0) ∧
      ((2 : Int) % 4 ≠ 0) ∧
      ((2 : Int) % 2 = 0) := by omega

theorem mod8_nonzero_kernel_generator_reduces_zero :
    ((2*4 : Int) % 8 = 0) ∧
      ((4 : Int) % 8 ≠ 0) ∧
      ((4 : Int) % 4 = 0) := by omega

theorem mod16_nonzero_kernel_generator_reduces_zero :
    ((2*8 : Int) % 16 = 0) ∧
      ((8 : Int) % 16 ≠ 0) ∧
      ((8 : Int) % 8 = 0) := by omega

theorem mod32_nonzero_kernel_generator_reduces_zero :
    ((2*16 : Int) % 32 = 0) ∧
      ((16 : Int) % 32 ≠ 0) ∧
      ((16 : Int) % 16 = 0) := by omega

/-- The full coefficient observer at depth 2 identifies source states
only if their original imaginary-coordinate difference becomes zero
at the preceding depth 1. -/
theorem mod4_observer_collision_implies_mod2_equality
    (a b : Int) (h : (2*a) % 4 = (2*b) % 4) :
    a % 2 = b % 2 := by omega

theorem mod8_observer_collision_implies_mod4_equality
    (a b : Int) (h : (2*a) % 8 = (2*b) % 8) :
    a % 4 = b % 4 := by omega

theorem mod16_observer_collision_implies_mod8_equality
    (a b : Int) (h : (2*a) % 16 = (2*b) % 16) :
    a % 8 = b % 8 := by omega

/-- An odd target coefficient cannot be reconstructed by an even
conductor frame. This is the finite cokernel control. -/
theorem no_odd_target_mod2 (a : Int) :
    (2*a) % 2 ≠ 1 := by omega

theorem no_odd_target_mod4 (a : Int) :
    (2*a) % 4 ≠ 1 := by omega

theorem no_odd_target_mod8 (a : Int) :
    (2*a) % 8 ≠ 1 := by omega

theorem no_odd_target_mod16 (a : Int) :
    (2*a) % 16 ≠ 1 := by omega

/-- Positive and negative facts coexist at the same observation
depth. The kernel is finite-level nontrivial but its lift at the
next level projects to zero; target odd parity remains missing. -/
theorem mod8_source_ambiguity_and_target_obstruction :
    ((2*4 : Int) % 8 = 0) ∧
      (4 : Int) % 8 ≠ 0 ∧
      (∀ a : Int, (2*a) % 8 ≠ 1) := by
  constructor
  · omega
  constructor
  · omega
  · exact no_odd_target_mod8

end TenthDiscriminant.E30

#print axioms TenthDiscriminant.E30.mod4_kernel_reduces_zero_mod2
#print axioms TenthDiscriminant.E30.mod8_kernel_reduces_zero_mod4
#print axioms TenthDiscriminant.E30.mod16_kernel_reduces_zero_mod8
#print axioms TenthDiscriminant.E30.mod32_kernel_reduces_zero_mod16
#print axioms TenthDiscriminant.E30.mod4_observer_collision_implies_mod2_equality
#print axioms TenthDiscriminant.E30.mod8_source_ambiguity_and_target_obstruction
