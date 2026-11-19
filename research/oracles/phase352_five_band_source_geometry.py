#!/usr/bin/env python3
"""Phase352: five-band inner-polygon original-ellipse exact integer oracle.

The UNIFORM all-D argument appears separately in the research note.
This executable is a deterministic 110-case arithmetic checker, not
a Lean proof for infinitely many D or a field discriminant claim.

No floating roots: comparisons of integer fourth powers construct
floor(alpha*D^(1/4)), floor(beta*D^(3/4)), and ceil(radius).
"""
from math import isqrt
import random
import json

BETAS=(43,40,36,30,18)
assert all(beta*beta+(8*i)**2<=44**2 for i,beta in enumerate(BETAS,1))

def floor_scaled_root(num,den,d,power):
    target=num**4*d**power
    high=1
    while (den*high)**4<=target:
        high*=2
    low=0
    while low+1<high:
        mid=(low+high)//2
        if (den*mid)**4<=target:low=mid
        else:high=mid
    return low

def ceil_scaled_root(num,den,d,power):
    low=floor_scaled_root(num,den,d,power)
    return low if (den*low)**4==num**4*d**power else low+1

def exact_source_count(d,radius):
    max_y=isqrt(radius*radius//d)
    return sum(2*isqrt(radius*radius-d*y*y)+1
               for y in range(-max_y,max_y+1))

def case(d):
    radius=ceil_scaled_root(11,25,d,3)
    ys=[0]+[floor_scaled_root(2*i,25,d,1) for i in range(1,6)]
    xs=[floor_scaled_root(beta,100,d,3) for beta in BETAS]
    assert ys==sorted(ys)
    assert all(xs[i-1]**2+d*ys[i]**2<=radius**2 for i in range(1,6))
    five_band=2*sum((ys[i]-ys[i-1])*(2*xs[i-1]+1) for i in range(1,6))
    r=d//4;s=r//25
    required=2*(r-1)+(s-1)
    full=exact_source_count(d,radius)
    assert five_band>required
    assert full>=five_band
    return {
      "D":d,"thinRadius":radius,"original_count":full,
      "original_interpolation_required":required,
      "five_band_count_lower":five_band,
      "five_band_surplus":five_band-required
    }

def run():
    rng=random.Random(351)
    ds=set()
    for b in [274,275,280,290,298,301,302,303,306,307,320,500]:
        for delta in (-1,0,1):
            d=b**4+delta
            if d>=274**4:ds.add(d)
    for _ in range(75):
        ds.add(rng.randrange(274**4,600**4))
    rows=[case(d) for d in sorted(ds)]
    assert len(rows)==110
    assert 61*274**4-16700*274**3-2000*274+32500>0
    return rows

if __name__=="__main__":
    rows=run()
    print(json.dumps({
      "evidence":"M, deterministic 110 exact integer cases",
      "symbolic_thesis":"five rational bands yield N > 334/625*t^4 - 167/25*t^3 - 4/5*t +10, t=D^(1/4) >= 274; uniform proof to be ported to Lean",
      "not_proved_in_code":"uniform theorem for all D, or any field discriminant improvement",
      "sample_count":len(rows),"minimum_certificate_surplus":
          min(x["five_band_surplus"] for x in rows),
      "selected": [r for r in rows if r["D"] in
          (274**4,302**4,306**4,307**4)]
    },indent=2))
