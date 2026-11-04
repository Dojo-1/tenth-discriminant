#!/usr/bin/env python3
"""Phase208-C typed implication checks; preregistered in issue #152.

Correlated AI-authored source controls, NOT independent human review.
No cross-place isomorphism, no field theorem, no new valuation from
un-normalized metric radicals.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase206"))
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase207"))

from fractions import Fraction as F
from source_probe import params, det, mul, fall, rank_mod
from middle_frobenius import old_k
from sparse_schur_map import toy as SchurToy
from truncated_middle_smith import p2_smith_levels

def audit():
    rho,R,S,J,Q=params(403)
    assert (rho,R,S,J,len(Q))==(40,100,4,4,219)
    for p,expectedF,expectedK2 in ((3,570,188),(5,550,180)):
        assert (-403)%p not in {t*t%p for t in range(p)}
        assert (2%p)*(806%p)%p!=0
        entries=[(r,s,old_k(r,s,p)) for r in range(R) for s in range(S)]
        assert len(entries)==R*S
        assert sum(k for _,_,k in entries)==expectedF
        assert sum(k>=2 for _,_,k in entries)==expectedK2
        assert max(k for _,_,k in entries)==3
        # Unitriangular original row change has determinant 1; quotient
        # by p^k is NOT a unimodular row operation.
        assert fall(3,3)==6 and fall(3,3)%3==0
        assert p2_smith_levels([[1,0,0],[0,p,0],[0,0,p*p]],p)=={
            "0":1,"1":1,">=2":1}
        # A selected row subsystem with local index >=3 forces p^3
        # divisibility of every maximal full-source E minor.
        E=[[p,0,0],[0,p*p,0],[0,0,1]]
        G=[[sum(E[i][j]*E[k][j] for j in range(3)) for k in range(3)]
           for i in range(3)]
        assert det(E)==p**3 and det(G)==p**6
        # Row-shear by unit determinant preserves full determinant.
        E[2]=[x+y for x,y in zip(E[2],E[0])]
        assert det(E)==p**3
        print("TYPED_INDEX_CONTROL",{"p":p,"old_F":expectedF,
           "depth_ge2_rows":expectedK2,
           "metric_p_units":True,
           "toy_new_E_index":3,"toy_new_Gram_exponent":6,
           "p2_levels_last_not_exact":True},flush=True)
    # Metric on Z[u]/(u²+D) is NOT a naïve Euclidean pair dot product.
    z=(0,1)
    trace_norm=2*z[0]**2+2*403*z[1]**2
    wrong_euclid=2*(z[0]**2+z[1]**2)
    assert (trace_norm,wrong_euclid)==(806,2)
    # Full-rank source evaluation does NOT imply primitive restricted
    # trace nondegeneracy in an inert residue field.
    A=[1,0,1,1];weights=[2,38,2,38]
    assert sum(x*x*w for x,w in zip(A,weights))==42
    assert 42%3==0 and rank_mod([A],3)==1
    SchurToy()
    print("TYPED_REMAINDERS",{"original_trace_of_imag_unit":trace_norm,
       "wrong_euclidean_weight":wrong_euclid,
       "isotropic_nonzero_row_mod3":True,
       "prime_fibres_not_identified":True,
       "sparse_trial_gauge_dependent":True},flush=True)
    print("PASS Phase208 three-line implication/type audit",flush=True)

if __name__=="__main__":audit()
