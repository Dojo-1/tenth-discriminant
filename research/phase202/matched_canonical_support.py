#!/usr/bin/env python3
"""Phase202 matched-support control; requires sibling placewise_jet_probe.py.

The 59-point radius-16 support is NOT the canonical Phase200 rho(D).
For D=215 the canonical rho(D)=ceil((11/25)*D^(3/4))=25, with 133 points.
Both use the same integer pair lattice, rows, ordinary jets and trace metric.
"""
from placewise_jet_probe import channels, jets, rank_p, rank_p2, trace_gram

D, R, S, J, p = 215, 53, 2, 2, 53
for radius, expected_n, old_guard in [(16, 59, False), (25, 133, True)]:
    Q, rows, cols, A = jets(D, R, S, J, radius, p)
    assert len(Q) == expected_n
    assert (len(Q) > 2*(R-1)+(S-1)) == old_guard
    assert 2*radius < p
    assert len(set((x%p,y%p) for x,y in Q)) == len(Q)
    rank_a = rank_p2(A, D, p)
    rank_e = rank_p(channels(A), p)
    rank_g = rank_p(trace_gram(A, D, p), p)
    assert (rank_a, rank_e, rank_g) == (R*S,R*S,R*S)
    print("MATCHED_SUPPORT",{"D":D,"rho":radius,"canonical":radius==25,
        "points":len(Q),"old_count_guard":old_guard,
        "rank_A_Fp2":rank_a,"rank_E_Fp":rank_e,"rank_G_Fp":rank_g})
print("PASS: both supports; no substitution of Gram determinants")
