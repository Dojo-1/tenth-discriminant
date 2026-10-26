import TenthDiscriminant.Arithmetic

/-! Count the existing staircase by column heights, with no new valuation. -/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

def clippedFloorSum (R p t : Nat) : Nat :=
  ∑ r ∈ Finset.range R, min (r/p) t

private theorem min_floor_step (p t : Nat) (hp : 0<p) (r : Nat) :
    min (r/p) (t+1) = min (r/p) t + if p*(t+1)≤r then 1 else 0 := by
  by_cases h : p*(t+1)≤r
  · have hd : t+1≤r/p := (Nat.le_div_iff_mul_le hp).mpr
      (by simpa only [Nat.mul_comm] using h)
    simp only [if_pos h]
    omega
  · have hh : r<p*(t+1) := by omega
    have hd : r/p<t+1 := (Nat.div_lt_iff_lt_mul hp).mpr
      (by simpa only [Nat.mul_comm] using hh)
    simp only [if_neg h]
    omega

/-- One more column height counts the rows that reach it. -/
theorem clippedFloorSum_succ (R p t : Nat) (hp : 0<p) :
    clippedFloorSum R p (t+1)=clippedFloorSum R p t+(R-p*(t+1)) := by
  have hf : (Finset.range R).filter (fun r => p*(t+1)≤r)=Finset.Ico (p*(t+1)) R := by
    ext r
    simp only [Finset.mem_filter,Finset.mem_range,Finset.mem_Ico]
    omega
  have hcount : (∑ r ∈ Finset.range R, if p*(t+1)≤r then (1 : Nat) else 0)=R-p*(t+1) := by
    calc
      _ = ∑ _r ∈ (Finset.range R).filter (fun r => p*(t+1)≤r), (1 : Nat) := by
        rw [Finset.sum_filter]
      _ = ((Finset.range R).filter (fun r => p*(t+1)≤r)).card := by simp
      _ = _ := by rw [hf]; simp
  unfold clippedFloorSum
  simp_rw [min_floor_step p t hp]
  rw [Finset.sum_add_distrib,hcount]

theorem clippedFloorSum_closed (R p t : Nat) (hp : 0<p) (hcut : p*t≤R) :
    2*(clippedFloorSum R p t : Real)=
      (t : Real)*(2*(R : Real)-(p : Real)*((t : Real)+1)) := by
  induction t generalizing R with
  | zero => simp [clippedFloorSum]
  | succ t ih =>
    have hprev : p*t≤R := (Nat.mul_le_mul_left p (Nat.le_succ t)).trans hcut
    have hi := ih R hprev
    have hstep := congrArg (fun n : Nat => (n : Real)) (clippedFloorSum_succ R p t hp)
    push_cast [Nat.cast_sub hcut] at hstep ⊢
    nlinarith only [hi,hstep]

private theorem valuationWeight_succ_columns (R S p : Nat) :
    valuationWeight R (S+1) p=valuationWeight R S p+clippedFloorSum R p S := by
  unfold valuationWeight clippedFloorSum
  simp_rw [Finset.sum_range_succ]
  exact Finset.sum_add_distrib

/-- Exact in the complementary regime where the full last threshold fits. -/
theorem valuationWeight_exact_of_last_threshold (R S p : Nat) (hp : 0<p)
    (hcut : p*(S-1)≤R) :
    6*(valuationWeight R S p : Real)=
      (S : Real)*((S : Real)-1)*(3*(R : Real)-(p : Real)*((S : Real)+1)) := by
  induction S generalizing R with
  | zero => simp [valuationWeight]
  | succ S ih =>
    have hlast : p*S≤R := by simpa using hcut
    have hprev : p*(S-1)≤R := (Nat.mul_le_mul_left p (Nat.sub_le S 1)).trans hlast
    have hi := ih R hprev
    have hc := clippedFloorSum_closed R p S hp hlast
    have hstep := congrArg (fun n : Nat => (n : Real)) (valuationWeight_succ_columns R S p)
    push_cast at hstep ⊢
    nlinarith only [hi,hc,hstep]

theorem exact_weight_zero_p_rejected :
    ¬ 6*(valuationWeight 4 2 0 : Real)=
      (2 : Real)*(2-1)*(3*4-(0 : Real)*(2+1)) := by
  norm_num [valuationWeight,Finset.sum_range_succ]

theorem exact_weight_missing_threshold_rejected :
    ¬ 6*(valuationWeight 1 3 2 : Real)=
      (3 : Real)*(3-1)*(3*1-(2 : Real)*(3+1)) := by
  norm_num [valuationWeight,Finset.sum_range_succ]

theorem exact_weight_saturated_control : valuationWeight 8 2 2=6 := by decide

end
end TenthDiscriminant
