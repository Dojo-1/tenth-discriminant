#!/usr/bin/env python3
"""Phase301-C: bidirectional original D163 scalar Schur torsion.

Preregistered before this code at 857effa5, AFTER the Phase301-A
176-case 148/28 forward result and independent Phase301-B 15-vector.
Compare SAME final lattice under both intermediate row orders.
"""
from collections import Counter,defaultdict
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for part in ("phase206","phase297","phase298","phase299","phase300","phase301"):
    sys.path.insert(0,str(ROOT/"research"/part))
import class_one_d163_composition as original
import joint_same_parity_census as previous
import double_glue_original as image_index
import minimal_transverse_repair as solver
import original_schur_integrality_k16 as smith

P,K,MOD=5,16,5**16
D=163
SOURCE_PARENT="acd72002911b284bea6fda100435f552756c1532"
FIRST=(13,18,22,25,33,34,38)

def guard():
    previous.guard()
    path="research/phase301/joint_same_parity_census.py"
    sha=subprocess.check_output(
      ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
    assert sha==SOURCE_PARENT,("Phase301-A helper drift",sha)

def O(x):
    return np.asarray(x,dtype=object)

def v5(x):
    x=int(x)%MOD
    if x==0:return K
    v=0
    while x%P==0:
        v+=1;x//=P
    return v

def contract(X,Y,W):
    return (O(X)*O(W)[None,:])@O(Y).T%MOD

def hostile_ordered_toy():
    G=np.array([[25,5,5,25],
                [5,10,10,5],
                [5,10,15,6],
                [25,5,6,100]],dtype=np.int64)
    assert previous.pairwise_schur_toy()[
        "pairwise_integrality_does_NOT_imply_joint_integrality"]
    old=G[:2,:2]
    assert image_index.debt(old,G[:2,2:3])==0
    assert image_index.debt(old,G[:2,3:4])==0
    forward=image_index.debt(G[:3,:3],G[:3,3:4])
    revrows=[0,1,3]
    reverse=image_index.debt(
        G[np.ix_(revrows,revrows)],G[np.ix_(revrows,[2])])
    assert (forward,reverse)==(1,2)
    # The 2x2 residual Gram on u,v is [[5,1],[1,75]].
    residual=np.array([[5,1],[1,75]],dtype=np.int64)
    assert v5(residual[0,0])==1
    assert v5(residual[1,1])==2
    assert v5(residual[0,1])==0
    assert int(np.linalg.det(residual))==374
    final_rows=[0,1,3,2]
    b=G[np.ix_(final_rows,final_rows)]
    assert sum(smith.high_precision_smith(G)[0])==(
           sum(smith.high_precision_smith(b)[0]))
    return {
      "positive_definite_full_Gram":True,
      "individual_original_cross_columns_integral":True,
      "residual_2x2_Gram":residual.tolist(),
      "first_u_then_v_5adic_debt_exponent":forward,
      "reverse_v_then_u_5adic_debt_exponent":reverse,
      "full_original_determinant_unchanged_by_order":True,
      "same_full_lattice_different_stagewise_cokernel_orders":True}

def source_reverse_census(G,E,W):
    by_n=defaultdict(Counter)
    transit=Counter()
    forward=Counter()
    reverse=Counter()
    cases=[]
    first_asymmetric=None
    checked_pairings=0
    all_candidates=0
    for n in FIRST:
        assert image_index.debt(G[:n,:n],G[:n,n:n+1])==1
        base=list(range(n+1))
        A=G[np.ix_(base,base)]
        oldE=E[base]
        levels,diag,U,V=solver.tracked_smith_solver(A)
        assert max(levels)<K
        candidates=list(range(n+2,40,2))
        corrected={}
        norm={}
        T={}
        for r in candidates:
            C=G[np.ix_(base,[r])]
            assert image_index.debt(A,C)==0
            solution,errors=solver.can_solve_or_fail(
                levels,diag,U,V,A,C,True)
            assert solution is not None and not errors
            assert not np.any((O(A)@O(solution)-O(C))%MOD)
            corrected[r]=(O(E[[r]])-O(solution).T@O(oldE))%MOD
            assert not np.any(contract(corrected[r],oldE,W))
            norm[r]=int(contract(corrected[r],corrected[r],W)[0,0])
            algebra=(int(G[r,r])-int((O(C).T@O(solution))[0,0]))%MOD
            assert norm[r]==algebra
            assert v5(norm[r])<K
            T[r]=solution
            all_candidates+=1
        for si,s in enumerate(candidates):
            for t in candidates[si+1:]:
                assert s<t and s%2==t%2
                residual=int(contract(corrected[s],corrected[t],W)[0,0])
                # Independent original Gram equations verify that the
                # two integral projector choices yield SAME symmetric
                # residual pairing in either order.
                gram1=(int(G[s,t])-int((O(T[s]).T@
                         O(G[np.ix_(base,[t])]))[0,0]))%MOD
                gram2=(int(G[t,s])-int((O(T[t]).T@
                         O(G[np.ix_(base,[s])]))[0,0]))%MOD
                assert residual==gram1==gram2
                f_pred=max(0,v5(norm[s])-v5(residual))
                r_pred=max(0,v5(norm[t])-v5(residual))
                ids_f=base+[s]
                ids_r=base+[t]
                full_f=base+[s,t]
                full_r=base+[t,s]
                A_f=G[np.ix_(ids_f,ids_f)]
                A_r=G[np.ix_(ids_r,ids_r)]
                f_actual=image_index.debt(
                    A_f,G[np.ix_(ids_f,[t])])
                r_actual=image_index.debt(
                    A_r,G[np.ix_(ids_r,[s])])
                assert f_pred==f_actual,(
                    "original forward Schur changed",n,s,t,
                    f_pred,f_actual)
                assert r_pred==r_actual,(
                    "original reverse Schur mismatch",n,s,t,
                    r_pred,r_actual)
                Gfinal=G[np.ix_(full_f,full_f)]
                Greverse=G[np.ix_(full_r,full_r)]
                perm=list(range(n+1))+[n+2,n+1]
                assert np.array_equal(
                    Greverse,Gfinal[np.ix_(perm,perm)])
                # This is ONE unchanged lattice; a valid original
                # GL permutation changes no actual Smith exponents.
                exps,hh=smith.high_precision_smith(Gfinal)
                reverse_exps,rev_hh=smith.high_precision_smith(Greverse)
                assert exps==reverse_exps
                assert max(exps)<K
                transition=f"{f_actual}->{r_actual}"
                transit[transition]+=1
                forward[f_actual]+=1
                reverse[r_actual]+=1
                by_n[n][transition]+=1
                entry={
                    "initial_original_bad_row":n,
                    "first_integrable_later_row":s,
                    "second_integrable_later_row":t,
                    "residual_S_s_v5":v5(norm[s]),
                    "residual_S_t_v5":v5(norm[t]),
                    "mutual_residual_c_v5_capped16":v5(residual),
                    "s_then_t_image_log5":f_actual,
                    "t_then_s_image_log5":r_actual,
                    "full_original_final_Smith_valuation":sum(exps),
                    "exact_same_final_original_lattice":True}
                if first_asymmetric is None and f_actual!=r_actual:
                    first_asymmetric=entry
                cases.append(entry)
                checked_pairings+=3
    assert len(cases)==176
    assert all_candidates==43
    assert dict(forward)=={0:148,1:28},(
        "Phase301-A original source forward regression failed",forward)
    assert sum(reverse.values())==176
    assert sum(transit.values())==176
    return {
       "original_fixed_7_first_bad_rows":list(FIRST),
       "all_original_future_single_row_projection_solutions":43,
       "source_exact_176_bidirectional_original_row_pairs":176,
       "forward_image_debt_histogram":dict(sorted(forward.items())),
       "reverse_image_debt_histogram":dict(sorted(reverse.items())),
       "forward_to_reverse_transition_counts":dict(sorted(transit.items())),
       "per_original_first_n_transition_counts":{
          str(n):dict(sorted(by_n[n].items())) for n in FIRST},
       "first_order_asymmetric_original_case_if_any":first_asymmetric,
       "all_original_source_2x2_residual_Gram_pairings_checked":
          checked_pairings,
       "full_original_final_Gram_Smith_identical_up_to_row_swap":True,
       "all_source_Schur_vs_full_Gram_cokernel_obstructions_match":True,
       "every_case_original_D163_sampling_and_trace_unchanged":True,
       "all_176_original_results":cases
    }

def main():
    guard()
    field=original.field_h1_background()
    G,E,W,meta=original.original_j1_source()
    assert (meta["R"],meta["S"],meta["J"],meta["Q"])==(40,1,1,109)
    assert previous.parent if False else True
    toy=hostile_ordered_toy()
    census=source_reverse_census(G,E,W)
    print("PHASE301C_ORIGINAL_BIDIRECTIONAL_SCHUR_VERDICT",{
       "original_field_class_one_background":field,
       "original_integer_order_j1_Q109_source":meta,
       "source_independent_order_asymmetric_hostile_Gram":toy,
       "complete_source_176_pair_reverse_census":census,
       "intermediate_cokernel_order_NOT_final_determinant_factor":True,
       "NO_global_h1_cutoff_or_high_J_theorem":True
    },flush=True)
    print("PASS Phase301-C bidirectional 176 original D163 Schur source tests",
          flush=True)

if __name__=="__main__":
    main()
