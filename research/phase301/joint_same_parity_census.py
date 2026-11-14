#!/usr/bin/env python3
"""Phase301: pairwise-to-joint p5 integral Gram projection in original D163.

Preregistered at adc663e8 BEFORE this code and its results.
Fixed seven original first-nonintegral stages, every 176 later
same-parity pair. Class h1 is a FIELD property; this is still the
ORIGINAL integer-order J1/Q109 sampler. No original determinant extras.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for part in ("phase206","phase297","phase298","phase299","phase300","phase301"):
    sys.path.insert(0,str(ROOT/"research"/part))
from source_probe import params
import class_one_d163_composition as original
import same_parity_challenge as previous
import double_glue_original as smithapi
import minimal_transverse_repair as solver

P=5
K=16
MOD=P**K
D=163
N_LIST=(13,18,22,25,33,34,38)
PARENT_SHA="d05864330eb95fcda1f1025f16abe977d870c686"

def guard():
    previous.guard()
    path="research/phase300/same_parity_challenge.py"
    actual=subprocess.check_output(
        ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
    assert actual==PARENT_SHA,("source/previous exhaustive test changed",actual)

def O(x):
    return np.asarray(x,dtype=object)

def v5(x):
    v=int(x)%MOD
    if v==0:return K
    k=0
    while v%P==0:
        v//=P;k+=1
    return k

def weighted(E,F,W):
    return (O(E)*O(W)[None,:])@O(F).T%MOD

def pairwise_schur_toy():
    """PD toy where BOTH future rows project integrally into L1,
    but the SECOND becomes nonintegral AFTER attaching the first.
    """
    G=np.asarray([
       [25,5,5,25],
       [5,10,10,5],
       [5,10,15,6],
       [25,5,6,100]],dtype=np.int64)
    A0=G[:1,:1]
    A1=G[:2,:2]
    A2=G[:3,:3]
    assert smithapi.debt(A0,G[:1,1:2])==1
    assert smithapi.debt(A1,G[:2,2:3])==0
    assert smithapi.debt(A1,G[:2,3:4])==0
    assert smithapi.debt(A2,G[:3,3:4])==1
    # Sylvester principal minors: 25,225,1125,225*(5*75-1).
    minors=[25,225,1125,225*374]
    assert all(x>0 for x in minors)
    assert Fraction(5,25)==Fraction(1,5)
    # y2 projects into L1 along y1; y3 projects along old x.
    assert G[:2,2].tolist()==G[:2,1].tolist()
    assert G[:2,3].tolist()==G[:2,0].tolist()
    y2_schur=int(G[2,2])-int(G[2,1])
    assert y2_schur==5
    residual=int(G[2,3])-int(G[1,3])
    assert residual==1
    assert v5(y2_schur)-v5(residual)==1
    return {
      "positive_definite_leading_principal_minors":minors,
      "first_old_to_y1_denominator_order":5,
      "both_later_columns_individually_integral_into_L1":True,
      "new_scalar_Schur":y2_schur,
      "cross_residual_for_third_row":residual,
      "actual_third_row_new_image_order":5,
      "pairwise_integrality_does_NOT_imply_joint_integrality":True
    }

def finite_field_period(E,Q):
    # Over F25: u²=-D=2, Frobenius conjugation, |F25*|=24.
    # For r>=1 both sides vanish on z≡0, so all samples qualify.
    assert (-D)%P==2
    nonsquares={x*x%P for x in range(P)}
    assert 2 not in nonsquares
    checked=0
    for r in range(1,16):
        for qi in range(len(Q)):
            for coord in (0,1):
                a=int(E[r+24,2*qi+coord])%P
                b=int(E[r,2*qi+coord])%P
                assert a==b,("original mod5 F25 period24 failure",r,qi,coord)
                checked+=1
    zero=Q.index((0,0))
    assert int(E[0,2*zero])%P==1
    assert int(E[24,2*zero])%P==0
    return {
      "original_row_indices_checked":[1,15],
      "finite_field_F25_multiplicative_order":24,
      "original_raw_jet_real_imag_mod5_checks":checked,
      "original_r0_not_24_periodic_at_zero_residue":True,
      "mod5_period_does_NOT_prove_Z5_image_inclusion":True
    }

def source_census(G,E,W):
    cases=[]
    by_n=defaultdict(Counter)
    histogram=Counter()
    source_checks=0
    first_stage_checks=0
    individually_integral_checks=0
    total_pairs=0
    for n in N_LIST:
        A0=G[:n,:n]
        y1=G[:n,n:n+1]
        assert smithapi.debt(A0,y1)==1
        first_stage_checks+=1
        oldrows=list(range(n))+[n]
        A=G[np.ix_(oldrows,oldrows)]
        Eold=E[oldrows]
        assert A.shape==(n+1,n+1)
        levels,diagonal,U,V=solver.tracked_smith_solver(A)
        assert max(levels)<K
        candidates=list(range(n+2,40,2))
        for si,s in enumerate(candidates):
            assert s%2==n%2
            C=G[np.ix_(oldrows,[s])]
            assert smithapi.debt(A,C)==0
            individually_integral_checks+=1
            T,err=solver.can_solve_or_fail(
                levels,diagonal,U,V,A,C,True)
            assert T is not None and not err and T.shape==(n+1,1)
            assert not np.any((O(A)@O(T)-O(C))%MOD)
            # Construct the ACTUAL source-native corrected row. Smith
            # coordinates are returned to original monomial row basis.
            corrected=(O(E[[s]])-O(T).T@O(Eold))%MOD
            oldpair=weighted(Eold,corrected,W)
            assert not np.any(oldpair)
            s_mod=int(weighted(corrected,corrected,W)[0,0])
            s_alg=(int(G[s,s])-int((O(C).T@O(T))[0,0]))%MOD
            assert s_mod==s_alg
            vs=v5(s_mod)
            assert vs<K,("Schur scalar censored at fixed p16",n,s)
            source_checks+=len(oldrows)+1
            for t in candidates[si+1:]:
                total_pairs+=1
                assert t>s and t%2==s%2
                C3=G[np.ix_(oldrows,[t])]
                assert smithapi.debt(A,C3)==0,(
                    "prior 43-case individual membership changed",n,t)
                rt=int(weighted(corrected,E[[t]],W)[0,0])
                residue=(int(G[s,t])-int((O(T).T@O(C3))[0,0]))%MOD
                assert rt==residue,(
                    "original trace cross versus Gram Schur mismatch",n,s,t)
                vr=v5(rt)
                predicted=max(0,vs-vr)
                added=oldrows+[s]
                A2=G[np.ix_(added,added)]
                Cnext=G[np.ix_(added,[t])]
                actual=smithapi.debt(A2,Cnext)
                assert predicted==actual,(
                    "conditional Schur source composition failure",
                    n,s,t,vs,vr,predicted,actual)
                histogram[actual]+=1
                by_n[n][actual]+=1
                cases.append({
                    "n":n,"first_original_row":n,
                    "second_original_row":s,"third_original_row":t,
                    "scalar_Schur_v5":vs,
                    "next_original_cross_residual_v5_capped16":vr,
                    "scalar_Schur_predicted_log5_debt":predicted,
                    "full_original_Gram_measured_log5_debt":actual,
                    "original_source_double_Gram_verified":True
                })
                source_checks+=1
    assert first_stage_checks==7
    assert individually_integral_checks==43
    assert total_pairs==176==len(cases)
    assert sum(histogram.values())==176
    return {
       "source_original_first_obstructed_n":list(N_LIST),
       "all_individually_integral_later_original_rows":43,
       "all_fixed_same_parity_joint_original_pairs_tested":176,
       "new_third_stage_image_index_histogram":dict(sorted(histogram.items())),
       "per_first_n_index_counts":{
          str(n):dict(sorted(Counter(by_n[n]).items()))
          for n in N_LIST
       },
       "first_nonzero_joint_case_if_any":next(
          (c for c in cases if c[
             "full_original_Gram_measured_log5_debt"]>0),None),
       "all_pair_original_source_results":cases,
       "independent_original_jet_metric_G_schur_checks":source_checks,
       "all_schur_and_full_Gram_cokernel_predictions_agree":True,
       "no_adaptive_source_case_selection":True,
       "NO_determinant_valuation_double_counting":True
    }

def main():
    guard()
    field=original.field_h1_background()
    G,E,W,meta=original.original_j1_source()
    assert (meta["R"],meta["S"],meta["J"],meta["Q"])==(40,1,1,109)
    symmetry=previous.symmetry(G,E,W)
    toy=pairwise_schur_toy()
    period=finite_field_period(E,params(D)[-1])
    census=source_census(G,E,W)
    # One line in log for independent extraction and source record.
    print("PHASE301_ORIGINAL_D163_JOINT_SATURATION_VERDICT",{
       "field_class_number_one_background":field,
       "original_integer_order_source":meta,
       "integer_parity_controls":symmetry,
       "source_F25_residue_field_period":period,
       "source_independent_positive_Gram_hostile_toy":toy,
       "complete_fixed_original_source_census":census,
       "no_uniform_h1_high_J_or_tenth_discriminant_cutoff_claim":True
    },flush=True)
    print("PASS Phase301 complete original D163 same-parity joint projection scan",
          flush=True)

if __name__=="__main__":
    main()
