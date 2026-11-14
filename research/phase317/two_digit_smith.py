#!/usr/bin/env python3
"""Phase317-B: exact TWO Smith layers of the SAME original Gram mod25.

A in Mat_n(Z/25): the number e0 of 5-adic Smith factors of exponent0
equals rank_F5(A mod5). Eliminate all 5-adic unit pivots by INVERTIBLE
row/column operations over Z/25. The residual Schur complement is
divisible by5. Then e1=rank_F5((residual/5) mod5), and
e>=2=n-e0-e1. This counts only the FIRST TWO exponent strata: it
does not determine total v5(det), full deeper Smith or a new field
bound. Counts are invariant under GL_n(Z/25) equivalence.

Fixed D163 NATIVE ORIGINAL integer-order source Q109/R40:
compare actual Gram mod25 with all five synthetic conjugation-covariant
norm-preserving gauge shifts k*t, t=(20,10). They agree mod5 and
differ only at norm164 in the source. E1 can stay constant or change;
we DO NOT assume the outcome.
"""
from collections import Counter
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313","phase314",
               "phase315","phase316","phase317"):
    sys.path.insert(0,str(ROOT/"research"/folder))

from inert_trace_radicals import rank_f5
from wild_log125 import exhaustive_lift_table
from wild_gauge import actual_original_ray_twist,shifted_ray_tag,T,M
from conductor250_original_mod25 import (
    original_integer_source_oracle,unit_and_nonunit_counts,
    gram_from_unit_rays_and_nonunit_lifts
)
from realization_obstruction import signed_ideal_spectra_for_original_source

MOD=25
P=5
D=163


def two_smith_slices(mat):
    """Unimodular Smith filtration (e=0, e=1, e>=2) over Z/25.

    Deliberately independent of sympy/SNF implementation and any
    heuristic real matrix rank. Every pivot must be a unit mod5.
    """
    a=np.asarray(mat,dtype=np.int64).copy()%MOD
    n,k=a.shape
    if n!=k:
        raise ValueError("square matrix required")
    r0=0
    pivots=[]
    while r0<n:
        corner=np.argwhere(a[r0:,r0:]%P!=0)
        if len(corner)==0:
            break
        i,j=(r0+int(z) for z in corner[0])
        if i!=r0:
            a[[r0,i],:]=a[[i,r0],:]
        if j!=r0:
            a[:,[r0,j]]=a[:,[j,r0]]
        pivot=int(a[r0,r0])
        assert pivot%P!=0
        inv=pow(pivot,-1,MOD)
        pivots.append(pivot)
        if r0+1<n:
            col=a[r0+1:,r0].copy()
            row=a[r0,r0+1:].copy()
            a[r0+1:,r0+1:]=(
                a[r0+1:,r0+1:]-np.outer(col,row)*inv
            )%MOD
            a[r0+1:,r0]=0
            a[r0,r0+1:]=0
        r0+=1
    assert r0==rank_f5(mat)
    residual=a[r0:,r0:]%MOD
    assert residual.shape==(n-r0,n-r0)
    assert not np.any(residual%P)
    quotient=(residual//P)%P
    r1=rank_f5(quotient)
    r2=n-r0-r1
    assert min(r0,r1,r2)>=0
    # Kernel size on the Z/25 module, not a full p-adic index:
    # |ker(A mod25)|=5^(e1+2*e>=2)
    return {
        "dimension":n,
        "e0_unit_smith_factors":r0,
        "e1_exactly_one_five":r1,
        "e_at_least_2":r2,
        "mod25_kernel_log5_cardinality":r1+2*r2,
        "unimodular_unit_pivots_used":len(pivots),
        "remaining_divisible_by5_matrix_shape":tuple(residual.shape),
    }


def hostile_smith_controls():
    fixtures=[
        (np.asarray([[1,0],[0,5]]), (1,1,0)),
        (np.asarray([[0,1],[5,0]]), (1,1,0)),
        (np.asarray([[5,0,0],[0,0,0],[0,0,1]]), (1,1,1)),
        (np.asarray([[5,5],[5,5]]), (0,1,1)),
        (np.asarray([[0,0],[0,0]]), (0,0,2)),
        (np.asarray([[1,0,0],[0,1,0],[0,0,5]]), (2,1,0)),
        (np.asarray([[5,1,0],[0,5,0],[0,0,1]]), (2,0,1)),
    ]
    data=[]
    for idx,(a,expected) in enumerate(fixtures):
        s=two_smith_slices(a)
        result=(s["e0_unit_smith_factors"],
                s["e1_exactly_one_five"],
                s["e_at_least_2"])
        assert result==expected,("hostile expected Smith controls failed",idx,result,expected)
        # Invertible row and column shears and permutation MUST
        # preserve ALL three Smith counts.
        m=len(a)
        perm=np.arange(m)[::-1]
        b=a[np.ix_(perm,perm)].copy()%MOD
        if m>=2:
            b[1,:]=(b[1,:]+7*b[0,:])%MOD
            b[:,0]=(b[:,0]+11*b[:,1])%MOD
        t=two_smith_slices(b)
        assert tuple(t[k] for k in (
            "e0_unit_smith_factors",
            "e1_exactly_one_five",
            "e_at_least_2"))==expected
        data.append({"fixture":idx,"dimension":m,"expected":expected,
                     "row_col_unimodular_invariance":True})
    return data


def signed_original_gram_under_twist(qomega,nonunit,lookup,k):
    t=(k*T[0]%MOD,k*T[1]%MOD)
    counts,nu=actual_original_ray_twist(qomega,t)
    assert nu==nonunit
    mat=gram_from_unit_rays_and_nonunit_lifts(counts,nonunit,lookup)
    return mat,counts,t


def actual_vs_gauge_smith_certificate():
    fixtures=hostile_smith_controls()
    qint,qomega,Greal,source=original_integer_source_oracle()
    assert len(qomega)==109 and Greal.shape==(40,40)
    actual_unit,actual_nonunit=unit_and_nonunit_counts(qomega)
    lookup,local=exhaustive_lift_table(D)
    assert np.array_equal(
        gram_from_unit_rays_and_nonunit_lifts(actual_unit,actual_nonunit,lookup),
        Greal)
    exact_spectra,_,_=signed_ideal_spectra_for_original_source(qint)
    actual_164=exact_spectra[164]
    # An independently isolated, exact generator-fibre contribution.
    G164actual=gram_from_unit_rays_and_nonunit_lifts(
        actual_164,Counter(),lookup)

    real=two_smith_slices(Greal)
    assert real["e0_unit_smith_factors"]==23
    records=[]
    distinct_profiles=set()
    changed_any=False
    for k in range(5):
        Gk,counts,t=signed_original_gram_under_twist(
            qomega,actual_nonunit,lookup,k)
        assert np.array_equal(Gk%5,Greal%5)
        assert rank_f5(Gk%5)==23
        # Nothing outside the literal norm164 Diophantine fibre is
        # allowed to explain an apparent change of Smith invariants.
        norm164_twisted=Counter()
        for original,z in zip(qint,qomega):
            x,y=original
            if x*x+D*y*y==164 and z<(-z[0],-z[1]):
                norm164_twisted[shifted_ray_tag(z,t)]+=1
        assert sum(norm164_twisted.values())==2
        G164twisted=gram_from_unit_rays_and_nonunit_lifts(
            norm164_twisted,Counter(),lookup)
        dist=(Gk-Greal)%MOD
        assert np.array_equal(dist,(G164twisted-G164actual)%MOD),(
            "synthetic change not entirely explained by norm164 fibre",k)
        changed_cells=int(np.count_nonzero(dist))
        assert changed_cells==0 if k==0 else changed_cells>0
        if changed_cells:
            changed_any=True
        current=two_smith_slices(Gk)
        assert current["e0_unit_smith_factors"]==23
        assert current["e0_unit_smith_factors"]+current["e1_exactly_one_five"]+current["e_at_least_2"]==40
        # Independently invariant under two deterministic GL40 shears
        b=np.asarray(Gk,dtype=np.int64).copy()
        b[0,:]=(b[0,:]+7*b[1,:])%MOD
        b[:,2]=(b[:,2]+11*b[:,3])%MOD
        shuffled=b[np.ix_(np.arange(40)[::-1],np.arange(40)[::-1])]
        stwo=two_smith_slices(shuffled)
        for label in ("e0_unit_smith_factors","e1_exactly_one_five","e_at_least_2"):
            assert current[label]==stwo[label],("GL40 equivalent Smith label mismatch",k,label)
        profile=(current["e0_unit_smith_factors"],
                 current["e1_exactly_one_five"],
                 current["e_at_least_2"])
        distinct_profiles.add(profile)
        ij=np.argwhere(dist)
        first=None
        if len(ij):
            i,j=ij[0]
            first=(int(i),int(j),int(dist[i,j]))
        records.append({
            "twist_k_mod5":k,
            "tracezero_two_digit_shift":t,
            "changed_original_Gram_cells_mod25":changed_cells,
            "first_changed_cell_if_any":first,
            "original_mod5_source_unchanged":True,
            "exact_mod25_smith":current,
        })
    assert changed_any
    assert records[0]["changed_original_Gram_cells_mod25"]==0
    assert records[1]["changed_original_Gram_cells_mod25"]==363
    assert records[1]["first_changed_cell_if_any"]==(0,26,15)
    return {
        "D":D,"source_R":40,"source_original_Q":len(qomega),
        "original_primitive_Gram_cells":int(Greal.size),
        "original_e0_e1_ege2":real,
        "full_5_point_tracezero_gauge_family":records,
        "distinct_first_two_smith_profiles_in_gauge_family":len(distinct_profiles),
        "some_wild_twist_changes_e1_or_ege2":len(distinct_profiles)>1,
        "if_all_profiles_same_record_as_negative":len(distinct_profiles)==1,
        "hostile_unit_pivot_permutation_and_shear_controls":fixtures,
        "exact_norm164_ray_source_premise_checked":sum(actual_164.values())==2,
        "not_a_real_alternative_quadratic_field":True,
        "not_full_v5_det_or_uniform_valuation_bound":True,
    }


def main():
    print("PHASE317_ORIGINAL_GRAM_MOD25_TWO_SMITH_SLICES_PASS",
          actual_vs_gauge_smith_certificate(),flush=True)


if __name__=="__main__":
    main()
