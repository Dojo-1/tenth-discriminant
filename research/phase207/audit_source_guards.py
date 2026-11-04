#!/usr/bin/env python3
"""Phase207-C (#148): exact source-type and valuation-direction controls.

Reuses classical minor/index logic and a small analytic counterworld;
no number-field theorem is asserted.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "phase206"))

from source_probe import params, det, rank_mod, fall
from middle_frobenius import old_k

def run():
    D=403
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(40,100,4,4,219)
    assert D==13*31 and D%4==3
    for p in (3,5):
        assert (-D)%p not in {a*a%p for a in range(p)}
        assert 2%p and (2*D)%p  # Original 2,2D trace form nondegenerate.
        k=[[old_k(r,s,p) for s in range(S)] for r in range(R)]
        F=sum(sum(row) for row in k)
        for L in range(S):
            actual=sum(x<=L for row in k for x in row)
            ceiling=(L+1)*(p*S+R)
            assert actual<=ceiling
        # The columns-per-depth capacity controls only a FORMAL tropical
        # factorial-matching bound, not a real minor's p-unit status.
        for r in range(R):
            for s in range(S):
                j=old_k(r,s,p)
                assert j<J
                v=1
                for t in range(1,j+1):v*=t
                vp=0
                while v and v%p==0:v//=p;vp+=1
                assert vp<=j
        print("SOURCE_TYPE",{"D":D,"p":p,"rows":R*S,"old_F":F,
               "original_metric_nondegenerate_mod_p":True,
               "row_depth_count_bound":True,
               "factorial_only_does_not_certify_extra_index":True},flush=True)
    # Small exact model of an extra evaluation index and its *two*
    # determinant factors.  Rank deficiency is a lower guarantee, not a
    # substitute for the fully primitive source Smith valuation.
    for p in (3,5):
        E=[[1,0],[1,p]]
        B=[1,1]
        G=[[sum(E[i][j]*B[j]*E[t][j] for j in range(2))
             for t in range(2)] for i in range(2)]
        assert rank_mod(E,p)==1
        assert det(G)==p*p
    # Ordinary j=p derivative != Hasse coefficient, even when source
    # p3 j3 is inside the retained depth S=J=4.
    assert fall(3,3)==6 and fall(3,3)%3==0
    assert fall(3,3)!=1
    print("NEGATIVE_HASSE",{"p":3,"ordinary_derivative_of_Z3_order3":6,
                            "Hasse_coefficient":1},flush=True)
    print("PASS Phase207 type controls, no double counting",flush=True)

if __name__=="__main__":run()
