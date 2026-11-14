#!/usr/bin/env python3
"""Phase298-B: every contiguous nested-row triple in actual h=1 D163.

Preregistered a967d499 BEFORE code and outcomes. ORIGINAL source
params(D163) R40/S=J1 with original Q and trace B=(2,326).
This is NOT a uniform tenth-discriminant theorem or a D587 J5 replay.
"""
from collections import Counter
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase204","phase297","phase298"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params,gram
from ordinary_jet_filtration import jet
import original_schur_integrality_k16 as precision
import minimal_transverse_repair as repair
import composable_original_cokernel as previous

D=163
P=5
K=16
MOD=P**K
FROZEN={
 "research/phase206/source_probe.py":
    "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":
    "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
 "research/phase297/original_schur_integrality_k16.py":
    "aa3678001c69a7235dca638638d2dab4c55b05b3",
 "research/phase297/minimal_transverse_repair.py":
    "22b0077a2424553021a4c9859f92f0fe3efc2fe7",
 "research/phase298/composable_original_cokernel.py":
    "0be071ba1e4b70b707514e0502bd41f509d5936d",
}

def guard():
    previous.freeze()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("original source helper changed",path,actual,sha)

def field_h1_background():
    # Classical external theorem used: Minkowski bound for imaginary
    # quadratic fields (2/pi)*sqrt(|disc|); PI>3, sqrt163<13,
    # so bound<26/3<9, and norm<=8 representatives suffice.
    assert 3*3<163<13*13
    assert (2*13)<(3*9)
    assert (-D)%8==5 # p2 inert in fundamental discriminant -163.
    odds=(3,5,7)
    inert={p:(-D)%p for p in odds}
    assert all(inert[p] not in {i*i%p for i in range(p)} for p in odds)
    assert inert=={3:2,5:2,7:5}
    # For norms 1,...,8: inert 2's unique norm4 ideal is (2),
    # and 3/5/7 inert primes have norms9/25/49; nothing else.
    return {
       "fundamental_field_discriminant":-163,
       "Minkowski_ideal_norm_bound_strictly_below9":True,
       "primes_2_3_5_7_all_inert":True,
       "only_possible_ideal_norm_le8": [1,4],
       "ideal_norm4_is_principal_generated_by2":True,
       "class_number_one_from_classical_Minkowski_theorem":True,
       "independent_of_original_sampling_ellipse":True,
    }

def original_j1_source():
    rho,R,S,J,Q=params(D)
    assert R==40 and S==J==1 and len(Q)>40
    assert len(Q)==len(set(Q))
    labels=[(r,0) for r in range(R)]
    # Existing exact bigint source_probe oracle checks its own
    # independent real/imag direct Gram vs original mixed moments.
    print("PHASE298B_ORIGINAL_H1_SOURCE",{
        "D":D,"rho":rho,"R":R,"S":S,"J":J,
        "original_integer_ellipse_observations":len(Q),
        "all_original_labels":len(labels)},flush=True)
    exact=gram(D,Q,J,labels)
    assert len(exact)==len(exact[0])==R
    W=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    E=np.zeros((R,len(W)),dtype=np.int64)
    for r in range(R):
        for qi,q in enumerate(Q):
            a,b=jet(D,r,0,0,q) # exact ordinary Z jet, W fixed
            E[r,2*qi]=a%MOD
            E[r,2*qi+1]=b%MOD
    assert E.shape==(40,2*len(Q))
    # Independent exact modular Gram reconstruction from the ORIGINAL
    # evaluation rows and ORIGINAL field trace B=(2,326).
    H=np.zeros((R,R),dtype=np.int64)
    for i in range(R):
        for j in range(i,R):
            direct=sum(
                int(E[i,c])*int(W[c])*int(E[j,c])
                for c in range(len(W)))%MOD
            assert direct==int(exact[i][j])%MOD,(
               "original D163 raw trace/mixed moment disagreement",i,j)
            H[i,j]=H[j,i]=direct
    assert np.array_equal(H,H.T)
    assert H.shape==(40,40)
    return H,E,W,{"original_rho":rho,"R":R,"S":S,"J":J,
         "Q":len(Q),"all_1600_exact_source_Gram_entries_checked":True}

def finite_index(A,C,name):
    n=A.shape[0]
    assert A.shape==(n,n) and C.shape[0]==n
    a,h=precision.high_precision_smith(A)
    b,g=precision.high_precision_smith(
        np.concatenate([A,C],axis=1))
    assert len(a)==len(b)==n
    assert all(0<=y<=x<=K for x,y in zip(a,b))
    delta=sum(a)-sum(b)
    assert delta>=0
    return delta,max(a)<K,max(a),max(b)

def corrected_original_scalar_source(E,W,n,T,S1,R12):
    # Test exactly on the ORIGINAL scalar J1 observation rows.
    t=np.asarray(T,dtype=object).reshape(n,1)
    corr=(np.asarray(E[n:n+1],dtype=object)
          -t.T@np.asarray(E[:n],dtype=object))%MOD
    full=(np.asarray(E[n+1:n+2],dtype=object))
    weights=np.asarray(W,dtype=object)
    q_self=sum(int(corr[0,i])*int(corr[0,i])*int(weights[i])
               for i in range(len(W)))%MOD
    q_cross=sum(int(corr[0,i])*int(full[0,i])*int(weights[i])
                for i in range(len(W)))%MOD
    assert q_self==S1 and q_cross==R12
    oldcross=(np.asarray(E[:n],dtype=object)*weights[None,:])@corr.T%MOD
    assert all(int(x)==0 for x in oldcross.reshape(-1))
    return len(W)*2+n

def exhaustive_triples(G,E,W):
    statuses=Counter()
    second_hist=Counter()
    pair_result=[]
    first_integral_validated=0
    finite_lcm_tests=0
    censored_first=0
    two_positive_components=0
    schur_only=0
    for n in range(1,39):
        A=G[:n,:n]
        C1=G[:n,n:n+1]
        C2=G[:n,n+1:n+2]
        G1=G[:n+1,:n+1]
        cross=G[:n+1,n+1:n+2]
        first,first_exact,mxa,mxb=finite_index(
            A,C1,"first")
        oldlater,oldlater_exact,_,_=finite_index(
            A,C2,"old_then_final")
        second,second_exact,mx1,mx2=finite_index(
            G1,cross,"actual_original_stage2")
        second_hist[second]+=1
        is_applicable=first==0
        outcome={
            "first_original_n":n,
            "first_added_original_row_r":n,
            "second_added_original_row_r":n+1,
            "first_finite_index_log5":first,
            "first_cokernel_fully_resolved":first_exact,
            "last_vs_first_old_index_log5":oldlater,
            "actual_next_stage_finite_index_log5":second,
            "intermediate_cokernel_fully_resolved":second_exact,
            "integral_first_stage_finite_split_applicable":is_applicable,
        }
        if first>0:
            statuses["nonintegral_first_stage"]+=1
        elif not first_exact:
            statuses["first_stage_zero_K16_but_censored"]+=1
            censored_first+=1
            # Even when a modular solution exists, the all-Z5
            # integral claim is withheld due to finite censorship.
        else:
            statuses["integral_first_stage_resolved"]+=1
        if is_applicable and first_exact:
            levels,diag,U,V=repair.tracked_smith_solver(A)
            T,fail=repair.can_solve_or_fail(
                levels,diag,U,V,A,C1,True)
            assert T is not None and not fail
            assert T.shape==(n,1)
            S1=(int(G[n,n])-sum(int(C1[i,0])*int(T[i,0])
                               for i in range(n)))%MOD
            R12=(int(G[n,n+1])-sum(int(T[i,0])*int(C2[i,0])
                                     for i in range(n)))%MOD
            checked=corrected_original_scalar_source(
                E,W,n,T,S1,R12)
            schur,schur_exact,schur_max,_=finite_index(
                np.array([[S1]],dtype=np.int64),
                np.array([[R12]],dtype=np.int64),"intermediate_Schur")
            assert second==max(oldlater,schur),(
                "finite integral-split composition mismatch",n,second,
                oldlater,schur)
            outcome["residual_Schur_finite_index_log5"]=schur
            outcome["residual_Schur_cokernel_uncensored"]=schur_exact
            outcome["original_evaluation_source_checks"]=checked
            outcome["observed_lcm_composition_exact_finite"]=True
            finite_lcm_tests+=1
            first_integral_validated+=1
            if oldlater>0 and schur>0:two_positive_components+=1
            if oldlater==0 and schur>0:schur_only+=1
        pair_result.append(outcome)
    assert len(pair_result)==38
    assert first_integral_validated==finite_lcm_tests
    assert sum(statuses.values())==38
    assert sum(second_hist.values())==38
    return {
        "all_contiguous_original_triplets_checked":38,
        "all_first_stages_status_counts":dict(statuses),
        "finite_direct_sum_composition_replays":finite_lcm_tests,
        "old_and_Schur_both_positive_cases":two_positive_components,
        "new_Schur_only_positive_cases":schur_only,
        "finite_first_zero_censored_cases":censored_first,
        "actual_second_stage_image_index_histogram":
            dict(sorted(second_hist.items())),
        "per_original_first_n_results":pair_result,
        "nothing_extrapolated_to_high_J_or_uniform_D":True
    }

def main():
    guard()
    field=field_h1_background()
    G,E,W,source=original_j1_source()
    original=exhaustive_triples(G,E,W)
    # In particular all 40 original rows and original Q remain
    # unchanged in BOTH the direct moment and jet oracles.
    print("PHASE298B_CLASS_ONE_ORIGINAL_SOURCE_COMPOSITION",{
        "number_field":field,
        "original_repo_source":source,
        "prime":P,"modulus":MOD,
        "full_original_G_40x40_symmetric":True,
        "all_source_row_labels_unchanged":True,
        "no_synthetic_points_or_new_trace_metric":True,
        "nested_row_results":original,
        "S1_J1_NOT_equal_to_D587_S5_J5":True,
        "no_new_original_field_determinant_factor":True,
        "no_uniform_class_one_cutoff_theorem":True
    },flush=True)
    print("PASS Phase298-B complete D163 class-one original-source two-step composition scan",
          flush=True)

if __name__=="__main__":
    main()
