#!/usr/bin/env python3
"""Phase292-B: matched original support Q383, two different p5 local fields.

Preregistered ed11df6 BEFORE code/results. The D587 r<145
diagnostic is NOT the actual 730-row field-theorem source.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase280","phase281","phase292"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from full_d403_second_layer import first_two_smith
from full_d403_third_layer import smith_profile_k3
from matched_inert5_neighbor import (
    P,K,source_normalized,oracle_exact,
    source_smith_with_row_map,independent_rank,metric_gram
)

BASE_SCRIPT_SHA="9216de10f311cf301413de663738804b5fbec203"
FROZEN_HIST={0:165,1:155,2:145,3:135,4:125}
ORIGINAL_D587_730={"source_index":584,"primitive_residual_v5":36,
                   "original_v5":3924}

def source_guard():
    actual=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase292/matched_inert5_neighbor.py"],
        cwd=ROOT,text=True).strip()
    assert actual==BASE_SCRIPT_SHA,("Phase292 A source changed",actual)
    assert P==5 and K==9

def parity_source(C,R,S,J,Q):
    n=R*S
    assert C.shape==(n,2*J*len(Q))
    assert all(Q[i]==(-Q[-1-i][0],-Q[-1-i][1]) for i in range(len(Q)))
    sign=np.array([(-1)**(r+s) for r in range(R) for s in range(S)],
                  dtype=np.int64)
    A=(C%25).reshape(n,J,len(Q),2)
    for j in range(J):
        assert np.array_equal((sign[:,None,None]*A[:,j])%25,
                              ((-1)**j*A[:,j,::-1,:])%25)
    even=[r*S+s for r in range(R) for s in range(S) if (r+s)%2==0]
    odd=[r*S+s for r in range(R) for s in range(S) if (r+s)%2!=0]
    assert (len(even),len(odd))==(363,362)
    f_even=sum(min(r//P,S-1-s) for r in range(R)
               for s in range(S) if (r+s)%2==0)
    f_odd=sum(min(r//P,S-1-s) for r in range(R)
              for s in range(S) if (r+s)%2!=0)
    assert (f_even,f_odd)==(676,674)
    # The C2 identity applies to the ORIGINAL Frobenius-normalized source
    # independently of the metric parameter; an actual Gram check follows.
    return even,odd

def evaluate_same_rank(D,R,S,J,Q,C,source_kind):
    n=R*S
    assert n==725 and C.shape==(725,3830)
    even,odd=parity_source(C,R,S,J,Q)
    gram25=metric_gram(C,D,J,Q,25)
    assert np.count_nonzero(gram25[np.ix_(even,odd)])==0
    assert np.count_nonzero(gram25[np.ix_(odd,even)])==0
    raw=independent_rank(C%P)
    assert raw<=625 and n-raw>=100
    raw_G=independent_rank(gram25%P)
    assert raw_G<=raw
    first_two=first_two_smith(C%(P**2),P)
    assert first_two["0"]==raw
    levels,hist,U=source_smith_with_row_map(C)
    assert len(levels)==n and sum(hist.values())==n
    assert hist.get(0,0)==raw
    assert first_two["1"]==hist.get(1,0)
    assert first_two[">=2"]==sum(c for e,c in hist.items() if e>=2)
    F=1350
    index_lower=sum(levels)
    result={
        "D":D,"kind":source_kind,"p":P,
        "original_support_point_count":len(Q),
        "original_row_count_if_full":n if source_kind=="original_D583" else 730,
        "rows_actually_tested":n,
        "original_jets":J,"unchanged_observation_columns":C.shape[1],
        "is_full_original_source_for_its_D":source_kind=="original_D583",
        "old_F_on_these_rows_counted_once":F,
        "original_C2_even_odd_rows":[len(even),len(odd)],
        "old_F_even_odd":[676,674],
        "C0_rank_mod5":raw,"C0_Gram_rank_mod5":raw_G,
        "C0_unsaturated_pairing_defect_NOT_ADDITIVE":raw-raw_G,
        "source_first_two_Smith":first_two,
        "source_secondary_K9":hist,
        "source_secondary_index_lower":index_lower,
        "source_secondary_censored_count":hist.get(K,0),
        "tested_source_v5_lower_excluding_primitive":2*(F+index_lower),
    }
    if hist.get(K,0):
        result["primitive_status"]="UNRESOLVED_SOURCE_INDEX"
        return result
    assert sum(levels)==index_lower
    depth=K-max(levels)
    m=P**min(3,depth)
    numer=(U@C)%(P**K)
    primitive=np.zeros_like(C)
    for i,e in enumerate(levels):
        assert np.all(numer[i]%(P**e)==0)
        primitive[i]=(numer[i]//(P**e))%m
    assert independent_rank(primitive%P)==n
    H=metric_gram(primitive,D,J,Q,m)
    rank_H=independent_rank(H%P)
    result.update({"secondary_source_index_exact":index_lower,
        "primitive_rows_full_rank":n,
        "primitive_available_digits":depth,
        "primitive_H_mod5_rank":rank_H,
        "primitive_H_corank_mod5":n-rank_H})
    if rank_H==n:
        residual=0; exact=True
    elif depth>=3:
        prof=smith_profile_k3(H%125,P)
        compare=first_two_smith(H%25,P)
        assert prof["0"]==rank_H==compare["0"]
        assert prof["1"]==compare["1"]
        assert prof["2"]+prof[">=3"]==compare[">=2"]
        residual=prof["1"]+2*prof["2"]+3*prof[">=3"]
        exact=prof[">=3"]==0
        result["primitive_H_K3"]=prof
    elif depth==2:
        prof=first_two_smith(H%25,P)
        residual=prof["1"]+2*prof[">=2"]
        exact=prof[">=2"]==0
        result["primitive_H_K2"]=prof
    else:
        residual=n-rank_H;exact=False
        result["primitive_H_K1"]=dict(unit=rank_H,ge1=residual)
    result["primitive_residual_v5_exact" if exact
           else "primitive_residual_v5_lower"]=residual
    result["tested_source_v5_exact" if exact
           else "tested_source_v5_lower"]=2*(F+index_lower)+residual
    result["not_an_extra_inert_factor_or_uniform_theorem"]=True
    return result

def local_isometry_and_remainder(Q):
    for modulus,alpha in ((5,2),(25,17),(125,67)):
        assert (alpha*alpha*583-587)%modulus==0
        # Trace metric after the p-adic change of imaginary coordinate.
        assert (2*583*alpha*alpha-2*587)%modulus==0
    qset=set(Q)
    assert len(qset)==383
    canonical=lambda t: (t+2)%5-2
    moved={(x,canonical(2*y)) for x,y in Q}
    assert len(moved)==383
    overlap=len(qset.intersection(moved))
    lost=len(moved-qset)
    assert (overlap,lost)==(279,104)
    assert (22,1) in qset and (22,2) not in qset
    assert (22,2) in moved-qset
    return {
      "local_Z5_unit_sqrt_mod5_25_125":[2,17,67],
      "D587_over_D583_local_square_unit":True,
      "mod5_canonical_scaled_coordinate_support_overlap":overlap,
      "original_points_lost_under_mod5_field_isometry":lost,
      "pointwise_counterexample":[22,1],
      "mapped_counterexample":[22,2],
      "same_source_by_isometry_alone":False,
    }

def main():
    source_guard()
    rhoA,RA,SA,JA,QA=params(583)
    rhoB,RB,SB,JB,QB=params(587)
    assert (rhoA,RA,SA,JA,len(QA))==(53,145,5,5,383)
    assert (rhoB,RB,SB,JB,len(QB))==(53,146,5,5,383)
    assert QA==QB
    assert dict(Counter(y for x,y in QA))=={
       -2:43,-1:95,0:107,1:95,2:43}
    assert (-583)%5==2 and (-587)%5==3
    assert 583==11*53 and all(583%(q*q) for q in range(2,25))
    assert 583%4==3 and (583+1)//4==146
    assert len({(x%25,y%25) for x,y in QA})==125
    assert 383>2*(145-1)+4
    local=local_isometry_and_remainder(QA)

    C583,F583,h583=source_normalized(583,QA,RA,SA,JA)
    assert F583==1350 and h583==FROZEN_HIST
    exact=oracle_exact(583,QA,RA,SA,JA,C583)
    assert exact==480
    full=evaluate_same_rank(583,RA,SA,JA,QA,C583,"original_D583")
    full["exact_original_jet_coordinate_checks"]=exact
    print("PHASE292B_FULL_ORIGINAL_D583",full,flush=True)

    C587,F587,h587=source_normalized(587,QB,RB,SB,JB)
    assert F587==1360 and h587=={0:166,1:156,2:146,3:136,4:126}
    assert C587.shape==(730,3830)
    diagnostic=C587[:RA*SA,:]
    # Exactly the SAME row labels 0<=r<145, 0<=s<5, but a
    # DIFFERENT field, metric, and NOT the full D587 row module.
    restricted=evaluate_same_rank(
        587,RA,SA,JA,QB,diagnostic,"D587_725row_diagnostic")
    restricted["previous_full_original_D587"]=ORIGINAL_D587_730
    print("PHASE292B_D587_ROW_RESTRICTED_NOT_FIELD_SOURCE",restricted,flush=True)
    print("PHASE292B_LOCAL_FIELD_TRANSPORT_REMAINDER",local,flush=True)
    print("PASS Phase292-B original D583 and matched 725-row D587 diagnostic",
          flush=True)

if __name__=="__main__":
    main()
