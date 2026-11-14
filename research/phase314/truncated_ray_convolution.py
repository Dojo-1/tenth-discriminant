#!/usr/bin/env python3
"""Phase314-B: h1 conductor50 convolution closes on 216 wild second jets.

A full principal ideal ray distribution is an element of
F5[C3 x C12 x C5^2]. Quotient by wild augmentation J^3 gives
3*12*6 = 216 coordinates. Unlike mere Gram compression, this
quadratic-moment quotient is an ALGEBRA: convolution of full ray
distributions is computed exactly by a six-coordinate moment product.

Original suborder selection is performed only AFTER the full
maximal-order ray convolution. Odd norms select F4 residue1,
even norms prime-to5 require a separate original 2-divisible stratum;
5-divisible observations require a further first-lift stratum.
The resulting moments reproduce the SAME original h1 D163
integer-order primitive Gram, not a maximal-order substitute.
"""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase206","phase311","phase312","phase313","phase314"):
    sys.path.insert(0,str(ROOT/"research"/p))
from tame_wild_ray import tame_orbit,ray_tag
from fermat_lift import mul
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from conductor2_order_gate import (
    full_maximal_ray50_distribution,coprime_odd_non5_pairs,
    project_to_original_count,suborder_coprime_counterexample,
    ray50_product
)
from wild_quadratic_gram import (
    monomials,all_tame,count_moments_signed,count_moments_unrestricted,
    unit_and_nonunit_coefficients,gram_from_moments
)
from ray_to_original_gram import (
    embed_integer_pair_to_omega,ray_and_nonunit_strata,
    ray_count_Gram_D163_native
)
from inert_trace_radicals import full_omega_q,rank_f5
import source_probe

D=163
P=5


def direct_jet50(hist):
    """Actual 900-class signed ray count -> at most 216 mod5 moments."""
    raw=defaultdict(lambda:[0]*6)
    for (r2,(c,w)),multiplicity in hist.items():
        v=raw[(r2,c)]
        f=monomials(w)
        for i in range(6):
            v[i]=(v[i]+multiplicity*f[i])%5
    return {k:tuple(v) for k,v in raw.items() if any(v)}


def moment_product_six(a,b):
    """Exact multiplication of first and second RAW moments of x+y.

    vec=(mass, sum x, sum y, sum x², sum xy, sum y²).
    This is a finite-dimensional quotient of group-algebra convolution.
    """
    a0,ax,ay,axx,axy,ayy=a
    b0,bx,by,bxx,bxy,byy=b
    return (
        a0*b0,
        ax*b0+a0*bx,
        ay*b0+a0*by,
        axx*b0+2*ax*bx+a0*bxx,
        axy*b0+ax*by+ay*bx+a0*bxy,
        ayy*b0+2*ay*by+a0*byy,
    )


def moment_convolution50(A,B):
    """Closed six-jet product, including C3 and C12 multiplication."""
    out=defaultdict(lambda:[0]*6)
    for (r2,c),a in A.items():
        for (s2,d),b in B.items():
            k=(mul(r2,s2,D,2),tame_orbit(mul(c,d,D,5),D))
            vals=moment_product_six(a,b)
            v=out[k]
            for i in range(6):
                v[i]=(v[i]+vals[i])%5
    return {k:tuple(v) for k,v in out.items() if any(v)}


def add_moments(v,w):
    return tuple((v[i]+w[i])%5 for i in range(6))


def moments_for_selected_original(full,Qmax):
    """Convolve globally FIRST, then project odd norms through mod2.

    Returns 12 signed conductor25 unit moment vectors (rather than
    raw 300 classes). Even prime-to5 norms are routed separately,
    since they have no conductor50 unit tag.
    """
    selected=defaultdict(lambda:(0,)*6)
    odd_count=0
    for n,counts in full.items():
        if gcd(n,10)!=1:
            raise AssertionError("full conductor50 distribution includes nonunit norm")
        for (r2,(c,w)),multiplicity in counts.items():
            if r2==(1,0):
                cvec=tuple((multiplicity*x)%5 for x in monomials(w))
                selected[c]=add_moments(selected[c],cvec)
                odd_count+=multiplicity
    even_count=0
    for z in Qmax:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if n%2==0 and n%5!=0:
            assert z[1]%2==0
            c,w=ray_tag(z,D)
            selected[c]=add_moments(selected[c],monomials(w))
            even_count+=1
    return {c:v for c,v in selected.items() if any(v)},odd_count,even_count


def recover_Gram_from_quadratic_vectors(unit_moments,nonunit_moments,
                                        unit_coeff,nonunit_coeff):
    gram=np.zeros((40,40),dtype=np.int64)
    for c,v in unit_moments.items():
        gram=(gram+np.einsum(
            "i,ijk->jk",np.asarray(v,dtype=np.int64),
            unit_coeff[c]))%5
    gram=(gram+np.einsum(
        "i,ijk->jk",np.asarray(nonunit_moments,dtype=np.int64),
        nonunit_coeff))%5
    return gram


def full_conductor50_quadratic_certificate():
    Qmax=tuple(full_omega_q(D,21))
    assert len(Qmax)==225
    full,principal=full_maximal_ray50_distribution(Qmax)
    assert principal==84
    primes=[n for n in range(1,442) if gcd(n,10)==1]
    assert len(primes)==177
    jets={n:direct_jet50(full[n]) for n in primes}
    assert all(len(v)<=36 for v in jets.values())

    pairs=0
    equal_class_jet_cells=0
    nonzero_nonidentity=0
    for m,n in coprime_odd_non5_pairs():
        got=jets[m*n]
        calc=moment_convolution50(jets[m],jets[n])
        assert got==calc,(
            "class-one full conductor50 six-moment algebra convolution failed",m,n)
        # Independent real source's total ideal number agrees with mass.
        assert sum(full[m*n].values())==all_ideal_count_at_norm(D,m*n)
        pairs+=1
        equal_class_jet_cells+=6*len(set(got)|set(calc))
        if m>1 and n>1 and got:
            nonzero_nonidentity+=1
    assert pairs==270

    rho,R,S,J,Qint=source_probe.params(D)
    assert (rho,R,S,J)==(21,40,1,1)
    Qoriginal=tuple(embed_integer_pair_to_omega(z) for z in Qint)
    assert len(Qoriginal)==109

    selected,odd,even=moments_for_selected_original(full,Qmax)
    direct_unit_counts,nonunit_counts=ray_and_nonunit_strata(Qoriginal,D)
    direct_moments=count_moments_signed(direct_unit_counts)
    direct_moments={k:tuple(v) for k,v in direct_moments.items() if any(v)}
    assert selected==direct_moments,(
        "compressed full ray50 global projection does not match ORIGINAL order")
    assert odd==26 and even==24
    assert sum(direct_unit_counts.values())==50
    assert sum(nonunit_counts.values())==9
    nm=count_moments_unrestricted(nonunit_counts)

    unit_coeff,nu_coeff,coeffmeta=unit_and_nonunit_coefficients(D)
    gram=recover_Gram_from_quadratic_vectors(selected,nm,unit_coeff,nu_coeff)
    same_g,meta=ray_count_Gram_D163_native(Qoriginal)
    assert np.array_equal(gram,same_g)
    assert rank_f5(gram)==23
    selected_full,odd_f,even_f=project_to_original_count(Qmax,full)
    assert selected_full==direct_unit_counts
    assert odd_f==odd and even_f==even
    _g2,um2,nm2=gram_from_moments(selected_full,nonunit_counts,
                                  unit_coeff,nu_coeff)
    assert np.array_equal(_g2,gram)
    assert {k:tuple(v) for k,v in um2.items() if any(v)}==selected
    assert nm2==nm
    suborder=suborder_coprime_counterexample()
    assert suborder["projecting_convolution_before_multiplication_is_invalid"]
    return {
        "field_D":D,
        "class_number_one_imported_from_independent_reduced_forms":1,
        "maximal_order_Q":len(Qmax),
        "original_integer_order_Q":len(Qoriginal),
        "full_signed_ray50_classes":900,
        "truncated_wild_second_jet_coordinates":216,
        "wild_feature_dimension_per_tame_and_conductor2":6,
        "eligible_norm_shells_exactly_accounted":len(primes),
        "full_900_ray_convolution_jet_pairs_verified":pairs,
        "matched_6moment_per_group_cells_checked":equal_class_jet_cells,
        "nontrivial_nonidentity_coprime_products":nonzero_nonidentity,
        "selected_odd_norm_unit_ideals":odd,
        "selected_even_norm_unit_ideals":even,
        "nonunit_first_lift_observations":sum(nonunit_counts.values()),
        "original_selected_signed_ray_second_jet_blocks":len(selected),
        "original_selected_72plus6_moment_capacity":78,
        "same_original_integer_Gram_cells_reconstructed":int(gram.size),
        "same_original_integer_primitive_Gram_rank_mod5":rank_f5(gram),
        "source_coefficients_full_25wild_value_checks":coeffmeta[
            "full_signed_unit_ray_classes_checked"],
        "suborder_projection_NOT_a_convolution_map":True,
        "truncated_wild_quotient_convolution_compatible":True,
        "no_class_number_one_extra_valuation_inferred":True
    }


def main():
    print("PHASE314_CONDUCTOR50_TRUNCATED_WILD_CONVOLUTION_PASS",
          full_conductor50_quadratic_certificate(),flush=True)


if __name__=="__main__":
    main()
