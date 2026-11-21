#!/usr/bin/env python3
"""Exact source-Gram mod-p radical vs full-rank evaluation, and frame controls.

Reconstructs the D=3, rho=2, R=S=J=2 original ordinary-Z-jet
integer trace Gram directly from integer-pair samples. This is a finite
counterworld, not a counterexample to the large-D class-number-one theorem.
"""
from itertools import product

D=3

def mat_mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def tr(a):return [list(x) for x in zip(*a)]

def rank_mod_p(a,p):
    m=[[(v%p) for v in row] for row in a]
    rows=len(m); cols=len(m[0]); r=0
    for c in range(cols):
        pivot=next((i for i in range(r,rows) if m[i][c]), None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r]
        inv=pow(m[r][c],-1,p)
        m[r]=[(v*inv)%p for v in m[r]]
        for i in range(rows):
            if i!=r:
                mult=m[i][c]
                m[i]=[(m[i][j]-mult*m[r][j])%p for j in range(cols)]
        r+=1
        if r==rows:break
    return r

def determinant(a):
    # integer Bareiss; small dimensions
    m=[list(map(int,row)) for row in a]
    n=len(m)
    if n==1:return m[0][0]
    sign=1; prev=1
    for k in range(n-1):
        piv=next((i for i in range(k,n) if m[i][k]),None)
        if piv is None:return 0
        if piv!=k:m[piv],m[k]=m[k],m[piv];sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=m[i][j]*pivot-m[i][k]*m[k][j]
                assert num%prev==0
                m[i][j]=num//prev
            m[i][k]=0
        prev=pivot
    return sign*m[-1][-1]

def int_gaussian_mul(a,b):
    a0,a1=a;b0,b1=b
    return a0*b0-D*a1*b1, a0*b1+a1*b0

def gaussian_pow(z,n):
    result=(1,0)
    for _ in range(n):result=int_gaussian_mul(result,z)
    return result

def ordinary_z_jet(z,r,s,j):
    if j>r:return (0,0)
    fall=1
    for k in range(j):fall*=r-k
    zterm=gaussian_pow(z,r-j)
    wterm=gaussian_pow((z[0],-z[1]),s)
    a,b=int_gaussian_mul(zterm,wterm)
    return fall*a,fall*b

def original_gram():
    points=[(x,y) for x in range(-2,3) for y in range(-1,2) if x*x+D*y*y<=4]
    assert len(points)==11
    rows=[(r,s) for r in range(2) for s in range(2)]
    e=[[] for _ in rows]
    diag=[]
    for j in range(2):
        for z in points:
            vals=[ordinary_z_jet(z,*rs,j) for rs in rows]
            for k,coord in enumerate((0,1)):
                diag.append(2 if coord==0 else 2*D)
                for i in range(len(rows)):
                    e[i].append(vals[i][coord])
    assert len(e)==4 and len(e[0])==44 and len(diag)==44
    weighted=[[v*w for v,w in zip(row,diag)] for row in e]
    g=mat_mul(weighted,tr(e))
    return points,e,diag,g

def tests():
    points,e,diag,g=original_gram()
    known=[[22,0,0,64],[0,64,-8,0],[0,-8,86,0],[64,0,0,296]]
    assert g==known, (g,known)
    assert determinant(g)==13143040
    assert rank_mod_p(e,5)==4
    assert rank_mod_p(g,5)==3
    # A full row-rank evaluation over a finite field may span an isotropic line.
    assert rank_mod_p([[1,2]],5)==1
    assert (1*1+2*2)%5==0
    # Unimodular integral row-frame transform preserves exact determinant.
    u=[[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    e2=mat_mul(u,e)
    g2=mat_mul(mat_mul(u,g),tr(u))
    assert mat_mul([[v*w for v,w in zip(row,diag)] for row in e2],tr(e2))==g2
    assert determinant(u)==1
    assert determinant(g2)==determinant(g)
    assert rank_mod_p(g2,5)==rank_mod_p(g,5)==3
    # A projection of observation columns is not an invertible frame change.
    eproj=[row[:2] for row in e]
    assert rank_mod_p(eproj,5)<4
    print('PASS: original Q has',len(points),'points; 44 weighted integer observation channels')
    print('Exact Gram determinant:',determinant(g))
    print('Mod 5: evaluation row rank=',rank_mod_p(e,5),'Gram rank=',rank_mod_p(g,5))
    print('Unimodular frame invariant: determinant and mod-5 radical dimension preserved')

if __name__=='__main__':tests()
