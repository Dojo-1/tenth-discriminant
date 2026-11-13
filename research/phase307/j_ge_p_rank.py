#!/usr/bin/env python3
"""Phase307-H: exact closed-form ordinary-J>=p Frobenius source rank.

In Fp[x], (x^(p^2)-x)^p = x^(p^3)-x^p.
No heavy quotient matrix or new field-class-number theorem.
"""
from pathlib import Path
from math import isqrt
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase305"))
from frobenius_hermite_rank import kernel_census, valuation_weight


def is_prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def canonical_exponent(n,p):
    if p<2 or n<0:
        raise ValueError("prime>=2 and n>=0 required")
    if n<p:
        return n
    period=p**3-p
    return p+(n-p)%period


def quotient_rank_j_ge_p(R,S,p):
    if not (R>0 and S>=p and is_prime(p)):
        raise ValueError("J=S>=prime p required")
    image={canonical_exponent(r+p*s,p)
           for r in range(R) for s in range(S)}
    rank=len(image)
    assert rank<=p**3 and rank<=R*S
    return {"R":R,"S":S,"p":p,"original_J":S,
            "quotient_dimension":p**3,
            "exact_image_rank":rank,
            "first_level_h":R*S-rank,
            "existing_valuationWeight":valuation_weight(R,S,p)}


def independent_remainder_controls():
    controls=((9,3,3),(15,3,3),(25,4,3),(30,4,3),
              (15,5,5),(25,5,5),(40,6,5))
    out=[]
    for R,S,p in controls:
        fast=quotient_rank_j_ge_p(R,S,p)
        other=kernel_census(R,S,S,p)
        assert fast["exact_image_rank"]==other["image_rank"],(
            "canonical exponent collision vs actual quotient rank",R,S,p)
        assert fast["first_level_h"]==other["kernel_dimension"]
        out.append((R,S,p,fast["first_level_h"],fast["existing_valuationWeight"]))
    return out


def native_policy_bounded_sweep():
    summary=[]
    for R in (100,200,400,800,1600):
        S=R//25
        primes=[p for p in range(3,S+1,2) if is_prime(p)]
        cases=[quotient_rank_j_ge_p(R,S,p) for p in primes]
        positive=[(x["p"],x["first_level_h"]-x["existing_valuationWeight"])
                  for x in cases
                  if x["first_level_h"]>x["existing_valuationWeight"]]
        max_delta=max((x["first_level_h"]-x["existing_valuationWeight"]
                       for x in cases),default=None)
        summary.append({"R":R,"S":S,"primes_tested":primes,
                        "positive_h_minus_weight":positive,
                        "max_difference":max_delta,
                        "all_inertness_conditions_untested":True})
    return summary


def main():
    c=independent_remainder_controls()
    s=native_policy_bounded_sweep()
    print("PHASE307_J_GE_P_CANONICAL_EXPONENT_PASS",{
        "actual_quotient_relation":"(x^(p^2)-x)^p=x^(p^3)-x^p",
        "independent_polynomial_remainder_checks":c,
        "bounded_original_source_policy_R_and_S":s,
        "not_every_tested_prime_is_inert_for_an_actual_field":True,
        "no_asymptotic_or_new_h1_cutoff":True
    },flush=True)


if __name__=="__main__":
    main()
