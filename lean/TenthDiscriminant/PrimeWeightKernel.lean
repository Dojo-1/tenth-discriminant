import TenthDiscriminant.ExcludedPrimeAssembly
import Mathlib.Analysis.SpecialFunctions.Log.Monotone
import Mathlib.Data.Complex.ExponentialBounds

/-!
# Counting excluded primes pays for their lost determinant factors

The only new arithmetic input is a prefix count bound. Everything converting
that count into a weighted loss is universal and proved here.
-/
open scoped BigOperators
namespace TenthDiscriminant.ExcludedPrime
set_option autoImplicit false
noncomputable section

def primeKernel (n : Nat) : Real := Real.log (n : Real) / (n : Real)

def lossScale (R S : Nat) : Real := ((R * (R-1) * S : Nat) : Real)

theorem valuationWeight_mul_le (R S p : Nat) :
    (2 * valuationWeight R S p) * p ≤ R * (R-1) * S := by
  have hv : valuationWeight R S p ≤ S * (∑ r ∈ Finset.range R, r / p) := by
    unfold valuationWeight
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro r hr
    calc
      _ ≤ ∑ t ∈ Finset.range S, r / p :=
        Finset.sum_le_sum (fun t ht => min_le_left _ _)
      _ = S * (r / p) := by simp
  have hd : (∑ r ∈ Finset.range R, r / p) * p ≤ ∑ r ∈ Finset.range R, r := by
    rw [Finset.sum_mul]
    exact Finset.sum_le_sum (fun r hr => Nat.div_mul_le_self r p)
  calc
    _ ≤ (2 * (S * (∑ r ∈ Finset.range R, r / p))) * p :=
      Nat.mul_le_mul_right p (Nat.mul_le_mul_left 2 hv)
    _ = S * 2 * ((∑ r ∈ Finset.range R, r / p) * p) := by ring
    _ ≤ S * 2 * (∑ r ∈ Finset.range R, r) := Nat.mul_le_mul_left _ hd
    _ = S * ((∑ r ∈ Finset.range R, r) * 2) := by ring
    _ = R * (R-1) * S := by rw [Finset.sum_range_id_mul_two]; ring

theorem weight_le_primeKernel (R S p : Nat) (hp : 0 < p) :
    weight R S p ≤ lossScale R S * primeKernel p := by
  have hpR : (0 : Real) < p := by exact_mod_cast hp
  have hlog : 0 ≤ Real.log (p : Real) := Real.log_nonneg (by exact_mod_cast hp)
  have hv : ((2 * valuationWeight R S p : Nat) : Real) * (p : Real) ≤ lossScale R S := by
    unfold lossScale
    exact_mod_cast valuationWeight_mul_le R S p
  have hdiv := (le_div_iff₀ hpR).mpr hv
  have hm := mul_le_mul_of_nonneg_right hdiv hlog
  unfold weight primeKernel
  calc
    _ ≤ (lossScale R S / (p : Real)) * Real.log (p : Real) := hm
    _ = _ := by ring

theorem primeKernel_nonneg (n : Nat) : 0 ≤ primeKernel n := by
  by_cases hn : n = 0
  · simp [primeKernel, hn]
  · exact div_nonneg (Real.log_nonneg (by exact_mod_cast Nat.one_le_iff_ne_zero.mpr hn))
      (Nat.cast_nonneg n)

theorem primeKernel_antitone (L : Nat) : AntitoneOn primeKernel (Set.Icc 3 L) := by
  intro m hm n hn hmn
  have he : Real.exp 1 ≤ (3 : Real) := by linarith [Real.exp_one_lt_d9]
  have hm3 : (3 : Real) ≤ m := by exact_mod_cast hm.1
  have hn3 : (3 : Real) ≤ n := by exact_mod_cast hn.1
  exact Real.log_div_self_antitoneOn (he.trans hm3) (he.trans hn3)
    (by exact_mod_cast hmn)

theorem excluded_prime_budget_log_div (P G : Finset Nat) (D D2 rho R S L : Nat)
    (B : Nat → Real)
    (hD : 0 < D) (hD2 : D ≤ D2) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hL : 3 ≤ L) (hG : G ⊆ P)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p ≠ 2)
    (hmax : ∀ p ∈ P, p ≤ L) (hns : ∀ p ∈ G, ¬ IsSquare (-(D : ZMod p)))
    (hB : ∀ n, 3 ≤ n → n ≤ L → prefixCount (P\G) n ≤ B n)
    (hradius : (1001/1000 : Real)*
        Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
        10*Real.sqrt D2 ≤ (rho : Real)) :
    mass P R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i)) +
      lossScale R S * kernelCost L primeKernel B := by
  apply excluded_prime_budget P G D D2 rho R S L primeKernel B (lossScale R S)
    hD hD2 hR hS hL hG hprime hodd hmax hns (primeKernel_antitone L)
    (primeKernel_nonneg L) (by unfold lossScale; positivity) hB
  · intro p hp
    exact weight_le_primeKernel R S p (hprime p (Finset.mem_sdiff.mp hp).1).pos
  · exact hradius

theorem nonzero_weight_control : valuationWeight 4 2 3 = 1 ∧ lossScale 4 2 = 24 := by
  norm_num [valuationWeight, Finset.sum_range_succ, lossScale]

theorem zero_scale_control (S : Nat) : lossScale 1 S = 0 := by simp [lossScale]

theorem endpoint_control (B : Nat → Real) : kernelCost 3 primeKernel B = primeKernel 3 * B 3 := by
  simp [kernelCost]

theorem small_domain_rejected : primeKernel 1 < primeKernel 3 := by
  have hlog : 0 < Real.log (3 : Real) := Real.log_pos (by norm_num)
  simpa [primeKernel] using div_pos hlog (by norm_num : (0 : Real) < 3)

end
end TenthDiscriminant.ExcludedPrime

#audit_namespace TenthDiscriminant.ExcludedPrime
