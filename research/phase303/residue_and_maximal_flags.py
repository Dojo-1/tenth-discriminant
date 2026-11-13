#!/usr/bin/env python3
"""Phase303-D: F25 multiplicity trace mechanism and maximal-order flags.

Separately preregistered at 7d071a98 after A/B results and before
this code. Fixed genuine maximal-order D163 rho21 norm441 Q225, J1,
R40 original polynomial rows. No changed prime/cutoff or field bound.
"""
from collections import Counter,defaultdict
from pathlib import Path
import json
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for part in ("phase206","phase297","phase298","phase303"):
    sys.path.insert(0,str(ROOT/"research"/part))
import maximal_order_source as source
import minimal_transverse_repair as solver
import original_schur_integrality_k16 as smith

P=5
K=16
MOD=P**K
D=163
FIRST={2:2,6:1,16:1,36:1,37:1}
SOURCE_SHA="e68f66dac1c914a97c0fe93655a693053f80386f"

def guard():
    source.freeze()
    path="research/phase303/maximal_order_source.py"
    actual=subprocess.check_output(
      ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
    assert actual==SOURCE_SHA,("preregistered original source changed",actual)

def mul5(x,y):
    a,b=x;c,d=y
    return ((a*c-b*d)%P,(a*d+b*c+b*d)%P)

def conjugate5(z):
    a,b=z
    return ((a+b)%P,-b%P)

def trace5(z):
    a,b=z
    return (2*a+b)%P

def pow5(z,n):
    q=(1,0)
    for _ in range(n):q=mul5(q,z)
    return q

def f25_trace_multiplicity(Q,Gram,label):
    multiplicities=Counter((a%P,b%P) for a,b in Q)
    residue_set=set(multiplicities)
    assert len(residue_set)==(15 if label=="even" else 25)
    assert all(conjugate5(z) in residue_set for z in residue_set)
    assert all(multiplicities[z]==multiplicities[conjugate5(z)]
               for z in residue_set)
    # Independently build ALL moment entries from FINITE field
    # residue multiplicities rather than Q-source big integer powers.
    Gfinite=[[0]*40 for _ in range(40)]
    powers={z:[pow5(z,r) for r in range(40)] for z in residue_set}
    for i in range(40):
        for j in range(i,40):
            rhs=sum(
              m*trace5(mul5(powers[z][i],
                             conjugate5(powers[z][j])))
              for z,m in multiplicities.items())%P
            assert rhs==int(Gram[i,j])%P,(
                "p5 residue multiplicity trace Gram mismatch",
                label,i,j,rhs,int(Gram[i,j])%P)
            Gfinite[i][j]=Gfinite[j][i]=rhs
    assert source.rank_mod5(Gfinite)==len(residue_set)
    unit_count=sum(m%P!=0 for m in multiplicities.values())
    assert unit_count==len(residue_set),(
        "trace weight was 0 mod5 although Gram/eval full rank",
        label,unit_count,len(residue_set))
    return {
      "source":label,
      "actual_observation_points":len(Q),
      "distinct_F25_support_points":len(residue_set),
      "all_residue_multiplicities_nonzero_mod5":True,
      "actual_frequency_count_histogram":
          dict(sorted(Counter(multiplicities.values()).items())),
      "frequency_remainder_mod5_histogram":
          dict(sorted(Counter(m%P for m in multiplicities.values()).items())),
      "per_F25_residue_source_multiplicities":{
          f"{a},{b}":multiplicities[(a,b)]for a,b in sorted(residue_set)},
      "conjugation_invariance_multiplicity":True,
      "all_1600_F25_trace_moment_to_original_Gram_cells_agree":True,
      "Gram_rank_mod5_from_weighted_perfect_trace":len(residue_set),
      "unramified_F25_polynomial_eval_space_dim":len(residue_set),
      "no_new_original_full_field_determinant_mass":True
    }

def O(x):
    return np.asarray(x,dtype=object)

def modarr(x):
    return np.asarray(O(x)%MOD,dtype=np.int64)

def v5(x):
    v=int(x)%MOD
    if v==0:return K
    k=0
    while v%P==0:
        k+=1;v//=P
    return k

def tracepair(aa,bb):
    """Actual ORIGINAL ω-coordinate raw evaluation row trace norm."""
    u=[int(x) for x in np.asarray(aa).reshape(-1)]
    v=[int(x) for x in np.asarray(bb).reshape(-1)]
    assert len(u)==len(v) and len(u)%2==0
    return sum(
      2*u[i]*v[i]+u[i]*v[i+1]+u[i+1]*v[i]+82*u[i+1]*v[i+1]
      for i in range(0,len(u),2))%MOD

def image_debt(A,C):
    assert A.shape[0]==A.shape[1] and C.shape[0]==A.shape[0]
    levels,_=smith.high_precision_smith(A)
    bigger,_=smith.high_precision_smith(np.concatenate([A,C],axis=1))
    assert max(levels)<K,("Gram cokernel censored",max(levels))
    assert all(x>=y for x,y in zip(levels,bigger))
    return sum(levels)-sum(bigger)

def binary_local(S):
    aa=int(S[0,0]);cc=int(S[0,1]);bb=int(S[1,1])
    d=min(v5(aa),v5(cc),v5(bb))
    assert d<K
    U=np.array([[int(S[i,j])//(P**d)%P for j in range(2)]
                for i in range(2)],dtype=np.int64)
    det=(int(U[0,0])*int(U[1,1])-int(U[0,1])*int(U[1,0]))%P
    rank=2 if det else 1
    roots=[(1,t) for t in range(P) if
      (int(U[0,0])+2*int(U[0,1])*t+int(U[1,1])*t*t)%P==0]
    if int(U[1,1])%P==0:roots.append((0,1))
    if rank==2:assert len(roots) in (0,2)
    else:assert len(roots)==1
    return {"source_scale_depth":d,
            "normalized_Gram_rank_mod5":rank,
            "projective_isotropic_lines_mod5":roots}

def maximal_flag_census(Gram,E):
    G=source.gram_mod(Gram)
    events=[]
    pairs=[]
    single_hist=Counter()
    conditional_hist=Counter()
    transition=Counter()
    per_n=defaultdict(Counter)
    first_examples={}
    count_candidates=0
    total_pairs=0
    for n,expected in FIRST.items():
        old0=G[:n,:n]
        c1=G[:n,n:n+1]
        assert image_debt(old0,c1)==expected
        oldids=list(range(n+1))
        A=G[np.ix_(oldids,oldids)]
        oldE=E[oldids,:]
        levels,diag,U,V=solver.tracked_smith_solver(A)
        assert max(levels)<K
        candidates=list(range(n+2,40,2))
        assert len(candidates)=={2:18,6:16,16:11,36:1,37:1}[n]
        individual={}
        for r in candidates:
            count_candidates+=1
            C=G[np.ix_(oldids,[r])]
            debt=image_debt(A,C)
            single_hist[debt]+=1
            entry={"initial_obstructed_original_row":n,
                   "new_original_same_parity_monomial_row":r,
                   "original_old_row_count":len(oldids),
                   "actual_cross_image_log5":debt}
            if debt==0:
                t,issues=solver.can_solve_or_fail(
                  levels,diag,U,V,A,C,True)
                assert t is not None and not issues
                assert not np.any((O(A)@O(t)-O(C))%MOD)
                corrected=(O(E[[r],:])-O(t).T@O(oldE))%MOD
                for old in oldE:
                    assert tracepair(corrected,old)==0
                norm=tracepair(corrected,corrected)
                assert norm==(
                    int(G[r,r])-int((O(C).T@O(t))[0,0]))%MOD
                assert v5(norm)<K
                individual[r]={"T":t,"E":corrected.reshape(-1),
                               "S":norm}
                entry["original_source_integral_projection_verified"]=True
            else:
                entry["original_source_integral_projection_verified"]=False
            events.append(entry)
            per_n[n]["second_original_source_debt_"+str(debt)]+=1
        for i,s in enumerate(candidates):
            for t in candidates[i+1:]:
                total_pairs+=1
                record={"first_nonintegral_initial_original_row":n,
                        "later_original_s":s,
                        "later_original_t":t}
                if s not in individual or t not in individual:
                    record["joint_lemma_applicable"]=False
                    record["reason"]="one_or_both_later_rows_nonintegral_to_common_base"
                    conditional_hist["not_applicable"]+=1
                    pairs.append(record)
                    continue
                Es=individual[s]["E"];Et=individual[t]["E"]
                norm_s=individual[s]["S"];norm_t=individual[t]["S"]
                c=tracepair(Es,Et)
                algebra=(int(G[s,t])-int((O(individual[s]["T"]).T@
                        O(G[np.ix_(oldids,[t])]))[0,0]))%MOD
                assert c==algebra
                assert c==tracepair(Et,Es)
                assert v5(norm_s)<K and v5(norm_t)<K
                Sf=np.array([[norm_s,c],[c,norm_t]],dtype=np.int64)
                fd=max(0,v5(norm_s)-v5(c))
                rd=max(0,v5(norm_t)-v5(c))
                af=oldids+[s]
                ar=oldids+[t]
                gf=G[np.ix_(af,af)]
                gr=G[np.ix_(ar,ar)]
                cf=G[np.ix_(af,[t])]
                cr=G[np.ix_(ar,[s])]
                assert fd==image_debt(gf,cf)
                assert rd==image_debt(gr,cr)
                finalids=oldids+[s,t]
                finalids_swapped=oldids+[t,s]
                a=G[np.ix_(finalids,finalids)]
                b=G[np.ix_(finalids_swapped,finalids_swapped)]
                perm=list(range(len(oldids)))+[
                    len(oldids)+1,len(oldids)]
                assert np.array_equal(a[np.ix_(perm,perm)],b)
                fa,_=smith.high_precision_smith(a)
                fb,_=smith.high_precision_smith(b)
                assert fa==fb and max(fa)<K
                local=binary_local(Sf)
                conditional_hist["applicable"]+=1
                transition[f"{fd}->{rd}"]+=1
                per_n[n][f"joint_{fd}_to_{rd}"]+=1
                record.update({
                  "joint_lemma_applicable":True,
                  "original_residual_2x2_p5":Sf.tolist(),
                  "original_norm_s_val":v5(norm_s),
                  "original_norm_t_val":v5(norm_t),
                  "original_mutual_residual_val_capped16":v5(c),
                  "s_then_t_cross_class_log5":fd,
                  "t_then_s_cross_class_log5":rd,
                  "full_original_same_lattice_p5_Gram_v5":sum(fa),
                  "local_binary_residual_type":local
                })
                if (fd or rd) and "first_eligible_obstruction" not in first_examples:
                    first_examples["first_eligible_obstruction"]=record
                if fd!=rd and "first_order_asymmetry" not in first_examples:
                    first_examples["first_order_asymmetry"]=record
                pairs.append(record)
    assert count_candidates==47
    assert total_pairs==328==len(pairs)
    assert sum(single_hist.values())==47
    assert sum(conditional_hist.values())==328
    return {
      "initial_full_maximal_source_nonintegral_prefix_debts":FIRST,
      "all_47_preregistered_same_parity_single_rows":events,
      "single_source_cross_image_log5_histogram":dict(sorted(single_hist.items())),
      "all_328_preregistered_original_pair_classifications":pairs,
      "total_328_later_pair_cases":328,
      "typed_integral_schur_applicability":dict(sorted(conditional_hist.items())),
      "both_orders_corrected_Schur_debt_transition":
          dict(sorted(transition.items())),
      "per_first_bad_row_outcomes":{
          str(n):dict(sorted(per_n[n].items()))for n in FIRST},
      "first_reproducible_examples_if_any":first_examples,
      "no_source_or_original_final_Gram_change":True,
      "no_class_one_uniform_high_J_conclusion":True
    }

def main():
    guard()
    a=source.all_arms()
    even=a["Qeven"];full=a["Qfull"]
    P1=f25_trace_multiplicity(even,a["G_even"],"even")
    P2=f25_trace_multiplicity(full,a["G_full"],"full")
    print("PHASE303D_F25_RESIDUE_MULTIPLICITY_RESULT",{
      "old_source":P1,"full_maximal_source":P2,
      "trace_form_perfect_mod5_over_F25":True,
      "source_support_extension_explains_mod5_rank_gain":True,
      "no_p5_Gram_valuation_monotonicity_asserted":True
    },flush=True)
    census=maximal_flag_census(a["G_full"],a["E_full"])
    # All cases reproducible deterministically; concise summary line
    # avoids truncating the 328 structured records in CI logs.
    summary={k:v for k,v in census.items()
      if k not in ("all_47_preregistered_same_parity_single_rows",
                   "all_328_preregistered_original_pair_classifications")}
    print("PHASE303D_FULL_MAXIMAL_ORDER_FLAG_CENSUS",{
      "source_D":D,"source_original_J":1,
      "original_full_maximal_Q":len(full),
      "maximal_source_fixed_norm_cutoff":441,
      "census":summary,
      "original_all_records_reconstructible_from_pinned_source":True,
      "no_extra_field_determinant_mass":True
    },flush=True)
    print("PASS Phase303-D exact F25 multiplicity rank and full maximal-order flag census",flush=True)

if __name__=="__main__":
    main()
