#!/usr/bin/env python3
"""Phase312-C: a GLOBAL necessary class-number-one norm-shell identity.

Independent total ideal counts from zeta_K(s)=zeta(s)L(s,chi_-D), compared
with principal norm-shell element counts from the original quadratic norm.
The formula is standard prior arithmetic, not a new solution to a tenth
discriminant. Plus/minus symmetry makes the UNWEIGHTED first Fermat moment
identically zero in every centrally symmetric norm ball, regardless of h.
"""
from collections import Counter
from math import isqrt
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase311","phase312"):
    sys.path.insert(0,str(ROOT/"research"/p))
from inert_trace_radicals import full_omega_q
from fermat_lift import epsilon,add,scale

FIELDS=((43,1),(163,1),(183,8))
RHO=21


def quadratic_norm(z,D):
    a,b=z
    m=(D+1)//4
    return a*a+a*b+m*b*b


def factor_integer(n):
    if n<1:raise ValueError("positive integer required")
    out=[]
    q=n
    k=2
    while k*k<=q:
        e=0
        while q%k==0:
            q//=k
            e+=1
        if e:out.append((k,e))
        k+=1
    if q>1:out.append((q,1))
    return out


def quadratic_character_at_prime(D,p):
    delta=-D
    if p==2:
        r=delta%8
        if r==1 or r==7:return 1
        if r==3 or r==5:return -1
        return 0
    if D%p==0:return 0
    q=pow(delta%p,(p-1)//2,p)
    if q==1:return 1
    if q==p-1:return -1
    raise AssertionError("prime Legendre relation failed")


def kronecker_character(D,n):
    if n==1:return 1
    out=1
    for p,e in factor_integer(n):
        out*=quadratic_character_at_prime(D,p)**e
    return out


def all_ideal_count_at_norm(D,n):
    """Coefficient of zeta(s)*L(s,chi_-D), all ideals incl nonprincipal."""
    return sum(kronecker_character(D,d)
               for d in range(1,n+1) if n%d==0)


def unit_orbit(z):
    z=(z[0]%5,z[1]%5)
    if z==(0,0):return None
    neg=((-z[0])%5,(-z[1])%5)
    return min(z,neg)


def actual_shell_and_orbit_certificate(D,expected_class_number):
    q=full_omega_q(D,RHO)
    assert len(q)==len(set(q))
    norms=Counter(quadratic_norm(z,D) for z in q)
    assert norms[0]==1
    failed=[]
    samples=[]
    for n in range(1,RHO*RHO+1):
        all_ideals=all_ideal_count_at_norm(D,n)
        elements=norms[n]
        assert 0<=elements//2<=all_ideals
        assert elements%2==0
        if elements != 2*all_ideals:
            failed.append({
                "n":n,
                "all_ideals_norm_n":all_ideals,
                "principal_norm_n_element_count":elements,
                "nonprincipal_ideal_count":all_ideals-elements//2,
            })
        if n in (1,2,3,5,7,11):
            samples.append({"n":n,"all_ideal_count":all_ideals,
                            "principal_element_count":elements})

    if expected_class_number==1:
        assert not failed,(D,failed[:3])
    elif D==183:
        assert failed and failed[0]["n"]==2
        assert failed[0]["all_ideals_norm_n"]==2
        assert failed[0]["principal_norm_n_element_count"]==0

    # +/- residue orbits partition *principal generators*. 5 is inert,
    # so all nonzero residues are units and there are exactly12 orbits.
    groups=Counter(unit_orbit(z) for z in q if z!=(0,0))
    assert len([x for x in groups if x is not None])==12
    assert all(v%2==0 for k,v in groups.items() if k is not None)
    principal_orbits={
        str(k):v//2 for k,v in sorted(
            (k,v) for k,v in groups.items() if k is not None)
    }
    # The global norm-ball is stable under z->-z. epsilon is odd,
    # so its entire first moment vanishes automatically for ALL h.
    qset=set(q)
    total=(0,0)
    for z in q:
        minus=(-z[0],-z[1])
        assert minus in qset
        a=epsilon(z,D)
        b=epsilon(minus,D)
        assert b==scale(-1,a,5)
        total=add(total,a,5)
    assert total==(0,0)
    return {
      "D":D,
      "expected_class_number_from_external_forms_control":expected_class_number,
      "matched_radius":RHO,
      "actual_norm_ball_observations":len(q),
      "all_positive_norm_shells_checked":RHO*RHO,
      "norm_shell_equalities_tested":RHO*RHO,
      "all_ideals_from_quadratic_character_divisor_sum":True,
      "first_nonprincipal_shell_if_any":failed[0] if failed else None,
      "total_nonprincipal_ideals_norm_at_most_rho_squared":
          sum(x["nonprincipal_ideal_count"] for x in failed),
      "first_norm_samples":samples,
      "twelve_principal_unit_orbit_counts":principal_orbits,
      "total_unweighted_first_Fermat_moment_mod5":total,
      "vanishing_first_moment_is_sign_symmetry_NOT_h1":True,
      "global_h1_necessary_norm_shell_identity_no_congruence_moment_theorem":True
    }


def main():
    results=[actual_shell_and_orbit_certificate(D,h) for D,h in FIELDS]
    assert results[0]["first_nonprincipal_shell_if_any"] is None
    assert results[1]["first_nonprincipal_shell_if_any"] is None
    assert results[2]["first_nonprincipal_shell_if_any"]["n"]==2
    print("PHASE312_GLOBAL_NORM_SHELL_AND_NULL_MOMENT_PASS",{
       "fields":results,
       "class_number_one_uniform_norm_shell_equality_is_classical":True,
       "ray_class_orbit_finer_sums_still_uncontrolled":True,
       "no_new_uniform_tenth_discriminant_bound":True,
    },flush=True)

if __name__=="__main__":
    main()
