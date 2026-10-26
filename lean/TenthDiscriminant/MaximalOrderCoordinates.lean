import TenthDiscriminant.HalfOrderAlgebraicNorm
import Mathlib.Data.Rat.Lemmas
import Mathlib.Algebra.Squarefree.Basic

/-!
# Rational coordinates for the prospective maximal quadratic order

For squarefree `D ≡ 3 (mod 4)`, integer trace `2a` and integer norm
`a² + D b²` force `a + b√(-D)` to have the half-integral coordinate
shape `x + y(1+√(-D))/2`. This is an arithmetic criterion on rational
coordinates, **not** yet an identification with `𝓞 (ℚ(√(-D)))`.
The crucial denominator step is `D q² ∈ ℤ → q ∈ ℤ`; the `D=9` control
shows why squarefreeness cannot be omitted.
-/

namespace TenthDiscriminant

theorem squarefree_rational_coefficient_integral
    (D : ℕ) (hD : Squarefree D) (q : ℚ)
    (h : ∃ k : ℤ, (D : ℚ) * q ^ 2 = (k : ℚ)) :
    ∃ n : ℤ, q = (n : ℚ) := by
  obtain ⟨k, hk⟩ := h
  have hD0 : D ≠ 0 := hD.ne_zero
  have hDq : (D : ℚ) ≠ 0 := by exact_mod_cast hD0
  have hq : q ^ 2 = (k : ℚ) / (D : ℚ) := by
    apply (eq_div_iff hDq).2
    simpa only [mul_comm] using hk
  have hqdiv : q ^ 2 = Rat.divInt k (D : ℤ) := by
    simpa only [Rat.divInt_eq_div, Int.cast_natCast] using hq
  have hi : ((q.den ^ 2 : ℕ) : ℤ) ∣ (D : ℤ) := by
    simpa only [← Rat.den_pow, hqdiv] using Rat.den_dvd k (D : ℤ)
  have hdiv : q.den ^ 2 ∣ D := Int.natCast_dvd_natCast.mp hi
  have hu : IsUnit q.den := hD q.den (by simpa [pow_two] using hdiv)
  have hden : q.den = 1 := Nat.isUnit_iff.mp hu
  exact ⟨q.num, ((Rat.den_eq_one_iff q).mp hden).symm⟩

private theorem square_mod_four_eq_mod_two (m : ℤ) :
    m ^ 2 % 4 = m % 2 := by
  rcases Int.even_or_odd' m with ⟨u, rfl | rfl⟩
  · have h : (2 * u) ^ 2 = 4 * u ^ 2 := by ring
    rw [h]
    omega
  · have h : (2 * u + 1) ^ 2 = 4 * (u ^ 2 + u) + 1 := by ring
    rw [h]
    omega

theorem same_parity_of_integral_quadratic_norm (D m n : ℤ)
    (hD : D % 4 = 3) (hN : 4 ∣ m ^ 2 + D * n ^ 2) :
    m % 2 = n % 2 := by
  have hm := square_mod_four_eq_mod_two m
  have hn := square_mod_four_eq_mod_two n
  have hN4 : (m ^ 2 + D * n ^ 2) % 4 = 0 := Int.emod_eq_zero_of_dvd hN
  rw [Int.add_emod, Int.mul_emod] at hN4
  rw [hD, hm, hn] at hN4
  have hcases : n % 2 = 0 ∨ n % 2 = 1 := by omega
  rcases hcases with h0 | h1 <;> omega

theorem nine_third_counterexample :
    (9 : ℚ) * (1 / 3 : ℚ) ^ 2 = 1 ∧
      ¬ ∃ n : ℤ, (1 / 3 : ℚ) = (n : ℚ) := by
  constructor
  · norm_num
  · rintro ⟨n, hn⟩
    have hden := congrArg Rat.den hn
    norm_num at hden

theorem rational_quadratic_integral_coordinates
    (D : ℕ) (hDsq : Squarefree D) (hDmod : (D : ℤ) % 4 = 3)
    (a b : ℚ)
    (htrace : ∃ m : ℤ, 2 * a = (m : ℚ))
    (hnorm : ∃ k : ℤ, a ^ 2 + (D : ℚ) * b ^ 2 = (k : ℚ)) :
    ∃ x y : ℤ,
      a = (x : ℚ) + (y : ℚ) / 2 ∧ b = (y : ℚ) / 2 := by
  obtain ⟨m, hm⟩ := htrace
  obtain ⟨k, hk⟩ := hnorm
  have hm2 : (2 * a) ^ 2 = (m : ℚ) ^ 2 := congrArg (· ^ 2) hm
  have hb2 : (D : ℚ) * (2 * b) ^ 2 = ((4 * k - m ^ 2 : ℤ) : ℚ) := by
    push_cast
    nlinarith [hk, hm2]
  obtain ⟨n, hn⟩ :=
    squarefree_rational_coefficient_integral D hDsq (2 * b)
      ⟨4 * k - m ^ 2, hb2⟩
  have hq4 : ((m ^ 2 + (D : ℤ) * n ^ 2 : ℤ) : ℚ) = ((4 * k : ℤ) : ℚ) := by
    calc
      ((m ^ 2 + (D : ℤ) * n ^ 2 : ℤ) : ℚ) =
          (m : ℚ) ^ 2 + (D : ℚ) * (n : ℚ) ^ 2 := by push_cast; ring
      _ = (2 * a) ^ 2 + (D : ℚ) * (2 * b) ^ 2 := by rw [hm, hn]
      _ = 4 * (a ^ 2 + (D : ℚ) * b ^ 2) := by ring
      _ = ((4 * k : ℤ) : ℚ) := by rw [hk]; push_cast; ring
  have hi4 : m ^ 2 + (D : ℤ) * n ^ 2 = 4 * k := by
    exact_mod_cast hq4
  have hpar := same_parity_of_integral_quadratic_norm (D : ℤ) m n hDmod
    (by rw [hi4]; exact dvd_mul_right 4 k)
  have hdiv : 2 ∣ m - n := by omega
  obtain ⟨x, hx⟩ := hdiv
  refine ⟨x, n, ?_, ?_⟩
  · have hxe : (m : ℚ) - (n : ℚ) = 2 * (x : ℚ) := by exact_mod_cast hx
    nlinarith [hm, hn, hxe]
  · linarith [hn]

theorem rational_quadratic_coordinates_unique
    (x₁ y₁ x₂ y₂ : ℤ)
    (ha : (x₁ : ℚ) + (y₁ : ℚ) / 2 = (x₂ : ℚ) + (y₂ : ℚ) / 2)
    (hb : (y₁ : ℚ) / 2 = (y₂ : ℚ) / 2) :
    x₁ = x₂ ∧ y₁ = y₂ := by
  have hyq : (y₁ : ℚ) = (y₂ : ℚ) := by linarith
  have hy : y₁ = y₂ := by exact_mod_cast hyq
  subst y₂
  have hxq : (x₁ : ℚ) = (x₂ : ℚ) := by linarith
  exact ⟨by exact_mod_cast hxq, rfl⟩

theorem rational_quadratic_coordinate_trace_norm
    (D : ℕ) (hDmod : (D : ℤ) % 4 = 3) (x y : ℤ) :
    ∃ m k : ℤ,
      2 * ((x : ℚ) + (y : ℚ) / 2) = (m : ℚ) ∧
      ((x : ℚ) + (y : ℚ) / 2) ^ 2 +
        (D : ℚ) * ((y : ℚ) / 2) ^ 2 = (k : ℚ) := by
  have hc : 4 ∣ (D : ℤ) + 1 := by omega
  obtain ⟨c, hc⟩ := hc
  refine ⟨2 * x + y, x ^ 2 + x * y + c * y ^ 2, ?_, ?_⟩
  · push_cast
    ring
  · have hD : (D : ℚ) + 1 = 4 * (c : ℚ) := by exact_mod_cast hc
    push_cast
    nlinarith [hD]

theorem fifteen_rational_coordinate_control (a b : ℚ)
    (htrace : ∃ m : ℤ, 2 * a = (m : ℚ))
    (hnorm : ∃ k : ℤ, a ^ 2 + (15 : ℚ) * b ^ 2 = (k : ℚ)) :
    ∃ x y : ℤ,
      a = (x : ℚ) + (y : ℚ) / 2 ∧ b = (y : ℚ) / 2 :=
  rational_quadratic_integral_coordinates 15 (by
    have h35 : IsRelPrime (3 : ℕ) 5 :=
      Nat.coprime_iff_isRelPrime.mp (by decide)
    have h3 : Squarefree (3 : ℕ) := (by norm_num : Nat.Prime 3).squarefree
    have h5 : Squarefree (5 : ℕ) := (by norm_num : Nat.Prime 5).squarefree
    simpa using (squarefree_mul_iff.mpr ⟨h35, h3, h5⟩)) (by decide)
    a b htrace hnorm

end TenthDiscriminant
