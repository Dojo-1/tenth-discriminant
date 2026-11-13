#!/usr/bin/env python3
"""Phase312-D: universal inert GF25 ordinary-jet kernel vs existing weight.

F5[Z,W]/(W-Z^5,(Z^25-Z)^J_eff) is a vector space of dimension
25*J_eff, J_eff=min(J,5) because ordinary derivatives >=5 vanish
in characteristic 5. For R>=25*J_eff the original s0 rows span it.
No new class-number-one cutoff follows merely from this comparison.
"""
from math import comb
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase311",):
    sys.path.insert(0,str(ROOT/"research"/folder))
from inert_trace_radicals import rank_f5,rank_f25
from residue_multiplicity import full_original_residue_evaluator

P=5
D=163


def modulus_polynomial(J):
    """Coefficients of (Z^25-Z)^min(J,5), monic, over F5."""
    if J<1:raise ValueError("J>=1 required")
    k=min(J,5)
    degree=25*k
    f=[0]*(degree+1)
    for h in range(k+1):
        degree_piece=25*h+(k-h)
        f[degree_piece]=(f[degree_piece]+(-1)**(k-h)*comb(k,h))%5
    assert f[-1]==1
    return tuple(f)


def all_power_remainders(max_exponent,J):
    mod=modulus_polynomial(J)
    degree=len(mod)-1
    current=[0]*degree
    current[0]=1
    out=[]
    for e in range(max_exponent+1):
        out.append(tuple(current))
        carry=current[-1]
        nxt=[0]+current[:-1]
        if carry:
            nxt=[(nxt[t]-carry*mod[t])%5 for t in range(degree)]
        current=nxt
    return out


def quotient_rectangular_matrix(R,S,J):
    if min(R,S,J)<1:raise ValueError("nonempty rectangular source and jets")
    d=25*min(J,5)
    max_exp=(R-1)+5*(S-1)
    remainders=all_power_remainders(max_exp,J)
    A=np.asarray([remainders[r+5*s]
                  for r in range(R) for s in range(S)],dtype=np.int64)
    assert A.shape==(R*S,d)
    actual_rank=rank_f5(A)
    if R>=d:
        assert actual_rank==d
    return A,actual_rank


def weight(R,S):
    return sum(min(r//5,t) for r in range(R) for t in range(S))


def weight_closed_form(R,S):
    if min(R,S)<1 or R<5*(S-1):
        return None
    n=S*(S-1)*(3*R-5*(S+1))
    assert n%6==0
    ans=n//6
    assert ans==weight(R,S)
    return ans


def original_residue_jet_oracle(R,S,J):
    j_eff=min(J,5)
    d=25*j_eff
    if R<d:raise ValueError("surjectivity not preregistered")
    all_F25=tuple((a,b) for a in range(5) for b in range(5))
    E=full_original_residue_evaluator(all_F25,D,R,S,J)%5
    assert E.shape==(R*S,2*J*25)
    rank=rank_f25(E,D)
    assert rank==d,(R,S,J,rank,d)
    Q,rank_q=quotient_rectangular_matrix(R,S,J)
    assert rank_q==d
    # The original s=0 rows Z^0..Z^(d-1) form the quotient basis.
    indices=[r*S for r in range(d)]
    reconstruction=(Q@E[indices,:])%5
    assert np.array_equal(E,reconstruction),(
        "universal modular kernel fails an original held-W ordinary jet")
    return {
        "R_S_J":[R,S,J],
        "original_source_rows":R*S,
        "full_universal_F25_ordinary_jet_channels":25*J,
        "active_jet_channels":d,
        "actual_GF25_evaluation_rank":rank,
        "quotient_rank_F5":rank_q,
        "modular_source_kernel":R*S-d,
        "exact_original_residue_source_field_coordinates_checked":int(E.size),
        "pivot_remainder_coordinate_checks":int(E.size),
        "j_ge_5_zero_by_ordinary_factorial":True,
    }


def native_comparator(R,S):
    if R<25*S or S<1:
        raise ValueError("native parameter requires R>=25S and S>=1")
    J=S
    eff=min(S,5)
    h=R*S-25*eff
    w=weight_closed_form(R,S)
    assert w is not None
    if S==1:
        assert (h>w)==(R>25),(R,S,h,w)
    elif S==2:
        assert h>w,(R,S,h,w)
    else:
        assert w>=h,(R,S,h,w)
    return {
        "R":R,"S_equals_J":S,
        "first_level_GF25_kernel_h":h,
        "existing_valuationWeight_formula_w":w,
        "new_first_level_index_square_exponent_2h":2*h,
        "old_weight_exponent_2w":2*w,
        "first_level_kernel_exceeds_old_weight":h>w,
        "old_weight_meets_or_exceeds_first_level_for_S_ge3":S>=3,
        "first_level_not_additive_to_old_weight":True,
        "no_uniform_analytic_cutoff_promotion":True,
    }


def controls():
    oracles=[original_residue_jet_oracle(*case)
             for case in ((40,1,1),(50,2,2),(75,3,3))]
    native_cases=[(25,1),(40,1),(49,1),(50,2),(74,2),
                  (75,3),(99,3),(100,4),(125,5),(150,6),
                  (500,20),(1250,50)]
    comparisons=[native_comparator(*x) for x in native_cases]
    assert all(c["first_level_kernel_exceeds_old_weight"]
               for c in comparisons if c["S_equals_J"]<=2 and c["R"]>25)
    assert all(not c["first_level_kernel_exceeds_old_weight"]
               for c in comparisons if c["S_equals_J"]>=3)
    # A smaller R cannot be assumed to span all 25*J_eff directions.
    short,rankshort=quotient_rectangular_matrix(8,1,1)
    assert rankshort==8 and short.shape==(8,25)
    # Ordinary derivatives of order five are identically zero modulo5.
    x=full_original_residue_evaluator(((0,0),(1,0),(0,1)),D,8,2,6)
    assert not np.any(x[:,2*5*3:2*6*3])
    return {
        "independent_real_F25_original_ordinary_jet_oracles":oracles,
        "native_R_S_comparisons":comparisons,
        "R_below_25J_effective_not_promoted_to_full_rank":True,
        "fifth_ordinary_jet_vanishing_verified":True,
        "stronger_first_level_exists_only_S1_or_S2_in_native_tested_range":True,
        "for_target_large_S_first_level_kernel_does_not_beat_old_weight":True,
        "higher_padic_primitive_remainder_or_ray_class_bound_still_open":True
    }


def main():
    print("PHASE312_KERNEL_WEIGHT_CROSSOVER_PASS",controls(),flush=True)


if __name__=="__main__":
    main()
