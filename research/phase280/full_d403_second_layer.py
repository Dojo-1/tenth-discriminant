#!/usr/bin/env python3
"""Phase280: frozen full D403 ordinary-jet second Smith layer, K=2.

Read PRE_REGISTERED_D403_FULL_P2_PANEL.md before changing this. Finite
sample, no general bound. Integers only, full original row/jet/ellipse,
unmodified signed trace metric. The actual class-number-one premise is
NOT satisfied at D403; p11 split is a deliberate negative control.
"""
from collections import Counter
from math import comb
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"phase206"))
sys.path.insert(0,str(ROOT/"phase207"))
sys.path.insert(0,str(ROOT/"phase204"))
from source_probe import params, fall, mul, rank_mod
from middle_frobenius import old_k, pair_powers, source_dualjet
from ordinary_jet_filtration import jet as integer_jet

D,R,S,J,QSIZE,N,M,K=403,100,4,4,219,400,1752,2
OLD={3:570,5:550,11:0}
SUBSET={3:{"0":54,"1":18,">=2":116},
        5:{"0":120,"1":15,">=2":45}}

def field_type(p):
    squares={j*j%p for j in range(p)}
    val=(-D)%p
    assert val!=0
    return "split" if val in squares else "inert"

def source_matrix(p,points):
    typ=field_type(p)
    inert=typ=="inert"
    assert (p in (3,5))==inert
    q=p**5 if inert else p**2
    red=p**K
    cache=[]
    for x,y in points:
        z=(x%q,y%q)
        w=(x%q,(-y)%q)
        cache.append((pair_powers(z,R,q),pair_powers(w,S-1,q)))
    C=np.zeros((N,M),dtype=np.int64)
    census=0
    for r in range(R):
        for s in range(S):
            i=r*S+s
            k=old_k(r,s,p) if inert else 0
            census+=k
            divide=p**k
            for j in range(J):
                for qi,(zp,wp) in enumerate(cache):
                    re=im=0
                    for t in range(k+1):
                        a=r-p*t
                        if a<j:continue
                        v=mul(zp[a-j],wp[s+t],D,q)
                        scalar=(-1 if t&1 else 1)*comb(k,t)*fall(a,j)
                        re=(re+scalar*v[0])%q
                        im=(im+scalar*v[1])%q
                    assert re%divide==0 and im%divide==0,(p,r,s,j,qi)
                    col=2*(j*len(points)+qi)
                    C[i,col]=re//divide%red
                    C[i,col+1]=im//divide%red
    assert census==OLD[p],(p,census,OLD[p])
    return C,cache

def vec_rank(MAT,p):
    A=np.array(MAT,dtype=np.int64,copy=True)%p
    n,m=A.shape
    t=0
    for j in range(m):
        if t==n:break
        opts=np.flatnonzero(A[t:,j])
        if not len(opts):continue
        i=t+int(opts[0])
        if i!=t:A[[t,i]]=A[[i,t]]
        A[t,j:]=A[t,j:]*pow(int(A[t,j]),-1,p)%p
        js=np.flatnonzero(A[t+1:,j])+t+1
        if len(js):
            A[js,j:]=(A[js,j:]-A[js,j,None]*A[t,j:])%p
        t+=1
    return t

def first_two_smith(MAT,p):
    """Full rectangular p² unit elimination, then p-divided tail rank.

    Row and column swaps are internal Smith operations, not a change
    to the original signed trace metric.
    """
    mod=p*p
    A=np.array(MAT,dtype=np.int64,copy=True)%mod
    n,m=A.shape
    t=0
    while t<n:
        # Search for the first p-unit in the *entire* trailing block.
        loc=None
        for j in range(t,m):
            ix=np.flatnonzero(A[t:,j]%p)
            if len(ix):
                loc=(t+int(ix[0]),j)
                break
        if loc is None:break
        i,j=loc
        if i!=t:A[[t,i]]=A[[i,t]]
        if j!=t:A[:,[t,j]]=A[:,[j,t]]
        a=int(A[t,t])
        assert a%p!=0
        inv=pow(a,-1,mod)
        if t+1<n:
            factors=A[t+1:,t]*inv%mod
            A[t+1:,t+1:]=(A[t+1:,t+1:]-factors[:,None]*A[t,t+1:])%mod
            A[t+1:,t]=0
        t+=1
    assert np.all(A[t:,t:]%p==0)
    tail=A[t:,t:]//p
    t1=vec_rank(tail,p) if len(tail) else 0
    assert t+t1<=n
    return {"0":t,"1":t1,">=2":n-t-t1}

def negative_toy(p):
    toy=np.diag([1,p,p*p]).astype(np.int64)
    expected={"0":1,"1":1,">=2":1}
    assert first_two_smith(toy,p)==expected
    toy[0]+=toy[1]
    toy[:,1]+=toy[:,0]
    assert first_two_smith(toy,p)==expected

def oracle_check(C,p,Q):
    """Independent exact integer jet and truncated dual-number oracles."""
    typ=field_type(p)
    labels=[(0,0),(1,3),(p,0),(2*p,0),(50,1),(99,0),(99,3)]
    if p in (3,5):labels.extend([(p*3,0),(p*2,1)])
    labels=sorted(set(z for z in labels if z[0]<R))
    q=p**5 if typ=="inert" else p*p
    for r,s in labels:
        k=old_k(r,s,p) if typ=="inert" else 0
        for j in range(J):
            for qi in (0,len(Q)//2,len(Q)-1):
                x,y=Q[qi]
                # Full exact integer oracle, independent of modular powers.
                a=b=0
                for t in range(k+1):
                    rr=r-p*t
                    if rr<j:continue
                    v=integer_jet(D,rr,s+t,j,(x,y))
                    z=(-1 if t%2 else 1)*comb(k,t)
                    a+=z*v[0]
                    b+=z*v[1]
                div=p**k
                assert a%div==b%div==0
                c=2*(j*len(Q)+qi)
                assert tuple(C[r*S+s,c:c+2])==((a//div)%(p*p),(b//div)%(p*p)),(p,r,s,j,qi)
                if k:
                    z=(x%q,y%q);w=(x%q,(-y)%q)
                    extra=source_dualjet(z,w,r,s,k,p,q)
                    assert tuple(int(v)%q for v in extra[j])==(a%q,b%q)
    return len(labels)

def main():
    rho,R0,S0,J0,Q=params(D)
    assert (rho,R0,S0,J0,len(Q))==(40,R,S,J,QSIZE)
    assert len(Q)*2*J==M
    assert (-D)%3==2 and (-D)%5==2 and (-D)%11==4
    all_rows=[(r,s) for r in range(R) for s in range(S)]
    assert len(all_rows)==N
    for p in (3,5,11):
        negative_toy(p)
        C,cache=source_matrix(p,Q)
        assert C.shape==(N,M)
        nc=oracle_check(C,p,Q)
        # Full rank replay by independent, scalar row-basis algorithm.
        r0=vec_rank(C%p,p)
        assert r0==rank_mod(C.tolist(),p)
        prof=first_two_smith(C,p)
        assert prof["0"]==r0
        if p in SUBSET:
            selected=[r*S+s for r,s in all_rows if old_k(r,s,p)>=2]
            restricted=first_two_smith(C[selected],p)
            assert restricted==SUBSET[p],(p,restricted,SUBSET[p])
        else:
            restricted=None
        # Entire original trace metric 2, 2D; no flattening.
        w=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
        W=w%p
        A=C%p
        G=((A*W)@A.T)%p
        assert np.array_equal(G,G.T)
        grank=vec_rank(G,p)
        assert grank==rank_mod(G.tolist(),p)
        assert grank<=r0
        assert (2*D)%p!=0
        if p==11:assert (2*D)%p!=2%p
        # Removing the highest derivative is an explicitly WRONG-source
        # comparator, not a valid replacement.
        drop_rank=vec_rank(A[:,:2*(J-1)*len(Q)],p)
        assert drop_rank<=r0
        # Metamorphic unimodular row shear and paired-column reversal.
        T=C.copy()
        T[0]=(T[0]+T[-1])%(p*p)
        assert first_two_smith(T,p)==prof
        assert first_two_smith(C[:,::-1],p)==prof
        budget=prof["1"]+2*prof[">=2"]
        print("FULL_D403_SECOND_LAYER",{
            "D":D,"p":p,"type":field_type(p),"rows":N,"columns":M,
            "old_F_once":OLD[p],
            "full_histogram_capped2":prof,
            "evaluation_index_lower":budget,
            "original_Gram_vp_lower":2*(OLD[p]+budget),
            "rank_C_modp":r0,"rank_Gram_modp":grank,
            "unsaturated_image_radical":r0-grank,
            "rank_without_j3_wrong_source":drop_rank,
            "subset_previous_histogram":restricted,
            "source_oracle_rows":nc,
            "primitive_H_not_constructed":True
        },flush=True)
    print("PASS Phase280 original D403 full p2 matched inert/split panel",flush=True)

if __name__=="__main__":main()
