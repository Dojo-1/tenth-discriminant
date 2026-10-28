import TenthDiscriminant.EvenMinkowski
import TenthDiscriminant.UniformTwoClass

/-! A full all-range contradiction for the actual even quadratic chart. -/
open scoped BigOperators NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.EvenTwoClass
open FirstCertificate ExcludedPrime ClosedKernel OddMinkowski UniformTwoClass
set_option autoImplicit false
noncomputable section

theorem even_classNumber_gt_two (D : Nat) (hD : 2^50≤D)
    [Fact (0<D)] (hsq : Squarefree D) (hm : (D : Int)%4=1 ∨ (D : Int)%4=2) :
    2<NumberField.classNumber (EvenQuadraticField D) := by
  by_contra hn
  have hc : NumberField.classNumber (EvenQuadraticField D)≤2 := le_of_not_gt hn
  have hgeom : 41006250000≤D := by omega
  have hfifty : 50000000000≤D := by omega
  let r := Tuned.R D
  let s := Tuned.S D
  let rho := Tuned.rho D
  let n := ellipsePaddedUpperCount D rho (ellipseVerticalBound D rho)
  let P := oddPrimesBelow r
  have hd := Tuned.dimensions D hgeom
  have hr : 2≤r := by dsimp [r]; omega
  have hs : 1≤s := by dsimp [s]; omega
  have hRS : r≤10000*s := hd.2.2.2.1
  have h25 : 25*s≤r := by dsimp [s,Tuned.S]; exact Nat.mul_div_le _ _
  have hrD : r≤D := by dsimp [r,Tuned.R,envelopeR]; exact Nat.div_le_self _ _
  have hmem (p : Nat) (hp : p ∈ P) : p<r ∧ p.Prime ∧ p≠2 := by
    simpa only [P,oddPrimesBelow,Finset.mem_filter,Finset.mem_range] using hp
  have hbudget := EvenMinkowski.scalar_actual_gram_budget D hsq hm hc P D rho r s r
    le_rfl (by omega) hs (by omega)
    (fun p hp => (hmem p hp).2.1) (fun p hp => (hmem p hp).2.2)
    (fun p hp => (hmem p hp).1.le) (Tuned.chosen_radius D hgeom)
  change exactOddPrimeMass r s ≤ Real.log (Finset.univ.prod (fun i =>
    rectangularTraceGram (ellipsePoints D rho) s r s i i))+
    lossScale r s*chartCost D r+((r*s*(s-1) : Nat) : Real)*Real.log D at hbudget
  have hdiag := ellipseTraceGram_log_diag_le_upperB D D rho r s n
    (by omega) le_rfl (by omega) hs (Tuned.radius_lt_R D hgeom) (Tuned.chosen_radius D hgeom)
    (ellipsePairs_card_le_padded_upper_count D D rho (ellipseVerticalBound D rho) (by omega) le_rfl le_rfl)
  have ht := certifiedPrimeMassLower_antitone_tail r s hs FirstEnderInterval.tail_le_budget
  have hrec : recoveredPrimeMassLower r s FirstEnderInterval.tailBudget≤
      recoveredPrimeMassLower r s (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith
  have hmass := hrec.trans ((recoveredPrimeMassLower_le_production r s (enderTailIntegral 10000) hr hs).trans
    (enderPrimeMassLower_le_exact_production r s 10000 hr hs (by norm_num) hRS))
  have htotal : recoveredPrimeMassLower r s FirstEnderInterval.tailBudget≤
      enderUpperB r s s rho n+lossScale r s*chartCost D r+
      ((r*s*(s-1) : Nat) : Real)*Real.log D := by linarith
  have hscale := comparisonScale_pos r s (by omega) (by omega)
  have hloss := loss_cost_ratio r s (chartCost D r) (by omega) (by omega)
    (chart_cost_uniform D r hD (by omega) hrD)
  have hu := (uniform_envelope D hD).2
  have hdiv := divisor_cost_ratio r s (Real.log D) (by omega) (by omega) h25 (by linarith)
  have hnorm := div_le_div_of_nonneg_right htotal hscale.le
  rw [add_div,add_div] at hnorm
  have hlo := Tuned.fifty_normalized_lower D hfifty
  have hhi := Tuned.normalized_upper D hgeom
  change (999997/1000000 : Real)*Real.log D-5739/1000≤
    recoveredPrimeMassLower r s FirstEnderInterval.tailBudget/comparisonScale r s at hlo
  change enderUpperB r s s rho n/comparisonScale r s≤(4/5 : Real)*Real.log D-813/1000 at hhi
  have hsep := scalar_separation (Real.log D) hu
  linarith only [hnorm,hloss,hdiv,hlo,hhi,hsep]

theorem even_radicand_bound (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2) : D<2^50 := by
  by_contra hn
  exact (not_lt_of_ge h) (even_classNumber_gt_two D (by omega) hsq hm)

theorem even_discriminant_bound (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2)
    (h : NumberField.classNumber (EvenQuadraticField D)≤2) :
    (NumberField.discr (EvenQuadraticField D)).natAbs<4*2^50 := by
  have hr := even_radicand_bound D hsq hm h
  have he : (NumberField.discr (EvenQuadraticField D)).natAbs=4*D := by
    rw [even_actual_discr D hsq hm]
    simp [Int.natAbs_mul]
  rw [he]
  omega

theorem endpoint_control : (2 : Nat)^50=1125899906842624 ∧
    4*(2 : Nat)^50=4503599627370496 := by norm_num

theorem factor_four_control : ¬ 4*(2 : Nat)^50=(2 : Nat)^50 := by norm_num

theorem mod_chart_control : ¬ ((3 : Int)%4=1 ∨ (3 : Int)%4=2) := by decide

theorem rational_margin_control :
    (159997/1000000 : Real)*(693/20)-4926/1000-3/5=1789605/100000000 ∧
      0<(159997/1000000 : Real)*(693/20)-4926/1000-3/5 := by norm_num
end
end TenthDiscriminant.EvenTwoClass

#check TenthDiscriminant.EvenTwoClass.even_classNumber_gt_two
#check TenthDiscriminant.EvenTwoClass.even_radicand_bound
#check TenthDiscriminant.EvenTwoClass.even_discriminant_bound
#check TenthDiscriminant.EvenTwoClass.endpoint_control
#check TenthDiscriminant.EvenTwoClass.factor_four_control
#check TenthDiscriminant.EvenTwoClass.mod_chart_control
#check TenthDiscriminant.EvenTwoClass.rational_margin_control
#print axioms TenthDiscriminant.EvenTwoClass.even_classNumber_gt_two
#print axioms TenthDiscriminant.EvenTwoClass.even_radicand_bound
#print axioms TenthDiscriminant.EvenTwoClass.even_discriminant_bound
#audit_namespace TenthDiscriminant.EvenTwoClass

