import TenthDiscriminant.E16Lower300
import TenthDiscriminant.Phase331JointBinaryOddLog315
import TenthDiscriminant.Phase331OddMassSplit315
import TenthDiscriminant.Phase331BinaryNormalizedGain315
import TenthDiscriminant.Phase331OddTenNormalizedGain315
import TenthDiscriminant.BinaryGap375
import TenthDiscriminant.Phase259Horizontal321

/-!
RESEARCH ONLY: 300-domain candidate, not a certificate until exact-head Lean CI
and independent source-fidelity inspection. Uses same original Qthin ordinary
Z jets and the same integer trace Gram as the 313-domain theorem.
# Phase338 — one same original source Gram lower at D >= 300^4.
This is the Phase331 arithmetic structure, independently rechecking
the numerical R,S, log and prime-budget bounds at the smaller floor.

Uses the SAME jointly unimodular 2-adic row frame; the existing
odd-prime product, and the ten horizontal odd-prime factors.
NO Phase332 mixed-binary gain or other source substitution is used.

This file is only a candidate pending exact-head compilation and
the intended-source semantic audit. The geometric positivity and
analytic upper at 300 are separate theorems.
-/
namespace TenthDiscriminant.E16
open scoped BigOperators Classical
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
open TenthDiscriminant.Phase259
open TenthDiscriminant.Phase331
set_option autoImplicit false
noncomputable section

theorem original_source_joint_normalized_lower_300
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
       (QuadraticField (((D : Int)+1)/4)) = 1)
    (hpositive : 0 < (integerRectangularTraceGram Q D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det) :
    (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) ≤
      Real.log ((integerRectangularTraceGram Q D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
          comparisonScale (Tuned.R D) (Tuned.S D) := by
  let R := Tuned.R D
  let S := Tuned.S D
  have hd := Tuned.dimensions_300 D hD
  have hR : 0 < R := by dsimp [R]; omega
  have hS : 0 < S := by dsimp [S]; omega
  have hcap : D ≤ 5*R := by
    change D ≤ 5*(D/4)
    omega
  have hsource := TenthDiscriminant.Phase331.joint_binary_odd_log_of_pos
    Q D R S hsq hc (Tuned.strict_inertness D) hpositive
  have hodd := Tuned.recovered_mass_le_exact_odd_300 D hD
  have hsplit := jointOddMass_ge_old_plus_three_five_and_ten
    R S (by omega)
  have hexp : jointBinaryGramExponent R S =
      binaryNullGramExponent R S + 2*R*floorMass 4 S := by
    simpa only [floorMass] using jointBinaryGramExponent_eq_old_add R S
  have hexpReal :
      (jointBinaryGramExponent R S : Real) =
      (binaryNullGramExponent R S : Real) +
      ((2*R*floorMass 4 S : Nat) : Real) := by
    rw [hexp]
    push_cast
    ring
  rw [hexpReal] at hsource
  have hmass :
      (binaryNullGramExponent R S : Real)*Real.log 2 +
      ((2*R*floorMass 4 S : Nat) : Real)*Real.log 2 +
      recoveredPrimeMassLower R S FirstEnderInterval.tailBudget +
      (horizontalPrimeMass R S : Real)/500 +
      (((2*R*(∑ p ∈ TenthDiscriminant.Phase323.oddHorizontalPrimes,
         floorMass (p*p) S) : Nat) : Real)*(189/100 : Real)) ≤
        Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
    nlinarith only [hsource,hodd,hsplit]
  have hp := comparisonScale_pos R S hR hS
  have hscaled := div_le_div_of_nonneg_right hmass hp.le
  simp only [add_div] at hscaled
  have hbase := Tuned.recovered_normalized_lower_300 D hD
  have hbin := normalized_binary_quarter R S hR hS
  have hthree := normalizedHorizontalGain_lower
    D R S (by omega) hR hS hcap (by
      dsimp [R,S]
      rfl)
  change (4659/625000 : Real)-16895455/(625000*(D : Real)) ≤
    ((horizontalPrimeMass R S : Real)/500)/comparisonScale R S at hthree
  have hbinary := normalized_new_horizontal_binary_gain R S hR hS (by
    dsimp [R,S]
    rfl)
  have hten := normalized_ten_prime_horizontal_gain R S hR hS (by
    dsimp [R,S]
    rfl)
  dsimp [R,S] at *
  linarith only [hscaled,hbase,hbin,hthree,hbinary,hten]


/-- Same E6/E15 positive original integer Gram: no changed matrix or primes.
The lower is a source arithmetic statement, not a field cutoff. -/
theorem euclid_original_joint_lower_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
       (QuadraticField (((D : Int)+1)/4)) = 1) :
    (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real)) ≤
      Real.log ((integerRectangularTraceGram
        (ellipsePairs D (Tuned.euclidRadius D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
          comparisonScale (Tuned.R D) (Tuned.S D) := by
  have h252 : (252 : Nat)^4 ≤ D := by omega
  have hp := Tuned.euclid_original_integer_gram_det_pos_252 D h252
  exact original_source_joint_normalized_lower_300
    (ellipsePairs D (Tuned.euclidRadius D)) D hD hsq hc hp

end
end TenthDiscriminant.E16

#print axioms TenthDiscriminant.E16.original_source_joint_normalized_lower_300

#print axioms TenthDiscriminant.E16.euclid_original_joint_lower_300
