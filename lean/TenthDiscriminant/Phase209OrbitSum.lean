import TenthDiscriminant.ObservationConjugation

/-!
Phase209: the FINITE-SUM combinatorial bridge from an original
conjugation-stable Q to real samples and positive-imaginary representatives.

This is a whole-finite-set statement, not a numerical sample and not
a residue-class collapse. The extra per-jet source trace formula is in
Phase209ConjugateFold; assembling full matrix/weighted Cauchy-Binet
still requires additional Lean proofs.
-/
namespace TenthDiscriminant.Phase209OrbitSum

open TenthDiscriminant

/-- A conjugation-even integer summand over Q can be folded exactly:
each nonreal orbit occurs twice, with a unique positive-imaginary
representative; real fixed points occur once. -/
theorem sum_conjugate_orbits
    (Q : Finset (Int × Int))
    (hQ : ∀ q : Int × Int, q ∈ Q ↔ pairConj q ∈ Q)
    (f : Int × Int → Int)
    (hf : ∀ q, f (pairConj q) = f q) :
    (∑ q ∈ Q, f q) =
       (∑ q ∈ Q.filter (fun q => q.2 = 0), f q) +
          2 * (∑ q ∈ Q.filter (fun q => 0 < q.2), f q) := by
  classical
  have hnegpos :
      (∑ q ∈ Q.filter (fun q => q.2 < 0), f q) =
      (∑ q ∈ Q.filter (fun q => 0 < q.2), f q) := by
    apply Finset.sum_bij (fun q _ => pairConj q)
    · intro q hq
      rcases Finset.mem_filter.mp hq with ⟨hqQ, hn⟩
      apply Finset.mem_filter.mpr
      constructor
      · exact (hQ q).mp hqQ
      · simpa [pairConj] using (show 0 < -q.2 by omega)
    · intro q hq q' hq' eq
      exact pairConj_injective eq
    · intro q hq
      rcases Finset.mem_filter.mp hq with ⟨hqQ, hp⟩
      refine ⟨pairConj q, ?_, ?_⟩
      · apply Finset.mem_filter.mpr
        constructor
        · exact (hQ q).mp hqQ
        · simpa [pairConj] using (show -q.2 < 0 by omega)
      · exact pairConj_twice q
    · intro q hq
      exact (hf q).symm
  have hnonneg_zero :
      (Q.filter (fun q => ¬ q.2 < 0)).filter (fun q => q.2 = 0) =
        Q.filter (fun q => q.2 = 0) := by
    ext q
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨⟨hq, hn⟩, hz⟩
      exact ⟨hq, hz⟩
    · rintro ⟨hq, hz⟩
      exact ⟨⟨hq, by omega⟩, hz⟩
  have hnonneg_pos :
      (Q.filter (fun q => ¬ q.2 < 0)).filter (fun q => ¬ q.2 = 0) =
        Q.filter (fun q => 0 < q.2) := by
    ext q
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨⟨hq, hn⟩, hz⟩
      exact ⟨hq, by omega⟩
    · rintro ⟨hq, hp⟩
      exact ⟨⟨hq, by omega⟩, by omega⟩
  have hs1 :
      (∑ q ∈ Q, f q) =
        (∑ q ∈ Q.filter (fun q => q.2 < 0), f q) +
        (∑ q ∈ Q.filter (fun q => ¬ q.2 < 0), f q) := by
    exact (Finset.sum_filter_add_sum_filter_not
      (s := Q) (p := fun q : Int × Int => q.2 < 0) (f := f)).symm
  have hs2 :
      (∑ q ∈ Q.filter (fun q => ¬ q.2 < 0), f q) =
      (∑ q ∈ Q.filter (fun q => q.2 = 0), f q) +
      (∑ q ∈ Q.filter (fun q => 0 < q.2), f q) := by
    have h := Finset.sum_filter_add_sum_filter_not
      (s := Q.filter (fun q => ¬ q.2 < 0))
      (p := fun q : Int × Int => q.2 = 0) (f := f)
    rw [hnonneg_zero, hnonneg_pos] at h
    exact h.symm
  rw [hs1, hs2, hnegpos]
  ring


/-- The ORIGINAL source support (the complete thin ellipse) is invariant
under conjugating the integer-pair observation; no residue substitution. -/
theorem original_ellipse_conjugation (D rho : Nat) (hD : 0 < D)
    (q : Int × Int) :
    q ∈ ellipsePairs D rho ↔ pairConj q ∈ ellipsePairs D rho := by
  rcases q with ⟨x, y⟩
  simpa [pairConj, mem_ellipsePairs_iff D rho hD]

/-- Specialize the general orbit formula to the ORIGINAL complete ellipse.
This identifies exactly N=|Q| effective per-jet observation channels when
paired with Phase209ConjugateFold; determinant transport remains separate. -/
theorem sum_original_ellipse_orbits (D rho : Nat) (hD : 0 < D)
    (f : Int × Int → Int)
    (hf : ∀ q, f (pairConj q) = f q) :
    (∑ q ∈ ellipsePairs D rho, f q) =
      (∑ q ∈ (ellipsePairs D rho).filter (fun q => q.2 = 0), f q) +
        2 * (∑ q ∈ (ellipsePairs D rho).filter (fun q => 0 < q.2), f q) :=
  sum_conjugate_orbits (ellipsePairs D rho)
    (original_ellipse_conjugation D rho hD) f hf

end TenthDiscriminant.Phase209OrbitSum

#print axioms TenthDiscriminant.Phase209OrbitSum.sum_conjugate_orbits
#print axioms TenthDiscriminant.Phase209OrbitSum.sum_original_ellipse_orbits
