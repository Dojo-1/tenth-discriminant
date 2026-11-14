#!/usr/bin/env python3
"""Phase314-A: ORIGINAL primitive mod5 Gram factors through wild J^3.

For D203 actual divided 100-row original ordinary-jets and h1 D163
actual 40-row original INTEGER-order primitive source, each unit
signed-ray Gram coefficient is a degree<=2 polynomial of the two F5
coordinates of delta=(z^5-conj(z))/(5 conj(z)). The 25 first-nonunit
lift Gram coefficients are also quadratic in u=z/5 mod5.

The wild additive group algebra F5[C5^2] has augmentation ideal J;
hence the Gram map kills J^3, factoring through six jet moments per
tame class. All 300 plus25 direct original coefficient matrices are
verified, not fitted on actual class-one counts. This claim applies to
primitive Gram MOD5 only; not full integral determinants or deeper
5-adic Smith digits.
"""
from collections import Counter,defaultdict
from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase206","phase304","phase307","phase311","phase312","phase313"):
    sys.path.insert(0,str(ROOT/"research"/p))
from tame_wild_ray import tame_orbit,norm_mod5
from ray_to_original_gram import (
    ray_and_nonunit_strata,wild_unit_features,nonunit_features,
    generated_D203_E,generated_D163_native_E,
    ray_count_Gram_D203,ray_count_Gram_D163_native,
    embed_integer_pair_to_omega, native_integer_original_primitive,
)
from inert_trace_radicals import trace_gram_from_original,rank_f5
from source_saturation import original_fifty_row_saturation
import highjet_d203_original as pilot
import source_probe


P=5
MONOMIALS=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
WILD=tuple(product(range(5),repeat=2))
DIRECTION=(1,0),(0,1)


def monomials(w):
    x,y=w
    return (1,x%5,y%5,x*x%5,x*y%5,y*y%5)


def all_tame(D):
    result={
        tame_orbit((a,b),D)
        for a,b in WILD if norm_mod5((a,b),D)
    }
    assert len(result)==12
    return tuple(sorted(result))


def direct_unit_Gram(D,c,w):
    neg=((-c[0])%5,(-c[1])%5)
    if D==203:
        E=generated_D203_E(
            [c,neg],[wild_unit_features(c,w,D),
                     wild_unit_features(neg,w,D)])
    elif D==163:
        E=generated_D163_native_E(
            [c,neg],[wild_unit_features(c,w,D),
                     wild_unit_features(neg,w,D)])
    else:
        raise ValueError("only original D203/D163 source labels available")
    return trace_gram_from_original(E,D)


def direct_nonunit_Gram(D,u):
    if D==203:
        E=generated_D203_E([(0,0)],[nonunit_features(u,D)])
    elif D==163:
        E=generated_D163_native_E([(0,0)],[nonunit_features(u,D)])
    else:
        raise ValueError("unknown original source")
    return trace_gram_from_original(E,D)


def extract_six_coefficients(table):
    """Recover coefficients Q=A+Bx+Cy+Dx²+Exy+Fy² over F5.

    Uses exactly six source direct matrices, not a free polynomial fit
    to actual observed ray counts. Checks the OTHER 19 values separately.
    """
    A=table[(0,0)]
    ix=3 # 2^-1 in F5
    Bx=(ix*(table[(1,0)]-table[(4,0)]))%5
    Cxx=(ix*(table[(1,0)]+table[(4,0)]-2*A))%5
    By=(ix*(table[(0,1)]-table[(0,4)]))%5
    Cyy=(ix*(table[(0,1)]+table[(0,4)]-2*A))%5
    Cxy=(table[(1,1)]-A-Bx-By-Cxx-Cyy)%5
    coeff=np.stack((A,Bx,By,Cxx,Cxy,Cyy),axis=0)%5
    for w in WILD:
        vec=np.asarray(monomials(w),dtype=np.int64)
        predicted=np.einsum("i,ijk->jk",vec,coeff)%5
        assert np.array_equal(predicted,table[w]),(
            "quadratic Gram coefficient failed direct original source",w)
    return coeff


def mixed_third_difference(table,start,dirs):
    """Δ_h Δ_k Δ_l table(w) exact over F5, using group addition."""
    assert len(dirs)==3
    out=np.zeros_like(next(iter(table.values())))
    for mask in range(8):
        step=(0,0)
        count=0
        for i in range(3):
            if mask & (1<<i):
                step=((step[0]+dirs[i][0])%5,(step[1]+dirs[i][1])%5)
                count+=1
        z=((start[0]+step[0])%5,(start[1]+step[1])%5)
        out=(out+(-1)**(3-count)*table[z])%5
    return out


def unit_and_nonunit_coefficients(D):
    """All 300 signed unit and all25 nonunit original Gram matrices."""
    n=100 if D==203 else 40
    unit_coeff={}
    checked_unit=0
    third_checks=0
    any_second=False
    sample_nonzero_second=None
    tame=all_tame(D)
    for c in tame:
        table={w:direct_unit_Gram(D,c,w) for w in WILD}
        coeff=extract_six_coefficients(table)
        assert coeff.shape==(6,n,n)
        unit_coeff[c]=coeff
        checked_unit+=len(table)*n*n
        for start in WILD:
            for i in range(2):
                for j in range(i,2):
                    for k in range(j,2):
                        dirs=(DIRECTION[i],DIRECTION[j],DIRECTION[k])
                        assert not np.any(mixed_third_difference(table,start,dirs)),(
                            "wild third augmentation difference survives",D,c,start,dirs)
                        third_checks+=1
        second=(table[(2,0)]-2*table[(1,0)]+table[(0,0)])%5
        if np.any(second):
            any_second=True
            if sample_nonzero_second is None:
                i,j=np.argwhere(second)[0]
                sample_nonzero_second={
                    "tame_class":c,"matrix_cell":[int(i),int(j)],
                    "nonzero_second_difference":int(second[i,j])
                }
    assert any_second,("quadratic wild part collapsed to first order",D)

    nonunit_table={u:direct_nonunit_Gram(D,u) for u in WILD}
    nonunit_coeff=extract_six_coefficients(nonunit_table)
    checked_nonunit=len(nonunit_table)*n*n
    for start in WILD:
        for i in range(2):
            for j in range(i,2):
                for k in range(j,2):
                    assert not np.any(mixed_third_difference(
                        nonunit_table,start,
                        (DIRECTION[i],DIRECTION[j],DIRECTION[k]))),(
                            "nonunit third difference survives",D,start,i,j,k)
                    third_checks+=1

    return unit_coeff,nonunit_coeff,{
        "D":D,
        "source_rows":n,
        "signed_tame_classes":len(tame),
        "full_signed_unit_ray_classes_checked":len(tame)*len(WILD),
        "first_nonunit_lift_classes_checked":len(WILD),
        "exact_direct_unit_Gram_matrix_cells_checked":checked_unit,
        "exact_direct_nonunit_Gram_matrix_cells_checked":checked_nonunit,
        "all_third_difference_Gram_matrices_zero":third_checks,
        "second_augmentation_layer_nonzero":sample_nonzero_second,
        "total_second_jet_features_at_most":len(tame)*6+6,
        "full_wild_group_algebra_dimension":25,
        "quotient_F5_C5_squared_by_J_cubed_dimension":6,
        "no_higher_5adic_valuation_from_mod5_compression":True
    }


def count_moments_signed(counts):
    """Counter ((tame c, wild w) -> multiplicity) -> c -> F5^6."""
    result=defaultdict(lambda:[0]*6)
    for (c,w),num in counts.items():
        mm=monomials(w)
        v=result[c]
        for k in range(6):
            v[k]=(v[k]+num*mm[k])%5
    return dict(result)


def count_moments_unrestricted(counts):
    """Counter wild u -> n -> six exact raw moments modulo5."""
    v=[0]*6
    for w,num in counts.items():
        for k,val in enumerate(monomials(w)):
            v[k]=(v[k]+num*val)%5
    return tuple(v)


def gram_from_moments(unit_counts,nonunit_counts,unit_coeff,nonunit_coeff):
    """The exact original primitive F5-linear map through J³."""
    n=nonunit_coeff.shape[1]
    unit_moments=count_moments_signed(unit_counts)
    nonunit_moments=count_moments_unrestricted(nonunit_counts)
    gram=np.zeros((n,n),dtype=np.int64)
    for c,v in unit_moments.items():
        C=unit_coeff[c]
        gram=(gram+np.einsum(
            "i,ijk->jk",np.asarray(v,dtype=np.int64),C))%5
    gram=(gram+np.einsum(
        "i,ijk->jk",np.asarray(nonunit_moments,dtype=np.int64),
        nonunit_coeff))%5
    return gram,unit_moments,nonunit_moments


def abstract_cubic_augmentation_kernel(D,unit_coeff):
    """Two NONNEGATIVE abstract signed-ray histograms with identical
    six moments and same primitive Gram, but different full class counts.
    They are NOT claimed to correspond to actual ideals of a number field.
    """
    c=all_tame(D)[0]
    a=Counter({(c,(x,0)):3 for x in range(4)})
    b=Counter({(c,(0,0)):2,(c,(1,0)):6,
               (c,(2,0)):0,(c,(3,0)):4})
    assert a!=b
    assert sum(a.values())==sum(b.values())==12
    va=count_moments_signed(a)
    vb=count_moments_signed(b)
    assert va==vb
    ca=unit_coeff[c]
    first=np.einsum("i,ijk->jk",np.asarray(va[c]),ca)%5
    second=np.einsum("i,ijk->jk",np.asarray(vb[c]),ca)%5
    assert np.array_equal(first,second)
    assert a[(c,(0,0))]!=b[(c,(0,0))]
    return {
        "source_D":D,
        "abstract_nonnegative_histogram_A":[3,3,3,3],
        "abstract_nonnegative_histogram_B":[2,6,0,4],
        "same_z0_z1_z2_wild_moments":True,
        "same_original_primitive_Gram_mod5":True,
        "not_claimed_as_real_number_field_ray_counts":True,
    }


def full_original_certificates():
    records=[]
    for D in (203,163):
        coeff,nonunit_coeff,meta=unit_and_nonunit_coefficients(D)
        if D==203:
            q=tuple(pilot.qmax(24))
            assert len(q)==263
            direct,prior=ray_count_Gram_D203(q)
            E=pilot.evaluate_original_jets(q,50,2,2,25)
            _,prim,selected=original_fifty_row_saturation(E)
            assert len(selected)==50
            untouched=pilot.original_trace_gram(
                np.asarray(prim,dtype=np.int64)%5,len(q),2,5)
        else:
            rho,r,s,j,Q=source_probe.params(D)
            assert (rho,r,s,j)==(21,40,1,1)
            q=tuple(embed_integer_pair_to_omega(z) for z in Q)
            assert len(q)==109
            direct,prior=ray_count_Gram_D163_native(q)
            E=native_integer_original_primitive(tuple(Q),25)
            # In original O' pair coordinates (a,b), transform exactly
            # to omega coordinates (a-b,2b) before Hermitian trace.
            transformed=np.zeros_like(E)
            transformed[:,0::2]=(E[:,0::2]-E[:,1::2])%5
            transformed[:,1::2]=(2*E[:,1::2])%5
            untouched=trace_gram_from_original(transformed,D)
        unit_counts,nonunit_counts=ray_and_nonunit_strata(q,D)
        recovered,um,nm=gram_from_moments(
            unit_counts,nonunit_counts,coeff,nonunit_coeff)
        assert np.array_equal(recovered,direct)
        assert np.array_equal(recovered,untouched)
        assert rank_f5(recovered)==(63 if D==203 else 23)
        meta.update({
            "full_actual_original_Q":len(q),
            "populated_signed_ray_bins_before_compression":len(unit_counts),
            "compressed_tame_moment_blocks":len(um),
            "full_uncompressed_signed_ray_unit_capacity":300,
            "full_uncompressed_first_lift_capacity":25,
            "compressed_total_F5_feature_capacity":78,
            "same_original_primitive_Gram_cells_preserved":int(recovered.size),
            "same_original_primitive_Gram_rank_F5":rank_f5(recovered),
            "independent_original_source_Gram_matches":True,
            "abstract_J_cube_null_counterworld":
                abstract_cubic_augmentation_kernel(D,coeff),
        })
        records.append(meta)
    return records


def main():
    print("PHASE314_ORIGINAL_WILD_SECOND_JET_GRAM_PASS",
          full_original_certificates(),flush=True)


if __name__=="__main__":
    main()
