import TenthDiscriminant

#print TenthDiscriminant.integerTraceGramEntry_eq_zero_of_central_symmetry
#print TenthDiscriminant.ellipsePairs_central_symmetry
#print TenthDiscriminant.ellipseTraceGramEntry_eq_zero_of_odd_degree
#print TenthDiscriminant.central_symmetry_required_control
#print axioms TenthDiscriminant.integerTraceGramEntry_eq_zero_of_central_symmetry
#print axioms TenthDiscriminant.ellipsePairs_central_symmetry
#print axioms TenthDiscriminant.ellipseTraceGramEntry_eq_zero_of_odd_degree
#print axioms TenthDiscriminant.central_symmetry_required_control

example : TenthDiscriminant.integerTraceGramEntry
    (TenthDiscriminant.ellipsePairs 19 5) 19 7 3 1 2 1 = 0 :=
  TenthDiscriminant.ellipseTraceGramEntry_eq_zero_of_odd_degree
    19 5 7 3 1 2 1 (by decide) (by decide)

example : TenthDiscriminant.integerTraceGramEntry {(1,0)} 1 1 0 0 1 0 ≠ 0 := by
  rw [TenthDiscriminant.central_symmetry_required_control]
  norm_num
