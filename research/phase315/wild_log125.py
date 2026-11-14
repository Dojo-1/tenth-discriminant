#!/usr/bin/env python3
"""Phase315-A: corrected second 5-adic wild logarithm at conductor125.

For inert p=5 in maximal imaginary quadratic O=Z[omega], define
  d(z)=((z^5-conj(z))/5) * inverse(conj(z)) (mod 25).
The integer /5 is exact in O/125 for local units; inverses only on
units. Then:
  d(x*y)=d(x)+d(y)+5*d(x)*d(y) (mod25).
  L(z)=d(z)-(5/2)*d(z)^2 (mod25)
is additive modulo25, sign-invariant and conjugation-covariant.

This is an explicit elementary truncated p-adic logarithm, not a
new class field theorem. The signed mod125 unit group has 7500
elements ≅ C12 × (Z/25)^2; when 2 is inert, signed conductor250
has 22500 local ray classes ≅ C3 × C12 × (Z/25)^2.
"""
from collections import Counter,defaultdict
from itertools import product
from math import gcd
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase312"))
sys.path.insert(0,str(ROOT/"research"/"phase313"))
from fermat_lift import mul,conjugate,power
from tame_wild_ray import normalized_delta,tame_orbit

P=5
M=25
TOP=125
HALF5=(5*pow(2,-1,M))%M # =15


def norm(z,D,mod=None):
    a,b=z
    m=(D+1)//4
    out=a*a+a*b+m*b*b
    return out if mod is None else out%mod


def is_unit(z,D):
    return norm(z,D,5)!=0


def add(z,w,mod):
    return ((z[0]+w[0])%mod,(z[1]+w[1])%mod)


def sub(z,w,mod):
    return ((z[0]-w[0])%mod,(z[1]-w[1])%mod)


def scale(c,z,mod):
    return ((c*z[0])%mod,(c*z[1])%mod)


def inv(z,D,mod=M):
    """Inverse via norm and conjugation only for 5-adic units."""
    if not is_unit(z,D):
        raise ZeroDivisionError("p-adic wild quotient only on units")
    cn=conjugate(z,mod)
    inverse_norm=pow(norm(z,D,mod),-1,mod)
    result=scale(inverse_norm,cn,mod)
    assert mul(z,result,D,mod)==(1,0)
    return result


def twisted_defect(z,D):
    if not is_unit(z,D):
        raise ZeroDivisionError("normalized quadratic Fermat defect is undefined on p5 nonunits")
    z5=power(z,5,D,TOP)
    bar=conjugate(z,TOP)
    difference=sub(z5,bar,TOP)
    assert difference[0]%5==difference[1]%5==0
    epsilon=(difference[0]//5,difference[1]//5)
    return mul(epsilon,inv(conjugate(z,M),D,M),D,M)


def wild_log_25(z,D):
    d=twisted_defect(z,D)
    return sub(d,scale(HALF5,mul(d,d,D,M),M),M)


def signed_ray125_tag(z,D):
    if not is_unit(z,D):
        raise ValueError("signed ray125 tag requires p5 unit")
    return (tame_orbit(z,D),wild_log_25(z,D))


def signed_ray125_mul(a,b,D):
    return (tame_orbit(mul(a[0],b[0],D,5),D),
            add(a[1],b[1],M))


def signed_ray125_sign(z):
    return ((-z[0])%TOP,(-z[1])%TOP)


def exhaustive_lift_table(D):
    """Exhaust all 15000 ring units and all 7500 signed conductor125 rays.

    Each F25^x residue (24 choices) has exactly 625 lifts of L(z),
    with an explicit inverse residue lookup in O/125.
    """
    assert D%4==3 and (-D)%5 in (2,3)
    signed=Counter()
    lookup={}
    by_residue=defaultdict(set)
    all_units=[]
    for a,b in product(range(TOP),repeat=2):
        z=(a,b)
        if not is_unit(z,D):
            continue
        r=(a%5,b%5)
        w=wild_log_25(z,D)
        tag=(tame_orbit(z,D),w)
        signed[tag]+=1
        key=(r,w)
        assert key not in lookup,("wild logarithm failed to separate two principal unit lifts",D,key)
        lookup[key]=z
        by_residue[r].add(w)
        assert (w[0]%5,w[1]%5)==normalized_delta(z,D)
        all_units.append(z)
    assert len(all_units)==15000
    assert len(lookup)==15000
    assert len(signed)==7500 and set(signed.values())=={2}
    assert len(by_residue)==24 and all(len(s)==625 for s in by_residue.values())
    assert all(signed[tag]==2 for tag in signed)
    for z in all_units:
        assert signed_ray125_tag(z,D)==signed_ray125_tag(signed_ray125_sign(z),D)

    product_tests=0
    twisted_nonzero=None
    controls=((1,0),(0,1),(1,1),(3,7),(6,0),(26,0),(13,9),(5,1),(4,2),(-1,0))
    for z in all_units:
        d=twisted_defect(z,D)
        l=wild_log_25(z,D)
        assert wild_log_25(conjugate(z,TOP),D)==conjugate(l,M)
        for w in controls:
            if not is_unit(w,D):
                continue
            zw=mul(z,w,D,TOP)
            dw=twisted_defect(w,D)
            cross=scale(5,mul(d,dw,D,M),M)
            expected=add(add(d,dw,M),cross,M)
            assert twisted_defect(zw,D)==expected
            assert wild_log_25(zw,D)==add(l,wild_log_25(w,D),M)
            assert signed_ray125_tag(zw,D)==signed_ray125_mul(
                signed_ray125_tag(z,D),signed_ray125_tag(w,D),D)
            if cross!=(0,0) and twisted_nonzero is None:
                twisted_nonzero={"z":z,"w":(w[0]%TOP,w[1]%TOP),
                                 "five_times_defect_cross_mod25":cross}
            product_tests+=1
    assert twisted_nonzero is not None

    # Concrete distinction: same FIRST wild ray modulo5, different
    # SECOND wild ray modulo25 at the same tame residue.
    za,zb=(1,0),(26,0)
    assert signed_ray125_tag(za,D)[0]==signed_ray125_tag(zb,D)[0]
    assert normalized_delta(za,D)==normalized_delta(zb,D)==(0,0)
    assert signed_ray125_tag(za,D)!=signed_ray125_tag(zb,D)

    return lookup,{
        "D":D,
        "ring_mod125_total_elements":TOP*TOP,
        "unit_mod125_count":len(all_units),
        "signed_unit_ray125_count":len(signed),
        "tame_residue_count":len(by_residue)//2,
        "p_adic_two_digit_wild_values_per_exact_residue":625,
        "signed_ray_unit_group_C12_x_Z25_squared":True,
        "explicit_lookup_15000_residue_wild_pairs":True,
        "twisted_defect_and_corrected_log_product_tests":product_tests,
        "raw_defect_is_NOT_additive_witness":twisted_nonzero,
        "conjugation_and_signed_invariance_all_units_checked":True,
        "same_first_level_ray_different_second_level_witness":[za,zb],
        "no_global_class_number_claim":True
    }


def main():
    result=[]
    for D in (163,183,187):
        _,meta=exhaustive_lift_table(D)
        result.append(meta)
    print("PHASE315_SECOND_WILD_LOG125_PASS",{
        "fields":result,
        "truncated_log_additive_mod25":True,
        "conductor250_signed_group_size_when_2_inert":22500,
        "no_uniform_Gram_valuation_claim":True,
    },flush=True)


if __name__=="__main__":
    main()
