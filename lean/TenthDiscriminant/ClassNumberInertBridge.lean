import TenthDiscriminant.QuadraticFieldChart

/-!
# From class number one to the local Gram valuation

The maximal-order equivalence lets a residue root define a quotient
of the actual ring of integers. Class number one makes its kernel
principal. Positivity of the imaginary quadratic norm removes the
absolute-value ambiguity, yielding Ender's small-prime nonsquare
input. The analytic cutoff and classification are separate.
-/

namespace TenthDiscriminant
open NumberField
open scoped NumberField

theorem principalNorm_nonneg (D : ℕ) (hD : (D : ℤ) % 4 = 3)
    (x y : ℤ) : 0 ≤ principalNorm (D : ℤ) x y := by
  have hfour := principalNorm_four (D : ℤ) x y hD
  have hD0 : 0 ≤ (D : ℤ) := by omega
  have hy : 0 ≤ y ^ 2 := sq_nonneg y
  have hDy : 0 ≤ (D : ℤ) * y ^ 2 := mul_nonneg hD0 hy
  nlinarith [sq_nonneg (2 * x + y)]

theorem smallPrimeNormLifting_of_classNumber_one
    (D p : ℕ) [Fact p.Prime] [Fact ((D : ℤ) % 4 = 3)]
    (hDsq : Squarefree D)
    (hp2 : p ≠ 2)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : ℤ) + 1) / 4)) = 1) :
    SmallPrimeNormLifting D p := by
  have hD : (D : ℤ) % 4 = 3 := Fact.out
  intro z hz
  let e := halfOrderEquivRingOfIntegers D hDsq
  let f : NumberField.RingOfIntegers
      (QuadraticField (((D : ℤ) + 1) / 4)) →+* ZMod p :=
    (halfOrderResidueMap D p hD hp2 z hz).comp e.symm.toRingHom
  obtain ⟨a, ha⟩ :=
    exists_integer_of_absNorm_of_classNumber_one
      (QuadraticField (((D : ℤ) + 1) / 4)) p f hclass
  let w := e.symm a
  obtain ⟨x, y, hxy⟩ := halfOrder_coordinates D w
  have hanorm : Algebra.norm ℤ a = principalNorm (D : ℤ) x y := by
    have he : e w = a := e.apply_symm_apply a
    rw [← he]
    change Algebra.norm ℤ (halfOrderToRingOfIntegers D w) = _
    rw [hxy]
    exact halfOrder_ringOfIntegers_norm D x y
  have hnonneg := principalNorm_nonneg D hD x y
  have habs : (principalNorm (D : ℤ) x y).natAbs = p := by
    rwa [hanorm] at ha
  have hnorm : principalNorm (D : ℤ) x y = (p : ℤ) := by omega
  exact ⟨x, y, hnorm⟩

theorem smallPrime_nonsquare_of_classNumber_one
    (D p : ℕ) [Fact p.Prime] [Fact ((D : ℤ) % 4 = 3)]
    (hDsq : Squarefree D) (hp2 : p ≠ 2)
    (hsmall : (p : ℤ) < ((D : ℤ) + 1) / 4)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : ℤ) + 1) / 4)) = 1) :
    ¬ IsSquare (-(D : ZMod p)) := by
  exact small_prime_nonsquare_of_norm_lifting D p Fact.out Fact.out hsmall
    (smallPrimeNormLifting_of_classNumber_one D p hDsq hp2 hclass)

theorem rectangularTraceGram_valuation_of_classNumber_one
    (Q : Finset (ℤ × ℤ)) (D J R S p : ℕ)
    [Fact p.Prime] [Fact ((D : ℤ) % 4 = 3)]
    (hDsq : Squarefree D) (hp2 : p ≠ 2)
    (hsmall : (p : ℤ) < ((D : ℤ) + 1) / 4)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : ℤ) + 1) / 4)) = 1) :
    (p : ℤ) ^ (2 * valuationWeight R S p) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  exact rectangularTraceGram_valuation_of_small_prime_norm_lifting
    Q D J R S p Fact.out hp2 hsmall
      (smallPrimeNormLifting_of_classNumber_one D p hDsq hp2 hclass)

theorem fifteen_squarefree : Squarefree (15 : ℕ) := by
  have h35 : IsRelPrime (3 : ℕ) 5 :=
    Nat.coprime_iff_isRelPrime.mp (by decide)
  have h3 : Squarefree (3 : ℕ) := (by norm_num : Nat.Prime 3).squarefree
  have h5 : Squarefree (5 : ℕ) := (by norm_num : Nat.Prime 5).squarefree
  simpa using (squarefree_mul_iff.mpr ⟨h35, h3, h5⟩)

private instance fifteenFieldPositiveFact : Fact (0 < 4 * (4 : ℤ) - 1) :=
  ⟨by norm_num⟩

/-- The recorded `D=15,p=3` ramified root rules out class number one
for this particular quadratic field. It checks that the global
hypothesis has not been silently dropped. -/
theorem fifteen_classNumber_ne_one :
    NumberField.classNumber (QuadraticField 4) ≠ 1 := by
  intro hclass
  letI : Fact (((15 : ℕ) : ℤ) % 4 = 3) := ⟨by decide⟩
  have hlift : SmallPrimeNormLifting 15 3 :=
    smallPrimeNormLifting_of_classNumber_one 15 3 fifteen_squarefree
      (by decide) (by simpa using hclass)
  exact fifteen_three_not_norm_lifting hlift

end TenthDiscriminant
