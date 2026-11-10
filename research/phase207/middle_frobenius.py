#!/usr/bin/env python3
"""Phase207-B (#147): old Frobenius row basis at k>=2 and k>=3.

All ordinary Z jets j=0..3 with W FIXED in differentiation,
all points of original D403 ellipse, BOTH integer-pair channels.
Only p^(k+1) precision; source row subset ranks give LOWER bounds on
uncounted evaluation index, not the full Smith invariant vector.
"""
from math import comb, factorial
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "phase206"))

from source_probe import params, mul, fall, rank_mod

D=403
R=100
S=J=4
def old_k(r,s,p):return min(r//p,S-1-s)

def pair_powers(z,n,mod):
    v=[(1,0)]
    for i in range(n):
        v.append(mul(v[-1],z,D,mod))
    return v

def normalized_row(r,s,p,Q,cache):
    k=old_k(r,s,p)
    mod=p**4
    line=[]
    for zpow,wpow in cache:
        for j in range(J):
            re=im=0
            for t in range(k+1):
                a=r-p*t
                if a<j:continue
                x,y=mul(zpow[a-j],wpow[s+t],D,mod)
                coeff=(-1 if t%2 else 1)*comb(k,t)*fall(a,j)
                re=(re+coeff*x)%mod;im=(im+coeff*y)%mod
            assert re%(p**k)==0 and im%(p**k)==0, (p,r,s,j)
            line.extend((re//(p**k)%p,im//(p**k)%p))
    # our internal loop orders z then j; original source convention is j then z.
    # Unshuffle to the original column order before rank/oracle comparison.
    n=len(cache)
    return [line[2*(qi*J+j)+component]
            for j in range(J) for qi in range(n) for component in (0,1)]

def source_dualjet(z,w,r,s,k,p,mod):
    """Independent exact polynomial f(z+h,w), h^4=0; multiply j! after."""
    zero=(0,0);one=(1,0)
    def ppow(x,n):
        a=one
        for _ in range(n):a=mul(a,x,D,mod)
        return a
    def P(n):
        return [tuple((comb(n,j)*c)%mod for c in ppow(z,n-j))
                if j<=n else zero for j in range(J)]
    def add(A,B):
        return [((a[0]+b[0])%mod,(a[1]+b[1])%mod) for a,b in zip(A,B)]
    def neg(A):
        return [((-a[0])%mod,(-a[1])%mod) for a in A]
    def prod(A,B):
        out=[zero]*J
        for i in range(J):
            for j in range(J-i):
                a,b=mul(A[i],B[j],D,mod)
                out[i+j]=((out[i+j][0]+a)%mod,(out[i+j][1]+b)%mod)
        return out
    W=[ppow(w,s)]+[zero]*(J-1)
    zp=P(r-p*k)
    zp_minus_w=add(P(p),neg([w]+[zero]*(J-1)))
    H=[one]+[zero]*(J-1)
    for _ in range(k):H=prod(H,zp_minus_w)
    coeff=prod(prod(zp,W),H)
    return [(factorial(j)*v[0]%mod,factorial(j)*v[1]%mod)
            for j,v in enumerate(coeff)]

def direct_combined_jets(z,w,r,s,k,p,mod):
    zpow=pair_powers(z,R,mod)
    wpow=pair_powers(w,S-1,mod)
    out=[]
    for j in range(J):
        x=y=0
        for t in range(k+1):
            a=r-p*t
            if a<j:continue
            v=mul(zpow[a-j],wpow[s+t],D,mod)
            tcoeff=(-1 if t%2 else 1)*comb(k,t)*fall(a,j)
            x=(x+tcoeff*v[0])%mod;y=(y+tcoeff*v[1])%mod
        out.append((x,y))
    return out

def rank_cols(M,p):
    """Independent column-pivot Gauss check for the smaller high stratum."""
    A=[[x%p for x in row] for row in M]
    n=len(A);m=len(A[0]);q=0
    for j in range(m):
        pivot=next((i for i in range(q,n) if A[i][j]),None)
        if pivot is None:continue
        A[pivot],A[q]=A[q],A[pivot]
        inv=pow(A[q][j],-1,p)
        for i in range(q+1,n):
            if A[i][j]:
                t=A[i][j]*inv%p
                A[i][j]=0
                for h in range(j+1,m):A[i][h]=(A[i][h]-t*A[q][h])%p
        q+=1
        if q==n:break
    return q

def run(p):
    rho,R0,S0,J0,Q=params(D)
    assert (rho,R0,S0,J0,len(Q))==(40,R,S,J,219)
    assert (-D)%p not in {x*x%p for x in range(p)}
    mod=p**4
    # Original points and coordinate order preserved; no point-selection.
    cache=[]
    for x,y in Q:
        z=(x%mod,y%mod);w=(x%mod,(-y)%mod)
        cache.append((pair_powers(z,R,mod),pair_powers(w,S-1,mod)))
    rows=[(r,s,old_k(r,s,p)) for r in range(R) for s in range(S)]
    F=sum(k for r,s,k in rows)
    selected=[(r,s,k) for r,s,k in rows if k>=2]
    high=[v for v in selected if v[2]>=3]
    assert selected and high and set(high).issubset(set(selected))
    M=[normalized_row(r,s,p,Q,cache) for r,s,k in selected]
    MH=[row for row,(_,_,k) in zip(M,selected) if k>=3]
    r2=rank_mod(M,p);r3=rank_mod(MH,p)
    assert r3==rank_cols(MH,p) # separate elimination order
    # Post-result preregistered (Issue #147) rank reproduction of the
    # larger k>=2 row family: distinct elimination and point permutation.
    assert r2==rank_cols(M,p)
    col_order=[2*(j*len(Q)+qi)+component
               for j in range(J) for qi in range(len(Q)-1,-1,-1)
               for component in (0,1)]
    MP=[[row[t] for t in col_order] for row in M]
    assert r2==rank_mod(MP,p)
    n2=len(selected);n3=len(high)
    d2=n2-r2;d3=n3-r3
    assert 0<=d3<=d2
    # Deterministic first, middle and last from each selected stratum.
    samples=[]
    for sample in (selected,high):
        for t in (sample[0],sample[len(sample)//2],sample[-1]):
            if t not in samples:samples.append(t)
    for r,s,k in samples:
        for x,y in Q:
            z=(x%mod,y%mod);w=(x%mod,(-y)%mod)
            a=source_dualjet(z,w,r,s,k,p,mod)
            b=direct_combined_jets(z,w,r,s,k,p,mod)
            assert a==b, ("independent jet disagreement",p,r,s,x,y)
            assert all(v[0]%p**k==v[1]%p**k==0 for v in a)
    # Negative source: j=0 cannot substitute all j for ordinary Z jets.
    assert fall(3,1)==3 and fall(3,3)==6
    # Previously preregistered split witness: D287, p3 at z=1+u.
    z=(1,1);z3=mul(mul(z,z,287,3),z,287,3)
    assert ((z3[0]-1)%3,(z3[1]+1)%3)==(0,2)
    print("PHASE207_MIDDLE_FROBENIUS",{"D":D,"p":p,"rho":rho,"R":R,
       "S":S,"J":J,"Q":len(Q),"channels":2*len(Q)*J,
       "old_F":F,"old_2F":2*F,
       "rows_k2plus":n2,"rank_k2plus":r2,"nullity_k2plus":d2,
       "rows_k3plus":n3,"rank_k3plus":r3,"nullity_k3plus":d3,
       "new_E_index_at_least":d2,
       "additional_Gram_exponent_at_least":2*d2,
       "total_p_Gram_valuation_at_least":2*F+2*d2,
       "dualjet_oracle_samples":len(samples),"independent_k2_rank_replay":True,
       "point_column_permutation_invariance":True,"all_j_kept":True,
       "strata_are_nested_no_double_count":True},flush=True)

if __name__=="__main__":
    for p in (3,5):run(p)
    print("PASS Phase207 original-source middle-high modular Frobenius probe",flush=True)
