import TenthDiscriminant.IntegerTraceGram

/-!
Phase390: a universal, source-preserving maximal-order coordinate interface.

For D=4*c-1 and omega=(1+sqrt(-D))/2, the original source element
x+y*sqrt(-D) has maximal-order coordinates (x-y,2*y). The map is
injective but its index is TWO; it must never be treated as a GL(2,Z)
basis change or used to replace the original sample Q by the full O_K.

The statements here transport the *unchanged* complete ordinary Z-jet
values, W held fixed, and the entire original integer trace Gram.
They DO NOT establish any new p-adic valuation, class-number-one
prime-inertness, analytic Hadamard bound, or 302^4 field theorem.
-/

namespace TenthDiscriminant.Phase390
open scoped BigOperators
set_option autoImplicit false

def toMax (z : Int × Int) : Int × Int :=
  (z.1-z.2,2*z.2)

def maxMul (c : Int) (a b : Int × Int) : Int × Int :=
  (a.1*b.1-c*a.2*b.2,
   a.1*b.2+a.2*b.1+a.2*b.2)

def maxConj (a : Int × Int) : Int × Int :=
  (a.1+a.2,-a.2)

def maxScale (n : Int) (a : Int × Int) : Int × Int :=
  (n*a.1,n*a.2)

def maxPow (c : Int) (a : Int × Int) : Nat → Int × Int
  | 0 => (1,0)
  | n+1 => maxMul c (maxPow c a n) a

def maxDerivative (c : Int) (r s j : Nat) (z : Int × Int) : Int × Int :=
  if j ≤ r then
    maxScale (r.descFactorial j : Int)
      (maxMul c (maxPow c z (r-j)) (maxPow c (maxConj z) s))
  else (0,0)

def maxTrace (c : Int) (a b : Int × Int) : Int :=
  2*a.1*b.1+a.1*b.2+a.2*b.1+2*c*a.2*b.2

theorem toMax_mul (D : Nat) (c : Int)
    (hD : (D : Int) = 4*c-1) (a b : Int × Int) :
    toMax (pairMul D a b) =
      maxMul c (toMax a) (toMax b) := by
  rcases a with ⟨x,y⟩
  rcases b with ⟨u,v⟩
  simp only [toMax,pairMul,maxMul,Prod.fst,Prod.snd,Prod.mk.injEq]
  rw [hD]
  constructor <;> ring

theorem toMax_conj (a : Int × Int) :
    toMax (pairConj a) = maxConj (toMax a) := by
  rcases a with ⟨x,y⟩
  simp [toMax,pairConj,maxConj]

theorem toMax_scale (n : Int) (a : Int × Int) :
    toMax (pairScale n a) = maxScale n (toMax a) := by
  rcases a with ⟨x,y⟩
  simp only [toMax,pairScale,maxScale,Prod.fst,Prod.snd,Prod.mk.injEq]
  constructor <;> ring

theorem toMax_pow (D : Nat) (c : Int)
    (hD : (D : Int) = 4*c-1) (a : Int × Int) (n : Nat) :
    toMax (pairPow D a n) = maxPow c (toMax a) n := by
  induction n with
  | zero => simp [pairPow,maxPow,toMax]
  | succ n ih =>
    simp only [pairPow,maxPow]
    rw [toMax_mul D c hD,ih]

theorem toMax_derivative (D : Nat) (c : Int)
    (hD : (D : Int) = 4*c-1)
    (r s j : Nat) (z : Int × Int) :
    toMax (integerDerivativeRow D r s j z) =
      maxDerivative c r s j (toMax z) := by
  by_cases hj : j ≤ r
  · simp only [integerDerivativeRow,maxDerivative,hj,ite_true]
    rw [toMax_scale,toMax_mul D c hD,
        toMax_pow D c hD,toMax_pow D c hD,toMax_conj]
  · simp [integerDerivativeRow,maxDerivative,hj,toMax]

theorem toMax_trace (D : Nat) (c : Int)
    (hD : (D : Int) = 4*c-1) (a b : Int × Int) :
    integerPairTrace D a b =
      maxTrace c (toMax a) (toMax b) := by
  rcases a with ⟨x,y⟩
  rcases b with ⟨u,v⟩
  simp only [integerPairTrace,toMax,maxTrace,Prod.fst,Prod.snd]
  rw [hD]
  ring

/-- The one original physical sample Q, expressed in the maximal-order
basis. The image is not enlarged to the complete maximal-order ellipse. -/
def maxTraceGramEntry (Q : Finset (Int × Int)) (c : Int)
    (J r s t u : Nat) : Int :=
  (Finset.range J).sum (fun j =>
    Q.sum (fun z => maxTrace c
      (maxDerivative c r s j (toMax z))
      (maxDerivative c t u j (toMax z))))

theorem original_entry_eq_same_samples_maximal_chart
    (Q : Finset (Int × Int)) (D : Nat) (c : Int)
    (hD : (D : Int) = 4*c-1)
    (J r s t u : Nat) :
    integerTraceGramEntry Q D J r s t u =
      maxTraceGramEntry Q c J r s t u := by
  unfold integerTraceGramEntry maxTraceGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  apply Finset.sum_congr rfl
  intro z hz
  rw [toMax_trace D c hD,
      toMax_derivative D c hD,
      toMax_derivative D c hD]

/-- Universal full-matrix identity for arbitrary finite Q, arbitrary
rectangular dimensions and arbitrary ordinary derivative depth.
The *physical* Q and full ordered row family remain unchanged. -/
theorem full_original_gram_eq_same_samples_maximal_chart
    (Q : Finset (Int × Int)) (D : Nat) (c : Int)
    (hD : (D : Int) = 4*c-1) (J R S : Nat) :
    integerRectangularTraceGram Q D J R S =
      (fun i j : Fin (R*S) =>
        maxTraceGramEntry Q c J
          (i.val/S) (i.val%S) (j.val/S) (j.val%S)) := by
  ext i j
  exact original_entry_eq_same_samples_maximal_chart
    Q D c hD J (i.val/S) (i.val%S) (j.val/S) (j.val%S)

/-- Sharp order-163 boundary: c=41 is represented by omega and
the polynomial X^2-X+41 has distinct roots 0,1 modulo 41. The
class-number-one inert-prime gate MUST be strict p<c. -/
theorem forty_one_boundary_controls :
    (163 : Int) = 4*41-1 ∧
    maxMul 41 (0,1) (1,-1) = (41,0) ∧
    (0 : ZMod 41)^2-(0 : ZMod 41)+41=0 ∧
    (1 : ZMod 41)^2-(1 : ZMod 41)+41=0 := by
  norm_num [maxMul]

end TenthDiscriminant.Phase390

#print axioms TenthDiscriminant.Phase390.full_original_gram_eq_same_samples_maximal_chart
