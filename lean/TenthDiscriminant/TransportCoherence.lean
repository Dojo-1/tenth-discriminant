import TenthDiscriminant.ProofTransport
import TenthDiscriminant.PassiveTransport
import TenthDiscriminant.RankDivisorCompatibility

/-!
# Phase179: certificate transport coherence and the determinant's blind spots

A determinant is a decategorified view of an integral certificate.
These statements make THREE different conditions explicit:
  (1) an integral unimodular row gauge preserves the original Gram
      determinant and every divisor of that exact determinant;
  (2) a rational congruence changes the determinant by det(T)^2;
  (3) det(T)=1 over Q does NOT imply that T transports Z^n to Z^n.

This is NOT a new discriminant bound, hardness theorem or general
sheaf/hypercomplex obstruction. The proof source, integer ordinary-jet
observations, and the full field theorem are unchanged.
-/
namespace TenthDiscriminant.TransportCoherence
open Matrix
set_option autoImplicit false
noncomputable section

/-- The exact determinant weight of ANY integer frame: no positivity,
field hypothesis, or changed source matrix is assumed. -/
theorem integer_congruence_factor {n : Nat}
    (U G : Matrix (Fin n) (Fin n) Int) :
    (U * G * U.transpose).det = U.det^2 * G.det := by
  simp only [Matrix.det_mul, Matrix.det_transpose]
  ring

/-- Integral unimodularity, not arbitrary rational invertibility,
is sufficient for a determinant-preserving integer row gauge. -/
theorem integer_unimodular_congruence {n : Nat}
    (U G : Matrix (Fin n) (Fin n) Int)
    (hU : U.det = 1 ∨ U.det = -1) :
    (U * G * U.transpose).det = G.det := by
  rw [integer_congruence_factor]
  rcases hU with h | h
  · simp [h]
  · rw [h]
    ring

/-- Source-level instance: one unchanged integer ordinary-jet trace
Gram on the original finite support Q, with original D,J,R,S. -/
theorem original_gram_integral_gauge
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (U : Matrix (Fin (R*S)) (Fin (R*S)) Int)
    (hU : U.det = 1 ∨ U.det = -1) :
    (U * integerRectangularTraceGram Q D J R S * U.transpose).det =
      (integerRectangularTraceGram Q D J R S).det :=
  integer_unimodular_congruence U _ hU

/-- Every previously established arithmetic divisor survives the
SAME integer Gram under a unimodular row change. -/
theorem original_gram_integral_divisor_transport
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (U : Matrix (Fin (R*S)) (Fin (R*S)) Int)
    (hU : U.det = 1 ∨ U.det = -1)
    (w : Int)
    (hw : w ∣ (integerRectangularTraceGram Q D J R S).det) :
    w ∣ (U * integerRectangularTraceGram Q D J R S * U.transpose).det := by
  rw [original_gram_integral_gauge Q D J R S U hU]
  exact hw

/-- The rational determinant rule by itself has NO implication of
lattice-image preservation. In particular, a rational det-one shear
can fail to be an integral automorphism. -/
theorem rational_congruence_factor {n : Nat}
    (T G : Matrix (Fin n) (Fin n) Rat) :
    (T * G * T.transpose).det = T.det^2 * G.det := by
  simp only [Matrix.det_mul, Matrix.det_transpose]
  ring

/-- A rational volume-one shear: its off-diagonal is one half. -/
def halfShear : Matrix (Fin 2) (Fin 2) Rat :=
  !![1, 1/2; 0, 1]

theorem halfShear_det_one : halfShear.det = 1 := by
  norm_num [halfShear, Matrix.det_fin_two]

theorem halfShear_preserves_det (G : Matrix (Fin 2) (Fin 2) Rat) :
    (halfShear * G * halfShear.transpose).det = G.det := by
  rw [rational_congruence_factor, halfShear_det_one]
  ring

/-- The same det-one map cannot be the rational cast of ANY integral
matrix. This blocks promotion from SL_2(Q) to GL_2(Z). -/
theorem halfShear_not_integral :
    ¬ ∃ U : Matrix (Fin 2) (Fin 2) Int,
      U.map (Int.castRingHom Rat) = halfShear := by
  rintro ⟨U, hU⟩
  have he := congrArg (fun A : Matrix (Fin 2) (Fin 2) Rat => A 0 1) hU
  have heq : (U 0 1 : Rat) = 1/2 := by
    simpa [halfShear] using he
  have hr : (2 : Rat) * (U 0 1 : Rat) = 1 := by
    linarith
  have hz : (2 : Int) * U 0 1 = 1 := by
    exact_mod_cast hr
  omega

/-- Two different positive integer Gram matrices whose rational
half-shear relationship does NOT imply integral equivalence. -/
def integerToyGram : Matrix (Fin 2) (Fin 2) Int :=
  !![4, 0; 0, 4]

def rationallyTransportedIntegerToyGram : Matrix (Fin 2) (Fin 2) Int :=
  !![5, 2; 2, 4]

theorem integerToyGram_determinant_control :
    integerToyGram.det = 16 ∧
      rationallyTransportedIntegerToyGram.det = 16 := by
  constructor <;>
    norm_num [integerToyGram, rationallyTransportedIntegerToyGram,
      Matrix.det_fin_two]

/-- The Gram coordinates are BOTH integral with the same determinant;
the rational moving frame is still not an integer gauge. Their Smith
factors differ, as certified separately by the exact finite oracle. -/
theorem integerToyGram_rational_shear :
    halfShear *
      (integerToyGram.map (Int.castRingHom Rat)) *
      halfShear.transpose =
      rationallyTransportedIntegerToyGram.map (Int.castRingHom Rat) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [halfShear, integerToyGram, rationallyTransportedIntegerToyGram,
      Matrix.mul_apply, Fin.sum_univ_two]

/-- The elementary Fourier change is invertible over Q but not
unimodular over Z: its determinant introduces a factor four in the
congruent Gram determinant if one keeps the original metric fixed. -/
def Fourier2 : Matrix (Fin 2) (Fin 2) Int :=
  !![1, 1; 1, -1]

theorem Fourier2_det : Fourier2.det = -2 := by
  norm_num [Fourier2, Matrix.det_fin_two]

theorem Fourier2_congruence_factor (G : Matrix (Fin 2) (Fin 2) Int) :
    (Fourier2 * G * Fourier2.transpose).det = 4 * G.det := by
  rw [integer_congruence_factor, Fourier2_det]
  ring

theorem Fourier2_not_integral_gauge :
    Fourier2.det ≠ 1 ∧ Fourier2.det ≠ -1 := by
  rw [Fourier2_det]
  omega

/-- The p=2 reduction is singular; the failure is integral,
not a failure of rational invertibility. -/
theorem Fourier2_mod_two_singular :
    (Fourier2.map (Int.castRingHom (ZMod 2))).det = 0 := by
  norm_num [Fourier2, Matrix.det_fin_two]

end
end TenthDiscriminant.TransportCoherence
