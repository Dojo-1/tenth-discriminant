#!/usr/bin/env python3
"""Phase301-B: explicit source-original D163 joint nonintegrality dual.

Case (13,27,31) selected RETROSPECTIVELY as first nonzero result
of full preregistered Phase301-A 176-case CI; this witness experiment
was independently preregistered at 40e720d2 before its code/results.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for part in ("phase206","phase297","phase298","phase299","phase300","phase301"):
    sys.path.insert(0,str(ROOT/"research"/part))
import class_one_d163_composition as original
import joint_same_parity_census as parent
import minimal_transverse_repair as solver
import double_glue_original as source_smith

P=5
K=16
MOD=P**K
N=13
S=27
T=31
PARENT_SHA="acd72002911b284bea6fda100435f552756c1532"

def guard():
    parent.guard()
    path="research/phase301/joint_same_parity_census.py"
    actual=subprocess.check_output([
        "git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
    ).strip()
    assert actual==PARENT_SHA,("Phase301-A source changed",actual)

def v5(x):
    v=int(x)
    if v==0:return 10**9
    k=0
    while v%P==0:
        v//=P
        k+=1
    return k

def raw_weighted(left,right,W,modulus):
    """Direct original E/trace weight contraction; no SNF observation map."""
    L=np.asarray(left,dtype=object)
    R=np.asarray(right,dtype=object)
    ww=np.asarray(W,dtype=object)
    return ((L*ww[None,:])@R.T)%modulus

def positive_individual_projections(G,E,W):
    original_rows=list(range(14))
    A=G[:14,:14]
    levels,diag,U,V=solver.tracked_smith_solver(A)
    assert max(levels)<K
    result=[]
    for r in (S,T):
        c=G[np.ix_(original_rows,[r])]
        assert source_smith.debt(A,c)==0
        x,issues=solver.can_solve_or_fail(
            levels,diag,U,V,A,c,True)
        assert x is not None and not issues
        assert not np.any((np.asarray(A,dtype=object)@
              np.asarray(x,dtype=object)-
              np.asarray(c,dtype=object))%MOD)
        corrected=(np.asarray(E[[r]],dtype=object)-
                  np.asarray(x,dtype=object).T@
                  np.asarray(E[original_rows],dtype=object))%MOD
        assert not np.any(raw_weighted(
            corrected,E[original_rows],W,MOD))
        result.append({
            "original_new_row":r,
            "old_original_rows":len(original_rows),
            "integral_projection_verified_mod5pow16":True,
            "original_source_old_cross_pairings_zero":len(original_rows)
        })
    return result

def original_dual_witness(G,E,W):
    original_rows=list(range(14))+[S]
    assert len(original_rows)==15
    A=G[np.ix_(original_rows,original_rows)]
    c=G[np.ix_(original_rows,[T])]
    assert source_smith.debt(A,c)==1
    levels,diagonal,U,V=solver.tracked_smith_solver(A)
    assert max(levels)<K
    impossible,issues=solver.can_solve_or_fail(
        levels,diagonal,U,V,A,c,False)
    assert impossible is None and issues
    observed=None
    for i,e in enumerate(levels):
        if e==0:continue
        modulus=P**e
        ell=[int(value)%modulus for value in U[i]]
        vector=np.asarray(ell,dtype=object)
        old=(vector@np.asarray(A,dtype=object))%modulus
        assert not np.any(old),("old annihilation failed",i,e)
        new=int((vector@np.asarray(c,dtype=object))[0])%modulus
        if new==0:continue
        # Independently construct the actual weighted observation
        # functional on the original raw 109-point j0 E rows.
        f=(vector[None,:]@
           np.asarray(E[original_rows],dtype=object))%modulus
        by_source=raw_weighted(f,E[original_rows],W,modulus)
        assert not np.any(by_source),(
            "source trace old-row annihilator mismatch",i,e)
        source_new=int(raw_weighted(f,E[[T]],W,modulus)[0,0])
        assert source_new==new and source_new!=0
        # The exact image index in the full old Gram cokernel is
        # order five, so the detected element has order five.
        assert v5(new)==e-1
        digest=hashlib.sha256(json.dumps(
            ell,separators=(",",":")).encode()).hexdigest()
        observed={
            "original_old_row_labels_Z_powers":original_rows,
            "nonintegrally_attached_original_Z_power":T,
            "original_old_Gram_rank":15,
            "old_original_Gram_max_p_smith_exponent":max(levels),
            "actual_smith_row_index_for_dual":i,
            "dual_modulus":modulus,
            "dual_grade":e,
            "full_original_15_component_dual_row_vector":ell,
            "all_old_original_Gram_pairings_zero":15,
            "new_cross_pairing_mod5pow_grade":new,
            "new_cross_pairing_5valuation":v5(new),
            "short_vector_compact_json_sha256":digest,
            "native_original_source_j0_trace_B_crosscheck":True,
            "original_sampled_109_points_and_218_real_imag_channels":True,
            "no_synthetic_observations_or_valuation_double_counting":True
        }
        break
    assert observed is not None
    return observed

def main():
    guard()
    field=original.field_h1_background()
    G,E,W,meta=original.original_j1_source()
    assert (meta["R"],meta["S"],meta["J"],meta["Q"])==(40,1,1,109)
    assert parent.symmetry(G,E,W)[
        "exact_original_mixed_parity_Gram_zeros"]==800
    positive=positive_individual_projections(G,E,W)
    witness=original_dual_witness(G,E,W)
    print("PHASE301B_ORIGINAL_FIRST_JOINT_DUAL_CERTIFICATE",{
        "field_class_one_background":field,
        "original_integer_order_sample":meta,
        "first_nonzero_176_case_selected_retrospectively":[N,S,T],
        "both_future_original_rows_integral_to_L14":positive,
        "now_Z31_not_integral_after_adjoining_Z27":witness,
        "no_global_h1_class_number_or_new_discriminant_cutoff_claim":True
    },flush=True)
    print("PASS Phase301-B explicit 15-vector original D163 higher-order dual",flush=True)

if __name__=="__main__":
    main()
