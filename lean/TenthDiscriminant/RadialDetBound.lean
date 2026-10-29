import TenthDiscriminant.RadialJetMajorant
import TenthDiscriminant.TunedAnalyticCutoff

/-! Phase119: the actual integral determinant at the unchanged production radius.
The preceding Phase118 namespace is an exact local dependency, not a new model. -/
namespace TenthDiscriminant.RadialDetBound
open Polynomial FirstCertificate
open scoped BigOperators ComplexConjugate Classical
set_option autoImplicit false
noncomputable section

/-- Additive coordinate chart only; no complex-to-residue-field map is used. -/
def chart (D : Nat) : Zsqrtd (-(D : Int)) →+ Complex where
  toFun v := pairEval D (v.re,v.im)
  map_zero' := by simp [pairEval,latticePoint]
  map_add' v w := by
    apply Complex.ext <;> simp [pairEval,latticePoint,add_mul]

theorem chart_pair (D : Nat) (q : Int × Int) :
    chart D (pairZsqrtdEquiv D q)=pairEval D q := by rfl

theorem actual_jet_value (D R S : Nat) (a : Int) (i : Fin (R*S))
    (q : Int × Int) (j : Nat) :
    chart D (RadialOperator.integerJet D R S a i q j)=
      RadialJetMajorant.jet a (i.val/S) (i.val%S) j (pairEval D q) := by
  calc
    _ = chart D (zsqrtdJetTransform (RadialOperator.matrix R S a)
        (rectangularCanonicalJet D R S) i q j) :=
      congrArg (chart D) (RadialOperator.integer_jet_action D R S a i q j).symm
    _ = ∑ h : Fin (R*S), RadialOperator.matrix R S a i h •
        derivativeRow (h.val/S) (h.val%S) j (pairEval D q) := by
      rw [zsqrtdJetTransform,map_sum]
      apply Finset.sum_congr rfl
      intro h hh
      rw [map_zsmul]
      congr 1
      change pairEval D (integerDerivativeRow D (h.val/S) (h.val%S) j q)=_
      exact integerDerivativeRow_eval D (h.val/S) (h.val%S) j q
    _ = _ := RadialOperator.complex_jet_action R S a i (pairEval D q) j

theorem trace_square (D : Nat) (v : Zsqrtd (-(D : Int))) :
    (zsqrtdTrace D v v : Real)=2*‖chart D v‖^2 := by
  have h := integerPairTrace_cast D (v.re,v.im) (v.re,v.im)
  change (zsqrtdTrace D v v : Real)=2*‖pairEval D (v.re,v.im)‖^2
  simpa only [integerPairTrace,zsqrtdTrace,Complex.mul_conj',← Complex.ofReal_pow,
    Complex.ofReal_re] using h

/-- The original factor2 and original sample/derivative indexing, entrywise. -/
theorem actual_diagonal (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int)
    (i : Fin (R*S)) :
    ((RadialOperator.gram Q D J R S a).map (Int.castRingHom Real)) i i =
      2*∑ j ∈ Finset.range J, ∑ q ∈ Q,
        ‖RadialJetMajorant.jet a (i.val/S) (i.val%S) j (pairEval D q)‖^2 := by
  change ((∑ j ∈ Finset.range J, ∑ q ∈ Q,
    zsqrtdTrace D (RadialOperator.integerJet D R S a i q j)
      (RadialOperator.integerJet D R S a i q j) : Int) : Real)=_
  push_cast
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro q hq
  rw [trace_square,actual_jet_value]

def rowFactor (S r s : Nat) : Real :=
  if 9*S ≤ r then (13/20 : Real)^(2*s) else 1

def rowPenalty (S r s : Nat) : Real :=
  if 9*S ≤ r then (2*s : Nat)*Real.log (20/13 : Real) else 0

def rowLog (S rho : Nat) (n : Real) (r s : Nat) : Real :=
  Real.log (2*n*S)+(2*(r+s) : Nat)*Real.log (rho : Real)+
    (2*(S-1) : Nat)*max 0 (Real.log ((r : Real)/rho))

theorem rowFactor_pos (S r s : Nat) : 0 < rowFactor S r s := by
  unfold rowFactor
  split_ifs <;> positivity

theorem rowFactor_log (S r s : Nat) :
    Real.log (rowFactor S r s) = -rowPenalty S r s := by
  unfold rowFactor rowPenalty
  split_ifs with h
  · rw [Real.log_pow]
    have he : (13/20 : Real)=(20/13 : Real)⁻¹ := by norm_num
    rw [he,Real.log_inv]
    ring
  · simp

/-- Actual squared jets, with both the old radius and derivative correction. -/
theorem actual_jet_square (rho S r s j : Nat) (hrho : 5 ≤ rho) (hS : 1 ≤ S)
    (hs : s < S) (hj : j < S) (z : Complex) (hz : ‖z‖ ≤ rho) :
    ‖RadialJetMajorant.jet (rho^2/2 : Nat) r s j z‖^2 ≤
      rowFactor S r s * ((rho : Real)^(2*(r+s))*
        (max 1 ((r : Real)/rho))^(2*(S-1))) := by
  have hf := (rowFactor_pos S r s).le
  by_cases hjr : j ≤ r
  · have hsq : ‖RadialJetMajorant.jet (rho^2/2 : Nat) r s j z‖^2 ≤
        rowFactor S r s*((r.descFactorial j : Real)^2*(rho : Real)^(2*(r+s-j))) := by
      by_cases he : 9*S ≤ r
      · have h := RadialJetMajorant.ordinary_jet_gain rho hrho S r s j hS hs hj he z hz
        have hp := pow_le_pow_left₀ (norm_nonneg _) h 2
        rw [rowFactor,if_pos he]
        convert hp using 1
        simp only [mul_pow,← pow_mul,Nat.mul_comm s 2,Nat.mul_comm (r+s-j) 2]
        ring
      · have h := RadialJetMajorant.ordinary_jet_no_loss rho hrho r s j hjr z hz
        have hp := pow_le_pow_left₀ (norm_nonneg _) h 2
        rw [rowFactor,if_neg he,one_mul]
        convert hp using 1
        simp only [mul_pow,← pow_mul,Nat.mul_comm (r+s-j) 2]
    exact hsq.trans (mul_le_mul_of_nonneg_left
      (radial_derivative_term_le rho r s S j (by omega) hjr hj) hf)
  · rw [RadialJetMajorant.high_jet_zero _ r s j (by omega) z]
    simp only [norm_zero,zero_pow (by decide : 2 ≠ 0)]
    positivity

theorem actual_diagonal_uniform (Q : Finset (Int × Int)) (D R S rho : Nat)
    (hrho : 5 ≤ rho) (hS : 1 ≤ S)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) (i : Fin (R*S)) :
    ((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map (Int.castRingHom Real)) i i ≤
      rowFactor S (i.val/S) (i.val%S)*
        (2*(Q.card : Real)*S*(rho : Real)^(2*(i.val/S+i.val%S))*
          (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1))) := by
  let B := rowFactor S (i.val/S) (i.val%S)*
    ((rho : Real)^(2*(i.val/S+i.val%S))*
      (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1)))
  rw [actual_diagonal]
  calc
    _ ≤ 2*∑ j ∈ Finset.range S, ∑ q ∈ Q, B := by
      apply mul_le_mul_of_nonneg_left _ (by norm_num)
      apply Finset.sum_le_sum
      intro j hj
      apply Finset.sum_le_sum
      intro q hq
      exact actual_jet_square rho S (i.val/S) (i.val%S) j hrho hS
        (Nat.mod_lt _ (by omega)) (Finset.mem_range.mp hj) (pairEval D q) (hbound q hq)
    _ = _ := by
      simp only [Finset.sum_const,Finset.card_range,nsmul_eq_mul]
      dsimp only [B]
      ring

theorem actual_log_diagonal (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hrho : 5 ≤ rho) (hS : 1 ≤ S) (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) (i : Fin (R*S))
    (hpos : 0 < ((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map
      (Int.castRingHom Real)) i i) :
    Real.log (((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map
      (Int.castRingHom Real)) i i) ≤
      rowLog S rho n (i.val/S) (i.val%S)-rowPenalty S (i.val/S) (i.val%S) := by
  have hf := rowFactor_pos S (i.val/S) (i.val%S)
  have hn' : rowFactor S (i.val/S) (i.val%S)*
      (2*(Q.card : Real)*S*(rho : Real)^(2*(i.val/S+i.val%S))*
        (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1))) ≤
      rowFactor S (i.val/S) (i.val%S)*
      (2*n*S*(rho : Real)^(2*(i.val/S+i.val%S))*
        (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1))) := by gcongr
  have hl := Real.log_le_log hpos ((actual_diagonal_uniform Q D R S rho hrho hS hbound i).trans hn')
  rw [Real.log_mul hf.ne' (by positivity),rowFactor_log,
    Real.log_mul (by positivity) (by positivity),Real.log_mul (by positivity) (by positivity),
    Real.log_pow,Real.log_pow,log_max_one_ratio rho (i.val/S) (by omega)] at hl
  unfold rowLog
  linarith

private theorem tail_sum (K R : Nat) (c : Real) :
    (∑ r ∈ Finset.range R, if K ≤ r then c else 0)=(R-K : Nat)*c := by
  induction R with
  | zero => simp
  | succ R ih =>
    rw [Finset.sum_range_succ,ih]
    by_cases h : K ≤ R
    · rw [if_pos h]
      have he : R+1-K=R-K+1 := by omega
      rw [he]
      push_cast
      ring
    · have h0 : R-K=0 := by omega
      have h1 : R+1-K=0 := by omega
      simp [h,h0,h1]

/-- Natural subtraction gives zero when the eligible rectangle is empty. -/
theorem penalty_sum (R S : Nat) (hS : 1 ≤ S) :
    (∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S, rowPenalty S r s)=
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
  have inner (r : Nat) : (∑ s ∈ Finset.range S,rowPenalty S r s)=
      if 9*S ≤ r then (S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) else 0 := by
    by_cases h : 9*S ≤ r
    · simp only [rowPenalty,if_pos h,Nat.cast_mul,Nat.cast_ofNat]
      rw [← Finset.sum_mul,← Finset.mul_sum,sum_cast_range,Nat.cast_sub hS,Nat.cast_one]
      ring
    · simp [rowPenalty,h]
  simp_rw [inner]
  rw [tail_sum]
  ring

theorem baseline_sum (R S rho : Nat) (n : Real) (hrho : 0 < rho) (hRrho : rho < R) :
    (∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S,rowLog S rho n r s) ≤
      enderUpperB R S S rho n := by
  unfold rowLog
  rw [rectangular_log_row_sum]
  have hcorr := log_derivative_correction_le_upperB rho R hrho hRrho
  have hscaled := mul_le_mul_of_nonneg_left hcorr
    (by positivity : (0 : Real) ≤ 2*S*((S-1 : Nat) : Real))
  unfold enderUpperB
  exact add_le_add_left hscaled _

/-- The logarithm is of the SAME original integer determinant. -/
theorem integer_log_upper (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S) (hrho : 5 ≤ rho) (hRrho : rho < R)
    (hcard : 2*(R-1)+(S-1) < Q.card) (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) :
    Real.log ((integerRectangularTraceGram Q D S R S).det : Real) ≤
      enderUpperB R S S rho n-
        (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
  let H := (RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map (Int.castRingHom Real)
  have hp : H.PosDef := RadialOperator.real_posDef Q D S R S _ hD hR hS le_rfl hcard
  have hd (i : Fin (R*S)) : 0 < H i i := real_posDef_diagonal_pos _ H hp i
  have hh := real_psd_det_le_diag (R*S) H hp.posSemidef
  have hl := Real.log_le_log hp.det_pos hh
  rw [Real.log_prod Finset.univ _ (fun i hi => (hd i).ne')] at hl
  have hrows : (∑ i : Fin (R*S),Real.log (H i i)) ≤
      ∑ i : Fin (R*S), (rowLog S rho n (i.val/S) (i.val%S)-
        rowPenalty S (i.val/S) (i.val%S)) := by
    apply Finset.sum_le_sum
    intro i hi
    exact actual_log_diagonal Q D R S rho n hrho hS hnpos hn hbound i (hd i)
  rw [Finset.sum_sub_distrib,rectangular_row_sum R S (rowLog S rho n),
    rectangular_row_sum R S (rowPenalty S),penalty_sum R S hS] at hrows
  have hb := baseline_sum R S rho n (by omega) hRrho
  have he : H.det=((integerRectangularTraceGram Q D S R S).det : Real) := by
    dsimp only [H]
    simpa only [RadialOperator.gram_det] using
      ((Int.castRingHom Real).map_det (RadialOperator.gram Q D S R S (rho^2/2 : Nat))).symm
  rw [he] at hl
  linarith

theorem normalized_integer_upper (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hD : 0 < D) (hS : 100 ≤ S) (h25 : 25*S ≤ R) (h26 : R ≤ 26*S)
    (hrho : 5 ≤ rho) (hRrho : rho < R) (hcard : 2*(R-1)+(S-1) < Q.card)
    (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) :
    Real.log ((integerRectangularTraceGram Q D S R S).det : Real)/comparisonScale R S ≤
      enderUpperB R S S rho n/comparisonScale R S-1/100 := by
  have hu := integer_log_upper Q D R S rho n hD (by omega) (by omega) hrho
    hRrho hcard hnpos hn hbound
  have ht := comparisonScale_pos R S (by omega) (by omega)
  have hg : comparisonScale R S/100 ≤
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
    simpa only [comparisonScale,Nat.cast_mul,Nat.cast_pow] using RadialJetMajorant.scale_gain R S hS h25 h26
  have hgn : (1/100 : Real) ≤
      ((R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real))/comparisonScale R S := by
    apply (le_div_iff₀ ht).2
    simpa only [div_eq_mul_inv,mul_comm,one_mul] using hg
  calc
    _ ≤ (enderUpperB R S S rho n-
        (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real))/comparisonScale R S :=
      div_le_div_of_nonneg_right hu ht.le
    _ = _ := sub_div _ _ _
    _ ≤ _ := sub_le_sub_left hgn _

theorem production_guards (D : Nat) (hD : 41006250000 ≤ D) :
    100 ≤ Tuned.S D ∧ 25*Tuned.S D ≤ Tuned.R D ∧ Tuned.R D ≤ 26*Tuned.S D ∧
      5 ≤ Tuned.rho D := by
  have hd := Tuned.dimensions D hD
  have h25 : 25*Tuned.S D ≤ Tuned.R D := by unfold Tuned.S; omega
  have h26 : Tuned.R D ≤ 26*Tuned.S D := by unfold Tuned.S; omega
  refine ⟨by omega,h25,h26,?_⟩
  have hlo := (Tuned.radius_bounds D hD).1
  have hroot := Tuned.root_large D hD
  have hcube := pow_le_pow_left₀ (by norm_num : (0 : Real) ≤ 450) hroot 3
  have h5 : (5 : Real) ≤ Tuned.rho D := by nlinarith only [hlo,hcube]
  exact_mod_cast h5

/-- Actual determinant, actual chosen radius, all geometric-domain D; no class premise. -/
theorem production_normalized_upper (D : Nat) (hD : 41006250000 ≤ D) :
    Real.log ((integerRectangularTraceGram (ellipsePairs D (Tuned.rho D)) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real)/
      comparisonScale (Tuned.R D) (Tuned.S D) ≤ (4/5 : Real)*Real.log D-823/1000 := by
  obtain ⟨hS,h25,h26,h5⟩ := production_guards D hD
  have hd := Tuned.dimensions D hD
  have hD0 : 0 < D := by omega
  have hc := ellipsePairs_card_gt_of_ender_radius D (Tuned.rho D)
    (3*Tuned.R D+Tuned.S D) hD0 (by omega) (Tuned.chosen_radius D hD)
  have hcard : 2*(Tuned.R D-1)+(Tuned.S D-1) < (ellipsePairs D (Tuned.rho D)).card := by omega
  have hn := ellipsePairs_card_le_padded_upper_count D D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D)) hD0 le_rfl le_rfl
  have hnpos : 0 < ellipsePaddedUpperCount D (Tuned.rho D)
      (ellipseVerticalBound D (Tuned.rho D)) :=
    lt_of_lt_of_le (by exact_mod_cast (show 0 < (ellipsePairs D (Tuned.rho D)).card by omega)) hn
  have hbound (q : Int × Int) (hq : q ∈ ellipsePairs D (Tuned.rho D)) :
      ‖pairEval D q‖ ≤ Tuned.rho D := by
    apply ellipsePoint_norm_le D (Tuned.rho D) hD0
    exact Finset.mem_image.mpr ⟨q,hq,rfl⟩
  have hu := normalized_integer_upper (ellipsePairs D (Tuned.rho D)) D (Tuned.R D)
    (Tuned.S D) (Tuned.rho D) (ellipsePaddedUpperCount D (Tuned.rho D)
      (ellipseVerticalBound D (Tuned.rho D))) hD0 hS h25 h26 h5
      (Tuned.radius_lt_R D hD) hcard hnpos hn hbound
  linarith [Tuned.normalized_upper D hD]

theorem constant_trace_control : integerPairTrace 3 (1,0) (1,0)=2 := by
  norm_num [integerPairTrace]

theorem empty_rows_control (Q : Finset (Int × Int)) (D S rho : Nat) :
    (integerRectangularTraceGram Q D S 0 S).det=1 := by
  haveI : IsEmpty (Fin (0*S)) := by
    simpa only [Nat.zero_mul] using (inferInstance : IsEmpty (Fin 0))
  exact Matrix.det_isEmpty

theorem singleton_control :
    (integerRectangularTraceGram {(0,0)} 3 1 1 1).det=2 := by
  rw [Matrix.det_fin_one]
  norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,
    integerPairTrace,integerDerivativeRow,pairScale,pairMul,pairPow,Finset.sum_range_succ,
    Nat.descFactorial,Matrix.det_fin_one]

theorem singular_control :
    (integerRectangularTraceGram ∅ 3 1 1 1).det=0 := by
  rw [Matrix.det_fin_one]
  norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,Matrix.det_fin_one]

theorem origin_control :
    ‖RadialJetMajorant.jet 12 1 1 0 0‖^2=(144 : Real) ∧ derivativeRow 1 1 0 0=0 := by
  norm_num [RadialJetMajorant.jet,RadialOperator.polynomial,derivativeRow]

theorem single_column_control (R : Nat) :
    (∑ r ∈ Finset.range R,∑ s ∈ Finset.range 1,rowPenalty 1 r s)=0 := by
  rw [penalty_sum R 1 (by decide)]
  norm_num

theorem empty_eligible_control (R S : Nat) (hS : 1 ≤ S) (hR : R ≤ 9*S) :
    (∑ r ∈ Finset.range R,∑ s ∈ Finset.range S,rowPenalty S r s)=0 := by
  rw [penalty_sum R S hS,Nat.sub_eq_zero_of_le hR]
  simp

end
end TenthDiscriminant.RadialDetBound
