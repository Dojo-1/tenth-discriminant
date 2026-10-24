import TenthDiscriminant.FirstIntervalData

namespace TenthDiscriminant.FirstCertificate
set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem coverage_sixteen_high :
    (List.range' 9968 16).filter (fun p => decide p.Prime) = [9973] := by
  have h0 : ¬ Nat.Prime 9968 := by norm_num
  have h1 : ¬ Nat.Prime 9969 := by norm_num
  have h2 : ¬ Nat.Prime 9970 := by norm_num
  have h3 : ¬ Nat.Prime 9971 := by norm_num
  have h4 : ¬ Nat.Prime 9972 := by norm_num
  have h5 : Nat.Prime 9973 := by norm_num
  have h6 : ¬ Nat.Prime 9974 := by norm_num
  have h7 : ¬ Nat.Prime 9975 := by norm_num
  have h8 : ¬ Nat.Prime 9976 := by norm_num
  have h9 : ¬ Nat.Prime 9977 := by norm_num
  have h10 : ¬ Nat.Prime 9978 := by norm_num
  have h11 : ¬ Nat.Prime 9979 := by norm_num
  have h12 : ¬ Nat.Prime 9980 := by norm_num
  have h13 : ¬ Nat.Prime 9981 := by norm_num
  have h14 : ¬ Nat.Prime 9982 := by norm_num
  have h15 : ¬ Nat.Prime 9983 := by norm_num
  have b0 : decide (Nat.Prime 9968) = false := decide_eq_false h0
  have b1 : decide (Nat.Prime 9969) = false := decide_eq_false h1
  have b2 : decide (Nat.Prime 9970) = false := decide_eq_false h2
  have b3 : decide (Nat.Prime 9971) = false := decide_eq_false h3
  have b4 : decide (Nat.Prime 9972) = false := decide_eq_false h4
  have b5 : decide (Nat.Prime 9973) = true := decide_eq_true h5
  have b6 : decide (Nat.Prime 9974) = false := decide_eq_false h6
  have b7 : decide (Nat.Prime 9975) = false := decide_eq_false h7
  have b8 : decide (Nat.Prime 9976) = false := decide_eq_false h8
  have b9 : decide (Nat.Prime 9977) = false := decide_eq_false h9
  have b10 : decide (Nat.Prime 9978) = false := decide_eq_false h10
  have b11 : decide (Nat.Prime 9979) = false := decide_eq_false h11
  have b12 : decide (Nat.Prime 9980) = false := decide_eq_false h12
  have b13 : decide (Nat.Prime 9981) = false := decide_eq_false h13
  have b14 : decide (Nat.Prime 9982) = false := decide_eq_false h14
  have b15 : decide (Nat.Prime 9983) = false := decide_eq_false h15
  simp only [List.range', Nat.reduceAdd, List.filter_cons, List.filter_nil,
    b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,
    Bool.false_eq_true, ite_false, ite_true]

theorem coverage_sixteen_zero :
    (List.range' 0 16).filter (fun p => decide p.Prime) = [2,3,5,7,11,13] := by
  norm_num [List.range', List.filter]

theorem omitted_prime_rejected :
    (List.range' 9968 16).filter (fun p => decide p.Prime) ≠ [] := by
  rw [coverage_sixteen_high]
  simp

end TenthDiscriminant.FirstCertificate
