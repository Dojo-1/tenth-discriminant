#!/usr/bin/env python3
"""Phase310-B: exact full original split-prime DVR Smith and conjugate mirror.

At split p=3 the two local source evaluations are related by an actual
permutation at EVERY p-adic precision. Smith profiles are equal by typed
transport, not by a numeric coincidence.

No automatic field-bound improvement or globally principal Fitting ideal.
"""
from collections import Counter
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for path in ("phase304","phase307","phase308","phase310"):
    sys.path.insert(0,str(ROOT/"research"/path))

import highjet_d203_original as original
from source_saturation import independent_original_jets
from picard_tendrils import hensel_tower
from full_source_split_mirror import conjugation_permutation, f_rank

D,P,K=203,3,10
MOD=P**K
R,S,J=50,2,2


def v_p(x,p,limit):
    if x==0:
        return limit
    out=0
    while out<limit and x%p==0:
        out+=1
        x//=p
    return out


def rectangular_smith_dvr(matrix,p,precision):
    """Gaussian Smith reduction over Z/p^precision with censoring.

    Every operation is an invertible elementary row or column transformation.
    Choose the minimum valuation of a nonzero residue in the submatrix.
    That pivot divides every other entry in the submatrix; after suitable
    unit normalization it eliminates its entire column and row.
    Remaining factors >= precision are CENSORED, not declared zero.
    """
    modulus=p**precision
    A=np.asarray(matrix,dtype=np.int64).copy()%modulus
    if A.ndim!=2:
        raise ValueError("matrix must be 2D")
    n,m=A.shape
    count=min(n,m)
    levels=[]
    for t in range(count):
        block=A[t:,t:]
        found=None
        for e in range(precision):
            mask=(block%(p**e)==0)&(block%(p**(e+1))!=0)
            candidates=np.flatnonzero(mask)
            if candidates.size:
                rr,cc=np.unravel_index(int(candidates[0]),block.shape)
                found=(t+int(rr),t+int(cc),e)
                break
        if found is None:
            levels.extend([precision]*(count-t))
            break
        ri,ci,e=found
        if ri!=t:
            A[[t,ri],:]=A[[ri,t],:]
        if ci!=t:
            A[:,[t,ci]]=A[:,[ci,t]]
        pivot=int(A[t,t])
        q=p**e
        smaller=modulus//q
        assert pivot%q==0
        assert (pivot//q)%p!=0
        unit_inv=pow(pivot//q,-1,smaller)
        # Clear below pivot via exact invertible row operations.
        if t+1<n:
            col=A[t+1:,t].copy()
            assert np.all(col%q==0)
            factors=((col//q)*unit_inv)%smaller
            A[t+1:,t:]=(A[t+1:,t:]-factors[:,None]*A[t,t:])%modulus
            assert np.all(A[t+1:,t]==0)
        # Clear to the right via exact invertible column operations.
        if t+1<m:
            row=A[t,t+1:].copy()
            assert np.all(row%q==0)
            factors=((row//q)*unit_inv)%smaller
            A[t:,t+1:]=(A[t:,t+1:]-A[t:,t:t+1]*factors[None,:])%modulus
            assert np.all(A[t,t+1:]==0)
        levels.append(e)
    assert len(levels)==count
    assert levels==sorted(levels)
    resolved=[e for e in levels if e<precision]
    censored=sum(e==precision for e in levels)
    hist={int(k):int(v) for k,v in sorted(Counter(resolved).items())}
    return {
        "levels":levels,
        "resolved_histogram":hist,
        "censored_at_or_above_precision":censored,
        "lower_bound_valuation_sum":sum(levels),
        "exact_valuation_sum_if_uncensored":
            sum(levels) if not censored else None,
        "rank_mod_p":hist.get(0,0),
        "source_shape":[n,m],
        "modulus":modulus,
    }


def tiny_known_answer_controls():
    diagonal=np.diag(np.asarray([1,3,9,81],dtype=np.int64))
    expect={0:1,1:1,2:1,4:1}
    basic=rectangular_smith_dvr(diagonal,3,K)
    assert basic["resolved_histogram"]==expect and not basic["censored_at_or_above_precision"]
    changed=diagonal.copy()
    changed[0,:]+=2*changed[1,:]
    changed[:,2]+=4*changed[:,3]
    changed[1,:]-=changed[0,:]
    twisted=rectangular_smith_dvr(changed,3,K)
    assert twisted["resolved_histogram"]==expect
    z=rectangular_smith_dvr(np.zeros((3,5),dtype=np.int64),3,K)
    assert z["censored_at_or_above_precision"]==3
    rect=np.zeros((3,6),dtype=np.int64)
    rect[:3,:3]=np.eye(3,dtype=np.int64)
    assert rectangular_smith_dvr(rect,3,K)["resolved_histogram"]=={0:3}
    return {"known_diagonal_histogram":expect,
            "unimodular_row_column_shear_preserves":True,
            "zero_matrix_factors_censored":3,
            "rectangular_unit_test":True}


def actual_D203_split_dvr():
    controls=tiny_known_answer_controls()
    original.guard()
    rho,r,s,j,_=original.params(D)
    assert (rho,r,s,j)==(24,R,S,J)
    q=tuple(original.qmax(rho))
    assert len(q)==263
    E=original.evaluate_original_jets(q,R,S,J,MOD)
    independent=independent_original_jets(q,D,MOD)
    assert E.shape==(100,1052) and np.array_equal(E,independent)
    roots=hensel_tower(D,P,0,K)
    root=int(roots[-1].root)
    root_conj=(1-root)%MOD
    assert (root*root-root+51)%MOD==0
    assert (root_conj*root_conj-root_conj+51)%MOD==0
    assert root%3==0 and root_conj%3==1
    for t in roots:
        assert t.root==root%(3**t.level)
        assert (1-t.root)%(3**t.level)==root_conj%(3**t.level)

    A=E[:,0::2].astype(np.int64)
    B=E[:,1::2].astype(np.int64)
    X0=(A+root*B)%MOD
    X1=(A+root_conj*B)%MOD
    assert X0.shape==X1.shape==(100,526)
    perm=conjugation_permutation(q)
    idx=[k*len(q)+perm[i] for k in range(J) for i in range(len(q))]
    assert len(idx)==526
    assert np.array_equal(X1,X0[:,idx]),(
        "conjugate local maps not actual original point permutation mod p^K")

    original_gram=original.original_trace_gram(E,len(q),J,MOD)
    gram_cross=(X0@X1.T+X1@X0.T)%MOD
    gram_mirror=(2*(X0@X0[:,idx].T))%MOD
    assert np.array_equal(original_gram,gram_cross)
    assert np.array_equal(original_gram,gram_mirror)
    assert np.array_equal(original_gram,original_gram.T)

    local0=rectangular_smith_dvr(X0,P,K)
    local1=rectangular_smith_dvr(X1,P,K)
    gram=rectangular_smith_dvr(original_gram,P,K)
    assert local0["levels"]==local1["levels"]
    assert local0["rank_mod_p"]==local1["rank_mod_p"]==12
    assert gram["rank_mod_p"]==12
    assert f_rank(X0%3,3)==12 and f_rank(original_gram%3,3)==12

    v0=local0["exact_valuation_sum_if_uncensored"]
    vg=gram["exact_valuation_sum_if_uncensored"]
    if v0 is not None and vg is not None:
        residual=vg-2*v0
        assert residual>=0,(
            "DVR Smith mismatch: original trace not compatible with integral local index")
        exactly_resolved=True
    else:
        residual=None
        exactly_resolved=False
    return {
        "preregistered_precision":K,
        "modulus":MOD,
        "full_original_source_raw_coordinates_checked":int(E.size),
        "conjugate_local_source_coordinates_checked":int(X0.size),
        "full_original_Gram_cells_checked":int(original_gram.size),
        "hensel_root0":root,
        "hensel_root_conjugate":root_conj,
        "local_smith_hist0":local0["resolved_histogram"],
        "local_smith_hist1":local1["resolved_histogram"],
        "local_smith_censored_count":local0["censored_at_or_above_precision"],
        "local_index_lower_bound_log3":local0["lower_bound_valuation_sum"],
        "original_trace_Gram_smith_hist":gram["resolved_histogram"],
        "Gram_smith_censored_count":gram["censored_at_or_above_precision"],
        "Gram_det_lower_bound_log3":gram["lower_bound_valuation_sum"],
        "all_source_and_Gram_Smith_levels_resolved":exactly_resolved,
        "exact_local_source_index_log3_if_resolved":v0,
        "exact_original_Gram_det_log3_if_resolved":vg,
        "exact_residual_trace_after_two_source_indexes_if_resolved":residual,
        "K_one_source_and_Gram_rank_F3":[12,12],
        "tiny_DVR_oracles":controls,
        "full_original_Q_conjugation_mirror":True,
        "not_computed_global_Picard_ideal":True,
        "D203_non_h1":True,
        "no_field_bound_improved":True,
    }


def main():
    print("PHASE310_FULL_ORIGINAL_SPLIT_DVR_PASS",
          actual_D203_split_dvr(),flush=True)


if __name__=="__main__":
    main()
