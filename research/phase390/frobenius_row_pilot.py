"""Phase390 exact combined Frobenius row source/jet pilot.

For the ONE original row (r,s)=(p,p^2), with R=p+1, S=p^2+2,
the original Phase228 k=min(r//p,S-1-s)=1 and ell=s//(p*p)=1.
Its unimodular combined row has exactly FOUR original monomials:

Z^p W^(p^2) - Z^p W - W^(p^2+1) + W^2
= (Z^p-W)(W^(p^2)-W),

where ordinary d/dZ fixes W, W=conj(z) only AFTER differentiation.

This is a bounded semantic row-by-row pilot, not proof of the
universal unimodular source action, all rows, or production Gram.
"""
from research.phase390.independent_source_oracle import (
    source_points,derivative,mul_source,power,falling)

def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def scale(k,a):return k*a[0],k*a[1]
def conj(a):return a[0],-a[1]

def combination(D,p,z,j):
    pieces=((1,p,p*p),(-1,p,1),(-1,0,p*p+1),(1,0,2))
    out=(0,0)
    for coeff,r,s in pieces:
        out=add(out,scale(coeff,derivative(D,r,s,j,z,"source")))
    return out

def factored(D,p,z,j):
    w=conj(z)
    wPower=power(mul_source,D,w,p*p)
    h=sub(wPower,w)
    if j==0:
        zPower=power(mul_source,D,z,p)
        return mul_source(D,sub(zPower,w),h)
    if j<=p:
        zPower=power(mul_source,D,z,p-j)
        return scale(falling(p,j),mul_source(D,zPower,h))
    return(0,0)

def p_divisible(z,p,k):
    return z[0]%(p**k)==0 and z[1]%(p**k)==0

def row_pilot(D,p,rho):
    assert p in (3,5)
    Q=source_points(D,rho)
    R,S=p+1,p*p+2
    r,s=p,p*p
    k=min(r//p,S-1-s)
    ell=s//(p*p)
    assert (k,ell)==(1,1)
    count=0
    for z in Q:
        for j in range(p+3):
            row=combination(D,p,z,j)
            prod=factored(D,p,z,j)
            if row!=prod:raise AssertionError(("source polynomial identity",D,p,z,j,row,prod))
            if not p_divisible(row,p,k+ell):
                raise AssertionError(("inert combined row not p^2-divisible",D,p,z,j,row))
            count+=1
    return {"D":D,"p":p,"R":R,"S":S,"k":k,"ell":ell,
            "Q":len(Q),"ordinary_jets_checked":count,
            "whole_row_p2_divisible":True,
            "scope":"FIXED_COMBINED_ROW_INERT_SOURCE_ONLY"}

def split_prime_counterexample(D,p,span=4):
    for x in range(-span,span+1):
        for y in range(-span,span+1):
            z=(x,y);j=0
            a=combination(D,p,z,j)
            if not p_divisible(a,p,2):
                if a!=factored(D,p,z,j):raise AssertionError("identity mismatch")
                return {"D":D,"p":p,"z":z,"j":0,"combined_row":a,
                        "p_squared_divisibility_fails":True}
    raise AssertionError("no split-prime counterexample in bounded search")

if __name__=="__main__":
    for D,p,rho in ((163,3,18),(163,5,18)):
        print(row_pilot(D,p,rho))
    for D,p in ((11,3),(19,5)):
        print("SPLIT NEGATIVE:",split_prime_counterexample(D,p))
