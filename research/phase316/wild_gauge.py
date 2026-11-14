#!/usr/bin/env python3
"""Phase316: a GLOBAL norm-preserving wild gauge freedom of the h1 ray model.

K=Q(sqrt(-163)), omega²=omega-41, P=(omega), Pbar=(1-omega)
are conjugate prime ideals of norm41. On any nonzero z define
    nu(z)=v_P(z)-v_Pbar(z),
so nu(zw)=nu(z)+nu(w), nu(bar z)=-nu(z), nu(-z)=nu(z).
With trace-zero t=5*(-1+2omega)=(20,10) modulo25:
    L'(z)=L(z)+nu(z)*t  mod25.
This keeps tame and conductor2 tags, all norm residues modulo125,
conjugation covariance and all full coprime principal-ideal ray
convolutions, but is NOT the actual generator ray map of K.

When projected to the ORIGINAL D163 integer-order Q109 Gram, the
synthetic ray data can yield a different primitive Gram mod25 while
agreeing mod5. This would establish that ideal counts, full convolution,
local norms, conjugation and the conductor2 selector ALONE do not fix
the second wild digit; actual generator congruences remain necessary.
No field-theorem/discriminant claim.
"""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase308","phase311","phase312","phase313",
               "phase314","phase315","phase316"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from inert_trace_radicals import full_omega_q,rank_f5
from fermat_lift import conjugate
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from wild_log125 import (
    M,TOP,add,scale,is_unit,norm,
    signed_ray125_tag,signed_ray125_mul,exhaustive_lift_table
)
from conductor250_original_mod25 import (
    original_integer_source_oracle,unit_and_nonunit_counts,
    gram_from_unit_rays_and_nonunit_lifts,full_ray250_ideal_distribution,
    full_ray250_convolution
)

D=163
P=41
T=(20,10) # 5*(-1+2omega), trace exactly 0 mod25
BAD_T=(5,0) # nonzero trace 10 mod25


def integer_mul(z,w):
    """Exact Z[omega] multiplication, no modular reduction."""
    a,b=z;c,d=w
    return (a*c-P*b*d,a*d+b*c+b*d)


def omega_divide(z):
    """Exact z/omega only if omega divides z in O_K."""
    a,b=z
    if a%P:
        return None
    ans=(a//P+b,-a//P)
    assert integer_mul(ans,(0,1))==z
    return ans


def baromega_divide(z):
    """Exact z/baromega, baromega=1-omega."""
    a,b=z
    if (a+b)%P:
        return None
    ans=(-b,(a+b)//P)
    assert integer_mul(ans,(1,-1))==z
    return ans


def prime_divisibility(z):
    assert z!=(0,0)
    a=z
    b=z
    va=vb=0
    while True:
        q=omega_divide(a)
        if q is None:
            break
        a=q
        va+=1
        assert va<1000
    while True:
        q=baromega_divide(b)
        if q is None:
            break
        b=q
        vb+=1
        assert vb<1000
    return va,vb


def antisymmetric_valuation(z):
    a,b=prime_divisibility(z)
    return a-b


def shifted_ray_tag(z,twist=T):
    if not is_unit(z,D):
        raise ValueError("synthetic ray125 tag not defined on p5 nonunits")
    c,w=signed_ray125_tag(z,D)
    return (c,add(w,scale(antisymmetric_valuation(z),twist,M),M))


def ray250_tag(z,twist=T):
    n=quadratic_norm(z,D)
    if gcd(n,10)!=1:
        raise ValueError("ray250 requires p2,p5 unit")
    return ((z[0]%2,z[1]%2),shifted_ray_tag(z,twist))


def ray250_multiply(a,b):
    from fermat_lift import mul
    return (mul(a[0],b[0],D,2),signed_ray125_mul(a[1],b[1],D))


def full_ray_product(a,b):
    out=Counter()
    for x,n in a.items():
        for y,m in b.items():
            out[ray250_multiply(x,y)]+=n*m
    return +out


def all_principal_ideals(radius,twist=T):
    Q=tuple(full_omega_q(D,radius))
    seen=set(Q)
    assert len(Q)==len(seen)
    bins=defaultdict(Counter)
    val_nonzero=0
    actual_ideals=0
    for z in Q:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if gcd(n,10)!=1:
            continue
        assert -z[0],-z[1] in [] if False else True
        tag=ray250_tag(z,twist)
        assert tag==ray250_tag((-z[0],-z[1]),twist)
        bins[n][tag]+=1
        actual_ideals+=1
        if antisymmetric_valuation(z):
            val_nonzero+=1
    return Q,bins,actual_ideals,val_nonzero


def full_heldout_twist_certificate(radius):
    Q,bins,nideals,changed=all_principal_ideals(radius,T)
    assert changed>0
    N=radius*radius
    eligible=tuple(n for n in range(1,N+1) if gcd(n,10)==1)
    for n in eligible:
        assert sum(bins[n].values())==all_ideal_count_at_norm(D,n),(
            "actual h1 ideal norm counts changed by gauge",n)
    nontrivial=0
    if radius==60:
        support=sorted(n for n in bins if n>1 and bins[n])
        for i,m in enumerate(support):
            for n in support[i:]:
                if m*n>N or gcd(m,n)!=1:
                    continue
                assert bins[m*n]==full_ray_product(bins[m],bins[n]),(
                    "twisted h1 full conductor250 distribution not multiplicative",m,n)
                nontrivial+=1
        assert nontrivial==59
    else:
        from conductor2_order_gate import coprime_odd_non5_pairs
        for m,n in coprime_odd_non5_pairs():
            assert bins[m*n]==full_ray_product(bins[m],bins[n]),(
                "twisted native h1 conductor250 convolution failed",m,n)
        nontrivial=270
    return Q,bins,{
        "radius_heldout_or_native":radius,
        "maximal_order_observations":len(Q),
        "principal_ideals_prime_to10":nideals,
        "principal_ideals_with_nonzero_41_adic_asymmetry":changed,
        "independently_verified_total_ideal_shells":len(eligible),
        "full_conductor250_twisted_coprime_convolutions_verified":nontrivial,
        "same_ideal_counts_and_full_convolution_as_actual_h1":True
    }


def shifted_generator_invariants(z,lookup):
    """Norm and conjugation tests on actual O_K generator, not fake fields."""
    assert is_unit(z,D)
    original=signed_ray125_tag(z,D)
    altered=shifted_ray_tag(z)
    assert original[0]==altered[0]
    assert original[1][0]%5==altered[1][0]%5
    assert original[1][1]%5==altered[1][1]%5
    c,w=altered
    synthetic=lookup[(c,w)]
    assert norm(synthetic,D,TOP)==norm(z,D,TOP),(
        "trace-zero wild twist did not preserve original norm modulo125",z)
    cz=conjugate(z,TOP)
    assert shifted_ray_tag(cz)[1]==conjugate(altered[1],M)
    assert shifted_ray_tag(cz)[0]==signed_ray125_tag(cz,D)[0]
    return synthetic


def actual_original_ray_twist(qomega,twist=T):
    counts=Counter()
    nonunit=Counter()
    seen=set(qomega)
    for z in qomega:
        if is_unit(z,D):
            neg=(-z[0],-z[1])
            assert neg in seen
            if z<neg:
                counts[shifted_ray_tag(z,twist)]+=1
        else:
            assert z[0]%5==z[1]%5==0
            u=(z[0]//5%M,z[1]//5%M)
            nonunit[u]+=1
    assert 2*sum(counts.values())+sum(nonunit.values())==len(qomega)==109
    return counts,nonunit


def project_native_conductor2(Qmax,ray250,twist=T):
    """Full 2,5-unit convolution FIRST; then original order selector.
    Separate even norms prime-to5 and first-nonunit lifts.
    """
    selected=Counter()
    odd=even=0
    for n,C in ray250.items():
        for (r2,t),cnt in C.items():
            if r2==(1,0):
                selected[t]+=cnt
                odd+=cnt
    for z in Qmax:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if n%2==0 and n%5!=0:
            assert z[1]%2==0
            selected[shifted_ray_tag(z,twist)]+=1
            even+=1
    return selected,odd,even


def full_gauge_countercertificate():
    assert integer_mul((0,1),(1,-1))==(41,0)
    assert quadratic_norm((0,1),D)==quadratic_norm((1,-1),D)==41
    assert prime_divisibility((0,1))==(1,0)
    assert prime_divisibility((1,-1))==(0,1)
    assert prime_divisibility((41,0))==(1,1)
    assert conjugate(T,M)==scale(-1,T,M)
    assert conjugate(BAD_T,M)==BAD_T

    lookup,local=exhaustive_lift_table(D)
    q60,bins60,stress=full_heldout_twist_certificate(60)
    q21,bins21,native=full_heldout_twist_certificate(21)
    assert len(q60)==1785 and len(q21)==225

    local_checks=0
    changed_log_ideals=0
    for z in q60:
        if z==(0,0) or not is_unit(z,D):
            continue
        synthetic=shifted_generator_invariants(z,lookup)
        local_checks+=1
        if shifted_ray_tag(z)!=signed_ray125_tag(z,D):
            changed_log_ideals+=1
    assert changed_log_ideals>0

    # Recheck antisymmetry of prime-factor valuation under exact ring
    # products, independently of ray algebra.
    valprod=0
    controls=((0,1),(1,-1),(2,0),(1,1),(3,1),(5,0))
    for z in q21:
        if z==(0,0):
            continue
        for w in controls:
            assert antisymmetric_valuation(integer_mul(z,w))==(
                antisymmetric_valuation(z)+antisymmetric_valuation(w))
            assert antisymmetric_valuation(conjugate(z,None))==-antisymmetric_valuation(z)
            valprod+=1

    qint,qomega,Gdirect,source=original_integer_source_oracle()
    actual_unit,nonunit=unit_and_nonunit_counts(qomega)
    assert sum(actual_unit.values())==50 and sum(nonunit.values())==9
    baseline=gram_from_unit_rays_and_nonunit_lifts(actual_unit,nonunit,lookup)
    assert np.array_equal(baseline,Gdirect)

    twisted_unit,twisted_non=actual_original_ray_twist(qomega)
    assert twisted_non==nonunit
    selected,odd,even=project_native_conductor2(q21,bins21)
    assert selected==twisted_unit
    assert odd==26 and even==24
    twisted_G=gram_from_unit_rays_and_nonunit_lifts(selected,nonunit,lookup)
    assert np.array_equal(twisted_G%5,Gdirect%5)
    diff=(twisted_G-Gdirect)%M
    first_diff=None
    changed_cells=np.argwhere(diff)
    if len(changed_cells):
        i,j=changed_cells[0]
        first_diff={"row":int(i),"col":int(j),
                    "synthetic_minus_actual_mod25":int(diff[i,j])}

    zero_unit,zero_non=actual_original_ray_twist(qomega,(0,0))
    assert zero_unit==actual_unit and zero_non==nonunit
    assert np.array_equal(
        gram_from_unit_rays_and_nonunit_lifts(zero_unit,zero_non,lookup),Gdirect)

    bad_z=(0,1)
    assert antisymmetric_valuation(bad_z)==1
    bad_shift=shifted_ray_tag(bad_z,BAD_T)
    synthetic_bad=lookup[bad_shift]
    assert norm(synthetic_bad,D,TOP)!=norm(bad_z,D,TOP),(
        "bad traceful twist unexpectedly preserved the original norm")
    bar=conjugate(bad_z,None)
    assert shifted_ray_tag(bar,BAD_T)[1]!=conjugate(
        shifted_ray_tag(bad_z,BAD_T)[1],M)

    return {
        "field_D":D,
        "class_number_one_external_input":True,
        "exact_norm41_conjugate_prime_generators":{
            "omega":(0,1),"conjugate_omega":(1,-1),"product":(41,0)},
        "trace_zero_depth2_wild_shift":T,
        "shift_reduction_mod5_is_zero":True,
        "global_h1_full_signed_ray250_heldout":stress,
        "global_h1_full_signed_ray250_native":native,
        "unit_generator_norm_mod125_and_conjugation_checks":local_checks,
        "units_whose_second_wild_log_changed":changed_log_ideals,
        "exact_principal_ideal_valuation_product_tests":valprod,
        "original_native_integer_source_Q":len(qomega),
        "original_native_primitive_modulus":M,
        "native_original_Gram_entries_compared":int(Gdirect.size),
        "native_original_G_F5_rank":rank_f5(Gdirect%5),
        "synthetic_twisted_G_F5_rank":rank_f5(twisted_G%5),
        "synthetic_vs_actual_Gram_equal_mod5":True,
        "synthetic_vs_actual_Gram_changed_mod25":bool(len(changed_cells)),
        "changed_mod25_matrix_cells":int(len(changed_cells)),
        "first_changed_original_matrix_cell_if_any":first_diff,
        "zero_twist_identical_original_ray_and_Gram":True,
        "traceful_twist_breaks_norm_mod125_and_conjugation":True,
        "synthetic_tags_not_actual_global_principal_generator_rays":True,
        "no_uniform_determinant_or_discriminant_bound_inferred":True,
    }


def main():
    print("PHASE316_NORM_PRESERVING_WILD_GAUGE_PASS",
          full_gauge_countercertificate(),flush=True)


if __name__=="__main__":
    main()
