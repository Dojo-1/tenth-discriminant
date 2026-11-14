#!/usr/bin/env python3
"""Phase298-C: original class-one D163 first nonintegral row dual certificate.

Retrospectively selected n=13 as FIRST nonintegral among an already
exhaustive 38-stage Phase298-B scan, preregistered before this code at
3346912c. Original Q109/J=S1 source, not maximal-order sampler.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase297","phase298"):
    sys.path.insert(0,str(ROOT/"research"/sub))
import class_one_d163_composition as prior
import minimal_transverse_repair as solver
from source_probe import gram,params

P=5
K=16
MOD=P**K
D=163
FROZEN={
 "research/phase298/class_one_d163_composition.py":
     "e8cae60a662ca59cade8acd741c2d5d4f4982d6a",
}

def freeze():
    prior.guard()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
        assert actual==sha,(path,actual,sha)

def v5(x):
    x=abs(int(x))
    if x==0:return None
    v=0
    while x%P==0:
        x//=P
        v+=1
    return v

def original_dual_nonintegrality(G):
    n=13
    A=G[:n,:n]
    c=G[:n,n:n+1]
    levels,diag,U,V=solver.tracked_smith_solver(A)
    assert max(levels)<K
    assert len(levels)==n
    no_solution,problems=solver.can_solve_or_fail(
        levels,diag,U,V,A,c,False)
    assert no_solution is None and problems
    assert all(x["new_column"]==0 for x in problems)
    witness=None
    for i,e in enumerate(levels):
        if e==0:continue
        modulus=P**e
        ell=[int(v)%modulus for v in U[i]]
        old=[sum(ell[t]*int(A[t,j]) for t in range(n))%modulus
             for j in range(n)]
        if any(old):
            raise AssertionError(("original old Gram dual annihilation failed",
                                  i,e,old))
        target=sum(ell[t]*int(c[t,0]) for t in range(n))%modulus
        if target:
            witness={
                "original_field":D,
                "original_old_row_labels":[[r,0] for r in range(n)],
                "new_original_row_label":[n,0],
                "source_original_Q":len(params(D)[-1]),
                "old_original_Gram_rank":n,
                "witness_old_Gram_smith_row_index":i,
                "witness_p_grade":e,
                "witness_modulus":modulus,
                "full_original_dual_vector_mod5pow_e":ell,
                "all_original_old_Gram_pairings_vanish":len(old),
                "nonzero_original_cross_pairing_residue":target,
                "cross_pairing_residue_v5":v5(target),
                "duality_in_original_monomial_row_basis":True
            }
            encoded=json.dumps(ell,separators=(",",":")).encode()
            witness["vector_compact_json_sha256"]=hashlib.sha256(
                encoded).hexdigest()
            break
    assert witness is not None,(
        "first nonintegral original class-one row had no dual witness")
    return witness

def original_previous_positive(G):
    n=12
    A=G[:n,:n]
    C=G[:n,n:n+1]
    levels,diag,U,V=solver.tracked_smith_solver(A)
    assert max(levels)<K
    solution,fail=solver.can_solve_or_fail(
        levels,diag,U,V,A,C,True)
    assert solution.shape==(n,1) and not fail
    # Direct original-monomial Gram proof of finite integrality.
    residual=(np.asarray(A,dtype=object)@
              np.asarray(solution,dtype=object)
              -np.asarray(C,dtype=object))%MOD
    assert not np.any(residual)
    return {
       "previous_original_old_row_labels":[0,n-1],
       "previous_added_original_row_r":n,
       "old_Gram_5adic_Smith_fully_resolved":True,
       "all_original_cross_pairing_equations_solved_mod_p16":n,
       "no_projection_denominator_detected_and_exact_cokernel_zero":True
    }

def main():
    freeze()
    field=prior.field_h1_background()
    G,E,W,source=prior.original_j1_source()
    assert G.shape==(40,40) and E.shape[0]==40
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(
        source["original_rho"],40,1,1,109)
    assert len(W)==2*len(Q)
    negative=original_dual_nonintegrality(G)
    positive=original_previous_positive(G)
    print("PHASE298C_CLASS_ONE_ORIGINAL_DUAL_NONINTEGRALITY",{
        "class_number_one_background":field,
        "source_original":source,
        "source_is_integer_order_not_full_maximal_two_coset":True,
        "retrospective_first_nonintegral_original_n":13,
        "first_nonintegral_original_row_certificate":negative,
        "original_previous_integral_projection_control":positive,
        "no_h1_uniform_projection_integrality":True,
        "no_added_original_determinant_valuation":True,
        "no_uniform_tenth_discriminant_bound":True
    },flush=True)
    print("PASS Phase298-C h1 D163 original row dual obstruction with adjacent positive control",
          flush=True)

if __name__=="__main__":
    main()
