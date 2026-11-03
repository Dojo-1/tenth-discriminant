#!/usr/bin/env python3
"""Phase181 small-D thin-ellipse stress controls; NOT the large-D theorem.

Reproduces Lean ellipsePairs / thinRadius / R / S formulas exactly
with integer arithmetic, then checks original vs normalized 2-adic Smith
barcodes. All D are far below the proven field cutoff and may lack its
field/class-number premises. No uniform or asymptotic conclusion.
"""
from __future__ import annotations

from math import isqrt
from phase159_observation_continuum import ordinary_effective
from phase159_padic_gram import gram_mod_2_power, smith_exponents_2
from phase180_binary_hull import binary_rank
from phase181_normalized_binary_filtration import lambda1,source_normalize,smith_profile


def thin_radius(D):
    assert D > 0
    rho = 0
    while (25*rho)**4 < 11**4 * D**3:
        rho += 1
    assert rho and (25*(rho-1))**4 < 11**4 * D**3
    return rho


def ellipse_pairs(D,rho):
    assert D > 0 and rho >= 0
    ymax = isqrt((rho*rho)//D)
    Q = []
    for y in range(-ymax,ymax+1):
        xmax = isqrt(rho*rho-D*y*y)
        for x in range(-xmax,xmax+1):
            Q.append((x,y))
    assert len(set(Q)) == len(Q)
    assert all(x*x+D*y*y <= rho*rho for x,y in Q)
    return Q


def inspect(Q,D,R,S,expected):
    E,w,_ = ordinary_effective(Q,D,R,S)
    N,_ = source_normalize(E,R,S)
    C = [v//2 for v in w]
    assert all(v in (1,D) for v in C)
    H = gram_mod_2_power(N,C,128)
    G = gram_mod_2_power(E,w,128)
    residual,barcode,hexp = smith_profile(H,128)
    original,_,gexp = smith_profile(G,128)
    assert original == lambda1(R,S)+residual
    rn,rh = binary_rank(N),binary_rank(H)
    n1 = R*S-rh
    assert n1 == barcode[0]
    got = (len(Q),len(w),R*S,lambda1(R,S),rn,rh,n1,residual,original)
    assert got == expected,(D,got,expected)
    print("PHASE181_THIN",dict(
        D=D,R=R,S=S,nodes=len(Q),n1=n1,
        residual=residual,original=original,scale=R*R*S,
        top_H=max(hexp),top_G=max(gexp)),flush=True)
    return barcode


def main():
    # Tiny exact Lean LatticeEllipse cardinality controls.
    assert len(ellipse_pairs(1,1)) == 5
    assert len(ellipse_pairs(19,5)) == 21
    samples = [
        (103,15,(77,123,25,157,4,1,24,362,519)),
        (127,17,(85,135,31,241,4,1,30,575,816)),
        (163,21,(109,175,40,400,4,1,39,641,1041)),
        (199,24,(127,205,49,601,4,1,48,1546,2147)),
        (251,28,(151,490,124,1924,8,2,122,3098,5022)),
    ]
    for D,rho,expected in samples:
        assert D%4 == 3 and thin_radius(D) == rho
        R,S = D//4,(D//4)//25
        Q = ellipse_pairs(D,rho)
        inspect(Q,D,R,S,expected)
        if D == 199:
            E,w,_ = ordinary_effective(Q,D,R,S)
            N,_ = source_normalize(E,R,S)
            H64 = gram_mod_2_power(N,[v//2 for v in w],64)
            _,censored = smith_exponents_2(H64,64)
            assert censored > 0, "negative control: 64-bit precision must fail"
            print("PHASE181_PRECISION_NEGATIVE_CONTROL_PASS",censored,flush=True)
        if D == 163:
            # One-node perturbations of the same full thin-formula support.
            for removed,n1,res in [((0,0),40,642),
                                   ((21,0),38,642),
                                   ((16,1),37,639)]:
                assert removed in Q
                eq = [q for q in Q if q != removed]
                E,w,_ = ordinary_effective(eq,D,R,S)
                N,_ = source_normalize(E,R,S)
                H = gram_mod_2_power(N,[v//2 for v in w],128)
                h,b,_ = smith_profile(H,128)
                assert (len(eq),R*S-binary_rank(H),h) == (108,n1,res)
                print("PHASE181_THIN_DELETION",removed,n1,res,flush=True)
    print("PHASE181_THIN_SUPPORT_PILOT_PASS: small D, finite only",flush=True)


if __name__ == "__main__":
    main()
