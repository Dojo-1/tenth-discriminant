import TenthDiscriminant.Phase334ConductorTwo

/-!
# Phase335 — local filtrations of the SAME original ordinary-Z jets

Continue the classical-to-source order comparison from Phases 333–334.
The selected samples Q, source integer-pair lattice, ordinary derivative
direction, row indexing, jet cutoff J, trace pairing and production Gram
remain entirely unchanged.

For a modulus q, define the filtration by requiring every original
ordinary jet to be divisible by q in both integer coordinates.
Odd-modulus filtrations agree in the source and maximal-order bases;
at any even modulus 2*q, maximal-coordinate divisibility loses at most
one factor of 2 when transported back to the original source.

The source mixed factor H(Z,W)=Z^2-W^2 has an exact FOUR-divisible value,
but its first ordinary Z-jet can have valuation only one at p=2.
This explicitly blocks upgrading a full-jet determinant exponent
merely because the order-zero sample has one more factor of two.

No surrogate source, no new field result, no additional Gram divisor.
-/
namespace TenthDiscriminant.Phase335

open TenthDiscriminant
open TenthDiscriminant.Phase333
open TenthDiscriminant.Phase334
set_option autoImplicit false

/-- Coordinatewise modulus filtration of the original rectangular
ordinary-Z evaluation rows, with W held fixed in differentiation. -/
def sourceJetFiltration (Q : Finset (Int × Int))
    (D J R S : Nat) (q : Int) : Prop :=
  ∀ i : Fin (R*S), ∀ a ∈ Q, ∀ j ∈ Finset.range J,
    pairDvd q (integerDerivativeRow D (i.val/S) (i.val%S) j a)

/-- Exactly the SAME jets and sampling points, only written in the
maximal-order coordinate basis (1,omega). -/
def maximalCoordinateJetFiltration (Q : Finset (Int × Int))
    (D J R S : Nat) (q : Int) : Prop :=
  ∀ i : Fin (R*S), ∀ a ∈ Q, ∀ j ∈ Finset.range J,
    pairDvd q
      (sourceToMaximalCoords
        (integerDerivativeRow D (i.val/S) (i.val%S) j a))

/-- A source-lattice divisible vector remains divisible after ANY
integral change to the larger maximal-order coordinate basis. -/
theorem source_pair_divisible_implies_maximal
    (q : Int) (a : Int × Int)
    (h : pairDvd q a) :
    pairDvd q (sourceToMaximalCoords a) := by
  rcases h with ⟨hx,hy⟩
  change q ∣ a.1-a.2 ∧ q ∣ 2*a.2
  constructor
  · exact hx.sub hy
  · obtain ⟨k,hk⟩ := hy
    refine ⟨2*k, ?_⟩
    rw [hk]
    ring

/-- Exact local agreement for all ODD moduli, including odd prime
powers, applied simultaneously to every unchanged ordinary source jet. -/
theorem odd_jet_filtration_equivalence
    (Q : Finset (Int × Int))
    (D J R S : Nat) (q : Int) (hq : q % 2 = 1) :
    sourceJetFiltration Q D J R S q ↔
      maximalCoordinateJetFiltration Q D J R S q := by
  constructor
  · intro h i a ha j hj
    exact (odd_modulus_pair_divisibility_iff q hq _).2
      (h i a ha j hj)
  · intro h i a ha j hj
    exact (odd_modulus_pair_divisibility_iff q hq _).1
      (h i a ha j hj)

/-- For every modulus, stronger source-jet divisibility implies the
same maximal-coordinate filtration: no change in jets or Q. -/
theorem source_jet_filtration_in_maximal
    (Q : Finset (Int × Int)) (D J R S : Nat) (q : Int)
    (h : sourceJetFiltration Q D J R S q) :
    maximalCoordinateJetFiltration Q D J R S q := by
  intro i a ha j hj
  exact source_pair_divisible_implies_maximal q _ (h i a ha j hj)

/-- Index-two correction, in its strongest elementary form:
if the SAME original jet is divisible by 2*q in maximal-order
coordinates, it is divisible by q in source coordinates. -/
theorem maximal_pair_two_step_to_source
    (q : Int) (a : Int × Int)
    (h : pairDvd (2*q) (sourceToMaximalCoords a)) :
    pairDvd q a := by
  have hh := maximal_dvd_implies_twice_source_dvd (2*q) a h
  change (2*q) ∣ 2*a.1 ∧ (2*q) ∣ 2*a.2 at hh
  obtain ⟨⟨u,hu⟩,⟨v,hv⟩⟩ := hh
  constructor
  · refine ⟨u, ?_⟩
    nlinarith only [hu]
  · refine ⟨v, ?_⟩
    nlinarith only [hv]

/-- A uniform one-power-of-two loss bound for the full ORIGINAL
jet evaluation module, not just a single arbitrary coordinate pair. -/
theorem maximal_jet_two_step_to_source
    (Q : Finset (Int × Int)) (D J R S : Nat) (q : Int)
    (h : maximalCoordinateJetFiltration Q D J R S (2*q)) :
    sourceJetFiltration Q D J R S q := by
  intro i a ha j hj
  exact maximal_pair_two_step_to_source q _
    (h i a ha j hj)

/-- The source H(Z,W) evaluated at W=conj(Z), as a genuine pair in
the ORIGINAL quadratic order. -/
def sourceHValue (D : Nat) (a : Int × Int) : Int × Int :=
  pairSub (pairPow D a 2) (pairPow D (pairConj a) 2)

/-- Its ordinary Z-jets use exactly the production integerDerivativeRow
of the monomials Z^2 and W^2. In particular W is held fixed. -/
def originalHOrdinaryJet (D j : Nat) (a : Int × Int) : Int × Int :=
  pairSub (integerDerivativeRow D 2 0 j a)
    (integerDerivativeRow D 0 2 j a)

/-- Strong source-specific order-zero identity, no squarefree,
class-number, prime or field assumptions. -/
theorem sourceHValue_exact (D : Nat) (x y : Int) :
    sourceHValue D (x,y) = (0,4*x*y) := by
  apply Prod.ext <;>
    simp [sourceHValue,pairSub,pairPow,pairMul,pairConj] <;> ring

/-- The original ordinary derivative at j=0 really is the
H(Z,W) value. This is an essential source-semantics bridge. -/
theorem sourceHJet_zero_eq_value (D : Nat) (a : Int × Int) :
    originalHOrdinaryJet D 0 a = sourceHValue D a := by
  rcases a with ⟨x,y⟩
  apply Prod.ext <;>
    simp [originalHOrdinaryJet,sourceHValue,integerDerivativeRow,
      pairSub,pairScale,pairPow,pairMul,pairConj,Nat.descFactorial] <;>
    ring

/-- Every source order-zero mixed H jet has a FULL factor 4. -/
theorem sourceHJet_zero_divisible_by_four
    (D : Nat) (a : Int × Int) :
    pairDvd 4 (originalHOrdinaryJet D 0 a) := by
  rcases a with ⟨x,y⟩
  rw [sourceHJet_zero_eq_value, sourceHValue_exact]
  change (4 : Int) ∣ 0 ∧ (4 : Int) ∣ 4*x*y
  exact ⟨dvd_zero _, ⟨x*y, by ring⟩⟩

/-- A sharp counterexample in the ACTUAL ordinary-Z derivative
convention: at z=w=1 the first H jet is 2, not divisible by 4. -/
theorem originalH_first_ordinary_jet_not_four :
    ¬ pairDvd 4 (originalHOrdinaryJet 3 1 (1,0)) := by
  have heq : originalHOrdinaryJet 3 1 (1,0) = (2,0) := by decide
  rw [heq]
  norm_num [pairDvd]

/-- The same obstruction occurs for the second ordinary derivative,
which equals 2, not a Hasse coefficient. -/
theorem originalH_second_ordinary_jet_not_four :
    ¬ pairDvd 4 (originalHOrdinaryJet 3 2 (1,0)) := by
  have heq : originalHOrdinaryJet 3 2 (1,0) = (2,0) := by decide
  rw [heq]
  norm_num [pairDvd]

/-- Conjugation in maximal-order coordinates (1,omega) uses
conj(omega)=1-omega. Do NOT reuse the source pairConj formula. -/
def maximalConjugate (a : Int × Int) : Int × Int :=
  (a.1+a.2,-a.2)

/-- The same mixed polynomial H evaluated at an arbitrary
maximal-order point. This is a NEGATIVE control, not a new Q. -/
def maximalHValue (D : Nat) (a : Int × Int) : Int × Int :=
  pairSub (maximalPow D a 2)
    (maximalPow D (maximalConjugate a) 2)

/-- At omega itself, H(omega,conj(omega))=2omega-1
for every D. In the maximal-order basis it has an odd coefficient. -/
theorem maximalHValue_omega_exact (D : Nat) :
    maximalHValue D (0,1) = (-1,2) := by
  apply Prod.ext <;>
    simp [maximalHValue,maximalConjugate,maximalPow,maximalMul,pairSub] <;>
    ring

theorem maximalH_omega_not_even (D : Nat) :
    ¬ pairDvd 2 (maximalHValue D (0,1)) := by
  rw [maximalHValue_omega_exact]
  norm_num [pairDvd]

end TenthDiscriminant.Phase335

#print axioms TenthDiscriminant.Phase335.odd_jet_filtration_equivalence
#print axioms TenthDiscriminant.Phase335.maximal_jet_two_step_to_source
#print axioms TenthDiscriminant.Phase335.sourceHJet_zero_divisible_by_four
#print axioms TenthDiscriminant.Phase335.originalH_first_ordinary_jet_not_four
#print axioms TenthDiscriminant.Phase335.maximalH_omega_not_even
