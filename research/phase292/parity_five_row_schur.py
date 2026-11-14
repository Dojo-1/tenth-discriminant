#!/usr/bin/env python3
"""Phase292-C: exact D587 725->730 row-Schur p5 increments by C2 parity.

Preregistered b9fe765 BEFORE parity distribution known. Original D587
Q383/J5/B=diag(2,1174) never changes. The n725 cut is a diagnostic.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase281","phase292"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from full_d403_third_layer import smith_profile_k3
from matched_inert5_neighbor import (
    P,K,source_normalized,source_smith_with_row_map,
    independent_rank,metric_gram
)

D=587
BLOBS={
 "research/phase292/matched_inert5_neighbor.py":
       "9216de10f311cf301413de663738804b5fbec203",
 "research/phase292/matched_support_local_field.py":
       "eaa5d2ca3bf5833285cad062110cd612adb1cbb3",
}
HIST_SOURCE={
 "cut_725":{0:625,4:10,5:20,6:70},
 "full_730":{0:625,3:1,4:11,5:21,6:72},
}
HIST_H={
 "cut_725":{"0":690,"1":35,"2":0,">=3":0},
 "full_730":{"0":694,"1":36,"2":0,">=3":0},
}

def guard():
    for path,sha in BLOBS.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("changed parent source",path,actual,sha)

def v5(n):
    n=abs(int(n))
    assert n
    v=0
    while n%P==0:
        n//=P
        v+=1
    return v

def hostile_trace_counterworld():
    a=(1,2,0)
    b=(1,0,0)
    old=2*sum(x*x for x in a)
    cross=2*sum(x*y for x,y in zip(a,b))
    new=2*sum(y*y for y in b)
    det=old*new-cross*cross
    assert (old,cross,new,det)==(10,2,2,16)
    assert old>0 and det>0 and v5(old)==1 and v5(det)==0
    # Positive definite integral Gram row extension DOES NOT guarantee
    # nondecreasing prime-local determinant valuation.
    return {"old_v5":1,"extended_v5":0,"old_det":10,"new_det":16}

def sector(Q,C,ids,parity,S,J):
    n=len(ids)
    assert n>0
    rows=C[ids]
    levels,hist,U=source_smith_with_row_map(rows)
    assert len(levels)==n and max(levels)<=6 and K==9
    assert hist.get(K,0)==0
    index=sum(levels)
    numerator=(U@rows)%(P**K)
    Cp=np.zeros_like(rows)
    for i,e in enumerate(levels):
        assert np.all(numerator[i]%(P**e)==0)
        Cp[i]=(numerator[i]//(P**e))%125
    assert independent_rank(Cp%P)==n
    H=metric_gram(Cp,D,J,Q,125)
    profile=smith_profile_k3(H,P)
    assert profile[">=3"]==0
    assert profile["0"]==independent_rank(H%P)
    residual=profile["1"]+2*profile["2"]
    f=sum(min((ind//S)//P,S-1-(ind%S)) for ind in ids)
    val=2*(f+index)+residual
    return {
      "n":n,"old_F":f,"secondary_index":index,
      "secondary_hist":hist,"primitive_H_K3":profile,
      "primitive_H_v5":residual,"original_sector_G_v5":val,
    },Cp

def evaluate_source(C,Q,R,S,J,label):
    n=R*S
    assert C.shape==(730,3830)
    cut=C[:n,:]
    assert cut.shape==(n,3830)
    even=[i for i in range(n) if ((i//S)+(i%S))%2==0]
    odd=[i for i in range(n) if ((i//S)+(i%S))%2==1]
    assert len(even)+len(odd)==n
    if label=="cut_725":
        assert (R,len(even),len(odd))==(145,363,362)
    else:
        assert (R,len(even),len(odd))==(146,365,365)
    parity=np.array([(-1)**((i//S)+(i%S)) for i in range(n)],
                    dtype=np.int64)
    A=(cut%125).reshape(n,J,len(Q),2)
    for j in range(J):
        assert np.array_equal((parity[:,None,None]*A[:,j])%125,
                              ((-1)**j*A[:,j,::-1,:])%125)

    ev,Cev=sector(Q,cut,even,0,S,J)
    od,Cod=sector(Q,cut,odd,1,S,J)
    B=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    cross=((Cev*(B%125))@Cod.T)%125
    assert cross.shape==(len(even),len(odd))
    assert np.count_nonzero(cross)==0

    h=Counter(ev["secondary_hist"])
    h.update(od["secondary_hist"])
    assert dict(h)==HIST_SOURCE[label],(h,HIST_SOURCE[label])
    h2=Counter(ev["primitive_H_K3"])
    h2.update(od["primitive_H_K3"])
    assert dict(h2)==HIST_H[label],(h2,HIST_H[label])
    total=ev["original_sector_G_v5"]+od["original_sector_G_v5"]
    assert total==({"cut_725":3855,"full_730":3924}[label])
    return {"label":label,"R":R,"rows":n,"original_Q":len(Q),
            "full_original_D587":label=="full_730",
            "even":ev,"odd":od,
            "total_original_trace_Gram_v5":total,
            "all_even_odd_primitive_pairings_zero_mod125":True,
            "full_primitive_profiles_reconstructed_without_row_mixing":True}

def main():
    guard()
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(53,146,5,5,383)
    assert (-D)%P==3
    C,F,hist=source_normalized(D,Q,R,S,J)
    assert F==1360 and hist=={0:166,1:156,2:146,3:136,4:126}
    cut=evaluate_source(C,Q,145,S,J,"cut_725")
    full=evaluate_source(C,Q,146,S,J,"full_730")
    delta={}
    for par in ("even","odd"):
        old=cut[par]
        new=full[par]
        assert new["n"]-old["n"]==(2 if par=="even" else 3)
        dF=new["old_F"]-old["old_F"]
        dI=new["secondary_index"]-old["secondary_index"]
        dH=new["primitive_H_v5"]-old["primitive_H_v5"]
        dV=new["original_sector_G_v5"]-old["original_sector_G_v5"]
        assert 2*(dF+dI)+dH==dV
        delta[par]={"added_original_rows":new["n"]-old["n"],
             "old_F_increase":dF,
             "secondary_index_increase":dI,
             "primitive_residual_v5_change":dH,
             "Schur_sector_det_v5":dV}
    assert delta["even"]["old_F_increase"]==4
    assert delta["odd"]["old_F_increase"]==6
    assert sum(d["secondary_index_increase"] for d in delta.values())==24
    assert sum(d["primitive_residual_v5_change"] for d in delta.values())==1
    assert sum(d["Schur_sector_det_v5"] for d in delta.values())==69
    hostile=hostile_trace_counterworld()

    print("PHASE292C_SOURCE_PARITY",{"cut":cut,"full":full},flush=True)
    print("PHASE292C_FIVE_ROW_SCHUR",{
        "D":D,"actual_Q":len(Q),"old_original_rows":725,
        "full_original_rows":730,"new_original_r":145,
        "unchanged_metric":"diag(2,2D) on all original j,q channels",
        "even_odd_contributions":delta,
        "Schur_total_v5":69,
        "source_exact_gluing_one_field_not_cross_D":True,
        "old_F_and_secondary_and_primitive_counted_once":True,
        "hostile_integral_positive_metric_counterworld":hostile,
        "no_uniform_monotone_p_local_Schur_theorem":True,
        "no_new_tenth_discriminant_field_bound":True,
    },flush=True)
    print("PASS Phase292-C original D587 parity-resolved five-row Schur",flush=True)

if __name__=="__main__":
    main()
