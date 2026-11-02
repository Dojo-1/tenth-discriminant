import TenthDiscriminant.RectangularGramFactor
import TenthDiscriminant.GramDivisibility

/-!
# The exact factor-two normalization in the original integer trace metric

The old zsqrtdJetGram is the actual source trace pairing with weights
2 and 2D; its factor two is not a separately invented observation.
This generic theorem converts a valid unimodular original-jet
row factorization into an integer determinant divisor.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- The integer half-trace (real coordinates squared plus D times
imaginary coordinates squared) on the SAME original jet family. -/
def zsqrtdHalfJetGram {n : Nat} (Q : Finset (Int × Int))
    (D J : Nat)
    (V : Fin n → Int × Int → Nat → Zsqrtd (-(D : Int))) :
    Matrix (Fin n) (Fin n) Int :=
  fun i l => (Finset.range J).sum fun j =>
    Q.sum fun a =>
      (V i a j).re * (V l a j).re +
        (D : Int) * (V i a j).im * (V l a j).im

/-- The exact source metric has one factor two on its left.
This is a matrix equality over integers, not a comparison of trace forms. -/
theorem zsqrtdJetGram_two_half {n : Nat}
    (Q : Finset (Int × Int)) (D J : Nat)
    (V : Fin n → Int × Int → Nat → Zsqrtd (-(D : Int))) :
    zsqrtdJetGram Q D J V =
      Matrix.diagonal (fun _ : Fin n => (2 : Int)) *
        zsqrtdHalfJetGram Q D J V := by
  ext i l
  simp only [Matrix.diagonal_mul, zsqrtdJetGram,
    zsqrtdHalfJetGram, zsqrtdTrace]
  simp only [Finset.mul_sum]

/-- A generic original-jet integer row factorization yields BOTH the
two-sided row factors and the independent global factor-two trace metric.
The family Q, derivative order J, and integer quadratic-order chart are
unchanged. No claim about which U admits such a factorization is made. -/
theorem binaryGramFactor_dvd_generic {n : Nat}
    (Q : Finset (Int × Int)) (D J : Nat)
    (U : Matrix (Fin n) (Fin n) Int)
    (V W : Fin n → Int × Int → Nat → Zsqrtd (-(D : Int)))
    (k : Fin n → Nat)
    (hU : U.det = 1)
    (hscale : ∀ i a j, a ∈ Q → j ∈ Finset.range J →
      zsqrtdJetTransform U V i a j =
        ((2 : Int)^k i) • W i a j) :
    (2 : Int)^(n + 2*(∑ i : Fin n, k i)) ∣
      (zsqrtdJetGram Q D J V).det := by
  classical
  let d : Fin n → Int := fun i => (2 : Int)^k i
  let K := zsqrtdHalfJetGram Q D J W
  have hfactor :
      U * zsqrtdJetGram Q D J V * U.transpose =
        Matrix.diagonal d *
          (Matrix.diagonal (fun _ : Fin n => (2 : Int)) * K) *
          Matrix.diagonal d := by
    calc
      _ = zsqrtdJetGram Q D J (zsqrtdJetTransform U V) := by
        rw [zsqrtdJetGram_transform]
      _ = Matrix.diagonal d * zsqrtdJetGram Q D J W *
          Matrix.diagonal d :=
        zsqrtdJetGram_scale Q D J
          (zsqrtdJetTransform U V) W d hscale
      _ = _ := by rw [zsqrtdJetGram_two_half]
  have hd := congrArg Matrix.det hfactor
  have hprod : (∏ i : Fin n, d i) =
      (2 : Int)^(∑ i : Fin n, k i) := by
    dsimp [d]
    simpa using (Finset.prod_pow_eq_pow_sum Finset.univ k (2 : Int))
  have htwo : (∏ _i : Fin n, (2 : Int)) = (2 : Int)^n := by
    simp
  simp only [Matrix.det_mul, Matrix.det_transpose, Matrix.det_diagonal,
    hU, one_mul, mul_one, hprod, htwo] at hd
  refine ⟨K.det, ?_⟩
  calc
    (zsqrtdJetGram Q D J V).det =
        (2 : Int)^(∑ i : Fin n, k i) *
          ((2 : Int)^n * K.det) *
          (2 : Int)^(∑ i : Fin n, k i) := hd
    _ = (2 : Int)^(n + 2*(∑ i : Fin n, k i)) * K.det := by
      rw [pow_add, two_mul, pow_add]
      ring

end TenthDiscriminant
