import TenthDiscriminant.IntegerTraceGram

/-!
# Phase384 — the index-two quadratic-order interface in integer coordinates

A source-to-maximal-order CHART calculation for D = 4c-1.
The source pair x+y*sqrt(-D) is sent to
  (x-y) + (2y)*omega, omega=(1+sqrt(-D))/2.
No hypothesis about class number, Frobenius, or large determinants
is proved here. The true maximal-order identification is a separate
number-theoretic theorem used by the original field chart.
-/

namespace TenthDiscriminant.Phase384
set_option autoImplicit false

/-- Coordinates of x+y*sqrt(-D) in basis (1,omega). -/
def sourceToMax (p : Int × Int) : Int × Int :=
  (p.1 - p.2, 2 * p.2)

/-- Multiplication for omega^2 = omega-c in basis (1,omega). -/
def maxMul (c : Int) (a b : Int × Int) : Int × Int :=
  (a.1 * b.1 - c * a.2 * b.2,
   a.1 * b.2 + a.2 * b.1 + a.2 * b.2)

/-- The positive conjugate-trace pairing in the (1,omega) chart. -/
def maxTrace (c : Int) (a b : Int × Int) : Int :=
  2 * a.1 * b.1 + a.1 * b.2 + a.2 * b.1 + 2 * c * a.2 * b.2

/-- Exact multiplication preservation when D=4c-1. -/
theorem sourceToMax_mul
    (D : Nat) (c : Int) (hDc : (D : Int) = 4*c-1)
    (a b : Int × Int) :
    sourceToMax (pairMul D a b) =
      maxMul c (sourceToMax a) (sourceToMax b) := by
  rcases a with ⟨x,y⟩
  rcases b with ⟨u,v⟩
  apply Prod.ext
  · simp [sourceToMax, pairMul, maxMul, hDc]
    ring
  · simp [sourceToMax, pairMul, maxMul]
    ring

/-- Preserve the actual integerPairTrace from IntegerTraceGram. -/
theorem sourceToMax_trace
    (D : Nat) (c : Int) (hDc : (D : Int) = 4*c-1)
    (a b : Int × Int) :
    integerPairTrace D a b =
      maxTrace c (sourceToMax a) (sourceToMax b) := by
  rcases a with ⟨x,y⟩
  rcases b with ⟨u,v⟩
  simp [integerPairTrace, sourceToMax, maxTrace, hDc]
  ring

/-- The source trace matrix has determinant 4D; the maximal-order
conjugate-trace matrix has determinant D. This is a trace-form identity,
NOT an assertion that det(source jet Gram)=field discriminant. -/
theorem traceMetric_index_four
    (D : Nat) (c : Int) (hDc : (D : Int) = 4*c-1) :
    (2 : Int) * (2 * (D : Int)) =
      4 * ((2 : Int) * (2*c) - 1) := by
  rw [hDc]
  ring

/-- In the original odd chart, c=(D+1)/4 is an integer and D=4c-1. -/
theorem odd_coefficient_identity
    (D : Nat) (hmod : (D : Int) % 4 = 3) :
    (D : Int) = 4 * (((D : Int) + 1) / 4) - 1 := by
  omega

/-- Source multiplication in the original D % 4 = 3 chart. -/
theorem sourceToMax_mul_odd
    (D : Nat) (hmod : (D : Int) % 4 = 3) (a b : Int × Int) :
    sourceToMax (pairMul D a b) =
      maxMul (((D : Int) + 1) / 4) (sourceToMax a) (sourceToMax b) :=
  sourceToMax_mul D _ (odd_coefficient_identity D hmod) a b

/-- Source conjugate trace in the original D % 4 = 3 chart. -/
theorem sourceToMax_trace_odd
    (D : Nat) (hmod : (D : Int) % 4 = 3) (a b : Int × Int) :
    integerPairTrace D a b =
      maxTrace (((D : Int) + 1) / 4) (sourceToMax a) (sourceToMax b) :=
  sourceToMax_trace D _ (odd_coefficient_identity D hmod) a b

/-- Witness of the index-two obstruction: omega itself does not belong
to the integer span of (1,sqrt(-D)), because its second chart coordinate
would be 2y=1. This is exactly why the p=2 map is not invertible. -/
theorem omega_not_in_source (x y : Int) :
    sourceToMax (x,y) ≠ (0,1) := by
  intro h
  have heq : 2*y = 1 := by
    simpa only [sourceToMax, Prod.mk.injEq, and_true] using
      congrArg Prod.snd h
  omega

end TenthDiscriminant.Phase384

#print axioms TenthDiscriminant.Phase384.sourceToMax_mul_odd
#print axioms TenthDiscriminant.Phase384.sourceToMax_trace_odd
#print axioms TenthDiscriminant.Phase384.omega_not_in_source
