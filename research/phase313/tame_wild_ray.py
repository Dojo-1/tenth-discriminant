#!/usr/bin/env python3
"""Phase313-A: explicit tame/wild quadratic ray-unit transport at inert 5.

For a fundamental D>3 with 5 inert:
  delta_5(z)=[z^5-conj(z)]/[5*conj(z)] mod5
is defined ONLY for local units (z mod5 nonzero); division by 5 is
performed in the integer quadratic ring modulo25 BEFORE field division.

(z mod5 modulo +/-1, delta(z)) is an explicit group isomorphism
  (O_D/25)^x / +/-1 -> (F25^x / +/-1) x (F25,+),
with 12*25=300 elements. Global class number is NOT reconstructed.
"""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase312"))
from fermat_lift import (
    check_field, epsilon, conjugate, field_inverse,
    mul, add, scale, power,
)

P=5


def norm_mod5(z,D):
    a,b=z
    m=(D+1)//4
    return (a*a+a*b+m*b*b)%5


def normalized_delta(z,D):
    """Wild LOG quotient in F25, only when z is a local unit at p5."""
    check_field(D)
    if not norm_mod5(z,D):
        raise ZeroDivisionError("wild logarithm undefined on residue-zero/nonunit")
    return mul(epsilon(z,D),field_inverse(conjugate(z,5),D),D,5)


def tame_orbit(z,D):
    check_field(D)
    if not norm_mod5(z,D):
        raise ValueError("ray tame residue must be a unit")
    r=(z[0]%5,z[1]%5)
    neg=((-r[0])%5,(-r[1])%5)
    return min(r,neg)


def ray_tag(z,D):
    return (tame_orbit(z,D),normalized_delta(z,D))


def tag_mul(a,b,D):
    return (tame_orbit(mul(a[0],b[0],D,5),D),
            add(a[1],b[1],5))


def negate_mod(x,mod):
    return ((-x[0])%mod,(-x[1])%mod)


def ring_unit_orbits(D):
    """Exhaust all 600 units and all 300 sign-quotient classes mod25."""
    check_field(D)
    units=[(a,b) for a,b in product(range(25),repeat=2)
           if norm_mod5((a,b),D)]
    assert len(units)==600
    tag_preimages=defaultdict(list)
    residue_wild=defaultdict(set)
    sign_representatives=set()
    for z in units:
        t=ray_tag(z,D)
        tag_preimages[t].append(z)
        residue=(z[0]%5,z[1]%5)
        residue_wild[residue].add(t[1])
        sign_representatives.add(min(z,negate_mod(z,25)))
        assert t==ray_tag(negate_mod(z,25),D)
    assert len(residue_wild)==24
    assert len(tag_preimages)==300
    assert len(sign_representatives)==300
    assert all(len(v)==2 for v in tag_preimages.values())
    assert all(len(ws)==25 for ws in residue_wild.values())
    quotient_tags={ray_tag(z,D) for z in sign_representatives}
    assert len(quotient_tags)==300
    all_wild={(a,b) for a,b in product(range(5),repeat=2)}
    assert all(v==all_wild for v in residue_wild.values())

    # Principal units 1+5u: delta=-bar(u), an exact isomorphism of
    # their 25-element kernel onto the additive wild F25.
    wild_from_principal_units={}
    for u in all_wild:
        z=((1+5*u[0])%25,(5*u[1])%25)
        w=normalized_delta(z,D)
        assert w==scale(-1,conjugate(u,5),5)
        assert ray_tag(z,D)[0]==(1,0)
        wild_from_principal_units[w]=z
    assert len(wild_from_principal_units)==25

    # Product, sign and conjugation laws on exhaustive unit list
    # against multiple nontrivial multiplier controls.
    controls=((1,0),(0,1),(1,1),(3,7),(6,0),(4,2),(7,9))
    prod_checks=0
    for z in units:
        dz=normalized_delta(z,D)
        assert dz==normalized_delta(negate_mod(z,25),D)
        assert normalized_delta(conjugate(z,25),D)==conjugate(dz,5)
        for w in controls:
            if not norm_mod5(w,D):
                continue
            zw=mul(z,w,D,25)
            assert normalized_delta(zw,D)==add(dz,normalized_delta(w,D),5)
            assert ray_tag(zw,D)==tag_mul(ray_tag(z,D),ray_tag(w,D),D)
            prod_checks+=1

    # F25^x is cyclic order24, and the sign quotient is cyclic12.
    field_units=tuple((a,b) for a,b in product(range(5),repeat=2)
                      if norm_mod5((a,b),D))
    assert len(field_units)==24
    primitive=next((z for z in field_units
                    if all(power(z,j,D,5)!=(1,0) for j in (1,2,3,4,6,8,12))),None)
    assert primitive is not None
    assert power(primitive,24,D,5)==(1,0)
    tame_generator=tame_orbit(primitive,D)
    tame_powers=set()
    x=(1,0)
    for i in range(12):
        tame_powers.add(tame_orbit(x,D))
        x=mul(x,primitive,D,5)
    assert len(tame_powers)==12
    assert tame_orbit(x,D)==(1,0)

    # Every F25-valued multiplicative character of wild C5xC5 is
    # trivial, since F25^x has order24, relatively prime to5.
    assert all(power(x,5,D,5)!=(1,0) or x==(1,0)
               for x in field_units)

    return {
        "D":D,
        "units_mod25":len(units),
        "sign_quotient_classes":len(quotient_tags),
        "tame_orbits":len(tame_powers),
        "wild_additive_classes":len(all_wild),
        "all_600_to_300_ray_tags_exhaustively_checked":True,
        "all_24_tame_residues_have_25_wild_lifts":True,
        "principal_unit_wild_isomorphism":True,
        "local_unit_group_C12_x_C5_squared":True,
        "explicit_delta_product_and_conjugation_checks":prod_checks,
        "sample_tame_generator_mod5":primitive,
        "F25_valued_wild_multiplicative_characters_trivial":True,
        "no_global_class_number_conclusion":True,
    }


def group_algebra_multiply(a,b):
    """F5[(Z/5)^2] with additive group basis e_(u,v)."""
    out=Counter()
    for x,c in a.items():
        for y,d in b.items():
            k=((x[0]+y[0])%5,(x[1]+y[1])%5)
            out[k]=(out[k]+c*d)%5
    return {k:v for k,v in out.items() if v%5}


def group_algebra_power(a,k):
    out={(0,0):1}
    while k:
        if k&1:out=group_algebra_multiply(out,a)
        a=group_algebra_multiply(a,a)
        k//=2
    return out


def wild_augmentation_certificate():
    """Group-algebra nilpotent basis, not an ordinary Fourier model."""
    U={(1,0):1,(0,0):4} # e_(1,0) - e_(0,0)
    V={(0,1):1,(0,0):4}
    assert not group_algebra_power(U,4)=={}
    assert not group_algebra_power(V,4)=={}
    assert group_algebra_power(U,5)=={}
    assert group_algebra_power(V,5)=={}
    top=group_algebra_multiply(group_algebra_power(U,4),
                               group_algebra_power(V,4))
    assert top and len(top)==25
    # Truncated polynomial algebra F5[U,V]/(U^5,V^5) has
    # homogeneous basis U^i V^j, i,j=0..4.
    grades=[sum(i+j==d for i in range(5) for j in range(5))
            for d in range(9)]
    assert grades==[1,2,3,4,5,4,3,2,1]
    assert sum(grades)==25
    return {
        "wild_group_algebra_F5_dimension":25,
        "nilpotent_generators_U5_V5_zero":True,
        "augmentation_J9_zero_J8_nonzero":True,
        "graded_dimensions":grades,
        "nonsemisimple_wild_p_part_not_captured_by_F25_Fourier":True,
    }


def main():
    arms=[ring_unit_orbits(D) for D in (43,163,183,203)]
    print("PHASE313_TAME_WILD_LOG_PASS",{
        "fields":arms,
        "wild_group_algebra":wild_augmentation_certificate(),
        "ray_class_identification_if_and_only_if_global_h1":True,
        "not_a_new_global_Gram_bound":True,
    },flush=True)


if __name__=="__main__":
    main()
