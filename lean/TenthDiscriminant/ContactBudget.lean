import TenthDiscriminant.SylvesterDegree

/-!
# Sum the local multiplicities without erasing nonvanishing

Distinct parameter points are a Finset. A nonzero determinant polynomial is an
explicit hypothesis, not an inferred consequence of an upper degree bound.
Irreducibility-to-nonzero-determinant and global jet uniqueness remain open.
-/
namespace TenthDiscriminant
open Polynomial Matrix
open scoped BigOperators
noncomputable section
variable {K : Type*} [Field K]

/-- Distinct root-power divisors of a nonzero polynomial spend its degree. -/
theorem polynomial_distinct_root_power_budget
    (E : Polynomial K) (hE : E ≠ 0) (s : Finset K) (m : K -> Nat)
    (h : forall w, w ∈ s -> (Polynomial.X - Polynomial.C w)^(m w) ∣ E) :
    s.sum m <= E.natDegree := by
  classical
  have hc (w : K) (hw : w ∈ s) : m w <= E.roots.count w := by
    have hh := Multiset.count_le_of_le w (Polynomial.roots.le_of_dvd hE (h w hw))
    simpa only [Polynomial.roots_pow, Polynomial.roots_X_sub_C,
      Multiset.count_nsmul, Multiset.count_singleton_self, mul_one] using hh
  have hs : s.sum (fun w => E.roots.count w) <=
      E.roots.toFinset.sum (fun w => E.roots.count w) := by
    calc
      _ <= (s ∪ E.roots.toFinset).sum (fun w => E.roots.count w) :=
        Finset.sum_le_sum_of_subset_of_nonneg Finset.subset_union_left
          (fun w hw hn => Nat.zero_le _)
      _ = E.roots.toFinset.sum (fun w => E.roots.count w) := by
        symm
        apply Finset.sum_subset Finset.subset_union_right
        intro w hw hn
        have hnot : w ∉ E.roots := by simpa using hn
        exact Multiset.count_eq_zero.mpr hnot
  calc
    s.sum m <= s.sum (fun w => E.roots.count w) := Finset.sum_le_sum hc
    _ <= E.roots.toFinset.sum (fun w => E.roots.count w) := hs
    _ = E.roots.card := Multiset.toFinset_sum_count_eq _
    _ <= E.natDegree := Polynomial.card_roots' E

/-- Combine the existing local theorem with the actual determinant degree bound. -/
theorem fixedDerivativeSylvester_contact_sum
    (F : Polynomial (Polynomial K)) (a b : Nat)
    (hZ : F.natDegree <= a)
    (hW : forall i, (F.coeff i).natDegree <= b)
    (hE : (fixedSylvesterMatrix F F.derivative a (a-1)).det ≠ 0)
    (s : Finset K) (z : K -> K) (m : K -> Nat)
    (hspecial : forall w, w ∈ s -> F.map (Polynomial.evalRingHom w) ≠ 0)
    (hroot : forall w, w ∈ s ->
      (Polynomial.X - Polynomial.C (z w))^(m w) ∣ F.map (Polynomial.evalRingHom w)) :
    s.sum (fun w => m w - 1) <= (a+(a-1))*b := by
  have hdiv (w : K) (hw : w ∈ s) :
      (Polynomial.X - Polynomial.C w)^(m w-1) ∣
        (fixedSylvesterMatrix F F.derivative a (a-1)).det :=
    fixedDerivativeSylvester_multiplicity_at_nonzero F a hZ w (z w) (m w)
      (hspecial w hw) (hroot w hw)
  exact (polynomial_distinct_root_power_budget _ hE s (fun w => m w-1) hdiv).trans
    (fixedDerivativeSylvester_natDegree_le F a b hW)

/-- At most 2a-1 excessive contacts, provided the SAME determinant is nonzero. -/
theorem fixedDerivativeSylvester_excessive_contact_card
    (F : Polynomial (Polynomial K)) (a b : Nat) (ha : 1 <= a) (hb : 0 < b)
    (hZ : F.natDegree <= a)
    (hW : forall i, (F.coeff i).natDegree <= b)
    (hE : (fixedSylvesterMatrix F F.derivative a (a-1)).det ≠ 0)
    (s : Finset K) (z : K -> K) (m : K -> Nat)
    (hspecial : forall w, w ∈ s -> F.map (Polynomial.evalRingHom w) ≠ 0)
    (hroot : forall w, w ∈ s ->
      (Polynomial.X - Polynomial.C (z w))^(m w) ∣ F.map (Polynomial.evalRingHom w))
    (hcontact : forall w, w ∈ s -> b < m w) :
    s.card <= 2*a-1 := by
  have hs := fixedDerivativeSylvester_contact_sum F a b hZ hW hE s z m hspecial hroot
  have hl : s.card*b <= s.sum (fun w => m w-1) := by
    calc
      s.card*b = s.sum (fun _ => b) := by simp
      _ <= s.sum (fun w => m w-1) := by
        apply Finset.sum_le_sum
        intro w hw
        have hh := hcontact w hw
        omega
  have hn : a+(a-1) = 2*a-1 := by omega
  rw [hn] at hs
  by_contra! hbad
  have hstep : 2*a-1+1 <= s.card := by omega
  nlinarith

end
end TenthDiscriminant
