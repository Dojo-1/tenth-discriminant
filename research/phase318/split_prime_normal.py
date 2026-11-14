#!/usr/bin/env python3
"""Phase318-B: split-prime ideal-valuation characters on FULL native Q109.

Enumerate ALL maximal-order principal generators of prime norms <=441
in the exact D163 radius21 norm ball. For every split prime p with
pi not associate to conjugate(pi), the character

    nu_pi(z) = v_(pi)(z) - v_(conj pi)(z)

is multiplicative, sign-invariant and conjugation-antisymmetric. An
exact integer quotient z/pi=(z*conj pi)/p computes valuations; NO
residue representatives are used for ideal arithmetic.

Shift the corrected conductor125 wild logarithm by nu_pi(z)*T
(T=(20,10) mod25 trace-zero), keeping norm125, signed tame/mod5 and
conductor2 tags. Reconstruct SAME native integer-order 40x40 Gram
mod25 and compare its radical normal restriction with the COMPLETE
Phase318 local norm-preserving site basis.

This does NOT claim the synthetic ray tags are actual integral
generator rays, nor that the finite prime list generates all
multiplicative characters. No field-uniform valuation bound.
"""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase308","phase311","phase312","phase313",
               "phase314","phase315","phase316","phase317","phase318"):
    sys.path.insert(0,str(ROOT/"research"/folder))

from inert_trace_radicals import full_omega_q,rank_f5
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from fermat_lift import conjugate
from wild_log125 import (
    signed_ray125_tag,signed_ray125_mul,exhaustive_lift_table,
    norm,add,scale
)
from wild_gauge import integer_mul,T
from local_wild_normal import (
    signed_unit_sites,entire_norm_line,site_differentials,
    trace_norm_differential,upper_vectors
)
from conductor250_original_mod25 import (
    original_integer_source_oracle,gram_of_observations,
    full_ray250_convolution,unit_and_nonunit_counts
)
from conductor2_order_gate import coprime_odd_non5_pairs
from radical_tangent import kernel_basis_mod5,first_radical_form
from two_digit_smith import two_smith_slices
from norm_first_fibre import prime_by_integer_divisors

D=163
P=5
MOD=25
TOP=125


def split_principal_prime_generators():
    Q=tuple(full_omega_q(D,21))
    assert len(Q)==225
    bynorm=defaultdict(set)
    for z in Q:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if n%10==0 or gcd(n,10)!=1 or not prime_by_integer_divisors(n):
            continue
        bynorm[n].add(z)
    out={}
    discarded_ramified=[]
    for p,values in sorted(bynorm.items()):
        vals=tuple(sorted(values))
        assert all(quadratic_norm(z,D)==p for z in vals)
        if len(vals)==1:
            # Ramified prime p=D: conjugation gives associate.
            z=vals[0]
            conj=conjugate(z,None)
            assert conj==z or conj==(-z[0],-z[1])
            discarded_ramified.append(p)
            continue
        assert len(vals)==2,("unexpected >2 principal norm-p ideals",p,vals)
        a,b=vals
        assert min(conjugate(a,None),
                   tuple(-x for x in conjugate(a,None)))==b
        out[p]=a
    assert 41 in out
    assert 163 in discarded_ramified
    return Q,out,discarded_ramified


def divide_by_prime_generator(z,pi):
    p=quadratic_norm(pi,D)
    assert prime_by_integer_divisors(p)
    numer=integer_mul(z,conjugate(pi,None))
    if any(n%p for n in numer):
        return None
    q=tuple(n//p for n in numer)
    assert integer_mul(q,pi)==z
    return q


def valuation_at_pi(z,pi):
    if z==(0,0):
        raise ValueError("nonzero principal ideal required")
    value=z
    k=0
    while True:
        q=divide_by_prime_generator(value,pi)
        if q is None:
            break
        value=q
        k+=1
        assert k<64
    return k


def split_prime_character(z,pi):
    return valuation_at_pi(z,pi)-valuation_at_pi(
        z,conjugate(pi,None))


def signed_wild_character_tag(z,pi):
    tame,wild=signed_ray125_tag(z,D)
    return tame,add(wild,scale(split_prime_character(z,pi),T,MOD),MOD)


def recover_oriented_residue(z,pi,lookup):
    tag=signed_wild_character_tag(z,pi)
    w=lookup[tag]
    zres=(z[0]%TOP,z[1]%TOP)
    if (w[0]%5,w[1]%5)!=(zres[0]%5,zres[1]%5):
        opposite=((-w[0])%TOP,(-w[1])%TOP)
        assert (opposite[0]%5,opposite[1]%5)==(
            zres[0]%5,zres[1]%5)
        w=opposite
    # Shifts of wild log by 5T' preserve the complete
    # original ray mod25, so adjusted residue differs by25h.
    difference=((w[0]-zres[0])%TOP,(w[1]-zres[1])%TOP)
    assert difference[0]%25==difference[1]%25==0,(
        "two-digit wild shift unexpectedly changes first-level ray tag",z,pi)
    h=(difference[0]//25,difference[1]//25)
    assert trace_norm_differential(h,z)==0
    assert norm(w,D,TOP)==norm(z,D,TOP)
    return w,h


def verify_exact_ideal_valuation_character(pi,points):
    assert quadratic_norm(pi,D)==quadratic_norm(conjugate(pi,None),D)
    assert integer_mul(pi,conjugate(pi,None))==(
        quadratic_norm(pi,D),0)
    controls=((0,1),(1,-1),(2,0),(3,1),(5,0),pi,conjugate(pi,None))
    checked=0
    for z in points:
        if z==(0,0):
            continue
        v=split_prime_character(z,pi)
        assert v==split_prime_character((-z[0],-z[1]),pi)
        assert split_prime_character(conjugate(z,None),pi)==-v
        for w in controls:
            zw=integer_mul(z,w)
            assert split_prime_character(zw,pi)==(
                v+split_prime_character(w,pi)),(
                "exact split-prime valuation not multiplicative",pi,z,w)
            checked+=1
    return checked


def one_prime_original_gram(pi,sites,non,K,bases,mats,lookup,Greal):
    assert len(sites)==len(bases)==len(mats)==50
    Hsum=np.zeros((40,40),dtype=np.int64)
    direct=np.zeros_like(Hsum)
    affected=0
    for i,z in enumerate(sites):
        baseline=gram_of_observations((z,(-z[0],-z[1])))
        w,h=recover_oriented_residue(z,pi,lookup)
        base=bases[i]
        coefficient=next((c for c in range(5)
                          if ((c*base[0])%5,(c*base[1])%5)==h),None)
        assert coefficient is not None
        shifted=gram_of_observations((w,(-w[0],-w[1])))
        diff=(shifted-baseline)%MOD
        assert not np.any(diff%5)
        assert np.array_equal(diff//5,(coefficient*mats[i])%5),(
            "global character fails to factor through full local norm line",
            pi,z,h,coefficient)
        Hsum=(Hsum+coefficient*mats[i])%5
        direct=(direct+shifted)%MOD
        if coefficient:
            affected+=1
    for z in non:
        direct=(direct+gram_of_observations((z,)))%MOD
    predicted=(Greal+5*Hsum)%MOD
    assert np.array_equal(direct,predicted),(
        "global prime character original Gram not sum of site variations")
    assert np.array_equal(direct%5,Greal%5)
    B=first_radical_form(direct,K)
    restriction=(K.T@Hsum@K)%5
    assert np.array_equal((B-first_radical_form(Greal,K))%5,restriction)
    smith=two_smith_slices(direct)
    changed=int(np.count_nonzero((direct-Greal)%MOD))
    Nrank=rank_f5(restriction)
    return {
        "prime":quadratic_norm(pi,D),
        "chosen_exact_prime_generator":pi,
        "changed_signed_original_sites":affected,
        "changed_original_Gram_cells_mod25":changed,
        "changed_original_Gram_cells_mod5":0,
        "normal_restriction_rank":Nrank,
        "first_radical_form_equal_original":Nrank==0,
        "first_radical_lift_rank":rank_f5(B),
        "original_first_two_smith_layers":[
            smith["e0_unit_smith_factors"],
            smith["e1_exactly_one_five"],
            smith["e_at_least_2"]],
        "global_normal_equals_linear_combination_all_local_site_normals":True,
        "signed_wild_log_shift_preserves_norm_mod125":True,
    },restriction


def global_ray_replay_one_prime(pi,Q):
    bins=defaultdict(Counter)
    for z in Q:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if gcd(n,10)!=1:
            continue
        tag=((z[0]%2,z[1]%2),signed_wild_character_tag(z,pi))
        assert signed_wild_character_tag(z,pi)==signed_wild_character_tag(
            (-z[0],-z[1]),pi)
        bins[n][tag]+=1
    eligible=[n for n in range(1,442) if gcd(n,10)==1]
    assert len(eligible)==177
    for n in eligible:
        assert sum(bins[n].values())==all_ideal_count_at_norm(D,n)
    pairs=0
    for m,n in coprime_odd_non5_pairs():
        assert bins[m*n]==full_ray250_convolution(bins[m],bins[n]),(
            "global split prime character full ray250 convolution failed",pi,m,n)
        pairs+=1
    assert pairs==270
    return {"prime":quadratic_norm(pi,D),
            "all_independent_h1_ideal_norm_shells":len(eligible),
            "full_22500_conductor250_coprime_products":pairs}


def global_split_prime_normal_certificate():
    qint,qomega,Greal,_=original_integer_source_oracle()
    sites,non=signed_unit_sites(qomega)
    bases,mats=site_differentials(sites)
    K,_,_=kernel_basis_mod5(Greal%5)
    assert K.shape==(40,17)
    lookup,_=exhaustive_lift_table(D)
    Q,maximal_primes,ramified=split_principal_prime_generators()
    results=[]
    normal_vectors=[]
    exact_products=0
    active=[]
    for prime,pi in sorted(maximal_primes.items()):
        products=verify_exact_ideal_valuation_character(pi,qomega)
        exact_products+=products
        rec,normal=one_prime_original_gram(
            pi,sites,non,K,bases,mats,lookup,Greal)
        rec["exact_principal_valuation_product_checks"]=products
        results.append(rec)
        if rec["changed_signed_original_sites"]:
            active.append(prime)
            normal_vectors.append(normal)
    assert 41 in active
    assert len(active)>1,(
        "finite D163 native original source has no other active split primes")

    # Exact Phase316 41-character is recovered up to orientation:
    # either +T or -T, both with 363 cells and tangent normal zero.
    old=next(x for x in results if x["prime"]==41)
    assert old["changed_original_Gram_cells_mod25"]==363
    assert old["normal_restriction_rank"]==0
    assert old["original_first_two_smith_layers"]==[23,7,10]

    tri=np.triu_indices(17)
    matrix=np.column_stack([x[tri] for x in normal_vectors])%5
    rank=rank_f5(matrix)
    nonzero=[x for x in results if x["normal_restriction_rank"]>0]
    e1_changed=[x for x in results
                if x["original_first_two_smith_layers"]!=[23,7,10]]
    # Sample native 270-pair global convolution for first THREE active
    # split primes, always including 41 due to sorted order.
    replayed=[]
    for p in active[:3]:
        replayed.append(global_ray_replay_one_prime(maximal_primes[p],Q))
    assert replayed and replayed[0]["prime"]==41
    assert all(x["full_22500_conductor250_coprime_products"]==270
               for x in replayed)

    return {
        "D":D,
        "original_integer_order_Q":len(qomega),
        "maximal_order_radius21_Q":len(Q),
        "ramified_prime_excluded_from_antisymmetric_character":ramified,
        "distinct_split_principal_prime_characters_tested":len(results),
        "active_native_original_characters":len(active),
        "active_prime_list":active,
        "exact_nonmodular_prime_valuation_multiplication_checks":exact_products,
        "per_character_source_and_radical_records":results,
        "normal_image_span_rank_among_active_global_characters":rank,
        "nonzero_radical_normal_global_characters":[x["prime"] for x in nonzero],
        "characters_changing_first_two_smith_layers":[x["prime"] for x in e1_changed],
        "native_41_character_is_tangent_recovered":True,
        "replayed_full_250_ray_h1_convolution_selected_characters":replayed,
        "all_characters_are_synthetic_not_real_new_field_generators":True,
        "no_improvement_to_uniform_discriminant_cutoff":True
    }


def main():
    print("PHASE318_SPLIT_PRIME_GLOBAL_NORMAL_FAMILY_PASS",
          global_split_prime_normal_certificate(),flush=True)


if __name__=="__main__":
    main()
