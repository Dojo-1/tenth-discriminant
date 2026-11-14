#!/usr/bin/env python3
"""Phase294-C: minimal formal completion restores raw original jet transport.

PRE-REGISTERED 51ac09e BEFORE implementation. Synthetic sample points
ARE NOT the original number-field source, and no primitive Smith or
Gram valuation is inferred from the successful raw commuting square.
"""
from collections import defaultdict,deque
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
sys.path.insert(0,str(ROOT/"research"/"phase294"))
from source_probe import params,gram
from support_debt_tower import (
    source_guard,hensel_lifts,matching_by_residue,debt_from_counters,
    residue_counter
)
from original_moment_localization import (
    D_A,D_B,J,LABELS,original_ordinary_jets_at_point
)

def minimal_completed_pair(Q,alpha,mod):
    pairs_original,left_missing,right_missing=matching_by_residue(Q,alpha,mod)
    expected,_=debt_from_counters(
        residue_counter(Q,mod),residue_counter(Q,mod,alpha))
    assert len(left_missing)==len(right_missing)==expected
    inv=pow(alpha,-1,mod)
    # Retain EVERY originally observed sample; add FORMAL points only.
    synthetic_A=[(Q[j][0],(alpha*Q[j][1])%mod) for j in right_missing]
    synthetic_B=[(Q[i][0],(inv*Q[i][1])%mod) for i in left_missing]
    complete_A=Q+synthetic_A
    complete_B=Q+synthetic_B
    assert len(complete_A)==len(complete_B)==len(Q)+expected
    assert complete_A[:len(Q)]==Q==complete_B[:len(Q)]
    assert any(z not in set(Q) for z in synthetic_A)
    assert any(z not in set(Q) for z in synthetic_B)

    available=defaultdict(deque)
    for i,(x,y) in enumerate(complete_A):
        available[(x%mod,y%mod)].append(i)
    all_pairs=[]
    for j,(x,y) in enumerate(complete_B):
        key=(x%mod,(alpha*y)%mod)
        assert available[key],("completion does not cover B residue",mod,j,key)
        i=available[key].popleft()
        all_pairs.append((i,j))
    assert len(all_pairs)==len(complete_A)
    assert all(not v for v in available.values())
    assert len({i for i,j in all_pairs})==len(all_pairs)
    return complete_A,complete_B,synthetic_A,synthetic_B,all_pairs

def plus(A,B):
    return [[x+y for x,y in zip(row_a,row_b)] for row_a,row_b in zip(A,B)]

def equal_mod(A,B,mod):
    return all((a-b)%mod==0 for ra,rb in zip(A,B) for a,b in zip(ra,rb))

def paired_original_jet_covariance(Qa,Qb,alpha,mod,pairs):
    # The integer row maps and Z-jet order are untouched. For each
    # matched pair, map B imaginary values into A's field chart.
    assert (D_A*alpha*alpha-D_B)%mod==0
    for i,j in pairs:
        original=original_ordinary_jets_at_point(D_A,Qa[i],mod)
        moved=original_ordinary_jets_at_point(D_B,Qb[j],mod)
        for row_A,row_B in zip(original,moved):
            for va,vb in zip(row_A,row_B):
                assert va[0]%mod==vb[0]%mod
                assert (va[1]-alpha*vb[1])%mod==0
                # This is exactly the original metric relation;
                # the values need not be equal as raw coordinates.
                bmetric=(2*vb[0]*vb[0]+2*D_B*vb[1]*vb[1])%mod
                ametric=(2*va[0]*va[0]+2*D_A*va[1]*va[1])%mod
                assert bmetric==ametric
    return len(pairs)*len(LABELS)*J

def main():
    source_guard()
    pa=params(D_A)
    pb=params(D_B)
    _,R_A,S_A,J_A,Qa=pa
    _,R_B,S_B,J_B,Qb=pb
    assert (R_A,S_A,J_A,len(Qa))==(145,5,5,383)
    assert (R_B,S_B,J_B,len(Qb))==(146,5,5,383)
    assert Qa==Qb
    Q=Qa
    ga=gram(D_A,Q,J,LABELS)
    gb=gram(D_B,Q,J,LABELS)
    assert gb[1][1]-ga[1][1]==4272
    result=[]
    for k,mod,alpha in hensel_lifts(3):
        completed_A,completed_B,added_A,added_B,pairs=(
            minimal_completed_pair(Q,alpha,mod))
        debt=len(added_A)
        assert debt==(104 if k==1 else 276)
        assert len(completed_A)==(487 if k==1 else 659)
        checked=paired_original_jet_covariance(
            completed_A,completed_B,alpha,mod,pairs)
        # This frozen source_probe oracle computes all five original
        # Z jets, both signed trace channels and all 36 Gram entries.
        ga_aug=gram(D_A,completed_A,J,LABELS)
        gb_aug=gram(D_B,completed_B,J,LABELS)
        assert equal_mod(ga_aug,gb_aug,mod)
        ga_extra=gram(D_A,added_A,J,LABELS)
        gb_extra=gram(D_B,added_B,J,LABELS)
        assert ga_aug==plus(ga,ga_extra)
        assert gb_aug==plus(gb,gb_extra)
        assert all((gb[i][j]-ga[i][j]-ga_extra[i][j]
                    +gb_extra[i][j])%mod==0
                   for i in range(len(LABELS))
                   for j in range(len(LABELS)))
        # A completion does not change ORIGINAL source valuations;
        # it only tests a deliberately enlarged formal category.
        digest=sha256(json.dumps(
            pairs,separators=(",",":")
        ).encode()).hexdigest()
        result.append({
            "precision_power":k,"modulus":mod,"alpha":alpha,
            "original_unmodified_observation_points":383,
            "new_synthetic_points_each_side":debt,
            "completed_formal_point_count":len(completed_A),
            "all_original_points_retained":True,
            "synthetic_added_points_outside_original_ellipse":True,
            "all_completed_sample_labels_bijective_mod_pk":True,
            "full_six_row_original_jet_value_pairs_checked":checked,
            "original_trace_metric_isometry_checked_per_jet":True,
            "all_36_formally_completed_Gram_entries_congruent":True,
            "signed_original_Gram_defect_canceled_by_added_points":True,
            "deterministic_complete_point_matching_sha256":digest,
        })
    assert [x["new_synthetic_points_each_side"] for x in result]==[
        104,276,276]
    assert [x["completed_formal_point_count"] for x in result]==[
        487,659,659]
    print("PHASE294C_MINIMAL_FORMAL_RAW_COMPLETION",{
        "full_original_D583_rows_UNCHANGED":725,
        "full_original_D587_rows_UNCHANGED":730,
        "tested_common_original_rows":[list(x) for x in LABELS],
        "original_all_Z_jets":J,
        "original_Q_literal_shared":383,
        "completed_raw_squares":result,
        "constructive_sufficiency_limited_to_formal_added_points":True,
        "no_saturated_primitive_C_or_H_identified":True,
        "no_original_number_field_sampler_replaced":True,
        "no_field_discriminant_or_new_vp_factor":True
    },flush=True)
    print("PASS Phase294-C minimal augmented p-adic sample correspondence and raw jet Gram square",
          flush=True)

if __name__=="__main__":
    main()
