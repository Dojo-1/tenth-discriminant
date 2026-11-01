import TenthDiscriminant.PrimeMassAssembly
import TenthDiscriminant.BinaryNullPolynomial

/-!
# Binary and odd-prime determinant divisibility, without double counting

The class-number-one theorem already supplies odd-prime divisors of the
same original integer trace Gram. Once a SEPARATELY PROVED binary divisor
is supplied, its coprimality with the odd-prime mass gives their product.

The present module does not yet construct the binary row factorization:
hbinary remains a visible hypothesis until its source-level Lean proof.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- A binary power can be multiplied by a product of odd prime powers
that divide the very same integer. Neither exponent may be counted twice. -/
theorem binaryOddLocalProduct_dvd
    (P : Finset Nat) (e : Nat → Nat) (n : Nat) (z : Int)
    (hnot : 2 ∉ P)
    (hprime : ∀ p ∈ P, p.Prime)
    (hlocal : ∀ p ∈ P, (p : Int) ^ e p ∣ z)
    (hbinary : (2 : Int) ^ n ∣ z) :
    ((2 ^ n * ∏ p ∈ P, p ^ e p : Nat) : Int) ∣ z := by
  classical
  let P' := insert 2 P
  let e' := fun p : Nat => if p = 2 then n else e p
  have hp' : ∀ p ∈ P', p.Prime := by
    intro p hp
    rcases Finset.mem_insert.mp hp with htwo | hp
    · subst p
      decide
    · exact hprime p hp
  have hl' : ∀ p ∈ P', (p : Int) ^ e' p ∣ z := by
    intro p hp
    rcases Finset.mem_insert.mp hp with htwo | hp
    · subst p
      simpa [e'] using hbinary
    · have hpne : p ≠ 2 := by
        intro he
        subst p
        exact hnot hp
      simpa [e', hpne] using hlocal p hp
  have h := primePowerProduct_dvd_int P' e' z hp' hl'
  have hprod : (∏ p ∈ P, p ^ e' p : Nat) =
      ∏ p ∈ P, p ^ e p := by
    apply Finset.prod_congr rfl
    intro p hp
    have hpne : p ≠ 2 := by
      intro he
      subst p
      exact hnot hp
    simp [e', hpne]
  dsimp [P'] at h
  rw [Finset.prod_insert hnot, hprod] at h
  simpa [e', Nat.cast_mul] using h

/-- The full old odd-prime mass of the original Gram combines with an
additional binary certificate, IF the latter is supplied by a valid
unimodular original-jet factorization. It is not introduced as an axiom. -/
theorem originalGram_binary_and_odd_mass_dvd
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int) % 4 = 3)]
    (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4)
    (hbinary : (2 : Int) ^ binaryNullGramExponent R S ∣
      (integerRectangularTraceGram Q D S R S).det) :
    ((2 ^ binaryNullGramExponent R S *
        ∏ p ∈ oddPrimesBelow R,
          p ^ (2 * valuationWeight R S p) : Nat) : Int) ∣
      (integerRectangularTraceGram Q D S R S).det := by
  classical
  let P := oddPrimesBelow R
  have hnot : 2 ∉ P := by simp [P, oddPrimesBelow]
  have hp : ∀ p ∈ P, p.Prime := by
    intro p hp
    exact (Finset.mem_filter.mp hp).2.1
  have hl : ∀ p ∈ P,
      (p : Int) ^ (2 * valuationWeight R S p) ∣
        (integerRectangularTraceGram Q D S R S).det := by
    intro p hpP
    letI : Fact p.Prime := ⟨hp p hpP⟩
    have hodd : p ≠ 2 := (Finset.mem_filter.mp hpP).2.2
    have hpr : p < R :=
      Finset.mem_range.mp (Finset.mem_filter.mp hpP).1
    have hpri : (p : Int) < R := by exact_mod_cast hpr
    exact rectangularTraceGram_valuation_of_classNumber_one
      Q D S R S p hDsq hodd (hpri.trans hRcut) hclass
  exact binaryOddLocalProduct_dvd P
    (fun p => 2 * valuationWeight R S p)
    (binaryNullGramExponent R S)
    (integerRectangularTraceGram Q D S R S).det
    hnot hp hl hbinary

end TenthDiscriminant
