#!/usr/bin/env python3
"""Phase292: original-source p5 D587 heldout versus frozen D563 control.

PREREGISTERED at commit 52135e0 BEFORE implementation/results.
All original rectangular rows, original ordinary Z jets with W fixed,
full ellipse, trace metric diag(2,2D). No new uniform or h=1 theorem.
"""
from collections import Counter
from math import comb
from pathlib import Path
import subprocess
import sys

import numpy as np

HERE=Path(__file__).resolve()
ROOT=HERE.parents[2]
for sub in ("phase206","phase204","phase280","phase281"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params,mul,fall
from ordinary_jet_filtration import jet
from full_d403_second_layer import first_two_smith
from full_d403_third_layer import smith_profile_k3

P=5
K=9
EXPECTED_GEOMETRY={
    563:dict(rho=51,R=140,S=5,J=5,Q=359,m=3590,
             counts={-2:37,-1:91,0:103,1:91,2:37},
             F=1300,k_hist={0:160,1:150,2:140,3:130,4:120}),
    587:dict(rho=53,R=146,S=5,J=5,Q=383,m=3830,
             counts={-2:43,-1:95,0:107,1:95,2:43},
             F=1360,k_hist={0:166,1:156,2:146,3:136,4:126}),
}
FROZEN_BLOBS={
 "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":"dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
 "research/phase280/full_d403_second_layer.py":"7abffdf4f4916dacef08ebe097e5eed700837ad4",
 "research/phase281/full_d403_third_layer.py":"d28b1420a371ca3a8a0297a19ecec75feedfc978",
}

def freeze():
    for path,sha in FROZEN_BLOBS.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("source helper changed",path,actual,sha)

def ppowers(z,length,D,mod):
    out=[(1,0)]
    for _ in range(length):
        out.append(mul(out[-1],z,D,mod))
    return out

def k_old(r,s,S):
    return min(r//P,S-1-s)

def source_normalized(D,Q,R,S,J):
    """New parameterized original source. No import of Phase291 source builder."""
    q=P**(K+S-1)
    red=P**K
    n=R*S
    m=2*J*len(Q)
    C=np.zeros((n,m),dtype=np.int64)
    cache=[]
    for x,y in Q:
        z=(x%q,y%q)
        w=(x%q,(-y)%q)
        zp=ppowers(z,R-1,D,q)
        wp=ppowers(w,S-1,D,q)
        assert zp[P][0]%P==w[0]%P and zp[P][1]%P==w[1]%P
        cache.append((zp,wp))
    hist=Counter()
    old=0
    for r in range(R):
        if r%40==0:
            print("PHASE292_SOURCE_PROGRESS",{"D":D,"row_r":r,"R":R},flush=True)
        for s in range(S):
            k=k_old(r,s,S)
            hist[k]+=1
            old+=k
            div=P**k
            row=r*S+s
            for j in range(J):
                offset=2*j*len(Q)
                for i,(zp,wp) in enumerate(cache):
                    a=b=0
                    for t in range(k+1):
                        rr=r-P*t
                        if rr<j:continue
                        coefficient=comb(k,t)*(-1 if t%2 else 1)*fall(rr,j)
                        u,v=mul(zp[rr-j],wp[s+t],D,q)
                        a=(a+coefficient*u)%q
                        b=(b+coefficient*v)%q
                    assert a%div==0 and b%div==0,(
                        "bad Frobenius integral row",D,r,s,j,Q[i],k)
                    C[row,offset+2*i]=a//div%red
                    C[row,offset+2*i+1]=b//div%red
    return C,old,dict(sorted(hist.items()))

def oracle_exact(D,Q,R,S,J,C):
    probes=[
        (0,0),(0,4),(1,3),(4,0),(5,0),(5,4),(10,2),(15,1),
        (25,0),(35,4),(69,2),(70,0),(99,3),(110,1),(R-1,0),(R-1,4)
    ]
    assert len(probes)==16
    seen=set()
    for r,s in probes:
        assert r<R and s<S
        k=k_old(r,s,S)
        seen.add(k)
        div=P**k
        for j in range(J):
            for qi in (0,len(Q)//2,len(Q)-1):
                z=Q[qi]
                exact=[0,0]
                for t in range(k+1):
                    aa,bb=jet(D,r-P*t,s+t,j,z)
                    coef=comb(k,t)*(-1 if t%2 else 1)
                    exact[0]+=coef*aa
                    exact[1]+=coef*bb
                assert all(v%div==0 for v in exact)
                expected=(exact[0]//div%P**K,exact[1]//div%P**K)
                col=2*(j*len(Q)+qi)
                actual=(int(C[r*S+s,col]),int(C[r*S+s,col+1]))
                assert actual==expected,("wrong ordinary jet",D,r,s,j,qi)
    assert {0,1,2,3,4}.issubset(seen)
    return 16*J*3*2

def independent_rank(M,p=P):
    """Pivot-first finite-field elimination, independent of Smith valuation loop."""
    a=np.array(M,dtype=np.int64,copy=True)%p
    n,m=a.shape
    row=0
    for col in range(m):
        if row==n:break
        js=np.flatnonzero(a[row:,col])
        if not js.size:continue
        candidate=row+int(js[0])
        if candidate!=row:a[[row,candidate]]=a[[candidate,row]]
        inv=pow(int(a[row,col]),-1,p)
        a[row,col:]=(a[row,col:]*inv)%p
        others=np.flatnonzero(a[row+1:,col])+row+1
        if others.size:
            a[others,col:]=(a[others,col:]
                    -a[others,col,None]*a[row,col:])%p
        row+=1
    return row

def source_smith_with_row_map(C):
    """Capped K9 p-local Smith, track ONLY unimodular source ROW map.

    Internal column swaps are only used to discover invariant factors,
    never transported into the original observation metric.
    """
    mod=P**K
    n,m=C.shape
    assert n<=800 and m<=4000 and n*mod*mod < 2**63
    A=np.array(C,dtype=np.int64,copy=True)%mod
    U=np.eye(n,dtype=np.int64)
    levels=[]
    for i in range(n):
        tail=A[i:,i:]
        pivot=None
        for v in range(K):
            hits=tail%(P**(v+1))!=0
            if np.any(hits):
                h=int(hits.argmax())
                row,col=divmod(h,tail.shape[1])
                pivot=(v,i+row,i+col)
                break
        if pivot is None:
            levels.extend([K]*(n-i))
            break
        v,r,c=pivot
        if r!=i:
            A[[i,r]]=A[[r,i]]
            U[[i,r]]=U[[r,i]]
        if c!=i:A[:,[i,c]]=A[:,[c,i]]
        div=P**v
        modulus=mod//div
        assert int(A[i,i])%div==0
        inverse=pow(int(A[i,i])//div,-1,modulus)
        coefficients=(A[i+1:,i]//div*inverse)%modulus
        if i+1<n:
            A[i+1:,i+1:]=(A[i+1:,i+1:]
                           -coefficients[:,None]*A[i,i+1:])%mod
            U[i+1:,:]=(U[i+1:,:]-coefficients[:,None]*U[i,:])%mod
            A[i+1:,i]=0
        # Since below-pivot column is zero, valid elementary column
        # elimination changes only first-row off-diagonal entries.
        assert np.all(A[i,i+1:]%div==0)
        A[i,i+1:]=0
        levels.append(v)
        if (i+1)%150==0 or i+1==n:
            print("PHASE292_SMITH_PROGRESS",{
                "processed":i+1,"total":n,"level":v},flush=True)
    assert len(levels)==n
    histogram=dict(sorted(Counter(levels).items()))
    assert independent_rank(U%P,P)==n
    return levels,histogram,U

def metric_gram(C,D,J,Q,mod):
    assert C.shape[1]==2*J*len(Q)
    weights=np.tile(np.array((2,2*D),dtype=np.int64),J*len(Q))
    A=C%mod
    H=((A*(weights%mod))@A.T)%mod
    assert np.array_equal(H,H.T)
    for i,j in ((0,0),(0,len(H)-1),(len(H)//2,len(H)-1)):
        direct=sum(int(A[i,c])*int(A[j,c])*int(weights[c])
                   for c in range(len(weights)))%mod
        assert direct==int(H[i,j])
    return H

def parity_guard(C,D,Q,R,S,J):
    n=R*S
    assert C.shape==(n,2*J*len(Q))
    parity=np.array([(-1)**(r+s) for r in range(R)
                     for s in range(S)],dtype=np.int64)
    A=(C%25).reshape(n,J,len(Q),2)
    assert all(Q[i]==(-Q[len(Q)-1-i][0],-Q[len(Q)-1-i][1])
               for i in range(len(Q)))
    for j in range(J):
        lhs=(parity[:,None,None]*A[:,j])%25
        rhs=((-1)**j*A[:,j,::-1,:])%25
        assert np.array_equal(lhs,rhs),("C2 inversion broken",D,j)
    even=[r*S+s for r in range(R) for s in range(S) if (r+s)%2==0]
    odd=[r*S+s for r in range(R) for s in range(S) if (r+s)%2!=0]
    assert len(even)==len(odd)==n//2
    f_even=sum(k_old(r,s,S) for r in range(R)
               for s in range(S) if (r+s)%2==0)
    f_odd=sum(k_old(r,s,S) for r in range(R)
              for s in range(S) if (r+s)%2!=0)
    assert f_even==f_odd==EXPECTED_GEOMETRY[D]["F"]//2
    return even,odd

def toy():
    mod=P**K
    A=np.diag([1,P,P**2,P**8,P**9]).astype(np.int64)
    levels,hist,U=source_smith_with_row_map(A)
    assert levels==[0,1,2,8,9]
    assert 9 in hist
    B=A.copy()
    B[1]=(B[1]+B[0])%mod
    B[:,0]=(B[:,0]+B[:,1])%mod
    levels2,_,_=source_smith_with_row_map(B)
    assert levels2==levels
    return True

def specimen(D):
    geometry=EXPECTED_GEOMETRY[D]
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(
        geometry["rho"],geometry["R"],geometry["S"],geometry["J"],
        geometry["Q"])
    assert 2*J*len(Q)==geometry["m"]
    assert dict(Counter(y for x,y in Q))==geometry["counts"]
    assert len(Q)>2*(R-1)+(S-1)
    assert (-D)%P in (2,3)
    assert len({(x%25,y%25) for x,y in Q})==125
    assert len(Q)==len(set(Q))
    C,F,k_hist=source_normalized(D,Q,R,S,J)
    assert C.shape==(R*S,geometry["m"])
    assert (F,k_hist)==(geometry["F"],geometry["k_hist"])
    checks=oracle_exact(D,Q,R,S,J,C)
    even,odd=parity_guard(C,D,Q,R,S,J)
    raw_rank=independent_rank(C%P)
    raw_gram=metric_gram(C,D,J,Q,P)
    raw_gram_rank=independent_rank(raw_gram)
    assert raw_rank<=J*125 and raw_gram_rank<=raw_rank
    # An independent earlier first-two-Smith implementation checks
    # the first two levels, without sharing the saturation pivot code.
    two=first_two_smith(C%(P**2),P)
    assert two["0"]==raw_rank
    levels,hist,U=source_smith_with_row_map(C)
    assert hist.get(0,0)==raw_rank and sum(hist.values())==R*S
    assert hist.get(1,0)==two["1"]
    assert sum(count for e,count in hist.items() if e>=2)==two[">=2"]
    idxlower=sum(levels)
    censored=hist.get(K,0)
    value={
       "D":D,"p":P,"prime_type":"inert","R":R,"S":S,"J":J,
       "rho":rho,"Q_full_original":len(Q),"original_rows":R*S,
       "original_columns":C.shape[1],"frozen_source_hashes":True,
       "old_frobenius_F_counted_once":F,
       "old_k_histogram":k_hist,
       "exact_original_jet_coordinate_checks":checks,
       "T_p2_original_residue_classes":125,
       "phase208_rank_ceiling":J*125,
       "raw_C0_rank_modp":raw_rank,
       "unsaturated_original_metric_gram_rank_modp":raw_gram_rank,
       "unsaturated_radical_NOT_ADDITIVE":raw_rank-raw_gram_rank,
       "secondary_smith_K9":hist,
       "secondary_index_lower":idxlower,
       "unresolved_secondary_levels_K9":censored,
       "mod25_first_two_independent_smith":two,
       "C2_original_row_even_odd_counts":[len(even),len(odd)],
       "original_F_in_each_parity_sector":F//2,
       "same_source_Gram_vp_lower_without_primitive":2*(F+idxlower),
    }
    if censored:
        value["primitive_H_status"]="NOT_COMPUTED: censored secondary Smith"
        return value
    # An exact finite source index; p-adic image saturation only if
    # the original observation columns are preserved.
    idx=sum(levels)
    depth=K-max(levels)
    assert 1<=depth<=K
    numerator=(U@C)%(P**K)
    Cprim=np.zeros_like(C)
    m=P**min(depth,3)
    for i,e in enumerate(levels):
        assert np.all(numerator[i]%(P**e)==0)
        Cprim[i]=(numerator[i]//(P**e))%m
    assert independent_rank(Cprim%P)==R*S
    value.update({
       "secondary_index_exact":idx,
       "primitive_precision_available":depth,
       "primitive_C_rank_modp":R*S,
    })
    H=metric_gram(Cprim,D,J,Q,m)
    h0=independent_rank(H%P)
    value["primitive_H_rank_modp"]=h0
    value["primitive_H_corank_modp"]=R*S-h0
    if h0==R*S:
        residual=0
        exact=True
        value["primitive_H_smith"]="unit"
    elif depth>=3:
        profile=smith_profile_k3(H%(P**3),P)
        assert profile["0"]==h0
        test2=first_two_smith(H%(P**2),P)
        assert profile["1"]==test2["1"] and profile["0"]==test2["0"]
        assert profile["2"]+profile[">=3"]==test2[">=2"]
        residual=profile["1"]+2*profile["2"]+3*profile[">=3"]
        exact=profile[">=3"]==0
        value["primitive_H_smith_K3"]=profile
    elif depth==2:
        profile=first_two_smith(H%(P**2),P)
        residual=profile["1"]+2*profile[">=2"]
        exact=profile[">=2"]==0
        value["primitive_H_smith_K2"]=profile
    else:
        residual=R*S-h0
        exact=False
        value["primitive_H_smith_K1"]={"unit":h0,"ge1":R*S-h0}
    vp=2*(F+idx)+residual
    value["primitive_H_valuation_exact" if exact
          else "primitive_H_valuation_lower"]=residual
    value["original_full_Gram_v5_exact" if exact
          else "original_full_Gram_v5_lower"]=vp
    value["no_unproved_asymptotic_or_field_claim"]=True
    if D==563:
        assert hist=={0:620,1:5,5:15,6:60}
        assert idx==440 and depth>=3
        assert value["primitive_H_smith_K3"]=={
            "0":684,"1":15,"2":1,">=3":0}
        assert exact and vp==3497
    return value

def main():
    freeze()
    assert toy()
    for D in (563,587):
        result=specimen(D)
        print("PHASE292_MATCHED_INERT5",result,flush=True)
    print("PASS Phase292 matched original-source p5 D563 regression + D587 holdout",
          flush=True)

if __name__=="__main__":
    main()
