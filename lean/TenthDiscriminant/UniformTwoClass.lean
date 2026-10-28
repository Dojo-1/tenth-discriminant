import TenthDiscriminant.OddMinkowski
import TenthDiscriminant.FiftyBillionCutoff

/-! An all-range comparison, independent of the sampled feasibility grid. -/
open scoped BigOperators NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.UniformTwoClass
open FirstCertificate ExcludedPrime ClosedKernel OddMinkowski
set_option autoImplicit false
noncomputable section

def q (u : Real) : Real := 2+u*(1+u)
def Hlog (u : Real) : Real := (4*Real.exp (-(u/2))+Real.exp (-(u/4)))*q u+1/3

theorem q_growth (a v : Real) (ha : 9≤a) (hv : 0≤v) :
    q (a+v) ≤ q a*Real.exp (v/4) := by
  have h32 : 32≤q a := by unfold q; nlinarith
  have hc : 4*(1+2*a)≤q a := by unfold q; nlinarith
  have h1 := mul_le_mul_of_nonneg_right (show 1+2*a≤q a/4 by linarith) hv
  have h2 := mul_le_mul_of_nonneg_right (show (1 : Real)≤q a/32 by linarith) (sq_nonneg v)
  have hid : q (a+v)=q a+(1+2*a)*v+v^2 := by unfold q; ring
  calc
    _ ≤ q a*(1+v/4+(v/4)^2/2) := by rw [hid]; nlinarith only [h1,h2]
    _ ≤ _ := mul_le_mul_of_nonneg_left
      (Real.quadratic_le_exp_of_nonneg (by linarith : 0≤v/4)) (by linarith : 0≤q a)

theorem q_decay_quarter (a u : Real) (ha : 9≤a) (hau : a≤u) :
    q u*Real.exp (-(u/4)) ≤ q a*Real.exp (-(a/4)) := by
  have hg := q_growth a (u-a) ha (sub_nonneg.mpr hau)
  rw [show a+(u-a)=u by ring] at hg
  calc
    _ ≤ (q a*Real.exp ((u-a)/4))*Real.exp (-(u/4)) :=
      mul_le_mul_of_nonneg_right hg (Real.exp_pos _).le
    _ = _ := by rw [mul_assoc,←Real.exp_add,show (u-a)/4+-(u/4)=-(a/4) by ring]

theorem q_decay_half (a u : Real) (ha : 9≤a) (hau : a≤u) :
    q u*Real.exp (-(u/2)) ≤ q a*Real.exp (-(a/2)) := by
  have hg := q_growth a (u-a) ha (sub_nonneg.mpr hau)
  rw [show a+(u-a)=u by ring] at hg
  have he : Real.exp ((u-a)/4)≤Real.exp ((u-a)/2) := Real.exp_le_exp.mpr (by linarith)
  have hq : 0≤q a := by unfold q; positivity
  have hg2 := hg.trans (mul_le_mul_of_nonneg_left he hq)
  calc
    _ ≤ (q a*Real.exp ((u-a)/2))*Real.exp (-(u/2)) :=
      mul_le_mul_of_nonneg_right hg2 (Real.exp_pos _).le
    _ = _ := by rw [mul_assoc,←Real.exp_add,show (u-a)/2+-(u/2)=-(a/2) by ring]

theorem envelope_antitone (a u : Real) (ha : 9≤a) (hau : a≤u) : Hlog u≤Hlog a := by
  have hq := q_decay_quarter a u ha hau
  have hh := q_decay_half a u ha hau
  unfold Hlog
  nlinarith only [hq,hh]

theorem quarter_exp (D : Nat) (hD : 0<D) : Real.exp (Real.log (D : Real)/4)=fourthRoot D := by
  have ht : 0<fourthRoot D := by unfold fourthRoot; positivity
  have he : Real.log (fourthRoot D)=Real.log (D : Real)/4 := by
    unfold fourthRoot
    rw [Real.log_sqrt (Real.sqrt_nonneg _),Real.log_sqrt (Nat.cast_nonneg D)]
    ring
  rw [←he,Real.exp_log ht]

theorem half_exp (D : Nat) (hD : 0<D) : Real.exp (Real.log (D : Real)/2)=Real.sqrt D := by
  rw [←Real.log_sqrt (Nat.cast_nonneg D),Real.exp_log (by positivity : 0<Real.sqrt (D : Real))]

theorem slope_root (t : Real) (ht : 0<t) :
    linearSlope (t^4) ((2/Real.pi)*t^2) ≤ 4/t^2+1/t := by
  have hq : 0≤(2 : Real)/(3*Real.pi) := by positivity
  have hs := Real.sq_sqrt hq
  have hn := Real.sqrt_nonneg ((2 : Real)/(3*Real.pi))
  have hr : (2 : Real)/(3*Real.pi)≤1/4 :=
    (div_le_iff₀ (by positivity : 0<3*Real.pi)).mpr (by linarith [Real.pi_gt_three])
  have hc : 2*Real.sqrt ((2 : Real)/(3*Real.pi))≤1 := by nlinarith
  have hsqrt : Real.sqrt (t^4)=t^2 := by
    rw [show t^4=(t^2)^2 by ring,Real.sqrt_sq (sq_nonneg t)]
  have harg : ((2/Real.pi)*t^2)/(3*t^4)=(2/(3*Real.pi))*(1/t)^2 := by
    field_simp [ht.ne',Real.pi_ne_zero]
    ring
  unfold linearSlope
  rw [hsqrt,harg,Real.sqrt_mul hq,Real.sqrt_sq (by positivity : 0≤1/t)]
  have hp := div_le_div_of_nonneg_right Real.pi_lt_four.le (sq_nonneg t)
  have hm := mul_le_mul_of_nonneg_right hc (by positivity : 0≤1/t)
  nlinarith only [hp,hm]

theorem slope_exp (D : Nat) (hD : 0<D) :
    linearSlope D ((2/Real.pi)*Real.sqrt D) ≤
      4*Real.exp (-(Real.log D/2))+Real.exp (-(Real.log D/4)) := by
  have hi := fourthRoot_identities D
  have ht : 0<fourthRoot D := by unfold fourthRoot; positivity
  have hh := slope_root (fourthRoot D) ht
  rw [hi.2.1,hi.2.2] at hh
  rw [Real.exp_neg,Real.exp_neg,half_exp D hD,quarter_exp D hD]
  convert hh using 1 <;> ring

theorem chart_cost_majorant (D L : Nat) (hD : 0<D) (hL : 3≤L) (hLD : L≤D) :
    chartCost D L ≤ Hlog (Real.log D) := by
  have hu : 0≤Real.log (D : Real) := Real.log_nonneg (by exact_mod_cast hD)
  have hv : 0≤Real.log (L : Real) := Real.log_nonneg (by exact_mod_cast (by omega : 1≤L))
  have hlog : Real.log (L : Real)≤Real.log D :=
    Real.log_le_log (by exact_mod_cast (by omega : 0<L)) (by exact_mod_cast hLD)
  have h3 : Real.log (3 : Real)≤2 := by
    have hh := Real.log_le_sub_one_of_pos (by norm_num : (0 : Real)<3)
    linarith
  have hp : Real.log 3+Real.log L*(1+Real.log L)≤q (Real.log D) := by
    have hm := mul_le_mul hlog (add_le_add_left hlog 1) (by linarith : 0≤1+Real.log (L : Real)) hu
    unfold q
    linarith
  have ha : 0≤linearSlope D ((2/Real.pi)*Real.sqrt D) := by unfold linearSlope; positivity
  have hq : 0≤q (Real.log D) := by unfold q; positivity
  change linearSlope D ((2/Real.pi)*Real.sqrt D)*(Real.log 3+Real.log L*(1+Real.log L))+Real.log 3/6 ≤ _
  calc
    _ ≤ linearSlope D ((2/Real.pi)*Real.sqrt D)*q (Real.log D)+1/3 :=
      add_le_add (mul_le_mul_of_nonneg_left hp ha) (by linarith)
    _ ≤ _ := add_le_add_right (mul_le_mul_of_nonneg_right (slope_exp D hD) hq) _

theorem endpoint_log_bounds :
    (693/20 : Real)≤Real.log ((2^50 : Nat) : Real) ∧ Real.log ((2^50 : Nat) : Real)≤35 := by
  have he : Real.log ((2^50 : Nat) : Real)=50*Real.log 2 := by
    rw [Nat.cast_pow,Real.log_pow]
    norm_num
  rw [he]
  constructor <;> linarith [Real.log_two_gt_d9,Real.log_two_lt_d9]

theorem endpoint_envelope : Hlog (Real.log ((2^50 : Nat) : Real))≤3/5 := by
  let u := Real.log ((2^50 : Nat) : Real)
  have hu := endpoint_log_bounds
  have he : u=50*Real.log 2 := by
    have hz : Real.log ((2^50 : Nat) : Real)=50*Real.log 2 := by
      rw [Nat.cast_pow,Real.log_pow]
      norm_num
    exact hz
  have hhalf : Real.exp (-(u/2))=1/(2^25 : Real) := by
    rw [he,show -(50*Real.log 2/2)=-(Real.log ((2 : Real)^25)) by rw [Real.log_pow]; ring]
    rw [Real.exp_neg,Real.exp_log (by positivity)]
    simp only [one_div]
  have ht : (5000 : Real)≤fourthRoot (2^50) := by
    unfold fourthRoot
    apply Real.le_sqrt_of_sq_le
    apply Real.le_sqrt_of_sq_le
    norm_num
  have hquarter : Real.exp (-(u/4))≤1/5000 := by
    have hexp : Real.exp (u/4)=fourthRoot (2^50) := quarter_exp (2^50) (by norm_num)
    rw [Real.exp_neg,hexp]
    simpa only [one_div] using one_div_le_one_div_of_le (by norm_num : (0 : Real)<5000) ht
  have hq : q u≤1262 := by
    have hmul := mul_nonneg (show 0≤35-u by exact sub_nonneg.mpr hu.2)
      (show 0≤35+u+1 by dsimp [u]; linarith [hu.1])
    unfold q
    nlinarith only [hmul]
  have hc : 4*Real.exp (-(u/2))+Real.exp (-(u/4))≤4/(2^25 : Real)+1/5000 := by
    rw [hhalf]
    linarith
  have hm1 := mul_le_mul_of_nonneg_left hq
    (by positivity : 0≤4*Real.exp (-(u/2))+Real.exp (-(u/4)))
  have hm2 := mul_le_mul_of_nonneg_right hc (by norm_num : (0 : Real)≤1262)
  change (4*Real.exp (-(u/2))+Real.exp (-(u/4)))*q u+1/3≤3/5
  norm_num at hm2
  nlinarith only [hm1,hm2]

theorem uniform_envelope (D : Nat) (hD : 2^50≤D) :
    Hlog (Real.log D)≤3/5 ∧ (693/20 : Real)≤Real.log D := by
  have hl : Real.log ((2^50 : Nat) : Real)≤Real.log (D : Real) :=
    Real.log_le_log (by norm_num) (by exact_mod_cast hD)
  have he := endpoint_log_bounds
  have ha : (9 : Real)≤Real.log ((2^50 : Nat) : Real) :=
    (show (9 : Real)≤693/20 by norm_num).trans he.1
  have hb := envelope_antitone (Real.log ((2^50 : Nat) : Real)) (Real.log (D : Real)) ha hl
  exact ⟨hb.trans endpoint_envelope,he.1.trans hl⟩

theorem chart_cost_uniform (D L : Nat) (hD : 2^50≤D) (hL : 3≤L) (hLD : L≤D) :
    chartCost D L≤3/5 :=
  (chart_cost_majorant D L (by omega) hL hLD).trans (uniform_envelope D hD).1

theorem loss_cost_ratio (R S : Nat) (C : Real) (hR : 0<R) (hS : 0<S) (hC : C≤3/5) :
    lossScale R S*C/comparisonScale R S≤3/5 := by
  have hi : R*(R-1)*S≤R*R*S := Nat.mul_le_mul_right S (Nat.mul_le_mul_left R (Nat.sub_le R 1))
  have hr : lossScale R S≤comparisonScale R S := by
    simpa only [lossScale,comparisonScale,pow_two,Nat.cast_mul] using (show ((R*(R-1)*S : Nat) : Real)≤((R*R*S : Nat) : Real) by exact_mod_cast hi)
  have ha : 0≤lossScale R S := by unfold lossScale; positivity
  apply (div_le_iff₀ (comparisonScale_pos R S hR hS)).mpr
  calc
    lossScale R S*C ≤ lossScale R S*(3/5) := mul_le_mul_of_nonneg_left hC ha
    _ ≤ comparisonScale R S*(3/5) :=
      mul_le_mul_of_nonneg_right hr (by norm_num : (0 : Real)≤3/5)
    _ = (3/5)*comparisonScale R S := by ring

theorem divisor_cost_ratio (R S : Nat) (u : Real) (hR : 0<R) (hS : 0<S)
    (hRS : 25*S≤R) (hu : 0≤u) :
    ((R*S*(S-1) : Nat) : Real)*u/comparisonScale R S≤u/25 := by
  have hi := Nat.mul_le_mul_left (R*S)
    ((Nat.mul_le_mul_left 25 (Nat.sub_le S 1)).trans hRS)
  have hn : 25*(R*S*(S-1))≤R*R*S := by
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using hi
  have hr : (25 : Real)*((R*S*(S-1) : Nat) : Real)≤comparisonScale R S := by
    simpa only [comparisonScale,pow_two,Nat.cast_mul,Nat.cast_ofNat] using (show ((25*(R*S*(S-1)) : Nat) : Real)≤((R*R*S : Nat) : Real) by exact_mod_cast hn)
  have hm := mul_le_mul_of_nonneg_right hr hu
  apply (div_le_iff₀ (comparisonScale_pos R S hR hS)).mpr
  nlinarith only [hm]

theorem scalar_separation (u : Real) (hu : 693/20≤u) :
    (4/5 : Real)*u-813/1000+3/5+u/25 < (999997/1000000 : Real)*u-5739/1000 := by
  linarith

theorem odd_classNumber_gt_two (D : Nat) (hD : 2^50≤D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    2<NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) := by
  by_contra hn
  have hc : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2 := le_of_not_gt hn
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
  have hbudget := normalized_actual_gram_budget D hsq hc P D rho r s r
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

theorem endpoint_control : (2 : Nat)^50=1125899906842624 := by norm_num

theorem zero_shift_control (a : Real) : q (a+0)=q a := by simp

theorem small_guard_rejected : ¬ (4*(1+2*(0 : Real))≤q 0) := by norm_num [q]

theorem rational_margin_control :
    (159997/1000000 : Real)*(693/20)-4926/1000-3/5=1789605/100000000 := by norm_num
end
end TenthDiscriminant.UniformTwoClass

#check TenthDiscriminant.UniformTwoClass.q_growth
#check TenthDiscriminant.UniformTwoClass.q_decay_quarter
#check TenthDiscriminant.UniformTwoClass.q_decay_half
#check TenthDiscriminant.UniformTwoClass.envelope_antitone
#check TenthDiscriminant.UniformTwoClass.quarter_exp
#check TenthDiscriminant.UniformTwoClass.half_exp
#check TenthDiscriminant.UniformTwoClass.slope_root
#check TenthDiscriminant.UniformTwoClass.slope_exp
#check TenthDiscriminant.UniformTwoClass.chart_cost_majorant
#check TenthDiscriminant.UniformTwoClass.endpoint_log_bounds
#check TenthDiscriminant.UniformTwoClass.endpoint_envelope
#check TenthDiscriminant.UniformTwoClass.uniform_envelope
#check TenthDiscriminant.UniformTwoClass.chart_cost_uniform
#check TenthDiscriminant.UniformTwoClass.loss_cost_ratio
#check TenthDiscriminant.UniformTwoClass.divisor_cost_ratio
#check TenthDiscriminant.UniformTwoClass.scalar_separation
#check TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two
#check TenthDiscriminant.UniformTwoClass.endpoint_control
#check TenthDiscriminant.UniformTwoClass.zero_shift_control
#check TenthDiscriminant.UniformTwoClass.small_guard_rejected
#check TenthDiscriminant.UniformTwoClass.rational_margin_control
#print TenthDiscriminant.UniformTwoClass.q
#print TenthDiscriminant.UniformTwoClass.Hlog
#print TenthDiscriminant.OddMinkowski.chartCost
#print axioms TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two
#audit_namespace TenthDiscriminant.UniformTwoClass
