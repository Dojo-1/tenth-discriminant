#!/usr/bin/env python3
"""Phase304-C: true original D203 J2 primitive trace Gram and source radical.

Separately preregistered at 41c2c7d9 AFTER B original evidence,
BEFORE this code. Frozen B code, actual source rho24/R50/J2/Q
and p5^16 original Gram. Primitive G has precision p5^15.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase297","phase304"):
    sys.path.insert(0,str(ROOT/"research"/p))
import highjet_d203_original as pilot
from original_schur_integrality_k16 import high_precision_smith

MOD=5**16
LOW=5**15
N=100
FROZEN_PILOT="901d01dc084dd51235d659c2248fec49c89db06e"

def guard():
    pilot.guard()
    p="research/phase304/highjet_d203_original.py"
    actual=subprocess.check_output(
        ["git","rev-parse","HEAD:"+p],cwd=ROOT,text=True).strip()
    assert actual==FROZEN_PILOT,("Phase304-B reference drift",actual)

def independent_image_basis(E):
    """Separate plain F5 row echelon to identify actual source image basis."""
    pivots={}
    indices=[]
    for idx,raw in enumerate(E):
        r=[int(z)%5 for z in raw]
        for col in sorted(pivots):
            c=r[col]
            if c:
                pr=pivots[col]
                for j in range(col,len(r)):
                    r[j]=(r[j]-c*pr[j])%5
        pivot=next((j for j,z in enumerate(r) if z),None)
        if pivot is not None:
            iv=pow(r[pivot],-1,5)
            for j in range(pivot,len(r)):
                r[j]=r[j]*iv%5
            pivots[pivot]=r
            indices.append(idx)
    return indices

def source_primitive_audit(E,G,Q,J,arm):
    assert E.shape==(N,2*J*Q)
    U=np.eye(N,dtype=object)
    rows=[]
    for r in range(5,50):
        i=2*r
        U[i,2*(r-5)+1]-=1
        rows.append(i)
    assert len(rows)==45
    old=np.asarray(E,dtype=object)
    transformed=(U@old)%MOD
    assert not np.any(transformed[rows,:]%5)
    primitive=np.asarray(transformed,dtype=object)
    for i in rows:
        primitive[i,:]=(primitive[i,:]//5)%LOW
    Gprim=pilot.original_trace_gram(
        np.asarray(primitive,dtype=np.int64),Q,J,LOW)
    UG=(U@np.asarray(G,dtype=object)@U.T)%MOD
    selected=set(rows)
    for i in range(N):
        for j in range(N):
            factor=(5 if i in selected else 1)*(
                5 if j in selected else 1)
            right=(factor*int(Gprim[i,j]))%MOD if factor>1 else int(G[i,j])
            assert int(UG[i,j])==right%MOD
    source_levels,source_hist=high_precision_smith(G,K=16)
    assert max(source_levels)<16
    primitive_levels,primitive_hist=high_precision_smith(Gprim,K=15)
    assert max(primitive_levels)<15,(
        "original primitive Smith censored at prereg precision",arm)
    v_orig=sum(source_levels)
    v_prim=sum(primitive_levels)
    assert v_orig==90+v_prim
    erank=pilot.rank_F5(primitive)
    grank=pilot.rank_F5(Gprim)
    idx=independent_image_basis(primitive)
    assert len(idx)==erank
    restricted=Gprim[np.ix_(idx,idx)]
    restriction_rank=pilot.rank_F5(restricted)
    assert restriction_rank==grank
    # Source E: R^100 -> ambient original (2 jets)*(2 coords)*Q.
    # Metric Bomega is unit mod5: det [[2,1],[1,102]]=203≡3.
    assert (2*102-1)%5==3
    rank_kernel=N-erank
    radical=erank-restriction_rank
    assert rank_kernel+radical+grank==N
    original_eval_rank=pilot.rank_F5(E)
    original_gram_rank=pilot.rank_F5(G)
    assert original_eval_rank-original_gram_rank>=0
    assert N-original_eval_rank+(
        original_eval_rank-original_gram_rank
    )+original_gram_rank==N
    excess=v_prim-(N-grank)
    assert excess>=0
    if arm=="old":
        assert (v_orig,v_prim,erank,grank,rank_kernel,radical)==(
             252,162,60,42,40,18)
    else:
        assert (v_orig,v_prim,erank,grank,rank_kernel,radical)==(
             138,48,95,58,5,37)
    return {
        "actual_original_source":arm,
        "original_source_Q":Q,
        "original_R":50,"original_S_and_J":J,
        "original_100row_p16_full_Smith_profile":source_hist,
        "original_100row_v5_det":v_orig,
        "original_45_divisible_Frobenius_rows":len(rows),
        "original_index_square_v5_contribution":90,
        "primitive_100row_K15_full_Smith_profile":primitive_hist,
        "primitive_residual_v5_det":v_prim,
        "primitive_source_E_mod5_image_rank":erank,
        "primitive_source_Gram_mod5_rank":grank,
        "restricted_trace_Gram_rank_on_independent_image_basis":
            restriction_rank,
        "actual_primitive_source_evaluation_kernel_dimension":
            rank_kernel,
        "primitive_trace_image_radical_dimension":radical,
        "primitive_Gram_mod5_kernel_total_dimension":N-grank,
        "higher_valuation_beyond_one_per_positive_primitive_level":excess,
        "original_undivided_evaluation_rank_mod5":original_eval_rank,
        "original_undivided_trace_Gram_rank_mod5":original_gram_rank,
        "original_undivided_trace_image_radical_dimension":
            original_eval_rank-original_gram_rank,
        "all_10000_original_U_G_vs_D5_Gprim_D5_entries_checked":10000,
        "not_a_new_field_class_number_bound_or_extra_original_mass":True
    }

def main():
    guard()
    rho,R,S,J,Qold=pilot.params(pilot.D)
    assert (rho,R,S,J)==(24,50,2,2)
    full=pilot.qmax(rho)
    even=[q for q in full if q[1]%2==0]
    assert len(even)==len(Qold)==127 and len(full)==263
    Eo=pilot.evaluate_original_jets(even,R,S,J,MOD)
    Ef=pilot.evaluate_original_jets(full,R,S,J,MOD)
    Go=pilot.original_trace_gram(Eo,len(even),J,MOD)
    Gf=pilot.original_trace_gram(Ef,len(full),J,MOD)
    old=source_primitive_audit(Eo,Go,len(even),J,"old")
    maximal=source_primitive_audit(Ef,Gf,len(full),J,"maximal")
    print("PHASE304C_ORIGINAL_D203_J2_PRIMITIVE_TRACE_RADICAL",{
       "old_source":old,
       "full_maximal_source":maximal,
       "separate_original_source_evaluation_kernel_from_trace_radical":True,
       "beyond_45_Frobenius_first_level_higher_jet_obstruction":True,
       "no_source_policy_change_or_h1_inference":True
    },flush=True)
    print("PASS Phase304-C J2 original source primitive Gram and trace radical",flush=True)

if __name__=="__main__":
    main()
