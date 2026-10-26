import TenthDiscriminant

open TenthDiscriminant TenthDiscriminant.FirstCertificate
#check @small35_add_retained_le_production
#check @recoveredPrimeMassLower_le_production
#check @certified_lt_recoveredPrimeMassLower
#check @recovered_three_two_zero_control
#print axioms small35_add_retained_le_production
#print axioms recoveredPrimeMassLower_le_production
#print axioms certified_lt_recoveredPrimeMassLower
#print axioms recovered_three_two_zero_control

example (I : Real) : certifiedPrimeMassLower 4 2 I < recoveredPrimeMassLower 4 2 I :=
  certified_lt_recoveredPrimeMassLower 4 2 I (by decide) (by decide)

example (I : Real) : recoveredPrimeMassLower 4 2 I =
    certifiedPrimeMassLower 4 2 I + 2*Real.log 3 := recovered_four_two_control I

example (I : Real) : ¬ certifiedPrimeMassLower 3 2 I < recoveredPrimeMassLower 3 2 I := by
  rw [recovered_three_two_zero_control]
  exact lt_irrefl _

example (R S : Nat) (I : Real) (hR : 2 ≤ R) (hS : 1 ≤ S) :
    recoveredPrimeMassLower R S I ≤ enderPrimeMassLower R S 10000 I :=
  recoveredPrimeMassLower_le_production R S I hR hS
