#!/usr/bin/env python3
"""Phase316-B: exact elementary small-norm rigidity + ideal character gauge.

For imaginary fundamental discriminant -D with D=4m-1 and D>3,
N(a+b omega)=a²+ab+mb², so 4N=(2a+b)²+D b².
For b!=0, N>=m. Thus elements of norm n<m are only integers ±a,
and their norm is a². If h(K)=1 then ALL ideal norm shells n<m
are exactly the rational square ideals (a): mass1 at squares,0 else.

The Phase316 synthetic norm-preserving twist along the two conjugate
41-prime valuations is ZERO on every rational integer, so it fixes
ALL such rigorously determined small-norm ray125 and ray250 data.
Yet higher-norm synthetic tags can change the original Gram mod25.
This tests a stronger set of constraints than convolution+mass alone,
but does not imply a new tenth-discriminant bound.
"""
from collections import Counter
from math import isqrt,gcd
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase308","phase311","phase312","phase313",
               "phase314","phase315","phase316"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from adaptive_torsion_family import independent_reduced_forms
from inert_trace_radicals import full_omega_q
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from wild_log125 import signed_ray125_tag
from wild_gauge import antisymmetric_valuation,shifted_ray_tag,full_gauge_countercertificate
from ray_to_original_gram import embed_integer_pair_to_omega
import source_probe


def small_norm_form_proof_data(D):
    assert D>3 and D%4==3 and D%2==1
    m=(D+1)//4
    assert 4*m-D==1
    # The mathematical proof is independent of this enumeration:
    # for b !=0, b²>=1, 4*N>=D=4m-1.
    # But 4*N is divisible by4, so N>=m for integral N.
    Q=tuple(full_omega_q(D,isqrt(m)+1))
    seen=set(Q)
    norms=Counter()
    principal=Counter()
    for z in Q:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if n>=m:
            continue
        assert z[1]==0,("small norm nonrational actual element",D,z,n)
        assert n==z[0]*z[0]
        assert (-z[0],-z[1]) in seen
        norms[n]+=1
        principal[n]+=1
    expected={a*a:1 for a in range(1,isqrt(m-1)+1)}
    assert dict(norms)==expected
    return m,Q,principal,expected


def class_one_small_norm_rigidity(D):
    assert D in (43,163)
    assert len(independent_reduced_forms(D))==1
    m,Q,principal,expected=small_norm_form_proof_data(D)
    low_full={}
    for n in range(1,m):
        mass=all_ideal_count_at_norm(D,n)
        expected_mass=1 if isqrt(n)**2==n else 0
        assert mass==expected_mass,(
            "h1 small-norm ideal rigidity failed",D,n,mass,expected_mass)
        assert principal[n]==mass,(
            "small-norm principal vs independent all ideals mismatch",D,n)
        low_full[n]=mass
    # D163 actual original h1 wild gauge: all z=a rational have
    # valuation difference 0 at the conjugate 41-prime factors,
    # so not even the SECOND wild depth is perturbed.
    twisted=0
    signed_tags=0
    if D==163:
        for n in range(1,m):
            if not low_full[n]:
                continue
            a=isqrt(n)
            assert antisymmetric_valuation((a,0))==0
            # The rational generator 5 has norm25 but is NOT a local
            # 5-unit: conductor125 signed ray tags are undefined there.
            # It belongs to the independent nonunit first-lift stratum,
            # whose gauge remains zero; never create a fake unit tag.
            if a%5:
                assert signed_ray125_tag((a,0),D)==shifted_ray_tag((a,0))
            if gcd(n,10)==1:
                signed_tags+=1
            twisted+=1
        assert twisted==len(expected)
    return {
        "D":D,
        "maximal_order_m":m,
        "class_number":1,
        "actual_small_norm_observations_rho":isqrt(m)+1,
        "maximal_order_observation_count":len(Q),
        "all_independent_ideal_shells_n_less_m_checked":m-1,
        "all_ideal_shells_iff_rational_squares":True,
        "number_of_rational_square_ideal_shells":len(expected),
        "smallest_nonrational_element_norm":m,
        "synthetic_41prime_wild_twist_small_norm_shells_unchanged":twisted,
        "signed_conductor250_eligible_low_norm_shells_unchanged":signed_tags,
        "small_prime_ideal_norm_obstruction_implies_inertness_under_h1":True,
        "not_new_determinant_valuation":True
    }


def class_number_gt1_counterworld():
    D=187
    forms=independent_reduced_forms(D)
    assert len(forms)==2
    m,Q,principal,expected=small_norm_form_proof_data(D)
    failures=[]
    for n in range(1,m):
        total=all_ideal_count_at_norm(D,n)
        if total!=principal[n]:
            failures.append({"norm":n,"all_integral_ideals":total,
                             "principal_ideals":principal[n]})
    assert any(x["norm"]==11 and x["all_integral_ideals"]==1
               and x["principal_ideals"]==0 for x in failures)
    assert any(x["norm"]==17 and x["all_integral_ideals"]==1
               and x["principal_ideals"]==0 for x in failures)
    return {
        "D":D,
        "class_number":len(forms),
        "same_small_norm_element_rational_square_rule_as_h1":True,
        "maximal_order_m":m,
        "independent_ideal_shells_compared":m-1,
        "explicit_nonprincipal_ideal_norm_failures":failures,
        "not_a_new_field_bound":True,
    }


def original_integer_order_first_twist_gate():
    """The exact original O'=Z[sqrt(-D)] norm ball has a later threshold.

    Every nonrational original integer x+y sqrt(-D) has N>=D.
    In D163, the first such element has norm163 (sqrt(-163)).
    The first element divisible by omega but not its conjugate
    appears at norm164=4*N(omega), namely 2*omega=1+sqrt(-163).
    """
    D=163
    rho,R,S,J,Q=source_probe.params(D)
    assert (rho,R,S,J)==(21,40,1,1)
    q=tuple(Q)
    assert len(q)==109
    assert all(y==0 for x,y in q if x*x+D*y*y<D)
    nonrational=min(x*x+D*y*y for x,y in q if y!=0)
    assert nonrational==D
    active=[]
    for z in q:
        if z==(0,0):
            continue
        norminteger=z[0]*z[0]+D*z[1]*z[1]
        if antisymmetric_valuation(embed_integer_pair_to_omega(z)):
            active.append((norminteger,z))
    first=min(n for n,z in active)
    assert first==4*((D+1)//4)==164
    assert any(n==164 and z==(1,1) for n,z in active)
    return {
        "original_integer_order_source_Q":len(q),
        "smallest_nonrational_original_order_element_norm":nonrational,
        "smallest_norm_original_order_element_affected_by_wild_twist":first,
        "first_wild_gauge_active_integer_point":[1,1],
        "maximal_order_omega_first_nonrational_norm":(D+1)//4,
        "exact_suborder_conductor2_delay_factor_at_first_active_point":4,
        "original_integer_point_not_replaced_by_maximal_order":True
    }


def all_controls():
    positives=[class_one_small_norm_rigidity(D) for D in (43,163)]
    negative=class_number_gt1_counterworld()
    original_first=original_integer_order_first_twist_gate()
    # Compare against the independent CI-gated Phase316-A result.
    synthetic=full_gauge_countercertificate()
    assert synthetic["synthetic_vs_actual_Gram_equal_mod5"]
    assert synthetic["synthetic_vs_actual_Gram_changed_mod25"],(
        "Phase316-A mod25 synthetic Gram change unexpectedly disappeared")
    assert positives[1]["synthetic_41prime_wild_twist_small_norm_shells_unchanged"]>0
    return {
        "h1_small_norm_ideal_rigidity":positives,
        "h2_nonprincipal_ideal_counterworld":negative,
        "native_original_integer_order_threshold":original_first,
        "second_depth_twist_preserves_all_h1_rational_square_shells_below_m":True,
        "but_h1_original_integer_Gram_mod25_changes_above_m":True,
        "native_source_Q":synthetic["original_native_integer_source_Q"],
        "synthetic_original_Gram_changed_cells_mod25":
            synthetic["changed_mod25_matrix_cells"],
        "small_norm_criterion_classical_not_novel":True,
        "no_uniform_cutoff_change":True,
    }


def main():
    print("PHASE316_SMALL_NORM_RIGIDITY_AND_GAUGE_PASS",
          all_controls(),flush=True)

if __name__=="__main__":
    main()
