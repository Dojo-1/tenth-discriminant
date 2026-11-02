import TenthDiscriminant.BinaryExponentNormalization

/-!
# Phase166: the source-exact binary and odd-prime mass logarithm

One integer; one observation support; one derivative convention.

Phase164 already proves that the product of the univariate 2-primary
divisor and the *odd-only* Frobenius prime product is no larger than the
positive integer determinant of the original thin-Q ordinary-jet Gram.

We now take the monotone real logarithm of THAT SAME inequality and
expand the positive integer prime product exactly, not numerically.
No alternative Q, trace metric, Hasse derivative or new field cutoff.
-/

namespace TenthDiscriminant.BinaryThinLogBridge
open FirstCertificate RadialCutoff
set_option autoImplicit false
noncomputable section

/-- The *odd-only* finite product from the existing source determinant
theorem. This is only a readable abbreviation, not a new prime family. -/
private def oddFactor (R S : Nat) : Nat :=
  ∏ p ∈ oddPrimesBelow R, p ^ (2 * valuationWeight R S p)

/-- Also handles an empty odd-prime set: then the product is exactly 1. -/
private theorem oddFactor_pos (R S : Nat) : 0 < oddFactor R S := by
  unfold oddFactor
  apply Finset.prod_pos
  intro p hp
  have hprime : p.Prime := (Finset.mem_filter.mp hp).2.1
  exact pow_pos hprime.pos _

/-- The finite odd product has exactly the OLD odd-prime log mass:
no prime 2 occurs here. -/
private theorem log_oddFactor_eq (R S : Nat) :
    Real.log ((oddFactor R S : Nat) : Real) =
      exactOddPrimeMass R S := by
  unfold oddFactor
  simp only [Nat.cast_prod, Nat.cast_pow]
  rw [Real.log_prod]
  · simp only [Real.log_pow, exactOddPrimeMass]
  · intro p hp
    have hprime : p.Prime := (Finset.mem_filter.mp hp).2.1
    have hpos : (0 : Real) < (p : Real) := by
      exact_mod_cast hprime.pos
    exact (pow_pos hpos _).ne'

/-- The general elementary principle: if a positive integer z is at
least 2^L times the exact odd product, the LOG of z is at least
L * log(2) plus the old exact odd mass. -/
private theorem log_binary_odd_le_of_int_le
    (R S L : Nat) (z : Int)
    (hz : 0 < z)
    (hle : (((2 ^ L * oddFactor R S : Nat) : Int)) ≤ z) :
    (L : Real) * Real.log 2 + exactOddPrimeMass R S ≤
      Real.log (z : Real) := by
  have hoddNat : 0 < oddFactor R S := oddFactor_pos R S
  have hoddNe : ((oddFactor R S : Nat) : Real) ≠ 0 := by
    exact_mod_cast (Nat.ne_of_gt hoddNat)
  have hprodNat : 0 < (2 ^ L * oddFactor R S : Nat) := by
    exact mul_pos (pow_pos (by decide : (0 : Nat) < 2) L) hoddNat
  have hprodReal :
      (0 : Real) < ((2 ^ L * oddFactor R S : Nat) : Real) := by
    exact_mod_cast hprodNat
  have hcast : ((2 ^ L * oddFactor R S : Nat) : Real) ≤
      (z : Real) := by
    exact_mod_cast hle
  have hlog := Real.log_le_log hprodReal hcast
  have hlogProduct :
      Real.log ((2 ^ L * oddFactor R S : Nat) : Real) =
        (L : Real) * Real.log 2 + exactOddPrimeMass R S := by
    calc
      Real.log ((2 ^ L * oddFactor R S : Nat) : Real) =
          Real.log ((2 : Real) ^ L * ((oddFactor R S : Nat) : Real)) := by
            norm_num
      _ = Real.log ((2 : Real) ^ L) +
            Real.log ((oddFactor R S : Nat) : Real) := by
            rw [Real.log_mul
              (pow_ne_zero _ (by norm_num : (2 : Real) ≠ 0)) hoddNe]
      _ = (L : Real) * Real.log 2 + exactOddPrimeMass R S := by
            rw [Real.log_pow, log_oddFactor_eq]
  rw [hlogProduct] at hlog
  exact hlog

/-- A reusable source-level inequality that does NOT need an ellipse
or a large-D hypothesis.  The support Q may be any original integer-pair
observation set for which the ORIGINAL ordinary-jet trace Gram has
strictly positive determinant.  That positivity is a necessary explicit
premise before logarithms; it is NOT imported from the field cutoff. -/
theorem original_binary_and_exact_odd_mass_log_of_pos
    (Q : Finset (Int × Int)) (D R S : Nat)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1)
    (hRcut : (R : Int) < ((D : Int)+1)/4)
    (hdet : 0 < (integerRectangularTraceGram Q D S R S).det) :
    (binaryNullGramExponent R S : Real) * Real.log 2 +
      exactOddPrimeMass R S ≤
      Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  have hdvd :
      ((2 ^ binaryNullGramExponent R S * oddFactor R S : Nat) : Int) ∣
        (integerRectangularTraceGram Q D S R S).det := by
    simpa only [oddFactor] using
      (originalGram_binary_oddMass_unconditional Q D R S
        hsq hclass hRcut)
  have hle :
      ((2 ^ binaryNullGramExponent R S * oddFactor R S : Nat) : Int) ≤
        (integerRectangularTraceGram Q D S R S).det :=
    Int.le_of_dvd hdet hdvd
  exact log_binary_odd_le_of_int_le R S
    (binaryNullGramExponent R S)
    (integerRectangularTraceGram Q D S R S).det hdet hle

/-- This is the actual SAME-thin-Q theorem under the old original
class-number-one field assumptions and the already-checked geometry
threshold D >= 450^4. It is not a smaller field cutoff. -/
theorem thin_binary_and_exact_odd_mass_log (D : Nat)
    (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    (binaryNullGramExponent (Tuned.R D) (Tuned.S D) : Real) *
      Real.log 2 + exactOddPrimeMass (Tuned.R D) (Tuned.S D) ≤
      Real.log ((integerRectangularTraceGram
        (ellipsePairs D (Tuned.thinRadius D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) := by
  have hpositive :
      0 < (integerRectangularTraceGram
        (ellipsePairs D (Tuned.thinRadius D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det :=
    BinaryThinGramBridge.thin_original_gram_pos D hD
  have hsource :
      ((2 ^ binaryNullGramExponent (Tuned.R D) (Tuned.S D) *
        oddFactor (Tuned.R D) (Tuned.S D) : Nat) : Int) ≤
        (integerRectangularTraceGram
          (ellipsePairs D (Tuned.thinRadius D)) D
          (Tuned.S D) (Tuned.R D) (Tuned.S D)).det := by
    simpa only [oddFactor] using
      (BinaryThinGramBridge.thin_binary_odd_le_original_gram
        D hD hsq hclass)
  exact log_binary_odd_le_of_int_le
    (Tuned.R D) (Tuned.S D)
    (binaryNullGramExponent (Tuned.R D) (Tuned.S D))
    (integerRectangularTraceGram
      (ellipsePairs D (Tuned.thinRadius D)) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det
    hpositive hsource

/-- Independent of the Gram support: the EXISTING recovered odd mass
is bounded by exactly the same odd-only prime product's log mass.
This extracts the old algebraic chain rather than adding or copying
any prime valuation that may already have been counted. -/
theorem recovered_mass_le_exact_odd (D : Nat)
    (hD : 41006250000 ≤ D) :
    recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
      FirstEnderInterval.tailBudget ≤
      exactOddPrimeMass (Tuned.R D) (Tuned.S D) := by
  have hd := Tuned.dimensions D hD
  have hs : 1 ≤ Tuned.S D := by omega
  have htail := certifiedPrimeMassLower_antitone_tail
    (Tuned.R D) (Tuned.S D) hs
    FirstEnderInterval.tail_le_budget
  have hrec :
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
        FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
        (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith
  have hprod := recoveredPrimeMassLower_le_production
    (Tuned.R D) (Tuned.S D)
    (enderTailIntegral 10000)
    (by omega) hs
  have hmass := enderPrimeMassLower_le_exact_production
    (Tuned.R D) (Tuned.S D) 10000
    (by omega) hs (by decide) hd.2.2.2.1
  exact hrec.trans (hprod.trans hmass)

/-- The arithmetic input for a FUTURE normalized comparison:
the extra q=2 term is added only to a proven odd-only lower mass,
and both are bounded by the logarithm of the ONE thin Gram. -/
theorem thin_binary_and_recovered_mass_log (D : Nat)
    (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    (binaryNullGramExponent (Tuned.R D) (Tuned.S D) : Real) *
      Real.log 2 +
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
        FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram
        (ellipsePairs D (Tuned.thinRadius D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) := by
  have hm := recovered_mass_le_exact_odd D hD
  have he := thin_binary_and_exact_odd_mass_log D hD hsq hclass
  linarith

end
end TenthDiscriminant.BinaryThinLogBridge
