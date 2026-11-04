#!/usr/bin/env python3
"""Phase208-A — predeclared explicit sparse row-map test (issue #150).

All original ordinary-Z jets j<J and all ellipse points are retained.
The sparse map is constructed BEFORE optimal Schur evaluation from one
source predecessor per target row. It is coordinate dependent by design.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase206"))
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase207"))

from fractions import Fraction as F
from source_probe import params, fibers, gram, inv, mm, tr
from full_schur_spectrum import inertia

def transpose(A):
    return [list(x) for x in zip(*A)]

def sub(A,B):
    assert len(A)==len(B)
    return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]

def add(A,B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]

def pencil_residual(S,B,t):
    return [[S[i][j]-t*B[i][j] for j in range(len(B))]
            for i in range(len(B))]

def evaluate_pair(D,Q,J,I,K,thetas):
    a,b=len(I),len(K)
    G=gram(D,Q,J,I+K)
    A=[[F(v) for v in row[:a]] for row in G[:a]]
    B=[[F(v) for v in row[a:]] for row in G[a:]]
    C=[[F(v) for v in row[a:]] for row in G[:a]]
    AinvC=mm(inv(A),C)
    L=[[F(0) for _ in range(b)] for _ in range(a)]
    lookup={key:i for i,key in enumerate(I)}
    represented=0
    for j,(r,s) in enumerate(K):
        i=lookup.get((r-2,s))
        if i is None:continue
        L[i][j]=C[i][j]/A[i][i]
        represented+=1
    Sopt=sub(B,mm(transpose(C),AinvC))
    Strial=add(sub(sub(B,mm(transpose(C),L)),mm(transpose(L),C)),
               mm(mm(transpose(L),A),L))
    delta=sub(L,AinvC)
    PSD=mm(mm(transpose(delta),A),delta)
    assert sub(Strial,Sopt)==PSD
    assert inertia(PSD)[0]==0
    assert inertia(Sopt)==(0,0,b)
    assert inertia(Strial)==(0,0,b)
    counts={}
    for name,theta in thetas:
        nopt,zopt,_=inertia(pencil_residual(Sopt,B,theta))
        ntrial,ztrial,_=inertia(pencil_residual(Strial,B,theta))
        assert zopt==ztrial==0,("threshold degeneracy",D,I,K,name)
        assert ntrial<=nopt,("wrong minmax direction",D,I,K,name)
        counts[name]=(ntrial,nopt)
    return represented,counts

def fixed_matching(R,S):
    ds=list(range(1-S,R))
    return [(a[i],a[i+1]) for a in
            ([d for d in ds if d%2==0],[d for d in ds if d%2==1])
            for i in range(0,len(a)-1,2)]

def run(D):
    rho,R,S,J,Q=params(D)
    match=fixed_matching(R,S)
    assert len(match)==(35 if D==283 else 51)
    theta=[("1/2",F(1,2)),("1/8",F(1,8)),
           ("1/1024",F(1,1024)),
           ("2^-ceil(R/10)",F(1,2**((R+9)//10)))]
    counts={name:{"trial":0,"optimal":0} for name,_ in theta}
    matched=target_modes=0
    for d,e in match:
        I=fibers(R,S,d);K=fibers(R,S,e)
        n,results=evaluate_pair(D,Q,J,I,K,theta)
        matched+=n;target_modes+=len(K)
        for name,(nt,no) in results.items():
            counts[name]["trial"]+=nt
            counts[name]["optimal"]+=no
    if D==283:
        assert all(z["optimal"]==0 for z in counts.values())
    if D==403:
        assert counts["1/2"]["optimal"]==65
        assert counts["1/8"]["optimal"]==33
        assert counts["1/1024"]["optimal"]==12
    print("PHASE208_SPARSE_MAP",{
        "D":D,"R":R,"S":S,"J":J,"rho":rho,"Q":len(Q),
        "pair_count":len(match),"target_modes":target_modes,
        "rows_with_predecessor":matched,
        "exact_threshold_counts":counts,
        "all_original_jets":True,
        "sparse_map_is_row_frame_dependent":True},flush=True)

def toy():
    A=[[F(1)]];B=[[F(1)]];C=[[F(3,4)]]
    L=[[F(0)]]
    Sopt=sub(B,mm(tr(C),mm(inv(A),C)))
    Strial=add(sub(sub(B,mm(tr(C),L)),mm(tr(L),C)),mm(mm(tr(L),A),L))
    assert Sopt==[[F(7,16)]] and Strial==[[F(1)]]
    assert inertia(pencil_residual(Sopt,B,F(1,2)))[0]==1
    assert inertia(pencil_residual(Strial,B,F(1,2)))[0]==0
    print("SPARSE_MAP_COUNTERWORLD",{"optimal_residual":"7/16",
        "trial_residual":"1","trial_misses_genuine_deep_mode":True})

if __name__=="__main__":
    toy()
    run(283);run(403)
    print("PASS Phase208 explicit sparse source-map and Schur residual direction")
