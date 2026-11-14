#!/usr/bin/env python3
"""Phase318-E: exact original-order integer norm fibres reject synthetic resonance.

For the SAME native D163 original integer order Q109/R40, compare actual
signed conductor125 ray classes at EACH exact integer norm n with
globally multiplicative, norm125-preserving SYNTHETIC characters of
split primes p53,p227. The altered classes must NOT have generators
of the exact norm n in the original O'=Z[sqrt(-163)] norm ball.

Measured earlier: p53 selects normal lambda3 with synthetic e1=3,
p227 likewise, while p41 selects tangent lambda0 and e1=7.
NOW independently verify the complete Diophantine fibres:
  p41: original norm164, (±1,±1)
  p53: original norm212, (±7,±1)
  p227: original norm227, (±8,±1).
There are two signed actual ideals in every fibre.

Each fake class has correct local norm mod125 and conductor2
admissibility, yet no globally integral generator of exact norm.
All synthetic Gram mod25 differences come from ONLY that norm fibre.
Not a real alternate field and not a uniform determinant theorem.
"""
from collections import Counter,defaultdict
from math import isqrt
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313",
               "phase314","phase315","phase316","phase317","phase318"):
    sys.path.insert(0,str(ROOT/"research"/folder))

from fermat_lift import conjugate
from norm_shell_bridge import quadratic_norm
from wild_log125 import signed_ray125_tag,exhaustive_lift_table,norm
from split_prime_normal import (
    split_principal_prime_generators,signed_wild_character_tag
)
from conductor250_original_mod25 import (
    original_integer_source_oracle,unit_and_nonunit_counts,
    gram_from_unit_rays_and_nonunit_lifts
)
from ray_to_original_gram import embed_integer_pair_to_omega
from local_wild_normal import signed_unit_sites,site_differentials
from radical_tangent import kernel_basis_mod5,first_radical_form
from two_digit_smith import two_smith_slices
from normal_pencil import scale_of_one_dimensional_normal
from heldout_global_ray import nonh1_counterworld

D=163
MOD=25
TOP=125


def exact_integer_norm_fibre(n):
    assert n>0
    solutions=set()
    for y in range(-isqrt(n//D),isqrt(n//D)+1):
        remainder=n-D*y*y
        if remainder<0:
            continue
        x=isqrt(remainder)
        if x*x==remainder:
            solutions.add((x,y))
            solutions.add((-x,y))
    assert all(x*x+D*y*y==n for x,y in solutions)
    return tuple(sorted(solutions))


def all_signed_native_ray_norm_shells(qomega,pi):
    sites,non=signed_unit_sites(qomega)
    real=defaultdict(Counter)
    synthetic=defaultdict(Counter)
    for z in sites:
        n=quadratic_norm(z,D)
        real[n][signed_ray125_tag(z,D)]+=1
        synthetic[n][signed_wild_character_tag(z,pi)]+=1
    assert sum(map(lambda x:sum(x.values()),real.values()))==50
    assert sum(map(lambda x:sum(x.values()),synthetic.values()))==50
    changed=sorted(n for n in set(real)|set(synthetic)
                   if real[n]!=synthetic[n])
    return sites,non,real,synthetic,changed


def direct_gram_of_ray_counts(C,lookup):
    return gram_from_unit_rays_and_nonunit_lifts(C,Counter(),lookup)


def one_exact_fibre_character(prime,pi,qomega,Gactual,lookup,K,base_normal):
    sites,non,real,synthetic,changed=all_signed_native_ray_norm_shells(
        qomega,pi)
    expected_norm={41:164,53:212,227:227}[prime]
    assert changed==[expected_norm],(
        "split prime synthetic tags change unexpected exact norm shells",
        prime,changed,expected_norm)
    n=expected_norm
    fibres=exact_integer_norm_fibre(n)
    a=isqrt(n-D)
    assert a*a==n-D
    expected={(x,y) for x in (-a,a) for y in (-1,1)}
    assert set(fibres)==expected
    assert len(fibres)==4

    real_support={
        signed_ray125_tag(embed_integer_pair_to_omega(z),D)
        for z in fibres
    }
    assert len(real_support)==2
    assert set(real[n])==real_support and sum(real[n].values())==2
    assert sum(synthetic[n].values())==2
    assert set(synthetic[n]).isdisjoint(real_support),(
        "SYNTHETIC local norm ray was already an actual exact-norm generator",
        prime)
    local_witness=[]
    for tag in sorted(synthetic[n]):
        residue=lookup[tag]
        assert norm(residue,D,TOP)==n%TOP
        # Inert2 original suborder: b even. Norm parity forces
        # a even for even n, a odd for odd n. CRT with 125 supplies
        # the specified parity without changing mod125 ray/norm.
        wanted=(n%2,0)
        lift=tuple(int(residue[i])+125*((wanted[i]-residue[i])%2)
                   for i in range(2))
        assert tuple(v%2 for v in lift)==wanted
        assert norm(lift,D,TOP)==n%TOP
        assert signed_ray125_tag(lift,D)==tag
        assert tag not in real_support
        local_witness.append({
            "synthetic_signed_ray_tag":tag,
            "representative_mod125":residue,
            "CRT_original_suborder_lift":lift,
            "norm_mod125":norm(lift,D,TOP),
            "globally_integral_exact_norm_generator_exists":False,
        })
    assert len(local_witness)==2

    base,_=unit_and_nonunit_counts(qomega)
    actual_unit=Counter()
    fake_unit=Counter()
    for C in real.values():
        actual_unit.update(C)
    for C in synthetic.values():
        fake_unit.update(C)
    assert actual_unit==base
    original_non=unit_and_nonunit_counts(qomega)[1]
    actual_G=gram_from_unit_rays_and_nonunit_lifts(
        actual_unit,original_non,lookup)
    assert np.array_equal(actual_G,Gactual)
    fake_G=gram_from_unit_rays_and_nonunit_lifts(
        fake_unit,original_non,lookup)
    delta=(fake_G-Gactual)%MOD
    assert not np.any(delta%5)
    only_shell=(direct_gram_of_ray_counts(synthetic[n],lookup)
                -direct_gram_of_ray_counts(real[n],lookup))%MOD
    assert np.array_equal(only_shell,delta),(
        "all synthetic primitive Gram changes not concentrated at exact norm",
        prime,n)
    changed_cells=int(np.count_nonzero(delta))
    assert changed_cells=={41:363,53:363,227:250}[prime]
    smith=two_smith_slices(fake_G)
    expected_smith={41:[23,7,10],53:[23,3,14],227:[23,3,14]}[prime]
    profile=[smith["e0_unit_smith_factors"],
             smith["e1_exactly_one_five"],
             smith["e_at_least_2"]]
    assert profile==expected_smith
    normal=(K.T@((delta//5)%5)@K)%5
    coeff=scale_of_one_dimensional_normal(normal,base_normal)
    assert coeff=={41:0,53:3,227:3}[prime]
    assert np.array_equal(
        (first_radical_form(fake_G,K)-first_radical_form(Gactual,K))%5,
        normal)
    return {
        "split_prime":prime,
        "principal_maximal_order_generator":pi,
        "first_changed_original_integer_norm_shell":n,
        "exact_integer_fibre_solutions":fibres,
        "exact_original_signed_norm_fibre_count":sum(real[n].values()),
        "synthetic_signed_norm_fibre_count":sum(synthetic[n].values()),
        "synthetic_tag_support_disjoint_from_actual_exact_norm_fibre":True,
        "synthetic_classes_locally_norm125_and_conductor2_admissible":local_witness,
        "all_other_original_norm_shell_spectra_identical":True,
        "all_original_Gram_changes_only_from_this_exact_norm_fibre":True,
        "same_original_Gram_entries_compared_mod25":int(Gactual.size),
        "synthetic_changed_primitive_Gram_cells_mod25":changed_cells,
        "normal_pencil_lambda_mod5":coeff,
        "synthetic_first_two_smith_layers":profile,
        "not_claimed_actual_alt_quadratic_field":True,
    }


def exact_resonant_global_fibre_certificate():
    Qint,Qomega,G,_=original_integer_source_oracle()
    sites,non=signed_unit_sites(Qomega)
    bases,mats=site_differentials(sites)
    K,_,_=kernel_basis_mod5(G%5)
    first=next(i for i,m in enumerate(mats)
               if np.any((K.T@m@K)%5))
    base_normal=(K.T@mats[first]@K)%5
    assert len(Qomega)==109 and K.shape==(40,17)
    Qmax,primes,_=split_principal_prime_generators()
    assert len(Qmax)==225
    lookup,_=exhaustive_lift_table(D)
    records=[
        one_exact_fibre_character(p,primes[p],Qomega,G,lookup,K,base_normal)
        for p in (41,53,227)
    ]
    h2=nonh1_counterworld()
    assert h2["D"]==187
    assert h2["principal_only_convolution_fails_despite_same_local_ray_group"]
    return {
        "D":D,
        "original_integer_order_Q":len(Qomega),
        "first_original_norm_fibres_for_3_characters":records,
        "all_synthetic_resonant_rays_fail_exact_global_norm_fibre_test":True,
        "h2_D187_global_ideal_class_negative_control":True,
        "no_alternate_real_quadratic_field_or_field_uniform_valuation_claim":True,
    }


def main():
    print("PHASE318_RESONANT_RAYS_UNREALIZABLE_EXACT_FIBRES_PASS",
          exact_resonant_global_fibre_certificate(),flush=True)


if __name__=="__main__":
    main()
