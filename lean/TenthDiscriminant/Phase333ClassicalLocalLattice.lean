import TenthDiscriminant.IntegerTraceGram

/-!
# Phase333 — the classical maximal-order lattice and the original jet lattice

For odd squarefree D with D ≡ 3 (mod 4), write
  L = Z[√(-D)] and O = Z[(1 + √(-D))/2].
In coordinates relative to (1,√(-D)) and (1,ω) respectively,
the SAME element x + y√(-D) has coordinates (x,y) and (x-y,2y).

All theorems below keep the existing source Q, original ordinary-Z jets,
and the original positive integral trace pairing. In particular, the
maximal-order coordinate expression is NOT a new sampling set or a
replacement Gram determinant.

The image of L has index two. Divisibility of individual jet values
is equivalent at every odd modulus but not at 2. The binary exception
is shown by a strict negative control.

This file does NOT prove a class-number theorem, additional prime
valuation, analytic comparison or improved discriminant cutoff.
-/

namespace TenthDiscriminant.Phase333
open TenthDiscriminant
set_option autoImplicit false

/-- Coordinates (x-y,2y) of x+y√(-D) in the basis (1,ω),
with ω=(1+√(-D))/2. The formula is independent of D. -/
def sourceToMaximalCoords (a : Int × Int) : Int × Int :=
  (a.1 - a.2, 2*a.2)

/-- The integer matrix of the source-lattice inclusion. -/
def sourceToMaximalMatrix : Matrix (Fin 2) (Fin 2) Int :=
  !![1,-1;0,2]

theorem sourceToMaximalMatrix_det :
    sourceToMaximalMatrix.det = 2 := by
  norm_num [sourceToMaximalMatrix, Matrix.det_fin_two]

/-- Exactly the maximal-order coordinate pairs with even second
coordinate come from the original Z[√(-D)] lattice. -/
theorem sourceToMaximal_range_iff_even (m : Int × Int) :
    (∃ a : Int × Int, sourceToMaximalCoords a = m) ↔
      m.2 % 2 = 0 := by
  constructor
  · rintro ⟨⟨x,y⟩, h⟩
    have hy : 2*y = m.2 := by
      have h2 := congrArg Prod.snd h
      simpa [sourceToMaximalCoords] using h2
    omega
  · intro hm
    refine ⟨(m.1 + m.2/2, m.2/2), ?_⟩
    apply Prod.ext
    · dsimp [sourceToMaximalCoords]
      omega
    · dsimp [sourceToMaximalCoords]
      omega

/-- The maximal-order basis element ω does not lie in the original
lattice: it is precisely the nontrivial parity class. -/
theorem maximal_omega_not_in_source :
    ¬ ∃ a : Int × Int, sourceToMaximalCoords a = (0,1) := by
  rw [sourceToMaximal_range_iff_even]
  norm_num

/-- Positive trace pairing in the maximal basis (1,ω).
The coefficient (D+1)/2 is integral for odd D. -/
def maximalTracePair (D : Nat) (a b : Int × Int) : Int :=
  2*a.1*b.1 + a.1*b.2 + a.2*b.1 +
    (((D : Int)+1)/2)*a.2*b.2

/-- The positive trace pairing is exactly preserved under the
index-two inclusion, for odd D and the SAME two source elements. -/
theorem maximalTracePair_source_eq_original
    (D : Nat) (hodd : ((D : Int) % 2) = 1)
    (a b : Int × Int) :
    maximalTracePair D (sourceToMaximalCoords a)
      (sourceToMaximalCoords b) = integerPairTrace D a b := by
  have ht : 2 * (((D : Int)+1)/2) = (D : Int)+1 := by omega
  rcases a with ⟨x,y⟩
  rcases b with ⟨u,v⟩
  change
    2*(x-y)*(u-v) + (x-y)*(2*v) +
        (2*y)*(u-v) + (((D : Int)+1)/2)*(2*y)*(2*v) =
      2*(x*u + (D : Int)*y*v)
  calc
    _ = 2*(x*u + (2*(((D : Int)+1)/2)-1)*y*v) := by ring
    _ = 2*(x*u + (D : Int)*y*v) := by rw [ht]; ring

/-- Coordinatewise divisibility in a free rank-two integral lattice. -/
def pairDvd (q : Int) (a : Int × Int) : Prop :=
  q ∣ a.1 ∧ q ∣ a.2

/-- Bézout cancellation of the factor two at an odd modulus.
This does not require primality or invertibility assumptions hidden
inside an unproved field equivalence. -/
theorem odd_modulus_dvd_of_dvd_two_mul
    (q y : Int) (hq : q % 2 = 1) (h : q ∣ 2*y) : q ∣ y := by
  obtain ⟨k,hk⟩ := h
  have hbezout : 2*(q/2+1)-q = 1 := by omega
  refine ⟨(q/2+1)*k-y, ?_⟩
  calc
    y = (2*(q/2+1)-q)*y := by rw [hbezout]; ring
    _ = (q/2+1)*(2*y)-q*y := by ring
    _ = (q/2+1)*(q*k)-q*y := by rw [hk]
    _ = q*((q/2+1)*k-y) := by ring

/-- For every odd modulus q (in particular, every odd prime power),
the source and maximal coordinates have equivalent divisibility.
The result applies to each unchanged original ordinary jet. -/
theorem odd_modulus_pair_divisibility_iff
    (q : Int) (hq : q % 2 = 1) (a : Int × Int) :
    pairDvd q (sourceToMaximalCoords a) ↔ pairDvd q a := by
  constructor
  · intro h
    change q ∣ a.1-a.2 ∧ q ∣ 2*a.2 at h
    rcases h with ⟨hx,hy⟩
    have hy' : q ∣ a.2 :=
      odd_modulus_dvd_of_dvd_two_mul q a.2 hq hy
    have hx' : q ∣ a.1 := by
      have hadd : q ∣ (a.1-a.2)+a.2 := hx.add hy'
      simpa only [sub_add_cancel] using hadd
    exact ⟨hx',hy'⟩
  · rintro ⟨hx,hy⟩
    change q ∣ a.1-a.2 ∧ q ∣ 2*a.2
    constructor
    · exact hx.sub hy
    · obtain ⟨k,hk⟩ := hy
      refine ⟨2*k, ?_⟩
      rw [hk]
      ring

/-- For ANY modulus, maximal-coordinate divisibility implies
source-coordinate divisibility after multiplication by two. Thus any
extra binary divisibility from the larger order costs at most the
index-two factor; it is not freely transferable to the original
ordinary-jet lattice. -/
theorem maximal_dvd_implies_twice_source_dvd
    (q : Int) (a : Int × Int)
    (h : pairDvd q (sourceToMaximalCoords a)) :
    pairDvd q (2*a.1,2*a.2) := by
  change q ∣ a.1-a.2 ∧ q ∣ 2*a.2 at h
  rcases h with ⟨hx,hy⟩
  change q ∣ 2*a.1 ∧ q ∣ 2*a.2
  have htwice : q ∣ 2*(a.1-a.2) := by
    obtain ⟨k,hk⟩ := hx
    refine ⟨2*k, ?_⟩
    rw [hk]
    ring
  constructor
  · have hh : 2*a.1 = 2*(a.1-a.2)+2*a.2 := by ring
    rw [hh]
    exact htwice.add hy
  · exact hy

/-- Failure of unqualified 2-adic transport. Although 1+√(-D)
is twice ω in the maximal order, it is not twice an original
source-lattice element. -/
theorem binary_non_equivalence_control :
    pairDvd 2 (sourceToMaximalCoords (1,1)) ∧
      ¬ pairDvd 2 (1,1) := by
  norm_num [pairDvd, sourceToMaximalCoords]

/-- The SAME original ordinary-Z jets rewritten using maximal-order
coordinates, with no replacement of samples or derivative convention. -/
def sameSourceMaximalTraceGramEntry
    (Q : Finset (Int × Int)) (D J r s t u : Nat) : Int :=
  (Finset.range J).sum (fun j =>
    Q.sum (fun p =>
      maximalTracePair D
        (sourceToMaximalCoords (integerDerivativeRow D r s j p))
        (sourceToMaximalCoords (integerDerivativeRow D t u j p))))

theorem sameSourceMaximalTraceGramEntry_eq_original
    (Q : Finset (Int × Int)) (D J r s t u : Nat)
    (hodd : ((D : Int) % 2) = 1) :
    sameSourceMaximalTraceGramEntry Q D J r s t u =
      integerTraceGramEntry Q D J r s t u := by
  unfold sameSourceMaximalTraceGramEntry integerTraceGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  apply Finset.sum_congr rfl
  intro p hp
  exact maximalTracePair_source_eq_original D hodd _ _

def sameSourceMaximalRectangularTraceGram
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  fun i k =>
    sameSourceMaximalTraceGramEntry Q D J
      (i.val/S) (i.val%S) (k.val/S) (k.val%S)

theorem sameSourceMaximalRectangularTraceGram_eq_original
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (hodd : ((D : Int) % 2) = 1) :
    sameSourceMaximalRectangularTraceGram Q D J R S =
      integerRectangularTraceGram Q D J R S := by
  ext i k
  exact sameSourceMaximalTraceGramEntry_eq_original Q D J
    (i.val/S) (i.val%S) (k.val/S) (k.val%S) hodd

/-- The two coordinate descriptions have exactly the SAME original
integer determinant, not a merely bounded or rescaled substitute. -/
theorem sameSourceMaximalRectangularTraceGram_det_eq_original
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (hodd : ((D : Int) % 2) = 1) :
    (sameSourceMaximalRectangularTraceGram Q D J R S).det =
      (integerRectangularTraceGram Q D J R S).det := by
  rw [sameSourceMaximalRectangularTraceGram_eq_original Q D J R S hodd]

end TenthDiscriminant.Phase333

#print axioms TenthDiscriminant.Phase333.sourceToMaximal_range_iff_even
#print axioms TenthDiscriminant.Phase333.maximalTracePair_source_eq_original
#print axioms TenthDiscriminant.Phase333.odd_modulus_pair_divisibility_iff
#print axioms TenthDiscriminant.Phase333.maximal_dvd_implies_twice_source_dvd
#print axioms TenthDiscriminant.Phase333.sameSourceMaximalRectangularTraceGram_det_eq_original
