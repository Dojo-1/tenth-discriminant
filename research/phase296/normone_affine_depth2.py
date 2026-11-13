#!/usr/bin/env python3
"""Phase296-B: exhaustive norm-one A_2 affine transport at p²=25.

Preregistered at 0e874956 BEFORE implementation. All 37,500 lifts
to the unramified quadratic local ring modulo 25 are tested. Original
D583 n725 and D587 n730 samplers are unchanged. No field theorem.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
from source_probe import params

DA=583
DB=587
P=5
M=25
ALPHA=17
FROZEN={
 "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase296/affine_semilinear_transporter.py":"ba95668c0bd90cd7cac0426060f6d2f210b48de3",
}
EMPTY=(0,0)
ONE=(1,0)

def guard():
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("frozen source changed",path,actual,sha)

def qmul(a,b,mod=M):
    return ((a[0]*b[0]-DA*a[1]*b[1])%mod,
            (a[0]*b[1]+a[1]*b[0])%mod)

def qconj(z,mod=M):
    return (z[0]%mod,(-z[1])%mod)

def qnorm(z,mod=M):
    val=qmul(z,qconj(z,mod),mod)
    assert val[1]==0
    assert val[0]==(z[0]*z[0]+DA*z[1]*z[1])%mod
    return val[0]

def coord(z,mod=M):
    return (z[0]%mod,z[1]%mod)

def all_elements(mod=M):
    return list(product(range(mod),repeat=2))

def add(z,b,mod=M):
    return ((z[0]+b[0])%mod,(z[1]+b[1])%mod)

def transformed(z,a,b,eps,mod=M):
    if eps==-1:z=qconj(z,mod)
    return add(qmul(a,z,mod),b,mod)

def scalar_weighted_match(src,candidate):
    assert sum(src.values())==sum(candidate.values())==383
    return sum(min(src[z],candidate[z]) for z in src.keys()|candidate.keys())

def independent_sorted_match(src,arr):
    aa=sorted(v for v,n in src.items() for _ in range(n))
    bb=sorted(arr)
    assert len(aa)==len(bb)==383
    i=j=common=0
    while i<len(aa) and j<len(bb):
        if aa[i]==bb[j]:common+=1;i+=1;j+=1
        elif aa[i]<bb[j]:i+=1
        else:j+=1
    return common

def original_source():
    rhoA,RA,SA,JA,QA=params(DA)
    rhoB,RB,SB,JB,QB=params(DB)
    assert (rhoA,RA,SA,JA,len(QA))==(53,145,5,5,383)
    assert (rhoB,RB,SB,JB,len(QB))==(53,146,5,5,383)
    assert QA==QB
    assert (DA*ALPHA*ALPHA-DB)%M==0
    return QA,(RA*SA,RB*SB)

def positive_and_hostile_controls(Q):
    source=Counter(coord(q) for q in Q)
    assert scalar_weighted_match(source,Counter(coord(q) for q in Q))==383
    for a,eps in ((ONE,1),((M-1,0),1),(ONE,-1)):
        moved=Counter(transformed(coord(q),a,EMPTY,eps)
                      for q in Q)
        assert moved==source
    # A GENERIC Z/25-linear coordinate re-scaling can cancel phi
    # exactly but fails to preserve the quadratic RING or trace form.
    inverse_alpha=pow(ALPHA,-1,M)
    assert inverse_alpha==3
    phi=[(x%M,ALPHA*y%M) for x,y in Q]
    repaired=[(x,inverse_alpha*y%M) for x,y in phi]
    assert Counter(repaired)==source
    u=(0,1)
    map_lin=lambda z:(z[0]%M,inverse_alpha*z[1]%M)
    assert map_lin(qmul(u,u))!=qmul(map_lin(u),map_lin(u))
    assert qnorm(u)!=qnorm(map_lin(u))
    return {
      "same_field_original_Q_identity_inversion_conjugation_full_match":True,
      "F25_base_linear_inverse_alpha_mod25":inverse_alpha,
      "F25_base_linear_map_repairs_all_383_sample_residues":True,
      "F25_base_linear_map_not_quadratic_ring_or_norm_isometry":True}

def full_normone_search(Q):
    src=Counter(coord(q) for q in Q)
    target=[(x%M,ALPHA*y%M) for x,y in Q]
    allvals=all_elements()
    units=[a for a in allvals if qnorm(a)==1]
    assert len(units)==30
    assert len([a for a in units if a[1]==0])==2
    assert set(a for a in units if a[1]==0)=={(1,0),(24,0)}
    hist=Counter()
    selectors=("norm_one_all_translation",
               "norm_one_translation_real",
               "norm_one_multiplier_real",
               "norm_one_both_real")
    summaries={name:{"count":0,"best":384,"ties":[]} for name in selectors}
    total=0
    for eps in (1,-1):
        initial=[coord(q) if eps==1 else qconj(q) for q in target]
        for a in units:
            rotated=Counter(qmul(a,q) for q in initial)
            assert sum(rotated.values())==383
            for b in allvals:
                # Fast but exact: translate the UNIQUE pre-aggregated
                # 25-adic point residue fibers, not all 383 point labels.
                matching=sum(min(v,src[add(z,b)]) for z,v in rotated.items())
                debt=383-matching
                assert debt>=64,("mod25 match beats modulo5 normone bound",a,b,eps,debt)
                assert debt>0
                total+=1
                hist[debt]+=1
                tags=["norm_one_all_translation"]
                if b[1]==0:tags.append("norm_one_translation_real")
                if a[1]==0:tags.append("norm_one_multiplier_real")
                if a[1]==0 and b[1]==0:tags.append("norm_one_both_real")
                for name in tags:
                    s=summaries[name]
                    s["count"]+=1
                    if debt<s["best"]:
                        s["best"]=debt
                        s["ties"]=[(a,b,eps)]
                    elif debt==s["best"]:
                        s["ties"].append((a,b,eps))
    assert total==30*625*2==37500
    assert [summaries[name]["count"] for name in selectors]==[
        37500,1500,2500,100]
    assert sum(hist.values())==37500

    reports={}
    for name,s in summaries.items():
        ties=sorted(s["ties"],key=lambda x:(x[2],x[0],x[1]))
        assert len(ties)>0 and s["best"]>=64
        # Independent slow Counter transform AND a separately
        # implemented sorted-list matching for EVERY best candidate.
        for a,b,eps in ties:
            moved=[transformed(q,a,b,eps) for q in target]
            slow=scalar_weighted_match(src,Counter(moved))
            independently=independent_sorted_match(src,moved)
            assert slow==independently==383-s["best"],(
                "independent best candidate mismatch",name,a,b,eps)
        reports[name]={
            "tested_exact_candidates":s["count"],
            "minimum_unmatched_points_each_side_mod25":s["best"],
            "maximum_matched_original_points":383-s["best"],
            "number_of_best_ties":len(ties),
            "all_best_candidates_replayed_by_two_independent_oracles":True,
            "best_representatives":[{
                "a":list(a),"b":list(b),"epsilon":eps,
                "norm_slope_mod25":qnorm(a)}
                for a,b,eps in ties[:8]]
        }
    reports["norm_one_all_translation"]["exact_37500_debt_histogram"]=dict(
        sorted(hist.items()))
    return reports

def retrospective_mod5_real_translation_regression(Q):
    """Post-result correction: do not confuse an all-translation floor
    64 with the exact 60-map BASE-translation subgroup minimum 72.
    This was checked separately after the preregistered p25 run.
    """
    mod=5
    src=Counter((x%mod,y%mod) for x,y in Q)
    normone=[a for a in all_elements(mod)
             if qnorm(a,mod)==1]
    assert len(normone)==6
    best=384
    ties=0
    checked=0
    for eps in (1,-1):
        for a in normone:
            for b0 in range(mod):
                b=(b0,0)
                moved=Counter(
                    transformed((x%mod,(2*y)%mod),a,b,eps,mod)
                    for x,y in Q)
                debt=383-scalar_weighted_match(src,moved)
                checked+=1
                if debt<best:
                    best=debt
                    ties=1
                elif debt==best:
                    ties+=1
    assert checked==60
    assert best==72 and ties==16
    return {"complete_60_maps":checked,
            "exact_minimum_missing_mod5":best,
            "number_of_best_ties":ties,
            "retrospective_independent_correction_not_preregistered":True}

def main():
    guard()
    Q,rows=original_source()
    assert rows==(725,730)
    control=positive_and_hostile_controls(Q)
    mod5_control=retrospective_mod5_real_translation_regression(Q)
    report=full_normone_search(Q)
    print("PHASE296B_NORMONE_MOD25_COMPLETE",{
       "full_original_D583_R145_rows":rows[0],
       "full_original_D587_R146_rows":rows[1],
       "original_Q_unchanged":len(Q),
       "original_ordinary_jet_J":5,
       "local_order":"Z/25[u]/(u^2+583)",
       "local_isometry_alpha":ALPHA,
       "norm_one_slope_count":30,
       "affine_norm_one_semilinear_candidates":37500,
       "source_and_counterworld_controls":control,
       "post_result_mod5_real_translation_correction":mod5_control,
       "exact_search_results":report,
       "minimum_mod25_debt_never_below_mod5_64":True,
       "translation_is_not_necessarily_trace_form_linear":True,
       "base_field_original_row_and_primitive_source_lift_NOT_established":True,
       "no_extra_5adic_determinant_factor_or_h1_field_theorem":True
    },flush=True)
    print("PASS Phase296-B full mod25 norm-one translated affine transporter scan",
          flush=True)

if __name__=="__main__":
    main()
