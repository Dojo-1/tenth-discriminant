#!/usr/bin/env python3
"""Phase205-B: reproduce prior Phase137 monic frames and exact source-jet variance."""
from fractions import Fraction as F
from math import log
from source_spectral_pilot import G, rows, Q, D, R, S, J, jet

def pmul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C
base=[-12,1]
centered=[[1]];cheb=[[1]]
for m in range(1,S):
    centered.append(pmul(centered[-1],base))
    if m==1:cheb.append(base[:])
    elif m==2:
        v=pmul(cheb[1],base);v[0]-=86;cheb.append(v)
    else:
        v=pmul(cheb[-1],base)
        for j,c in enumerate(cheb[-2]):v[j]-=43*c
        cheb.append(v)
def upper(polys):
    out=1;n=len(rows)
    for r,s in rows:
        m=min(r,s);v=[0]*n
        for t,c in enumerate(polys[m]):v[rows.index((r-m+t,s-m+t))]=c
        d=sum(v[i]*G[i][j]*v[j] for i in range(n) for j in range(n))
        assert d>0
        out*=d
    return out
Lc=log(upper(centered));Lh=log(upper(cheb))
assert abs(Lc-585.557677543)<1e-8
assert abs(Lh-579.753853408)<1e-8

i=rows.index((3,1));k=rows.index((4,2))
a=G[i][i];b=G[i][k];c=G[k][k]
mu=F(0);mu2=F(0);mass=0;amax=F(0)
for j in range(J):
    for x,y in Q:
        z=jet(3,1,j,(x,y));w=2*(z[0]*z[0]+D*z[1]*z[1])
        value=F(4*(x*x+D*y*y),4-j)
        mu+=w*value;mu2+=w*value*value;mass+=w
        amax=max(amax,value)
assert mass==a and mu==b and mu2==c and amax==100
actual=1-F(b*b,a*c)
coarse=1-F(b,a)/amax
assert actual==F(55532672116391,829327396387947)
assert coarse==F(41172467,55081050) and actual<coarse
print('PRIOR_FRAMES',{'centered_log':Lc,'chebyshev_log':Lh})
print('ORIGINAL_JET_VARIANCE',{'rows':[(3,1),(4,2)],
     'exact_ratio':str(actual),'ratio':float(actual),'moment_only_upper':str(coarse)})
print('PASS source frame and variance negative-strength controls')
