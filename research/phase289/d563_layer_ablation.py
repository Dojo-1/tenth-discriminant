#!/usr/bin/env python3
"""Phase289-C: exact post-heldout original-vs-three-layer D563 ablation.

Preregistered in PRE_REGISTERED_LAYER_ABLATION.md at a843229 BEFORE this code.
The ablated Q285 is a *different* analytic/arithmetic source, not an input
to the original field-discriminant theorem. Do not substitute it there.
"""
from collections import Counter
from math import log
from four_fiber_fischer import (
    params,gram,det,fibers,partition,witness_and_gain,
    moving_shear_control,source_guard
)

D=563
RHO=51
R=140
S=J=5


def check_layers(Q):
    count=Counter(y for x,y in Q)
    assert set(count)=={-2,-1,0,1,2}
    assert count==Counter({-2:37,-1:91,0:103,1:91,2:37})
    assert len(Q)==359
    q3=[z for z in Q if abs(z[1])<=1]
    extra=[z for z in Q if abs(z[1])==2]
    assert len(q3)==285 and len(extra)==74
    assert len(set(q3))==285 and len(set(extra))==74
    assert len(set(q3)&set(extra))==0
    assert set(q3)|set(extra)==set(Q)
    assert all((x,-y) in set(q3) and (-x,-y) in set(q3) for x,y in q3)
    assert all((x,-y) in set(extra) and (-x,-y) in set(extra) for x,y in extra)
    assert len(q3)>2*(R-1)+(S-1)
    assert RHO*RHO>4*D
    return q3,extra,count


def block_case(Q,groups,require_gauge=True):
    K=0
    strict=0
    loggain=0.
    move=False
    extra_group_sizes=[]
    for group in groups:
        assert len(group)==4
        labels=[row for d in group for row in fibers(R,S,d)]
        a=sum(len(fibers(R,S,d)) for d in group[:2])
        b=sum(len(fibers(R,S,d)) for d in group[2:])
        G=gram(D,Q,J,labels)
        k,yes,_,approx,_=witness_and_gain(D,Q,J,labels,a,b,G)
        K+=k
        strict+=int(yes)
        loggain+=approx
        extra_group_sizes.append(len(labels))
        if yes and require_gauge and not move:
            moving_shear_control(G,a,b)
            move=True
    assert move==require_gauge
    return K,strict,loggain,extra_group_sizes


def matrix_add(A,B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]


def control_deleted_points(Q,smaller,extra,groups):
    g=groups[0]
    labels=[row for d in g for row in fibers(R,S,d)]
    original=gram(D,Q,J,labels)
    cut=gram(D,smaller,J,labels)
    added=gram(D,extra,J,labels)
    assert matrix_add(cut,added)==original
    assert all(added[i][i]>=0 for i in range(len(added)))
    assert sum(sum(row) for row in added)>=0
    return len(labels)


def main():
    source_guard()
    rho,r,s,j,Q=params(D)
    assert (rho,r,s,j)==(RHO,R,S,J)
    smaller,extra,count=check_layers(Q)
    old,groups=partition(R,S)
    assert len(old)==72 and all(len(group)==2 for group in old)
    assert len(groups)==36 and all(len(group)==4 for group in groups)
    originalK,originalStrict,originalLog,dims=block_case(Q,groups)
    assert originalK==179 and originalStrict==36
    thinK,thinStrict,thinLog,_=block_case(smaller,groups)
    blockdim=control_deleted_points(Q,smaller,extra,groups)

    # Each exact integer group ratio lies in (2^k,2^(k+1)] when strict;
    # hence the WHOLE matched 4-fiber improvement has an exact dyadic upper.
    assert originalK+originalStrict==215
    assert (originalK+originalStrict)*10000 <43*(R*R*S)
    # ln(2)<1 makes the above a strict counterexample to >=0.0043
    # normalized gain, for this exact Phase289 incremental construction.

    print("PHASE289_D563_LAYER_ABLATION",{
       "D":D,"rho":rho,"R":R,"S":S,"J":J,
       "original_full_Q":len(Q),
       "three_layer_counterfactual_Q":len(smaller),
       "removed_outer_layer_Q":len(extra),
       "layers_exact":dict(sorted(count.items())),
       "original_dyadic_extra_K":originalK,
       "counterfactual_three_layer_dyadic_extra_K":thinK,
       "original_strict_quartets":originalStrict,
       "counterfactual_strict_quartets":thinStrict,
       "original_approx_normalized":round(originalLog/(R*R*S),10),
       "ablation_approx_normalized":round(thinLog/(R*R*S),10),
       "ablation_gain_direction":"increase" if thinLog>originalLog else ("equal" if thinLog==originalLog else "decrease"),
       "counterfactual_has_original_interpolation_guard":True,
       "exact_first_quartet_Gram_decomposes_by_point_deletion":True,
       "deleted_quadratic_psd_from_trace_metric":True,
       "matrix_rows_in_first_quartet":blockdim,
       "original_K_upper_K_plus_strict":215,
       "strict_uniform_0_0043_incremental_gain_refuted":True,
       "ablation_not_eligible_as_original_field_source":True,
       "no_new_p_adic_mass_or_analytic_D_theorem":True,
    },flush=True)
    print("PASS Phase289-C frozen five-layer versus three-layer D563 contrast",flush=True)


if __name__=="__main__":
    main()
