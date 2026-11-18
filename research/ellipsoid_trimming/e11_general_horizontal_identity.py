#!/usr/bin/env python3
"""E11: exact 12x12 ordinary-Z-jet identity and universal mod-5 rank gate.

No Lean proof of the general determinant identity is claimed.
"""
import sympy as s
from math import factorial
D,a,t=s.symbols('D a t',integer=True)
def mul(x,y):
    return (s.expand(x[0]*y[0]-D*x[1]*y[1]),
            s.expand(x[0]*y[1]+x[1]*y[0]))
def power(z,n):
    q=(s.Integer(1),s.Integer(0))
    for _ in range(n): q=mul(q,z)
    return q
def source_matrix():
    out=[]
    for r in range(6):
        for k in range(2):
            row=[]
            for x in (0,a,t):
                for j in range(2):
                    if j>r:
                        row.extend([0,0]);continue
                    u=mul(power((x,1),r-j),power((x,-1),k))
                    f=factorial(r)//factorial(r-j)
                    row.extend([f*u[0],f*u[1]])
            out.append(row)
    return s.Matrix(out)
def H(d,b,c):
    m=2*c-b;v=m*m
    b2=b*b;b4=b2*b2;b6=b4*b2;b8=b4*b4;b10=b8*b2
    d2=d*d;d3=d2*d;d4=d3*d;d5=d4*d
    A8=3*(4*d+b2)*(28*d-9*b2)
    A6=4*(4*d+b2)*(1088*d2-132*d*b2+27*b4)
    A4=2*(159744*d4+34304*d3*b2+8176*d2*b4+24*d*b6-81*b8)
    A2=4*(589824*d5+479232*d4*b2+161536*d3*b4+11312*d2*b6+72*d*b8+27*b10)
    A0=(1024*d3+896*d2*b2+132*d*b4+9*b6)*(5120*d3+2432*d2*b2+20*d*b4-3*b6)
    return ((((A8*v+A6)*v+A4)*v+A2)*v+A0)
actual=source_matrix().det(method='domain-ge')
expected=s.Rational(1,256)*a**4*t**4*(t-a)**4*H(D,a,t)
assert s.expand(actual-expected)==0
print('PASS: exact 12x12 source-jet determinant polynomial identity.')
for d in range(5):
    for b in range(5):
        if b==0 or (d+b*b)%5:continue
        residues=[int(H(d,b,c))%5 for c in range(5)]
        assert all(x!=0 for x in residues)
        print('D,a mod5=',d,b,'H(t) mod5:',residues)
print('PASS: for 5 not dividing a, D+a^2=0 mod 5, all H(D,a,t) are nonzero.')
print('Thus distinct integer sample nodes give nonzero determinant.')
