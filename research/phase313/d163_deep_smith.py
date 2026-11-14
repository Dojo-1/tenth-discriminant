#!/usr/bin/env python3
"""Phase313-E: exact original h1 D163 integer-order primitive Smith filtration.

NO maximal-order substitution. Original Q109 rho21, R40/S=J1, 40 rows
of Z[sqrt(-163)] and exact trace 2(ac+163bd). Compute source mod5^7,
15 exact integral Frobenius25 /5 row divisions, primitive Gram mod5^6,
and two independent odd-prime Smith algorithms. If any factor remains
censored at depth6, report ONLY a lower bound, not an exact valuation.
"""
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase206","phase310","phase311","phase312","phase313"):
    sys.path.insert(0,str(ROOT/"research"/p))
import source_probe
from kernel_vs_weight import original_integer_ring_mul
from secondary_trace_radical import staged_trace_radical
from split_dvr_smith import rectangular_smith_dvr
from inert_trace_radicals import rank_f5

D,P=163,5
PRECISION=6
MOD=P**PRECISION
RAW_MOD=P**(PRECISION+1)
R=40


def primitive_source_and_Gram():
    rho,r,s,j,Q=source_probe.params(D)
    assert (rho,r,s,j)==(21,40,1,1)
    q=tuple(Q)
    assert len(q)==109 and len(set(q))==109
    e=np.zeros((R,2*len(q)),dtype=np.int64)
    for qi,z in enumerate(q):
        val=(1,0)
        for row in range(R):
            e[row,2*qi:2*qi+2]=val
            val=original_integer_ring_mul(val,z,D,RAW_MOD)
    assert e.shape==(40,218)

    U=np.eye(R,dtype=np.int64)
    changed=e.copy()
    chosen=set(range(25,R))
    for row in sorted(chosen):
        U[row,row-24]-=1
        changed[row,:]=(e[row,:]-e[row-24,:])%RAW_MOD
        assert not np.any(changed[row,:]%P)
    prim=changed.copy()
    for row in chosen:
        prim[row,:]=changed[row,:]//P
    prim%=MOD

    def original_integer_trace(v):
        a=v[:,0::2]%MOD
        b=v[:,1::2]%MOD
        return (2*(a@a.T+D*(b@b.T)))%MOD

    g_raw=original_integer_trace(e)
    g_prim=original_integer_trace(prim)
    d=np.ones(R,dtype=np.int64)
    d[list(chosen)]=P
    lhs=(U@g_raw@U.T)%MOD
    rhs=(d[:,None]*g_prim*d[None,:])%MOD
    assert np.array_equal(lhs,rhs),(
        "Original Lean integer-order same-raw-Gram source factorization broke")
    assert g_prim.shape==(40,40)
    assert rank_f5(g_prim%5)==23
    assert np.array_equal(g_prim,g_prim.T)
    # Characteristic-zero nonvanishing: y=0 has 43 distinct integer
    # x in [-21,21], so degree<40 row polynomials span injectively.
    assert sum(y==0 for x,y in q)==43
    return g_prim,{
        "D":D,"original_integer_Q":len(q),
        "original_native_rho_R_S_J":[rho,r,s,j],
        "original_integer_E_mod5pow7_shape":list(e.shape),
        "source_raw_modulus":RAW_MOD,
        "primitive_modulus":MOD,
        "exact_integral_shears":len(chosen),
        "exact_divided_rows":len(chosen),
        "same_original_1600_Gram_factorization_cells_verified":1600,
        "primitive_G_rank_mod5":rank_f5(g_prim%5),
        "original_nonsingular_from_43_integer_points":True,
    }


def congruence_change(g):
    """Two genuine, independently chosen integer-unimodular shears."""
    a=np.asarray(g,dtype=np.int64).copy()%MOD
    for i,j,t in ((0,11,2),(31,3,-1)):
        a[i,:]=(a[i,:]+t*a[j,:])%MOD
        a[:,i]=(a[:,i]+t*a[:,j])%MOD
    assert np.array_equal(a,a.T)
    return a


def exact_D163_smith_certificate():
    g,source=primitive_source_and_Gram()
    stages=staged_trace_radical(g,P,PRECISION)
    assert stages["levels_unit_ranks"][0]==23
    assert stages["levels_residual_dimensions"][0]==40
    assert stages["levels_residual_dimensions"][1]==17
    generic=rectangular_smith_dvr(g,P,PRECISION)
    assert generic["resolved_histogram"]==stages["smith_exponent_histogram"]
    assert generic["censored_at_or_above_precision"]==stages["censored_factors_at_depth"]
    changed=staged_trace_radical(congruence_change(g),P,PRECISION)
    assert changed["smith_exponent_histogram"]==stages["smith_exponent_histogram"]
    assert changed["censored_factors_at_depth"]==stages["censored_factors_at_depth"]
    count=stages["censored_factors_at_depth"]
    hist=stages["smith_exponent_histogram"]
    primitive_floor=sum(level*value for level,value in hist.items())+PRECISION*count
    assert primitive_floor>=17
    original_floor=2*source["exact_divided_rows"]+primitive_floor
    assert original_floor>=47
    exact_prim=stages["exact_det_valuation_if_all_resolved"]
    exact_original=(2*source["exact_divided_rows"]+exact_prim
                    if exact_prim is not None else None)
    assert (exact_prim is None)==(count>0)
    if exact_original is not None:
        assert exact_original==original_floor
    return {
        "source":source,
        "primitive_smith_histogram_resolved":hist,
        "staged_primitive_residual_dimensions":stages["levels_residual_dimensions"],
        "staged_primitive_unit_ranks":stages["levels_unit_ranks"],
        "censored_factors_at_or_above_depth6":count,
        "primitive_determinant_v5_lower_bound":primitive_floor,
        "same_original_determinant_v5_lower_bound":original_floor,
        "primitive_exact_v5_if_uncensored":exact_prim,
        "same_original_exact_v5_if_uncensored":exact_original,
        "independent_rectangular_DVR_Smith_matches":True,
        "integer_unimodular_source_shears_preserve_smith":True,
        "none_of_this_additive_to_valuationWeight0":True,
        "no_large_field_bound_improvement":True,
    }


def main():
    print("PHASE313_H1_ORIGINAL_DEEP_SMITH_PASS",
          exact_D163_smith_certificate(),flush=True)


if __name__=="__main__":
    main()
