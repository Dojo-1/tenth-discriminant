#!/usr/bin/env python3
"""Exact occupied-class Smith-layer bound for the original source ellipse.

Paper premises external to this finite program:
  - normalized original ordinary Frobenius jets descend mod p^m from
    source coordinates modulo p^(m+1);
  - the original thin integer trace-Gram is nonsingular.
This computes no production determinant and uses no floating-point gate.
"""
from math import isqrt, log

D = 322**4 + 15
P = 3
R = D//4
S = R//25
J = S
RHO = 14_689_950
Y = isqrt(RHO*RHO//D)
N = R*S

def y_slices(D0=D,rho=RHO):
    limit=isqrt(rho*rho//D0)
    return [(y,isqrt(rho*rho-D0*y*y)) for y in range(-limit,limit+1)]

def count_by_residue(q,slices):
    """Separate enumerative oracle for only modest q."""
    occupied=set()
    for y,width in slices:
        for r in range(q):
            first=-width+(r+width)%q
            if first<=width:occupied.add((r,y%q))
    return len(occupied)

def count_by_slices(q,slices):
    """Exact when q exceeds the full height of the y interval."""
    ymin=slices[0][0];ymax=slices[-1][0]
    assert q>ymax-ymin
    return sum(min(q,2*width+1) for y,width in slices)

def small_ellipse_checks():
    for d,rho in ((3,4),(19,9),(43,12)):
        ys=y_slices(d,rho)
        points=[(x,y) for y,width in ys for x in range(-width,width+1)]
        for q in (3,9,27,81):
            a=len({(x%q,y%q) for x,y in points})
            assert a==count_by_residue(q,ys),(d,rho,q)
            if q>ys[-1][0]-ys[0][0]:
                assert a==count_by_slices(q,ys)
    print("PASS three small ellipses: direct point residue sets = modular slice counts")

def main():
    assert (D,R,S,Y)==(10_750_371_871,2_687_592_967,107_503_718,141)
    slices=y_slices()
    assert len(slices)==283
    assert sum(2*w+1 for y,w in slices)==6_538_432_431
    small_ellipse_checks()
    table=[]
    for m in range(1,16):
        q=P**(m+1)
        c=count_by_slices(q,slices) if q>2*Y else count_by_residue(q,slices)
        if m<=6:assert c==count_by_residue(q,slices)
        deficiency=max(0,N-2*J*c)
        table.append((m,q,c,deficiency))
        print(f"depth {m:2d} | modulus {q:>9} | occupied {c:>11} | certified Smith count {deficiency:>20}")
    assert [x[2] for x in table[:13]]==[
        81,729,6_561,59_049,206_307,618_921,1_856_763,
        5_570_289,16_710_867,50_132_601,150_397_803,
        451_193_409,1_349_220_519]
    assert all(x[3]>0 for x in table[:12])
    assert all(x[3]==0 for x in table[12:])
    total=sum(x[3] for x in table)
    assert total==3_321_607_828_039_681_992
    assert 2*total==6_643_215_656_079_363_984
    print("PASS twelve nonzero layers, source row-index lower >=",total)
    print("PASS independent residual Gram valuation lower >=",2*total)
    print("DISPLAY ONLY: normalized log contribution",2*total*log(3)/(R*R*S))
    print("NOT a computation of det(G) and NOT an improved field bound")

if __name__=="__main__":main()
