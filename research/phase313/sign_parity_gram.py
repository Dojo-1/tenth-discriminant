#!/usr/bin/env python3
"""Phase313-C: exact sign-parity orthogonal decomposition of ORIGINAL Grams.

For any conjugation- and sign-stable original norm ball and ordinary
Z-jets (W fixed), a row of bidegree (r,s) has sign parity r+s.
Each ordinary jth derivative changes the parity by j. Pairing rows
i,k at the SAME j introduces (-1)^(pi+pk), so opposite-parity
Gram entries cancel under z -> -z, EXACTLY over the integers.

The Phase307 F and K source shears preserve the source-row parity.
This block splitting explains an algebraic invariant but is NOT extra
valuation on top of the existing primitive v5(det)=38.
"""
from collections import Counter
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase304","phase311"):
    sys.path.insert(0,str(ROOT/"research"/p))
import highjet_d203_original as pilot
from secondary_trace_radical import original_primitive_factorization,staged_trace_radical

D=203
R,S,J=50,2,2
N=100
MOD=125


def source_row_parity():
    return tuple((i//S+i%S)%2 for i in range(N))


def sign_parity_gram_certificate():
    pilot.guard()
    q=tuple(pilot.qmax(24))
    assert len(q)==263
    assert all((-z[0],-z[1]) in set(q) for z in q)
    ps=source_row_parity()
    even=[i for i,x in enumerate(ps) if x==0]
    odd=[i for i,x in enumerate(ps) if x==1]
    assert len(even)==len(odd)==50
    # Universal source-row parity: every F_r term has degrees r,r-4;
    # every K_a term has degrees 46+a,26+a,2+a.
    assert all((r-(r-4))%2==0 for r in range(5,R))
    assert all((46+a)%2==(26+a)%2==(2+a)%2 for a in range(5))

    E=pilot.evaluate_original_jets(q,R,S,J,MOD)
    original=pilot.original_trace_gram(E,len(q),J,MOD)
    g,source=original_primitive_factorization() # already mod125
    assert original.shape==g.shape==(N,N)
    zero_cross_original=original[np.ix_(even,odd)]
    zero_cross_primitive=g[np.ix_(even,odd)]
    assert not np.any(zero_cross_original)
    assert not np.any(zero_cross_primitive)
    assert not np.any(original[np.ix_(odd,even)])
    assert not np.any(g[np.ix_(odd,even)])
    assert np.array_equal(original,original.T)
    assert np.array_equal(g,g.T)

    c_even=staged_trace_radical(g[np.ix_(even,even)],5,3)
    c_odd=staged_trace_radical(g[np.ix_(odd,odd)],5,3)
    assert c_even["censored_factors_at_depth"]==0
    assert c_odd["censored_factors_at_depth"]==0
    combined=Counter(c_even["smith_exponent_histogram"])+Counter(
        c_odd["smith_exponent_histogram"])
    assert dict(combined)=={0:63,1:36,2:1}
    v_even=c_even["exact_det_valuation_if_all_resolved"]
    v_odd=c_odd["exact_det_valuation_if_all_resolved"]
    assert v_even+v_odd==38

    # Explicit adverse norm-ball: delete the (+1,0) observation but
    # retain its (-1,0) partner. Constant and Z rows then cease to
    # be orthogonal. This tests the actual sign-closure hypothesis,
    # not an arbitrary offdiagonal matrix.
    assert (1,0) in q and (-1,0) in q
    cut=tuple(z for z in q if z!=(1,0))
    assert (1,0) not in cut and (-1,0) in cut
    ec=pilot.evaluate_original_jets(cut,2,1,1,MOD)
    gc=pilot.original_trace_gram(ec,len(cut),1,MOD)
    assert ec.shape==(2,2*len(cut))
    assert gc.shape==(2,2)
    assert gc[0,1]==(-2)%MOD
    return {
        "D":D,
        "actual_Q":len(q),
        "original_source_rows":N,
        "same_original_ordinary_jet_layers":J,
        "even_row_count":len(even),
        "odd_row_count":len(odd),
        "original_opposite_parity_Gram_zero_cells":2*len(even)*len(odd),
        "primitive_opposite_parity_Gram_zero_cells":2*len(even)*len(odd),
        "precise_modulus_checked":MOD,
        "primitive_even_smith_levels":c_even["smith_exponent_histogram"],
        "primitive_odd_smith_levels":c_odd["smith_exponent_histogram"],
        "even_exact_v5":v_even,
        "odd_exact_v5":v_odd,
        "combined_primitive_exact_v5":v_even+v_odd,
        "same_original_v5_after_50_5_divisions":2*50+v_even+v_odd,
        "asymmetric_observation_Gram_constant_Z_cross":int(gc[0,1]),
        "sign_parity_requires_full_actual_source_support":True,
        "parity_split_does_not_add_new_valuation":True,
    }


def main():
    print("PHASE313_ORIGINAL_PARITY_GRAM_PASS",
          sign_parity_gram_certificate(),flush=True)


if __name__=="__main__":
    main()
