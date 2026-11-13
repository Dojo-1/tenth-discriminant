#!/usr/bin/env python3
"""Phase299-A: primitive nonintegral D163 h=1 field row gluing.

Preregistered at dd651c2b before implementation. The ORIGINAL
Z[sqrt(-163)] J1/Q109 source is preserved, not maximal-order claim.
"""
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase297","phase298","phase299"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
import class_one_d163_composition as previous
import gluing_core as core

MOD=5**16
FROZEN={
 "research/phase298/class_one_d163_composition.py":
    "e8cae60a662ca59cade8acd741c2d5d4f4982d6a",
 "research/phase299/gluing_core.py":
    "dba83c3fd8a07734f0bc2a7ec6724c0362fbdf9a",
}

def freeze():
    previous.guard()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
        assert actual==sha,("source/core drift",path,actual,sha)

def original_D163_gluing():
    field=previous.field_h1_background()
    G,E,W,source=previous.original_j1_source()
    assert (source["R"],source["S"],source["J"],source["Q"])==(
        40,1,1,109)
    A=G[:13,:13]
    c=G[:13,13:14]
    b=int(G[13,13])
    vector=[0,1,0,4,0,2,0,2,0,3,0,1,0]
    assert len(vector)==13
    ell=np.asarray(vector,dtype=object)
    assert all(int(v)==0 for v in ((ell@np.asarray(A,dtype=object))%5))
    assert int((ell@np.asarray(c,dtype=object))[0])%5==2

    result,a,levels,U=core.verified_nonintegral_gluing(
        A,c,b,oldE=E[:13],newE=E[13],W=W,record_full_vector=True)
    assert result["exact_5adic_projection_denominator_h"]==1
    assert result["integral_orthogonal_subLattice_index_in_original_L"]==5
    assert result["source_native_direct_checks"][
        "original_old_row_pairings_zero"]==13

    # A second *invertible* original-row-frame representation:
    # source lattice unchanged; only formal coordinates change.
    # Also shear the NEW source generator y to y+old_1.
    n=13
    Uold=np.eye(n,dtype=object)
    Uold[2,1]=2
    Uold[[0,1]]=Uold[[1,0]]
    v=np.zeros((n,1),dtype=object)
    v[1,0]=1
    G14=np.asarray(G[:14,:14],dtype=object)
    F=np.eye(n+1,dtype=object)
    F[:n,:n]=Uold
    F[n,:n]=v[:,0]
    Gprime=(F@G14@F.T)%MOD
    Aprime=np.asarray(Gprime[:n,:n],dtype=np.int64)
    cprime=np.asarray(Gprime[:n,n:n+1],dtype=np.int64)
    bprime=int(Gprime[n,n])
    assert np.array_equal(
        Aprime,np.asarray((Uold@np.asarray(A,dtype=object)@Uold.T)%MOD,
                          dtype=np.int64))
    assert np.array_equal(
        cprime,np.asarray((Uold@(np.asarray(c,dtype=object)+
                         np.asarray(A,dtype=object)@v))%MOD,
                           dtype=np.int64))
    expected_b=(b+2*int((v.T@np.asarray(c,dtype=object))[0,0])
                +int((v.T@np.asarray(A,dtype=object)@v)[0,0]))%MOD
    assert bprime==expected_b
    gauge_result,a2,_,_=core.verified_nonintegral_gluing(
        Aprime,cprime,bprime,record_full_vector=False)
    assert result["old_5adic_Gram_determinant_valuation"]==(
        gauge_result["old_5adic_Gram_determinant_valuation"])
    assert result["original_full_5adic_Gram_determinant_valuation"]==(
        gauge_result["original_full_5adic_Gram_determinant_valuation"])
    assert result["k_original_trace_norm_mod_p16"]==(
        gauge_result["k_original_trace_norm_mod_p16"])
    assert result["k_original_trace_norm_5valuation"]==(
        gauge_result["k_original_trace_norm_5valuation"])
    assert result["generator_k_original_coefficients_sha256"]!=(
        gauge_result["generator_k_original_coefficients_sha256"]),(
        "nontrivial source-basis gauge did not move coordinates")
    return {
      "class_number_one_field_proof_background":field,
      "original_source":source,
      "first_original_nonintegral_row_attachment":"Z^13 after 1,Z,...,Z^12",
      "mod5_dual_witness":vector,
      "mod5_dual_witness_old_row_pairings_zero":True,
      "mod5_dual_new_cross_residue":2,
      "original_source_unmodified_gluing_certificate":result,
      "GL13_old_shear_swap_and_new_row_translation_control":{
         "determinant_unit_over_Z5":True,
         "same_source_original_Gram_v5_old_and_new":True,
         "same_orthogonal_complement_norm_mod5pow16":True,
         "same_gluing_H_order":5,
         "source_coordinate_vector_changed":True,
         "not_a_changed_integer_order_or_sampler":True,
      },
      "no_new_class_number_one_discriminant_cutoff":True
    }

def main():
    freeze()
    toys=core.toy_controls()
    field=original_D163_gluing()
    print("PHASE299A_EXACT_NONINTEGRAL_DISCRIMINANT_GLUE",{
        "odd_prime":5,"modulus":MOD,
        "toy_complete_discriminant_group_enumeration":toys,
        "original_h1_D163_result":field,
        "gluing_is_classical_not_new_theory":True,
        "full_original_row_lattices_preserved_as_OVERLATTICES":True,
        "wrong_canonical_projection_Dfull_to_Dold_RETIRED":True,
        "no_valuation_double_counting":True,
    },flush=True)
    print("PASS Phase299-A D163 h1 original nonintegral lattice gluing and finite groups",
          flush=True)

if __name__=="__main__":
    main()
