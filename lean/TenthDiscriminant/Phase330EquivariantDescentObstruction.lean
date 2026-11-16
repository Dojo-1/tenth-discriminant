import TenthDiscriminant.Phase329IntegralKnotLift
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring

/-!
# Phase330 — two-chart knot: an integral equivariant retraction obstruction

Let M be an additive abelian group. On M x M, C2 swaps the two
entries; on M the action is trivial. The diagonal Delta(x)=(x,x)
is equivariant. An additive return P is equivariant precisely when
P(x,y)=P(y,x). If P*Delta=id, then x=2*P(x,0), so M must be
2-divisible. For a nonzero finite-rank free Z-module this fails.

The result is a *necessary* condition for a symmetric descent of
two conjugate jet charts. It does not prove that the actual unequal
R x S / S x R ordinary-Z jet charts have been identified: the
matching of those domain and derivative types remains independent.

The non-equivariant projection first(x,y)=x still returns exactly
over Z, as in Phase328. In characteristic seven, symmetric averaging
with coefficient four (inverse to two) is possible, but is not an
integral lift in characteristic zero.

No new arithmetic factor, F1' field, or discriminant endpoint claimed.
-/
namespace TenthDiscriminant.Phase330
set_option autoImplicit false

variable {M : Type*} [AddCommGroup M]

/-- An equivariant additive left inverse to the diagonal forces every
element to be twice another element. -/
theorem swap_equivariant_retraction_forces_double
    (P : (M × M) →+ M)
    (hswap : ∀ x y : M, P (x, y) = P (y, x))
    (hretract : ∀ x : M, P (x, x) = x)
    (x : M) :
    P (x, 0) + P (x, 0) = x := by
  have hpair : (x, x) = (x, 0) + (0, x) := by
    ext <;> simp
  calc
    P (x, 0) + P (x, 0) =
      P (x, 0) + P (0, x) := by rw [hswap 0 x]
    _ = P ((x, 0) + (0, x)) := by rw [map_add]
    _ = P (x, x) := by rw [← hpair]
    _ = x := hretract x

/-- Exact no-go for the smallest possible nontrivial integral jet.
This blocks a symmetric integer return from two identical charts. -/
theorem no_integral_swap_equivariant_retraction
    (P : (Int × Int) →+ Int)
    (hswap : ∀ x y : Int, P (x, y) = P (y, x))
    (hretract : ∀ x : Int, P (x, x) = x) :
    False := by
  have h := swap_equivariant_retraction_forces_double P hswap
    hretract (1 : Int)
  omega

/-- The same obstruction on any nonempty free integral row lattice,
including the original Fin (R*S) row space when R*S > 0. -/
theorem no_integral_swap_return_on_fin
    (n : Nat) (hn : 0 < n)
    (P : (((Fin n → Int) × (Fin n → Int))) →+
      (Fin n → Int))
    (hswap : ∀ x y : Fin n → Int, P (x, y) = P (y, x))
    (hretract : ∀ x : Fin n → Int, P (x, x) = x) :
    False := by
  let x : Fin n → Int := fun _ => 1
  have h := swap_equivariant_retraction_forces_double P hswap
    hretract x
  let i : Fin n := ⟨0, hn⟩
  have hi := congrArg (fun v : Fin n → Int => v i) h
  change P (x, 0) i + P (x, 0) i = 1 at hi
  omega

/-- Ordinary first-chart projection is a valid *integral* retraction.
It explicitly fails equivariance under the swap. -/
def firstChartReturn : (Int × Int) →+ Int :=
  { toFun := Prod.fst
    map_zero' := rfl
    map_add' := by intros x y; rfl }

theorem first_chart_integral_retract (x : Int) :
    firstChartReturn (x, x) = x := rfl

theorem first_chart_not_swap_equivariant :
    firstChartReturn ((1 : Int), (0 : Int)) ≠
      firstChartReturn ((0 : Int), (1 : Int)) := by
  decide

/-- Finite characteristic seven has a symmetric return: 4=1/2. -/
def averageSeven (x y : ZMod 7) : ZMod 7 :=
  (4 : ZMod 7) * (x + y)

theorem average_seven_swap (x y : ZMod 7) :
    averageSeven x y = averageSeven y x := by
  simp [averageSeven, add_comm]

theorem average_seven_retract (x : ZMod 7) :
    averageSeven x x = x := by
  change (4 : ZMod 7) * (x + x) = x
  have h8 : (8 : ZMod 7) = 1 := by decide
  calc
    (4 : ZMod 7) * (x + x) = (8 : ZMod 7) * x := by ring
    _ = x := by rw [h8]; ring

/-!
## Positive solution: retain the parity-glued lattice

The integral map W(x,y)=(x+y,x-y) has image exactly the pairs
(u,v) with even difference. It is injective but not surjective
on Z x Z. It diagonalizes chart exchange as (u,v)->(u,-v),
while retaining the index-two integral remainder.

This does not descend to a single chart and does not create
arithmetic prime mass.
-/

/-- Woven two-chart coordinates (symmetric/antisymmetric), as an
integral map rather than a rational averaging projector. -/
def weavePair (xy : Int × Int) : Int × Int :=
  (xy.1 + xy.2, xy.1 - xy.2)

/-- Integral weaving makes the conjugation swap a sign on the
antisymmetric channel. -/
theorem weave_swap (x y : Int) :
    weavePair (y, x) =
      ((weavePair (x, y)).1, -(weavePair (x, y)).2) := by
  simp [weavePair]
  omega

/-- The double weave is precisely multiplication by two. -/
theorem weave_twice (x y : Int) :
    weavePair (weavePair (x, y)) = (2 * x, 2 * y) := by
  simp [weavePair]
  omega

/-- Exact image: two woven channels can be deweaved integrally
if and only if their coordinates have the same parity. -/
theorem weave_image_iff_parity (u v : Int) :
    (∃ xy : Int × Int, weavePair xy = (u, v)) ↔
      (∃ t : Int, u - v = 2 * t) := by
  constructor
  · rintro ⟨⟨x, y⟩, h⟩
    have hu : x + y = u := congrArg Prod.fst h
    have hv : x - y = v := congrArg Prod.snd h
    refine ⟨y, ?_⟩
    omega
  · rintro ⟨t, ht⟩
    refine ⟨(u - t, t), ?_⟩
    apply Prod.ext
    · dsimp [weavePair]
      omega
    · dsimp [weavePair]
      omega

/-- Two-channel weaving is injective over the integers. -/
theorem weave_injective : Function.Injective weavePair := by
  intro a b h
  rcases a with ⟨x, y⟩
  rcases b with ⟨s, t⟩
  have h1 : x + y = s + t := congrArg Prod.fst h
  have h2 : x - y = s - t := congrArg Prod.snd h
  have hx : x = s := by omega
  have hy : y = t := by omega
  simp [hx, hy]

/-- The index-two parity remainder excludes (1,0). -/
theorem weave_not_surjective : ¬ Function.Surjective weavePair := by
  intro h
  obtain ⟨xy, heq⟩ := h ((1 : Int), (0 : Int))
  have hp := (weave_image_iff_parity 1 0).mp ⟨xy, heq⟩
  rcases hp with ⟨t, ht⟩
  omega

end TenthDiscriminant.Phase330

#print axioms TenthDiscriminant.Phase330.swap_equivariant_retraction_forces_double
#print axioms TenthDiscriminant.Phase330.no_integral_swap_equivariant_retraction
#print axioms TenthDiscriminant.Phase330.no_integral_swap_return_on_fin
#print axioms TenthDiscriminant.Phase330.average_seven_retract

#print axioms TenthDiscriminant.Phase330.weave_image_iff_parity
#print axioms TenthDiscriminant.Phase330.weave_injective
#print axioms TenthDiscriminant.Phase330.weave_not_surjective
