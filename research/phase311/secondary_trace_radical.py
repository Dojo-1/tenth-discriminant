#!/usr/bin/env python3
"""Phase311-B: staged symmetric 5-adic trace-radical proof on ORIGINAL D203.

Remove unit trace directions, divide the residual form by5, repeat.
The surviving 1D second-stage radical is resolved by one more quotient,
recovering exact v5(det primitive)=38 from precision 5^3, and original
v5(det G)=2*50+38=138 through explicit unchanged-source factorization.

This is classical DVR congruence algebra; NOT a new universal field bound
or a genuinely cohomological Bockstein.
"""
from collections import Counter
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for name in ("phase304","phase307","phase310"):
    sys.path.insert(0,str(ROOT/"research"/name))
import highjet_d203_original as pilot
from source_saturation import original_fifty_row_saturation
from split_dvr_smith import rectangular_smith_dvr

D,P=203,5
RAW_PRECISION=4
RAW_MOD=P**RAW_PRECISION
GRAM_PRECISION=3
GRAM_MOD=P**GRAM_PRECISION
N,R,S,J=100,50,2,2


def split_units_symmetric(gram,p,precision):
    """Unimodular congruence Schur reduction over Z/p^precision.

    For odd p, an off-diagonal unit in a symmetric residual block can
    be moved to a unit diagonal via e_i -> e_i+e_j. All congruence
    steps preserve determinant valuation; each unit pivot has val0.
    """
    modulus=p**precision
    A=np.asarray(gram,dtype=np.int64).copy()%modulus
    assert A.ndim==2 and A.shape[0]==A.shape[1]
    assert np.array_equal(A,A.T)
    n=A.shape[0]
    k=0
    diag_uses=0
    offdiag_shears=0
    while k<n:
        pivot=next((i for i in range(k,n) if A[i,i]%p!=0),None)
        if pivot is None:
            pair=next(((i,j) for i in range(k,n)
                        for j in range(i+1,n) if A[i,j]%p!=0),None)
            if pair is None:
                break
            i,j=pair
            # Integral shear e_i -> e_i+e_j (row and same column).
            A[i,:]=(A[i,:]+A[j,:])%modulus
            A[:,i]=(A[:,i]+A[:,j])%modulus
            assert A[i,i]%p!=0
            offdiag_shears+=1
            pivot=i
        else:
            diag_uses+=1
        if pivot!=k:
            A[[pivot,k],:]=A[[k,pivot],:]
            A[:,[pivot,k]]=A[:,[k,pivot]]
        pivot_val=int(A[k,k])
        assert pivot_val%p!=0
        inverse=pow(pivot_val,-1,modulus)
        if k+1<n:
            below=A[k+1:,k].copy()
            beside=A[k,k+1:].copy()
            A[k+1:,k+1:]=(A[k+1:,k+1:]
                           -below[:,None]*beside[None,:]*inverse)%modulus
            A[k+1:,k]=0
            A[k,k+1:]=0
        k+=1
    rest=A[k:,k:].copy()
    assert not np.any(rest%p)
    assert np.array_equal(rest,rest.T)
    return {
        "unit_rank":k,
        "divisible_residual":rest,
        "unit_diagonal_pivots_used":diag_uses,
        "offdiagonal_to_diagonal_unit_shears":offdiag_shears,
        "precision":precision,
        "modulus":modulus
    }


def staged_trace_radical(gram,p,precision):
    """Repeated radical filtration, retaining exact censoring on last stage."""
    if precision<1:
        raise ValueError("precision must be positive")
    stage=np.asarray(gram,dtype=np.int64).copy()%(p**precision)
    ranks=[]
    dimensions=[]
    shears=[]
    for level in range(precision):
        d=split_units_symmetric(stage,p,precision-level)
        k=d["unit_rank"]
        dimensions.append(len(stage))
        ranks.append(k)
        shears.append(d["offdiagonal_to_diagonal_unit_shears"])
        rest=d["divisible_residual"]
        if not len(rest):
            break
        if level+1==precision:
            break
        stage=(rest//p)%(p**(precision-level-1))
    censored=dimensions[-1]-ranks[-1]
    histogram={i:k for i,k in enumerate(ranks) if k}
    return {
        "levels_unit_ranks":ranks,
        "levels_residual_dimensions":dimensions,
        "unit_offdiagonal_shears_by_level":shears,
        "smith_exponent_histogram":histogram,
        "censored_factors_at_depth":censored,
        "exact_det_valuation_if_all_resolved":
            sum(i*k for i,k in histogram.items()) if censored==0 else None
    }


def elementary_source_frame():
    """Literal 50 unimodular row shears already used in Phase307."""
    U=np.eye(N,dtype=np.int64)
    chosen=[]
    for r in range(5,R):
        i=2*r
        U[i,2*(r-5)+1]-=1
        chosen.append(i)
    for a in range(5):
        i=2*(45+a)+1
        U[i,2*(26+a)]-=2
        U[i,2*(2+a)]+=1
        chosen.append(i)
    assert len(set(chosen))==50
    return U,set(chosen)


def original_primitive_factorization():
    pilot.guard()
    rho,r,s,j,_=pilot.params(D)
    assert (rho,r,s,j)==(24,R,S,J)
    q=tuple(pilot.qmax(rho))
    assert len(q)==263
    E=pilot.evaluate_original_jets(q,R,S,J,RAW_MOD)
    changed,primitive,selected=original_fifty_row_saturation(E)
    assert len(selected)==50
    original=pilot.original_trace_gram(E,len(q),J,RAW_MOD)
    transformed=pilot.original_trace_gram(changed,len(q),J,RAW_MOD)
    U,chosen=elementary_source_frame()
    assert chosen==selected
    assert np.array_equal((U@original@U.T)%RAW_MOD,transformed)
    primitive_gram=pilot.original_trace_gram(primitive,len(q),J,GRAM_MOD)
    assert primitive_gram.shape==(100,100)
    # p^4 raw precision and p^3 primitive precision are both explicit.
    checked=0
    for i in range(N):
        for j in range(N):
            f=(5 if i in selected else 1)*(5 if j in selected else 1)
            modulus=GRAM_MOD if f==1 else RAW_MOD
            assert int(transformed[i,j])%modulus == (
                f*int(primitive_gram[i,j]))%modulus,(i,j,f)
            checked+=1
    return primitive_gram, {
        "original_D":203,
        "original_Q":len(q),
        "unchanged_original_source_shape":list(E.shape),
        "original_and_primitive_Gram_100x100_factorization_cells_checked":checked,
        "unimodular_shear_count":50,
        "exact_divided_rows":len(selected),
        "original_Gram_mod625_verified":True
    }


def known_answer_controls():
    diag=np.diag(np.asarray([1]*63+[5]*36+[25],dtype=np.int64))
    target={0:63,1:36,2:1}
    a=staged_trace_radical(diag,5,3)
    assert a["smith_exponent_histogram"]==target
    assert a["exact_det_valuation_if_all_resolved"]==38
    # A fully invertible symmetric offdiag form cannot be mistaken for
    # a p-divisible form just because its diagonal is zero.
    b=staged_trace_radical(np.asarray([[0,1],[1,0]]),5,3)
    assert b["smith_exponent_histogram"]=={0:2}
    assert b["unit_offdiagonal_shears_by_level"][0]>=1
    z=staged_trace_radical(np.zeros((3,3),dtype=np.int64),5,3)
    assert z["censored_factors_at_depth"]==3
    assert z["exact_det_valuation_if_all_resolved"] is None
    return {
        "known_diagonal_profile":target,
        "offdiagonal_nonEuclidean_unit_witness":True,
        "censored_zero_matrix_refused_exact_val":True
    }


def unitriangular_congruence(G):
    mod=125
    A=np.asarray(G,dtype=np.int64).copy()%mod
    # Two nontrivial unimodular source-coordinate shears.
    for i,j,t in ((0,11,2),(57,3,-1)):
        A[i,:]=(A[i,:]+t*A[j,:])%mod
        A[:,i]=(A[:,i]+t*A[:,j])%mod
    assert np.array_equal(A,A.T)
    return A


def certificate():
    controls=known_answer_controls()
    g,source=original_primitive_factorization()
    base=staged_trace_radical(g,P,GRAM_PRECISION)
    hist=base["smith_exponent_histogram"]
    expected={0:63,1:36,2:1}
    assert hist==expected
    assert base["levels_residual_dimensions"]==[100,37,1]
    assert base["levels_unit_ranks"]==[63,36,1]
    assert base["censored_factors_at_depth"]==0
    assert base["exact_det_valuation_if_all_resolved"]==38
    independent=rectangular_smith_dvr(g,P,GRAM_PRECISION)
    assert independent["resolved_histogram"]==expected
    assert independent["censored_at_or_above_precision"]==0
    assert independent["exact_valuation_sum_if_uncensored"]==38
    twisted=staged_trace_radical(unitriangular_congruence(g),P,GRAM_PRECISION)
    assert twisted["smith_exponent_histogram"]==expected
    assert twisted["exact_det_valuation_if_all_resolved"]==38
    original_det_val=2*source["exact_divided_rows"]+38
    assert original_det_val==138
    return {
        "source":source,
        "primitive_Gram_trace_radical_dimensions":[100,37,1],
        "primitive_levels_unit_ranks":[63,36,1],
        "primitive_5adic_smith_profile":hist,
        "primitive_exact_determinant_v5":38,
        "original_exact_determinant_v5":original_det_val,
        "independent_generic_DVR_Smith_matches":True,
        "unimodular_congruence_shears_preserve_profile":True,
        "secondary_1D_radical_is_nonzero_after_second_division":True,
        "first_level_lower_bound137_vs_exact138":[137,138],
        "known_answer_controls":controls,
        "no_overlap_with_valuationWeight45_asserted":True,
        "no_new_uniform_h1_bound":True,
        "not_actual_cohomological_Bockstein":True,
    }


def main():
    print("PHASE311_SECONDARY_TRACE_RADICAL_PASS",certificate(),flush=True)


if __name__=="__main__":
    main()
