#!/usr/bin/env python3
"""Preregistered #137: seven anchors mod49 vs all points in residue tubes."""
from math import gcd
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase203"))
from check_intertwiner_f7 import U_at
m=49;n=14
H=[[pow(a,r,m) if j==0 else (r*pow(a,r-1,m)%m if r else 0)
    for r in range(n)] for a in range(7) for j in (0,1)]
O=[[0]*n for _ in range(n)]
for a in range(7):O[2*a][2*a+1]=1;O[2*a+1][2*a]=-1
I=[[int(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):
    C=list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col))%m for col in C] for row in A]
def inverse(A):
    A=[row[:]+I[i] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if gcd(A[i][j],m)==1)
        A[j],A[k]=A[k],A[j]
        t=pow(A[j][j],-1,m);A[j]=[x*t%m for x in A[j]]
        for i in range(n):
            if i!=j:
                t=A[i][j]
                A[i]=[(x-t*y)%m for x,y in zip(A[i],A[j])]
    assert [row[:n] for row in A]==I
    return [row[n:] for row in A]
U=mm(mm(inverse(H),O),H)
assert mm(U,U)==[[-x%m for x in row] for row in I]
assert [[x%7 for x in row] for row in U]==U_at(7)
for k in range(n):
    c=[U[r][k] for r in range(n)]
    for a in range(7):
        v=sum(x*pow(a,r,m) for r,x in enumerate(c))%m
        d=sum(r*x*pow(a,r-1,m) for r,x in enumerate(c) if r)%m
        assert v==(k*pow(a,k-1,m)%m if k else 0)
        assert d==-pow(a,k,m)%m
h=[U[r][0] for r in range(n)]
v=lambda z:sum(x*pow(z,r,m) for r,x in enumerate(h))%m
assert v(0)==0 and U[1][0]==48 and v(7)==42
assert 31*31%49==(-215)%49
print("ANCHORS",{"modulus":49,"points":7,"U_squared":"-I",
                  "reduces_to_original_U7":True})
print("TUBE_NO_GO",{"zero":v(0),"shifted_7":v(7),
                     "derivative_at_zero":U[1][0]})
print("PASS Phase204-B anchored lift vs full tube obstruction")
