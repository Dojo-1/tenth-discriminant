#!/usr/bin/env python3
"""Phase313-H: exact conductor-2 order gate for GLOBAL h1 -> ORIGINAL Gram.

Crucial correction: h1 convolution counts ideals in maximal O_K, while
the Lean original integer source uses O'=Z[sqrt(-D)]=Z+2O_K.
For D163, 2 is INERT, O/2=F4, and original z=a+b omega belongs to
O' iff b is even, equivalently:
  odd norm -> F4 unit residue must be 1,
  even norm -> z divisible2, automatically in O'.

Full prime-to10 ray group: (O/50)^x / +/-1 =
      C3 x C12 x C5² (900 signed classes).
Convolve FULL 900-class maximal-order ideal spectra under h1; project
only afterwards to F4-residue1, and carry even norms and 5-divisible
observations in distinct typed strata. The result reconstructs the SAME
ORIGINAL integer-order D163 primitive Gram, not a substituted source.

Projected original-suborder distributions DO NOT themselves convolve
in general, even under h1 (omega norm41, 1+omega norm43, product in O').
"""
from collections import Counter,defaultdict
from itertools import product
from math import gcd
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from inert_trace_radicals import full_omega_q,trace_gram_from_original,rank_f5
from fermat_lift import mul
from tame_wild_ray import ray_tag,tag_mul,norm_mod5
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from ray_to_original_gram import (
    embed_integer_pair_to_omega,ray_and_nonunit_strata,
    generated_D163_native_E,wild_unit_features,nonunit_features,
    ray_count_Gram_D163_native
)
import source_probe

D=163
RHO=21
MAX_N=RHO*RHO


def unit_mod2(z):
    return (z[0]%2,z[1]%2)


def norm_mod2(z):
    a,b=z
    m=(D+1)//4
    return (a*a+a*b+m*b*b)%2


def ray50_tag(z):
    if not norm_mod2(z) or not norm_mod5(z,D):
        raise ValueError("conductor50 ray tag only on 2-and-5-units")
    return (unit_mod2(z),ray_tag(z,D))


def ray50_product(t,u):
    return (mul(t[0],u[0],D,2),tag_mul(t[1],u[1],D))


def full_maximal_ray50_distribution(Q):
    bins=defaultdict(Counter)
    counted=0
    seen=set(Q)
    for z in Q:
        if z==(0,0):
            continue
        neg=(-z[0],-z[1])
        assert neg in seen
        if z>neg:
            continue
        n=quadratic_norm(z,D)
        if gcd(n,10)!=1:
            continue
        tag=ray50_tag(z)
        assert tag==ray50_tag(neg)
        bins[n][tag]+=1
        counted+=1
    return bins,counted


def convolution(a,b):
    c=Counter()
    for x,v in a.items():
        for y,w in b.items():
            c[ray50_product(x,y)]+=v*w
    return +c


def coprime_odd_non5_pairs():
    for m in range(1,MAX_N+1):
        if gcd(m,10)!=1:
            continue
        for n in range(m,MAX_N//m+1):
            if gcd(n,10)==1 and gcd(m,n)==1:
                yield m,n


def project_to_original_count(Qmax,full_ray50):
    """GLOBAL maximal ideal counts -> selected original O' signed 25-tags.

    At odd norms: select the F4 residue 1 component of full C50.
    At even norms: 2 inert => z divisible2 and belongs automatically
    to the original suborder, but no conductor50 unit tag is defined.
    """
    selected=Counter()
    projected_odd_ideals=0
    for n,C in full_ray50.items():
        for (r2,t25),count in C.items():
            if r2==(1,0):
                selected[t25]+=count
                projected_odd_ideals+=count

    even_ideals=0
    seen=set(Qmax)
    for z in Qmax:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if n%2!=0 or n%5==0:
            continue
        assert z[1]%2==0,(
            "2 inert forces even norm element into original suborder",z)
        selected[ray_tag(z,D)]+=1
        even_ideals+=1
    return selected,projected_odd_ideals,even_ideals


def Gram_from_selected_counts(selected,nonunits):
    """Previous exact original D163 source coefficient map, with
    EXPLICIT COUNTS from the full ideal conductor50 projection.
    """
    g=np.zeros((40,40),dtype=np.int64)
    for (c,w),count in selected.items():
        neg=((-c[0])%5,(-c[1])%5)
        E=generated_D163_native_E(
            [c,neg],[wild_unit_features(c,w,D),
                     wild_unit_features(neg,w,D)])
        g=(g+count*trace_gram_from_original(E,D))%5
    for u,count in nonunits.items():
        E=generated_D163_native_E([(0,0)],[nonunit_features(u,D)])
        g=(g+count*trace_gram_from_original(E,D))%5
    return g


def suborder_coprime_counterexample():
    # omega and 1+omega have odd omega coefficient; neither is in O'.
    a=(0,1)
    b=(1,1)
    assert quadratic_norm(a,D)==41
    assert quadratic_norm(b,D)==43
    assert gcd(41,43)==1
    ab=(-41,2) # omega*(1+omega)=2omega-41
    # Independently verify the ring product without mod reduction.
    m=(D+1)//4
    aa,bb=a;cc,dd=b
    actual=(aa*cc-m*bb*dd,aa*dd+bb*cc+bb*dd)
    assert actual==ab
    assert a[1]%2==b[1]%2==1 and ab[1]%2==0
    assert quadratic_norm(ab,D)==41*43==1763
    # In original integer coordinates x+y sqrt(-D), ab=(-40,1).
    assert (ab[0]+ab[1]//2,ab[1]//2)==(-40,1)
    assert (-40)**2+D==1763
    assert all(x*x!=n for n in (41,43) for x in range(-7,8))
    assert min(x*x+D*y*y for y in (-1,1) for x in range(-1,2))>=D>43
    assert unit_mod2(a)==(0,1) and unit_mod2(b)==(1,1)
    assert mul(unit_mod2(a),unit_mod2(b),D,2)==(1,0)
    return {
        "field_h1":True,
        "non_suborder_factor_norms":[41,43],
        "product_norm":1763,
        "product_original_integer_coordinates":[-40,1],
        "no_original_suborder_norm41_or43":True,
        "original_suborder_product_norm1763_exists":True,
        "projecting_convolution_before_multiplication_is_invalid":True
    }


def conductor2_bridge_certificate():
    assert (-D)%8==5
    assert (D+1)//4%2==1
    # F4 field has 3 nonzero residues and they multiply cyclically.
    field4=[(1,0),(0,1),(1,1)]
    assert all(norm_mod2(z)==1 for z in field4)
    assert all(mul(z,z,D,2)!=(0,0) for z in field4)
    assert len(set(field4))==3

    qmax=tuple(full_omega_q(D,RHO))
    rho,R,S,J,Qint=source_probe.params(D)
    assert (rho,R,S,J)==(21,40,1,1)
    qoriginal=tuple(embed_integer_pair_to_omega(z) for z in Qint)
    qselected=tuple(z for z in qmax if z[1]%2==0)
    assert len(qmax)==225 and len(qoriginal)==len(qselected)==109
    assert set(qoriginal)==set(qselected)

    for z in qmax:
        n=quadratic_norm(z,D)
        assert n<=RHO*RHO
        if n%2:
            assert (z[1]%2==0)==(unit_mod2(z)==(1,0))
        else:
            assert unit_mod2(z)==(0,0)
            assert z[1]%2==0

    # All 300 signed conductor25 units times F4^x of order3
    # enumerate the full 900 CRT ray-unit group as typed product.
    tags25={
        ray_tag((a,b),D) for a,b in product(range(25),repeat=2)
        if norm_mod5((a,b),D)
    }
    assert len(tags25)==300
    tags50={(u,t) for u in field4 for t in tags25}
    assert len(tags50)==900

    full,counted=full_maximal_ray50_distribution(qmax)
    assert counted>0
    ideal_shell_tests=0
    for n in range(1,MAX_N+1):
        if gcd(n,10)!=1:continue
        assert sum(full[n].values())==all_ideal_count_at_norm(D,n)
        ideal_shell_tests+=1
    assert ideal_shell_tests==177
    pair_checks=0
    for m,n in coprime_odd_non5_pairs():
        assert full[m*n]==convolution(full[m],full[n]),(
            "GLOBAL h1 conductor50 convolution failed",m,n)
        pair_checks+=1
    assert pair_checks>100

    projected,projected_odd,even_ideals=project_to_original_count(qmax,full)
    direct,nonunits=ray_and_nonunit_strata(qoriginal,D)
    assert projected==direct,(
        "conductor2 full ray selection failed ORIGINAL suborder 25-ray census")
    assert projected_odd+even_ideals==sum(direct.values())
    assert sum(direct.values())==50
    assert sum(nonunits.values())==9

    g=Gram_from_selected_counts(projected,nonunits)
    direct_g,meta=ray_count_Gram_D163_native(qoriginal)
    assert np.array_equal(g,direct_g),(
        "projected global h1 conductor50 spectrum did not recover original Gram")
    assert g.shape==(40,40) and rank_f5(g)==23
    negative=suborder_coprime_counterexample()
    return {
        "D":163,
        "original_suborder":"Z[sqrt(-163)] = Z + 2 O_K",
        "maximal_order_radius21_observations":len(qmax),
        "actual_original_integer_suborder_observations":len(qselected),
        "all_original_observations_exactly_even_omega_coefficient":True,
        "conductor2_unit_group_C3":len(field4),
        "full_signed_conductor50_unit_classes":len(tags50),
        "global_principal_ideals_coprime10_count":counted,
        "independent_total_ideal_norm_shell_checks":ideal_shell_tests,
        "full_900_component_coprime_norm_convolutions_checked":pair_checks,
        "selected_odd_norm_ideals_ray2_1":projected_odd,
        "selected_even_norm_ideals_2divisible":even_ideals,
        "selected_original_5unit_ideal_count":sum(projected.values()),
        "original_5divisible_observation_count":sum(nonunits.values()),
        "projected_original_25ray_census_equal_direct":True,
        "projected_global_h1_to_same_original_Gram_cells_checked":int(g.size),
        "original_primitive_Gram_rank_mod5":rank_f5(g),
        "suborder_projection_not_convolution_homomorphism":negative,
        "no_uniform_extra_Gram_valuation":True
    }


def main():
    print("PHASE313_CONDUCTOR2_ORDER_GATE_PASS",
          conductor2_bridge_certificate(),flush=True)


if __name__=="__main__":
    main()
