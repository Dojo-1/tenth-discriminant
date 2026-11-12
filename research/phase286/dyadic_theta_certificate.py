#!/usr/bin/env python3
"""Phase286: exactly rational maximal-order theta at t=ln(2), not an L-zero proof.

Preregistered at 203ace3 before this script. Deliberately separate from the
original trace Gram and from analytic continuation/Mellin zero questions.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb, isqrt
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve()
ROOT=HERE.parents[2]
sys.path.insert(0,str(HERE.parents[1]/"phase206"))
from source_probe import params

SOURCE_BLOB="3f954b59d9f86b06ad53667c869b5b24f2e6c7f6"
CASES={
    19:{"rho":5,"integer":21,"lens":15,"half":20,"first_norm":5,
        "powers":((0,0),(1,0),(2,1),(2,2))},
    403:{"rho":40,"integer":219,"lens":213,"half":260,"first_norm":101,
         "powers":((0,0),(1,0),(2,1),(2,2),(6,6))},
}

def two_minus(n):
    assert isinstance(n,int) and n>=0
    return F(1,1<<n)

def freeze_source():
    actual=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase206/source_probe.py"],
        cwd=ROOT,text=True).strip()
    assert actual==SOURCE_BLOB,("original source changed",actual)
    rho,R,S,J,Q=params(403)
    assert (rho,R,S,J,len(Q))==(40,100,4,4,219)
    return Q

def norm(D,z):
    x,y=z
    n=x*x+D*y*y
    assert n>=0 and n.denominator==1,("not a maximal-order integral norm",D,z,n)
    return int(n)

def integral_disk(D,rho):
    points=[]
    for y in range(-isqrt(rho*rho//D),isqrt(rho*rho//D)+1):
        r=isqrt(rho*rho-D*y*y)
        for x in range(-r,r+1):
            points.append((F(x),F(y)))
    return points

def half_coset_disk(D,rho):
    """Independent odd-coordinate a,b numerator enumeration."""
    result=[]
    bound=4*rho*rho
    for b in range(-isqrt(bound//D),isqrt(bound//D)+1):
        if b%2==0:
            continue
        reach=isqrt(bound-D*b*b)
        for a in range(-reach,reach+1):
            if a%2==0:
                continue
            z=(F(a,2),F(b,2))
            assert 4*norm(D,z)==a*a+D*b*b
            result.append(z)
    return result

def lens(D,rho,integer_points):
    rr=rho*rho
    return [z for z in integer_points if
        (z[0]-1)**2+D*z[1]**2<=rr and
        (z[0]+1)**2+D*z[1]**2<=rr]

def product(D,v,w):
    a,b=v; c,d=w
    return (a*c-D*b*d,a*d+b*c)

def power(D,z,n):
    v=(F(1),F(0))
    assert n>=0
    while n:
        if n&1:
            v=product(D,v,z)
        z=product(D,z,z)
        n>>=1
    return v

def polynomial_a(D,z,a,b):
    """Independent oracle: expand both powers by binomial coefficients."""
    x,y=z
    out=[F(0),F(0)]
    for i in range(a+1):
        for j in range(b+1):
            h=i+j
            v=F(comb(a,i)*comb(b,j)*(-1)**j)*x**(a+b-h)*y**h*(-D)**(h//2)
            out[h%2]+=v
    return (out[0],out[1])

def sample_moment(D,z,a,b,oracle=False):
    if oracle:
        value=polynomial_a(D,z,a,b)
    else:
        value=product(D,power(D,z,a),power(D,(z[0],-z[1]),b))
    factor=two_minus(norm(D,z))
    return (value[0]*factor,value[1]*factor)

def sum_moments(D,points,a,b,oracle=False):
    re=F(0);im=F(0)
    for z in points:
        v=sample_moment(D,z,a,b,oracle)
        re+=v[0];im+=v[1]
    return re,im

def tail(D,rho,m):
    """Two-coset shell tail bound at t=ln2, exact rational."""
    assert D>=1 and rho>=1 and m>=0
    k=m+2
    q=F((rho+3)**k,(rho+2)**k*(1<<(2*rho+1)))
    assert 0<q<1,("dyadic geometric tail invalid",D,rho,m,q)
    radius=F(8*(rho+2)**k,1<<(rho*rho))/(1-q)
    assert radius>0
    return q,radius

def certified_binary_bits(radius):
    """Return k with radius < 2^(-k); comparisons use only integers."""
    assert 0<radius<1
    k=max(0,radius.denominator.bit_length()-radius.numerator.bit_length()-2)
    while radius>=two_minus(k):
        k-=1
    while radius<two_minus(k+1):
        k+=1
    assert radius<two_minus(k) and radius>=two_minus(k+1)
    return k

def check_case(D,source_Q):
    spec=CASES[D]
    rho=spec["rho"]
    old=integral_disk(D,rho)
    if D==403:
        assert [(int(x),int(y)) for x,y in old]==source_Q
    mid=lens(D,rho,old)
    removed=[z for z in old if z not in set(mid)]
    half=half_coset_disk(D,rho)
    full=old+half
    assert len(old)==spec["integer"] and len(mid)==spec["lens"]
    assert len(half)==spec["half"] and len(removed)==len(old)-len(mid)
    assert len(set(full))==len(full)
    assert not (set(half)&set(old))
    assert all((-x,-y) in set(full) for x,y in full)
    assert all((-x,-y) in set(half) for x,y in half)
    assert all(norm(D,z)<=rho*rho for z in full)
    assert min(norm(D,z) for z in half)==spec["first_norm"]
    assert (F(0),F(0)) in mid and (F(0),F(0)) not in half

    # Independent radial histogram oracle, using only integer norms.
    histogram=Counter(norm(D,z) for z in full)
    radial_hist=sum(F(count)*two_minus(n) for n,count in histogram.items())
    radial_direct=sum_moments(D,full,0,0)[0]
    assert radial_hist==radial_direct

    observed=[]
    radial_half=None
    radial_tail=None
    for a,b in spec["powers"]:
        m=a+b
        # Two multiplication routes, every source point and every fixed power.
        for z in full:
            assert sample_moment(D,z,a,b)==sample_moment(D,z,a,b,True),(
                "independent binomial/power oracle mismatch",D,z,a,b)
        original=sum_moments(D,old,a,b)
        direct=sum_moments(D,full,a,b)
        l=sum_moments(D,mid,a,b)
        dropped=sum_moments(D,removed,a,b)
        h=sum_moments(D,half,a,b)
        assert tuple(original[i] for i in (0,1))==(
            l[0]+dropped[0],l[1]+dropped[1])
        assert direct==(l[0]+dropped[0]+h[0],l[1]+dropped[1]+h[1])
        if m%2:
            assert direct==(0,0) and l==(0,0) and h==(0,0),(
                "broken inversion",D,a,b,direct,l,h)
        q,rad=tail(D,rho,m)
        bits=certified_binary_bits(rad)
        if (a,b)==(0,0):
            expected=16 if D==19 else 1500
            assert rad<two_minus(expected),("radial tail too large",D,rad)
            radial_half=h[0]
            radial_tail=rad
            assert h[1]==0
            assert radial_half>=4*two_minus(spec["first_norm"])
            assert radial_half>rad,("half coset hidden as tail",D)
        if D==403 and (a,b)==(6,6):
            assert rad<two_minus(1500),("angular tail too large",D,rad)
        observed.append((a,b,bits))
    assert radial_half is not None and radial_tail is not None
    # A deliberately false Gaussian weight 2^(-4*N) cannot replace 2^(-N).
    radial_wrong=sum(two_minus(4*norm(D,z)) for z in full)
    assert radial_wrong<radial_hist
    print("PHASE286_EXACT_DYADIC",{
        "D":D,"rho":rho,
        "original_points":len(old),
        "lens_points":len(mid),
        "deleted_original_points":len(removed),
        "half_coset_points":len(half),
        "maximal_order_disk_points":len(full),
        "minimum_half_coset_norm":spec["first_norm"],
        "fixed_angular_moments_and_certified_tail_bits":observed,
        "radial_half_coset_exceeds_two_coset_outer_tail":True,
        "exact_fraction_two_oracles":True,
        "no_floating_point":True,
        "not_original_Gram_or_an_L_zero_theorem":True,
    },flush=True)

def main():
    source=freeze_source()
    for D in (19,403):
        check_case(D,source)
    print("PASS Phase286 exact two-coset dyadic theta and radial/angular bounds",flush=True)

if __name__=="__main__":
    main()
