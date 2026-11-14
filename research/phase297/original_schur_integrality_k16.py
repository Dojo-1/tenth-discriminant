#!/usr/bin/env python3
"""Phase297-B: p^16 original D587 Schur projection coker refinement.

Preregistered ae04e06 BEFORE any K16 code, after K9 focused success.
Full original source D587 Q383/J5/row R146, five r145 new rows.
No extra determinant factor; source original polynomial and trace metric.
"""
from collections import Counter
from math import comb
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase204","phase292","phase297"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params,gram
from ordinary_jet_filtration import jet
import matched_inert5_neighbor as frozen_source
import original_schur_integrality as prior

D=587
P=5
K_HI=16
MOD=P**K_HI
BASE=P**6
J=S=5
FULL_R=146
CUT_R=145
OLD_MOD=P**9
CHUNK=128
EXPECTED_K9={
 "even":{0:63,2:15,3:47,4:63,5:47,6:10,7:5,8:50,9:63},
 "odd":{0:62,2:15,3:48,4:62,5:48,6:10,7:5,8:50,9:62},
}
FROZEN={
 "research/phase297/original_schur_integrality.py":
    "6ce23a8136ddd6208ef70d00a2bca419a105fdbb",
 "research/phase292/matched_inert5_neighbor.py":
    "9216de10f311cf301413de663738804b5fbec203",
}

def freeze():
    prior.guard()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("source changed",path,actual,sha)

def source_high_precision(Q):
    assert frozen_source.K==9
    frozen_source.K=K_HI
    try:
        C,oldF,hist=frozen_source.source_normalized(D,Q,FULL_R,S,J)
    finally:
        frozen_source.K=9
    assert frozen_source.K==9
    assert C.shape==(730,3830) and oldF==1360
    assert hist=={0:166,1:156,2:146,3:136,4:126}
    assert np.all((C>=0)&(C<MOD))
    return C

def rebuild_original(C,Q):
    n,m=C.shape
    assert (n,m)==(730,3830)
    E=np.zeros_like(C)
    for r in range(FULL_R):
        for s in range(S):
            idx=r*S+s
            k=frozen_source.k_old(r,s,S)
            out=(C[idx]*(P**k))%MOD
            for t in range(1,k+1):
                lower=(r-5*t)*S+s+t
                assert 0<=lower<idx
                factor=(-1 if t%2 else 1)*comb(k,t)
                out=(out-factor*E[lower])%MOD
            E[idx]=out
    assert np.all((E>=0)&(E<MOD))
    # Crucial full-entry congruence with independently replayed K9 source.
    E9,old_replay_checks=prior.original_rows_from_divided_source(
        C%OLD_MOD,Q)
    assert np.array_equal(E%OLD_MOD,E9),(
        "K16 original monomial basis does not replay K9")
    assert old_replay_checks==600

    rows=prior.PROBE_ROWS+[(13,2),(47,4),(81,0),(145,0)]
    qidx=(0,3,len(Q)//2,len(Q)-4,len(Q)-1)
    checked=0
    for r,s in rows:
        for j in range(J):
            for qi in qidx:
                val=jet(D,r,s,j,Q[qi])
                col=2*(j*len(Q)+qi)
                assert (
                    int(E[r*S+s,col]),int(E[r*S+s,col+1]))==(
                    val[0]%MOD,val[1]%MOD),("exact original jet",r,s,j,qi)
                checked+=2
    assert checked==len(rows)*J*len(qidx)*2
    return E,checked

def digits(X):
    assert X.dtype==np.int64
    return [X%BASE,(X//BASE)%BASE,(X//(BASE**2))%BASE]

def pairings_three_digits(X,Y,W):
    """Exact original weighted Gram mod5^16 via 3 base5^6 digits.

    Integer dot bound 128*(BASE-1)^2*(2D) <=2^63.
    Terms of digit total exponent >=3 vanish mod5^16.
    """
    assert X.shape[1]==Y.shape[1]==len(W)==3830
    assert BASE**2 < MOD < BASE**3
    bound=CHUNK*(BASE-1)**2*int(W.max())
    assert bound<2**63,("signed int64 overflow risk",bound)
    xx=digits(X)
    yy=digits(Y)
    out=np.zeros((X.shape[0],Y.shape[0]),dtype=np.int64)
    for start in range(0,len(W),CHUNK):
        end=min(len(W),start+CHUNK)
        for digit_sum in range(3):
            cap=MOD//(BASE**digit_sum)
            sub=np.zeros_like(out)
            for a in range(digit_sum+1):
                b=digit_sum-a
                lhs=xx[a][:,start:end]
                rhs=yy[b][:,start:end]
                # Without source digit decomposition the same
                # dot product WOULD OVERFLOW signed int64 here.
                part=((lhs*W[start:end])@rhs.T)%cap
                sub=(sub+part)%cap
            out=(out+(BASE**digit_sum)*sub)%MOD
    # independent integer direct weighted pairings, no numpy dot.
    probes=((0,0),(0,Y.shape[0]-1),
            (X.shape[0]-1,0),
            (X.shape[0]//2,Y.shape[0]//2))
    for i,j in probes:
        direct=sum(int(X[i,z])*int(W[z])*int(Y[j,z])
                   for z in range(len(W)))%MOD
        assert int(out[i,j])==direct,("digit split Gram drift",i,j)
    return out

def sanity_original_gram(E,Q,W):
    ids=[r*S+s for r,s in prior.GRAM_ROWS]
    actual=pairings_three_digits(E[ids],E[ids],W)
    exact=gram(D,Q,J,prior.GRAM_ROWS)
    assert all(int(actual[i,j])==int(exact[i][j])%MOD
               for i in range(len(ids)) for j in range(len(ids)))
    assert actual.shape==(6,6)
    return 36

def high_precision_smith(M,K=K_HI):
    """Exact p-adic elementary divisors over Z/p^K, bigint intermediates.

    Tracks only valuations, not alleged integral row/observation gauges.
    All arithmetic uses Python arbitrary-precision integers in
    numpy object arrays; no 64-bit scalar products.
    """
    mod=P**K
    A=np.asarray(M,dtype=object)%mod
    n,m=A.shape
    assert n<=m and 1<=n<=365
    levels=[]
    for i in range(n):
        tail=A[i:,i:]
        pivot=None
        for v in range(K):
            hits=np.argwhere(tail%(P**(v+1))!=0)
            if len(hits):
                r,c=map(int,hits[0])
                pivot=(v,i+r,i+c)
                break
        if pivot is None:
            levels.extend([K]*(n-i))
            break
        v,r,c=pivot
        if r!=i:A[[i,r]]=A[[r,i]]
        if c!=i:A[:,[i,c]]=A[:,[c,i]]
        d=P**v
        assert int(A[i,i])%d==0
        q=mod//d
        inv=pow(int(A[i,i])//d,-1,q)
        if i+1<n:
            col=A[i+1:,i]
            assert all(int(x)%d==0 for x in col)
            coefs=(col//d*inv)%q
            A[i+1:,i+1:]=(A[i+1:,i+1:]
                -coefs[:,None]*A[i,i+1:])%mod
            A[i+1:,i]=0
        assert all(int(x)%d==0 for x in A[i,i+1:])
        A[i,i+1:]=0
        levels.append(v)
        if (i+1)%100==0 or (i+1)==n:
            print("PHASE297B_BIGINT_SMITH_PROGRESS",{
                "processed":i+1,"n":n,"level":v,"K":K},flush=True)
    assert len(levels)==n
    assert levels==sorted(levels)
    hist=dict(sorted(Counter(levels).items()))
    assert sum(hist.values())==n
    return levels,hist

def smith_toys():
    # Positive finite-index witness hidden beyond k9: old Smith
    # [1,5^3,5^15,0], augmented column 5^10 e3.
    A=np.diag([1,P**3,P**15,0]).astype(np.int64)
    new=np.array([[0],[0],[P**10],[0]],dtype=np.int64)
    old,oldhist=high_precision_smith(A)
    aug,aughist=high_precision_smith(np.concatenate((A,new),axis=1))
    assert old==[0,3,15,16]
    assert aug==[0,3,10,16]
    assert sum(old)-sum(aug)==5
    # Unimodular row and column changes preserve Smith classes.
    T=np.eye(4,dtype=np.int64);T[0,1]=1;T[1,2]=2
    U=np.eye(4,dtype=np.int64);U[0,3]=1;U[2,1]=-1
    transformed=(T.astype(object)@A.astype(object)@U.astype(object))%MOD
    tr,_=high_precision_smith(transformed)
    assert tr==old
    for a,c,expect in ((10,2,1),(10,5,0)):
        l,_=high_precision_smith(np.array([[a]],dtype=np.int64))
        r,_=high_precision_smith(np.array([[a,c]],dtype=np.int64))
        assert sum(l)-sum(r)==expect
    return {"level15_v_level10_nonmembership_detected_delta5":True,
            "row_and_column_unimodular_controls":True,
            "nonintegral_and_integral_positive_Gram_toys":True}

def parity_blocks(E,Q,W):
    old_even=[i for i in range(CUT_R*S)
              if (i//S+i%S)%2==0]
    old_odd=[i for i in range(CUT_R*S)
              if (i//S+i%S)%2==1]
    new_even=[i for i in range(CUT_R*S,FULL_R*S)
              if (i//S+i%S)%2==0]
    new_odd=[i for i in range(CUT_R*S,FULL_R*S)
              if (i//S+i%S)%2==1]
    assert list(map(len,(old_even,old_odd,new_even,new_odd)))==[
        363,362,2,3]
    # Full ORIGINAL parity check at the new p16 precision.
    parity_cross=pairings_three_digits(
        E[old_even+new_even],E[old_odd+new_odd],W)
    assert not np.any(parity_cross),(
        "original parity cross Gram nonzero",np.count_nonzero(parity_cross))
    print("PHASE297B_FULL_PARITY",{
        "original_cross_pairs_zero_mod_5pow16":parity_cross.size,
        "full_D587_even_rows":365,"full_D587_odd_rows":365},flush=True)
    return {
        "even":(old_even,new_even),
        "odd":(old_odd,new_odd)}

def main():
    freeze()
    rho,R,s,j,Q=params(D)
    assert (rho,R,s,j,len(Q))==(53,146,5,5,383)
    assert (-D)%P==3 and MOD==152587890625
    toy=smith_toys()
    C=source_high_precision(Q)
    E,raw_oracle=rebuild_original(C,Q)
    W=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    gram_oracle=sanity_original_gram(E,Q,W)
    by_parity=parity_blocks(E,Q,W)
    result={}
    for parity,(oldids,newids) in by_parity.items():
        old=E[oldids];new=E[newids]
        A=pairings_three_digits(old,old,W)
        assert np.array_equal(A,A.T)
        Ccross=pairings_three_digits(old,new,W)
        print("PHASE297B_HIGH_SMITH_BEGIN",{
            "parity":parity,"n":len(old),"new":len(new),
            "K":K_HI},flush=True)
        x,h=high_precision_smith(A)
        y,g=high_precision_smith(
            np.concatenate((A,Ccross),axis=1))
        assert len(x)==len(y)==len(old)
        assert all(0<=b<=a<=K_HI for a,b in zip(x,y))
        delta=sum(x)-sum(y)
        assert delta>=0
        old_k9=Counter(min(v,9) for v in x)
        aug_k9=Counter(min(v,9) for v in y)
        assert dict(old_k9)==dict(aug_k9)==EXPECTED_K9[parity],(
            "does not reproduce original K9 capped Smith spectrum",
            parity,old_k9,aug_k9)
        assert sum(min(v,9) for v in x)==(
            1720 if parity=="even" else 1715)
        assert sum(min(v,9) for v in y)==(
            1720 if parity=="even" else 1715)
        result[parity]={
            "original_old_rows":len(old),
            "new_original_rows":len(new),
            "precision":K_HI,
            "hist_old_original_Gram":h,
            "hist_old_plus_cross_columns":g,
            "censored_old_Gram_rows_at_K16":h.get(K_HI,0),
            "old_capped_exponent_sum":sum(x),
            "augmented_capped_exponent_sum":sum(y),
            "exact_finite_image_index_log5_at_K16":delta,
            "detected_nonintegral_Z5_projection":bool(delta>0),
            "if_zero_Z5_integrality_still_OPEN":delta==0,
            "minimal_p5_denominator_exponent_lower_bound":
                (delta+len(new)-1)//len(new) if delta else 0,
            "entire_K9_original_smith_hist_replayed":True,
            "NO_new_original_determinant_factor":True,
        }
        print("PHASE297B_PARITY_COKERNEL",{
            "parity":parity,**result[parity]},flush=True)
    total=sum(s["exact_finite_image_index_log5_at_K16"]
              for s in result.values())
    print("PHASE297B_ORIGINAL_SCHUR_INTEGRAL_FRAME_VERDICT",{
        "field":D,
        "original_725_to730_row_attachment":True,
        "unchanged_original_Q":len(Q),
        "all_J5_ordinary_Z_jets_W_fixed":True,
        "original_trace_weights":[2,2*D],
        "modulus":MOD,"K":K_HI,
        "previous_K9_full_original_E_reproduced":True,
        "independent_original_jet_oracle_coordinates":raw_oracle,
        "independent_original_trace_Gram_oracle_entries":gram_oracle,
        "Smith_bigint_negative_and_positive_controls":toy,
        "parity_sector_results":result,
        "log5_new_cross_image_quotient_at_K16":total,
        "nonintegral_projection_if_total_positive":total>0,
        "historical_Schur_det_v5":69,
        "must_NOT_add_image_quotient_to_original_det_v5":True,
        "no_h1_or_uniform_field_theorem":True
    },flush=True)
    print("PASS Phase297-B original D587 Schur p16 image module gate",flush=True)

if __name__=="__main__":
    main()
