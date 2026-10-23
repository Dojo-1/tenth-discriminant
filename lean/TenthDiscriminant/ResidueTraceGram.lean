import TenthDiscriminant.IntegerTraceGram
import Mathlib.Data.ZMod.Basic

/-!
# Reduction of the integer trace-Gram matrix modulo `m`

The samples are indexed by the original integer-pair finset. Distinct integer
points can coincide after reduction modulo `m`; replacing that finset by its
image in `ZMod m × ZMod m` would then discard contributions.
-/

namespace TenthDiscriminant

/-- Reduce both coordinates of one selected-lattice point modulo `m`. -/
def residuePair (m : Nat) (a : Int × Int) : ZMod m × ZMod m :=
  ((a.1 : ZMod m), (a.2 : ZMod m))

/-- Multiplication in the selected quadratic order after reduction. -/
def residuePairMul (D m : Nat) (a b : ZMod m × ZMod m) : ZMod m × ZMod m :=
  (a.1 * b.1 - (D : ZMod m) * a.2 * b.2, a.1 * b.2 + a.2 * b.1)

def residuePairConj {m : Nat} (a : ZMod m × ZMod m) : ZMod m × ZMod m :=
  (a.1, -a.2)

def residuePairScale {m : Nat} (c : ZMod m) (a : ZMod m × ZMod m) : ZMod m × ZMod m :=
  (c * a.1, c * a.2)

def residuePairPow (D m : Nat) (a : ZMod m × ZMod m) : Nat → ZMod m × ZMod m
  | 0 => (1, 0)
  | n + 1 => residuePairMul D m (residuePairPow D m a n) a

theorem residuePair_mul (D m : Nat) (a b : Int × Int) :
    residuePair m (pairMul D a b) =
      residuePairMul D m (residuePair m a) (residuePair m b) := by
  ext <;> simp [residuePair, residuePairMul, pairMul]

theorem residuePair_conj (m : Nat) (a : Int × Int) :
    residuePair m (pairConj a) = residuePairConj (residuePair m a) := by
  ext <;> simp [residuePair, residuePairConj, pairConj]

theorem residuePair_scale (m : Nat) (c : Int) (a : Int × Int) :
    residuePair m (pairScale c a) =
      residuePairScale (c : ZMod m) (residuePair m a) := by
  ext <;> simp [residuePair, residuePairScale, pairScale]

theorem residuePair_pow (D m : Nat) (a : Int × Int) (n : Nat) :
    residuePair m (pairPow D a n) = residuePairPow D m (residuePair m a) n := by
  induction n with
  | zero => simp [pairPow, residuePairPow, residuePair]
  | succ n ih => rw [pairPow, residuePair_mul, ih, residuePairPow]

/-- Ordinary `Z`-derivative row computed wholly in residue coordinates. -/
def residueDerivativeRow (D r s j m : Nat) (p : ZMod m × ZMod m) :
    ZMod m × ZMod m :=
  if j ≤ r then
    residuePairScale (r.descFactorial j : ZMod m)
      (residuePairMul D m (residuePairPow D m p (r - j))
        (residuePairPow D m (residuePairConj p) s))
  else (0, 0)

theorem residueDerivativeRow_cast (D r s j m : Nat) (p : Int × Int) :
    residuePair m (integerDerivativeRow D r s j p) =
      residueDerivativeRow D r s j m (residuePair m p) := by
  by_cases hj : j ≤ r
  · simp [integerDerivativeRow, residueDerivativeRow, hj,
      residuePair_scale, residuePair_mul, residuePair_pow, residuePair_conj]
  · simp [integerDerivativeRow, residueDerivativeRow, hj, residuePair]

/-- The same factor-two trace pairing, now in the residue ring. -/
def residuePairTrace (D m : Nat) (a b : ZMod m × ZMod m) : ZMod m :=
  2 * (a.1 * b.1 + (D : ZMod m) * a.2 * b.2)

theorem residuePairTrace_cast (D m : Nat) (a b : Int × Int) :
    residuePairTrace D m (residuePair m a) (residuePair m b) =
      (integerPairTrace D a b : ZMod m) := by
  simp [residuePairTrace, residuePair, integerPairTrace]

/-- A local Gram entry. The inner sum retains every original sample. -/
def residueTraceGramEntry (Q : Finset (Int × Int)) (D J r s t u m : Nat) : ZMod m :=
  (Finset.range J).sum (fun j =>
    Q.sum (fun p => residuePairTrace D m
      (residueDerivativeRow D r s j m (residuePair m p))
      (residueDerivativeRow D t u j m (residuePair m p))))

theorem residueTraceGramEntry_eq_cast (Q : Finset (Int × Int))
    (D J r s t u m : Nat) :
    residueTraceGramEntry Q D J r s t u m =
      (integerTraceGramEntry Q D J r s t u : ZMod m) := by
  simp [residueTraceGramEntry, integerTraceGramEntry,
    ← residueDerivativeRow_cast, residuePairTrace_cast]

/-- Local Gram matrix for arbitrary row labels. -/
def residueTraceGramMatrix {n : Nat} (Q : Finset (Int × Int)) (D J m : Nat)
    (rows : Fin n → Nat × Nat) : Matrix (Fin n) (Fin n) (ZMod m) :=
  fun a b => residueTraceGramEntry Q D J
    (rows a).1 (rows a).2 (rows b).1 (rows b).2 m

theorem residueTraceGramMatrix_eq_map {n : Nat} (Q : Finset (Int × Int))
    (D J m : Nat) (rows : Fin n → Nat × Nat) :
    residueTraceGramMatrix Q D J m rows =
      (integerTraceGramMatrix Q D J rows).map (Int.castRingHom (ZMod m)) := by
  ext a b
  exact residueTraceGramEntry_eq_cast Q D J
    (rows a).1 (rows a).2 (rows b).1 (rows b).2 m

theorem residueTraceGramMatrix_det_eq_cast {n : Nat} (Q : Finset (Int × Int))
    (D J m : Nat) (rows : Fin n → Nat × Nat) :
    (residueTraceGramMatrix Q D J m rows).det =
      ((integerTraceGramMatrix Q D J rows).det : ZMod m) := by
  rw [residueTraceGramMatrix_eq_map]
  exact (Int.cast_det (R := ZMod m) _).symm

/-- Divisibility of the global determinant is precisely vanishing of its
local reduction. No valuation exponent is asserted here. -/
theorem residueTraceGramMatrix_det_zero_iff_dvd {n : Nat}
    (Q : Finset (Int × Int)) (D J m : Nat) (rows : Fin n → Nat × Nat)
    (_hm : 0 < m) :
    (residueTraceGramMatrix Q D J m rows).det = 0 ↔
      (m : Int) ∣ (integerTraceGramMatrix Q D J rows).det := by
  rw [residueTraceGramMatrix_det_eq_cast]
  exact ZMod.intCast_zmod_eq_zero_iff_dvd _ m

/-- Row-major rectangular specialization of the local matrix. -/
def residueRectangularTraceGram (Q : Finset (Int × Int))
    (D J R S m : Nat) : Matrix (Fin (R * S)) (Fin (R * S)) (ZMod m) :=
  residueTraceGramMatrix Q D J m (fun i => (i.val / S, i.val % S))

theorem residueRectangularTraceGram_eq_map (Q : Finset (Int × Int))
    (D J R S m : Nat) :
    residueRectangularTraceGram Q D J R S m =
      (integerRectangularTraceGram Q D J R S).map (Int.castRingHom (ZMod m)) :=
  residueTraceGramMatrix_eq_map Q D J m _

theorem residueRectangularTraceGram_det_eq_cast (Q : Finset (Int × Int))
    (D J R S m : Nat) :
    (residueRectangularTraceGram Q D J R S m).det =
      ((integerRectangularTraceGram Q D J R S).det : ZMod m) :=
  residueTraceGramMatrix_det_eq_cast Q D J m _

theorem residueRectangularTraceGram_det_zero_iff_dvd
    (Q : Finset (Int × Int)) (D J R S m : Nat) (hm : 0 < m) :
    (residueRectangularTraceGram Q D J R S m).det = 0 ↔
      (m : Int) ∣ (integerRectangularTraceGram Q D J R S).det :=
  residueTraceGramMatrix_det_zero_iff_dvd Q D J m _ hm

private def collisionQ : Finset (Int × Int) := {(0, 0), (3, 0)}

/-- Two distinct global points each contribute `2` to the constant row. -/
theorem residueTraceGram_collision_integer_control :
    (integerRectangularTraceGram collisionQ 1 1 1 1).det = 4 := by
  rw [Matrix.det_fin_one]
  norm_num [integerRectangularTraceGram,
    integerTraceGramMatrix, integerTraceGramEntry, integerPairTrace,
    integerDerivativeRow, pairScale, pairMul, pairPow, pairConj,
    collisionQ, Nat.descFactorial]; decide

/-- Reduction retains both contributions even though the points coincide
modulo `3`: `4 ≡ 1`. -/
theorem residueTraceGram_collision_mod_three_control :
    (residueRectangularTraceGram collisionQ 1 1 1 1 3).det = 1 := by
  rw [residueRectangularTraceGram_det_eq_cast,
    residueTraceGram_collision_integer_control]
  decide

private theorem collisionQ_image_mod_three :
    collisionQ.image (residuePair 3) =
      {((0 : ZMod 3), (0 : ZMod 3))} := by
  decide

/-- The tempting set-image rule is false: it counts the common residue
point once and gives `2`, not the correct value `1`. -/
theorem residueTraceGram_dedup_negative_control :
    (collisionQ.image (residuePair 3)).sum (fun _ => (2 : ZMod 3)) = 2 ∧
      (collisionQ.image (residuePair 3)).sum (fun _ => (2 : ZMod 3)) ≠
        (residueRectangularTraceGram collisionQ 1 1 1 1 3).det := by
  rw [collisionQ_image_mod_three, residueTraceGram_collision_mod_three_control]
  decide

private def asymmetricRows : Fin 2 → Nat × Nat :=
  fun i => if i = 0 then (0, 0) else (1, 1)

/-- Exact global control with the conjugate `W` held fixed under ordinary
`Z`-differentiation. -/
theorem residueTraceGram_asymmetric_integer_control :
    (integerTraceGramMatrix {(0, 1)} 3 2 asymmetricRows).det = 12 := by
  have hmatrix :
      integerTraceGramMatrix {(0, 1)} 3 2 asymmetricRows =
        !![2, 6; 6, 24] := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [integerTraceGramMatrix, integerTraceGramEntry, integerPairTrace,
        integerDerivativeRow, asymmetricRows, pairScale, pairMul, pairPow,
        pairConj, Finset.sum_range_succ, Nat.descFactorial]
  rw [hmatrix]
  norm_num [Matrix.det_fin_two]

theorem residueTraceGram_asymmetric_mod_three_control :
    (residueTraceGramMatrix {(0, 1)} 3 2 3 asymmetricRows).det = 0 := by
  rw [residueTraceGramMatrix_det_eq_cast,
    residueTraceGram_asymmetric_integer_control]
  decide

theorem residueTraceGram_asymmetric_mod_five_control :
    (residueTraceGramMatrix {(0, 1)} 3 2 5 asymmetricRows).det = 2 := by
  rw [residueTraceGramMatrix_det_eq_cast,
    residueTraceGram_asymmetric_integer_control]
  decide

end TenthDiscriminant
