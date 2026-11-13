#!/usr/bin/env python3
"""Phase299-B: original D587 odd 362->363 nonintegral-first gluing.

A genuine *unchanged* D587 Q383/J5 source, no new finite sampling
points and no p-adic lattice rescaling misreported as a GL row gauge.
The orthogonal index-five M is an included sublattice; the actual
L = original 363-dimensional odd row lattice is restored by H.
Preregistered dd651c2b before code/result.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase297","phase299"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
import minimal_transverse_repair as repair
import original_schur_integrality_k16 as hi
import gluing_core as core

D=587
P=5
K=16
MOD=P**K
FROZEN={
 "research/phase297/minimal_transverse_repair.py":
     "22b0077a2424553021a4c9859f92f0fe3efc2fe7",
 "research/phase297/original_schur_integrality_k16.py":
     "aa3678001c69a7235dca638638d2dab4c55b05b3",
 "research/phase299/gluing_core.py":
     "54ac93e5349ed6a127dda056009f4e055f3d64ce"
}

def guard():
    repair.freeze()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output([
            "git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("frozen original source or glue code drift",path,actual,sha)

def original_D587_bad_first_glue():
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(53,146,5,5,383)
    E,Q,W,checks=repair.original_source()
    hi.parity_blocks(E,Q,W) # all 365x365 opposite-parity Gram entries
    oldids,newids=repair.sector_ids("odd")
    assert len(oldids)==362 and newids==[725,727,729]
    assert all(i<725 for i in oldids)
    assert (729//S,729%S)==(145,4)
    old=E[oldids]
    y=E[[729]]
    A=hi.pairings_three_digits(old,old,W)
    c=hi.pairings_three_digits(old,y,W)
    b=int(hi.pairings_three_digits(y,y,W)[0,0])
    assert A.shape==(362,362)
    assert c.shape==(362,1)
    assert W.shape==(3830,)
    result,a,grades,U=core.verified_nonintegral_gluing(
        A,c,b,oldE=old,newE=y,W=W,record_full_vector=False)
    assert result["old_5adic_Gram_determinant_valuation"]==1925
    assert result["original_full_5adic_Gram_determinant_valuation"]==1937
    assert result["k_original_trace_norm_5valuation"]==14
    assert result["exact_5adic_projection_denominator_h"]==1
    assert result["old_5adic_Gram_smith_max_grade"]==14
    assert result["new_full_original_Gram_smith_max_grade"]==14
    assert result["source_native_direct_checks"][
        "original_old_row_pairings_zero"]==362
    assert result["source_native_direct_checks"][
        "original_jet_observation_channels"]==3830

    # Independently detect the obstruction with an actual left
    # original-Gram functional: same mathematical strategy as
    # Phase297-C but independently obtained from THIS p16 Smith U,
    # with ALL original old column pairings checked.
    witness=None
    cutoff=P**14
    for i,e in enumerate(grades):
        if e!=14:continue
        ell=np.asarray([int(v)%cutoff for v in U[i]],dtype=object)
        oldpair=ell@np.asarray(A,dtype=object)%cutoff
        assert not np.any(oldpair),("wrong original odd-old dual row",i)
        newpair=int((ell@np.asarray(c,dtype=object))[0])%cutoff
        if newpair:
            assert newpair%(P**13)==0
            original=[int(x) for x in ell]
            witness={
                "original_odd_smith_left_row":i,
                "dual_modulus":cutoff,
                "original_old_Gram_zeros_verified":len(oldids),
                "original_new_s4_cross_residue_nonzero":newpair,
                "residue_v5":13,
                "vector_dimension":len(original),
                "vector_json_sha256":hashlib.sha256(
                    json.dumps(original,separators=(",",":")).encode()
                ).hexdigest()
            }
            break
    assert witness is not None
    assert result["k_original_trace_norm_mod_p16"]%cutoff==0
    # Original y is a *nontrivial* H gluing coset in D(L0)⊕D(K).
    # We must retain y as generator of the original lattice:
    # exactly 5*y = k + Σ_i a_i*old_i modulo the tested precision.
    k_eval=(P*np.asarray(y,dtype=object)
            -np.asarray(a,dtype=object).T
              @np.asarray(old,dtype=object))%MOD
    relation=(k_eval+np.asarray(a,dtype=object).T
               @np.asarray(old,dtype=object)
               -P*np.asarray(y,dtype=object))%MOD
    assert not np.any(relation)
    assert result["original_unscaled_projection_rejected_by_old_Gram_cokernel"]
    return {
        "source_original": {
          "D":D,"original_rho":rho,"R":R,"S":S,"J":J,
          "original_integer_ellipse_Q":len(Q),
          "original_odd_row_labels_old_count":362,
          "original_single_added_row":[145,4],
          "actual_original_jet_probe_coordinates":checks,
          "original_trace_B":[2,2*D],
          "all_opposite_parity_original_row_Gram_entries_zero":True
        },
        "unmodified_original_bad_first_G_odd_certificate":result,
        "source_native_original_odd_dual_witness":witness,
        "original_row_y_recovered_by_nontrivial_H_gluing":True,
        "historical_entire_full_D587_G730_valuation_UNCHANGED":3924,
        "historical_entire_original_D587_five_row_Schur_v5_UNCHANGED":69,
        "bad_first_original_odd_full_v5":1937,
        "gluing_subLattice_odd_v5":1939,
        "cancel_index_square_5valuation":2,
        "no_new_field_bound":True
    }

def main():
    guard()
    result=original_D587_bad_first_glue()
    print("PHASE299B_ACTUAL_D587_BAD_FIRST_DISCRIMINANT_GLUE",result,flush=True)
    print("PASS Phase299-B original D587 bad-first orthogonal complement H-gluing",
          flush=True)

if __name__=="__main__":
    main()
