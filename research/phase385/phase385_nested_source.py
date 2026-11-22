#!/usr/bin/env python3
"""Independent binomial reconstruction of the original ordinary-jet Gram.
Finite exact witness, not a proof of uniform large-D determinant bounds.
Requires sympy.
"""
from math import comb, factorial
import sympy as sp

R,S,J=7,3,3

def samples(D,rho):
    return [(x,y) for x in range(-rho,rho+1) for y in range(-rho,rho+1)
            if x*x+D*y*y<=rho*rho]

def jet(D,r,s,j,x,y):
    if j>r:return (0,0)
    z=[0,0]
    for h in range(r-j+1):
        for t in range(s+1):
            v=h+t
            coeff=(comb(r-j,h)*comb(s,t)*(-1)**t*
                   x**(r-j-h+s-t)*y**v*(-D)**(v//2))
            z[v%2]+=coeff
    return tuple(v*(factorial(r)//factorial(r-j)) for v in z)

def rank_mod(M,p):
    A=[[int(M[i,j])%p for j in range(M.cols)] for i in range(M.rows)]
    rank=0
    for col in range(M.cols):
        piv=next((i for i in range(rank,len(A)) if A[i][col]),None)
        if piv is None:continue
        A[rank],A[piv]=A[piv],A[rank]
        inv=pow(A[rank][col],-1,p)
        A[rank]=[(v*inv)%p for v in A[rank]]
        for i in range(len(A)):
            if i!=rank and A[i][col]:
                c=A[i][col];A[i]=[(u-c*v)%p for u,v in zip(A[i],A[rank])]
        rank+=1
        if rank==len(A):break
    return rank

def vp(n,p):
    n=abs(int(n));assert n>0
    k=0
    while n%p==0:n//=p;k+=1
    return k

def form(D,p,rho):
    Q=samples(D,rho);n=R*S
    E=sp.zeros(n,2*J*len(Q))
    rows=[(r,s) for r in range(R) for s in range(S)]
    for i,(r,s) in enumerate(rows):
        for j in range(J):
            for a,(x,y) in enumerate(Q):
                E[i,2*(j*len(Q)+a)]=jet(D,r,s,j,x,y)[0]
                E[i,2*(j*len(Q)+a)+1]=jet(D,r,s,j,x,y)[1]
    U=sp.eye(n)
    exps=[]
    for i,(r,s) in enumerate(rows):
        k=min(r//p,S-1-s);exps.append(k)
        for t in range(1,k+1):
            U[i,(r-p*t)*S+s+t]+=(-1)**t*comb(k,t)
    assert U.det()==1
    F=U*E
    integral=True
    for i,k in enumerate(exps):
        for col in range(F.cols):
            if int(F[i,col])%p**k:
                integral=False
            else:
                F[i,col]=int(F[i,col])//p**k
    if not integral:return {'integral':False,'D':D,'p':p,'rho':rho,'Fsum':sum(exps)}
    Bweights=[2 if col%2==0 else 2*D for col in range(E.cols)]
    Ew=E.copy();Fw=F.copy()
    for col,w in enumerate(Bweights):
        Ew[:,col]*=w;Fw[:,col]*=w
    G=Ew*E.T
    H=Fw*F.T
    dg=int(G.det(method='domain-ge'))
    dh=int(H.det(method='domain-ge'))
    assert dg>0 and dh>0
    assert dg==p**(2*sum(exps))*dh
    assert dg==int(G.det(method='bareiss'))
    return {'integral':True,'Q':Q,'H':H,'det':dg,'extra':vp(dh,p),
            'total':vp(dg,p),'rank_H':rank_mod(H,p),'rank_F':rank_mod(F,p),
            'Fsum':sum(exps),'D':D,'p':p,'rho':rho}

def main():
    cases=[form(43,3,r) for r in (8,9,10,12)]
    expected=[(8,35,32,14,8),(9,45,18,0,21),(10,51,19,1,20),(12,67,18,0,21)]
    for c,(rho,nq,total,extra,rh) in zip(cases,expected):
        assert c['integral'] and (c['rho'],len(c['Q']),c['total'],c['extra'],c['rank_H'])==(rho,nq,total,extra,rh)
        assert c['rank_F']==21 and c['Fsum']==9
        print('rho',rho,'points',nq,'v3(det G)',total,'extra',extra,'rank mod 3',rh)
    assert set(cases[0]['Q']).issubset(cases[1]['Q'])
    assert cases[0]['det']<cases[1]['det']
    assert form(19,5,9)['integral'] is False # split prime: Frobenius premise absent
    assert all(x in samples(43,8) for x in ((0,0),(3,0),(6,0)))
    assert [((jet(43,3,0,0,x,0)[0]-x)//3)%3 for x in (0,3,6)]==[0,2,1]
    # Ordinary derivative at j=p is p!, Hasse coefficient is 1.
    assert jet(43,3,0,3,0,0)==(6,0) and 6%3==0 and 1%3!=0
    print('PASS source-binomial jets, normalized Gram residual and hostile controls')

if __name__=='__main__':main()
