#!/usr/bin/env python3
"""Phase204-A. Exact ordinary-Z jet factorial filtration; prereg #136."""
from math import factorial as fac, comb

def mul(a,b,D):
    return a[0]*b[0]-D*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def powpair(a,n,D):
    q=(1,0)
    for _ in range(n):q=mul(q,a,D)
    return q
def jet(D,r,s,j,z):
    if j>r:return (0,0)
    f=fac(r)//fac(r-j)
    a,b=mul(powpair(z,r-j,D),powpair((z[0],-z[1]),s,D),D)
    assert f==fac(j)*comb(r,j)
    return f*a,f*b
def gramstep(Q,D,R,S,j):
    A=[[jet(D,r,s,j,z) for z in Q] for r in range(R) for s in range(S)]
    return [[sum(2*(x[0]*y[0]+D*x[1]*y[1]) for x,y in zip(u,v))
             for v in A] for u in A]
def val(n,p):
    v=0
    while n and n%p==0:n//=p;v+=1
    return v
def check(p,D):
    R,S,J=p+2,2,p+2;Q=[(0,0),(1,0),(1,1)]
    n=R*S;tail=[[0]*n for _ in range(n)]
    for j in range(J):
        step=gramstep(Q,D,R,S,j);denom=2*fac(j)**2
        assert all(x%denom==0 for row in step for x in row)
        if j>=p:
            for i in range(n):
                for k in range(n):tail[i][k]+=step[i][k]
    assert any(x for row in tail for x in row)
    assert all(x%(p*p)==0 for row in tail for x in row)
    sharp=gramstep([(0,0)],D,R,1,p)[p][p]
    assert sharp==2*fac(p)**2 and val(sharp,p)==2
    assert sharp%(p**3)!=0
    assert 2*comb(p,p)**2%(p*p)!=0  # Hasse / divided derivative fails
    print("ODD",dict(p=p,D=D,source_rows=n,samples=len(Q),
          sharp=sharp,vp=val(sharp,p),nonzero_tail=sum(bool(x) for row in tail for x in row),
          nonzero_mod_p3=sum(bool(x%(p**3)) for row in tail for x in row)))
def check2():
    a=gramstep([(0,0)],3,4,1,2)[2][2]
    assert a==8 and val(a,2)==3
    for j in (2,3,4):
        assert all(x%(2*fac(j)**2)==0 for row in gramstep([(0,0),(1,0)],3,5,2,j) for x in row)
    print("BINARY",dict(j2=a,v2=val(a,2)))
if __name__=="__main__":
    check(3,7);check(5,3);check2()
    print("PASS source integer ordinary jets; sharp filtration, wrong-Hasse control")
