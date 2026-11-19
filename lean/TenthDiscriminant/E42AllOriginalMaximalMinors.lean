import TenthDiscriminant.E37GeneralIntegralGramCertificate

/-!
# E42 — Every maximal original evaluation minor inherits integral row factors

If a SAME-source integer rectangular evaluation matrix E has
a source-compatible unimodular row extraction
    U E = diag(d_i) F,
then EVERY n-column selected square minor of E has a product-d factor.
No selected minor is substituted for the full original Gram, and no
unmatched q-residue observer is imported.

A concrete real original-jets example Q={(1,0),(6,0),(11,0)},
D=25,J=1,R=3,S=1, has an exact original E and B with
E B Eᵀ = the original integer trace Gram. The mod5 source
minor vanishes but its mod7 source minor remains nonzero, showing
why p and an auxiliary q are different jobs.

No inference about Gaussian inertness of q=7, thin ellipses,
field class numbers or a new actual discriminant cutoff follows.
-/

namespace TenthDiscriminant.E42
set_option autoImplicit false
noncomputable section

/-- For every choice of n columns, a unimodular extraction of
the complete rectangular ORIGINAL evaluation E forces its
diagonal product to divide that particular maximal minor. -/
theorem all_maximal_minors_divisible
    {n m : Nat}
    (E F : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (d : Fin n → Int)
    (hU : E37.IntegerUnimodular U)
    (hE : U * E = Matrix.diagonal d * F)
    (pick : Fin n → Fin m) :
    (∏ i : Fin n, d i) ∣
      (E.submatrix id pick).det := by
  have hsub : U * (E.submatrix id pick) =
      Matrix.diagonal d * (F.submatrix id pick) := by
    ext i j
    have hpoint := congrArg
      (fun M : Matrix (Fin n) (Fin m) Int => M i (pick j)) hE
    simpa [Matrix.mul_apply, Matrix.submatrix] using hpoint
  have hd := congrArg Matrix.det hsub
  have hdet :
      U.det * (E.submatrix id pick).det =
        (∏ i : Fin n, d i) * (F.submatrix id pick).det := by
    simpa only [Matrix.det_mul, Matrix.det_diagonal] using hd
  rcases hU with hpos | hneg
  · refine ⟨(F.submatrix id pick).det, ?_⟩
    simpa [hpos] using hdet
  · refine ⟨-(F.submatrix id pick).det, ?_⟩
    have hn : - (E.submatrix id pick).det =
        (∏ i : Fin n, d i) * (F.submatrix id pick).det := by
      simpa [hneg] using hdet
    calc
      (E.submatrix id pick).det =
          - (-(E.submatrix id pick).det) := by ring
      _ = - ((∏ i : Fin n, d i) *
          (F.submatrix id pick).det) := by rw [hn]
      _ = (∏ i : Fin n, d i) *
          (-(F.submatrix id pick).det) := by ring

/-- A source p-extraction with positive p-content forbids a
nonzero maximal minor mod the SAME prime p. No statement is
made about the different auxiliary rank prime q. -/
theorem source_extraction_excludes_same_prime_full_rank_witness
    {n m : Nat}
    (E F : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (d : Fin n → Int)
    (hU : E37.IntegerUnimodular U)
    (hE : U * E = Matrix.diagonal d * F)
    (pick : Fin n → Fin m)
    (p : Int) (hp : p ∣ ∏ i : Fin n, d i) :
    p ∣ (E.submatrix id pick).det := by
  exact hp.trans (all_maximal_minors_divisible E F U d hU hE pick)

/-- Same original integer Q with ordinary Z derivatives j=0, and
same original column enumeration Q=(1,6,11) at D=25. -/
def sampleQ : Finset (Int × Int) :=
  {(1,0),(6,0),(11,0)}

def actualE : Matrix (Fin 3) (Fin 3) Int :=
  !![1,1,1;1,6,11;1,36,121]

def originalTraceB : Matrix (Fin 3) (Fin 3) Int :=
  Matrix.diagonal (fun _ : Fin 3 => (2 : Int))

def sourceU : Matrix (Fin 3) (Fin 3) Int :=
  !![1,0,0;-1,1,0;1,-2,1]

def sourceD : Fin 3 → Int :=
  fun i => if i = 0 then 1 else if i = 1 then 5 else 25

def sourceF : Matrix (Fin 3) (Fin 3) Int :=
  !![1,1,1;0,1,2;0,1,4]

theorem sourceU_is_integer_unimodular :
    E37.IntegerUnimodular sourceU := by
  left
  decide

theorem exact_original_evaluation_row_factor :
    sourceU * actualE = Matrix.diagonal sourceD * sourceF := by
  decide

/-- THIS equality verifies the actual complete three-row original
Gram, not an abstract E of convenient coordinates. No change to
original ordinary derivatives or the positive trace with factor 2. -/
theorem exact_original_evaluation_gram_identity :
    actualE * originalTraceB * actualE.transpose =
      integerRectangularTraceGram sampleQ 25 1 3 1 := by
  decide

theorem actual_source_det_via_evaluation :
    ((∏ i : Fin 3, sourceD i)^2) ∣
      (integerRectangularTraceGram sampleQ 25 1 3 1).det := by
  exact E37.original_jet_evaluation_factor
    sampleQ 25 1 3 1 3
    actualE sourceF originalTraceB sourceU sourceD
    sourceU_is_integer_unimodular
    exact_original_evaluation_gram_identity
    exact_original_evaluation_row_factor

/-- The same exact original square evaluation is invertible mod7
as witnessed by its integer determinant, but not mod5. -/
theorem original_evaluation_det_is_two_hundred_fifty :
    actualE.det = 250 := by
  decide

theorem same_source_two_prime_observer_control :
    ((5 : Int) ∣ actualE.det) ∧
      (¬ (7 : Int) ∣ actualE.det) := by
  rw [original_evaluation_det_is_two_hundred_fifty]
  decide

/-- This is a concrete internal source-matched, opposite-prime
control. It does NOT prove existence of inert auxiliary primes
with correct number-field hypotheses in the 307 proof. -/
theorem source_minor_five_factor_from_general_gate :
    (∏ i : Fin 3, sourceD i) ∣
      (actualE.submatrix id id).det := by
  exact all_maximal_minors_divisible actualE sourceF
    sourceU sourceD sourceU_is_integer_unimodular
    exact_original_evaluation_row_factor id

end
end TenthDiscriminant.E42

#print axioms TenthDiscriminant.E42.all_maximal_minors_divisible
#print axioms TenthDiscriminant.E42.source_extraction_excludes_same_prime_full_rank_witness
#print axioms TenthDiscriminant.E42.exact_original_evaluation_gram_identity
#print axioms TenthDiscriminant.E42.actual_source_det_via_evaluation
#print axioms TenthDiscriminant.E42.same_source_two_prime_observer_control
