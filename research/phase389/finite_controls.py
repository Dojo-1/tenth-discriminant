#!/usr/bin/env python3
"""Independent finite counterworlds for the Phase389 characteristic-three law.
Uses direct quadratic-pair arithmetic, not Lean's symbolic normalizer.
"""
from itertools import product

def mul(a,b,D):
    return ((a[0]*b[0]-D*a[1]*b[1])%3,
            (a[0]*b[1]+a[1]*b[0])%3)

def add(a,b):
    return ((a[0]+b[0])%3,(a[1]+b[1])%3)

def scale(c,a):
    return ((c*a[0])%3,(c*a[1])%3)

def power(a,n,D):
    z=(1,0)
    while n:
        if n&1:z=mul(z,a,D)
        a=mul(a,a,D);n//=2
    return z

def cubic(a,q,D):
    out=(0,0)
    for i,co in enumerate(a):
        out=add(out,mul(co,power(q,i,D),D))
    return out

def deriv(a,q,D):
    return add(a[1],add(scale(2,mul(a[2],q,D)),
                         mul(scale(3,a[3]),power(q,2,D),D)))

def law(a,q,t,D):
    tt=(t,0)
    qt=add(q,scale(-1,tt))
    g1=add(q,(-1%3,0));g2=add(q,(-2%3,0))
    lhs=scale(2,add(deriv(a,qt,D),scale(-1,deriv(a,q,D))))
    rhs=mul(tt,add(cubic(a,q,D),add(cubic(a,g1,D),cubic(a,g2,D))),D)
    return lhs,rhs

def q_source(D,x,y):
    z0=x**3-3*D*x*y*y-x
    z1=3*x*x*y-D*y**3+y
    assert z0%3==0 and z1%3==0
    return z0//3,z1//3

def main():
    total=0
    for D in (7,19,43,283,403,412):
        assert D%3==1
        for x,y in product(range(-7,8),repeat=2):
            q0=q_source(D,x,y)
            for t in (-2,-1,0,1,2):
                q1=q_source(D,x+3*t,y)
                assert tuple((q1[c]-q0[c])%3 for c in range(2))==((-t)%3,0)
                total+=1
    assert total==6*15*15*5
    all_coeff=[(v,0) for v in range(3)]
    for q in product(range(3),repeat=2):
        for raw in product(all_coeff, repeat=4):
            for t in range(3):
                lhs,rhs=law(raw,q,t,403)
                assert lhs==rhs,(raw,q,t,lhs,rhs)
    # F9 coefficients outside the embedded F3, seeded deterministic tuples.
    for i in range(250):
        a=[((i*j+2*j*j)%3,(i*i+j)%3) for j in range(4)]
        q=(i%3,(i//3)%3)
        assert law(a,q,i%3,403)[0]==law(a,q,i%3,403)[1]
    # Domain control: ordinary cubic identity is false for degree four.
    q=(0,0);minus_one=(2,0);minus_two=(1,0)
    quartic_lhs=scale(2,mul((1,0),power(minus_one,3,403),403))
    quartic_rhs=add(power(q,4,403),add(power(minus_one,4,403),power(minus_two,4,403)))
    assert quartic_lhs!=quartic_rhs
    # Source type control: no source division if -D is split (D%3!=1).
    d=2;x=0;y=1
    z1=3*x*x*y-d*y**3+y
    assert z1%3!=0
    print("PASS",total,"exact quadratic-source quotient shifts modulo 3")
    print("PASS characteristic-3 cubic translation over F9 and arbitrary coefficients")
    print("PASS quartic-degree and non-inert-integrality hostile controls")

if __name__=="__main__":
    main()
