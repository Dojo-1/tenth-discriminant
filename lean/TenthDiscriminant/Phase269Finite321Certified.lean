import TenthDiscriminant.Phase269Finite321Seed08

/-!
# Phase269: bounded finite CRT certificate

Only the existing generic wheel and quotient transport lemmas and
nine *fully computed* seed propositions enter this proof. In particular
the earlier global nine-field theorem is not imported.
-/
namespace TenthDiscriminant.Phase269
set_option autoImplicit false

theorem seeds269_exact :
    seeds269 = [11,35,43,83,99,115,123,131,139] := by decide +kernel

theorem all_seeds269 : seeds269.all seed269 = true := by
  rw [seeds269_exact]
  simp only [List.all_cons, List.all_nil,
    seed269_0, seed269_1, seed269_2, seed269_3, seed269_4,
    seed269_5, seed269_6, seed269_7, seed269_8, Bool.and_self]

/-- Closed arithmetic certificate at the already merged 322^4
field bound, with the original strict d/4 guard and every quotient bit. -/
theorem finite322_certificate :
    ∀ d : Nat, 163 < d → d < (322 : Nat)^4 → d % 8 = 3 →
      guardedPrimeTests d finite321Primes = false :=
  finite269_of_all_seeds all_seeds269

/-- Preserve the previously checked 321^4 result as a consequence of
the stronger certificate, without altering its statement. -/
theorem finite321_certificate :
    ∀ d : Nat, 163 < d → d < (321 : Nat)^4 → d % 8 = 3 →
      guardedPrimeTests d finite321Primes = false := by
  intro d hlo hhi hmod
  exact finite322_certificate d hlo
    (lt_trans hhi (by norm_num : (321 : Nat)^4 < (322 : Nat)^4)) hmod

/-- The new stand-alone bounded field exclusion. This depends on the
already-formalized field->inertness bridge and the new arithmetic certificate.
It does not depend on the old field-classification theorem. -/
theorem classNumber_ne_one_below_321_of_large (d : Nat)
    [Fact (0 < d)] (hsq : Squarefree d)
    (hlo : 163 < d) (hhi : d < (321 : Nat)^4) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 :=
  no_classNumber_one_of_finite321_certificate finite321_certificate d hsq hlo hhi

/-- Stand-alone bounded exclusion for the merged 322^4 endpoint.
This does NOT use the existing nine-field classification theorem. -/
theorem classNumber_ne_one_below_322_of_large (d : Nat)
    [Fact (0 < d)] (hsq : Squarefree d)
    (hlo : 163 < d) (hhi : d < (322 : Nat)^4) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  intro hc
  have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
  have htests := guardedPrimeTests_of_classNumber_one d hsq hc hmod
    finite321Primes finite321Primes_checked
  have hbad := finite322_certificate d hlo hhi hmod
  rw [hbad] at htests
  cases htests

#print axioms TenthDiscriminant.Phase269.finite322_certificate
#print axioms TenthDiscriminant.Phase269.classNumber_ne_one_below_322_of_large
#print axioms TenthDiscriminant.Phase269.finite321_certificate
#print axioms TenthDiscriminant.Phase269.classNumber_ne_one_below_321_of_large
end TenthDiscriminant.Phase269
