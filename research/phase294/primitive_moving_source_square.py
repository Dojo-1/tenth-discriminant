#!/usr/bin/env python3
"""Phase294-C: parity-preserving primitive source square on MOVED Q.

Preregistered e058423 BEFORE code. In synchronized p5-Smith frames,
all 725x3830 primitive source entries are transported mod125 by a
genuine p-adic field-value map WITH MOVED original observation points.
The ORIGINAL D583 Q is NOT this formal moved source.
"""
from collections import Counter
import hashlib
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase281","phase292","phase294"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from full_d403_third_layer import smith_profile_k3
from matched_inert5_neighbor import (
    source_normalized,source_smith_with_row_map,
    independent_rank,metric_gram,oracle_exact
)
from moving_normalized_field_chart import (
    original_guard,hensel_alpha,MOD,Q_MOD,K_NUM
)

D_A,D_B=583,587
P,K,R,S,J=5,9,145,5,5
EXPECTED_SRC={0:625,4:10,5:20,6:70}
EXPECTED_H={"0":690,"1":35,"2":0,">=3":0}
BLOB_PARENT="79bc80f9cc1f28129762bcc828576b86932c27e3"

def guard():
    original_guard()
    actual=subprocess.check_output(
        ["git","rev-parse",
         "HEAD:research/phase294/moving_normalized_field_chart.py"],
        cwd=ROOT,text=True
    ).strip()
    assert actual==BLOB_PARENT,("parent moving-source oracle changed",actual)

def source_parity_labels(parity):
    return [r*S+s for r in range(R) for s in range(S)
            if (r+s)%2==parity]

def synchronized_saturation(B,A,alpha,ids):
    """Compute source U,e ONLY from B and apply both to ORIGINAL columns."""
    assert B.shape==A.shape==(len(ids),3830)
    levels,hist,U=source_smith_with_row_map(B)
    assert len(levels)==len(ids) and max(levels)==6
    assert hist.get(K,0)==0
    precision=P**K
    VB=(U@B)%precision
    VA=(U@A)%precision
    assert len(levels)==VB.shape[0]
    cpB=np.zeros_like(B)
    cpA=np.zeros_like(A)
    for i,e in enumerate(levels):
        div=P**e
        assert e+3<=K
        assert np.all(VB[i]%div==0)
        assert np.all(VA[i]%div==0)
        cpB[i]=(VB[i]//div)%125
        cpA[i]=(VA[i]//div)%125
    YA=cpB.copy()
    YA[:,1::2]=(YA[:,1::2]*(alpha%125))%125
    assert np.array_equal(cpA,YA),(
        "source square failed after compatible p5-Smith normalization"
    )
    assert independent_rank(cpA%P)==independent_rank(cpB%P)==len(ids)
    def digest(C):
        return hashlib.sha256(C.astype(np.uint8).tobytes()).hexdigest()
    result={
        "original_row_parity":"even" if ids[0]==0 else "odd",
        "rows":len(ids),
        "secondary_source_index":sum(levels),
        "secondary_Smith_hist":hist,
        "max_secondary_exponent":max(levels),
        "synchronized_source_row_map_units_mod5":True,
        "same_original_observation_columns_retained":3830,
        "all_primitive_source_entries_covariant_mod125":cpA.size,
        "field_value_chart_alpha_mod125":alpha%125,
        "primitive_source_A_moved_SHA256":digest(cpA),
        "primitive_source_B_original_SHA256":digest(cpB),
    }
    return result,cpA,cpB

def original_trace_cross(even,odd,D,Q):
    weights=np.tile(np.array((2,2*D),dtype=np.int64),J*len(Q))%125
    assert even.shape[1]==odd.shape[1]==len(weights)==3830
    C=((even*weights)%125@odd.T)%125
    assert np.count_nonzero(C)==0,(
        "original central inversion metric cross sector drift",
        int(np.count_nonzero(C))
    )
    return C.shape[0]*C.shape[1]

def main():
    guard()
    alpha=hensel_alpha()
    assert K_NUM==13 and K==9 and (alpha%5,alpha%25,alpha%125)==(2,17,67)
    qa=params(D_A)
    qb=params(D_B)
    assert qa[:4]==(53,145,5,5)
    assert qb[:4]==(53,146,5,5)
    Q=qb[4]
    assert qa[4]==Q and len(Q)==383
    moved=[(x,(alpha*y)%Q_MOD) for x,y in Q]
    assert len(set(moved))==383
    # Matrix B is still the first725 row *diagnostic*, never n730.
    C_B,F_B,old_B=source_normalized(D_B,Q,R,S,J)
    C_A,F_A,old_A=source_normalized(D_A,moved,R,S,J)
    assert (F_A,F_B)==(1350,1350)
    assert old_A==old_B=={0:165,1:155,2:145,3:135,4:125}
    assert C_A.shape==C_B.shape==(725,3830)
    assert oracle_exact(D_A,moved,R,S,J,C_A)==480
    assert oracle_exact(D_B,Q,R,S,J,C_B)==480

    raw_chart=C_B.copy()
    raw_chart[:,1::2]=(raw_chart[:,1::2]*alpha)%MOD
    assert np.array_equal(raw_chart,C_A),(
        "previous Phase294-B normalized source full identity failed"
    )
    assert (D_A*alpha*alpha-D_B)%Q_MOD==0

    parts={}
    prim_A={}
    prim_B={}
    source_hist=Counter()
    primitive_hist=Counter()
    for parity,name in ((0,"even"),(1,"odd")):
        ids=source_parity_labels(parity)
        assert len(ids)==(363 if parity==0 else 362)
        res,PA,PB=synchronized_saturation(C_B[ids],C_A[ids],
                                          alpha,ids)
        assert res["original_row_parity"]==name
        assert all((r%S+(r//S))%2==parity for r in ids)
        f=sum(min((i//S)//P,S-1-i%S) for i in ids)
        assert f==(676 if parity==0 else 674)
        res["already_counted_old_F"]=f
        source_hist.update(res["secondary_Smith_hist"])
        prim_A[name],prim_B[name]=PA,PB
        HA=metric_gram(PA,D_A,J,moved,125)
        HB=metric_gram(PB,D_B,J,Q,125)
        assert np.array_equal(HA,HB),(
            "original trace metric covariance failed on primitive source"
        )
        prof=smith_profile_k3(HB,P)
        assert prof[">=3"]==0
        assert prof["0"]==(345 if parity==0 else 345)
        assert prof["1"]==(18 if parity==0 else 17)
        assert prof["2"]==0
        primitive_hist.update(prof)
        res.update({
           "primitive_metric_Gram_full_sector_equality_mod125":True,
           "primitive_H_Smith_existing_histogram":prof,
           "primitive_H_first_grade_rank_mod5":prof["0"],
           "primitive_H_residual_index_ALREADY_counted":prof["1"],
        })
        parts[name]=res
        print("PHASE294C_PRIMITIVE_SECTOR",res,flush=True)

    assert dict(source_hist)==EXPECTED_SRC
    assert dict(primitive_hist)==EXPECTED_H
    assert sum(x["secondary_source_index"] for x in parts.values())==560
    assert sum(x["already_counted_old_F"] for x in parts.values())==1350
    assert sum(x["primitive_H_residual_index_ALREADY_counted"]
               for x in parts.values())==35
    # Independent full row rank across sectors (the parity eigenspaces
    # are complementary because the characteristic is NOT 2).
    assert independent_rank(np.vstack((
        prim_B["even"],prim_B["odd"]))%P)==725
    assert independent_rank(np.vstack((
        prim_A["even"],prim_A["odd"]))%P)==725
    cross_B=original_trace_cross(prim_B["even"],prim_B["odd"],D_B,Q)
    cross_A=original_trace_cross(prim_A["even"],prim_A["odd"],D_A,moved)
    assert cross_A==cross_B==363*362
    assert 2*(1350+560)+35==3855  # prior, no new valuation

    # Hostile fixed-support negative: ordinary row Z, j0, original
    # q=(22,1) has imaginary source coefficient1 versus 2 in moved chart.
    qi=Q.index((22,1))
    irow=1*S
    icoord=2*qi+1
    assert C_B[irow,icoord]%P==1
    assert C_A[irow,icoord]%P==2
    assert (alpha-1)%P==1
    assert 5%5==10%5 and (5//5)%5!=(10//5)%5
    original_delta=Counter((x%P,y%P) for x,y in Q)
    transformed=Counter((x%P,(2*y)%P) for x,y in Q)
    L1=sum(abs(original_delta[z]-transformed[z])
           for z in original_delta.keys()|transformed.keys())//2
    assert L1==104

    print("PHASE294C_FULL_PRIMITIVE_MOVING_SUPPORT_SQUARE",{
      "D_A_original_full_rows":725,
      "D_A_support":"FORMAL PHI(Q_B), NOT ORIGINAL Q_A",
      "D_B_original_full_rows":730,
      "D_B_used_FIRST725_only_diagnostic":True,
      "all_original_points_Q_B":383,
      "all_original_j_orders":[0,1,2,3,4],
      "original_value_columns":3830,
      "prior_Hensel_source_precision":"p^13 numerator, p^9 normalized",
      "all_synchronized_primitive_entries_mod125":725*3830,
      "source_row_basis_parity_preserved":True,
      "old_F_counted_once":1350,
      "secondary_index_counted_once":560,
      "primitive_H_residual_valuation_counted_once":35,
      "previous_same_moved_form_v5_not_an_extra_factor":3855,
      "correct_previous_secondary_Smith_hist":dict(source_hist),
      "correct_previous_primitive_Smith_hist":dict(primitive_hist),
      "both_primitive_H_parity_cross_entries_zero_mod125":True,
      "parity_cross_entries_replayed_each_side":cross_A,
      "source_row_X_is_identity_IN_SYNCHRONIZED_PRIMITIVE_FRAMES":True,
      "field_value_Y_is_diagonal_and_metric_preserving":True,
      "unmoved_original_Q_support_mass":L1,
      "can_transport_original_unmoved_D583_source":False,
      "class_one_or_uniform_discriminant_theorem":False,
    },flush=True)
    print("PASS Phase294-C original n725 primitive source square on FORMAL MOVED Q",flush=True)

if __name__=="__main__":
    main()
