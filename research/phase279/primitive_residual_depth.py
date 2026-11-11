#!/usr/bin/env python3
"""Phase279: frozen L=6 primitive D283/p3 residual Smith, original source.

Read PRE_REGISTERED_PRIMITIVE_RESIDUAL_SMITH.md before changing precision.
All p-adic row operations are tracked; internal column swaps/elimination
are NOT transported into original trace weights.
"""
from collections import Counter
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase206"))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase278"))
from source_probe import params,eval_mod,old_frobenius_C0,rank_mod
from secondary_smith import smith_with_row_map,capped_val
from primitive_p3_high_precision import rank_numpy, source_control

P,K,L,N=3,18,6,140
EXPECTED_E={0:36,1:9,2:9,4:36,5:9,6:9,8:31,9:1}
OLD_F3=67
INDEX=527

def tracked_smith(C,p,K):
    """Exact modular Smith pivot levels and integral row map modulo p^K.

    The copied internal column elimination changes A ONLY. The signed
    trace form is restricted to primitive rows recovered from U*C.
    """
    mod=p**K
    n=len(C); m=len(C[0])
    A=[[x%mod for x in row] for row in C]
    U=[[int(i==j) for j in range(n)] for i in range(n)]
    levels=[]
    for k in range(n):
        best=(K,None,None)
        for i in range(k,n):
            for j in range(k,m):
                z=A[i][j]
                if z:
                    v=capped_val(z,p,K)
                    if v<best[0]:
                        best=(v,i,j)
                if best[0]==0:break
            if best[0]==0:break
        v,i,j=best
        if v==K:
            levels.extend([K]*(n-k))
            break
        A[k],A[i]=A[i],A[k]
        U[k],U[i]=U[i],U[k]
        for row in A:
            row[k],row[j]=row[j],row[k]
        d=p**v
        unit_mod=mod//d
        pivot=A[k][k]
        assert pivot%d==0
        inv=pow(pivot//d,-1,unit_mod)
        for ii in range(k+1,n):
            if A[ii][k]:
                assert A[ii][k]%d==0
                t=(A[ii][k]//d)*inv%unit_mod
                A[ii]=[(a-t*b)%mod for a,b in zip(A[ii],A[k])]
                U[ii]=[(a-t*b)%mod for a,b in zip(U[ii],U[k])]
        for jj in range(k+1,m):
            if A[k][jj]:
                assert A[k][jj]%d==0
                t=(A[k][jj]//d)*inv%unit_mod
                for ii in range(n):
                    A[ii][jj]=(A[ii][jj]-t*A[ii][k])%mod
        levels.append(v)
    assert len(levels)==n
    assert rank_mod(U,p)==n
    return levels,U

def primitive_lift(C0,levels,U,p,K,L):
    """Recover ORIGINAL-SOURCE primitive rows mod p^L.

    Reconstruct U*C0 with integer dot products modulo p^K BEFORE
    division; no Smith column operation appears in this recovery.
    """
    assert max(levels)+L<=K
    n=len(C0);m=len(C0[0]);mod=p**K
    out=[]
    for i,exponent in enumerate(levels):
        d=p**exponent
        row=[]
        for j in range(m):
            value=sum(U[i][r]*C0[r][j] for r in range(n))%mod
            assert value%d==0,(i,j,exponent)
            row.append((value//d)%(p**L))
        out.append(row)
    return out

def original_gram(C,mod):
    n=len(C);m=len(C[0])
    assert n==N and m==676
    # All calculations fit signed int64 by a wide margin:
    # 676*566*(3^L-1)^2 < 2e11 for L=6.
    q=np.array(C,dtype=np.int64)%mod
    W=np.tile(np.array([2,566],dtype=np.int64),m//2)
    H=((q*(W%mod))@q.T)%mod
    assert np.array_equal(H,H.T)
    # Different implementation: explicit source-weighted dots.
    for i in (0,1,69,139):
        for j in (0,37,69,139):
            direct=sum(int(q[i,k])*int(q[j,k])*int(W[k])
                       for k in range(m))%mod
            assert int(H[i,j])==direct
    return H

def test():
    D=283
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(31,70,2,2,169)
    assert (-D)%P==2
    E=eval_mod(D,Q,R,S,J,P,K+1)
    C0=old_frobenius_C0(E,R,S,P,K+1)
    assert source_control(E,C0,Q,P,K+1)

    levels,U=tracked_smith(C0,P,K)
    historical,C0mod3=smith_with_row_map(C0,P,K)
    assert levels==historical and C0mod3 is not None
    assert dict(sorted(Counter(levels).items()))==EXPECTED_E
    assert sum(levels)==INDEX and max(levels)==9
    Cprim=primitive_lift(C0,levels,U,P,K,L)
    assert rank_mod(Cprim,P)==N and rank_numpy(Cprim,P)==N
    # Both row-normalization implementations recover same mod-p
    # basis (same deterministic pivot selection).
    assert [[x%P for x in row] for row in Cprim]==C0mod3

    mod=P**L
    H=original_gram(Cprim,mod)
    assert rank_mod((H%P).tolist(),P)==124
    assert rank_numpy(H%P,P)==124
    assert 566%9!=2%9 # wrong metric can look equal mod3

    residual,quot=smith_with_row_map(H.tolist(),P,L)
    hist=dict(sorted(Counter(residual).items()))
    assert hist.get(0,0)==124
    # Integral unimodular shear preserving the local Smith profile.
    U2=np.eye(N,dtype=np.int64)
    U2[0,1]=1
    Hshear=(U2@H@U2.T)%mod
    hist_shear=dict(sorted(Counter(smith_with_row_map(Hshear.tolist(),P,L)[0]).items()))
    assert hist==hist_shear
    residual_lb=sum(residual)
    unresolved=hist.get(L,0)
    print("PRIMITIVE_P3_RESIDUAL",{
        "D":D,"p":P,"source_rows":N,"precision":L,
        "old_F3":OLD_F3,"exact_extra_eval_index":INDEX,
        "primitive_C_rank_mod3":N,"H_rank_mod3":124,
        "residual_histogram_capped":hist,
        "residual_valuation_lower":residual_lb,
        "unresolved_at_cap":unresolved,
        "total_original_v3_lower":2*(OLD_F3+INDEX)+residual_lb,
        "shear_invariant":True
    },flush=True)
    if unresolved:
        assert quot is None
        print("P279_TRUNCATED_LOWER; no exact v3(detG) claimed",flush=True)
    else:
        assert quot is not None and rank_mod(quot,P)==N
        print("P279_EXACT_FINITE",
              {"residual_v3":residual_lb,
               "exact_v3_original_G":2*(OLD_F3+INDEX)+residual_lb},
              flush=True)
    print("PASS Phase279 fixed-L6 same-source primitive residual test",flush=True)

if __name__=="__main__":
    test()
