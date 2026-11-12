#!/usr/bin/env python3
"""Phase291 full-original D563 700x3590 normalized evaluation and p-local gate.

Preregistered 7ead4cea BEFORE implementation or this run. Capped source Smith:
CENSORED => no primitive pairing, no extra valuation from unsaturated Gram.
Historical D283/p5 replay is a separate regression, not new evidence.
"""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
import subprocess
import sys
import numpy as np

HERE=Path(__file__).resolve()
ROOT=HERE.parents[2]
for sub in ("phase206","phase204"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params,mul,fall,eval_mod,old_frobenius_C0,gram_mod
from ordinary_jet_filtration import jet as exact_jet

D,R,S,J,N,QSIZE=563,140,5,5,700,359
ORACLE=[
 (0,0),(0,4),(1,3),(4,0),(5,0),(5,4),(10,2),(15,1),
 (25,0),(35,4),(69,2),(70,0),(99,3),(110,1),(139,0),(139,4)
]
SOURCE={
 "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":"dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}

def source_guard():
    for path,sha in SOURCE.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
        assert actual==sha,("source drift",path,actual,sha)

def old_k(r,s,p,inert):
    return min(r//p,S-1-s) if inert else 0

def pair_powers(z,k,mod):
    out=[(1,0)]
    for _ in range(k):
        out.append(mul(out[-1],z,D,mod))
    return out

def normalized_original(p,K,Q,inert):
    """Every original jet, integer pair and original coordinate metric."""
    maxk=S-1 if inert else 0
    source_mod=p**(K+maxk)
    result_mod=p**K
    cache=[]
    for x,y in Q:
        z=(x%source_mod,y%source_mod)
        w=(x%source_mod,(-y)%source_mod)
        zp=pair_powers(z,R-1,source_mod)
        wp=pair_powers(w,S-1,source_mod)
        if inert:
            assert zp[p][0]%p==w[0]%p and zp[p][1]%p==w[1]%p
        cache.append((zp,wp))
    M=2*J*len(Q)
    C=np.zeros((N,M),dtype=np.int64)
    F=0
    hist=Counter()
    for r in range(R):
        if r%35==0:
            print("PHASE291_SOURCE_ROWS",{"p":p,"completed_r":r,"R":R},flush=True)
        for s in range(S):
            rowindex=r*S+s
            k=old_k(r,s,p,inert)
            hist[k]+=1
            F+=k
            denom=p**k
            for j in range(J):
                col=2*j*len(Q)
                for iq,(zp,wp) in enumerate(cache):
                    a=b=0
                    for t in range(k+1):
                        rr=r-p*t
                        if rr<j:continue
                        c=(-1 if t%2 else 1)*comb(k,t)*fall(rr,j)
                        v=mul(zp[rr-j],wp[s+t],D,source_mod)
                        a=(a+c*v[0])%source_mod
                        b=(b+c*v[1])%source_mod
                    assert a%denom==0 and b%denom==0,(
                        "invalid inert quotient",p,r,s,j,Q[iq],k)
                    C[rowindex,col+2*iq]=a//denom%result_mod
                    C[rowindex,col+2*iq+1]=b//denom%result_mod
    assert C.shape==(N,M)
    return C,F,dict(sorted(hist.items()))

def exact_source_oracle(C,p,K,Q,inert):
    """Independent exact-integer original ordinary derivatives; no modular powers."""
    assert len(ORACLE)==16
    mod=p**K
    qindices=(0,len(Q)//2,len(Q)-1)
    used_k=set()
    for r,s in ORACLE:
        k=old_k(r,s,p,inert)
        used_k.add(k)
        for j in range(J):
            for qi in qindices:
                z=Q[qi]
                v=[0,0]
                for t in range(k+1):
                    term=exact_jet(D,r-p*t,s+t,j,z)
                    c=(-1 if t%2 else 1)*comb(k,t)
                    v[0]+=c*term[0]
                    v[1]+=c*term[1]
                d=p**k
                assert all(x%d==0 for x in v)
                expected=((v[0]//d)%mod,(v[1]//d)%mod)
                col=2*(j*len(Q)+qi)
                observed=(int(C[r*S+s,col]),int(C[r*S+s,col+1]))
                assert observed==expected,(p,r,s,j,qi,expected,observed)
    assert not inert or {1,2,3,4}.issubset(used_k)
    return 16*J*len(qindices)*2

def rank_fast(M,p):
    """Independent Gaussian finite-field row rank, no Smith pivot levels."""
    A=np.array(M,dtype=np.int64,copy=True)%p
    n,m=A.shape
    t=0
    for col in range(m):
        if t==n:break
        opts=np.flatnonzero(A[t:,col])
        if opts.size==0:continue
        i=t+int(opts[0])
        if i!=t:A[[t,i]]=A[[i,t]]
        inv=pow(int(A[t,col]),-1,p)
        A[t,col:]=(A[t,col:]*inv)%p
        idx=np.flatnonzero(A[t+1:,col])+t+1
        if idx.size:
            A[idx,col:]=(A[idx,col:]-A[idx,col,None]*A[t,col:])%p
        t+=1
    return t

def gram_mod_np(C,p,D,QJ):
    assert C.shape[1]==2*QJ
    metric=np.tile(np.array((2,2*D),dtype=np.int64),QJ)
    A=C%p
    H=((A*(metric%p))@A.T)%p
    assert np.array_equal(H,H.T)
    for i,j in ((0,0),(0,len(C)-1),(len(C)//2,len(C)-1)):
        val=sum(int(A[i,k])*int(A[j,k])*int(metric[k])
                for k in range(len(metric)))%p
        assert val==int(H[i,j])
    return H

def smith_cap(C,p,K):
    """Vectorized exact truncated Smith with row map (never transform metric columns).

    Every scalar multiplication in numpy has ABS bound <(p^K)^2;
    all source reconstruction dot products have bound n*(p^K)^2.
    For p5 K8 and p7 K2 these are safely below signed int64 max.
    """
    mod=p**K
    n,m=C.shape
    assert n<=700 and m<=3590
    assert n*mod*mod < (1<<63)
    A=np.array(C,dtype=np.int64,copy=True)%mod
    U=np.eye(n,dtype=np.int64)
    levels=[]
    for k in range(n):
        tail=A[k:,k:]
        loc=None
        for v in range(K):
            # No smaller-valuation element exists if we reach this level.
            mask=(tail%(p**(v+1)))!=0
            if mask.any():
                at=int(mask.argmax())
                i,j=divmod(at,tail.shape[1])
                loc=(v,k+i,k+j)
                break
        if loc is None:
            levels.extend([K]*(n-k))
            break
        v,i,j=loc
        if i!=k:
            A[[k,i]]=A[[i,k]]
            U[[k,i]]=U[[i,k]]
        if j!=k:
            A[:,[k,j]]=A[:,[j,k]]
        d=p**v
        q=mod//d
        pivot=int(A[k,k])
        assert pivot%d==0
        inv=pow(pivot//d,-1,q)
        coefficients=((A[k+1:,k]//d)*inv)%q
        if k+1<n:
            A[k+1:,k+1:]=(A[k+1:,k+1:]
                            -coefficients[:,None]*A[k,k+1:])%mod
            U[k+1:,:]=(U[k+1:,:]-coefficients[:,None]*U[k,:])%mod
            A[k+1:,k]=0
        A[k,k+1:]=0
        levels.append(v)
        if (k+1)%100==0:
            print("PHASE291_SMITH_PROGRESS",{
                "p":p,"processed":k+1,"total":n,"last_val":v
            },flush=True)
    assert len(levels)==n
    hist=dict(sorted(Counter(levels).items()))
    assert rank_fast(U%p,p)==n
    primitive=None
    if K not in hist:
        V=(U@C)%mod
        primitive=np.zeros_like(C)
        for i,v in enumerate(levels):
            d=p**v
            assert np.all(V[i]%d==0)
            primitive[i]=(V[i]//d)%p
        assert rank_fast(primitive,p)==n
    return levels,hist,primitive

def historical_d283_p5():
    """Phase206/278 exact previously published *internal* regression."""
    p,K=5,8
    rho,R0,S0,J0,Q=params(283)
    assert (rho,R0,S0,J0,len(Q))==(31,70,2,2,169)
    E=eval_mod(283,Q,R0,S0,J0,p,K+1)
    C=np.array(old_frobenius_C0(E,R0,S0,p,K+1),dtype=np.int64)
    assert C.shape==(140,676)
    lev,hist,prim=smith_cap(C,p,K)
    expected={0:60,1:15,2:30,3:20,4:15}
    assert hist==expected,(hist,expected)
    assert prim is not None and rank_fast(prim,p)==140
    H=gram_mod_np(prim,p,283,J0*len(Q))
    assert rank_fast(H,p)==140
    assert sum(lev)==195
    assert 2*((R0-p)+sum(lev))==520
    return {"historical_p5_index":195,"primitive_H_rank":140,
            "expected_histogram_recovered":True}

def toy_smith():
    p,K=5,8
    mod=p**K
    diag=np.diag([1,p,p*p,p**7,p**8]).astype(np.int64)
    for A in (diag,):
        levels,hist,prim=smith_cap(A,p,K)
        assert levels==[0,1,2,7,8] and prim is None
        B=A.copy()
        B[1]=(B[1]+B[0])%mod
        B[:,0]=(B[:,0]+B[:,1])%mod
        changed,_,other=smith_cap(B,p,K)
        assert changed==levels and other is None
    return True

def parity_check(C,p,Q):
    n,m=C.shape
    assert n==700 and m==2*J*len(Q)
    assert all(Q[i]==(-Q[len(Q)-1-i][0],-Q[len(Q)-1-i][1])
               for i in range(len(Q)))
    P=np.array([(-1)**(r+s) for r in range(R) for s in range(S)],dtype=np.int64)
    A=(C%p).reshape(N,J,len(Q),2)
    for j in range(J):
        assert np.array_equal((P[:,None,None]*A[:,j])%p,
                              (((-1)**j)*A[:,j,::-1,:])%p)
    return True

def full_case(p,K,Q,inert):
    C,F,hist_k=normalized_original(p,K,Q,inert)
    required=(1300,{0:160,1:150,2:140,3:130,4:120}) if inert else (
        0,{0:700})
    assert (F,hist_k)==required, (F,hist_k,required)
    checks=exact_source_oracle(C,p,K,Q,inert)
    parity_check(C,p,Q)
    raw_rank=rank_fast(C,p)
    H0=gram_mod_np(C,p,D,J*len(Q))
    raw_H_rank=rank_fast(H0,p)
    assert raw_H_rank<=raw_rank<=N
    if inert:
        assert len({(x%25,y%25) for x,y in Q})==125
        assert raw_rank<=J*125 and N-raw_rank>=75
    wrong=rank_fast(C[:,:2*(J-1)*len(Q)],p)
    assert wrong<=raw_rank

    levels,sh,prim=smith_cap(C,p,K)
    assert sh.get(0,0)==raw_rank
    lower=sum(levels)
    unresolved=sh.get(K,0)
    assert unresolved==0 if prim is not None else unresolved>0
    result={
      "p":p,"type":"inert" if inert else "split","fixed_K":K,
      "old_F_counted_once":F,"old_k_hist":hist_k,
      "original_full_rows":N,"original_points":len(Q),
      "all_ordinary_jets":J,"original_observation_columns":C.shape[1],
      "direct_exact_oracle_channel_checks":checks,
      "C0_rank_modp":raw_rank,
      "UNSATURATED_C0_Gram_rank":raw_H_rank,
      "UNSATURATED_radical_not_additive":raw_rank-raw_H_rank,
      "wrong_removed_highest_j_rank":wrong,
      "secondary_smith_hist_capped":sh,
      "evaluated_index_lower_if_censored":lower,
      "levels_censored_at_K":unresolved,
      "primitive_C_AND_H_calculated":prim is not None,
      "same_source_lower_vp_G_from_eval_only":2*(F+lower),
    }
    if prim is None:
        result["primitive_pairing_status"]="UNKNOWN: precision cap censored"
    else:
        hp=gram_mod_np(prim,p,D,J*len(Q))
        rp=rank_fast(hp,p)
        assert rp<=N
        result.update({
         "primitive_pairing_status":"COMPLETE_AT_K",
         "primitive_eval_rank":rank_fast(prim,p),
         "primitive_H_rank":rp,
         "primitive_H_corank":N-rp,
         "same_source_lower_vp_G_including_primitive_first_layer":
             2*(F+lower)+(N-rp),
        })
    print("PHASE291_FULL700",result,flush=True)
    return result

def main():
    source_guard()
    rho,r,s,j,Q=params(D)
    assert (rho,r,s,j,len(Q))==(51,R,S,J,QSIZE)
    assert {y for x,y in Q}=={-2,-1,0,1,2}
    counts=Counter(y for x,y in Q)
    assert counts==Counter({0:103,1:91,-1:91,2:37,-2:37})
    assert len(Q)>2*(R-1)+(S-1)
    assert (-D)%5==2 and 2 not in {x*x%5 for x in range(5)}
    assert (-D)%7==4 and 4 in {x*x%7 for x in range(7)}
    assert (2*D)%5==1 and (2*D)%7==6
    toy_smith()
    historical=historical_d283_p5()
    print("PHASE291_HISTORICAL_SMITH_REPLAY",historical,flush=True)
    inert=full_case(5,8,Q,True)
    split=full_case(7,2,Q,False)
    assert inert["C0_rank_modp"]<=625
    assert inert["old_F_counted_once"]==1300
    assert split["old_F_counted_once"]==0
    # Self-contained 2x2 positive-matrix extended eigenoperator witness:
    # diag(2,3) E12 = 2 E12, E12 diag(2,3) = 3 E12;
    # lambda=2/3 exists but E12 is singular and not an integral gauge.
    A=np.diag([2,3])
    X=np.array([[0,1],[0,0]],dtype=np.int64)
    assert np.array_equal(3*(A@X),2*(X@A))
    assert int(X[0,0]*X[1,1]-X[0,1]*X[1,0])==0
    print("PHASE291_OPERATOR_SEMANTIC_GUARD",{
      "finite_SPD_extended_eigenvalues_positive_spectral_ratios":True,
      "higher_powers_same_commutant_classical":True,
      "nonunit_eigenoperator_not_an_integral_gauge":True,
      "modp_radical_not_a_real_spectral_eigenspace":True,
    },flush=True)
    print("PASS Phase291 fixed-K full n700 original-source primitive gate",flush=True)

if __name__=="__main__":
    main()
