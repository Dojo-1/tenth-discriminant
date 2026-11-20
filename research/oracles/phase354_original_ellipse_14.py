#!/usr/bin/env python3
"""Phase354 source exactness: deterministic finite oracle; NOT a Lean proof.

The full original ellipse and exact ceiling 11/25*D^(3/4) are
reconstructed by integer arithmetic only. No float, no subset,
no Hasse-derivative or trace substitution.
"""
from math import isqrt
from fractions import Fraction
import json
import random

def floor_scaled_root(num, den, d, power):
    assert d > 0 and power in (1, 3)
    target = num**4 * d**power
    lo, hi = 0, 1
    while (den*hi)**4 <= target:
        hi *= 2
    while lo + 1 < hi:
        m = (lo+hi)//2
        if (den*m)**4 <= target:
            lo = m
        else:
            hi = m
    return lo

def ceil_scaled_root(num, den, d, power):
    v = floor_scaled_root(num, den, d, power)
    return v if (den*v)**4 == num**4*d**power else v+1

def full_ellipse_count(d, rho):
    ymax = isqrt(rho*rho//d)
    return sum(2*isqrt(rho*rho-d*y*y)+1
               for y in range(-ymax, ymax+1))

def case(d):
    assert d >= 14**4
    rho = ceil_scaled_root(11, 25, d, 3)
    card = full_ellipse_count(d, rho)
    R, S = d//4, (d//4)//25
    required = 2*R+S
    assert card > required
    return dict(D=d, radius=rho, Q_card=card,
                two_R_plus_S=required, surplus=card-required)

def run():
    assert Fraction(157,50)*Fraction(101,250)**2 > Fraction(51,100)
    assert Fraction(1+13**2,2) > Fraction(9,250)*13**3
    assert Fraction(1+14**2,2) <= Fraction(9,250)*14**3
    rng = random.Random(354)
    ds = set(range(14**4,14**4+121))
    for b in (14,15,16,17,18,19,20,21,23,27,35,50):
        for delta in (-1,0,1):
            d = b**4+delta
            if d >= 14**4: ds.add(d)
    while len(ds)<240:
        ds.add(rng.randrange(14**4,50**4+1))
    rows = [case(d) for d in sorted(ds)]
    assert len(rows)==240
    return dict(evidence="M, exact integer bounded oracle, no field theorem",
                source="original complete ellipse, unchanged Tuned R/S/rho",
                cases=len(rows), seed=354,
                min_surplus=min(x["surplus"] for x in rows),
                endpoint=case(14**4),
                selected=[case(b**4) for b in (14,15,20,21,35,50)],
                negative_control="at t=13 the selected error envelope fails")

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
