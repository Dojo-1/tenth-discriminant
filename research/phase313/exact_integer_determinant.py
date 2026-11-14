#!/usr/bin/env python3
"""Phase313-F independent EXACT INTEGER determinant, not a modular Smith.

Reconstruct the ORIGINAL Lean integer-order Z[sqrt(-163)] Q109 source,
40 polynomial rows 1,Z,...,Z^39, and integer trace 2(ac+163bd)
using only native Python arbitrary integers, THEN compute the 40x40
determinant via SymPy DomainMatrix (domain-ge) and ALSO the two 20x20
exact sign-parity block determinants. The 5-adic valuation is read
by exact integer division, not any Phase310/311/313 DVR routine.

This reproduces the SAME fixed D163 original determinant but is not
external independent human review and not a uniform field theorem.
"""
from math import isqrt

import sympy as sp

D=163
R=40
RHO=21


def original_exact_Gram():
    q=[]
    for y in range(-isqrt(RHO*RHO//D),isqrt(RHO*RHO//D)+1):
        xlim=isqrt(RHO*RHO-D*y*y)
        q.extend((x,y) for x in range(-xlim,xlim+1))
    assert len(q)==109 and len(set(q))==109
    assert sum(y==0 for x,y in q)==43
    g=[[0]*R for _ in range(R)]
    for x,y in q:
        powers=[(1,0)]
        for r in range(1,R):
            a,b=powers[-1]
            powers.append((a*x-D*b*y,a*y+b*x))
        for r in range(R):
            a,b=powers[r]
            for s in range(r,R):
                c,d=powers[s]
                g[r][s]+=2*(a*c+D*b*d)
    for r in range(R):
        for s in range(r):
            g[r][s]=g[s][r]
    assert all(g[r][s]==g[s][r] for r in range(R) for s in range(R))
    assert all(g[r][s]==0 for r in range(R) for s in range(R)
               if (r-s)%2)
    return g,q


def valuation_unit(n,p=5):
    assert n!=0
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v,n%p


def independent_integer_determinant_certificate():
    g,q=original_exact_Gram()
    # No modular input. SymPy's domain-ge exact determinant over ZZ
    # is independent of the earlier Schur and local Smith algorithms.
    full=sp.Matrix(g)
    d_full=int(full.det(method="domain-ge"))
    parity_dets=[]
    parity_records=[]
    for offset in (0,1):
        ids=list(range(offset,R,2))
        matrix=sp.Matrix([[g[r][s] for s in ids] for r in ids])
        det=int(matrix.det(method="domain-ge"))
        assert det>0
        v,unit=valuation_unit(det,5)
        parity_dets.append(det)
        parity_records.append({
            "row_parity":"even" if offset==0 else "odd",
            "block_size":len(ids),
            "exact_determinant_v5":v,
            "exact_determinant_unit_mod5":unit,
            "exact_decimal_digit_count":len(str(det)),
        })
    assert d_full>0 and d_full==parity_dets[0]*parity_dets[1]
    v_full,unit_full=valuation_unit(d_full,5)
    assert v_full==77,(v_full,parity_records)
    assert unit_full==2
    assert [x["exact_determinant_v5"] for x in parity_records]==[37,40]
    assert [x["exact_determinant_unit_mod5"] for x in parity_records]==[4,3]
    return {
        "D":D,
        "original_integer_Q":len(q),
        "original_integer_Gram_order":R,
        "true_40x40_unmodified_original_IntegerTraceGram":True,
        "all_odd_even_cross_entries_EXACTLY_zero":True,
        "independent_sympy_domain_ge_det_without_modular_Smith":True,
        "even_odd_exact_blocks":parity_records,
        "full_40x40_determinant_exact_v5":v_full,
        "full_40x40_determinant_unit_mod5":unit_full,
        "full_exact_determinant_decimal_digits":len(str(d_full)),
        "matches_prior_5adic_15_index_plus_primitive_Smith_77":True,
        "not_a_uniform_class_number_one_field_theorem":True,
    }


def main():
    print("PHASE313_EXACT_INTEGER_DETERMINANT_PASS",
          independent_integer_determinant_certificate(),flush=True)


if __name__=="__main__":
    main()
