import TenthDiscriminant

/-! Prime factorization, not an ellipse estimate, controls the zero row.
The final finite aggregation theorem is conditional on the nonzero-row
counts and on four representations per counted prime. -/
open scoped BigOperators
namespace TenthDiscriminant.PrimeAxisRepair
set_option autoImplicit false
noncomputable section

def form (a : Nat) (b c x y : Int) : Int := a*x^2+b*x*y+c*y^2

theorem axis_prime_iff (a p : Nat) (x : Int) (hp : p.Prime) :
    (a : Int)*x^2 = (p : Int) ↔ a=p ∧ (x=1 ∨ x= -1) := by
  constructor
  · intro hx
    have he : a*x.natAbs^2=p := by
      have hh := congrArg Int.natAbs hx
      simpa only [Int.natAbs_mul, Int.natAbs_pow, Int.natAbs_ofNat] using hh
    have hprime : (a*x.natAbs^2).Prime := he.symm ▸ hp
    rcases Nat.prime_mul_iff.mp hprime with ⟨ha, hu⟩ | ⟨hsq, ha⟩
    · have hxone : x.natAbs=1 := by simpa [Nat.pow_eq_one] using hu
      exact ⟨by simpa only [hu, mul_one] using he,
        by simpa using Int.natAbs_eq_iff.mp hxone⟩
    · exact False.elim ((Nat.Prime.not_prime_pow (by decide : 2 ≤ 2)) hsq)
  · rintro ⟨rfl, hx | hx⟩ <;> rw [hx] <;> simp

theorem form_axis_prime_iff (a p : Nat) (b c x : Int) (hp : p.Prime) :
    form a b c x 0 = (p : Int) ↔ a=p ∧ (x=1 ∨ x= -1) := by
  simpa [form] using axis_prime_iff a p x hp

def primeAxis (a : Nat) (U : Finset Int) : Finset Int := by
  classical
  exact U.filter (fun x => ∃ p : Nat, p.Prime ∧ (a : Int)*x^2=(p : Int))

theorem mem_primeAxis (a : Nat) (U : Finset Int) (x : Int) :
    x ∈ primeAxis a U ↔ x ∈ U ∧ a.Prime ∧ (x=1 ∨ x= -1) := by
  classical
  simp only [primeAxis, Finset.mem_filter]
  constructor
  · rintro ⟨hx, p, hp, he⟩
    have hh := (axis_prime_iff a p x hp).mp he
    exact ⟨hx, hh.1.symm ▸ hp, hh.2⟩
  · rintro ⟨hx, ha, hu⟩
    exact ⟨hx, a, ha, (axis_prime_iff a a x ha).mpr ⟨rfl, hu⟩⟩

theorem primeAxis_card_le_two (a : Nat) (U : Finset Int) :
    (primeAxis a U).card ≤ 2 := by
  have hs : primeAxis a U ⊆ ({-1,1} : Finset Int) := by
    intro x hx
    have hh := (mem_primeAxis a U x).mp hx
    simpa only [Finset.mem_insert, Finset.mem_singleton] using hh.2.2.symm
  exact (Finset.card_le_card hs).trans (by decide)

theorem principal_axis_empty (U : Finset Int) : primeAxis 1 U = ∅ := by
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro x hx
  have hh := (mem_primeAxis 1 U x).mp hx
  exact Nat.not_prime_one hh.2.1

theorem two_class_accounting {ι : Type} [DecidableEq ι]
    (I : Finset ι) (j : ι) (hj : j ∈ I) (hI : I.card ≤ 2)
    (q beta : ι → Real) (A N : Real)
    (hrows : ∀ i ∈ I, q i ≤ A+beta i+(if i=j then 0 else 2))
    (hfour : 4*N ≤ ∑ i ∈ I, q i) :
    N ≤ ((I.card : Real)*A + (∑ i ∈ I, beta i) + I.card)/4 := by
  have hzero : (∑ i ∈ I, if i=j then (0 : Real) else 2) = 2*(I.card : Real)-2 := by
    calc
      _ = ∑ i ∈ I, (2-(if i=j then (2 : Real) else 0)) := by
        apply Finset.sum_congr rfl
        intro i hi
        split_ifs <;> norm_num
      _ = _ := by rw [Finset.sum_sub_distrib]; simp [hj]; ring
  have hsum : (∑ i ∈ I, q i) ≤
      (I.card : Real)*A + (∑ i ∈ I, beta i) + 2*(I.card : Real)-2 := by
    calc
      _ ≤ ∑ i ∈ I, (A+beta i+(if i=j then 0 else 2)) :=
        Finset.sum_le_sum hrows
      _ = _ := by rw [Finset.sum_add_distrib, Finset.sum_add_distrib, hzero]; simp; ring
  have hc : (I.card : Real) ≤ 2 := by exact_mod_cast hI
  linarith

theorem counterexample_axis_control :
    primeAxis 3 ({-1,0,1} : Finset Int) = {-1,1} ∧
    form 3 1 1001 1 0=3 ∧ form 3 1 1001 (-1) 0=3 := by
  constructor
  · ext x
    norm_num [mem_primeAxis]
    omega
  · norm_num [form]

theorem principal_card_control (U : Finset Int) : (primeAxis 1 U).card=0 := by
  rw [principal_axis_empty]
  rfl

end
end TenthDiscriminant.PrimeAxisRepair

#audit_namespace TenthDiscriminant.PrimeAxisRepair
#print axioms TenthDiscriminant.PrimeAxisRepair.axis_prime_iff
#print axioms TenthDiscriminant.PrimeAxisRepair.two_class_accounting
