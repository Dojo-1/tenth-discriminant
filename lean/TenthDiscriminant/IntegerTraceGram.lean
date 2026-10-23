import TenthDiscriminant.LatticeEllipse

/-!
# Integer coordinates for the existing trace-Gram matrix

The pair `(x,y)` denotes `x + y √(-D)`. This is the selected lattice used by
the verifier, not a claim about the full ring of integers. The definitions below
retain the original derivative order, factor two, and rectangular row order.
-/
namespace TenthDiscriminant
open scoped ComplexConjugate

/-- Multiplication in the selected integer-pair lattice. -/
def pairMul (D : Nat) (a b : Int × Int) : Int × Int :=
  (a.1 * b.1 - (D : Int) * a.2 * b.2, a.1 * b.2 + a.2 * b.1)

def pairConj (a : Int × Int) : Int × Int := (a.1, -a.2)

def pairScale (c : Int) (a : Int × Int) : Int × Int :=
  (c * a.1, c * a.2)

def pairPow (D : Nat) (a : Int × Int) : Nat → Int × Int
  | 0 => (1, 0)
  | n + 1 => pairMul D (pairPow D a n) a

noncomputable def pairEval (D : Nat) (a : Int × Int) : Complex :=
  latticePoint (D : Real) a.1 a.2

theorem pairEval_mul (D : Nat) (a b : Int × Int) :
    pairEval D (pairMul D a b) = pairEval D a * pairEval D b := by
  have hs : (Real.sqrt (D : Real)) ^ 2 = (D : Real) := Real.sq_sqrt (by positivity)
  apply Complex.ext
  · simp [pairEval, pairMul, latticePoint, Complex.mul_re, Complex.mul_im]
    conv_lhs => rw [← hs]
    ring
  · simp [pairEval, pairMul, latticePoint, Complex.mul_re, Complex.mul_im]
    ring

theorem pairEval_conj (D : Nat) (a : Int × Int) :
    pairEval D (pairConj a) = conj (pairEval D a) := by
  apply Complex.ext
  · simp [pairEval, pairConj, latticePoint, Complex.mul_re, Complex.mul_im]
  · simp [pairEval, pairConj, latticePoint, Complex.mul_re, Complex.mul_im]

theorem pairEval_scale (D : Nat) (c : Int) (a : Int × Int) :
    pairEval D (pairScale c a) = (c : Complex) * pairEval D a := by
  apply Complex.ext
  · simp [pairEval, pairScale, latticePoint, Complex.mul_re, Complex.mul_im]
  · simp [pairEval, pairScale, latticePoint, Complex.mul_re, Complex.mul_im]
    ring

theorem pairEval_pow (D : Nat) (a : Int × Int) (n : Nat) :
    pairEval D (pairPow D a n) = (pairEval D a) ^ n := by
  induction n with
  | zero => simp [pairPow, pairEval, latticePoint]
  | succ n ih =>
      rw [pairPow, pairEval_mul, ih, pow_succ]

/-- An ordinary `Z`-derivative row, with the conjugate factor held fixed. -/
def integerDerivativeRow (D r s j : Nat) (p : Int × Int) : Int × Int :=
  if j ≤ r then
    pairScale (r.descFactorial j : Int)
      (pairMul D (pairPow D p (r - j)) (pairPow D (pairConj p) s))
  else (0, 0)

theorem integerDerivativeRow_eval (D r s j : Nat) (p : Int × Int) :
    pairEval D (integerDerivativeRow D r s j p) =
      derivativeRow r s j (pairEval D p) := by
  by_cases hj : j ≤ r
  · simp [integerDerivativeRow, derivativeRow, hj, pairEval_scale,
      pairEval_mul, pairEval_pow, pairEval_conj]
    ring
  · simp [integerDerivativeRow, derivativeRow, hj, pairEval, latticePoint]

/-- Twice the real trace pairing in integer coordinates. -/
def integerPairTrace (D : Nat) (a b : Int × Int) : Int :=
  2 * (a.1 * b.1 + (D : Int) * a.2 * b.2)

theorem integerPairTrace_cast (D : Nat) (a b : Int × Int) :
    (integerPairTrace D a b : Real) =
      2 * (pairEval D a * conj (pairEval D b)).re := by
  have hs : (Real.sqrt (D : Real)) ^ 2 = (D : Real) := Real.sq_sqrt (by positivity)
  simp [integerPairTrace, pairEval, latticePoint, Complex.mul_re, Complex.mul_im]
  conv_lhs => rw [← hs]
  ring

/-- The verifier's integer entry, summed over distinct input pairs. -/
def integerTraceGramEntry (Q : Finset (Int × Int)) (D J r s t u : Nat) : Int :=
  (Finset.range J).sum (fun j =>
    Q.sum (fun p => integerPairTrace D
      (integerDerivativeRow D r s j p)
      (integerDerivativeRow D t u j p)))

/-- Entrywise equality with the existing real trace, for distinct complex samples. -/
theorem integerTraceGramEntry_cast (Q : Finset (Int × Int)) (D J r s t u : Nat)
    (hD : 0 < D) :
    (integerTraceGramEntry Q D J r s t u : Real) =
      traceGramEntry (Q.image (pairEval D)) J r s t u := by
  classical
  unfold integerTraceGramEntry traceGramEntry
  push_cast
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  have hinj : Function.Injective (pairEval D) := latticePoint_injective D hD
  rw [Finset.sum_image hinj.injOn]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro p hp
  rw [integerPairTrace_cast, integerDerivativeRow_eval, integerDerivativeRow_eval]

/-- The same ordered derivative rows over the integer-pair coordinate lattice. -/
def integerTraceGramMatrix {n : Nat} (Q : Finset (Int × Int)) (D J : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) (Fin n) Int :=
  fun a b => integerTraceGramEntry Q D J
    (rows a).1 (rows a).2 (rows b).1 (rows b).2

theorem integerTraceGramMatrix_cast {n : Nat} (Q : Finset (Int × Int))
    (D J : Nat) (rows : Fin n → Nat × Nat) (hD : 0 < D) :
    (integerTraceGramMatrix Q D J rows).map (Int.castRingHom Real) =
      traceGramMatrix (Q.image (pairEval D)) J rows := by
  ext a b
  exact integerTraceGramEntry_cast Q D J
    (rows a).1 (rows a).2 (rows b).1 (rows b).2 hD

/-- The original row-major `(r,s)` enumeration, now over integer entries. -/
def integerRectangularTraceGram (Q : Finset (Int × Int)) (D J R S : Nat) :
    Matrix (Fin (R * S)) (Fin (R * S)) Int :=
  integerTraceGramMatrix Q D J (fun i => (i.val / S, i.val % S))

theorem integerRectangularTraceGram_cast (Q : Finset (Int × Int))
    (D J R S : Nat) (hD : 0 < D) :
    (integerRectangularTraceGram Q D J R S).map (Int.castRingHom Real) =
      rectangularTraceGram (Q.image (pairEval D)) J R S :=
  integerTraceGramMatrix_cast Q D J _ hD

theorem integerRectangularTraceGram_det_cast (Q : Finset (Int × Int))
    (D J R S : Nat) (hD : 0 < D) :
    ((integerRectangularTraceGram Q D J R S).det : Real) =
      (rectangularTraceGram (Q.image (pairEval D)) J R S).det := by
  calc
    _ = ((integerRectangularTraceGram Q D J R S).map
          (Int.castRingHom Real)).det := Int.cast_det (R := Real) _
    _ = _ := by rw [integerRectangularTraceGram_cast Q D J R S hD]

/-- The finite integer-radius ellipse is a specialization, not the verifier's
half-integer-radius campaign generator. -/
theorem ellipseIntegerTraceGram_cast (D rho J R S : Nat) (hD : 0 < D) :
    (integerRectangularTraceGram (ellipsePairs D rho) D J R S).map
      (Int.castRingHom Real) =
        rectangularTraceGram (ellipsePoints D rho) J R S := by
  simpa only [ellipsePoints, pairEval] using
    integerRectangularTraceGram_cast (ellipsePairs D rho) D J R S hD

theorem ellipseIntegerTraceGram_det_cast (D rho J R S : Nat) (hD : 0 < D) :
    ((integerRectangularTraceGram (ellipsePairs D rho) D J R S).det : Real) =
      (rectangularTraceGram (ellipsePoints D rho) J R S).det := by
  simpa only [ellipsePoints, pairEval] using
    integerRectangularTraceGram_det_cast (ellipsePairs D rho) D J R S hD

/-- The existing strict point-count guard makes the *integer* witness positive. -/
theorem ellipseIntegerTraceGram_det_pos_of_count (D rho J R S : Nat)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S) (hJ : S ≤ J)
    (hcard : 2 * (R - 1) + (S - 1) < (ellipsePairs D rho).card) :
    0 < (integerRectangularTraceGram (ellipsePairs D rho) D J R S).det := by
  have hreal :
      (0 : Real) < ((integerRectangularTraceGram (ellipsePairs D rho)
        D J R S).det : Real) := by
    rw [ellipseIntegerTraceGram_det_cast D rho J R S hD]
    exact (ellipseTraceGram_det_bounds D rho J R S hD hR hS hJ hcard).1
  exact_mod_cast hreal

private def asymmetricRows : Fin 2 → Nat × Nat :=
  fun i => if i = 0 then (0, 0) else (1, 1)

/-- A non-real point detects the conjugate factor and derivative convention:
`z = √(-3)`, `J=2`, rows `1` and `Z W`. The off-diagonal sign is positive. -/
theorem integerTraceGram_asymmetric_control :
    integerTraceGramMatrix {(0, 1)} 3 2 asymmetricRows =
      !![2, 6; 6, 24] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [integerTraceGramMatrix, integerTraceGramEntry, integerPairTrace,
      integerDerivativeRow, asymmetricRows, pairScale, pairMul, pairPow,
      pairConj, Finset.sum_range_succ, Nat.descFactorial]

theorem integerTraceGram_asymmetric_det_control :
    (integerTraceGramMatrix {(0, 1)} 3 2 asymmetricRows).det = 12 := by
  rw [integerTraceGram_asymmetric_control]
  norm_num [Matrix.det_fin_two]

end TenthDiscriminant
