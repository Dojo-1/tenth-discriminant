#!/usr/bin/env python3
"""Exact ordinary-Z-jet E9 rank counterworld; no integer singularity claim."""
import sympy as s
Z,W=s.symbols("Z W")
x=s.symbols("x",real=True)
P=3*x**8-24*x**7-40*x**6+576*x**5-2448*x**4+5504*x**3-12288*x**2+15360*x-13312
def feature(abscissa):
    mat=[]
    for r in range(6):
        for t in range(2):
            row=[]
            for a in (0,2,abscissa):
                for j in range(2):
                    f=s.expand(s.diff(Z**r*W**t,Z,j).subs({Z:a+s.I,W:a-s.I}))
                    row.extend([s.expand(s.re(f)),s.expand(s.im(f))])
            mat.append(row)
    return s.Matrix(mat)
symbolic=s.factor(feature(x).det(method="domain-ge"))
assert s.expand(symbolic-(-1024*x**4*(x-2)**4*P))==0
for v,expected in ((7,3063195031680000),(8,-2733042309267456)):
    assert feature(v).det(method="domain-ge")==expected
assert P.subs(x,7)<0<P.subs(x,8)
print("PASS: exact symbolic source determinant; by IVT a real singular x lies in (7,8).")
print("NOT a singular integer-coordinate lattice observation.")
