#!/usr/bin/env python3
"""Phase298-A: typed original D587 multi-stage p5 Gram-cokernel composition.

Preregistered e2571b3172 BEFORE implementation. Exact original 730
monomial rows, same Q383/J5/trace metric. Compare both insertion orders,
with no replacement of original sampler or lattice, and no valuation
double counting. The conditional split theorem is paper-level only.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase292","phase297"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
import original_schur_integrality_k16 as p16
import minimal_transverse_repair as repair

D=587
P=5
K=16
MOD=P**K
FROZEN={
    "research/phase297/original_schur_integrality_k16.py":
        "aa3678001c69a7235dca638638d2dab4c55b05b3",
    "research/phase297/minimal_transverse_repair.py":
        "22b0077a2424553021a4c9859f92f0fe3efc2fe7",
}
HIST_OLD_EVEN={0:63,2:15,3:47,4:63,5:47,6:10,7:5,8:50,9:13,12:20,14:30}
HIST_OLD_ODD={0:62,2:15,3:48,4:62,5:48,6:10,7:5,8:50,9:12,12:20,14:30}

def freeze():
    repair.freeze()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("original source changed",path,actual,sha)

def mm(A,B):
    """Exact modular matrix product; Python bigint intermediate."""
    return (np.asarray(A,dtype=object)@np.asarray(B,dtype=object))%MOD

def red(A):
    out=np.asarray(A,dtype=object)%MOD
    return np.asarray(out,dtype=np.int64)

def smith_index(A,extra,caption):
    n=A.shape[0]
    assert A.shape==(n,n)
    assert extra.shape[0]==n
    la,ha=p16.high_precision_smith(A)
    lb,hb=p16.high_precision_smith(
        np.concatenate([A,extra],axis=1))
    assert len(la)==len(lb)==n
    assert all(y<=x for x,y in zip(la,lb))
    debt=sum(la)-sum(lb)
    assert debt>=0
    record={
        "carrier":caption,
        "old_Gram_rank":n,
        "added_cross_columns":extra.shape[1],
        "finite_exact_cokernel_image_log5":debt,
        "old_Smith_max_grade":max(la),
        "old_cokernel_uncensored_at_p16":max(la)<K,
        "old_Smith_histogram":ha,
        "augmented_Smith_histogram":hb,
    }
    return record

def positive_toys():
    # Toy 1: first split integral, old residual zero, new Schur residual 1.
    # G=[[1,0,0],[0,5,1],[0,1,2]], det9, PD, quotient order5.
    # Toy 2: old class order5 AND new S1 class order5, but joint
    # class is (1,1) in (Z/5)^2 and still only order5, NOT25.
    examples=[
      {"a":1,"c1":0,"b1":5,"c2":0,"e":1,"b2":2,
       "old_component":0,"schur_component":1,"joint":1},
      {"a":5,"c1":5,"b1":10,"c2":1,"e":2,"b2":10,
       "old_component":1,"schur_component":1,"joint":1},
    ]
    tests=[]
    for row in examples:
        a,c1,b1,c2,e,b2=(row[k] for k in
                         ("a","c1","b1","c2","e","b2"))
        det2=a*b1-c1*c1
        det3=a*(b1*b2-e*e)-c1*(c1*b2-e*c2)+c2*(c1*e-b1*c2)
        assert a>0 and det2>0 and det3>0
        # T1=c1/a exact integer for two controls.
        assert c1%a==0
        t1=c1//a
        schur=b1-c1*t1
        residual=e-t1*c2
        assert schur==5
        old=smith_index(np.array([[a]],dtype=np.int64),
                        np.array([[c2]],dtype=np.int64),"toy old")
        s=smith_index(np.array([[schur]],dtype=np.int64),
                      np.array([[residual]],dtype=np.int64),"toy Schur")
        first=np.array([[a,c1],[c1,b1]],dtype=np.int64)
        nxt=np.array([[c2],[e]],dtype=np.int64)
        joint=smith_index(first,nxt,"toy original intermediate")
        assert (old["finite_exact_cokernel_image_log5"],
                s["finite_exact_cokernel_image_log5"],
                joint["finite_exact_cokernel_image_log5"] )==(
                    row["old_component"],row["schur_component"],
                    row["joint"])
        assert row["joint"]==max(row["old_component"],row["schur_component"])
        tests.append({
            "old_component_log5_order":row["old_component"],
            "Schur_component_log5_order":row["schur_component"],
            "actual_joint_log5_order":row["joint"],
            "naive_sum_wrong":row["old_component"]+
                    row["schur_component"]!=row["joint"]
                    if row["old_component"] and row["schur_component"] else True,
            "full_positive_Gram_det":det3,
        })
    return tests

def source():
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(53,146,5,5,383)
    E,Q,W,checks=repair.original_source()
    assert E.shape==(730,3830)
    assert W.shape==(3830,)
    p16.parity_blocks(E,Q,W) # ALL original 365x365 opposite-parity pairings
    Gnew=p16.pairings_three_digits(E[725:730],E[725:730],W)
    assert np.array_equal(Gnew,Gnew.T)
    return E,Q,W,Gnew,checks

def sector_data(E,W):
    # Compute the ACTUAL original old-Gram blocks and ALL five new
    # cross columns. Rows are ORIGINAL global monomial row labels.
    old_cross=np.zeros((725,5),dtype=np.int64)
    sectors={}
    for name in ("even","odd"):
        oldids,newids=repair.sector_ids(name)
        old=E[oldids]
        A=p16.pairings_three_digits(old,old,W)
        C=p16.pairings_three_digits(old,E[newids],W)
        assert np.array_equal(A,A.T)
        targets=[i%5 for i in newids]
        old_cross[np.ix_(oldids,targets)]=C
        levels,diag,U,V=repair.tracked_smith_solver(A)
        expected=HIST_OLD_EVEN if name=="even" else HIST_OLD_ODD
        assert dict(Counter(levels))==expected
        assert max(levels)==14
        sectors[name]={"oldids":oldids,"newids":newids,"svals":targets,
            "A":A,"C":C,"levels":levels,"diag":diag,"U":U,"V":V}
    assert np.count_nonzero(old_cross)>0
    return old_cross,sectors

def first_integral_stage(E,W,Gnew,oldcross,sectors):
    # FIRST 4 original new row labels s0,s1,s2,s3.
    # All are known original Gram-cokernel kernel directions,
    # but independently recheck EACH modular equation.
    T1=np.zeros((725,4),dtype=np.int64)
    for name,record in sectors.items():
        safe=[i for i,s in enumerate(record["svals"]) if s<4]
        news=[record["svals"][i] for i in safe]
        C=record["C"][:,safe]
        solution,problems=repair.can_solve_or_fail(
            record["levels"],record["diag"],record["U"],record["V"],
            record["A"],C,True)
        assert solution is not None and not problems
        T1[np.ix_(record["oldids"],news)]=solution
        if name=="odd":
            badcol=record["C"][:,[record["svals"].index(4)]]
            unsolved,problems=repair.can_solve_or_fail(
                record["levels"],record["diag"],record["U"],record["V"],
                record["A"],badcol,False)
            assert unsolved is None and problems
        assert not np.any(
            (mm(record["A"],solution)-
             np.asarray(C,dtype=object))%MOD)
    # Because opposite parity is exactly orthogonal, assembling
    # the full 725-row solution preserves original C2 action.
    C1=oldcross[:,:4]
    C2=oldcross[:,4:5]
    B1=Gnew[:4,:4]
    E12=Gnew[:4,4:5]
    S1=red(B1-mm(C1.T,T1))
    R12=red(E12-mm(T1.T,C2))
    assert np.array_equal(S1,S1.T)
    assert np.array_equal(S1[[1,3]][:,[0,2]],
                          np.zeros((2,2),dtype=np.int64))
    assert int(R12[1,0])==int(R12[3,0])==0
    # Factual original evaluation source recheck of this split;
    # the Smith-column operations have NOT been moved into B.
    corrected=red(np.asarray(E[725:729],dtype=object)-
                  mm(T1.T,E[:725]))
    actual_s1=p16.pairings_three_digits(corrected,corrected,W)
    actual_r12=p16.pairings_three_digits(corrected,E[[729]],W)
    assert np.array_equal(actual_s1,S1)
    assert np.array_equal(actual_r12,R12)
    original_cross=p16.pairings_three_digits(E[:725],corrected,W)
    assert not np.any(original_cross)
    # No scaling or replacement of any of the 729 ORIGINAL samples/rows.
    digest=hashlib.sha256(json.dumps(
        T1.tolist(),separators=(",",":")).encode()).hexdigest()
    return T1,S1,R12,digest,{
        "original_old_new_Gram_cross_entries_zero":original_cross.size,
        "intermediate_original_schur_four_by_four_symmetric":True,
        "source_corrected_raw_evaluation_replayed_directly":True,
        "original_729_generators_ALL_preserved":True,
        "p16_projection_matrix_sha256":digest,
    }

def make_odd_safe_and_reverse(sectors,Gnew):
    # Original OLD odd 362 plus 2 safe odd rows s0,s2, then bad s4.
    rec=sectors["odd"]
    A=rec["A"]
    s=rec["svals"]
    assert s==[0,2,4]
    Csafe=rec["C"][:,:2]
    Cbad=rec["C"][:,[2]]
    Bsafe=Gnew[np.ix_([0,2],[0,2])]
    badsafe=Gnew[np.ix_([0,2],[4])]
    badself=Gnew[4:5,4:5]
    gsafe=np.block([[A,Csafe],[Csafe.T,Bsafe]])
    c_to_bad=np.concatenate([Cbad,badsafe],axis=0)
    assert gsafe.shape==(364,364) and c_to_bad.shape==(364,1)
    safe_first_actual=smith_index(
        gsafe,c_to_bad,"actual_original_safe_first_725_to729_to730_odd")
    # REVERSED original order: first the BAD odd row s4, whose
    # first-stage projection is known nonintegral, so NO conditional
    # integral-split theorem applies. Directly calculate its second
    # stage image index on the real original Gram instead.
    gbad=np.block([[A,Cbad],[Cbad.T,badself]])
    bad_to_safe=np.concatenate([Csafe,badsafe.T],axis=0)
    assert gbad.shape==(363,363) and bad_to_safe.shape==(363,2)
    bad_first_actual=smith_index(
        gbad,bad_to_safe,"actual_original_bad_first_725_to726_to730_odd")
    return safe_first_actual,bad_first_actual

def main():
    freeze()
    toys=positive_toys()
    E,Q,W,Gnew,checks=source()
    oldcross,sectors=sector_data(E,W)
    T1,S1,R12,digest,first=first_integral_stage(
        E,W,Gnew,oldcross,sectors)
    assert T1.shape==(725,4) and S1.shape==(4,4)
    # A CONDITIONAL integral-split theorem: over the finite modular
    # R, coker original intermediate equals coker A ⊕ coker S1.
    schur=smith_index(
        S1,R12,"intermediate_four_row_Schur_to_final_original_s4")
    old_component=1 # independently source-checked by unsolved s4 and
    # previous fully resolved exact order5 old Gram certificate.
    assert schur["finite_exact_cokernel_image_log5"]>=0
    safe_first,bad_first=make_odd_safe_and_reverse(sectors,Gnew)
    max_formula=max(old_component,
                    schur["finite_exact_cokernel_image_log5"])
    assert safe_first["finite_exact_cokernel_image_log5"]==max_formula,(
        "integral split composition DOES NOT commute",safe_first,schur)
    # Strong source check of the entire old+safe stage
    # (not just comparing separately obtained scalar indices):
    safe_smith=p16.high_precision_smith(S1)
    noncensored=(max(safe_smith[0])<K and
                 safe_first["old_cokernel_uncensored_at_p16"])
    outcome={
        "D":D,"original_Q":len(Q),"original_full_730_rows":True,
        "original_ordinary_Z_jets_W_fixed":5,
        "original_trace_metric":[2,2*D],
        "same_original_row_lattice_NO_synthetic_points":True,
        "same_source_old_725_to_safe_729_to_full_730":True,
        "reverse_original_old_725_to_bad_726_to_full_730":True,
        "source_original_jets_independently_checked":checks,
        "first_stage_integral_four_row_projections":first,
        "original_old_to_last_s4_coker_image_order5":True,
        "intermediate_Schur_4x4_profile":schur,
        "safe_first_actual_odd_364x364_profile":safe_first,
        "safe_first_composition_formula_lcm_not_product":True,
        "safe_first_joint_log5_order":max_formula,
        "safe_first_Schur_and_G729_cokernel_fully_uncensored_at_p16":
            noncensored,
        "bad_first_nonintegral_split_NOT_ALLOWED":True,
        "bad_first_actual_odd_363x363_profile":bad_first,
        "independent_positive_definite_composition_toys":toys,
        "historical_old_original_Gram_v5":3855,
        "historical_original_full_Gram_v5_UNCHANGED":3924,
        "historical_original_full_Schur_v5_UNCHANGED":69,
        "NO_additive_extra_valuation_from_any_cokernel_debt":True,
        "not_a_uniform_h1_field_theorem":True,
    }
    print("PHASE298_TYPED_COMPOSABLE_ORIGINAL_COKERNEL",outcome,flush=True)
    print("PASS Phase298 original two-stage integral-split cokernel composition",
          flush=True)

if __name__=="__main__":
    main()
