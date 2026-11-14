#!/usr/bin/env python3
"""Phase313-G: h1 D163 vs h8 D183 with IDENTICAL ORIGINAL integer Q109.

Both fields have the same original matched radius21/R40/S=J1 integer
coordinate support, the same residue ring at prime5, and a different
global class number. This is a negative control for interpreting any
fixed-source v5 as class-number-one-specific. D183's R40 is deliberately
MATCHED, not its native policy.

Exact determinant: arbitrary integers and SymPy DomainMatrix, independent
of primitive modular Schur. Primitive Smith: a separate 5^6 source lift.
"""
from math import isqrt
from pathlib import Path
import sys
import sympy as sp
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase308","phase311"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from adaptive_torsion_family import independent_reduced_forms
from inert_trace_radicals import rank_f5
from secondary_trace_radical import staged_trace_radical

R=40
RHO=21
P=5
PRECISION=6
MOD=P**PRECISION
RAW_MOD=P**(PRECISION+1)


def integer_Q(D):
    q=[]
    for y in range(-isqrt(RHO*RHO//D),isqrt(RHO*RHO//D)+1):
        t=isqrt(RHO*RHO-D*y*y)
        q.extend((x,y) for x in range(-t,t+1))
    assert len(q)==len(set(q))
    return tuple(q)


def exact_source_Gram(D,q):
    g=[[0]*R for _ in range(R)]
    for x,y in q:
        powers=[(1,0)]
        for i in range(1,R):
            a,b=powers[-1]
            powers.append((a*x-D*b*y,a*y+b*x))
        for i in range(R):
            a,b=powers[i]
            for j in range(i,R):
                c,e=powers[j]
                g[i][j]+=2*(a*c+D*b*e)
    for i in range(R):
        for j in range(i):
            g[i][j]=g[j][i]
    assert all(g[i][j]==0 for i in range(R) for j in range(R)
               if (i-j)%2)
    return g


def vp5(n):
    assert n!=0
    v=0
    while n%5==0:
        n//=5
        v+=1
    return (v,n%5)


def primitive_Gram(D,q):
    e=np.zeros((R,2*len(q)),dtype=np.int64)
    for qi,(x,y) in enumerate(q):
        a,b=1,0
        for i in range(R):
            e[i,2*qi:2*qi+2]=(a,b)
            a,b=(a*x-D*b*y)%RAW_MOD,(a*y+b*x)%RAW_MOD
    changed=e.copy()
    for r in range(25,R):
        diff=(e[r,:]-e[r-24,:])%RAW_MOD
        assert not np.any(diff%5)
        changed[r,:]=diff//5
    changed%=MOD
    a,b=changed[:,0::2],changed[:,1::2]
    g=(2*(a@a.T+D*(b@b.T)))%MOD
    assert g.shape==(R,R)
    assert np.array_equal(g,g.T)
    assert rank_f5(g%5)>0
    return g


def arm(D,h):
    assert D in (163,183)
    assert len(independent_reduced_forms(D))==h
    q=integer_Q(D)
    assert len(q)==109
    assert sum(y==0 for x,y in q)==43
    g=exact_source_Gram(D,q)
    d_even=int(sp.Matrix([[g[i][j] for j in range(0,R,2)]
                          for i in range(0,R,2)]).det(method="domain-ge"))
    d_odd=int(sp.Matrix([[g[i][j] for j in range(1,R,2)]
                         for i in range(1,R,2)]).det(method="domain-ge"))
    d_full=int(sp.Matrix(g).det(method="domain-ge"))
    assert d_full==d_even*d_odd and d_full>0
    exact=(vp5(d_even),vp5(d_odd),vp5(d_full))
    gp=primitive_Gram(D,q)
    smith=staged_trace_radical(gp,5,PRECISION)
    h5=rank_f5(gp%5)
    primitive_floor=sum(i*k for i,k in smith["smith_exponent_histogram"].items())+PRECISION*smith["censored_factors_at_depth"]
    assert 2*15+primitive_floor<=exact[2][0],(
        "same-original determinant valuation below source/primitive floor",D)
    if smith["censored_factors_at_depth"]==0:
        assert 2*15+smith["exact_det_valuation_if_all_resolved"]==exact[2][0]
    return {
        "D":D,
        "h_by_standard_reduced_forms":h,
        "matched_not_native_R_S_J":[R,1,1],
        "identical_original_integer_Q109":True,
        "exact_original_integer_Gram_order":R,
        "exact_parity_block_v5":[exact[0][0],exact[1][0]],
        "exact_parity_block_unit_mod5":[exact[0][1],exact[1][1]],
        "exact_full_determinant_v5":exact[2][0],
        "exact_full_determinant_unit_mod5":exact[2][1],
        "primitive_Gram_rank_F5":h5,
        "primitive_Smith_resolved":smith["smith_exponent_histogram"],
        "primitive_Smith_censored_at_depth6":smith["censored_factors_at_depth"],
        "source_exact_5_divisions":15,
        "not_class_number_one_diagnostic":True,
    },g


def matched_controls():
    a,g163=arm(163,1)
    b,g183=arm(183,8)
    q163=integer_Q(163)
    q183=integer_Q(183)
    assert q163==q183
    assert all(z in q183 for z in q163)
    # Same original (x,y) support and D congruent mod5 imply exactly
    # the same first-level original Gram, but higher mod25 lifts need
    # not agree. The exact determinant may or may not differ.
    assert np.array_equal(np.asarray(g163,dtype=object)%5,
                          np.asarray(g183,dtype=object)%5)
    return {
        "h1_D163":a,
        "h8_D183":b,
        "identical_actual_original_pair_observation_support":True,
        "original_Gram_matched_mod5":True,
        "matched_fields_have_different_global_class_number":True,
        "same_exact_v5_measured_not_assumed_before_protocol":
            a["exact_full_determinant_v5"]==b["exact_full_determinant_v5"],
        "same_primitive_5adic_histogram_measured":
            a["primitive_Smith_resolved"]==b["primitive_Smith_resolved"],
        "no_uniform_h1_rank_or_val_inference":True,
    }


def main():
    print("PHASE313_MATCHED_H1_NONH1_ORIGINAL_GRAM_PASS",
          matched_controls(),flush=True)


if __name__=="__main__":
    main()
