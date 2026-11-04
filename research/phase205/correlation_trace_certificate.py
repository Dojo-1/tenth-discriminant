#!/usr/bin/env python3
"""Phase205-B: exact rational trace-correlation lower bound, issue #140.
Source is the frozen original Gram; no whole-Gram determinant enters tau.
"""
from fractions import Fraction as F
from math import log
from source_spectral_pilot import G, fib, part, determinant, R, S

def trans(A): return [list(row) for row in zip(*A)]
def mul(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def inverse(A):
    n=len(A);a=[[F(v) for v in row]+[F(int(i==j)) for j in range(n)]
                 for i,row in enumerate(A)]
    for j in range(n):
        i=next(i for i in range(j,n) if a[i][j])
        a[j],a[i]=a[i],a[j]
        q=a[j][j];a[j]=[x/q for x in a[j]]
        for i in range(n):
            if i!=j:
                q=a[i][j]
                if q:a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]
def block(I,K):return [[G[i][j] for j in K] for i in I]
def trace_coupling(I,K):
    A=block(I,I);B=block(K,K);C=block(I,K)
    P=mul(mul(mul(inverse(A),C),inverse(B)),trans(C))
    return sum(P[i][i] for i in range(len(I)))
def detprincipal(I):return determinant(block(I,I))

total=F(0);observed=0.0
for pair in part:
    if len(pair)==1:continue
    I=fib[pair[0]];K=fib[pair[1]]
    t=trace_coupling(I,K)
    gain=log(detprincipal(I))+log(detprincipal(K))-log(detprincipal(I+K))
    assert t>0 and float(t)<=gain+1e-12
    total+=t;observed+=gain
    print('CORRELATION',pair,'rational_trace',t,'trace',float(t),'actual_gain',gain)
assert trace_coupling(fib[-2],fib[-1])==0  # existing parity separation
assert abs(float(total)-1.1779427590761873)<1e-10
assert abs(observed-1.2877720967917412)<1e-10
assert 0.0043<float(total)/(R*R*S)<observed/(R*R*S)
print('TRACE_SANDWICH',{'lower':float(total),'actual':observed,
      'normalized_lower':float(total)/(R*R*S),
      'normalized_actual':observed/(R*R*S),
      'parity_negative':0})
print('PASS exact rational fixed-source correlation trace lower certificate')
