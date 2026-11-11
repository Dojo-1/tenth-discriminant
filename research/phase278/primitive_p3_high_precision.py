#!/usr/bin/env python3
"""Phase278 K=18 exact local p3 Smith with tracked original-source row map.

Protocol: PRE_REGISTERED_P3_SOURCE_SATURATION.md. This file makes no
class-number-one claim and does not promote any truncated levels to
exact primitive residual valuations. Replays old p5 primitive unit.
"""
from collections import Counter
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase206"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase204"))
from source_probe import params, eval_mod, old_frobenius_C0, gram_mod, rank_mod
from secondary_smith import smith_with_row_map
from primitive_p5_det import determinant_mod
from ordinary_jet_filtration import jet

D,R,S,J,RHO,N,QSIZE=283,70,2,2,31,140,169
P3,K=3,18
HIST_K6={0:36,1:9,2:9,4:36,5:9,6:41}
HIST_P5={0:60,1:15,2:30,3:20,4:15}

def rank_numpy(M,p):
    A=np.array(M,dtype=np.int64)%p
    n,m=A.shape
    row=0
    for col in range(m):
        if row==n:break
        nz=np.flatnonzero(A[row:,col])
        if not len(nz):continue
        pivot=row+int(nz[0])
        if pivot!=row:
            A[[row,pivot]]=A[[pivot,row]]
        A[row,col:]=A[row,col:]*pow(int(A[row,col]),-1,p)%p
        idx=np.flatnonzero(A[row+1:,col])+row+1
        if len(idx):
            A[idx,col:]=(A[idx,col:]-A[idx,col,None]*A[row,col:])%p
        row+=1
    return row

def source_control(E,C0,Q,p,precision):
    """Alternative integer (not modular power) original-jet evaluation.

    Check old Frobenius row quotient at selected boundary/middle rows,
    both s-values, all j, and 3 frozen observation points, INCLUDING
    imaginary coordinate. Comparisons use the full original E.
    """
    mod=p**precision
    reduced=p**(precision-1)
    for r in (0,1,p,p+1,34,69):
        for s in range(2):
            k=min(r//p,1-s)
            idx=2*r+s
            for j in range(J):
                for qi in (0,len(Q)//2,len(Q)-1):
                    z=Q[qi]
                    full=jet(D,r,s,j,z)
                    col=2*(j*len(Q)+qi)
                    assert tuple(E[idx][col+cc] for cc in (0,1)) == (
                        full[0]%mod,full[1]%mod)
                    if k:
                        lower=jet(D,r-p,s+1,j,z)
                        vals=tuple(full[cc]-lower[cc] for cc in (0,1))
                        assert all(v%p==0 for v in vals)
                        vals=tuple((v//p)%reduced for v in vals)
                    else:
                        vals=tuple(full[cc]%reduced for cc in (0,1))
                    assert tuple(C0[idx][col+cc] for cc in (0,1)) == vals,(
                        p,r,s,j,qi)
    return True

def primitive_test(p,K,expected,comparison):
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(RHO,70,2,2,QSIZE)
    assert (-D)%p not in {k*k%p for k in range(p)}
    # K+1 source precision is necessary for the OLD p denominator.
    E=eval_mod(D,Q,R,S,J,p,K+1)
    assert len(E)==N and len(E[0])==2*J*len(Q)==676
    C0=old_frobenius_C0(E,R,S,p,K+1)
    assert source_control(E,C0,Q,p,K+1)
    old=R-p
    assert rank_mod([[x%p for x in row] for row in C0],p)==(36 if p==3 else 60)
    levels,Cprim=smith_with_row_map(C0,p,K)
    hist=dict(sorted(Counter(levels).items()))
    clipped=dict(sorted(Counter(min(v,6) for v in levels).items()))
    if p==3:
        assert clipped==HIST_K6,(clipped,HIST_K6)
    if comparison:
        assert hist==expected, (hist,expected)
    index_lower=sum(levels)
    unresolved=hist.get(K,0)
    print("SMITH",{"p":p,"precision":K,"old_Fp":old,
                   "histogram":hist,"index_lower":index_lower,
                   "unresolved_at_cap":unresolved},flush=True)
    if Cprim is None:
        assert unresolved>0
        print("INCONCLUSIVE_NO_PRIMITIVE",{"p":p,"at_least_vp":2*(old+index_lower),
                                         "unresolved_levels":unresolved},flush=True)
        return None
    assert not unresolved
    assert rank_mod(Cprim,p)==N
    assert rank_numpy(Cprim,p)==N
    assert rank_numpy(np.array(Cprim)[:,:2*len(Q)],p) <=N
    # Restrict the ORIGINAL 2/2D metric; numeric products safe modulo p.
    weighted=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    C=np.array(Cprim,dtype=np.int64)%p
    H=((C*(weighted%p))@C.T)%p
    Hr=rank_numpy(H,p)
    assert Hr==rank_mod(H.tolist(),p)
    assert np.array_equal(H,H.T)
    # Cross-check a deterministic selection of Gram entries with a
    # separate explicit dot-product implementation, not a flat metric.
    for i in (0,1,69,139):
        for j in (0,37,69,139):
            entry=sum(int(C[i,k])*int(C[j,k])*int(weighted[k])
                      for k in range(C.shape[1]))%p
            assert int(H[i,j])==entry
    residual_lower=N-Hr
    print("PRIMITIVE",{"p":p,"full_C_rank":N,"H_rank":Hr,
                       "H_radical":residual_lower,
                       "total_vp_lower":2*(old+index_lower)+residual_lower},
          flush=True)
    if Hr==N:
        detmod=determinant_mod(H.tolist(),p)
        assert detmod!=0
        exact=2*(old+index_lower)
        print("EXACT_PRIMITIVE_UNIT",{"p":p,"detH_modp":detmod,
                                      "v_p_det_Gram":exact,
                                      "index":index_lower},flush=True)
    else:
        print("RESIDUAL_DEEPER_LAYERS_UNRESOLVED",
              {"p":p,"rank_defect":N-Hr,"do_not_claim_exact_valuation":True},
              flush=True)
    return (index_lower,Hr)

def main():
    # Negative control: SAME D283 source, independently established
    # complete p5 unit pairing. Do not count its old or new factors twice.
    p5=primitive_test(5,6,HIST_P5,comparison=True)
    assert p5==(195,N),p5
    print("P5_KNOWN_NEGATIVE_REPLAY_OK",flush=True)

    p3=primitive_test(P3,K,{},comparison=False)
    if p3 is None:
        print("P3_K18_STOP unresolved: no primitive pairing claim",flush=True)
    else:
        index,rankH=p3
        print("P3_K18_FINITE_RESULT",
              {"index":index,"primitive_H_rank":rankH,"D":D},
              flush=True)
    print("PASS Phase278 exact original-source fixed-K test; no uniform bound",flush=True)

if __name__=="__main__":
    main()
