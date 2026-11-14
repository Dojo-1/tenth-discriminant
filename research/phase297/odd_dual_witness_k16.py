#!/usr/bin/env python3
"""Phase297-C: explicit p^14 odd-sector dual obstruction to integral Schur.

Preregistered at 4eea98d BEFORE code/results. Independent original
D587 row functional detects nonmembership of cross pairing columns
in old Gram image; no original determinant double counting.
"""
import base64
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zlib

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase292","phase297"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
import original_schur_integrality_k16 as parent

P=5
K=16
MOD=P**K
WITNESS_MOD=P**14
D=587
FROZEN_PARENT={
    "research/phase297/original_schur_integrality_k16.py":
       "aa3678001c69a7235dca638638d2dab4c55b05b3",
    "research/phase297/original_schur_integrality.py":
       "6ce23a8136ddd6208ef70d00a2bca419a105fdbb",
}
EXPECTED_ODD_OLD={
     0:62,2:15,3:48,4:62,5:48,6:10,7:5,8:50,9:12,12:20,14:30,
}
EXPECTED_ODD_AUG={
     0:62,2:15,3:48,4:62,5:48,6:10,7:5,8:50,9:12,12:20,13:1,14:29,
}

def freeze():
    parent.freeze()
    for path,sha in FROZEN_PARENT.items():
        actual=subprocess.check_output(
           ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
        assert actual==sha,("parent source changed",path,actual,sha)

def smith_with_left_witness(A0):
    """Smith valuations + ACTUAL left unimodular U, no metric column map.

    U A_original V = diagonal mod p^16 for some internal V. We do NOT
    need V to certify a row ell of U, since row ell*A_original is then
    divisible by p^e across ALL original columns. Check directly.
    """
    A=np.asarray(A0,dtype=object)%MOD
    n,m=A.shape
    assert n==m==362
    U=np.eye(n,dtype=object)
    levels=[]
    for i in range(n):
        tail=A[i:,i:]
        pivot=None
        first=levels[-1] if levels else 0
        for v in range(first,K):
            hit=np.argwhere(tail%(P**(v+1))!=0)
            if len(hit):
                rr,cc=map(int,hit[0])
                pivot=(v,i+rr,i+cc)
                break
        assert pivot is not None,("unexpected grade K censorship",i)
        e,r,c=pivot
        if r!=i:
            A[[i,r]]=A[[r,i]]
            U[[i,r]]=U[[r,i]]
        if c!=i:A[:,[i,c]]=A[:,[c,i]]
        divisor=P**e
        assert int(A[i,i])%divisor==0
        quotient=MOD//divisor
        inv=pow(int(A[i,i])//divisor,-1,quotient)
        if i+1<n:
            col=A[i+1:,i]
            assert all(int(x)%divisor==0 for x in col)
            coeff=(col//divisor*inv)%quotient
            A[i+1:,i+1:]=(A[i+1:,i+1:]
                -coeff[:,None]*A[i,i+1:])%MOD
            U[i+1:,:]=(U[i+1:,:]-coeff[:,None]*U[i,:])%MOD
            A[i+1:,i]=0
        assert all(int(x)%divisor==0 for x in A[i,i+1:])
        A[i,i+1:]=0
        levels.append(e)
        if (i+1)%100==0 or i+1==n:
            print("PHASE297C_TRACKED_SMITH",{
                "rows_processed":i+1,"n":n,"grade":e},flush=True)
    assert levels==sorted(levels)
    hist=dict(sorted(Counter(levels).items()))
    assert hist==EXPECTED_ODD_OLD,(hist,EXPECTED_ODD_OLD)
    assert not np.count_nonzero(
        np.asarray(A,dtype=object)-np.diag(np.diag(A)))
    assert parent.frozen_source.independent_rank(
        np.asarray(U,dtype=np.int64)%P)==n
    return levels,U

def valuation_at_p(x):
    x=int(x)%WITNESS_MOD
    if x==0:return 14
    v=0
    while x%P==0:
        x//=P
        v+=1
    return v

def dual_functional(A,C):
    levels,U=smith_with_left_witness(A)
    assert C.shape==(362,3)
    Aobj=np.asarray(A,dtype=object)
    Cobj=np.asarray(C,dtype=object)
    all_grade14=[i for i,e in enumerate(levels) if e==14]
    assert len(all_grade14)==30
    witness=None
    for index in all_grade14:
        ell=[int(x)%WITNESS_MOD for x in U[index]]
        ellobj=np.asarray(ell,dtype=object)
        old=(ellobj@Aobj)%WITNESS_MOD
        assert all(int(z)==0 for z in old),(
            "Smith left-row fails original Gram annihilation",index)
        new=(ellobj@Cobj)%WITNESS_MOD
        if any(int(z)!=0 for z in new):
            nz=[(j,valuation_at_p(new[j]),int(new[j]))
                for j in range(3) if new[j]]
            # Prior image quotient index1 forces an order5 witness.
            assert min(v for j,v,z in nz)==13,nz
            witness={"smith_old_row_index":index,
               "Smith_old_grade":14,
               "nonzero_original_coefficients_mod5":sum(
                   1 for z in ell if z%P),
               "all_original_old_Gram_column_pairings_zero_mod5pow14":362,
               "new_original_cross_pairings_mod5pow14":[int(z) for z in new],
               "cross_residue_valuations":[int(valuation_at_p(z)) for z in new],
               "first_detected_new_original_odd_row":int(nz[0][0]),
               "first_detected_v5":int(nz[0][1]),
               "witness_original_row_vector":ell}
            break
    assert witness is not None,(
       "expected one odd-sector original-dual functional, none found")
    ell=witness.pop("witness_original_row_vector")
    raw=json.dumps(ell,separators=(",",":")).encode("ascii")
    compressed=base64.b85encode(zlib.compress(raw,9)).decode("ascii")
    witness.update({
        "vector_length":len(ell),
        "vector_sha256_of_compact_json":hashlib.sha256(raw).hexdigest(),
        "vector_base85_zlib_compact_json":compressed,
        "reconstruction_python":"json.loads(zlib.decompress(base64.b85decode(s)).decode())",
        "direct_uncensored_obstruction_modulus":WITNESS_MOD
    })
    # Independent decoding and all original-source pairings check.
    recovered=json.loads(zlib.decompress(
        base64.b85decode(compressed)).decode("ascii"))
    assert recovered==ell
    obj=np.asarray(recovered,dtype=object)
    assert all(int(z)==0 for z in ((obj@Aobj)%WITNESS_MOD))
    assert any(int(z)!=0 for z in ((obj@Cobj)%WITNESS_MOD))
    return witness

def exact_denominator_test(Aodd,Codd,Aeven,Ceven):
    # Independent image computation, no reliance on the tracked U.
    old_odd,o=parent.high_precision_smith(Aodd)
    aug_odd,u=parent.high_precision_smith(
        np.concatenate((Aodd,Codd),axis=1))
    scaled_odd,scaled=parent.high_precision_smith(
        np.concatenate((Aodd,(P*Codd)%MOD),axis=1))
    old_even,e=parent.high_precision_smith(Aeven)
    aug_even,f=parent.high_precision_smith(
        np.concatenate((Aeven,Ceven),axis=1))
    assert o==EXPECTED_ODD_OLD and u==EXPECTED_ODD_AUG
    assert max(old_odd)==max(old_even)==14
    assert sum(old_odd)-sum(aug_odd)==1
    assert old_odd==scaled_odd
    assert old_even==aug_even
    assert f==e
    assert scaled==o
    return {
        "odd_order5_cross_class_p5_image_quotient":True,
        "odd_cross_not_integral_as_projection":True,
        "odd_five_times_cross_IN_original_old_Gram_Z5_image":True,
        "even_cross_ALREADY_in_original_old_Gram_Z5_image":True,
        "highest_old_Gram_elementary_divisor":14,
        "no_grade16_censorship":True,
        "full_five_row_orthogonal_projection_exact_denominator_exponent":1,
        "historical_original_Schur_det_v5_NOT_modified":69
    }

def toy_functionals():
    # Real positive 2x2 Gram toy with nonintegral 5-adic projection.
    ell=P**13
    assert (ell*10)%WITNESS_MOD==0
    assert (ell*2)%WITNESS_MOD!=0
    assert (ell*5)%WITNESS_MOD==0
    return {"positive_Gram_A10_C2_detected":True,
            "positive_Gram_A10_C5_not_false_positive":True}

def main():
    freeze()
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(53,146,5,5,383)
    toys=toy_functionals()
    C=parent.source_high_precision(Q)
    E,checks=parent.rebuild_original(C,Q)
    W=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    assert parent.sanity_original_gram(E,Q,W)==36
    sectors={}
    for parity in ("even","odd"):
        ids=[i for i in range(725) if (i//5+i%5)%2==
             (0 if parity=="even" else 1)]
        new=[i for i in range(725,730) if (i//5+i%5)%2==
             (0 if parity=="even" else 1)]
        A=parent.pairings_three_digits(E[ids],E[ids],W)
        G=parent.pairings_three_digits(E[ids],E[new],W)
        sectors[parity]=(A,G)
    Aodd,Codd=sectors["odd"]
    Aeven,Ceven=sectors["even"]
    assert Aodd.shape==(362,362) and Codd.shape==(362,3)
    assert Aeven.shape==(363,363) and Ceven.shape==(363,2)
    witness=dual_functional(Aodd,Codd)
    print("PHASE297C_ODD_EXPLICIT_ORIGINAL_DUAL_WITNESS",witness,flush=True)
    exact=exact_denominator_test(Aodd,Codd,Aeven,Ceven)
    print("PHASE297C_EXACT_FULL_D587_TRANSVERSE_LATTICE_DEBT",{
       "original_field":D,
       "original_Q":len(Q),
       "original_polynomial_rows_cut":725,
       "original_polynomial_rows_full":730,
       "original_ordinary_Z_jets_W_fixed":J,
       "original_trace_B":[2,2*D],
       "K":K,"modulus":MOD,
       "independent_original_jet_coordinate_checks":checks,
       "dual_original_odd_Gram_annihilator_certificate":witness[
           "vector_sha256_of_compact_json"],
       "exact_projection_integrality_and_one_power_test":exact,
       "hostile_controls":toys,
       "NOT_an_additional_original_Gram_determinant_factor":True,
       "not_a_uniform_class_number_one_field_theorem":True
    },flush=True)
    print("PASS Phase297-C original D587 odd dual witness and exact 5-adic projection denominator",
          flush=True)

if __name__=="__main__":
    main()
