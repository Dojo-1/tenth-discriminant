#!/usr/bin/env python3
"""Phase208-B — p²-truncated Smith of preregistered k>=2 old-source rows.

Issue #151 froze D403 rho40 R100,S=J4,Q219,p3/p5 BEFORE this code.
All original ordinary j and integer-pair channels. Coefficients at
depth >=2 remain >=2; NO assertion of an exact full Smith spectrum.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase206"))
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase207"))

from collections import Counter
from math import comb
from source_probe import params, mul, fall, rank_mod
from middle_frobenius import old_k, pair_powers, rank_cols, source_dualjet

D,R,S,J=403,100,4,4

def original_jet_row_mod_p2(r,s,p,k,cache):
    # max k=3, so p^5 contains at least k+2 p-adic digits.
    q=p**5;denom=p**k;n=len(cache)
    assert k==old_k(r,s,p) and k>=2
    values=[]
    for j in range(J):
        for zpow,wpow in cache:
            re=im=0
            for t in range(k+1):
                a=r-p*t
                if a<j:continue
                x,y=mul(zpow[a-j],wpow[s+t],D,q)
                factor=(-1 if t%2 else 1)*comb(k,t)*fall(a,j)
                re=(re+factor*x)%q;im=(im+factor*y)%q
            assert re%denom==im%denom==0, ("Frobenius divisibility",p,r,s,j)
            values.extend((re//denom%(p*p),im//denom%(p*p)))
    assert len(values)==2*J*n
    return values

def p2_smith_levels(source,p):
    """Unit Gaussian over Z/p², then mod-p rank of divided trailing block."""
    q=p*p
    A=[[x%q for x in row] for row in source]
    n=len(A);m=len(A[0]);k=0
    while k<n:
        hit=None
        for i in range(k,n):
            j=next((j for j in range(k,m) if A[i][j]%p),None)
            if j is not None:
                hit=i,j;break
        if hit is None:break
        i,j=hit
        A[i],A[k]=A[k],A[i]
        if j!=k:
            for row in A:row[k],row[j]=row[j],row[k]
        inv=pow(A[k][k],-1,q)
        prow=A[k]
        for i in range(k+1,n):
            z=A[i][k]
            if z:
                t=z*inv%q
                rr=A[i]
                for j in range(k+1,m):
                    rr[j]=(rr[j]-t*prow[j])%q
                rr[k]=0
        k+=1
    # Unit-pivot block may be cleared on the right using unimodular
    # COLUMN operations; the trailing divisible-p block is unchanged.
    r0=k
    assert all(A[i][j]%p==0 for i in range(k,n) for j in range(k,m))
    trailing=[[A[i][j]//p%p for j in range(k,m)] for i in range(k,n)]
    r1=rank_cols(trailing,p) if trailing else 0
    r2=n-r0-r1
    assert r0+r1+r2==n and r2>=0
    return {"0":r0,"1":r1,">=2":r2}

def toy(p):
    rows=[[1,0,0],[0,p,0],[0,0,p*p]]
    expected={"0":1,"1":1,">=2":1}
    assert p2_smith_levels(rows,p)==expected
    B=[row[:] for row in rows]
    B[0]=[a+b for a,b in zip(B[0],B[1])]
    for row in B:row[1]+=row[0]
    assert p2_smith_levels(B,p)==expected

def independent_dual_oracle(p,original,points):
    q=p**5
    chosen=[]
    for v in (original,
              [w for w in original if w[2]>=3]):
        for t in (v[0],v[len(v)//2],v[-1]):
            if t not in chosen:chosen.append(t)
    for r,s,k in chosen:
        for x,y in points:
            z=(x%q,y%q);w=(x%q,(-y)%q)
            independent=source_dualjet(z,w,r,s,k,p,q)
            a=original_jet_row_mod_p2(r,s,p,k,
                  [(pair_powers(z,R,q),pair_powers(w,S-1,q))])
            expected=[v//p**k%(p*p) for vpair in independent
                      for v in vpair]
            assert a==expected,("independent ordinary-jet mismatch",p,r,s,x,y)
    return len(chosen)

def run(p):
    rho,R0,S0,J0,Q=params(D)
    assert (rho,R0,S0,J0,len(Q))==(40,R,S,J,219)
    assert (-D)%p not in {a*a%p for a in range(p)}
    rows=[(r,s,old_k(r,s,p)) for r in range(R) for s in range(S)]
    F=sum(k for r,s,k in rows)
    selected=[z for z in rows if z[2]>=2]
    q=p**5
    cache=[]
    for x,y in Q:
        z=(x%q,y%q);w=(x%q,(-y)%q)
        cache.append((pair_powers(z,R,q),pair_powers(w,S-1,q)))
    src=[original_jet_row_mod_p2(r,s,p,k,cache) for r,s,k in selected]
    first=rank_mod(src,p)
    second=rank_cols(src,p)
    assert first==second==(54 if p==3 else 120)
    levels=p2_smith_levels(src,p)
    assert levels["0"]==first
    lower=levels["1"]+2*levels[">=2"]
    first_only=len(selected)-first
    assert lower>=first_only
    oracles=independent_dual_oracle(p,selected,Q)
    toy(p)
    print("PHASE208_PADIC_SECOND_DEPTH",{
       "D":D,"p":p,"rho":rho,"R":R,"S":S,"J":J,
       "Q":len(Q),"source_columns":len(src[0]),
       "old_Fp":F,"old_exponent_2Fp":2*F,
       "subset_rows_k2":len(src),"levels_truncated_p2":levels,
       "first_defect":first_only,
       "extra_subset_index_lower":lower,
       "beyond_first_defect":lower-first_only,
       "extra_Gram_exponent_lower":2*lower,
       "total_Gram_vp_lower":2*(F+lower),
       "oracle_rows_all_points":oracles,
       "levels_ge2_are_NOT_exact":True},flush=True)

if __name__=="__main__":
    run(3);run(5)
    print("PASS Phase208 p^2-truncated original-source middle Frobenius Smith")
