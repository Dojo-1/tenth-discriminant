#!/usr/bin/env python3
"""E38 independent exact-integer oracle for the ORIGINAL ordinary-jet Gram.

Frozen bounded grid: p=2,3,5; a=-2,0,3; R=2,3,4; J=1,2,3;
D=25, S=1, original real samples Q={(a+p*t,0): t=0..R-1}.
No interpolation, Gram or source replacement. No external packages.
This is a bounded M-level reproduction, NOT a Lean/field theorem.
"""
from math import comb, factorial
from collections import Counter
import json

def pair_mul(D, x, y):
    return (x[0]*y[0]-D*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def pair_pow(D, x, r):
    o = (1,0)
    for _ in range(r):
        o = pair_mul(D,o,x)
    return o

def original_jet(D,r,s,j,q):
    if j>r: return (0,0)
    c=factorial(r)//factorial(r-j)
    z=pair_mul(D,pair_pow(D,q,r-j),pair_pow(D,(q[0],-q[1]),s))
    return (c*z[0],c*z[1])

def original_trace(D,x,y):
    return 2*(x[0]*y[0]+D*x[1]*y[1])

def original_gram(Q,D,J,R,S=1):
    rows=[(r,s) for r in range(R) for s in range(S)]
    return [[sum(original_trace(D,original_jet(D,r,s,j,q),
                                 original_jet(D,t,u,j,q))
                 for j in range(J) for q in Q)
             for t,u in rows] for r,s in rows]

def matmul(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def transpose(A):
    return list(map(list,zip(*A)))

def det(A):
    if not A: return 1
    A=[row[:] for row in A]
    sign,denom=1,1
    n=len(A)
    for k in range(n-1):
        if A[k][k]==0:
            ix=next((i for i in range(k+1,n) if A[i][k]),None)
            if ix is None:return 0
            A[k],A[ix]=A[ix],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%denom==0
                A[i][j]=num//denom
        for i in range(k+1,n):A[i][k]=0
        denom=pivot
    return sign*A[-1][-1]

def vp(n,p):
    if n==0:return None
    n=abs(n)
    c=0
    while n%p==0:
        c+=1
        n//=p
    return c

def shift_frame(a,R):
    return [[comb(r,k)*(-a)**(r-k) if k<=r else 0
             for k in range(R)] for r in range(R)]

def examine(p,a,R,J):
    D=25
    Q=[(a+p*t,0) for t in range(R)]
    G=original_gram(Q,D,J,R)
    U=shift_frame(a,R)
    assert det(U)==1 and det(G)>0
    shifted=matmul(matmul(U,G),transpose(U))
    assert det(shifted)==det(G)
    rows=[[original_jet(D,r,0,j,q) for j in range(J) for q in Q]
          for r in range(R)]
    exponents=[max(0,r-J+1) for r in range(R)]
    for r,e in enumerate(exponents):
        for c in range(J*len(Q)):
            witness=[sum(U[r][k]*rows[k][c][b] for k in range(R))
                     for b in (0,1)]
            assert all(x%(p**e)==0 for x in witness)
    lower=2*sum(exponents)
    actual=vp(det(G),p)
    assert actual is not None and actual>=lower
    if J==1:
        formula=2**R*p**(R*(R-1))
        for k in range(1,R):formula*=factorial(k)**2
        assert det(G)==formula
    return (p,a,R,J,lower,actual,det(G))

def main():
    cases=[examine(p,a,R,J) for p in (2,3,5)
           for a in (-2,0,3) for R in (2,3,4)
           for J in (1,2,3)]
    assert len(cases)==81
    Qunit=[(0,0),(1,0)]
    Qshift=[(1,0),(6,0)]
    U=[[1,0],[-1,1]]
    V=[[1,0],[0,5]]
    terminal=[[4,10],[10,50]]
    assert matmul(matmul(U,original_gram(Qshift,25,1,2)),transpose(U))==terminal
    assert matmul(matmul(V,original_gram(Qunit,25,1,2)),transpose(V))==terminal
    assert (det(U),det(V))==(1,5)
    assert (det(original_gram(Qshift,25,1,2)),
            det(original_gram(Qunit,25,1,2)))==(100,4)
    q1=examine(5,1,3,1)
    q2=examine(5,1,3,2)
    assert (q1[4],q1[5],q1[6])==(6,6,500000)
    assert (q2[4],q2[5],q2[6])==(2,2,784400)
    print(json.dumps({
      "cases":len(cases),"primes":[2,3,5],"translations":[-2,0,3],
      "row_counts":[2,3,4],"derivative_depths":[1,2,3],
      "slack_histogram":dict(Counter(v-lower for *_,lower,v,detG in cases)),
      "clock_example":{"same_Q":Qshift+[(11,0)],
                       "J1":{"lower":q1[4],"v5":q1[5],"det":q1[6]},
                       "J2":{"lower":q2[4],"v5":q2[5],"det":q2[6]}},
      "matched_invalid_transport":{"detU":1,"detV":5,
                     "original_determinants":[100,4],
                     "equal_terminal":terminal},
      "status":"exact bounded arithmetic; no field, complexity or asymptotic claim"
    },indent=2))

if __name__=="__main__":main()
