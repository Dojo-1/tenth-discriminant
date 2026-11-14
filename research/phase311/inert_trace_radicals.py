#!/usr/bin/env python3
"""Phase311: ORIGINAL inert-p5 maximal-order source vs trace-pairing radicals.

The quadratic residue field F25 and the actual conjugation permutation
explain why Frobenius evaluation-kernel mass is DIFFERENT from a restricted
Hermitian trace radical. Exact field arithmetic, not scalar geometry.
D203 is non-h1; D163 h1 vs D187 non-h1 are matched negative controls.
"""
from itertools import product
from math import isqrt
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
for folder in ("phase303", "phase304", "phase307"):
    sys.path.insert(0,str(ROOT/"research"/folder))
import highjet_d203_original as d203_source
import matched_nonh1_field_controls as matched_source
from source_saturation import independent_original_jets, omega_product, original_fifty_row_saturation

P=5
MOD=25
ROOT5=5


def is_inert_five(d):
    m=(d+1)//4
    return d>0 and d%4==3 and (1-4*m)%5 in (2,3)


def f25_norm(a,b,m):
    return (a*a+a*b+m*b*b)%5


def field_checks(d):
    if not is_inert_five(d):
        raise ValueError("selected prime5 must be inert in maximal order")
    m=(d+1)//4
    assert all(f25_norm(a,b,m)!=0
               for a,b in product(range(5),repeat=2) if a or b)
    omega=(0,1)
    z=(1,0)
    for _ in range(5):
        z=omega_product(z,omega,d,5)
    assert z==(1,4),("Frobenius omega5 must be conjugate omega",d,z)
    return True


def rank_f5(matrix):
    a=np.asarray(matrix,dtype=np.int64).copy()%5
    if a.ndim!=2:
        raise ValueError("Fp rank expects 2D array")
    n,cols=a.shape
    r=0
    for col in range(cols):
        where=np.flatnonzero(a[r:,col])
        if not len(where):
            continue
        i=r+int(where[0])
        if i!=r:
            a[[i,r],:]=a[[r,i],:]
        inv=pow(int(a[r,col]),-1,5)
        a[r,col:]=(a[r,col:]*inv)%5
        if r+1<n:
            coeff=a[r+1:,col:col+1].copy()
            a[r+1:,col:]=(a[r+1:,col:]-coeff*a[r:r+1,col:])%5
        r+=1
        if r==n:
            break
    return r


def rank_f25(E,d):
    """Genuine field-row elimination; an F5 row rank is insufficient."""
    field_checks(d)
    m=(d+1)//4
    E=np.asarray(E,dtype=np.int64)%5
    if E.ndim!=2 or E.shape[1]%2:
        raise ValueError("GF25 evaluation must contain omega coordinate pairs")
    a=E[:,0::2].copy()
    b=E[:,1::2].copy()
    n,cols=a.shape
    rank=0
    for col in range(cols):
        piv=next((i for i in range(rank,n)
                  if a[i,col]!=0 or b[i,col]!=0),None)
        if piv is None:
            continue
        if piv!=rank:
            a[[piv,rank],:]=a[[rank,piv],:]
            b[[piv,rank],:]=b[[rank,piv],:]
        u,v=int(a[rank,col]),int(b[rank,col])
        norm=f25_norm(u,v,m)
        assert norm!=0
        t=pow(norm,-1,5)
        inv_a=((u+v)*t)%5
        inv_b=(-v*t)%5
        old_a=a[rank,col:].copy()
        old_b=b[rank,col:].copy()
        a[rank,col:]=(inv_a*old_a-m*inv_b*old_b)%5
        b[rank,col:]=(inv_a*old_b+inv_b*old_a+inv_b*old_b)%5
        assert a[rank,col]==1 and b[rank,col]==0
        for i in range(rank+1,n):
            x,y=int(a[i,col]),int(b[i,col])
            if x==y==0:
                continue
            row_a=a[rank,col:]
            row_b=b[rank,col:]
            prod_a=(x*row_a-m*y*row_b)%5
            prod_b=(x*row_b+y*row_a+y*row_b)%5
            a[i,col:]=(a[i,col:]-prod_a)%5
            b[i,col:]=(b[i,col:]-prod_b)%5
            assert a[i,col]==b[i,col]==0
        rank+=1
        if rank==n:
            break
    return rank


def realification_rank(E,d):
    """Independent F5 encoding of the same F25-linear row span."""
    E=np.asarray(E,dtype=np.int64)%5
    a,b=E[:,0::2],E[:,1::2]
    m=(d+1)//4
    # ω*(a+bω)=-m*b+(a+b)ω
    double=np.vstack((
        np.concatenate((a,b),axis=1),
        np.concatenate(((-m*b)%5,(a+b)%5),axis=1)
    ))
    return rank_f5(double)


def trace_gram_from_original(E,d):
    E=np.asarray(E,dtype=np.int64)%5
    a,b=E[:,0::2],E[:,1::2]
    coef=(d+1)//2
    return (2*(a@a.T)+(a@b.T)+(b@a.T)+coef*(b@b.T))%5


def conjugation_permutation(q,J):
    idx={z:i for i,z in enumerate(q)}
    if len(idx)!=len(q):
        raise ValueError("actual source has duplicate observations")
    perm=[]
    for z in q:
        conjugate=(z[0]+z[1],-z[1])
        if conjugate not in idx:
            raise ValueError("observation support not conjugation-closed")
        perm.append(idx[conjugate])
    assert all(perm[perm[i]]==i for i in range(len(q)))
    return tuple(j*len(q)+perm[i] for j in range(J) for i in range(len(q)))


def inert_cross_trace_certificate(E,q,J,d):
    """Every Gram cell reconstructed via trace of conjugate-mirror product."""
    field_checks(d)
    E=np.asarray(E,dtype=np.int64)%5
    n=E.shape[0]
    assert E.shape[1]==2*J*len(q)
    index=conjugation_permutation(q,J)
    a,b=E[:,0::2],E[:,1::2]
    ap,bp=a[:,list(index)],b[:,list(index)]
    assert np.array_equal(ap,(a+b)%5)
    assert np.array_equal(bp,(-b)%5)
    m=(d+1)//4
    h_a=(a@ap.T-m*(b@bp.T))%5
    h_b=(a@bp.T+b@ap.T+b@bp.T)%5
    assert np.all(h_b==0),(
        "Conjugation-stable original source must make Hermitian moments F5-valued")
    gram=(2*h_a)%5
    from_original=trace_gram_from_original(E,d)
    assert np.array_equal(gram,from_original)
    assert np.array_equal(gram,gram.T)
    # The wrong nonconjugate contraction should fail on at least the D203
    # native source; do not demand this on every separately matched arm.
    wrong_a=(a@a.T-m*(b@b.T))%5
    wrong_b=(a@b.T+b@a.T+b@b.T)%5
    return {
        "full_Gram_cells_checked":n*n,
        "conjugation_mirror_field_coordinates_checked":int(E.size),
        "original_Gram_rank_F5":rank_f5(gram),
        "non_conjugate_contraction_differs":
            (not np.array_equal(wrong_a,h_a) or np.any(wrong_b)),
        "conjugation_fixed_moment":True
    }


def full_omega_q(d,rho):
    m=(d+1)//4
    bmax=isqrt((4*rho*rho)//d)
    q=[]
    for b in range(-bmax,bmax+1):
        bound=rho+bmax+1
        for a in range(-bound,bound+1):
            if a*a+a*b+m*b*b<=rho*rho:
                q.append((a,b))
    assert len(q)==len(set(q))
    return tuple(q)


def matched_full_source(d):
    assert d in (163,187)
    field_checks(d)
    raw,even=matched_source.norm_points(d,21*21)
    q=tuple(((x-y)//2,y) for x,y in raw)
    assert len(q)==len(set(q))
    assert set(q)==set(full_omega_q(d,21))
    E=np.zeros((40,2*len(q)),dtype=np.int64)
    for i,z in enumerate(q):
        val=(1,0)
        for r in range(40):
            E[r,2*i],E[r,2*i+1]=val
            val=omega_product(val,z,d,MOD)
    # Exact second evaluator from Phase304's independent half-order source.
    g=matched_source.power_grid(raw,d,40)
    assert len(g)==len(q)
    checked=0
    for i,line in enumerate(g):
        for r,(x,y) in enumerate(line):
            assert (x-y)%2==0
            expected=((x-y)//2%MOD,y%MOD)
            assert (E[r,2*i],E[r,2*i+1])==expected
            checked+=2
    return q,E,checked


def matched_primitive(E):
    E=np.asarray(E,dtype=np.int64)%MOD
    assert E.shape[0]==40
    prim=E.copy()
    for r in range(25,40):
        diff=(E[r,:]-E[r-24,:])%MOD
        assert not np.any(diff%5)
        prim[r,:]=diff//5
    return prim%5


def d203_full_source():
    field_checks(203)
    d203_source.guard()
    rho,R,S,J,_=d203_source.params(203)
    assert (rho,R,S,J)==(24,50,2,2)
    q=tuple(d203_source.qmax(rho))
    assert len(q)==263 and set(q)==set(full_omega_q(203,24))
    E=d203_source.evaluate_original_jets(q,R,S,J,MOD)
    E2=independent_original_jets(q,203,MOD)
    assert E.shape==(100,1052) and np.array_equal(E,E2)
    changed,primitive,selected=original_fifty_row_saturation(E)
    assert len(selected)==50 and all(not np.any(changed[i,:]%5) for i in selected)
    return q,E,primitive%5


def analyze_arm(d,q,E,prim,J,expected):
    n=len(E)
    re0=rank_f25(E,d)
    re1=rank_f25(prim,d)
    real0=realification_rank(E,d)
    real1=realification_rank(prim,d)
    assert (real0,real1)==(2*re0,2*re1)
    gram0=inert_cross_trace_certificate(E,q,J,d)
    gram1=inert_cross_trace_certificate(prim,q,J,d)
    rg0=gram0["original_Gram_rank_F5"]
    rg1=gram1["original_Gram_rank_F5"]
    assert re0>=rg0 and re1>=rg1
    assert [re0,rg0,re1,rg1]==expected,(d,[re0,rg0,re1,rg1],expected)
    source_divisions=n-re0
    primitive_radical=re1-rg1
    floor=2*source_divisions+primitive_radical
    if d==203:
        assert source_divisions==50 and primitive_radical==37
        assert floor==137
        assert gram0["non_conjugate_contraction_differs"]
    else:
        assert source_divisions==15 and primitive_radical==0
        assert floor==30
    return {
        "D":d,
        "actual_original_Q":len(q),
        "original_source_rows":n,
        "ordinary_jet_count":J,
        "original_evaluation_rank_F25":re0,
        "original_Gram_rank_F5":rg0,
        "original_evaluation_kernel_dimension":n-re0,
        "original_additional_restricted_trace_radical_dimension":re0-rg0,
        "primitive_evaluation_rank_F25":re1,
        "primitive_Gram_rank_F5":rg1,
        "primitive_source_kernel_dimension":n-re1,
        "primitive_restricted_trace_radical_dimension":primitive_radical,
        "exact_integral_p_divided_source_rows":source_divisions,
        "same_original_Gram_valuation_floor_from_disjoint_steps":floor,
        "full_original_or_primitive_Gram_cells_checked":
            gram0["full_Gram_cells_checked"]+gram1["full_Gram_cells_checked"],
        "source_and_primitive_realification_rank_checks":[real0,real1],
        "all_inert_cross_pairing_checks_pass":True,
        "not_class_number_one_diagnostic":True,
        "not_additive_to_old_valuationWeight":True,
        "no_new_uniform_field_cutoff":True
    }


def main():
    outcomes=[]
    q,e,prim=d203_full_source()
    outcomes.append(analyze_arm(203,q,e,prim,2,[50,38,100,63]))
    for d in (163,187):
        q,e,cnt=matched_full_source(d)
        prim=matched_primitive(e)
        arm=analyze_arm(d,q,e,prim,1,[25,25,40,40])
        arm["second_exact_original_source_coordinate_checks"]=cnt
        outcomes.append(arm)
    # Matched D163 (h1) and D187 (non-h1) carry the SAME profile.
    assert all(outcomes[1][key]==outcomes[2][key] for key in (
        "original_evaluation_rank_F25",
        "original_Gram_rank_F5",
        "primitive_evaluation_rank_F25",
        "primitive_Gram_rank_F5",
        "same_original_Gram_valuation_floor_from_disjoint_steps"
    ))
    try:
        field_checks(211)
        raise AssertionError("split field D211 misidentified as inert")
    except ValueError:
        pass
    # A missing conjugate point is not an admissible original full source.
    cut=tuple(z for z in q if z!=(0,1))
    if (1,-1) in cut:
        try:
            conjugation_permutation(cut,1)
            raise AssertionError("broken conjugate support accepted")
        except ValueError:
            pass
    print("PHASE311_INERT_TRACE_RADICAL_PASS",{
       "arms":outcomes,
       "matched_h1_D163_nonh1_D187_profiles_indistinguishable":True,
       "split_D211_negative_control_rejected":True,
       "absent_conjugate_observation_rejected":True,
       "D203_existing_exact_original_v5_G_regression":138,
       "new_same_original_D203_floor_le_exact_138":outcomes[0]["same_original_Gram_valuation_floor_from_disjoint_steps"]<=138,
       "no_field_bound_improvement":True
    },flush=True)


if __name__=="__main__":
    main()
