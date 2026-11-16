import TenthDiscriminant.Phase331OddMassSplit315
import TenthDiscriminant.Phase331BinaryNormalizedGain315
import TenthDiscriminant.Phase331OddTenNormalizedGain315
import TenthDiscriminant.Lower315
import TenthDiscriminant.BinaryGap375
import TenthDiscriminant.Phase259Horizontal321

/-!
# Phase331: enhanced source lower at the actual 315^4 dimensions

A *single* original integer ordinary-Z-jet trace Gram carries:
* the old exactly-counted vertical 2-primary factor;
* the new horizontal 2-primary factor via ONE combined unimodular frame;
* the existing old odd-prime mass;
* horizontal p² factors at p=3,5 and ten other selected primes.

The lower follows only from the source-level joint integer product and
sound finite prime logarithm/floor certificates. Nothing is assumed
about a padded or surrogate determinant.

This is a source lower theorem conditional on class-number-one and
positivity of the same original Gram. The geometric positivity of the
chosen THIN Q is a separate module.
-/
namespace TenthDiscriminant.Phase331
open scoped BigOperators Classical
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
open TenthDiscriminant.Phase259
set_option autoImplicit false
noncomputable section

/-- Full lower on one arbitrary original source observation support
whose original integer Gram determinant is positive. -/
theorem original_source_joint_normalized_lower_315
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : (315 : Nat)^4 ≤ D)
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
  have hd := Tuned.dimensions_315 D hD
  have hR : 0 < R := by dsimp [R]; omega
  have hS : 0 < S := by dsimp [S]; omega
  have hcap : D ≤ 5*R := by
    change D ≤ 5*(D/4)
    omega
  have hsource := joint_binary_odd_log_of_pos
    Q D R S hsq hc (Tuned.strict_inertness D) hpositive
  have hodd := Tuned.recovered_mass_le_exact_odd_315 D hD
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
  have hbase := Tuned.recovered_normalized_lower_315 D hD
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

end
end TenthDiscriminant.Phase331

#print axioms TenthDiscriminant.Phase331.original_source_joint_normalized_lower_315
