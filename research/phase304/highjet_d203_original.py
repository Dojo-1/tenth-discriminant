#!/usr/bin/env python3
"""Phase304-B: original-policy D203 J=S2 ordinary-jet Frobenius trace.

Preregistered 6bc1cfa4 BEFORE this code. D203 is PROVABLY non-h1
(split prime 3). Original R50/S=J2 and norm cutoff from source_probe.
45 source-row Frobenius (Z^5-W) monomial differences, all j=0,1.
No Hasse-jet change, no additional field-discriminant contribution.
"""
from collections import Counter
from math import isqrt
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase204","phase297","phase304"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from source_probe import params,gram as legacy_bigint_gram
from ordinary_jet_filtration import jet as legacy_jet
from original_schur_integrality_k16 import high_precision_smith

D=203
M=(D+1)//4
P=5
K=16
MOD=5**K
LOW=5**(K-1)
FROZEN={
  "research/phase206/source_probe.py":
    "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
  "research/phase204/ordinary_jet_filtration.py":
    "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
  "research/phase297/original_schur_integrality_k16.py":
    "aa3678001c69a7235dca638638d2dab4c55b05b3"
}

def guard():
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
        assert sha==actual,("frozen helper drift",path,sha,actual)

def mul(x,y,mod=None):
    a,b=x;c,d=y
    u=a*c-M*b*d
    v=a*d+b*c+b*d
    return (u,v)if mod is None else (u%mod,v%mod)

def conjugate(z):
    a,b=z
    return (a+b,-b)

def qmax(rho):
    m=4*rho*rho
    qb=isqrt(m//D)
    Q=[]
    for q in range(-qb,qb+1):
        pr=isqrt(m-D*q*q)
        for p in range(-pr,pr+1):
            if (p-q)%2==0:
                Q.append(((p-q)//2,q))
    assert len(Q)==len(set(Q))
    assert all(a*a+a*b+M*b*b<=rho*rho for a,b in Q)
    return Q

def mod_powers(z,R,mod):
    p=[(1,0)]
    for k in range(1,R):
        p.append(mul(p[-1],z,mod))
    return p

def original_rows(R,S):
    return [(r,s)for r in range(R)for s in range(S)]

def evaluate_original_jets(Q,R,S,J,mod):
    assert J==S==2
    n=R*S
    q=len(Q)
    E=np.zeros((n,2*J*q),dtype=np.int64)
    for qi,z in enumerate(Q):
        zpow=mod_powers(z,R,mod)
        w=conjugate(z)
        for r in range(R):
            for s in range(S):
                idx=2*r+s
                wp=(1,0) if s==0 else w
                for j in range(J):
                    col=2*(j*q+qi)
                    if r<j:continue
                    p=mul(zpow[r-j],wp,mod)
                    f=1 if j==0 else r
                    E[idx,col]=(p[0]*f)%mod
                    E[idx,col+1]=(p[1]*f)%mod
    return E

def original_trace_gram(E,Q,J,mod):
    # ω maximal-order hermitian trace Gram: [[2,1],[1,2*M]]
    assert len(E[0])==2*J*Q
    x=np.asarray(E[:,0::2],dtype=object)
    y=np.asarray(E[:,1::2],dtype=object)
    xx=2*x+y
    yy=x+(2*M)*y
    return np.asarray((xx@x.T+yy@y.T)%mod,dtype=np.int64)

def rank_F5(M):
    A=[[int(y)%5 for y in row] for row in M]
    if not A:return 0
    r=0
    for c in range(len(A[0])):
        k=next((i for i in range(r,len(A)) if A[i][c]),None)
        if k is None:continue
        A[k],A[r]=A[r],A[k]
        v=pow(A[r][c],-1,5)
        A[r][c:]=[v*x%5 for x in A[r][c:]]
        for i in range(r+1,len(A)):
            q=A[i][c]
            if q:
                for j in range(c,len(A[i])):
                    A[i][j]=(A[i][j]-q*A[r][j])%5
        r+=1
        if r==len(A):break
    return r

def frozen_source_even_jet_match(rho,R,S,J,Qold,even,Eeven):
    assert Qold and even==[(x-y,2*y) for x,y in Qold]
    checks=0
    for i,(r,s) in enumerate(original_rows(R,S)):
        for qi,q in enumerate(Qold):
            for j in range(J):
                old=legacy_jet(D,r,s,j,q)
                z=(old[0]-old[1],2*old[1])
                col=2*(j*len(Qold)+qi)
                assert int(Eeven[i,col])==z[0]%MOD
                assert int(Eeven[i,col+1])==z[1]%MOD
                checks+=2
    return checks

def independent_bigint_subset(Qold,Qfull,oldG,fullG,R,S,J):
    # Original source_probe.gram independently compares its DIRECT
    # integer original source evaluation with a distinct mixed-moment
    # formula for the following fixed 10x10 submatrix.
    choices=[0,1,2,3,10,11,50,51,98,99]
    assert max(choices)<R*S
    labels=original_rows(R,S)
    sampled=[labels[i] for i in choices]
    rho,Rp,Sp,Jp,points=params(D)
    assert points==Qold and (Rp,Sp,Jp)==(R,S,J)
    H=legacy_bigint_gram(D,Qold,J,sampled)
    for k,i in enumerate(choices):
        for l,j in enumerate(choices):
            assert int(oldG[i,j])==int(H[k][l])%MOD
    # Separate exact original ω-coordinate raw source oracle:
    # regenerate each selected row at each genuine maximal-order Q point
    # with NO modular arithmetic, then apply exact trace bilinear form.
    exact=[]
    for r,s in sampled:
        row=[]
        for j in range(J):
            for z in Qfull:
                if r<j:
                    row.append((0,0));continue
                p=(1,0)
                for _ in range(r-j):p=mul(p,z)
                if s:p=mul(p,conjugate(z))
                if j==1:p=(r*p[0],r*p[1])
                row.append(p)
        exact.append(row)
    for i,lab in enumerate(sampled):
        for k,other in enumerate(sampled):
            total=0
            for a,b in zip(exact[i],exact[k]):
                total+=2*a[0]*b[0]+a[0]*b[1]+a[1]*b[0]+2*M*a[1]*b[1]
            assert total%MOD==int(fullG[choices[i],choices[k]])
    return {"original_integer_order_bigint_mixed_moment_cells":100,
            "full_maximal_order_independent_bigint_trace_cells":100}

def frobenius_difference(E,R,S,J,Q,G,name):
    n=R*S
    assert E.shape==(n,2*J*Q)
    U=np.eye(n,dtype=object)
    selected=[]
    for r in range(5,R):
        idx=2*r # s0
        mate=2*(r-5)+1 # s1
        U[idx,mate]-=1
        selected.append(idx)
    assert len(selected)==45
    Eo=np.asarray(E,dtype=object)
    U_E=(U@Eo)%MOD
    # Every j ordinary jet of (Z5-W)Z^(r-5) at inert p5 is 0 mod5.
    assert not np.any(U_E[selected,:]%5),(
        "ordinary-jet Frobenius divisible source relation failed",name)
    # Distinguish U (unimodular original lattice) from division by5
    # into a separate evaluation SUPERLATTICE.
    Eprim=np.asarray(U_E,dtype=object)
    for idx in selected:
        Eprim[idx,:]=(Eprim[idx,:]//5)%LOW
    Gprim=original_trace_gram(
        np.asarray(Eprim,dtype=np.int64),Q,J,LOW)
    original=np.asarray(G,dtype=object)
    updated=(U@original@U.T)%MOD
    selected_set=set(selected)
    for i in range(n):
        for k in range(n):
            if i not in selected_set and k not in selected_set:
                expected=int(G[i,k])%MOD
            else:
                p=(5 if i in selected_set else 1)*(
                    5 if k in selected_set else 1)
                expected=p*int(Gprim[i,k])%MOD
            assert int(updated[i,k])==expected,(
               "original-trace-Gram Frobenius index-square equation failed",
               name,i,k,int(updated[i,k]),expected)
    levels,hist=high_precision_smith(np.asarray(G,dtype=np.int64))
    grade_censored=max(levels)>=K
    exact=None if grade_censored else sum(levels)
    if exact is not None:assert exact>=90
    primitive_rank=rank_F5(Gprim)
    if primitive_rank==n and exact is not None:
        assert exact==90
    return {
       "arm":name,
       "original_rows":n,
       "ordinary_Z_jets":J,
       "source_original_Q":Q,
       "Frobenius_source_rows":len(selected),
       "all_45_original_row_and_two_jet_raw_coordinate_divisibility_tests":
           len(selected)*J*Q*2,
       "all_10000_original_Gram_factorization_cells_checked":n*n,
       "original_G_Gram_mod5_rank":rank_F5(G),
       "source_original_E_mod5_rank":rank_F5(E),
       "primitive_E_mod5_rank":rank_F5(Eprim),
       "primitive_G_mod5_rank":primitive_rank,
       "p16_Smith_full_censored":grade_censored,
       "p16_Smith_histogram":hist,
       "exact_original_det_v5_if_uncensored":exact,
       "unconditional_Frobenius_saturation_lower_bound":90,
       "no_new_original_number_field_arithmetic_mass":True
    }

def main():
    guard()
    assert D==7*29 and D%4==3 and (-D)%5==2
    assert (-D)%3==1 and 3<(D+1)//4
    rho,R,S,J,Qold=params(D)
    assert (R,S,J)==(50,2,2)
    assert len(Qold)==len(set(Qold))
    Qmax=qmax(rho)
    even=[z for z in Qmax if z[1]%2==0]
    expected=[(x-y,2*y) for x,y in Qold]
    assert even==expected,("actual original source order arm mismatch",
                           len(even),len(expected))
    Eeven=evaluate_original_jets(even,R,S,J,MOD)
    Emax=evaluate_original_jets(Qmax,R,S,J,MOD)
    cross=frozen_source_even_jet_match(
       rho,R,S,J,Qold,even,Eeven)
    oldG=original_trace_gram(Eeven,len(even),J,MOD)
    fullG=original_trace_gram(Emax,len(Qmax),J,MOD)
    big=independent_bigint_subset(
       Qold,Qmax,oldG,fullG,R,S,J)
    # Stagewise source Frobenius control, no adaptation of J or jet type.
    old=frobenius_difference(
       Eeven,R,S,J,len(even),oldG,"original_integer_order_even")
    full=frobenius_difference(
       Emax,R,S,J,len(Qmax),fullG,"genuine_maximal_order_full")
    print("PHASE304B_ORIGINAL_SOURCE_J2_FROBENIUS",{
       "field_D":D,
       "h1_is_false_by_split_prime3":True,
       "source_original_rho":rho,
       "source_original_R":R,
       "source_original_S_and_J":S,
       "actual_old_Q":len(Qold),
       "actual_maximal_full_Q":len(Qmax),
       "new_odd_Q":len(Qmax)-len(even),
       "original_legacy_to_max_even_raw_coordinate_checks":cross,
       "independent_integer_oracles":big,
       "actual_original_old_source":old,
       "actual_maximal_full_source":full,
       "universal_Frobenius_ordinary_jet_divisibility_algebra":True,
       "this_is_NOT_an_actual_h1_J2_field":True,
       "no_new_tenth_discriminant_bound":True
    },flush=True)
    print("PASS Phase304-B genuine original-policy J2 Frobenius ordinary jets",flush=True)

if __name__=="__main__":
    main()
