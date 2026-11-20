import TenthDiscriminant.E44LabelledCRTObserverRefinement
import TenthDiscriminant.LatticeEllipse

/-!
# E45 - Saturated ellipse, source rigidity, and vanishing aggregate orientation probe

The original COMPLETE ellipse is closed under pair conjugation.
On such a finite support, independently conjugating points cannot
produce a NEW support if the finite image map is injective.

The imaginary-coordinate sum of the complete source is identically
zero. Consequently the E44 Gaussian (D=1) *aggregated* labelled-prime
gap, which equals four times this sum in ZMod 5, vanishes.

These are SOURCE facts. They do not modify the original jets, trace
metric, Gram, field chart, or discriminant bound. A nontrivial
sample-by-sample oriented observer remains a different instrument.
-/

namespace TenthDiscriminant.E45
set_option autoImplicit false
noncomputable section

/-- The SAME integer ellipse contains the conjugate of every sample.
We use the existing full-ellipse membership lemma; no replacement
sampling region is introduced. -/
theorem ellipse_conjugate_mem
    (D rho : Nat) (hD : 0 < D) (q : Int × Int)
    (hq : q ∈ ellipsePairs D rho) :
    pairConj q ∈ ellipsePairs D rho := by
  rcases q with ⟨x, y⟩
  change (x, -y) ∈ ellipsePairs D rho
  apply (mem_ellipsePairs_iff D rho hD x (-y)).2
  have h := (mem_ellipsePairs_iff D rho hD x y).1 hq
  simpa [pow_two] using h

/-- No exotic frame: global conjugation is a bijection of the
unchanged finite ellipse to ITSELF. -/
theorem ellipse_conjugate_image_eq
    (D rho : Nat) (hD : 0 < D) :
    (ellipsePairs D rho).image pairConj = ellipsePairs D rho := by
  classical
  apply Finset.ext
  intro q
  constructor
  · intro hq
    rcases Finset.mem_image.mp hq with ⟨p, hp, rfl⟩
    exact ellipse_conjugate_mem D rho hD p hp
  · intro hq
    exact Finset.mem_image.mpr
      ⟨pairConj q, ellipse_conjugate_mem D rho hD q hq,
       pairConj_twice q⟩

/-- A general finite, conjugation-saturated source has NO distinct
injectively pointwise-conjugated image. The map may exchange pair
elements, but its image support is unchanged. -/
theorem closed_support_injective_toggle_preserves_support
    (Q : Finset (Int × Int))
    (hclosed : ∀ q ∈ Q, pairConj q ∈ Q)
    (f : Int × Int → Int × Int)
    (hinj : Set.InjOn f Q)
    (hflip : ∀ q ∈ Q, f q = q ∨ f q = pairConj q) :
    Q.image f = Q := by
  classical
  apply Finset.ext
  intro q
  constructor
  · intro hm
    rcases Finset.mem_image.mp hm with ⟨u, hu, rfl⟩
    rcases hflip u hu with hs | hc
    · simpa [hs] using hu
    · simpa [hc] using hclosed u hu
  · intro hq
    rcases hflip q hq with hs | hc
    · exact Finset.mem_image.mpr ⟨q, hq, hs⟩
    · have hqc : pairConj q ∈ Q := hclosed q hq
      rcases hflip (pairConj q) hqc with hself | hconj
      · have hsame : q = pairConj q :=
          hinj hq hqc (hc.trans hself.symm)
        exact Finset.mem_image.mpr ⟨q, hq, hc.trans hsame.symm⟩
      · exact Finset.mem_image.mpr
          ⟨pairConj q, hqc, by simpa only [pairConj_twice] using hconj⟩

theorem ellipse_injective_partial_conjugation_no_new_source
    (D rho : Nat) (hD : 0 < D)
    (f : Int × Int → Int × Int)
    (hinj : Set.InjOn f (ellipsePairs D rho))
    (hflip : ∀ q ∈ ellipsePairs D rho,
      f q = q ∨ f q = pairConj q) :
    (ellipsePairs D rho).image f = ellipsePairs D rho := by
  exact closed_support_injective_toggle_preserves_support
    (ellipsePairs D rho)
    (fun q hq => ellipse_conjugate_mem D rho hD q hq) f hinj hflip

/-- The original full ellipse has no aggregate imaginary orientation. -/
theorem ellipse_imaginary_sum_zero
    (D rho : Nat) (hD : 0 < D) :
    (ellipsePairs D rho).sum (fun q => q.2) = (0 : Int) := by
  classical
  let Q : Finset (Int × Int) := ellipsePairs D rho
  have himage : Q.image pairConj = Q :=
    ellipse_conjugate_image_eq D rho hD
  have hs : Q.sum (fun q => q.2) =
      -(Q.sum (fun q => q.2)) := by
    calc
      Q.sum (fun q => q.2) =
          (Q.image pairConj).sum (fun q => q.2) := by rw [himage]
      _ = Q.sum (fun q => (pairConj q).2) := by
        rw [Finset.sum_image pairConj_injective.injOn]
      _ = -(Q.sum (fun q => q.2)) := by
        simp [pairConj, Finset.sum_neg_distrib]
  change Q.sum (fun q => q.2) = 0
  omega

/-- The E44 *Gaussian* aggregate probe collapses on its own
complete original D=1 ellipse. The split-prime labels are NOT
transported to an arbitrary D. -/
theorem gaussian_full_ellipse_total_prime_gap_zero
    (rho : Nat) :
    E44.totalPrimeGap (ellipsePairs 1 rho) = 0 := by
  rw [E44.total_prime_gap_is_imag_moment_mod5]
  have hs : (ellipsePairs 1 rho).sum (fun q => q.2) = (0 : Int) :=
    ellipse_imaginary_sum_zero 1 rho (by decide)
  have hcast :
      (ellipsePairs 1 rho).sum (fun q => (q.2 : ZMod 5)) = 0 := by
    calc
      (ellipsePairs 1 rho).sum (fun q => (q.2 : ZMod 5)) =
          (((ellipsePairs 1 rho).sum (fun q => q.2) : Int) : ZMod 5) := by
            simp
      _ = 0 := by rw [hs]; rfl
  rw [hcast]
  ring

/-- Positive control: the sparse example retains a NONZERO gap;
the full-ellipse zero result is not a claim that E44's gap is
identically zero for all finite supports. -/
theorem sparse_gap_not_universally_zero :
    E44.totalPrimeGap (E41.complexTwoSource 0 1 1 1) = 3 :=
  E44.labelled_prime_gap_distinguishes_partial_sign_sources.1

end
end TenthDiscriminant.E45

#print axioms TenthDiscriminant.E45.ellipse_conjugate_mem
#print axioms TenthDiscriminant.E45.ellipse_conjugate_image_eq
#print axioms TenthDiscriminant.E45.closed_support_injective_toggle_preserves_support
#print axioms TenthDiscriminant.E45.ellipse_injective_partial_conjugation_no_new_source
#print axioms TenthDiscriminant.E45.ellipse_imaginary_sum_zero
#print axioms TenthDiscriminant.E45.gaussian_full_ellipse_total_prime_gap_zero
