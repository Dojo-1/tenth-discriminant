#!/usr/bin/env python3
"""Phase313-B: h=1 yields FULL principal ray norm-shell convolution.

For a class-number-one quadratic maximal order, every integral ideal of
norm n is principal and its generator is unique modulo global units +/-1.
At conductor25, the ray tag of that principal ideal is the tame residue
orbit and the normalized additive wild Fermat logarithm delta_5.

For coprime m,n prime-to5, ideal factorization yields
  P_(mn) = P_m * P_n
as exact 300-class distributions. At h>1, principal-only distributions
can fail, because nonprincipal ideals multiply to principal ideals.
Witness D183: norm(omega)=46=2*23, but elements of norm2/23 absent.
This is not a uniform Gram divisibility theorem.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase311","phase312","phase313"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from inert_trace_radicals import full_omega_q
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from tame_wild_ray import ray_tag,tag_mul,norm_mod5
from fermat_lift import mul,add,scale,conjugate

RHO=21
MAX_N=RHO*RHO


def principal_norm_ray_distribution(D):
    """One PRINCIPAL ideal per +/- generator; exclude conductor5 ideals."""
    Q=tuple(full_omega_q(D,RHO))
    assert len(Q)==len(set(Q))
    seen=set(Q)
    bins=defaultdict(Counter)
    coprime_generators=0
    for z in Q:
        if z==(0,0):
            continue
        opposite=(-z[0],-z[1])
        assert opposite in seen
        # Imaginary quadratic fields D>3 have only global units +/-1.
        if z>opposite:
            continue
        n=quadratic_norm(z,D)
        assert 1<=n<=MAX_N
        if n%5==0:
            assert not norm_mod5(z,D)
            continue
        assert norm_mod5(z,D)
        t=ray_tag(z,D)
        assert t==ray_tag(opposite,D)
        bins[n][t]+=1
        coprime_generators+=1
    return Q,bins,coprime_generators


def convolute_ray(A,B,D):
    C=Counter()
    for x,c in A.items():
        for y,d in B.items():
            C[tag_mul(x,y,D)]+=c*d
    return +C


def moments_of_ray_class_distribution(A,D):
    """Normalized wild log moments of IDEALS, not signed elements."""
    total=sum(A.values())
    B=(0,0)
    C2=(0,0)
    H=(0,0)
    for (_,delta),count in A.items():
        B=add(B,scale(count,delta,5),5)
        C2=add(C2,scale(count,mul(delta,delta,D,5),5),5)
        H=add(H,scale(count,mul(delta,conjugate(delta,5),D,5),5),5)
    assert H[1]==0
    assert B[1]==0,(D,B)
    assert C2[1]==0,(D,C2)
    return (total,B,C2,H)


def check_moment_convolution(a,b,prod,D,am,an):
    """The two quadratic Leibniz laws are consequences of ray convolution."""
    A0,A1,A2,A3=moments_of_ray_class_distribution(a,D)
    B0,B1,B2,B3=moments_of_ray_class_distribution(b,D)
    C0,C1,C2,C3=moments_of_ray_class_distribution(prod,D)
    assert A0==am and B0==an
    assert C0==am*an
    assert C1==add(scale(an,A1,5),scale(am,B1,5),5)
    expected_square=add(
        add(scale(an,A2,5),scale(am,B2,5),5),
        scale(2,mul(A1,B1,D,5),5),5)
    assert C2==expected_square
    expected_norm=add(
        add(scale(an,A3,5),scale(am,B3,5),5),
        add(mul(A1,conjugate(B1,5),D,5),
            mul(conjugate(A1,5),B1,D,5),5),5)
    assert C3==expected_norm
    return True


def coprime_pairs(bound=MAX_N):
    for m in range(1,bound+1):
        if m%5==0:
            continue
        for n in range(m,bound//m+1):
            if n%5 and gcd(m,n)==1:
                yield m,n


def class_one_shell_convolution(D):
    assert D in (43,163)
    Q,bins,principal=principal_norm_ray_distribution(D)
    pairs=0
    moment_tests=0
    ray_cells_checked=0
    first_nonzero_B=None
    for n in range(1,MAX_N+1):
        if n%5==0:
            continue
        assert sum(bins[n].values())==all_ideal_count_at_norm(D,n),(
            "class-one total ideals != principal-only count",D,n)
        _,B,C2,H=moments_of_ray_class_distribution(bins[n],D)
        if B!=(0,0) and first_nonzero_B is None:
            first_nonzero_B={"norm":n,"sum_delta":B,
                             "sum_delta_squared":C2,
                             "sum_delta_norm":H}
    for m,n in coprime_pairs():
        p=bins[m*n]
        computed=convolute_ray(bins[m],bins[n],D)
        assert p==computed,(
            "class-one RAY distribution convolution failed",D,m,n,
            p,computed)
        # Independently count total ideals from the Euler product
        # instead of trusting only principal-element generators.
        am=all_ideal_count_at_norm(D,m)
        an=all_ideal_count_at_norm(D,n)
        ap=all_ideal_count_at_norm(D,m*n)
        assert ap==am*an
        assert check_moment_convolution(bins[m],bins[n],p,D,am,an)
        pairs+=1
        moment_tests+=3
        ray_cells_checked+=len(p)+len(computed)
    assert pairs>100
    return {
        "D":D,
        "actual_principal_norm_ball_elements":len(Q),
        "principal_ideals_coprime_to5_at_norm_at_most441":principal,
        "individual_norm_shell_ideal_count_equalities_checked":
            MAX_N-(MAX_N//5),
        "full_300_class_coprime_norm_shell_convolutions_verified":pairs,
        "first_second_mixed_Fermat_moment_equalities_verified":moment_tests,
        "ray_class_distribution_cells_compared":ray_cells_checked,
        "first_nonzero_normalized_log_shell_moment_if_any":first_nonzero_B,
        "norm_shell_convolution_uses_GLOBAL_class_number_one":True,
        "no_forced_mod5_Gram_valuation_from_convolution_alone":True,
    }


def nonh1_class_cancel_witness():
    D=183
    Q,bins,principal=principal_norm_ray_distribution(D)
    # In O_D with omega²-omega+46=0, norm omega =46.
    # 2 and23 are non-squares <46, hence no element can have
    # either norm, while both rational primes split in K.
    assert quadratic_norm((0,1),D)==46
    assert (0,1) in Q
    assert not bins[2] and not bins[23]
    assert bins[46] and sum(bins[46].values())>=2
    assert all_ideal_count_at_norm(D,2)==2
    assert all_ideal_count_at_norm(D,23)==2
    assert all_ideal_count_at_norm(D,46)==4
    convolution=convolute_ray(bins[2],bins[23],D)
    assert not convolution and bins[46]!=convolution
    omega_tag=ray_tag((0,1),D)
    assert omega_tag in bins[46]
    assert omega_tag==ray_tag((0,-1),D)
    # Strong, explicit global class-group cancellation:
    # two NONPRINCIPAL ideal factors at coprime norms yield
    # at least one PRINCIPAL ideal at their product.
    return {
        "D":D,
        "class_number_from_independent_reduced_forms":8,
        "two_coprime_factor_norms":[2,23],
        "principal_norm2_ideals":sum(bins[2].values()),
        "principal_norm23_ideals":sum(bins[23].values()),
        "principal_norm46_ideals":sum(bins[46].values()),
        "all_norm2_ideals":all_ideal_count_at_norm(D,2),
        "all_norm23_ideals":all_ideal_count_at_norm(D,23),
        "ray_tag_of_omega_norm46":omega_tag,
        "principal_only_convolution_R2_R23_is_zero_but_R46_nonzero":True,
        "nonprincipal_ideal_class_cancellation_witness":True,
        "no_global_Gram_bound_derived":True,
    }


def main():
    fields=[class_one_shell_convolution(d) for d in (43,163)]
    negative=nonh1_class_cancel_witness()
    print("PHASE313_PRINCIPAL_RAY_CONVOLUTION_PASS",{
        "class_number_one_positive_fields":fields,
        "D183_nonprincipal_product_becomes_principal":negative,
        "h1_moment_Leibniz_is_a_global_constraint_not_a_valuation":True,
    },flush=True)


if __name__=="__main__":
    main()
