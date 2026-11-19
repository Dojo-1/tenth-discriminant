import TenthDiscriminant.E37SourceCertificateNoFake

/-!
# E38 — Nonzero finite conductor kernels; zero compatible kernel thread

E30 established finite controls at 2,4,8,16,32.
This extends the transition lemma to EVERY depth n for the same
index-two imaginary coefficient frame, without replacing the
original arithmetic coefficient carrier.

At level n, the observation modulus is 2^(n+1).
Every level has a nonzero kernel coefficient 2^n, but any kernel
element at depth n+1 reduces to zero at depth n.

Consequently EVERY coherent sequence of kernel representatives
(under canonical reduction) is the zero sequence.
This is the explicit elementary inverse-limit universal property
for this kernel system. It does not instantiate the Mathlib Z_2
ring API or assert a general theorem on all p-adic orders.

The target coefficient 1 is also unattainable at every depth.
The source ambiguity and the missing-target obstruction behave
differently, even without a geometric curvature interpretation.
-/

namespace TenthDiscriminant.E38
set_option autoImplicit false

/-- The n-th local observation modulus, starting with 2. -/
def modulus (n : Nat) : Int :=
  (2 : Int)^(n+1)

theorem modulus_pos (n : Nat) : 0 < modulus n := by
  unfold modulus
  positivity

theorem modulus_succ (n : Nat) :
    modulus (n+1) = 2 * modulus n := by
  unfold modulus
  rw [show n+1+1 = (n+1)+1 by omega, pow_succ]
  ring

theorem modulus_eq_double_pow (n : Nat) :
    modulus n = 2 * (2 : Int)^n := by
  unfold modulus
  rw [pow_succ]
  ring

/-- GENERAL DEPTH: a source coefficient lost at depth n+1
has zero residue already at depth n. -/
theorem kernel_transition_all_depths
    (n : Nat) (a : Int)
    (h : (2*a) % modulus (n+1) = 0) :
    a % modulus n = 0 := by
  rw [modulus_succ] at h
  have hm : 0 < modulus n := modulus_pos n
  omega

/-- Nontrivial finite kernel at EVERY depth, not just samples
n<=4: the class of 2^n is nonzero modulo 2^(n+1) and is killed by 2. -/
theorem finite_kernel_is_nonzero_every_depth (n : Nat) :
    (2 * (2 : Int)^n) % modulus n = 0 ∧
      (2 : Int)^n % modulus n ≠ 0 := by
  rw [modulus_eq_double_pow]
  have hp : (0 : Int) < (2 : Int)^n := pow_pos (by norm_num) _
  constructor <;> omega

/-- The natural coefficient-target class 1 remains absent from the
image of the even conductor frame at ALL finite observation depths. -/
theorem target_one_missing_all_depths (n : Nat) (a : Int) :
    (2*a) % modulus n ≠ 1 := by
  rw [modulus_eq_double_pow]
  have hp : (0 : Int) < (2 : Int)^n := pow_pos (by norm_num) _
  omega

/-- Exact REPRESENTATIVE-level model of a compatible inverse
system of kernel residue classes: hkernel is the level-wise
kernel equation, hreduce demands compatibility with canonical
modulus reduction. No interval/canonical-representative premise
is needed for the ZERO conclusion. -/
def CoherentKernelThread (a : Nat → Int) : Prop :=
  (∀ n, (2*a n) % modulus n = 0) ∧
    (∀ n, a (n+1) % modulus n = a n)

/-- While every finite-level kernel has nonzero elements, a
compatible thread through ALL levels is necessarily zero. -/
theorem coherent_kernel_thread_is_zero
    (a : Nat → Int) (h : CoherentKernelThread a) :
    ∀ n, a n = 0 := by
  intro n
  have hz : a (n+1) % modulus n = 0 :=
    kernel_transition_all_depths n (a (n+1)) (h.1 (n+1))
  calc
    a n = a (n+1) % modulus n := (h.2 n).symm
    _ = 0 := hz

/-- The zero sequence is genuinely compatible and in each level's
kernel; the coherent kernel system is not empty. -/
theorem zero_thread_is_compatible :
    CoherentKernelThread (fun _ => (0 : Int)) := by
  constructor
  · intro n
    simp
  · intro n
    simp

/-- Complete characterization of this compatible inverse-kernel
object on exact integer representatives. -/
theorem compatible_kernel_iff_zero_thread (a : Nat → Int) :
    CoherentKernelThread a ↔ ∀ n, a n = 0 := by
  constructor
  · exact coherent_kernel_thread_is_zero a
  · intro hz
    have ha : a = fun _ => (0 : Int) := funext hz
    rw [ha]
    exact zero_thread_is_compatible

end TenthDiscriminant.E38

#print axioms TenthDiscriminant.E38.kernel_transition_all_depths
#print axioms TenthDiscriminant.E38.finite_kernel_is_nonzero_every_depth
#print axioms TenthDiscriminant.E38.target_one_missing_all_depths
#print axioms TenthDiscriminant.E38.coherent_kernel_thread_is_zero
#print axioms TenthDiscriminant.E38.compatible_kernel_iff_zero_thread
