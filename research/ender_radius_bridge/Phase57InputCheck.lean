import TenthDiscriminant

open TenthDiscriminant
#check @clippedFloorSum_succ
#check @clippedFloorSum_closed
#check @valuationWeight_exact_of_last_threshold
#check @exact_weight_zero_p_rejected
#check @exact_weight_missing_threshold_rejected
#check @exact_weight_saturated_control
#print axioms clippedFloorSum_succ
#print axioms clippedFloorSum_closed
#print axioms valuationWeight_exact_of_last_threshold

example (R S p : Nat) (hp : 0<p) (hcut : p*(S-1)≤R) :
    6*(valuationWeight R S p : Real)=
      (S : Real)*((S : Real)-1)*(3*(R : Real)-(p : Real)*((S : Real)+1)) :=
  valuationWeight_exact_of_last_threshold R S p hp hcut

example : valuationWeight 8 2 2=6 := exact_weight_saturated_control
example : (valuationWeight 8 2 2 : Real) ≠
    ((2 : Real)-1/2)*floorSum 8 2-(floorSquareSum 8 2 : Real)/2 :=
  saturated_polynomial_not_identity_control

example (R p : Nat) : valuationWeight R 1 p=0 := by
  simp [valuationWeight]
