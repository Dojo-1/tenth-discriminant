#!/usr/bin/env python3
"""Phase317-C: first 5-adic radical form and Gram congruence tangent test.

For G in Sym_40(Z/25) and G0=G mod5 with rank23, let K be an
independently computed 40x17 basis of ker(G0) over F5. The first
radical-lift form is B_G=(K^T G K mod25)/5 mod5. Its rank is
EXACTLY the e1 Smith multiplicity. This independently checks the
previous unit-pivot Schur algorithm (e1=7).

For a perturbation G'=G+5H, the form changes by K^T H K.
Over characteristic !=2, symmetric H is tangent to the congruence
orbit (H=XG0+G0 X^T) IFF its restriction to radical is zero.
We construct the tangent solution in a basis where G0=diag(A,0)
to independently validate this iff; we NEVER infer "congruence"
just from unchanged Smith rank.

Five synthetic norm-preserving trace-zero wild gauges and positive
and negative congruence controls. No alternate field or new v5 bound.
"""
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313",
               "phase314","phase315","phase316","phase317"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from inert_trace_radicals import rank_f5
from wild_log125 import exhaustive_lift_table
from wild_gauge import actual_original_ray_twist,T,M
from conductor250_original_mod25 import (
    original_integer_source_oracle,gram_from_unit_rays_and_nonunit_lifts,
    unit_and_nonunit_counts
)
from two_digit_smith import two_smith_slices

P=5
MOD=25


def kernel_basis_mod5(a):
    """Independent RREF nullspace, not the Phase311 rank routine."""
    b=np.asarray(a,dtype=np.int64).copy()%P
    rows,cols=b.shape
    pivots=[]
    r=0
    for j in range(cols):
        candidates=np.flatnonzero(b[r:,j])
        if not len(candidates):
            continue
        k=r+int(candidates[0])
        if k!=r:
            b[[r,k],:]=b[[k,r],:]
        b[r,:]=b[r,:]*pow(int(b[r,j]),-1,P)%P
        for i in range(rows):
            if i!=r and b[i,j]:
                b[i,:]=(b[i,:]-b[i,j]*b[r,:])%P
        pivots.append(j)
        r+=1
        if r==rows:
            break
    assert len(pivots)==rank_f5(a)
    free=[j for j in range(cols) if j not in set(pivots)]
    ker=np.zeros((cols,len(free)),dtype=np.int64)
    for k,f in enumerate(free):
        ker[f,k]=1
        for i,j in enumerate(pivots):
            ker[j,k]=(-b[i,f])%P
    assert rank_f5(ker)==len(free) if free else ker.shape[1]==0
    assert not np.any((np.asarray(a,dtype=np.int64)@ker)%P)
    return ker,pivots,free


def inverse_matrix_f5(a):
    a=np.asarray(a,dtype=np.int64)%P
    n,m=a.shape
    if n!=m:
        raise ValueError("inverse only for square matrices")
    b=np.hstack((a.copy(),np.eye(n,dtype=np.int64)))%P
    for j in range(n):
        piv=next((r for r in range(j,n) if b[r,j]%P),None)
        if piv is None:
            raise ValueError("singular matrix")
        if piv!=j:
            b[[piv,j]]=b[[j,piv]]
        b[j,:]=(b[j,:]*pow(int(b[j,j]),-1,P))%P
        for r in range(n):
            if r!=j and b[r,j]:
                b[r,:]=(b[r,:]-b[r,j]*b[j,:])%P
    inv=b[:,n:]%P
    assert np.array_equal((a@inv)%P,np.eye(n,dtype=np.int64)%P)
    return inv


def first_radical_form(g,k):
    mat=np.asarray(g,dtype=np.int64)%MOD
    assert np.array_equal(mat,mat.T)
    full=(k.T@mat@k)%MOD
    assert not np.any(full%P),(
        "radical lift not divisible5, invalid original mod5 kernel")
    B=(full//P)%P
    assert np.array_equal(B,B.T)
    return B


def tangent_witness_or_obstruction(g0,h,k):
    """Construct the generic congruence tangent equation when possible."""
    g0=np.asarray(g0,dtype=np.int64)%P
    h=np.asarray(h,dtype=np.int64)%P
    assert np.array_equal(g0,g0.T) and np.array_equal(h,h.T)
    n=len(g0)
    r=rank_f5(g0)
    assert k.shape==(n,n-r)
    restriction=(k.T@h@k)%P
    if np.any(restriction):
        return {"is_tangent_to_mod5_congruence_orbit":False,
                "radical_restriction_rank":rank_f5(restriction),
                "independent_solvability_witness":False}
    # Complete radical basis with standard columns to a full GL(n,F5).
    cols=[k[:,j] for j in range(k.shape[1])]
    C=[]
    current=len(cols)
    for i in range(n):
        e=np.eye(n,dtype=np.int64)[:,i]
        candidate=np.column_stack(cols+[e])
        if rank_f5(candidate)==current+1:
            cols.append(e)
            C.append(e)
            current+=1
            if current==n:
                break
    assert len(C)==r and current==n
    basis=np.column_stack(C+[k[:,j] for j in range(n-r)])%P
    assert rank_f5(basis)==n
    gp=(basis.T@g0@basis)%P
    hp=(basis.T@h@basis)%P
    assert not np.any(gp[r:,:])
    assert not np.any(gp[:,r:])
    A=gp[:r,:r]
    invA=inverse_matrix_f5(A)
    assert not np.any(hp[r:,r:])
    X=np.zeros((n,n),dtype=np.int64)
    X[:r,:r]=(3*hp[:r,:r]@invA)%P  # 1/2 = 3 in F5
    X[r:,:r]=(hp[r:,:r]@invA)%P
    result=(X@gp+gp@X.T)%P
    assert np.array_equal(result,hp),(
        "claimed tangent while constructive X does not exist")
    return {
        "is_tangent_to_mod5_congruence_orbit":True,
        "radical_restriction_rank":0,
        "independent_solvability_witness":True,
        "congruence_witness_basis_dimension":n,
    }


def radical_tangent_certificate():
    qint,qomega,real,source=original_integer_source_oracle()
    assert len(qomega)==109 and real.shape==(40,40)
    unit,nonunit=unit_and_nonunit_counts(qomega)
    lookup,_=exhaustive_lift_table(163)
    assert np.array_equal(
        gram_from_unit_rays_and_nonunit_lifts(unit,nonunit,lookup),real)

    g0=real%P
    k,piv,free=kernel_basis_mod5(g0)
    assert len(piv)==23 and len(free)==17
    assert k.shape==(40,17)
    baseB=first_radical_form(real,k)
    assert rank_f5(baseB)==7
    assert two_smith_slices(real)["e1_exactly_one_five"]==7

    records=[]
    for scalar in range(5):
        t=(scalar*T[0]%MOD,scalar*T[1]%MOD)
        selected,non2=actual_original_ray_twist(qomega,t)
        assert non2==nonunit
        G=gram_from_unit_rays_and_nonunit_lifts(selected,nonunit,lookup)
        assert np.array_equal(G%P,g0)
        d=(G-real)%MOD
        assert not np.any(d%P)
        H=(d//P)%P
        assert np.array_equal(H,H.T)
        B=first_radical_form(G,k)
        restriction=(k.T@H@k)%P
        assert np.array_equal((B-baseB)%P,restriction)
        smith=two_smith_slices(G)
        assert smith["e1_exactly_one_five"]==rank_f5(B)==7
        tangent=tangent_witness_or_obstruction(g0,H,k)
        assert tangent["radical_restriction_rank"]==rank_f5(restriction)
        nonzero=np.argwhere(restriction)
        witness=None
        if len(nonzero):
            i,j=nonzero[0]
            witness={"basis_i":int(i),"basis_j":int(j),
                     "pairing_mod5":int(restriction[i,j])}
        records.append({
            "twist_scalar":scalar,
            "actual_original_Gram_entries_changed_mod25":int(np.count_nonzero(d)),
            "radical_dim":k.shape[1],
            "first_radical_form_rank":rank_f5(B),
            "first_radical_form_equal_original":np.array_equal(B,baseB),
            "difference_restricted_to_radical_rank":rank_f5(restriction),
            "first_nonzero_radical_difference_if_any":witness,
            "tangent_result":tangent,
            "Smith_e0_e1_ege2":[smith["e0_unit_smith_factors"],
                                 smith["e1_exactly_one_five"],
                                 smith["e_at_least_2"]]
        })
    assert [x["actual_original_Gram_entries_changed_mod25"] for x in records]==[
        0,363,363,363,363]
    assert all(x["Smith_e0_e1_ege2"]==[23,7,10] for x in records)

    # Required positive tangent control. This U=I+5X is
    # invertible over Z/25 regardless of X.
    X=np.zeros((40,40),dtype=np.int64)
    X[0,1]=1;X[7,3]=2;X[20,39]=4
    U=(np.eye(40,dtype=np.int64)+5*X)%MOD
    congruent=(U@real@U.T)%MOD
    Hpos=(((congruent-real)%MOD)//P)%P
    Bpos=first_radical_form(congruent,k)
    assert np.array_equal(Bpos,baseB)
    tpos=tangent_witness_or_obstruction(g0,Hpos,k)
    assert tpos["is_tangent_to_mod5_congruence_orbit"]
    assert tpos["independent_solvability_witness"]
    assert two_smith_slices(congruent)["e1_exactly_one_five"]==7

    # Required non-tangent control, independent of the actual
    # gauge. Choose a rank-one symmetric perturbation visible on R.
    i=next(i for i in range(40) if np.any(k[i,:]))
    N=np.zeros((40,40),dtype=np.int64)
    N[i,i]=1
    assert rank_f5((k.T@N@k)%P)==1
    tneg=tangent_witness_or_obstruction(g0,N,k)
    assert not tneg["is_tangent_to_mod5_congruence_orbit"]
    assert tneg["radical_restriction_rank"]==1

    return {
        "D":163,
        "original_Q":len(qomega),
        "original_source_Gram_dimension":40,
        "original_Gram_mod5_rank":rank_f5(g0),
        "original_Gram_mod5_radical_dimension":k.shape[1],
        "independent_radical_first_lift_original_rank":rank_f5(baseB),
        "independent_Smith_unit_pivot_e1":7,
        "synthetic_five_gauge_first_lift_profiles":records,
        "positive_explicit_U_equal_I_plus_5X_congruence":tpos,
        "negative_rank_one_radical_non_tangent_control":tneg,
        "no_full_Smith_or_new_determinant_claim":True,
        "no_real_alternative_quadratic_field":True,
    }


def main():
    print("PHASE317_RADICAL_FIRST_LIFT_AND_TANGENT_PASS",
          radical_tangent_certificate(),flush=True)


if __name__=="__main__":
    main()
