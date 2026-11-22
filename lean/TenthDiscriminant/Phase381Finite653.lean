import TenthDiscriminant.FiniteSieveBridge

/-!
# Phase381 — small, source-matched finite class-number gate

The existing `smallSieveCandidate_of_classNumber_one` already transports the
actual class-number-one hypothesis through maximal-order arithmetic, prime 2,
and the eight odd base primes. This module only checks the range 0..652 and
returns to the *actual* number-field discriminant.

This is NOT an analytic proof of the 652 cutoff, and NOT a replacement for the
existing unconditional `ClassNumberClassification` theorem. In particular the
separate Epstein/Poisson / Dirichlet ZF(7/8) argument is not imported here.

No new axioms, sorry or classification assumption are introduced.
-/

namespace TenthDiscriminant
set_option autoImplicit false

/-- Finite computation: the existing eight-prime boolean sieve has exactly
nine candidates before applying any squarefree filter for d < 653. The
values are *radicands* rather than absolute field discriminants. -/
theorem phase381_sieve_candidates_below_653 :
    (List.range 653).filter smallSieveCandidate =
      [1, 2, 3, 7, 11, 19, 43, 67, 163] := by
  decide +kernel

/-- Transfer the already-established global-to-local arithmetic soundness
to the finite interval. Unlike a closed-world enumeration of class numbers,
this does not assume the nine-field classification theorem. -/
theorem phase381_classNumber_one_candidates_below_653
    (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d)
    (hclass : NumberField.classNumber (ImaginaryQuadraticField d) = 1)
    (hd : d < 653) :
    d ∈ ([1, 2, 3, 7, 11, 19, 43, 67, 163] : List Nat) := by
  have hm : d ∈ (List.range 653).filter smallSieveCandidate :=
    List.mem_filter.mpr
      ⟨List.mem_range.mpr hd,
        smallSieveCandidate_of_classNumber_one d hsq hclass⟩
  simpa only [phase381_sieve_candidates_below_653] using hm

/-- Return to the signed ACTUAL field discriminant. This deliberately uses
Mathlib's genuine `NumberField.discr`, not the source Gram determinant or
a parameter named discriminant. -/
theorem phase381_actual_discriminant_candidates_below_653
    (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d)
    (hclass : NumberField.classNumber (ImaginaryQuadraticField d) = 1)
    (hdisc : (NumberField.discr (ImaginaryQuadraticField d)).natAbs ≤ 652) :
    NumberField.discr (ImaginaryQuadraticField d) ∈
      ([-4, -8, -3, -7, -11, -19, -43, -67, -163] : List Int) := by
  have hrad : d < 653 := by
    rw [imaginaryQuadratic_discr_natAbs d hsq] at hdisc
    dsimp [absoluteDiscriminantParameter] at hdisc
    split_ifs at hdisc <;> omega
  have hmem :=
    phase381_classNumber_one_candidates_below_653 d hsq hclass hrad
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem
  rcases hmem with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    rw [imaginaryQuadratic_discr _ hsq] <;> norm_num

/-- Explicit hostile control. The finite sieve must not be promoted to a
universal characterization of class number one. The 10987 false positive
is excluded by a split prime 29, which is outside the sieve's base list. -/
theorem phase381_outside_range_false_positive :
    smallSieveCandidate 10987 = true := by
  decide +kernel

/-- A field's squarefree radicand is not its actual even-chart
discriminant: D=-232 corresponds to radicand d=58. -/
theorem phase381_even_chart_parameter_control :
    smallSieveCandidate 58 = false := by
  decide +kernel

end TenthDiscriminant

#check TenthDiscriminant.phase381_sieve_candidates_below_653
#check TenthDiscriminant.phase381_classNumber_one_candidates_below_653
#check TenthDiscriminant.phase381_actual_discriminant_candidates_below_653
#print axioms TenthDiscriminant.phase381_classNumber_one_candidates_below_653
#print axioms TenthDiscriminant.phase381_actual_discriminant_candidates_below_653
