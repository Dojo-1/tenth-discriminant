import TenthDiscriminant.PrimeWeightKernel
import TenthDiscriminant.AxiomAudit

/-! Prime divisors of the parameter have a finite product budget.
This is not yet a theorem identifying field ramification. -/
open scoped BigOperators
namespace TenthDiscriminant.PrimeDivisorLoss
open ExcludedPrime
set_option autoImplicit false
noncomputable section

theorem valuationWeight_uniform (R S p : Nat) :
    2 * valuationWeight R S p ≤ R*S*(S-1) := by
  have hv : valuationWeight R S p ≤ R*(∑ t ∈ Finset.range S, t) := by
    unfold valuationWeight
    calc
      _ ≤ ∑ r ∈ Finset.range R, ∑ t ∈ Finset.range S, t :=
        Finset.sum_le_sum (fun r hr => Finset.sum_le_sum (fun t ht => min_le_right _ _))
      _ = _ := by simp
  calc
    _ ≤ 2*(R*(∑ t ∈ Finset.range S, t)) := Nat.mul_le_mul_left 2 hv
    _ = R*((∑ t ∈ Finset.range S, t)*2) := by ring
    _ = _ := by rw [Finset.sum_range_id_mul_two]; ring

theorem prime_divisor_log_sum (T : Finset Nat) (D : Nat) (hD : 0 < D)
    (hprime : ∀ p ∈ T, p.Prime) (hdiv : ∀ p ∈ T, p ∣ D) :
    (∑ p ∈ T, Real.log (p : Real)) ≤ Real.log (D : Real) := by
  have hp := primePowerProduct_le_det T (fun _ => 1) (D : Int)
    (by exact_mod_cast hD) hprime (by
      intro p hp
      simpa using (show (p : Int) ∣ (D : Int) by exact_mod_cast hdiv p hp))
  simp only [pow_one, Int.natAbs_natCast] at hp
  have hprod : (0 : Real) < (∏ p ∈ T, (p : Real)) :=
    Finset.prod_pos (fun p hp => by exact_mod_cast (hprime p hp).pos)
  have hb : (∏ p ∈ T, (p : Real)) ≤ (D : Real) := by
    rw [← Nat.cast_prod]
    exact_mod_cast hp
  have hl := Real.log_le_log hprod hb
  rw [Real.log_prod T (fun p => (p : Real)) (fun p hp => ne_of_gt (by exact_mod_cast (hprime p hp).pos : (0 : Real) < p))] at hl
  exact hl

theorem prime_divisor_mass (T : Finset Nat) (D R S : Nat) (hD : 0 < D)
    (hprime : ∀ p ∈ T, p.Prime) (hdiv : ∀ p ∈ T, p ∣ D) :
    mass T R S ≤ ((R*S*(S-1) : Nat) : Real)*Real.log (D : Real) := by
  have hw : ∀ p ∈ T, weight R S p ≤
      ((R*S*(S-1) : Nat) : Real)*Real.log (p : Real) := by
    intro p hp
    apply mul_le_mul_of_nonneg_right
    · exact_mod_cast valuationWeight_uniform R S p
    · exact Real.log_nonneg (by exact_mod_cast (hprime p hp).one_le)
  calc
    _ ≤ ∑ p ∈ T, ((R*S*(S-1) : Nat) : Real)*Real.log (p : Real) :=
      Finset.sum_le_sum hw
    _ = ((R*S*(S-1) : Nat) : Real)*(∑ p ∈ T, Real.log (p : Real)) :=
      (Finset.mul_sum ..).symm
    _ ≤ _ := mul_le_mul_of_nonneg_left (prime_divisor_log_sum T D hD hprime hdiv)
      (Nat.cast_nonneg _)

/-- Only non-divisor excluded primes need the prefix-count input. -/
theorem excluded_budget_without_divisors (P G : Finset Nat) (D D2 rho R S L : Nat)
    (B : Nat → Real)
    (hD : 0 < D) (hD2 : D ≤ D2) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hL : 3 ≤ L) (hG : G ⊆ P)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p ≠ 2)
    (hmax : ∀ p ∈ P, p ≤ L) (hns : ∀ p ∈ G, ¬ IsSquare (-(D : ZMod p)))
    (hB : ∀ n, 3 ≤ n → n ≤ L →
      prefixCount ((P\G) \ ((P\G).filter (fun p => p ∣ D))) n ≤ B n)
    (hradius : (1001/1000 : Real)*
        Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
        10*Real.sqrt D2 ≤ (rho : Real)) :
    mass P R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i)) +
      lossScale R S * kernelCost L primeKernel B +
      ((R*S*(S-1) : Nat) : Real)*Real.log (D : Real) := by
  classical
  let E := P\G
  let T := E.filter (fun p => p ∣ D)
  let U := E\T
  have hTE : T ⊆ E := Finset.filter_subset _ _
  have hUP : U ⊆ P := by
    intro p hp
    exact (Finset.mem_sdiff.mp (Finset.mem_sdiff.mp hp).1).1
  have hU : ∀ p ∈ U, 3 ≤ p ∧ p ≤ L := by
    intro p hp
    have hh := hUP hp
    have h2 := (hprime p hh).two_le
    exact ⟨by have hn := hodd p hh; omega, hmax p hh⟩
  have hg := good_mass_bound G D D2 rho R S hD hD2 hR hS
    (fun p hp => hprime p (hG hp)) (fun p hp => hodd p (hG hp)) hns hradius
  have ht := prime_divisor_mass T D R S hD
    (fun p hp => hprime p (Finset.mem_sdiff.mp (hTE hp)).1)
    (fun p hp => (Finset.mem_filter.mp hp).2)
  have hu : mass U R S ≤ lossScale R S*kernelCost L primeKernel B := by
    calc
      _ ≤ ∑ p ∈ U, lossScale R S*primeKernel p := Finset.sum_le_sum (fun p hp =>
        weight_le_primeKernel R S p (hprime p (hUP hp)).pos)
      _ = lossScale R S*(∑ p ∈ U, primeKernel p) := (Finset.mul_sum ..).symm
      _ ≤ _ := mul_le_mul_of_nonneg_left
        (count_transfer U L primeKernel B hL hU (primeKernel_antitone L)
          (primeKernel_nonneg L) hB) (by unfold lossScale; positivity)
  have hpartP : mass E R S + mass G R S = mass P R S := by
    exact Finset.sum_sdiff hG
  have hpartE : mass U R S + mass T R S = mass E R S := by
    exact Finset.sum_sdiff hTE
  linarith

theorem one_column_control (R p : Nat) : valuationWeight R 1 p = 0 := by
  simp [valuationWeight]

theorem divisor_pair_control :
    (∏ p ∈ ({3,5} : Finset Nat), p) = 15 ∧
    mass {3,5} 4 2 ≤ (8 : Real)*Real.log 15 := by
  constructor
  · norm_num
  · simpa using prime_divisor_mass {3,5} 15 4 2 (by norm_num)
      (by intro p hp; simp only [Finset.mem_insert, Finset.mem_singleton] at hp
          rcases hp with rfl | rfl <;> norm_num)
      (by intro p hp; simp only [Finset.mem_insert, Finset.mem_singleton] at hp
          rcases hp with rfl | rfl <;> norm_num)

theorem empty_control (R S : Nat) : mass ∅ R S = 0 := by simp [mass]

theorem unit_parameter_control (T : Finset Nat)
    (hprime : ∀ p ∈ T, p.Prime) (hdiv : ∀ p ∈ T, p ∣ 1) : T = ∅ := by
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro p hp
  have he := Nat.dvd_one.mp (hdiv p hp)
  have h2 := (hprime p hp).two_le
  omega

theorem divisibility_guard_needed :
    ¬ mass {3} 4 2 ≤ ((4*2*(2-1) : Nat) : Real)*Real.log (1 : Real) := by
  have hl : 0 < Real.log (3 : Real) := Real.log_pos (by norm_num)
  norm_num [mass, weight, valuationWeight, Finset.sum_range_succ] at *
  linarith
end
end TenthDiscriminant.PrimeDivisorLoss

#check TenthDiscriminant.PrimeDivisorLoss.excluded_budget_without_divisors
#print axioms TenthDiscriminant.PrimeDivisorLoss.prime_divisor_log_sum
#print axioms TenthDiscriminant.PrimeDivisorLoss.prime_divisor_mass
#print axioms TenthDiscriminant.PrimeDivisorLoss.excluded_budget_without_divisors
#audit_namespace TenthDiscriminant.PrimeDivisorLoss
