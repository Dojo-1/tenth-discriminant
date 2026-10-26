import TenthDiscriminant.UniformPrimeMassCertified

/-! Recover the exact existing3/5 weights omitted by the>=7 uniform proxy.
This changes no valuation, production expression or discriminant cutoff. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

def small35Mass (R S : Nat) : Real :=
  (valuationWeight R S 3 : Real)*Real.log 3 +
    (valuationWeight R S 5 : Real)*Real.log 5

def retainedSevenMass (R S : Nat) : Real :=
  ∑ p ∈ retainedSmallPrimes 7 10000, (valuationWeight R S p : Real)*Real.log p

def recoveredPrimeMassLower (R S : Nat) (I : Real) : Real :=
  certifiedPrimeMassLower R S I + 2*small35Mass R S

theorem small35Mass_nonneg (R S : Nat) : 0 ≤ small35Mass R S := by
  unfold small35Mass
  exact add_nonneg
    (mul_nonneg (Nat.cast_nonneg _) (Real.log_nonneg (by norm_num)))
    (mul_nonneg (Nat.cast_nonneg _) (Real.log_nonneg (by norm_num)))

theorem retainedSevenMass_nonneg (R S : Nat) : 0 ≤ retainedSevenMass R S := by
  apply Finset.sum_nonneg
  intro p hp
  have h7 := (Finset.mem_filter.mp hp).2
  exact mul_nonneg (Nat.cast_nonneg _)
    (Real.log_nonneg (by exact_mod_cast (by omega : 1 ≤ p)))

/-- The recovered primes and the retained set are disjoint parts of the
original production small-prime sum; no weight is counted twice. -/
theorem small35_add_retained_le_production (R S : Nat) :
    small35Mass R S + retainedSevenMass R S ≤ smallOddValuationMass R S 10000 := by
  let T := retainedSmallPrimes 7 10000
  have h3 : (3 : Nat) ∉ insert 5 T := by simp [T, retainedSmallPrimes]
  have h5 : (5 : Nat) ∉ T := by simp [T, retainedSmallPrimes]
  have hsub : insert 3 (insert 5 T) ⊆
      (productionSmallPrimes 10000).filter (fun p => p ≠ 2) := by
    intro p hp
    simp only [Finset.mem_insert] at hp
    rcases hp with rfl | rfl | hp
    · norm_num [productionSmallPrimes]
    · norm_num [productionSmallPrimes]
    · rcases Finset.mem_filter.mp hp with ⟨hprod,h7⟩
      exact Finset.mem_filter.mpr ⟨hprod,by omega⟩
  rw [smallOddValuationMass_eq_padded]
  calc
    _ = ∑ p ∈ insert 3 (insert 5 T), (valuationWeight R S p : Real)*Real.log p := by
      rw [Finset.sum_insert h3, Finset.sum_insert h5]
      unfold small35Mass retainedSevenMass
      dsimp [T]
      ring
    _ ≤ _ := Finset.sum_le_sum_of_subset_of_nonneg hsub (by
      intro p hp hnot
      have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).2
      exact mul_nonneg (Nat.cast_nonneg _)
        (Real.log_nonneg (by exact_mod_cast hprime.one_le)))

theorem certifiedSmallOddLower_le_retained (R S : Nat) (hS : 1 ≤ S) :
    certifiedSmallOddLower R S ≤ retainedSevenMass R S := by
  have ha : (0 : Real) ≤ (S : Real)-1/2 := by
    have h : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have hb := mul_le_mul_of_nonneg_left certified_prime_log_constants.2.1
    (mul_nonneg ha (triangularMass_nonneg R))
  have he := mul_le_mul_of_nonneg_left certified_prime_log_constants.2.2.2
    (mul_nonneg ha (Nat.cast_nonneg R))
  have hc := mul_le_mul_of_nonneg_left certified_prime_log_constants.2.2.1 (squareMass_nonneg R)
  have hcert : certifiedSmallOddLower R S ≤ uniformSmallOddLower R S 7 10000 := by
    unfold certifiedSmallOddLower uniformSmallOddLower
    linarith
  have hsum : uniformSmallOddLower R S 7 10000 =
      ∑ p ∈ retainedSmallPrimes 7 10000, uniformValuationLower R S p*Real.log p := by
    unfold uniformSmallOddLower primeLogLinearConstant primeLogSquareConstant primeLogErrorConstant
    rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, Finset.sum_div,
      ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro p hp
    unfold uniformValuationLower
    ring
  apply hcert.trans
  rw [hsum]
  apply Finset.sum_le_sum
  intro p hp
  have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).2
  exact mul_le_mul_of_nonneg_right (uniformValuationLower_le R S p hS hprime.pos)
    (Real.log_nonneg (by exact_mod_cast hprime.one_le))

/-- A larger certified proxy for the SAME production mass. Its recovery
uses primes omitted by the proxy, not new divisibility of the determinant. -/
theorem recoveredPrimeMassLower_le_production (R S : Nat) (I : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) :
    recoveredPrimeMassLower R S I ≤ enderPrimeMassLower R S 10000 I := by
  have hm := max_le (certifiedSmallOddLower_le_retained R S hS) (retainedSevenMass_nonneg R S)
  have hs : max (certifiedSmallOddLower R S) 0 + small35Mass R S ≤
      smallOddValuationMass R S 10000 := by
    linarith [small35_add_retained_le_production R S]
  have hf := factorialSmallMass_le_certified R hR
  have ha : (0 : Real) ≤ (S : Real)-1/2 := by
    have h : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have ht : ((S : Real)-1/2)*
      (factorialLower R-certifiedFactorialUpper R-triangularMass R*I)-squareMass R*I/2 ≤
      enderTailLower R S 10000 I := by
    unfold enderTailLower
    nlinarith
  have hmax := max_le_max ht (le_refl (0 : Real))
  unfold recoveredPrimeMassLower certifiedPrimeMassLower enderPrimeMassLower
  linarith

theorem small35Mass_pos (R S : Nat) (hR : 4 ≤ R) (hS : 2 ≤ S) :
    0 < small35Mass R S := by
  have ht : min (3/3) 1 ≤ ∑ t ∈ Finset.range S, min (3/3) t :=
    Finset.single_le_sum (fun _ _ => Nat.zero_le _) (Finset.mem_range.mpr (by omega))
  have hr : (∑ t ∈ Finset.range S, min (3/3) t) ≤ valuationWeight R S 3 := by
    unfold valuationWeight
    exact Finset.single_le_sum
      (f := fun r : Nat => ∑ t ∈ Finset.range S, min (r/3) t)
      (fun _ _ => Nat.zero_le _)
      (show (3 : Nat) ∈ Finset.range R from Finset.mem_range.mpr (by omega))
  have hF : (0 : Real) < valuationWeight R S 3 := by
    have hnat : 0 < valuationWeight R S 3 :=
      lt_of_lt_of_le (by decide : 0 < min (3/3 : Nat) 1) (ht.trans hr)
    exact_mod_cast hnat
  have h3 := mul_pos hF (Real.log_pos (by norm_num : (1 : Real)<3))
  have h5 := mul_nonneg (Nat.cast_nonneg (valuationWeight R S 5))
    (Real.log_nonneg (by norm_num : (1 : Real)≤5))
  unfold small35Mass
  linarith

theorem certified_lt_recoveredPrimeMassLower (R S : Nat) (I : Real)
    (hR : 4 ≤ R) (hS : 2 ≤ S) :
    certifiedPrimeMassLower R S I < recoveredPrimeMassLower R S I := by
  unfold recoveredPrimeMassLower
  linarith [small35Mass_pos R S hR hS]

theorem recovered_four_two_control (I : Real) :
    recoveredPrimeMassLower 4 2 I = certifiedPrimeMassLower 4 2 I + 2*Real.log 3 := by
  norm_num [recoveredPrimeMassLower, small35Mass, valuationWeight, Finset.sum_range_succ]

theorem recovered_three_two_zero_control (I : Real) :
    recoveredPrimeMassLower 3 2 I = certifiedPrimeMassLower 3 2 I := by
  norm_num [recoveredPrimeMassLower, small35Mass, valuationWeight, Finset.sum_range_succ]

end
end TenthDiscriminant.FirstCertificate
