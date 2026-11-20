import TenthDiscriminant.E14MovingFrameJet

/-!
# E24: arithmetic worldlet transport -- exact original trace-Gram and integral remainder

For D>0 and positive k, this models the index-k inclusion of selected
quadratic orders Z[sqrt(-D*k*k)] into Z[sqrt(-D)] via (x,y)->(x,k*y).
For D=0, pairMul 0 is a DEGENERATE formal dual-number pair algebra,
not the quadratic number field Z[sqrt(0)]. The verified algebraic pair
identities still hold, but NO field/order interpretation is asserted.

It transports the integer rectangular trace Gram *exactly* if, and
only if for the asserted identity, the observation support is the
image under the same embedding. It does NOT identify the transported
support with all integer points in the destination presentation.

D=1, k=2 illustrates Z[2i] contained properly in Z[i].
Neither D=4 nor its nonmaximal order is an eligible imaginary
quadratic fundamental-discriminant field parameter in the 300^4 result.
We do not claim a new bound or a field isomorphism for unrelated D.
-/

namespace TenthDiscriminant.E24

open scoped BigOperators
set_option autoImplicit false
noncomputable section

/-- Map from Z[sqrt(-(D*k*k))] into Z[sqrt(-D)] on original integer pairs. -/
def squareOrderEmbed (k : Nat) (p : Int × Int) : Int × Int :=
  (p.1, (k : Int) * p.2)

/-- Additive and multiplicative source structure must both be transported. -/
theorem squareOrderEmbed_add (k : Nat) (a b : Int × Int) :
    squareOrderEmbed k (a.1+b.1, a.2+b.2) =
      ((squareOrderEmbed k a).1+(squareOrderEmbed k b).1,
       (squareOrderEmbed k a).2+(squareOrderEmbed k b).2) := by
  apply Prod.ext <;> simp [squareOrderEmbed] <;> ring

theorem squareOrderEmbed_one (k : Nat) :
    squareOrderEmbed k (1, 0) = (1, 0) := by
  simp [squareOrderEmbed]

/-- Exact algebraic coherence of the TWO different source multiplication laws. -/
theorem squareOrderEmbed_mul (D k : Nat) (a b : Int × Int) :
    squareOrderEmbed k (pairMul (D*k*k) a b) =
      pairMul D (squareOrderEmbed k a) (squareOrderEmbed k b) := by
  apply Prod.ext <;>
    simp [squareOrderEmbed, pairMul] <;>
    push_cast <;> ring

theorem squareOrderEmbed_conj (k : Nat) (a : Int × Int) :
    squareOrderEmbed k (pairConj a) =
      pairConj (squareOrderEmbed k a) := by
  apply Prod.ext <;> simp [squareOrderEmbed, pairConj] <;> ring

theorem squareOrderEmbed_scale (k : Nat) (c : Int) (a : Int × Int) :
    squareOrderEmbed k (pairScale c a) =
      pairScale c (squareOrderEmbed k a) := by
  apply Prod.ext <;> simp [squareOrderEmbed, pairScale] <;> ring

/-- Preservation of every original algebraic power, not just finite tests. -/
theorem squareOrderEmbed_pow (D k : Nat) (a : Int × Int) (n : Nat) :
    squareOrderEmbed k (pairPow (D*k*k) a n) =
      pairPow D (squareOrderEmbed k a) n := by
  induction n with
  | zero =>
      simp [pairPow, squareOrderEmbed]
  | succ n ih =>
      change squareOrderEmbed k (pairMul (D*k*k)
          (pairPow (D*k*k) a n) a) =
        pairMul D (pairPow D (squareOrderEmbed k a) n)
          (squareOrderEmbed k a)
      rw [squareOrderEmbed_mul, ih]

/-- Every ORIGINAL ordinary derivative order is transported.
Neither Hasse jets nor new rectangular rows have been substituted. -/
theorem squareOrderEmbed_ordinary_jet
    (D k r s j : Nat) (p : Int × Int) :
    squareOrderEmbed k (integerDerivativeRow (D*k*k) r s j p) =
      integerDerivativeRow D r s j (squareOrderEmbed k p) := by
  by_cases hj : j ≤ r
  · simp only [integerDerivativeRow, if_pos hj]
    rw [squareOrderEmbed_scale, squareOrderEmbed_mul,
      squareOrderEmbed_pow, squareOrderEmbed_pow,
      squareOrderEmbed_conj]
  · simp [integerDerivativeRow, hj, squareOrderEmbed]

/-- EXACT original source trace pairing, not a Euclidean surrogate. -/
theorem squareOrderEmbed_pairTrace
    (D k : Nat) (a b : Int × Int) :
    integerPairTrace D (squareOrderEmbed k a) (squareOrderEmbed k b) =
      integerPairTrace (D*k*k) a b := by
  simp [integerPairTrace, squareOrderEmbed]
  push_cast
  ring

theorem squareOrderEmbed_injective (k : Nat) (hk : 0 < k) :
    Function.Injective (squareOrderEmbed k) := by
  intro a b h
  apply Prod.ext
  · have hh := congrArg (fun p : Int × Int => p.1) h
    simpa [squareOrderEmbed] using hh
  · have hh := congrArg (fun p : Int × Int => p.2) h
    change (k : Int)*a.2 = (k : Int)*b.2 at hh
    have hne : (k : Int) ≠ 0 := by
      exact_mod_cast (Nat.ne_of_gt hk)
    exact mul_left_cancel₀ hne hh

/-- Exact image of the index-two embedding; the missing coset is real. -/
theorem squareOrderEmbed_two_image (p : Int × Int) :
    (∃ q, squareOrderEmbed 2 q = p) ↔
      (∃ z : Int, p.2 = 2*z) := by
  constructor
  · rintro ⟨q, hq⟩
    refine ⟨q.2, ?_⟩
    have hh := congrArg (fun r : Int × Int => r.2) hq
    dsimp [squareOrderEmbed] at hh
    omega
  · rintro ⟨z, hz⟩
    refine ⟨(p.1,z), ?_⟩
    apply Prod.ext
    · rfl
    · dsimp [squareOrderEmbed]
      omega

theorem squareOrderEmbed_two_not_surjective :
    ¬ Function.Surjective (squareOrderEmbed 2) := by
  intro hs
  obtain ⟨q,hq⟩ := hs (0,1)
  have hh := congrArg (fun r : Int × Int => r.2) hq
  dsimp [squareOrderEmbed] at hh
  omega

/-- Every target sample with an odd second coordinate is genuinely
absent from ANY image support, no matter how large the source support. -/
theorem target_odd_node_not_in_embedded_support
    (Q : Finset (Int × Int)) :
    (0,1) ∉ Q.image (squareOrderEmbed 2) := by
  classical
  intro h
  rcases Finset.mem_image.mp h with ⟨p,hp,hq⟩
  have hh := congrArg (fun r : Int × Int => r.2) hq
  dsimp [squareOrderEmbed] at hh
  omega

/-- Original source entry equality: SAME derivatives, SAME trace,
SAME observation support moved along the integral embedding. -/
theorem squareOrderEmbed_traceGramEntry
    (Q : Finset (Int × Int)) (D k J r s t u : Nat) (hk : 0 < k) :
    integerTraceGramEntry (Q.image (squareOrderEmbed k))
      D J r s t u =
    integerTraceGramEntry Q (D*k*k) J r s t u := by
  classical
  unfold integerTraceGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.sum_image (squareOrderEmbed_injective k hk).injOn]
  apply Finset.sum_congr rfl
  intro p hp
  simpa only [squareOrderEmbed_ordinary_jet] using
    (squareOrderEmbed_pairTrace D k
      (integerDerivativeRow (D*k*k) r s j p)
      (integerDerivativeRow (D*k*k) t u j p))

/-- All matrix entries match on the correctly transported source set. -/
theorem squareOrderEmbed_traceGramMatrix
    {n : Nat} (Q : Finset (Int × Int)) (D k J : Nat)
    (rows : Fin n → Nat × Nat) (hk : 0 < k) :
    integerTraceGramMatrix (Q.image (squareOrderEmbed k))
      D J rows =
    integerTraceGramMatrix Q (D*k*k) J rows := by
  ext a b
  exact squareOrderEmbed_traceGramEntry Q D k J
    (rows a).1 (rows a).2 (rows b).1 (rows b).2 hk

/-- The WHOLE original rectangular, ordinary-jet integer Gram
is transported exactly; the row-major enumeration is preserved. -/
theorem squareOrderEmbed_originalGram
    (Q : Finset (Int × Int)) (D k J R S : Nat) (hk : 0 < k) :
    integerRectangularTraceGram
      (Q.image (squareOrderEmbed k)) D J R S =
    integerRectangularTraceGram Q (D*k*k) J R S := by
  unfold integerRectangularTraceGram
  exact squareOrderEmbed_traceGramMatrix Q D k J _ hk

theorem squareOrderEmbed_originalGram_det
    (Q : Finset (Int × Int)) (D k J R S : Nat) (hk : 0 < k) :
    (integerRectangularTraceGram
      (Q.image (squareOrderEmbed k)) D J R S).det =
    (integerRectangularTraceGram Q (D*k*k) J R S).det := by
  rw [squareOrderEmbed_originalGram Q D k J R S hk]

/-- The trace pairing on the canonical integral pair basis.
This is the POSITIVE trace-with-conjugation matrix, not by itself
the signed field discriminant. -/
def sourceBasisTraceGram (D : Nat) : Matrix (Fin 2) (Fin 2) Int :=
  !![integerPairTrace D (1,0) (1,0),
      integerPairTrace D (1,0) (0,1);
      integerPairTrace D (0,1) (1,0),
      integerPairTrace D (0,1) (0,1)]

theorem sourceBasisTraceGram_closed (D : Nat) :
    sourceBasisTraceGram D = !![2,0;0,2*(D : Int)] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [sourceBasisTraceGram, integerPairTrace]

theorem sourceBasisTraceGram_det (D : Nat) :
    (sourceBasisTraceGram D).det = 4*(D : Int) := by
  rw [sourceBasisTraceGram_closed]
  simp [Matrix.det_fin_two]
  ring

/-- Under the index-k embedding, the *basis presentation* of the
integer trace determinant changes by the square of the index. This
does not contradict matched-support Gram invariance above. -/
theorem sourceBasis_det_square_index (D k : Nat) :
    (sourceBasisTraceGram (D*k*k)).det =
      (k : Int)^2 * (sourceBasisTraceGram D).det := by
  rw [sourceBasisTraceGram_det, sourceBasisTraceGram_det]
  push_cast
  ring

/-- The direct E14 coordinate normalization is the same index-two
issue up to conjugation: signs must also be transported. -/
theorem E14_index_two_chart_dictionary (p : Int × Int) :
    E14.frameIntegralCoordinates p =
      squareOrderEmbed 2 (pairConj p) := by
  apply Prod.ext <;> simp [E14.frameIntegralCoordinates,
    squareOrderEmbed,pairConj] <;> ring

/-- A real/rational quadratic-form equivalence can exist even where
there is no integral-lattice equivalence. -/
def rationalQuadraticForm (D : Nat) (p : Rat × Rat) : Rat :=
  p.1*p.1 + (D : Rat)*p.2*p.2

def rationalDown (p : Rat × Rat) : Rat × Rat := (p.1,p.2/2)
def rationalUp (p : Rat × Rat) : Rat × Rat := (p.1,2*p.2)

theorem rationalDown_up (p : Rat × Rat) :
    rationalDown (rationalUp p) = p := by
  cases p with
  | mk x y =>
      apply Prod.ext <;> simp [rationalDown,rationalUp] <;> ring

theorem rationalUp_down (p : Rat × Rat) :
    rationalUp (rationalDown p) = p := by
  cases p with
  | mk x y =>
      apply Prod.ext <;> simp [rationalDown,rationalUp] <;> ring

theorem rationalQuadraticForm_isometry (p : Rat × Rat) :
    rationalQuadraticForm 4 (rationalDown p) =
      rationalQuadraticForm 1 p := by
  cases p with
  | mk x y =>
      simp [rationalQuadraticForm, rationalDown]
      ring

/-- Membership in the ORIGINAL coordinate lattice, not a property
of the ambient rational vector space. -/
def IsIntegralPair (p : Rat × Rat) : Prop :=
  ∃ q : Int × Int, p = ((q.1 : Rat),(q.2 : Rat))

theorem rationalDown_loses_integral_witness :
    ¬ IsIntegralPair (rationalDown (0,1)) := by
  rintro ⟨q,hq⟩
  have hy := congrArg (fun p : Rat × Rat => p.2) hq
  have hhalf : (q.2 : Rat) = (1/2 : Rat) := by
    simpa [rationalDown] using hy.symm
  have hRat : (2 : Rat)*(q.2 : Rat) = 1 := by
    linarith only [hhalf]
  have hInt : (2*q.2 : Int) = 1 := by exact_mod_cast hRat
  omega


/-- D=0 is a formal pair algebra with a nonzero nilpotent.
No field or reduced quadratic-order reading is justified at D=0. -/
theorem degenerate_pair_algebra_nonzero_nilpotent :
    pairMul 0 (0,1) (0,1) = (0,0) ∧
      ((0,1) : Int × Int) ≠ (0,0) := by
  constructor <;> decide

end
end TenthDiscriminant.E24

#print axioms TenthDiscriminant.E24.squareOrderEmbed_ordinary_jet
#print axioms TenthDiscriminant.E24.squareOrderEmbed_originalGram
#print axioms TenthDiscriminant.E24.squareOrderEmbed_originalGram_det
#print axioms TenthDiscriminant.E24.sourceBasis_det_square_index
#print axioms TenthDiscriminant.E24.target_odd_node_not_in_embedded_support
#print axioms TenthDiscriminant.E24.rationalQuadraticForm_isometry
#print axioms TenthDiscriminant.E24.rationalDown_loses_integral_witness
#print axioms TenthDiscriminant.E24.degenerate_pair_algebra_nonzero_nilpotent
