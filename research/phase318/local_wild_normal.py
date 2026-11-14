#!/usr/bin/env python3
"""Phase318-A: COMPLETE local norm-preserving depth2 ray variations.

For each of 50 signed 5-unit observations in the SAME original
D163 integer-order Q109/R40/S=J1 source, enumerate the entire
F5-line of 5 local lifts z' = z+25h mod125 which retain signed ray25
and quadratic norm mod125:
    Tr(h*conj(z)) =0 mod5.

Compute the exact signed pair native primitive Gram mod25 for every
lift; its /5 differential H_i is a symmetric F5 40x40 matrix.
Restrict H_i to the original mod5 Gram radical R (dimension17):
    N_i = K^T H_i K mod5.
Measure rank of the complete 50-site normal map, AND the
conjugation-covariant subspace. Do NOT assume either rank is nonzero.

This is a local residue family, not alternate global integral
generators, class-one fields or a determinant bound.
"""
from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313","phase314",
               "phase315","phase316","phase317","phase318"):
    sys.path.insert(0,str(ROOT/"research"/folder))

from inert_trace_radicals import rank_f5
from fermat_lift import conjugate
from wild_gauge import integer_mul
from wild_log125 import signed_ray125_tag, norm, is_unit
from conductor250_original_mod25 import (
    original_integer_source_oracle, gram_of_observations,
    unit_and_nonunit_counts
)
from radical_tangent import kernel_basis_mod5,first_radical_form
from two_digit_smith import two_smith_slices

D=163
P=5
MOD=25
TOP=125
S=40


def signed_unit_sites(qomega):
    Q=tuple(qomega)
    seen=set(Q)
    sites=[]
    nonunits=[]
    for z in Q:
        neg=(-z[0],-z[1])
        assert neg in seen
        if is_unit(z,D):
            if z<neg:
                sites.append(z)
        else:
            nonunits.append(z)
    sites=tuple(sorted(sites))
    assert len(sites)==50
    assert len(nonunits)==9
    assert 2*len(sites)+len(nonunits)==len(Q)==109
    return sites,tuple(nonunits)


def trace_norm_differential(h,z):
    prod=integer_mul(h,conjugate(z,None))
    return (2*prod[0]+prod[1])%P


def entire_norm_line(z):
    if not is_unit(z,D):
        raise ValueError("norm-preserving p-adic unit lifts require 5-unit")
    candidates=tuple((u,v) for u,v in product(range(P),repeat=2)
                     if trace_norm_differential((u,v),z)==0)
    assert len(candidates)==5
    assert (0,0) in candidates
    base=next(h for h in candidates if h!=(0,0))
    assert set(candidates)==set(((k*base[0])%P,(k*base[1])%P)
                                for k in range(P))
    return base,candidates


def shifted_site_gram(z,h,k):
    lifted=(z[0]+25*k*h[0],z[1]+25*k*h[1])
    assert norm(lifted,D,TOP)==norm(z,D,TOP)
    old=signed_ray125_tag(z,D)
    new=signed_ray125_tag(lifted,D)
    assert old[0]==new[0]
    assert all(old[1][i]%5==new[1][i]%5 for i in range(2))
    gram=gram_of_observations((lifted,(-lifted[0],-lifted[1])))
    return gram,lifted


def site_differentials(sites):
    mats=[]
    bases=[]
    for z in sites:
        base,cands=entire_norm_line(z)
        baseline=gram_of_observations((z,(-z[0],-z[1])))
        assert np.array_equal(baseline,baseline.T)
        first=None
        for k in range(5):
            g,lifted=shifted_site_gram(z,base,k)
            diff=(g-baseline)%MOD
            assert np.array_equal(diff,diff.T)
            assert not np.any(diff%P)
            h=(diff//P)%P
            if k==0:
                assert not np.any(h)
            elif k==1:
                first=h
            else:
                assert np.array_equal(h,(k*first)%P),(
                    "wild local Gram differential nonlinear at depth2",z,k)
        assert first is not None
        bases.append(base)
        mats.append(first)
    return tuple(bases),tuple(mats)


def covariant_conjugate_combinations(sites,bases,mats):
    lookup={z:i for i,z in enumerate(sites)}
    assert len(lookup)==len(sites)
    used=set()
    cov=[]
    paired=0
    self_allowed=0
    self_forbidden=0
    for i,z in enumerate(sites):
        if i in used:
            continue
        cz=conjugate(z,None)
        selected=min(cz,(-cz[0],-cz[1]))
        assert selected in lookup
        j=lookup[selected]
        sign=1 if cz==sites[j] else -1
        assert cz==tuple(sign*x for x in sites[j])
        bh=conjugate(bases[i],None)
        want=((sign*bh[0])%P,(sign*bh[1])%P)
        coeff=next((c for c in range(1,P)
                    if ((c*bases[j][0])%P,(c*bases[j][1])%P)==want),None)
        assert coeff is not None
        if j==i:
            if coeff==1:
                tilted=(z[0]+25*bases[i][0],
                        z[1]+25*bases[i][1])
                ct=conjugate(tilted,None)
                assert all((ct[t]-sign*tilted[t])%TOP==0
                           for t in range(2))
                cov.append(mats[i])
                self_allowed+=1
            else:
                assert coeff==P-1
                self_forbidden+=1
            used.add(i)
        else:
            assert j not in used
            zi=(z[0]+25*bases[i][0],z[1]+25*bases[i][1])
            zj=(sites[j][0]+25*coeff*bases[j][0],
                sites[j][1]+25*coeff*bases[j][1])
            ci=conjugate(zi,None)
            assert all((ci[t]-sign*zj[t])%TOP==0
                       for t in range(2)),(
                "site-pair perturbation broke conjugation mod125",i,j)
            cov.append((mats[i]+coeff*mats[j])%P)
            paired+=1
            used.add(i);used.add(j)
            # Exactly conjugate selected generator changes.
            assert selected==sites[j]
    assert len(used)==len(sites)
    assert 2*paired+self_allowed+self_forbidden==len(sites)
    return cov,{"conjugate_pairs":paired,
                "self_conjugate_allowed_norm_directions":self_allowed,
                "self_conjugate_forbidden_norm_directions":self_forbidden,
                "conjugation_covariant_independent_local_parameters":
                   len(cov)}


def upper_vectors(mats,radical):
    q=radical.shape[1]
    tri=np.triu_indices(q)
    images=[]
    for mat in mats:
        a=(radical.T@mat@radical)%P
        assert np.array_equal(a,a.T)
        images.append(a[tri])
    if not images:
        return np.zeros((q*(q+1)//2,0),dtype=np.int64)
    return np.column_stack(images)%P


def local_normal_certificate():
    qint,qomega,G,source=original_integer_source_oracle()
    sites,non= signed_unit_sites(qomega)
    counts,noncounts=unit_and_nonunit_counts(qomega)
    assert sum(counts.values())==len(sites)
    assert sum(noncounts.values())==len(non)
    accum=np.zeros((S,S),dtype=np.int64)
    for z in sites:
        accum=(accum+gram_of_observations((z,(-z[0],-z[1]))))%MOD
    for z in non:
        accum=(accum+gram_of_observations((z,)))%MOD
    assert np.array_equal(accum,G),(
        "independent sum of 50 signed + 9 nonunit same-source site grams failed")

    K,_,_=kernel_basis_mod5(G%P)
    assert K.shape==(S,17)
    assert rank_f5(G%P)==23
    assert rank_f5(first_radical_form(G,K))==7
    bases,mats=site_differentials(sites)
    A=upper_vectors(mats,K)
    site_normal_rank=rank_f5(A)
    nonzero_sites=np.flatnonzero(np.any(A,axis=0))
    cov,cov_data=covariant_conjugate_combinations(sites,bases,mats)
    C=upper_vectors(cov,K)
    cov_rank=rank_f5(C)
    assert 0<=cov_rank<=site_normal_rank<=len(sites)
    witness=None
    if len(nonzero_sites):
        i=int(nonzero_sites[0])
        N=(K.T@mats[i]@K)%P
        ij=np.argwhere(N)[0]
        witness={"selected_signed_original_site":sites[i],
                 "site_index":i,
                 "admissible_h_basis_mod5":bases[i],
                 "first_nonzero_radical_entry":
                     [int(ij[0]),int(ij[1]),int(N[tuple(ij)])],
                 "single_site_normal_rank":rank_f5(N)}
    return {
        "D":D,"native_original_integer_order_Q":len(qomega),
        "native_original_primitive_rows":S,
        "native_original_mod25_Gram_cells":int(G.size),
        "signed_5unit_sites":len(sites),
        "separate_5nonunit_observations":len(non),
        "complete_admissible_lifts_per_5unit_site":5,
        "complete_local_site_5unit_lifts_checked":5*len(sites),
        "local_norm_functional_is_nonzero_and_kernel_line":True,
        "all_original_primitive_mod5_matrices_unchanged":True,
        "mod5_radical_dimension":K.shape[1],
        "original_first_radical_lift_rank":7,
        "all_50_site_normal_image_rank":site_normal_rank,
        "sites_with_nonzero_normal_restriction":len(nonzero_sites),
        "first_normal_site_witness_if_any":witness,
        "conjugation_covariant_local_parameter_controls":cov_data,
        "conjugation_covariant_normal_image_rank":cov_rank,
        "does_not_impose_full_global_ideal_convolution":True,
        "does_not_claim_new_field_or_valuation":True,
    }


def main():
    print("PHASE318_COMPLETE_LOCAL_WILD_NORMAL_MAP_PASS",
          local_normal_certificate(),flush=True)


if __name__=="__main__":
    main()
