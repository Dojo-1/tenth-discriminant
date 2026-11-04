import Mathlib

/-!
Phase209 — a genuinely generic formal stage of the ordinary-jet depth proof.

Given a Z-linear operator whose k-fold iterate sends EVERY element into pM,
its (k*m)-fold iterate sends every element into p^m M. This does NOT prove
that the specific divided-Frobenius polynomial derivation has the required
base-step property. That remains a separate source theorem.
-/
namespace TenthDiscriminant.Phase209Iteration

variable {M : Type*} [AddCommGroup M]

def iterateLinear (D : M →+ M) : ℕ → M → M
  | 0, x => x
  | n + 1, x => D (iterateLinear D n x)

theorem iterateLinear_add (D : M →+ M) (a b : ℕ) (x : M) :
    iterateLinear D (a+b) x = iterateLinear D a (iterateLinear D b x) := by
  induction a with
  | zero => simp [iterateLinear]
  | succ a ih =>
    simp only [Nat.succ_add, iterateLinear, ih]

theorem iterateLinear_smul (D : M →+ M) (n : ℕ) (c : ℤ) (x : M) :
    iterateLinear D n (c • x) = c • iterateLinear D n x := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simpa only [iterateLinear, ih] using D.map_zsmul c (iterateLinear D n x)

/-- Formal depth amplification without a source-specific nilpotence axiom.
One must prove the input h for the concrete integral derivation first. -/
theorem iterateLinear_divisible (D : M →+ M)
    (p k : ℕ)
    (h : ∀ x : M, ∃ y : M, iterateLinear D k x = (p : ℤ) • y)
    (m : ℕ) (x : M) :
    ∃ y : M, iterateLinear D (m*k) x = ((p : ℤ)^m) • y := by
  induction m with
  | zero =>
      refine ⟨x, ?_⟩
      simp [iterateLinear]
  | succ m ih =>
      rcases ih with ⟨y, hy⟩
      rcases h y with ⟨z, hz⟩
      refine ⟨z, ?_⟩
      calc
        iterateLinear D ((m+1)*k) x
            = iterateLinear D k (iterateLinear D (m*k) x) := by
                rw [show (m+1)*k=k+m*k by simp [Nat.succ_mul, Nat.add_comm], iterateLinear_add]
        _ = iterateLinear D k (((p : ℤ)^m) • y) := by rw [hy]
        _ = ((p : ℤ)^m) • iterateLinear D k y := iterateLinear_smul D k _ y
        _ = ((p : ℤ)^m) • ((p : ℤ) • z) := by rw [hz]
        _ = ((p : ℤ)^(m+1)) • z := by
            simpa only [pow_succ, smul_smul]

end TenthDiscriminant.Phase209Iteration

#print axioms TenthDiscriminant.Phase209Iteration.iterateLinear_divisible
