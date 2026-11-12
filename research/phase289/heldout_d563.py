#!/usr/bin/env python3
"""Phase289-D563: larger original-source held-out extension, prereg 9e54eff.

Not an ex post change to the D283/D403 experiments. The only fixed
predictions are original R/S/J/rho and the deterministic partition. The
third-source normalized gain remains an unobserved result until CI.
"""
from math import isqrt
from four_fiber_fischer import CASES,params,source_guard,partition,case

D=563


def independently_enumerated_q(D,rho):
    """Independent quadratic norm enumeration without sqrt bounds."""
    return [(x,y) for y in range(-rho,rho+1)
                  for x in range(-rho,rho+1)
                  if x*x+D*y*y<=rho*rho]


def main():
    assert D%4==3
    assert all(D%(p*p) for p in range(2,isqrt(D)+1))
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J)==(51,140,5,5)
    assert Q==independently_enumerated_q(D,rho)
    assert len(Q)>2*(R-1)+(S-1)
    assert (-D)%3==1  # Split p3 unlike prior inert controls.
    old,grouped=partition(R,S)
    assert sum(len(v)==2 for v in old)==72
    assert sum(len(v)==4 for v in grouped)==36
    assert sum(len(v)!=4 for v in grouped)==0
    CASES[D]={
        "params":(rho,R,S,J,len(Q)),
        "pairs":72,"four":36,"left_pairs":0,"singles":0,
    }
    source_guard()
    gain=case(D)
    assert gain>=1
    print("PHASE289_HOLDOUT_D563",{
        "D":D,
        "rho":rho,"R":R,"S":S,"J":J,
        "independent_original_Q_count":len(Q),
        "full_original_rows":R*S,
        "old_pairs":72,
        "new_quartets":36,
        "exact_dyadic_extra_gain_K":gain,
        "normalized_certified_lower":str(gain)+"/"+str(R*R*S)+" * ln2",
        "p3_split_negative_inertness_control":True,
        "uniform_D_analytic_bound_still_unproved":True,
    },flush=True)
    print("PASS Phase289-D563 held-out same-source four-fiber test",flush=True)


if __name__=="__main__":
    main()
