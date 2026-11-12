#!/usr/bin/env python3
"""Phase293-D: fixed-Q-index primitive evaluation intertwiner existence test.

Preregistered 2474a57 BEFORE implementation. A full D583 original
source versus the *first725* original D587 rows only. All 383 original
points, five j-jets, original values and pair metric: no source change.
"""
from collections import Counter
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase292","phase293"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from matched_inert5_neighbor import source_normalized, independent_rank
from primitive_graded_jordan import source_guard, source_sector, parity_rows
from explicit_primitive_isometry_mod125 import inverse_unimodular

P,MOD=5,125
R,S,J=145,5,5

def pivot_columns_mod5(M):
    """Find an independent column basis of a full-row-rank matrix over F5."""
    A=np.asarray(M,dtype=np.int64).copy()%P
    n,m=A.shape
    row=0
    columns=[]
    for col in range(m):
        if row>=n:break
        idxs=np.flatnonzero(A[row:,col])
        if not idxs.size:continue
        at=row+int(idxs[0])
        if at!=row:A[[row,at]]=A[[at,row]]
        scale=pow(int(A[row,col]),-1,P)
        A[row,col:]=(A[row,col:]*scale)%P
        lower=np.flatnonzero(A[row+1:,col])+row+1
        if lower.size:
            A[lower,col:]=(A[lower,col:]
                          -A[lower,col,None]*A[row,col:])%P
        columns.append(col)
        row+=1
    assert row==n and len(columns)==n
    return columns

def exact_row_space_lift(A,B,Q):
    """Try unique X imposed by n pivot original observation columns."""
    A=np.asarray(A,dtype=np.int64)%MOD
    B=np.asarray(B,dtype=np.int64)%MOD
    assert A.shape==B.shape
    n,m=A.shape
    assert m==2*J*len(Q)
    assert independent_rank(A%P)==independent_rank(B%P)==n
    pivots=pivot_columns_mod5(A)
    Ap=A[:,pivots]
    inv=inverse_unimodular(Ap)
    X=(B[:,pivots]@inv)%MOD
    assert np.array_equal((X@Ap)%MOD,B[:,pivots]%MOD)
    residual=(X@A-B)%MOD
    nonzero_p5=np.argwhere(residual%P!=0)
    nonzero_p125=np.argwhere(residual!=0)
    exists_mod5=not nonzero_p5.size
    exists_mod125=not nonzero_p125.size
    assert not exists_mod125 or exists_mod5
    if exists_mod5:
        assert independent_rank(X%P)==n
    witness=None
    if nonzero_p5.size:
        i,c=map(int,nonzero_p5[0])
        j=c//(2*len(Q))
        qi=(c%(2*len(Q)))//2
        ch=c%2
        witness={
           "primitive_row_index":i,
           "ordinary_jet_order":j,
           "original_sample_point":[int(x) for x in Q[qi]],
           "original_Q_index":qi,
           "coordinate_channel":"real" if ch==0 else "imaginary",
           "unique_candidate_prediction_mod5":int((X@A)[i,c]%P),
           "actual_target_mod5":int(B[i,c]%P),
           "residual_mod5":int(residual[i,c]%P)
        }
        assert witness["residual_mod5"]!=0
        assert c not in pivots
    return {
       "primitive_rows":n,"original_obs_channels":m,
       "independent_pivot_columns":len(pivots),
       "all_pivot_columns_replay_mod125":True,
       "any_row_X_with_fixed_Y_over_F5_exists":exists_mod5,
       "any_row_X_with_fixed_Y_mod125_exists":exists_mod125,
       "exact_nonzero_entries_residual_mod5":len(nonzero_p5),
       "exact_nonzero_entries_residual_mod125":len(nonzero_p125),
       "first_mod5_nonmembership_witness":witness,
       "candidate_X_rank_mod5":independent_rank(X%P),
       "no_general_observation_isometry_excluded":True
    }

def toys():
    A=np.array([[1,0,1],[0,1,1]],dtype=np.int64)
    B=np.array([[1,1,2],[1,0,1]],dtype=np.int64)
    # The general solver uses original Q shape; this toy checks exact
    # pivot-source uniqueness independently, without a fake Q mapping.
    piv=pivot_columns_mod5(A)
    assert len(piv)==2
    X=(B[:,piv]@inverse_unimodular(A[:,piv]))%MOD
    assert independent_rank(X%P)==2
    assert np.array_equal((X@A)%MOD,B)
    bad=np.array([[1,0,2],[0,1,1]],dtype=np.int64)
    Y=(bad[:,piv]@inverse_unimodular(A[:,piv]))%MOD
    assert not np.array_equal((Y@A)%P,bad%P)
    return {"positive_full_row_space_toy":True,
            "negative_fixed_pivots_witness_toy":True}

def primitive_sources():
    source_guard()
    a=params(583)
    b=params(587)
    rhoA,RA,SA,JA,Qa=a
    rhoB,RB,SB,JB,Qb=b
    assert (rhoA,RA,SA,JA,len(Qa))==(53,145,5,5,383)
    assert (rhoB,RB,SB,JB,len(Qb))==(53,146,5,5,383)
    assert Qa==Qb
    Ca,fa,_=source_normalized(583,Qa,RA,SA,JA)
    Cb,fb,_=source_normalized(587,Qb,RB,SB,JB)
    assert fa==1350 and fb==1360
    assert Ca.shape==(725,3830) and Cb.shape==(730,3830)
    Cb=Cb[:725,:]  # A DIAGNOSTIC ONLY, not the full D587 field source.
    results={}
    for parity,name in ((0,"even"),(1,"odd")):
        ids=parity_rows(R,S,parity)
        summaryA,primA=source_sector(Ca,583,Qa,R,S,J,ids)
        summaryB,primB=source_sector(Cb,587,Qb,R,S,J,ids)
        assert summaryA["row_count"]==summaryB["row_count"]==len(ids)
        # phi:B->A scales imaginary coords by alpha=67 mod125.
        # Y:A-coordinates->B-coordinates scales imaginary by 28.
        # Check the metric change, not just coordinate symbols.
        assert (67*28)%MOD==1
        assert (28*28*(2*587)-2*583)%MOD==0
        AtoB=primA.copy()
        AtoB[:,1::2]=(AtoB[:,1::2]*28)%MOD
        result=exact_row_space_lift(AtoB,primB,Qa)
        result.update({
          "parity":name,
          "same_actual_original_Q_labels_held_fixed":True,
          "original_field_value_coordinate_Y":"diag(1,28) at each j,q",
          "Y_B587_Yt_equals_B583_mod125":True,
          "field_iso_does_NOT_move_sample_points_in_this_test":True,
          "is_D587_full_730_field_source":False,
        })
        print("PHASE293D_FIXED_Q_ROWSPACE",result,flush=True)
        results[name]=result
    return results,Qa

def main():
    toy=toys()
    results,Q=primitive_sources()
    actual=Counter((x%P,y%P) for x,y in Q)
    moved=Counter((x%P,(2*y)%P) for x,y in Q)
    halfmass=sum(abs(actual[z]-moved[z])
                 for z in actual.keys()|moved.keys())//2
    assert halfmass==104
    assert all(x["primitive_rows"] in (363,362) for x in results.values())
    status={
       "D583_complete_original_row_source":725,
       "D587_FIRST725_only_diagnostic":True,
       "original_sample_points":len(Q),
       "metric_value_coordinate_Y_mod125":[1,28],
       "parity_sectors":results,
       "actual_point_residue_multiplicity_mismatch_mass":halfmass,
       "toys":toy,
       "fixed_label_row_space_square_mod5_exists_in_BOTH":all(
           results[par]["any_row_X_with_fixed_Y_over_F5_exists"]
           for par in ("even","odd")),
       "no_other_observation_Y_or_class_one_theorem_decided":True
    }
    print("PHASE293D_FIXED_LABEL_SQUARE_VERDICT",status,flush=True)
    print("PASS Phase293-D original-Q indexed field-coordinate source lift gate",flush=True)

if __name__=="__main__":
    main()
