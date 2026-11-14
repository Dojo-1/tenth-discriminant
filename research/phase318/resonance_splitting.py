#!/usr/bin/env python3
"""Phase318-D: exact common 3+4+10 splitting of the radical resonance.

For ORIGINAL D163 Q109 source, on the 17d mod5 Gram radical:
  B0 = 5^-1 K^T G K (mod5), rank7.
  N  = K^T deltaG_i K (mod5), first nonzero local wild normal,
       rank4, with B3=B0+3N of rank3.
Because rank B0=rank B3+rank N=7, the row/image spaces of
B3 and N are disjoint, and a common exact F5 basis has
  B3=diag(A3,0,0)
  N =diag(0,A4,0)
with blocks sizes 3,4,10, A3 and A4 nonsingular.

Thus the five-parameter pencil is literally
  B_lambda=diag(A3,(lambda-3)A4,0_10),
explaining the quartic 7x7 determinant minor resonance. This
is fixed-field finite algebra, not a proof of a field-uniform
class-number-one valuation or a new discriminant cutoff.
"""
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313",
               "phase314","phase315","phase316","phase317","phase318"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from inert_trace_radicals import rank_f5
from conductor250_original_mod25 import original_integer_source_oracle
from local_wild_normal import signed_unit_sites,site_differentials
from radical_tangent import kernel_basis_mod5,first_radical_form
from normal_pencil import determinant_mod5

P=5


def require_rank_additive(a,b,c):
    ra=rank_f5(a)
    rb=rank_f5(b)
    rc=rank_f5(c)
    if ra+rb!=rc:
        raise ValueError("forms do not have disjoint images: rank additivity failed")
    concatenated=np.hstack((a,b))%P
    stacked=np.vstack((a,b))%P
    if rank_f5(concatenated)!=rc or rank_f5(stacked)!=rc:
        raise ValueError("forms do not have full disjoint row/column images")
    return ra,rb,rc


def extend_common_kernel(common,larger,add):
    """Choose lex-first independent complement vectors within kernel."""
    n=common.shape[0]
    assert larger.shape[0]==n
    seed=[common[:,j] for j in range(common.shape[1])]
    assert rank_f5(common)==len(seed)
    complement=[]
    for j in range(larger.shape[1]):
        v=larger[:,j]
        trial=np.column_stack(seed+complement+[v])%P
        if rank_f5(trial)==len(seed)+len(complement)+1:
            complement.append(v)
        if len(complement)==add:
            break
    if len(complement)!=add:
        raise ValueError("could not construct requested common-kernel complement")
    result=np.column_stack(complement)%P
    assert rank_f5(np.column_stack((common,result))%P)==(
        common.shape[1]+add)
    return result


def resonance_common_splitting():
    qint,qomega,G,_=original_integer_source_oracle()
    sites,_=signed_unit_sites(qomega)
    bases,mats=site_differentials(sites)
    K,_,_=kernel_basis_mod5(G%P)
    assert K.shape==(40,17)
    B0=first_radical_form(G,K)
    normals=[(K.T@h@K)%P for h in mats]
    first=next(i for i,n in enumerate(normals) if np.any(n))
    N=normals[first]
    Bres=(B0+3*N)%P
    assert np.array_equal(B0,B0.T)
    assert np.array_equal(N,N.T)
    assert np.array_equal(Bres,Bres.T)
    ranks=require_rank_additive(Bres,N,B0)
    assert ranks==(3,4,7)
    kerN,_,_=kernel_basis_mod5(N)
    kerB,_,_=kernel_basis_mod5(Bres)
    common,_,_=kernel_basis_mod5(np.vstack((Bres,N)))
    assert kerN.shape==(17,13)
    assert kerB.shape==(17,14)
    assert common.shape==(17,10)
    assert not np.any(N@common%P)
    assert not np.any(Bres@common%P)

    W3=extend_common_kernel(common,kerN,3)
    W4=extend_common_kernel(common,kerB,4)
    assert not np.any(N@W3%P)
    assert not np.any(Bres@W4%P)
    basis=np.column_stack((W3,W4,common))%P
    assert basis.shape==(17,17) and rank_f5(basis)==17

    BA=(basis.T@Bres@basis)%P
    BN=(basis.T@N@basis)%P
    A3=BA[:3,:3]
    A4=BN[3:7,3:7]
    expected_BA=np.zeros((17,17),dtype=np.int64)
    expected_BN=np.zeros((17,17),dtype=np.int64)
    expected_BA[:3,:3]=A3
    expected_BN[3:7,3:7]=A4
    assert np.array_equal(BA,expected_BA),(
        "B_res has forbidden off-block coupling")
    assert np.array_equal(BN,expected_BN),(
        "N has forbidden off-block coupling")
    assert rank_f5(A3)==3 and rank_f5(A4)==4
    det3=determinant_mod5(A3)
    det4=determinant_mod5(A4)
    assert det3 and det4

    records=[]
    const=det3*det4%P
    for lam in range(5):
        observed=(basis.T@((B0+lam*N)%P)@basis)%P
        expected=expected_BA+((lam-3)%P)*expected_BN
        expected%=P
        assert np.array_equal(observed,expected),(
            "17x17 common splitting failed",lam)
        rank=rank_f5(observed)
        assert rank==(3 if lam==3 else 7)
        det7=determinant_mod5(observed[:7,:7])
        assert det7==const*pow((lam-3)%P,4,P)%P
        earlier_7minor=determinant_mod5(
            ((B0+lam*N)%P)[np.ix_(range(10,17),range(10,17))])
        assert earlier_7minor==4*pow((lam-3)%P,4,P)%P
        records.append({
            "lambda":lam,
            "exact_split_rank":rank,
            "upper_7x7_block_determinant":det7,
            "old_fixed_original_7x7_minor_determinant":earlier_7minor,
            "all_289_entries_of_split_pencil_verified":True,
        })

    # A deliberately WRONG generalization: two identical rank-one
    # symmetric operators have overlapping images, no additive rank.
    hostile=np.asarray([[1,0],[0,0]],dtype=np.int64)
    rejected=False
    try:
        require_rank_additive(hostile,hostile,
                              (hostile+hostile)%P)
    except ValueError:
        rejected=True
    assert rejected

    return {
        "D":163,
        "same_native_original_integer_order_Q":len(qomega),
        "same_native_original_Gram_mod5_radical_dim":K.shape[1],
        "normal_generator_first_signed_original_site":sites[first],
        "rank_B_original":rank_f5(B0),
        "rank_N":rank_f5(N),
        "rank_B_resonant_lambda3":rank_f5(Bres),
        "rank_sum_exactly_additive":True,
        "common_kernel_dimension":common.shape[1],
        "nondegenerate_complement_dimensions":[W3.shape[1],W4.shape[1]],
        "simultaneous_split_basis_dimensions":[3,4,10],
        "common_GL17_F5_basis_invertible":True,
        "nondegenerate_block_determinants_mod5":[det3,det4],
        "nonzero_quartic_block_minor_leading_constant_mod5":const,
        "exact_5_lambda_split_and_quartic_minors":records,
        "all_289_block_entries_verified_per_lambda":True,
        "noncomplementary_symmetric_pair_hostile_rejected":rejected,
        "no_universal_class_number_or_full_valuation_claim":True,
    }


def main():
    print("PHASE318_3_PLUS_4_PLUS_10_RESONANCE_SPLITTING_PASS",
          resonance_common_splitting(),flush=True)


if __name__=="__main__":
    main()
