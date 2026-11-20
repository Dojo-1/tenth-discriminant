import TenthDiscriminant.E41ComplexSourceSignObserver

/-!
# E42 — Complete three-moment signature of the original (1,Z) trace Gram

For any FINITE original integer-pair sample support Q, D : Nat,
and original ordinary-Z jets J=1, rectangular rows R=2,S=1,
the COMPLETE integer trace Gram depends on exactly three moments:

 N = card Q
 X = sum_{(x,y) in Q} x
 T = sum_{(x,y) in Q} (x*x + D*y*y).

The source remains the original Q, with no selected minor, auxiliary
Gram, floating substitution, or changed positive trace.
  G = 2 [[N,X],[X,T]]
  det G = 4 (N*T - X^2).

Conjugate-sign ambiguities are not intrinsic curvature and are not
conductor kernels: they are fibers of THIS finite observation map.
The general global conjugation theorem was already established in
ObservationConjugation.lean; E42 does not claim its novelty.

No class-number/307^4 improvement or ETH hardness theorem follows.
-/

namespace TenthDiscriminant.E42
set_option autoImplicit false
noncomputable section

def originalRealMoment (Q : Finset (Int × Int)) : Int :=
  Q.sum (fun q => q.1)

def originalNormMoment (Q : Finset (Int × Int)) (D : Nat) : Int :=
  Q.sum (fun q => q.1*q.1+(D : Int)*q.2*q.2)

/-- The entire real-coefficient 2x2 trace Gram is determined by
the original source's count, real sum and positive norm sum. -/
theorem original_source_moment_gram
    (Q : Finset (Int × Int)) (D : Nat) :
    integerRectangularTraceGram Q D 1 2 1 =
    !![2*(Q.card : Int), 2*originalRealMoment Q;
       2*originalRealMoment Q, 2*originalNormMoment Q D] := by
  classical
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [integerRectangularTraceGram, integerTraceGramMatrix,
      integerTraceGramEntry, integerDerivativeRow, integerPairTrace,
      pairPow, pairMul, pairScale, pairConj,
      originalRealMoment, originalNormMoment,
      Finset.sum_range_succ, Finset.mul_sum,
      Finset.sum_add_distrib] <;> ring
  all_goals
    simp only [Finset.sum_add_distrib, Finset.sum_mul]

/-- Full ORIGINAL determinant, with no loss of the sample cardinality
or y² channel. Works for empty Q and singletons as well. -/
theorem original_source_moment_det
    (Q : Finset (Int × Int)) (D : Nat) :
    (integerRectangularTraceGram Q D 1 2 1).det =
      4 * ((Q.card : Int)*originalNormMoment Q D -
         (originalRealMoment Q)^2) := by
  rw [original_source_moment_gram Q D]
  simp [Matrix.det_fin_two]
  ring

/-- Same three original integer moments imply identical full
observed Gram. This is the source-to-observation information loss
contract; it does NOT assert that the source supports are equal. -/
theorem equal_moments_same_full_original_gram
    (Q P : Finset (Int × Int)) (D : Nat)
    (hcard : Q.card = P.card)
    (hreal : originalRealMoment Q = originalRealMoment P)
    (hnorm : originalNormMoment Q D = originalNormMoment P D) :
    integerRectangularTraceGram Q D 1 2 1 =
      integerRectangularTraceGram P D 1 2 1 := by
  rw [original_source_moment_gram Q D,
    original_source_moment_gram P D,
    hcard, hreal, hnorm]

/-- Conversely the full observed Gram determines all three
moments (over the integers, where multiplying by two is injective). -/
theorem original_gram_equal_iff_moments
    (Q P : Finset (Int × Int)) (D : Nat) :
    integerRectangularTraceGram Q D 1 2 1 =
      integerRectangularTraceGram P D 1 2 1 ↔
      Q.card = P.card ∧
      originalRealMoment Q = originalRealMoment P ∧
      originalNormMoment Q D = originalNormMoment P D := by
  constructor
  · intro hg
    rw [original_source_moment_gram Q D,
      original_source_moment_gram P D] at hg
    have h00 := congrArg (fun M : Matrix (Fin 2) (Fin 2) Int => M 0 0) hg
    have h01 := congrArg (fun M : Matrix (Fin 2) (Fin 2) Int => M 0 1) hg
    have h11 := congrArg (fun M : Matrix (Fin 2) (Fin 2) Int => M 1 1) hg
    simp at h00 h01 h11
    constructor
    · exact_mod_cast (show (Q.card : Int) = P.card by omega)
    constructor
    · omega
    · omega
  · rintro ⟨hc,hr,hn⟩
    exact equal_moments_same_full_original_gram Q P D hc hr hn

/-- Even one nonreal point supplies two independent real trace
channels; this is different from one real point, which is rank-one
at most under the same 1,Z observation rows. -/
theorem one_nonreal_point_det (D : Nat) :
    (integerRectangularTraceGram {(0,1)} D 1 2 1).det =
      4 * (D : Int) := by
  rw [original_source_moment_det]
  simp [originalRealMoment, originalNormMoment]

theorem one_real_point_det (D : Nat) :
    (integerRectangularTraceGram {(0,0)} D 1 2 1).det = 0 := by
  rw [original_source_moment_det]
  simp [originalRealMoment, originalNormMoment]

/-- E41 partial sign collision is exactly a collision of the THREE
moments; global source conjugation is NOT the only way two finite
supports can share this coarse observation. -/
theorem partial_sign_collision_is_moment_collision :
    E41.complexTwoSource 0 1 1 1 ≠ E41.complexTwoSource 0 1 1 (-1) ∧
    originalRealMoment (E41.complexTwoSource 0 1 1 1) =
      originalRealMoment (E41.complexTwoSource 0 1 1 (-1)) ∧
    originalNormMoment (E41.complexTwoSource 0 1 1 1) 3 =
      originalNormMoment (E41.complexTwoSource 0 1 1 (-1)) 3 := by
  decide

end
end TenthDiscriminant.E42

#print axioms TenthDiscriminant.E42.original_source_moment_gram
#print axioms TenthDiscriminant.E42.original_source_moment_det
#print axioms TenthDiscriminant.E42.original_gram_equal_iff_moments
#print axioms TenthDiscriminant.E42.one_nonreal_point_det
#print axioms TenthDiscriminant.E42.partial_sign_collision_is_moment_collision
