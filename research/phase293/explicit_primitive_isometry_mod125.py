#!/usr/bin/env python3
"""Phase293-C: construct explicit primitive pairing isometries modulo 125.

Pre-registered at e84e3ce BEFORE implementation. Original D583 full
725-row source vs D587 first-725-row diagnostic. This is a Z/125
PRIMITIVE PAIRING congruence, NOT a GL_725(Z) original-source gauge.
"""
import hashlib
from collections import Counter
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase292","phase293"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from matched_inert5_neighbor import source_normalized, metric_gram, independent_rank
from primitive_graded_jordan import (
    source_guard, source_sector, parity_rows,
    EXPECTED_SOURCE, EXPECTED_PRIMITIVE
)

P=5
K=3
MOD=125
DVALUES=(583,587)

def diagonal_congruence_with_transform(H):
    """T H T^T is diagonal modulo 125; T is integral-unimodular mod 5."""
    A=np.asarray(H,dtype=np.int64).copy()%MOD
    n,m=A.shape
    assert n==m and np.array_equal(A,A.T)
    T=np.eye(n,dtype=np.int64)
    levels=[]
    for t in range(n):
        rem=A[t:,t:]
        level=next((e for e in range(K)
                    if np.any(rem%(P**(e+1))!=0)),None)
        assert level is not None,("unexpected 5-adic grade>=3",t,n)
        stride=P**(level+1)
        opts=np.flatnonzero(np.diag(A)[t:]%stride!=0)
        if opts.size:
            idx=t+int(opts[0])
        else:
            off=np.argwhere(rem%stride!=0)
            idx,j=next(((int(x)+t,int(y)+t)
                        for x,y in off if x!=y), (None,None))
            assert idx is not None
            A[idx,:]=(A[idx,:]+A[j,:])%MOD
            A[:,idx]=(A[:,idx]+A[:,j])%MOD
            T[idx,:]=(T[idx,:]+T[j,:])%MOD
            assert A[idx,idx]%stride!=0
        if idx!=t:
            A[[t,idx],:]=A[[idx,t],:]
            A[:,[t,idx]]=A[:,[idx,t]]
            T[[t,idx],:]=T[[idx,t],:]
        d=int(A[t,t])
        assert d%(P**level)==0 and d%stride!=0
        levels.append(level)
        if t+1<n:
            b=A[t+1:,t].copy()
            assert np.all(b%(P**level)==0)
            q=MOD//(P**level)
            inv=pow(d//(P**level),-1,q)
            c=(b//(P**level)*inv)%q
            oldT=T[t,:].copy()
            T[t+1:,:]=(T[t+1:,:]-c[:,None]*oldT)%MOD
            tail=A[t+1:,t+1:].copy()
            A[t+1:,t+1:]=(tail-np.outer(c,b)-np.outer(b,c)
                          +d*np.outer(c,c))%MOD
            A[t+1:,t]=0
            A[t,t+1:]=0
            assert np.array_equal(A[t+1:,t+1:],A[t+1:,t+1:].T)
    assert levels==sorted(levels)
    diagonal=np.diag(A).copy()
    assert np.count_nonzero(A-np.diag(diagonal))==0
    assert all((int(diagonal[i])//(P**e))%P
               for i,e in enumerate(levels))
    # Verify FULL, not only the diagonal or determinant.
    assert np.array_equal((T@H@T.T)%MOD,A)
    assert independent_rank(T%P)==n
    return diagonal,levels,T

def square_root_unit(ratio):
    """Hensel lift an odd-prime unit square to the unique selected root."""
    ratio=int(ratio)%MOD
    x=next((i for i in range(1,P) if i*i%P==ratio%P),None)
    if x is None:raise ValueError("unit target is a nonsquare modulo 5")
    for e in (1,2):
        power=P**e
        assert (ratio-x*x)%power==0
        delta=((ratio-x*x)//power)%P
        derivative=(2*x)%P
        t=(delta*pow(derivative,-1,P))%P
        x+=power*t
    assert x*x%MOD==ratio
    return x

def binary_norm_representation(a,c,b):
    """Find exact a*x^2+c*y^2=b modulo 125 with unit-vector control."""
    a,c,b=map(lambda z:int(z)%MOD,(a,c,b))
    assert a%P and b%P and c%P
    pair=next(((x,y) for x in range(P) for y in range(P)
               if (x or y) and (a*x*x+c*y*y-b)%P==0),None)
    if pair is None:raise ValueError("binary unit form failed to represent unit")
    x,y=pair
    for e in (1,2):
        power=P**e
        err=(b-a*x*x-c*y*y)
        assert err%power==0
        delta=(err//power)%P
        if x%P:
            step=delta*pow((2*a*x)%P,-1,P)%P
            x+=power*step
        else:
            assert y%P
            step=delta*pow((2*c*y)%P,-1,P)%P
            y+=power*step
    assert (a*x*x+c*y*y-b)%MOD==0
    return x%MOD,y%MOD

def match_unimodular_diagonals(src,tgt):
    """Construct S with S diag(src) S^T = diag(tgt) over Z/125."""
    a=[int(x)%MOD for x in src]
    b=[int(x)%MOD for x in tgt]
    n=len(a)
    assert n==len(b) and n>0
    assert all(x%P for x in a+b)
    S=np.eye(n,dtype=np.int64)
    old=np.diag(a).astype(np.int64)
    for i in range(n-1):
        ai,ci=a[i],a[i+1]
        bi=b[i]
        x,y=binary_norm_representation(ai,ci,bi)
        oldi=S[i,:].copy()
        oldj=S[i+1,:].copy()
        S[i,:]=(x*oldi+y*oldj)%MOD
        S[i+1,:]=(-ci*y*oldi+ai*x*oldj)%MOD
        assert (ai*x*x+ci*y*y)%MOD==bi
        a[i]=bi
        a[i+1]=(ai*ci*bi)%MOD
        assert a[i+1]%P
    last=square_root_unit(b[-1]*pow(a[-1],-1,MOD)%MOD)
    S[-1,:]=(last*S[-1,:])%MOD
    assert np.array_equal((S@old@S.T)%MOD,np.diag(b)%MOD)
    assert independent_rank(S%P)==n
    return S

def inverse_unimodular(A):
    """Entirely integral Gauss-Jordan inverse modulo 125."""
    A=np.asarray(A,dtype=np.int64)%MOD
    n,m=A.shape
    assert n==m
    augmented=np.concatenate((A.copy(),np.eye(n,dtype=np.int64)),axis=1)
    for j in range(n):
        opts=np.flatnonzero(augmented[j:,j]%P!=0)
        assert opts.size,("non-invertible candidate",j)
        pivot=j+int(opts[0])
        if pivot!=j:
            augmented[[j,pivot],:]=augmented[[pivot,j],:]
        inv=pow(int(augmented[j,j]),-1,MOD)
        augmented[j,:]=(inv*augmented[j,:])%MOD
        affected=np.flatnonzero(augmented[:,j])
        affected=affected[affected!=j]
        if affected.size:
            coef=augmented[affected,j].copy()
            augmented[affected,:]=(augmented[affected,:]
                                -coef[:,None]*augmented[j,:])%MOD
    assert np.array_equal(augmented[:,:n],np.eye(n,dtype=np.int64))
    result=augmented[:,n:]
    assert np.array_equal((result@A)%MOD,np.eye(n,dtype=np.int64))
    return result

def explicit_primitive_congruence(Ha,Hb):
    """Produce X in GL_n(Z/125) with X Ha X^T = Hb exactly mod 125."""
    assert Ha.shape==Hb.shape
    da,ea,Ta=diagonal_congruence_with_transform(Ha)
    db,eb,Tb=diagonal_congruence_with_transform(Hb)
    assert ea==eb,("different Jordan grade ranks",Counter(ea),Counter(eb))
    n=len(ea)
    S=np.zeros((n,n),dtype=np.int64)
    grades={}
    for e in sorted(set(ea)):
        idx=[i for i,v in enumerate(ea) if v==e]
        a=[int(da[i]//(P**e))%MOD for i in idx]
        b=[int(db[i]//(P**e))%MOD for i in idx]
        sign=lambda vec: 1 if pow(
            int(np.prod(np.array(vec,dtype=object)%P)%P),
            (P-1)//2,P)==1 else -1
        assert sign(a)==sign(b),("Jordan unit class obstruction",e)
        unit_change=match_unimodular_diagonals(a,b)
        S[np.ix_(idx,idx)]=unit_change
        grades[str(e)]={"rank":len(idx),"Legendre_unit_det":sign(a)}
    assert independent_rank(S%P)==n
    # Verify diagonalized congruence BEFORE converting the basis.
    assert np.array_equal((S@np.diag(da)@S.T)%MOD,np.diag(db)%MOD)
    X=(inverse_unimodular(Tb)@S@Ta)%MOD
    assert independent_rank(X%P)==n
    assert np.array_equal((X@Ha@X.T)%MOD,Hb%MOD),(
        "constructed pairing transport does not commute"
    )
    digest=hashlib.sha256(X.astype(np.uint8).tobytes()).hexdigest()
    return {"dimension":n,"Jordan_grades":grades,
            "original_mod125_pairing_congruence_verified":True,
            "GL_n_Zmod125_rank_mod5":n,
            "deterministic_isometry_matrix_sha256":digest}

def controls():
    mismatched=False
    try:
        match_unimodular_diagonals([1],[2])
    except ValueError:
        mismatched=True
    assert mismatched
    unit=match_unimodular_diagonals([1,1],[2,2])
    assert np.array_equal((unit@np.eye(2,dtype=np.int64)@unit.T)%MOD,
                          np.diag([2,2])%MOD)
    A=np.diag([1,2,5,10]).astype(np.int64)
    B=np.diag([2,1,10,5]).astype(np.int64)
    mixed=explicit_primitive_congruence(A,B)
    assert mixed["dimension"]==4
    off=np.array([[0,1],[1,0]],dtype=np.int64)
    T=np.array([[1,1],[1,2]],dtype=np.int64)
    C=(T@off@T.T)%MOD
    off_result=explicit_primitive_congruence(off,C)
    assert off_result["dimension"]==2
    return {"equal_smith_but_nonsquare_rank_one_isometry_rejected":True,
            "rank_two_unit_isometry_explicit":True,
            "mixed_grade_and_offdiagonal_congruence_verified":True}

def original_primitive_sectors(D):
    rho,R,S,J,Q=params(D)
    assert (rho,S,J,len(Q))==(53,5,5,383)
    assert R==(145 if D==583 else 146)
    C,F,_=source_normalized(D,Q,R,S,J)
    assert F==(1350 if D==583 else 1360)
    C=C[:725,:]
    prim={}
    expected_grade={0:Counter(),1:Counter()}
    for parity,name in ((0,"even"),(1,"odd")):
        ids=parity_rows(145,S,parity)
        summary,Pmat=source_sector(C,D,Q,145,S,J,ids)
        assert summary["row_count"]==(363 if name=="even" else 362)
        prim[name]=metric_gram(Pmat,D,J,Q,MOD)
        for label,grade in summary["primitive_H_Jordan_graded_signs"].items():
            expected_grade[parity][int(label)]=grade["rank"]
    assert sum(expected_grade[0].values())==363
    assert sum(expected_grade[1].values())==362
    return prim,Q

def main():
    source_guard()
    validated=controls()
    A,Q=original_primitive_sectors(583)
    B,Qb=original_primitive_sectors(587)
    assert Q==Qb
    assert 2*(587-583)*sum(y*y for x,y in Q)==4272
    witnesses={}
    for parity in ("even","odd"):
        witnesses[parity]=explicit_primitive_congruence(A[parity],B[parity])
        print("PHASE293C_CONSTRUCTIVE_PARITY_ISOMETRY",{
            "parity":parity,**witnesses[parity]},flush=True)
    assert witnesses["even"]["dimension"]==363
    assert witnesses["odd"]["dimension"]==362
    print("PHASE293C_EXPLICIT_PRIMITIVE_PAIRING_TRANSPORT",{
        "full_original_D583_n":725,
        "D587_first725_only_diagnostic":True,
        "all_original_Q":len(Q),"all_original_jets":5,
        "working_ring":"Z/125Z",
        "inversion_parity_respected":True,
        "exact_GL_363_and_GL_362_mod125_primitive_pairing_isometries":True,
        "checks":validated,
        "fixed_original_support_identity_Gram_delta_Z_row":4272,
        "original_observation_source_transport_verified":False,
        "integer_GL_725_Z_gauge_verified":False,
        "number_field_class_one_theorem":False,
    },flush=True)
    print("PASS Phase293-C constructive graded primitive pairing isometries mod 125",flush=True)

if __name__=="__main__":
    main()
