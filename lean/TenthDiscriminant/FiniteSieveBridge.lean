import TenthDiscriminant.OddPrimeTwo

/-! Necessary finite sieve conditions for the actual field. Finite Boolean
checks are sound; the unclosed middle-range certificate stays explicit. -/
namespace TenthDiscriminant
set_option autoImplicit false

def modularRootTest (d p : Nat) : Bool :=
  (List.range p).any (fun r => (r*r+d)%p == 0)

def guardedPrimeTest (d p : Nat) : Bool :=
  if 4*p ≤ d then !modularRootTest d p else true

def checkedOddPrimes (ps : List Nat) : Bool :=
  ps.all (fun p => decide (p.Prime ∧ p ≠ 2))

def guardedPrimeTests (d : Nat) (ps : List Nat) : Bool := ps.all (guardedPrimeTest d)

def crtBasePrimes : List Nat := [3,5,7,11,13,17,19,23]

def smallSieveCandidate (d : Nat) : Bool :=
  d==1 || d==2 || d==3 || d==7 || (d%8==3 && guardedPrimeTests d crtBasePrimes)

theorem modularRootTest_sound (d p : Nat) (h : modularRootTest d p=true) :
    IsSquare (-(d : ZMod p)) := by
  obtain ⟨r, _hr, hroot⟩ := List.any_eq_true.mp h
  have hzero : (r*r+d)%p=0 := by simpa using hroot
  have hdiv : p ∣ r*r+d := Nat.dvd_of_mod_eq_zero hzero
  have hz : ((r*r+d : Nat) : ZMod p)=0 :=
    (CharP.cast_eq_zero_iff (ZMod p) p _).2 hdiv
  push_cast at hz
  exact ⟨(r : ZMod p), by linear_combination -hz⟩

theorem modularRootTest_false_of_nonsquare (d p : Nat)
    (hno : ¬ IsSquare (-(d : ZMod p))) : modularRootTest d p=false := by
  cases h : modularRootTest d p with
  | false => rfl
  | true => exact False.elim (hno (modularRootTest_sound d p h))

theorem guardedPrimeTest_of_classNumber_one (d p : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hmod : d%8=3) (hp : p.Prime) (hp2 : p ≠ 2) : guardedPrimeTest d p=true := by
  by_cases hbind : 4*p ≤ d
  · have hodd : (d : Int)%4=3 := by omega
    letI : Fact ((d : Int)%4=3) := ⟨hodd⟩
    letI : Fact p.Prime := ⟨hp⟩
    have hc := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hclass
    have hsmall : (p : Int) < ((d : Int)+1)/4 := by omega
    have hn := smallPrime_nonsquare_of_classNumber_one d p hsq hp2 hsmall hc
    have hb := modularRootTest_false_of_nonsquare d p hn
    simp [guardedPrimeTest, hbind, hb]
  · simp [guardedPrimeTest, hbind]

theorem guardedPrimeTests_of_classNumber_one (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hmod : d%8=3) (ps : List Nat) (hps : checkedOddPrimes ps=true) :
    guardedPrimeTests d ps=true := by
  apply List.all_eq_true.mpr
  intro p hp
  have hprime : p.Prime ∧ p ≠ 2 := of_decide_eq_true ((List.all_eq_true.mp hps) p hp)
  exact guardedPrimeTest_of_classNumber_one d p hsq hclass hmod hprime.1 hprime.2

theorem crtBasePrimes_checked : checkedOddPrimes crtBasePrimes=true := by decide +kernel

theorem smallSieveCandidate_of_classNumber_one (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    smallSieveCandidate d=true := by
  rcases imaginaryQuadratic_classNumber_one_small_or_mod_eight d hsq hclass with h | h | h | h | h
  · simp [smallSieveCandidate, h]
  · simp [smallSieveCandidate, h]
  · simp [smallSieveCandidate, h]
  · simp [smallSieveCandidate, h]
  · have hs := guardedPrimeTests_of_classNumber_one d hsq hclass h _ crtBasePrimes_checked
    simp [smallSieveCandidate, h, hs]

/-- The bounded proof-control input is exactly [0,92), not a proxy for
the remaining middle interval. No class-number equality is inferred. -/
theorem smallSieveCandidate_complete_below_92 :
    (List.range 92).filter smallSieveCandidate=[1,2,3,7,11,19,43,67] := by decide +kernel

theorem classNumber_one_small_candidates (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hd : d < 92) : d ∈ ([1,2,3,7,11,19,43,67] : List Nat) := by
  have hm : d ∈ (List.range 92).filter smallSieveCandidate :=
    List.mem_filter.mpr ⟨List.mem_range.mpr hd, smallSieveCandidate_of_classNumber_one d hsq hclass⟩
  simpa only [smallSieveCandidate_complete_below_92] using hm

theorem crtBasePrimes_bounded : crtBasePrimes.all (fun p => decide (p ≤ 23))=true := by decide +kernel

theorem crtBasePrime_test_binds (d p : Nat) (hd : 92 ≤ d) (hp : p ∈ crtBasePrimes) : 4*p ≤ d := by
  have hb : p ≤ 23 := of_decide_eq_true ((List.all_eq_true.mp crtBasePrimes_bounded) p hp)
  omega

theorem checkedOddPrimes_append (ps qs : List Nat) :
    checkedOddPrimes (ps++qs)=(checkedOddPrimes ps && checkedOddPrimes qs) := by
  simp [checkedOddPrimes, List.all_append]

/-- A precise remaining obligation, not a proved classification: a complete
middle-range survivor theorem plus checked odd primes would finish the
necessary candidate list. The nine positive class-number equalities are
also not asserted here. -/
theorem classNumber_one_nine_candidates_of_middle_certificate
    (extra : List Nat) (hextra : checkedOddPrimes extra=true)
    (hcertificate : ∀ d : Nat, 92 ≤ d → d < 700000000000 → d%8=3 →
      guardedPrimeTests d (crtBasePrimes++extra)=true → d=163)
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hclass : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    d ∈ ([1,2,3,7,11,19,43,67,163] : List Nat) := by
  by_cases hd : d < 92
  · have hm := classNumber_one_small_candidates d hsq hclass hd
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hm ⊢
    tauto
  · have hlo : 92 ≤ d := by omega
    have hhi := imaginaryQuadratic_classNumber_one_radicand_bound d hsq hclass
    have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hclass
    have hp : checkedOddPrimes (crtBasePrimes++extra)=true := by
      rw [checkedOddPrimes_append, crtBasePrimes_checked, hextra]
      rfl
    have htests := guardedPrimeTests_of_classNumber_one d hsq hclass hmod _ hp
    have heq := hcertificate d hlo hhi hmod htests
    simp [heq]

theorem known_candidates_pass_control :
    ([1,2,3,7,11,19,43,67,163] : List Nat).all smallSieveCandidate=true := by decide +kernel

theorem inclusive_endpoint_rejected_control :
    guardedPrimeTest 163 41=true ∧ modularRootTest 163 41=true ∧
      (if 4*41 ≤ 163+1 then !modularRootTest 163 41 else true)=false := by decide +kernel

theorem composite_prime_list_rejected_control : checkedOddPrimes [9]=false := by decide +kernel

theorem prime_two_list_rejected_control : checkedOddPrimes [2]=false := by decide +kernel

end TenthDiscriminant
