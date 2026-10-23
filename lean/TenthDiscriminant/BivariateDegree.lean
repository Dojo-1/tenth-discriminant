import TenthDiscriminant.IrreducibleContact

/-! Exact exchange of the two polynomial coordinates, with multiplicative bidegree.
No sampled degree estimate or normalization is used. -/
namespace TenthDiscriminant
namespace JetAssembly
open Polynomial
noncomputable section
variable {K : Type*} [Field K]

/-- Exchange the coefficient variable W and the outer variable Z. -/
def swapHom : Polynomial (Polynomial K) →+* Polynomial (Polynomial K) :=
  Polynomial.eval₂RingHom (Polynomial.mapRingHom Polynomial.C) (Polynomial.C Polynomial.X)

@[simp] theorem swap_C (p : Polynomial K) : swapHom (Polynomial.C p) = p.map Polynomial.C := by
  simp [swapHom]

@[simp] theorem swap_X : swapHom (Polynomial.X : Polynomial (Polynomial K)) =
    Polynomial.C Polynomial.X := by simp [swapHom]

@[simp] theorem swap_monomial_monomial (n m : Nat) (c : K) :
    swapHom (Polynomial.monomial n (Polynomial.monomial m c)) =
      Polynomial.monomial m (Polynomial.monomial n c) := by
  simp [← Polynomial.C_mul_X_pow_eq_monomial, map_mul, map_pow] <;> ring

/-- This is an exact involution, not a lossy projection. -/
theorem swap_involutive (p : Polynomial (Polynomial K)) : swapHom (swapHom p) = p := by
  have hh : (swapHom (K := K)).comp swapHom = RingHom.id _ := by
    ext <;> simp [swapHom]
  exact congrArg (fun f : Polynomial (Polynomial K) →+* Polynomial (Polynomial K) => f p) hh

/-- Exchanging coordinates transposes the coefficient array. -/
theorem swap_coeff (p : Polynomial (Polynomial K)) (i j : Nat) :
    ((swapHom p).coeff i).coeff j = (p.coeff j).coeff i := by
  induction p using Polynomial.induction_on' with
  | add p q hp hq => simp only [map_add, Polynomial.coeff_add, hp, hq]
  | monomial n p =>
    induction p using Polynomial.induction_on' with
    | add p q hp hq => simp only [Polynomial.monomial_add, map_add, Polynomial.coeff_add, hp, hq]
    | monomial m c =>
      rw [swap_monomial_monomial]
      simp only [Polynomial.coeff_monomial]
      split_ifs <;> simp_all [Polynomial.coeff_monomial]

/-- Actual W degree, not a chosen upper bound. -/
def wDegree (p : Polynomial (Polynomial K)) : Nat := (swapHom p).natDegree

@[simp] theorem wDegree_C (p : Polynomial K) : wDegree (Polynomial.C p) = p.natDegree := by
  unfold wDegree
  rw [swap_C, Polynomial.natDegree_map_eq_of_injective Polynomial.C_injective]

theorem swap_ne_zero {p : Polynomial (Polynomial K)} (hp : p ≠ 0) : swapHom p ≠ 0 := by
  intro h
  apply hp
  have hh := congrArg (swapHom (K := K)) h
  simpa only [swap_involutive, map_zero] using hh

/-- Both degree coordinates are additive on actual nonzero products. -/
theorem wDegree_mul (p q : Polynomial (Polynomial K)) (hp : p ≠ 0) (hq : q ≠ 0) :
    wDegree (p*q) = wDegree p + wDegree q := by
  unfold wDegree
  rw [map_mul, Polynomial.natDegree_mul (swap_ne_zero hp) (swap_ne_zero hq)]

/-- Every inner coefficient lies below the actual W degree. -/
theorem coefficient_natDegree_le_wDegree (p : Polynomial (Polynomial K)) (i : Nat) :
    (p.coeff i).natDegree ≤ wDegree p := by
  by_cases hi : p.coeff i = 0
  · simp [hi]
  by_contra! h
  have hz : (swapHom p).coeff (p.coeff i).natDegree = 0 :=
    Polynomial.coeff_eq_zero_of_natDegree_lt h
  have hc : ((swapHom p).coeff (p.coeff i).natDegree).coeff i = 0 := by rw [hz]; simp
  rw [swap_coeff] at hc
  exact (Polynomial.leadingCoeff_ne_zero.mpr hi) hc

/-- The degree definition agrees with uniform coefficient-degree bounds. -/
theorem wDegree_le_of_coefficients (p : Polynomial (Polynomial K)) (b : Nat)
    (h : ∀ i, (p.coeff i).natDegree ≤ b) : wDegree p ≤ b := by
  by_cases hp : p = 0
  · simp [hp, wDegree]
  by_contra! hb
  have hz : (swapHom p).coeff (wDegree p) = 0 := by
    ext i
    rw [swap_coeff]
    exact Polynomial.coeff_eq_zero_of_natDegree_lt ((h i).trans_lt hb)
  exact (Polynomial.leadingCoeff_ne_zero.mpr (swap_ne_zero hp)) hz

/-- Zero W degree means an actual polynomial in Z with constant coefficients. -/
theorem exists_constant_coefficients (p : Polynomial (Polynomial K)) (h : wDegree p = 0) :
    ∃ q : Polynomial K, p = q.map Polynomial.C := by
  have hh : swapHom p = Polynomial.C ((swapHom p).coeff 0) :=
    Polynomial.eq_C_of_natDegree_eq_zero h
  refine ⟨(swapHom p).coeff 0, ?_⟩
  have hr := congrArg (swapHom (K := K)) hh
  simpa only [swap_involutive, swap_C] using hr

end
end JetAssembly
end TenthDiscriminant
