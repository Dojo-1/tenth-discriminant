import TenthDiscriminant.Phase333ClassicalLocalLattice
import TenthDiscriminant.BinaryNullPolynomial

/-!
# Phase334 — the conductor-two obstruction in the quadratic-order residue rings

The source lattice L = Z[√(-D)] and the maximal order O_K
agree at every odd localization (Phase333), but not at the prime 2.

For D ≡ 3 mod 4, the source-to-maximal coordinates are multiplicative,
where maximal multiplication is computed in the integral basis
(1, ω) with ω² = ω - (D+1)/4.

For any odd D, the residue of 1+√(-D) is a NONZERO NILPOTENT in L/2L.
The existing null polynomial F(Z)=Z⁴-Z² vanishes at all source
values modulo 2; at D=163, F(ω) is NOT divisible by 2 in O_K.
At D=7 the corresponding maximal-order test is even, providing a
guard against incorrectly universalizing the D=163 negative control.

All mathematics uses standard commutative algebra. These facts clarify
the origin of the existing 2-adic source-jet row factor; they do NOT
create an extra Gram valuation or a smaller discriminant bound.
-/

namespace TenthDiscriminant.Phase334
open TenthDiscriminant
open TenthDiscriminant.Phase333
set_option autoImplicit false

/-- Ordinary componentwise addition on integer-pair coordinates. -/
def pairAdd (a b : Int × Int) : Int × Int :=
  (a.1+b.1, a.2+b.2)

/-- A matrix of index two is nevertheless additive on all source pairs. -/
theorem sourceToMaximal_add (a b : Int × Int) :
    sourceToMaximalCoords (pairAdd a b) =
      pairAdd (sourceToMaximalCoords a) (sourceToMaximalCoords b) := by
  apply Prod.ext
  · dsimp [sourceToMaximalCoords, pairAdd]
    ring
  · dsimp [sourceToMaximalCoords, pairAdd]
    ring

theorem sourceToMaximal_one :
    sourceToMaximalCoords (1,0) = (1,0) := by
  rfl

/-- Multiplication in the maximal integral basis (1,ω), where
ω² = ω-(D+1)/4 for D ≡ 3 (mod 4). -/
def maximalMul (D : Nat) (a b : Int × Int) : Int × Int :=
  (a.1*b.1 - (((D : Int)+1)/4)*a.2*b.2,
   a.1*b.2 + a.2*b.1 + a.2*b.2)

/-- The inclusion of the source quadratic order into the maximal
order is multiplicative, not merely an additive change of coordinates.
The source pair multiplication is exactly the original verifier's. -/
theorem sourceToMaximal_mul (D : Nat)
    (hmod : ((D : Int) % 4) = 3)
    (a b : Int × Int) :
    sourceToMaximalCoords (pairMul D a b) =
      maximalMul D (sourceToMaximalCoords a)
        (sourceToMaximalCoords b) := by
  have ht : 4*(((D : Int)+1)/4) = (D : Int)+1 := by omega
  rcases a with ⟨x,y⟩
  rcases b with ⟨u,v⟩
  apply Prod.ext
  · change
      (x*u-(D : Int)*y*v)-(x*v+y*u) =
        (x-y)*(u-v)-(((D : Int)+1)/4)*(2*y)*(2*v)
    calc
      _ = (x-y)*(u-v)-((D : Int)+1)*y*v := by ring
      _ = (x-y)*(u-v)-(4*(((D : Int)+1)/4))*y*v := by rw [ht]
      _ = (x-y)*(u-v)-(((D : Int)+1)/4)*(2*y)*(2*v) := by ring
  · change
      2*(x*v+y*u) =
        (x-y)*(2*v)+(2*y)*(u-v)+(2*y)*(2*v)
    ring

/-- A nonzero nilpotent modulo 2 in the source order:
the residue of 1+√(-D) is nonzero but has square zero. -/
theorem source_mod_two_has_nonzero_nilpotent
    (D : Nat) (hodd : ((D : Int) % 2) = 1) :
    pairDvd 2 (pairMul D (1,1) (1,1)) ∧
      ¬ pairDvd 2 (1,1) := by
  have hfirst : (2 : Int) ∣ 1-(D : Int) := by
    refine ⟨(1-(D : Int))/2, ?_⟩
    omega
  constructor
  · simpa [pairDvd, pairMul] using
      (show (2 : Int) ∣ 1-(D : Int) ∧ (2 : Int) ∣ 2 from
        ⟨hfirst, dvd_refl (2 : Int)⟩)
  · norm_num [pairDvd]

/-- The already-proved source-polynomial result is retained exactly.
This is the SAME pairPow and not a maximal-order statement. -/
theorem original_source_binary_F_even
    (D : Nat) (a : Int × Int) :
    pairDvd 2
      ((pairPow D a 4).1 - (pairPow D a 2).1,
       (pairPow D a 4).2 - (pairPow D a 2).2) := by
  simpa [pairDvd] using binaryNullPower_even D a

/-- Componentwise subtraction in the (1,ω) basis. -/
def pairSub (a b : Int × Int) : Int × Int :=
  (a.1-b.1, a.2-b.2)

/-- Powers computed using the maximal-order multiplication. -/
def maximalPow (D : Nat) (a : Int × Int) : Nat → Int × Int
  | 0 => (1,0)
  | n+1 => maximalMul D (maximalPow D a n) a

/-- Direct, entirely integral control: F(ω) at D=163 is
1681-82ω, and has an odd coefficient. -/
theorem maximal_binary_F_163_exact :
    pairSub (maximalPow 163 (0,1) 4)
      (maximalPow 163 (0,1) 2) = (1681,-82) := by
  decide

/-- Negative control: F(Z)=Z⁴-Z² does not vanish modulo 2
on all elements of the maximal order at D=163. -/
theorem maximal_binary_F_163_not_even :
    ¬ pairDvd 2
      (pairSub (maximalPow 163 (0,1) 4)
        (maximalPow 163 (0,1) 2)) := by
  rw [maximal_binary_F_163_exact]
  norm_num [pairDvd]

/-- Opposite exact control at D=7: the same test DOES vanish.
Do not generalize the D=163 failure to every maximal order. -/
theorem maximal_binary_F_7_exact :
    pairSub (maximalPow 7 (0,1) 4)
      (maximalPow 7 (0,1) 2) = (4,-4) := by
  decide

theorem maximal_binary_F_7_even :
    pairDvd 2
      (pairSub (maximalPow 7 (0,1) 4)
        (maximalPow 7 (0,1) 2)) := by
  rw [maximal_binary_F_7_exact]
  norm_num [pairDvd]

end TenthDiscriminant.Phase334

#print axioms TenthDiscriminant.Phase334.sourceToMaximal_mul
#print axioms TenthDiscriminant.Phase334.source_mod_two_has_nonzero_nilpotent
#print axioms TenthDiscriminant.Phase334.original_source_binary_F_even
#print axioms TenthDiscriminant.Phase334.maximal_binary_F_163_not_even
#print axioms TenthDiscriminant.Phase334.maximal_binary_F_7_even
