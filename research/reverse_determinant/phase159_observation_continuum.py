#!/usr/bin/env python3
"""Phase159: original ordinary-jet Gram transport and prime-adic controls.

Exact bounded tests only. Does not prove the proposed 5-billion field bound.
Uses the selected integer-pair order, NOT the half-integral maximal-order basis.
"""
from itertools import combinations
from math import factorial, comb
from sympy import Matrix, diag
from sympy.matrices.normalforms import hermite_normal_form


def pairmul(a, b, D, p=None):
    a0 = a[0]*b[0]-D*a[1]*b[1]
    a1 = a[0]*b[1]+a[1]*b[0]
    if p is not None:
        return a0%p, a1%p
    return a0, a1


def powers(z, n, D, p=None):
    out=[(1,0)]
    for _ in range(n):out.append(pairmul(out[-1],z,D,p))
    return out


def ordinary_effective(Q,D,R,S,p=None):
    """Original row order (r,s), column order (point,j,real/imag).

    Identically zero imaginary columns of real-axis nodes are omitted.
    This retains the exact E diag(2,2D) E^T, not a Hasse-jet replacement.
    """
    cols=[];weights=[];orders=[]
    for x,y in Q:
        zp=powers((x,y),R-1,D,p)
        wp=powers((x,-y),S-1,D,p)
        for j in range(S):
            re=[];im=[]
            for r in range(R):
                for s in range(S):
                    if j>r:a,b=0,0
                    else:
                        a,b=pairmul(zp[r-j],wp[s],D,p)
                        f=factorial(r)//factorial(r-j)
                        a*=f;b*=f
                    if p is not None:a%=p;b%=p
                    re.append(a);im.append(b)
            cols.append(re);weights.append(2);orders.append(j)
            if y!=0:
                cols.append(im);weights.append(2*D);orders.append(j)
    E=[[col[i] for col in cols] for i in range(R*S)]
    return E,weights,orders


def rankmod(E,p):
    A=[[int(v)%p for v in row] for row in E]
    n=len(A);k=0
    for j in range(len(A[0])):
        i=next((i for i in range(k,n) if A[i][j]),None)
        if i is None:continue
        A[i],A[k]=A[k],A[i]
        u=pow(A[k][j],-1,p)
        for i in range(k+1,n):
            c=A[i][j]*u%p
            if c:
                for h in range(j+1,len(A[i])):
                    A[i][h]=(A[i][h]-c*A[k][h])%p
                A[i][j]=0
        k+=1
        if k==n:break
    return k


def polymul(a,b,p):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]=(v[i+j]+x*y)%p
    return v


def annihilator(Q,D,p):
    g=[1]
    for x,y in Q:
        f=[-x%p,1] if y==0 else [(x*x+D*y*y)%p,(-2*x)%p,1]
        g=polymul(g,f,p)
    return g


def obstruction(Q,D,p,S):
    g=annihilator(Q,D,p)
    assert len(g)==p and g[-1]==1
    h=[1]
    for _ in range(S):h=polymul(h,g,p)
    return [[h[k*p-1-j] for j in range(S-1)] for k in range(1,S)]


def determinant_mod(A,p):
    A=[[x%p for x in row] for row in A]
    n=len(A);v=1
    for j in range(n):
        r=next((i for i in range(j,n) if A[i][j]),None)
        if r is None:return 0
        if j!=r:A[j],A[r]=A[r],A[j];v=-v
        piv=A[j][j];v=v*piv%p
        inv=pow(piv,-1,p)
        for i in range(j+1,n):
            f=A[i][j]*inv%p
            if f:
                for k in range(j+1,n):A[i][k]=(A[i][k]-f*A[j][k])%p
                A[i][j]=0
    return v%p


def vq(n,q):
    assert n>0
    v=0
    while n%q==0:n//=q;v+=1
    return v


def vf(j,q):
    n=0
    while j:
        j//=q;n+=j
    return n


def beta(Q,D,R,S,q=2):
    m=R*S
    values=[]
    for x,y in Q:
        for j in range(S):
            values.append(2*vf(j,q)+vq(2,q))
            if y:values.append(2*vf(j,q)+vq(2*D,q))
    assert len(values)>=m
    return sum(sorted(values)[:m])


def source_correspondence():
    # Compare against the separately maintained Phase147 integer evaluator.
    from phase147_prime_adequacy import original_eval
    Q=[(-1,1),(0,0),(2,-1)]
    D,R,S=19,8,4
    raw=original_eval(Q,D)
    E,w,_=ordinary_effective(Q,D,R,S)
    A=Matrix(E)
    indices=[]
    for t,(_,y) in enumerate(Q):
        for j in range(S):
            indices.append(2*S*t+2*j)
            if y!=0:indices.append(2*S*t+2*j+1)
    assert A==raw[:,indices]
    source_weights=[k for _ in Q for _ in range(S) for k in (2,2*D)]
    assert A*diag(*w)*A.T==raw*diag(*source_weights)*raw.T
    print('PHASE159_EXACT_SOURCE_MATCH_PASS',flush=True)


def toy_exact_transport():
    D,R,S=3,2,2
    old=[(0,2)];new=old+[(0,1)]
    results=[]
    for Q in (old,new):
        E,w,_=ordinary_effective(Q,D,R,S)
        A=Matrix(E);G=A*diag(*w)*A.T
        d=abs(int(hermite_normal_form(A).det()))
        h=int(G.det())//(d*d)
        assert h>0 and int(G.det())==d*d*h
        terms=[]
        for I in combinations(range(A.cols),R*S):
            a=int(A[:,list(I)].det())
            if not a:continue
            c=a*a
            for j in I:c*=w[j]
            terms.append(c)
        assert sum(terms)==int(G.det())
        z=min(vq(c,2) for c in terms)
        leading=sum(c//(2**z) for c in terms if vq(c,2)==z)%2
        results.append((G,d,h,z,vq(int(G.det()),2),leading))
    G0,d0,h0,z0,v0,l0=results[0]
    G1,d1,h1,z1,v1,l1=results[1]
    assert (int(G0.det()),d0,h0,z0,v0,l0)==(2304,4,144,8,8,1)
    assert (int(G1.det()),d1,h1,z1,v1,l1)==(53280,1,53280,4,5,0)
    assert d0==4*d1 and h0<h1 and int(G0.det())<int(G1.det())
    B,w,_=ordinary_effective([(0,1)],D,R,S)
    assert G1-G0==Matrix(B)*diag(*w)*Matrix(B).T
    assert h0==2**4*D**2
    toy=Matrix([[1,0,1],[0,2,1]])
    assert toy[:,[0,2]].det()%2==1 and all(v%2==0 for v in [2,2,2])
    print('PHASE159_TOY',{'det_old':2304,'det_new':53280,
       'index_old':4,'index_new':1,'residual_old':144,'residual_new':53280,
       'tropical_v2_floor_new':4,'actual_v2_new':5,'leading_sum_mod2':0},flush=True)


def finite_deletion_controls():
    for D,p,S,Q,wanted in (
        (1,7,3,[(0,0),(0,1),(0,2),(2,2)],(18,17)),
        (3,11,3,[(-5,0),(-4,1),(-3,1),(-2,1),(-1,1),(3,2)],(30,29))):
        R=p-1;rho=3 if p==7 else 5
        assert D>0 and pow((-D)%p,(p-1)//2,p)==p-1
        assert all(x*x+D*y*y<=rho*rho for x,y in Q) and 2*rho<p
        roots=[(x%p,y%p) for x,y in Q]+[(x%p,(-y)%p) for x,y in Q if y]
        assert len(roots)==len(set(roots))==p
        assert len([q for q in Q if q[1]==0])==1
        Qm=[q for q in Q if q[1]!=0]
        er=rankmod(ordinary_effective(Q,D,R,S,p)[0],p)
        em=rankmod(ordinary_effective(Qm,D,R,S,p)[0],p)
        O=obstruction(Qm,D,p,S)
        assert (er,em)==wanted and determinant_mod(O,p)==0
        print('PHASE159_ROOT_DELETION_COUNTERWORLD',{
          'D':D,'p':p,'S':S,'rho':rho,'ranks':(er,em),
          'obstruction':O},flush=True)


def real_axis_witnesses():
    for p in (5,7,11,31):
        for S in range(2,min(p,6)):
            Q=[(x,0) for x in range(1,p)]
            O=obstruction(Q,1,p,S)
            expect=[[((-1)**(S-k)*comb(S,k))%p if j==k-1 else 0
                  for j in range(S-1)] for k in range(1,S)]
            assert O==expect and determinant_mod(O,p)!=0
    assert determinant_mod(obstruction([(x,0) for x in range(1,31)],163,31,5),31)==20
    print('PHASE159_MULTIPLICATIVE_GROUP_WITNESS_PASS',flush=True)


def d163_supports():
    D,p,R,S=163,31,30,5
    full=[(x,0) for x in range(-13,14)]+[(x,1) for x in range(-2,3)]
    re=sorted([q for q in full if q[1]==0],key=lambda q:(abs(q[0]),q[0]))[:21]
    nonreal=sorted([q for q in full if q[1]],key=lambda q:(q[0]*q[0]+D,abs(q[0]),q[0]))
    selected=re+nonreal
    assert len(selected)==26 and len(re)+2*len(nonreal)==31
    assert beta(full,D,R,S)==310 and beta(selected,D,R,S)==430
    dets=[]
    for a in re:
        q=[z for z in selected if z!=a]
        assert len(q)==25 and beta(q,D,R,S)==450
        d=determinant_mod(obstruction(q,D,p,S),p)
        assert d!=0
        dets.append((a[0],d))
    assert dets[0]==(0,3) and dets[-1]==(10,29)
    assert rankmod(ordinary_effective(selected,D,R,S,p)[0],p)==R*S
    for a,d in (dets[0],dets[-1]):
        q=[z for z in selected if z!=(a,0)]
        assert rankmod(ordinary_effective(q,D,R,S,p)[0],p)==R*S
    print('PHASE159_D163_ALL_REAL_DELETIONS_PASS',{
        'candidate_deletions':len(dets),'obstruction_determinants':dets,
        'beta_full':310,'beta_p':430,'beta_p_minus_one':450},flush=True)


def main():
    source_correspondence()
    toy_exact_transport()
    finite_deletion_controls()
    real_axis_witnesses()
    d163_supports()
    print('PHASE159_GRAM_CONTINUUM_PASS: finite source-model evidence only',flush=True)


if __name__=='__main__':main()
