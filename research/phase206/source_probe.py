#!/usr/bin/env python3
"""Phase206 original-jet pilot. PREREG Issues #142-144 BEFORE execution.

Not a class-number-one field test. Same D283 source for A and B;
D403 is a DIFFERENT source and analytic-only stress test.
"""
from functools import lru_cache
from fractions import Fraction as F
from math import factorial, isqrt, log

def params(D):
    assert D>0 and D%4==3 and all(D%(p*p) for p in range(2,isqrt(D)+1))
    rho=0
    while 25**4*rho**4<11**4*D**3:rho+=1
    R=D//4;S=J=R//25
    Q=[]
    for y in range(-isqrt(rho*rho//D),isqrt(rho*rho//D)+1):
        t=isqrt(rho*rho-D*y*y)
        Q.extend((x,y) for x in range(-t,t+1))
    return rho,R,S,J,Q

def mul(v,w,D,mod=None):
    a,b=v;c,d=w
    x=a*c-D*b*d;y=a*d+b*c
    return (x,y) if mod is None else (x%mod,y%mod)

def fall(r,j):
    return factorial(r)//factorial(r-j) if j<=r else 0

def det(A):
    A=[row[:] for row in A];n=len(A)
    if not n:return 1
    prev=1;sign=1
    for k in range(n-1):
        if not A[k][k]:
            t=next((i for i in range(k+1,n) if A[i][k]),None)
            if t is None:return 0
            A[k],A[t]=A[t],A[k];sign=-sign
        q=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=A[i][j]*q-A[i][k]*A[k][j]
                assert t%prev==0
                A[i][j]=t//prev
            A[i][k]=0
        prev=q
    return sign*A[-1][-1]

def mm(A,B):
    T=list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) for col in T] for row in A]
def tr(A):return [list(row) for row in zip(*A)]
def inv(A):
    n=len(A)
    A=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)]
       for i,row in enumerate(A)]
    for j in range(n):
        t=next(i for i in range(j,n) if A[i][j])
        A[t],A[j]=A[j],A[t]
        q=A[j][j];A[j]=[x/q for x in A[j]]
        for i in range(n):
            if i!=j and A[i][j]:
                q=A[i][j];A[i]=[x-q*y for x,y in zip(A[i],A[j])]
    return [row[n:] for row in A]

def gram(D,Q,J,labels):
    @lru_cache(None)
    def powpair(z,k):
        if k==0:return (1,0)
        if k%2==0:
            x=powpair(z,k//2);return mul(x,x,D)
        return mul(powpair(z,k-1),z,D)
    E=[]
    for r,s in labels:
        line=[]
        for j in range(J):
            for z in Q:
                if j>r:line.extend((0,0));continue
                x,y=mul(powpair(z,r-j),powpair((z[0],-z[1]),s),D)
                f=fall(r,j);line.extend((f*x,f*y))
        E.append(line)
    weights=[w for _j in range(J) for _z in Q for w in (2,2*D)]
    G=[[sum(a*b*w for a,b,w in zip(v,u,weights)) for u in E] for v in E]
    @lru_cache(None)
    def moment(a,b):
        return sum(mul(powpair(z,a),powpair((z[0],-z[1]),b),D)[0] for z in Q)
    H=[[2*sum(fall(r,j)*fall(t,j)*moment(r-j+u,s+t-j)
              for j in range(min(J,r+1,t+1))) for t,u in labels]
       for r,s in labels]
    assert G==H and all(G[i][j]==G[j][i] for i in range(len(G)) for j in range(len(G)))
    return G

def fibers(R,S,d):
    return [(r,s) for r in range(R) for s in range(S) if r-s==d]

def pair_data(D,Q,R,S,J,d):
    I=fibers(R,S,d);K=fibers(R,S,d+2)
    X=gram(D,Q,J,I+K);a=len(I);b=len(K)
    A=[row[:a] for row in X[:a]]
    B=[row[a:] for row in X[a:]]
    C=[row[a:] for row in X[:a]]
    da,db,dj=det(A),det(B),det(X)
    assert 0<dj<=da*db
    return (a,b),A,B,C,log(da)+log(db)-log(dj)

def analytic(D):
    rho,R,S,J,Q=params(D)
    assert (-D)%3==2 and (-D)%5 in (2,3)
    ds=(R//4-1,R//2-1,R-S-7)
    tau=F(0);total=0.
    for d in ds:
        (a,b),A,B,C,gain=pair_data(D,Q,R,S,J,d)
        T=mm(mm(mm(inv(A),C),inv(B)),tr(C))
        t=sum(T[i][i] for i in range(a))
        assert 0<=t<=min(a,b) and float(t)<=gain+1e-7
        tau+=t;total+=gain
        print('THREE_PAIR',D,d,d+2,(a,b),float(t),gain,flush=True)
        assert gram(D,Q,J, fibers(R,S,d)+fibers(R,S,d+2)) != (
            gram(D,Q,1, fibers(R,S,d)+fibers(R,S,d+2)))
    I=fibers(R,S,ds[0]);K=fibers(R,S,ds[0]+1)
    X=gram(D,Q,J,I+K)
    assert all(X[i][len(I)+j]==0 for i in range(len(I)) for j in range(len(K)))
    assert tau<=F(R*S,2)
    print('THREE_SUM',dict(D=D,rho=rho,R=R,S=S,Q=len(Q),
       tau=float(tau),gain=total,tau_normalized=float(tau)/(R*R*S),
       gain_normalized=total/(R*R*S),parity_control=True),flush=True)

def rank_mod(A,p):
    pivots={}
    for raw in A:
        row=[x%p for x in raw]
        for k,v in pivots.items():
            t=row[k]
            if t:
                for j in range(k,len(row)):row[j]=(row[j]-t*v[j])%p
        k=next((j for j,x in enumerate(row) if x),None)
        if k is not None:
            q=pow(row[k],-1,p)
            for j in range(k,len(row)):row[j]=row[j]*q%p
            pivots[k]=row
    return len(pivots)

def eval_mod(D,Q,R,S,J,p,K):
    mod=p**K;n=R*S
    E=[[0]*(2*J*len(Q)) for _ in range(n)]
    assert S==2
    for qi,(x,y) in enumerate(Q):
        z=(x%mod,y%mod);w=(x%mod,(-y)%mod)
        powers=[(1,0)]
        for r in range(R):powers.append(mul(powers[-1],z,D,mod))
        for j in range(J):
            col=2*(j*len(Q)+qi)
            for r in range(j,R):
                f=fall(r,j)
                a,b=powers[r-j]
                E[2*r][col]=f*a%mod;E[2*r][col+1]=f*b%mod
                a,b=mul(powers[r-j],w,D,mod)
                E[2*r+1][col]=f*a%mod;E[2*r+1][col+1]=f*b%mod
    return E

def old_frobenius_C0(E,R,S,p,K):
    assert S==2
    mod=p**K;low=p**(K-1);C=[]
    for r in range(R):
        for s in range(S):
            row=E[2*r+s]
            if s==0 and r>=p:
                b=E[2*(r-p)+1]
                v=[(x-y)%mod for x,y in zip(row,b)]
                assert all(x%p==0 for x in v)
                C.append([x//p for x in v])
            else:C.append([x%low for x in row])
    return C

def gram_mod(C,D,mod):
    n=len(C);m=len(C[0])
    W=[2 if j%2==0 else 2*D for j in range(m)]
    H=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(i,n):
            v=sum(x*y*w for x,y,w in zip(C[i],C[k],W))%mod
            H[i][k]=H[k][i]=v
    return H

def arithmetic():
    D=283;rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(31,70,2,2,169)
    for p in (3,5):
        assert (-D)%p not in {k*k%p for k in range(p)}
        E=eval_mod(D,Q,R,S,J,p,4)
        C=old_frobenius_C0(E,R,S,p,4)
        er=rank_mod(E,p);cr=rank_mod(C,p)
        H=gram_mod(C,D,p)
        hr=rank_mod(H,p)
        n=R*S
        assert cr<n
        print('FIRST_LOCAL',dict(p=p,D=D,n=n,m=len(E[0]),
             inherited_F=R-p,inherited_exponent=2*(R-p),
             rank_E=er,rank_C0=cr,rank_H0=hr,
             extra_eval_index_at_least=n-cr,
             uncounted_gram_exponent_at_least=2*(n-cr),
             H0_not_yet_primitive=True),flush=True)
    # Wrong inertness witness: D=287,p3 is split. (1+u)^3-(1-u)=2u.
    z=(1,1);z3=mul(mul(z,z,287,3),z,287,3)
    assert ((z3[0]-1)%3,(z3[1]+1)%3)==(0,2)
    print('NONINERT_NEGATIVE',287,3,(0,2),flush=True)

if __name__=='__main__':
    analytic(283)
    arithmetic()
    analytic(403)
    print('PASS Phase206 exact original-source pilot, NOT a field theorem')
