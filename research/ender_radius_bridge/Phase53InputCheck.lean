import TenthDiscriminant

open TenthDiscriminant TenthDiscriminant.FirstCertificate
#check @saturated_rows_lower_weight
#check @recovered_scale_gain
#check @recovered_normalized_gap
#check @raw_normalized_add_gain_le_recovered
#check @saturated_rows_zero_p_rejected
#check @normalized_gain_missing_S_guard_false
#print axioms saturated_rows_lower_weight
#print axioms recovered_scale_gain
#print axioms recovered_normalized_gap
#print axioms raw_normalized_add_gain_le_recovered

example (R S : Nat) (I : Real) (hS : 100 ≤ S) (h25 : 25*S ≤ R) (h26 : R ≤ 26*S) :
    rawPrimeMassLower R S I/comparisonScale R S+(3/50 : Real) ≤
      recoveredPrimeMassLower R S I/comparisonScale R S :=
  raw_normalized_add_gain_le_recovered R S I hS h25 h26

example (I : Real) : ¬ (3/50 : Real) ≤
    (recoveredPrimeMassLower 25 1 I-certifiedPrimeMassLower 25 1 I)/comparisonScale 25 1 :=
  normalized_gain_missing_S_guard_false I

example : ¬ (4-0*2)*2*(2-1) ≤ 2*valuationWeight 4 2 0 :=
  saturated_rows_zero_p_rejected
