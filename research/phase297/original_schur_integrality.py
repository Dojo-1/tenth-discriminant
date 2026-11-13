#!/usr/bin/env python3
"""Phase297-A: original D587 725->730 row Schur integrality via p5 coker.

PRE-REGISTERED at d7108a8 BEFORE the executable / CI result.
Exact ORIGINAL monomial/ordinary-Z-jet rows recovered from the fixed
p^-k Frobenius source by reversing its UNDIVIDED unitriangular polynomial
basis. Smith columns are invariant-factor tools ONLY, not metric gauges.
"""
from collections import Counter
from math import comb
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase204","phase281","phase292"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params,gram
from ordinary_jet_filtration import jet
from matched_inert5_neighbor import (
    P,K,k_old,source_normalized,source_smith_with_row_map,
    independent_rank,
)

D=587
S=5
J=5
MOD=P**K
FULL_R=146
CUT_R=145
FROZEN={
    "research/phase206/source_probe.py":
        "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase204/ordinary_jet_filtration.py":
        "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
    "research/phase281/full_d403_third_layer.py":
        "d28b1420a371ca3a8a0297a19ecec75feedfc978",
    "research/phase292/matched_inert5_neighbor.py":
        "9216de10f311cf301413de663738804b5fbec203",
    "research/phase292/parity_five_row_schur.py":
        "dc4b677678759b2d62c8e22a98cc3fbda1b856e9",
}
PROBE_ROWS=[(0,0),(1,0),(5,0),(25,2),(69,3),
            (100,1),(144,4),(145,0),(145,1),(145,2),(145,3),(145,4)]
GRAM_ROWS=[(0,0),(1,1),(5,0),(25,2),(144,4),(145,4)]

def guard():
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("source/helper drift",path,actual,sha)

def valuation(n):
    n=abs(int(n))
    assert n>0
    v=0
    while n%P==0:
        v+=1
        n//=P
    return v

def hostile_toys():
    # 1x1 original Gram A plus one new positive-definite row.
    # All computations valid for all K>=1.
    cases=((10,2,2,1),(10,5,10,0))
    results=[]
    for a,c,d,expected in cases:
        det=a*d-c*c
        assert a>0 and det>0
        ea=min(valuation(a),K)
        eb=min(valuation(__import__("math").gcd(a,c)),K)
        delta=ea-eb
        assert delta==expected
        # A^-1*C is c/a; integrality at p5 iff v5(c)>=v5(a).
        t_integral=valuation(c)>=valuation(a)
        assert t_integral==(delta==0)
        results.append({"old_Gram":a,"cross":c,"new_self":d,
                        "positive_full_Gram_det":det,
                        "v5_det_old":valuation(a),
                        "v5_det_full":valuation(det),
                        "p5_image_index_log":delta,
                        "projection_Z5_integral":t_integral})
    assert results[0]["v5_det_full"]==0
    assert results[0]["v5_det_old"]==1
    return results

def original_rows_from_divided_source(C0,Q):
    """Exact modulo p^9 reverse of the UNDVIDED integral row transform.

    No divided or saturated row is misidentified as an original row.
    For each (r,s), p^k*C0_(r,s) =
        E_(r,s)+sum_(t>=1) (-1)^t binom(k,t) E_(r-5t,s+t).
    """
    n=FULL_R*S
    m=2*J*len(Q)
    assert C0.shape==(n,m)
    raw=np.zeros((n,m),dtype=np.int64)
    normalized_k_hist=Counter()
    for r in range(FULL_R):
        for s in range(S):
            i=r*S+s
            k=k_old(r,s,S)
            normalized_k_hist[k]+=1
            row=(C0[i]*P**k)%MOD
            for t in range(1,k+1):
                j=(r-5*t)*S+(s+t)
                assert 0<=j<i and s+t<S
                coefficient=(-1 if t%2 else 1)*comb(k,t)
                row=(row-coefficient*raw[j])%MOD
            raw[i]=row
    assert dict(normalized_k_hist)=={
        0:166,1:156,2:146,3:136,4:126}
    assert raw.shape==(730,3830)
    # Truly independent integer-original-jet oracle: no Frobenius basis.
    checked=0
    for r,s in PROBE_ROWS:
        for j in range(J):
            for qi in (0,3,len(Q)//2,len(Q)-4,len(Q)-1):
                expected=jet(D,r,s,j,Q[qi])
                col=2*(j*len(Q)+qi)
                observed=(int(raw[r*S+s,col]),int(raw[r*S+s,col+1]))
                assert observed==(expected[0]%MOD,expected[1]%MOD),(
                    "undivided original monomial recovery failure",
                    r,s,j,qi,observed)
                checked+=2
    assert checked==len(PROBE_ROWS)*J*5*2
    return raw,checked

def weights(Q):
    return np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))

def chunked_pairings(X,Y,W,mod=MOD,chunk=128):
    """No signed int64 dot overflows: reduce every 128 columns."""
    assert X.shape[1]==Y.shape[1]==len(W)
    wmax=int(np.max(W))
    bound=chunk*(mod-1)*(mod-1)*wmax
    assert bound<2**63,("int64 chunk dot bound violated",bound)
    out=np.zeros((X.shape[0],Y.shape[0]),dtype=np.int64)
    for start in range(0,len(W),chunk):
        end=min(start+chunk,len(W))
        L=X[:,start:end]%mod
        R=Y[:,start:end]%mod
        weighted=(L*W[start:end])%mod
        out=(out+weighted@R.T)%mod
    # Independence oracle using native Python 64-bit-unbounded ints,
    # not the same numpy matrix multiplication as the source.
    probes=((0,0),(0,Y.shape[0]-1),
            (X.shape[0]-1,0),
            (X.shape[0]//2,Y.shape[0]//2))
    for i,j in probes:
        direct=sum(int(X[i,t])*int(W[t])*int(Y[j,t])
                   for t in range(len(W)))%mod
        assert int(out[i,j])==direct,("weighted Gram drift",i,j)
    return out

def validate_original_gram(E,Q,W):
    inds=[r*S+s for r,s in GRAM_ROWS]
    direct=gram(D,Q,J,GRAM_ROWS)
    actual=chunked_pairings(E[inds],E[inds],W)
    assert all(int(actual[i,j])==int(direct[i][j])%MOD
               for i in range(len(inds)) for j in range(len(inds)))
    return len(inds)**2

def source_parity(Q,E,W):
    n=FULL_R*S
    assert n==730
    assert all(Q[i]==(-Q[len(Q)-1-i][0],-Q[len(Q)-1-i][1])
               for i in range(len(Q)))
    old_even=[i for i in range(CUT_R*S) if ((i//S)+(i%S))%2==0]
    old_odd=[i for i in range(CUT_R*S) if ((i//S)+(i%S))%2==1]
    new_even=[i for i in range(CUT_R*S,n) if ((i//S)+(i%S))%2==0]
    new_odd=[i for i in range(CUT_R*S,n) if ((i//S)+(i%S))%2==1]
    assert (len(old_even),len(old_odd),len(new_even),len(new_odd))==(
        363,362,2,3)
    even=old_even+new_even
    odd=old_odd+new_odd
    # A complete ORIGINAL parity-cross check at p^9, not just mod125
    # of the previously saturated source.
    parity_cross=chunked_pairings(E[even],E[odd],W)
    assert not np.any(parity_cross),(
        "source original C2 symmetry crossed parity modulo p^9",
        int(np.count_nonzero(parity_cross)))
    return {"even":(old_even,new_even),"odd":(old_odd,new_odd)},{
        "cross_parity_pairs_checked":len(even)*len(odd),
        "vanish_mod":MOD}

def gram_and_coker_by_parity(E,Q,W):
    ids,symmetry=source_parity(Q,E,W)
    output={}
    for parity,(oldids,newids) in ids.items():
        old=E[oldids]
        new=E[newids]
        n,r=len(oldids),len(newids)
        A=chunked_pairings(old,old,W)
        assert np.array_equal(A,A.T)
        C=chunked_pairings(old,new,W)
        # The frozen Smith routine works on an arbitrary n×m matrix.
        # It determines row/column INVARIANT FACTORS of its linear map.
        # Never apply any of those internal column operations to B.
        print("PHASE297_SMITH_OLD_BEGIN",{
            "parity":parity,"n":n,"new_rows":r,"precision":K},flush=True)
        ea,ha,_=source_smith_with_row_map(A)
        print("PHASE297_SMITH_AUGMENTED_BEGIN",{
            "parity":parity,"n":n,"new_rows":r,"precision":K},flush=True)
        eb,hb,_=source_smith_with_row_map(
            np.concatenate((A,C),axis=1))
        assert len(ea)==len(eb)==n
        assert all(0<=a<=K and 0<=b<=K and b<=a
                   for a,b in zip(ea,eb))
        delta=sum(ea)-sum(eb)
        assert delta>=0
        assert delta==sum(a-b for a,b in zip(ea,eb))
        assert sum(ha.values())==sum(hb.values())==n
        # Truncated "image debt" is an EXACT finite-cokernel module index.
        # A positive value disproves integral Schur projection over Z5.
        output[parity]={
            "old_original_rows":n,
            "new_original_rows":r,
            "field_D":D,
            "original_full_Q":len(Q),
            "old_Gram_shape":list(A.shape),
            "cross_shape":list(C.shape),
            "smith_exponents_old_hist_K9":ha,
            "smith_exponents_augmented_hist_K9":hb,
            "old_capped_smith_sum":sum(ea),
            "augmented_capped_smith_sum":sum(eb),
            "log5_image_cokernel_index_K9":delta,
            "cross_classes_nonzero_mod5_pow9":bool(delta>0),
            "projection_Z5_nonintegrality_CERTIFIED":bool(delta>0),
            "projection_integrality_if_zero_NOT_PROVED":True,
            "minimum_denominator_power_lower_if_positive":
                (delta+r-1)//r if delta else 0,
            "no_inferred_det_factor":True,
        }
        print("PHASE297_PARITY_IMAGE_COKERNEL",{
            "sector":parity,**output[parity]},flush=True)
    combined=sum(o["log5_image_cokernel_index_K9"]
                 for o in output.values())
    assert all(o["new_original_rows"] in (2,3) for o in output.values())
    return output,symmetry,combined

def main():
    guard()
    rho,R,sourceS,sourceJ,Q=params(D)
    assert (rho,R,sourceS,sourceJ,len(Q))==(53,146,5,5,383)
    assert (-D)%P==3
    toy=hostile_toys()
    C0,F,khist=source_normalized(D,Q,R,sourceS,sourceJ)
    assert F==1360
    assert khist=={0:166,1:156,2:146,3:136,4:126}
    E,checked=original_rows_from_divided_source(C0,Q)
    W=weights(Q)
    independent=validate_original_gram(E,Q,W)
    records,symmetry,index=gram_and_coker_by_parity(E,Q,W)
    assert set(records)=={"even","odd"}
    assert sum(o["new_original_rows"] for o in records.values())==5
    assert sum(o["old_original_rows"] for o in records.values())==725
    assert index>=0
    print("PHASE297_ORIGINAL_INTEGRAL_SCHUR_GATE",{
        "D":D,
        "original_Q":len(Q),
        "original_rows_cut":725,
        "original_rows_full":730,
        "original_ordinary_Z_jets_W_fixed":5,
        "original_trace_metric":[2,2*D],
        "FROBENIUS_ROW_DIVISION_UNDONE":True,
        "integer_original_jet_probe_coordinates":checked,
        "independent_original_trace_Gram_pairs":independent,
        "even_odd_original_Gram_orthogonality":symmetry,
        "K":K,"modulus":MOD,
        "parity_gates":records,
        "total_log5_image_cokernel_index_K9":index,
        "exact_nonintegral_projection_if_index_positive":index>0,
        "historical_full_Schur_v5":69,
        "historical_even_odd_Schur_v5":[28,41],
        "no_double_counting_index_into_original_determinant":True,
        "no_automated_conclusion_beyond_K9_if_index_zero":True,
        "no_uniform_h1_field_or_discriminant_result":True,
        "hostile_positive_Gram_controls":toy
    },flush=True)
    print("PASS Phase297 original D587 integral Schur image-cokernel test",flush=True)

if __name__=="__main__":
    main()
