import TenthDiscriminant.E30FiniteKernelTransition

/-!
# E41 — Uniform conductor-kernel collapse under a deeper observation

E30 checked selected mod-4,8,16,32 transitions for the k=2
coefficient frame. E41 proves the universal exact INTEGER statement:

  (k*a) mod (k*m) = 0 and k != 0 => a mod m = 0.

Thus a kernel witness at observation modulus k*m becomes zero
when reduced to modulus m. This is an actual integral divisibility
cancellation, not the limit of an invented scalar-valued signal.

For k=p^e and m=p^n this covers all p≠0, e,n, not merely
a chosen list of finite 2-adic examples. It does NOT construct
Z_p or prove a categorical inverse-limit theorem. Kernel versus
cokernel remain separate, and no original-Gram or field bound
follows from this modular cancellation alone.
-/

namespace TenthDiscriminant.E41
set_option autoImplicit false
noncomputable section

/-- Arbitrary nonzero integral conductor: any kernel witness at
the finer modulus k*m reduces to zero at the coarser modulus m. -/
theorem integral_conductor_kernel_reduces_zero
    (k m a : Int) (hk : k ≠ 0)
    (h : (k*a) % (k*m) = 0) :
    a % m = 0 := by
  have hdiv : k*m ∣ k*a :=
    (Int.dvd_iff_emod_eq_zero).2 h
  rcases hdiv with ⟨w, hw⟩
  have hcancel : a = m*w := by
    apply mul_left_cancel₀ hk
    calc
      k*a = (k*m)*w := hw
      _ = k*(m*w) := by ring
  exact Int.emod_eq_zero_of_dvd ⟨w, hcancel⟩

/-- All positive dyadic observation depths, not only E30's
explicit finite tests, are governed by the same kernel reduction. -/
theorem all_dyadic_kernel_transitions (n : Nat) (a : Int)
    (h : (2*a) % (2*(2:Int)^n) = 0) :
    a % (2:Int)^n = 0 := by
  exact integral_conductor_kernel_reduces_zero 2
    ((2:Int)^n) a (by norm_num) h

/-- A uniform prime-power-shaped contract. No primality needed;
the statement is integral cancellation for every nonzero p. -/
theorem all_power_conductor_transitions
    (p : Int) (hp : p ≠ 0) (e n : Nat) (a : Int)
    (h : (p^e*a) % (p^e * p^n) = 0) :
    a % p^n = 0 := by
  exact integral_conductor_kernel_reduces_zero
    (p^e) (p^n) a (pow_ne_zero e hp) h

/-- A compatible coarse representative aLow retains no kernel
information after a fine observer is zero, relative to its
specific modulus p^n and conductor shift e. -/
theorem compatible_coarse_kernel_is_zero
    (p : Int) (hp : p ≠ 0) (e n : Nat)
    (aHigh aLow : Int)
    (hFine : (p^e*aHigh) % (p^e*p^n) = 0)
    (hCompat : aLow % p^n = aHigh % p^n) :
    aLow % p^n = 0 := by
  rw [hCompat]
  exact all_power_conductor_transitions p hp e n aHigh hFine

/-- The E30 finite mod-16 -> mod-8 instance is subsumed by the
all-depth theorem, with no new source or scalar proxy. -/
theorem mod16_to_mod8_via_universal
    (a : Int) (h : (2*a) % 16 = 0) :
    a % 8 = 0 := by
  have hh : (2*a) % (2*(2:Int)^3) = 0 := by
    norm_num at *
    exact h
  have hout := all_dyadic_kernel_transitions 3 a hh
  simpa using hout

/-- This is a kernel result; an inaccessible odd target is a
different cokernel obstruction already checked in E30. -/
theorem kernel_collapse_and_missing_target_coexist
    (a : Int) (h : (2*a) % 8 = 0) :
    (a % 4 = 0) ∧
      (∀ b : Int, (2*b) % 8 ≠ 1) := by
  constructor
  · have hh : (2*a) % (2*(2:Int)^2) = 0 := by
      norm_num at *
      exact h
    have ho := all_dyadic_kernel_transitions 2 a hh
    simpa using ho
  · exact E30.no_odd_target_mod8

end
end TenthDiscriminant.E41

#print axioms TenthDiscriminant.E41.integral_conductor_kernel_reduces_zero
#print axioms TenthDiscriminant.E41.all_dyadic_kernel_transitions
#print axioms TenthDiscriminant.E41.all_power_conductor_transitions
#print axioms TenthDiscriminant.E41.compatible_coarse_kernel_is_zero
#print axioms TenthDiscriminant.E41.kernel_collapse_and_missing_target_coexist
