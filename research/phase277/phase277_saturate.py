#!/usr/bin/env python3
"""Phase277: local Smith saturation of the ORIGINAL D403 trace Gram.

At p=7 only, remove the established old (Z^p-W)^k Frobenius row
factors ONCE. At split p=11 do not invoke that division. Subsequent
Smith operations on the original integer-coordinate evaluation matrix
provide a full-rank primitive row lattice modulo p. Its restricted
pairing uses the unchanged diagonal metric B=(2,2D,...).

A first-image radical is NOT a primitive pairing radical. Exact local
determinant valuation follows from diagonal Smith exponents and the
nondegenerate modulo-p^2 primitive Gram.
No asymptotic or class-number-one field claim follows.
"""
import sys
import time
from pathlib import Path
from collections import Counter
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from phase277_probe import build,gram_from_rows,rank_mod,p2_smith,D,R,S,J

def local_smith_with_U(C,p,L,prim_precision=1,log=True):
    n,m=C.shape
    mod=p**L
    A=np.asarray(C%mod,dtype=np.int64).copy()
    C_row=A.copy() # track unimodular ROW transforms separately from COLUMN ops
    exps=[]
    t0=time.monotonic()
    for k in range(n):
        hit=None
        for v in range(L):
            den=p**v
            for i in range(k,n):
                js=np.flatnonzero((A[i,k:]//den)%p)
                if len(js):
                    hit=(v,i,k+int(js[0]))
                    break
            if hit is not None:break
        if hit is None:
            print('SATURATION_INCOMPLETE',p,'k',k,'of',n,'L',L,flush=True)
            return exps,None
        v,i,j=hit
        if i!=k:
            A[[i,k]]=A[[k,i]]
            C_row[[i,k]]=C_row[[k,i]]
        if j!=k:A[:,[j,k]]=A[:,[k,j]]
        den=p**v
        inner=mod//den
        pivot=int(A[k,k])
        assert pivot%den==0 and pivot//den%p!=0,(p,k,pivot,v)
        inv=pow(pivot//den,-1,inner)
        vals=A[k+1:,k].copy()
        rr=np.flatnonzero(vals)
        if len(rr):
            indexes=k+1+rr
            assert np.all(vals[rr]%den==0)
            factors=((vals[rr]//den)*inv)%inner
            A[indexes,:]=(A[indexes,:]-factors[:,None]*A[k,:])%mod
            C_row[indexes,:]=(C_row[indexes,:]-factors[:,None]*C_row[k,:])%mod
        vals=A[k,k+1:].copy()
        jj=np.flatnonzero(vals)
        if len(jj):
            assert np.all(vals[jj]%den==0)
            factors=((vals[jj]//den)*inv)%inner
            cols=k+1+jj
            A[:,cols]=(A[:,cols]-A[:,k,None]*factors[None,:])%mod
        assert not np.any(A[k+1:,k])
        assert not np.any(A[k,k+1:])
        exps.append(v)
        if log and (k%50==49 or k==n-1):
            print('SMITH_PROGRESS',dict(p=p,k=k+1,
               levels={i:exps.count(i) for i in sorted(set(exps))},
               seconds=round(time.monotonic()-t0,2)),flush=True)
    assert len(exps)==n
    assert np.array_equal(A[:,:n]%mod,np.diag(np.diag(A[:,:n]))%mod)
    B=C_row.copy()
    for i,v in enumerate(exps):
        den=p**v
        assert np.all((B[i,:]%den)==0),(i,v)
        assert L-v>=prim_precision
        B[i,:]=(B[i,:]//den)%(p**prim_precision)
    primitive=B%(p**prim_precision)
    assert rank_mod(primitive%p,p)==n
    return exps,primitive

def gram_mod_power(C,p,power,weight_D=D):
    mod=p**power
    C=np.asarray(C%mod,dtype=np.int64)
    weights=np.tile(np.array([2,2*weight_D],dtype=np.int64),
                    C.shape[1]//2)%mod
    return (C@((C*weights)%mod).T)%mod

def run(p=7,L=6,prim_precision=2):
    assert (p,L,prim_precision) in ((7,6,2),(11,9,3))
    t=time.monotonic()
    C,k,Q=build(p,p==7,precision=L)
    assert C.shape==(400,1752) and len(Q)==219
    before=rank_mod(C%p,p)
    print('RAW_RANK',p,before,'frobenius_sum',sum(k),
          'elapsed_seconds',round(time.monotonic()-t,2),flush=True)
    exps,primitive=local_smith_with_U(C,p,L,prim_precision)
    assert primitive is not None
    hist=Counter(exps)
    K=gram_from_rows(primitive%p,p)
    rank=rank_mod(K,p)
    residual_levels=p2_smith(gram_mod_power(primitive,p,2),p,rank)
    summary=dict(D=D,p=p,precision=L,source_rows=len(C),
          old_F=int(sum(k)),eval_smith=dict(sorted(hist.items())),
          exact_eval_index=int(sum(exps)),
          primitive_eval_rank=rank_mod(primitive%p,p),
          residual_smith_p2=residual_levels,
          primitive_pairing_rank=rank,primitive_pairing_radical=400-rank,
          pairing_valuation_lower=400-rank,
          exact_vp_gram=(int(2*(sum(k)+sum(exps))+residual_levels['1'])
                         if residual_levels['>=2']==0 else None))
    assert summary['exact_vp_gram'] is not None
    expected={
      7:dict(old_F=530,eval_smith={0:331,1:5,2:4,3:23,4:37},
             exact_eval_index=230,residual_smith_p2={'0':400,'1':0,'>=2':0},
             primitive_pairing_radical=0,exact_vp_gram=1520),
      11:dict(old_F=0,eval_smith={0:132,1:66,2:44,3:44,4:44,5:44,6:26},
              exact_eval_index=838,residual_smith_p2={'0':394,'1':6,'>=2':0},
              primitive_pairing_radical=6,exact_vp_gram=1682)
    }
    for key,value in expected[p].items():
        assert summary[key]==value,(p,key,summary[key],value)
    print('PRIMITIVE_RESIDUAL',summary,flush=True)
    return summary

if __name__=='__main__':
    run(7,6,2)
    run(11,9,3)
    print('PASS Phase277 exact local Smith and same-original-Gram valuations')
