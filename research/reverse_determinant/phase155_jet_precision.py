#!/usr/bin/env python3
"""Phase155: exact ordinary-jet precision and Frobenius fat-point descent.

All finite tests run over F_p or F_(p^2). They do not establish a new
class-number-one field bound. Same original derivative and row order.
"""
from math import comb, factorial
from phase152_frobenius_graph import eval_rows as source_eval, rank_det_mod
from phase147_prime_adequacy import original_eval as source_integer_eval

def add(a,b,p): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def mul(a,b,D,p):
    return ((a[0]*b[0]-D*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def scale(a,n,p): return (a[0]*n%p,a[1]*n%p)
def power(a,n,D,p):
    v=(1,0)
    for _ in range(n): v=mul(v,a,D,p)
    return v
def falling(r,j):
    f=1
    for i in range(j): f*=r-i
    return f

def partial_coefficient(a,D,p,r,s,j):
    if j>r: return (0,0)
    w=(a[0],-a[1]%p)
    return scale(mul(power(a,r-j,D,p),power(w,s,D,p),D,p),comb(r,j),p)

def source_ordinary(a,D,p,r,s,j):
    return scale(partial_coefficient(a,D,p,r,s,j),factorial(j),p)

def graph_coefficient(a,D,p,r,s,j):
    """Coefficient h^j of (a+h)^r (a^p+h^p)^s, not a partial-Z jet."""
    ap=power(a,p,D,p)
    v=(0,0)
    for k in range(min(s,j//p)+1):
        u=j-p*k
        if u>r: continue
        w=mul(power(a,r-u,D,p),power(ap,s-k,D,p),D,p)
        v=add(v,scale(w,comb(r,u)*comb(s,k),p),p)
    return v

def poly_mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]=(c[i+j]+x*y)%p
    return c

def annihilator(Q,D,p):
    g=[1]
    for x,y in Q:
        factor=[-x%p,1] if y==0 else [(x*x+D*y*y)%p,-2*x%p,1]
        g=poly_mul(g,factor,p)
    assert g[-1]==1
    return g

def monomial_remainders(f,upto,p):
    n=len(f)-1
    out=[]
    for e in range(upto+1):
        if e<n: v=[int(j==e) for j in range(n)]
        else:
            old=out[-1]
            v=[0]+old[:-1]
            top=old[-1]
            if top:
                for j in range(n): v[j]=(v[j]-top*f[j])%p
        out.append(v)
    return out

def quotient_rank(Q,D,p,R,S):
    """Independent polynomial-quotient oracle for the S-th fat-point ideal."""
    g=annihilator(Q,D,p)
    assert len(g)-1==R
    f=[1]
    for _ in range(S): f=poly_mul(f,g,p)
    assert len(f)-1==R*S
    rem=monomial_remainders(f,R-1+p*(S-1),p)
    E=[rem[r+p*s] for r in range(R) for s in range(S)]
    return rank_det_mod(E,p)[0]

def source_match():
    Q=[(-1,1),(0,0),(2,-1)]
    p,D,R,S,J=31,19,8,4,4
    E=source_eval(Q,D,R,S,J,p)
    exact=source_integer_eval(Q,D)
    assert exact.shape==(R*S,2*J*len(Q))
    for row in range(R*S):
        r,s=divmod(row,S)
        for t,(x,y) in enumerate(Q):
            for j in range(J):
                v=source_ordinary((x%p,y%p),D,p,r,s,j)
                for k in range(2):
                    c=2*J*t+2*j+k
                    assert E[row][c]==v[k]==int(exact[row,c])%p
    print("PHASE155_SOURCE_MATCH_PASS",flush=True)

def jet_precision():
    tested=0
    for p,D in ((3,1),(5,2),(7,1),(11,1),(31,163)):
        assert pow(-D%p,(p-1)//2,p)==p-1
        for x,y in ((1,1),(2,3),(-2,1),(0,1)):
            a=(x%p,y%p)
            assert power(a,p,D,p)==(a[0],-a[1]%p)
            for r in range(min(p,11)):
                for s in range(5):
                    for j in range(min(p,9)):
                        u=partial_coefficient(a,D,p,r,s,j)
                        assert u==graph_coefficient(a,D,p,r,s,j)
                        assert source_ordinary(a,D,p,r,s,j)==scale(u,factorial(j),p)
                        tested+=1
        assert graph_coefficient((1,1),D,p,0,1,p)==(1,0)
        assert partial_coefficient((1,1),D,p,0,1,p)==(0,0)
        assert factorial(p)%p==0
    # Split, ramified and characteristic-two reductions are not inert Fp2.
    assert power((1,1),5,1,5)!=(1,-1%5)
    assert power((1,1),3,3,3)!=(1,-1%3)
    assert (-2)%2==0
    print("PHASE155_FROBENIUS_JET_PASS",tested,"cases; j=p boundary killed",flush=True)

def radial_frame_precision():
    """Check differentiation in Z with W constant, independent from frame sum."""
    tests=0
    for p,D in ((5,2),(7,1),(11,1),(31,163)):
        for z in ((1,1),(2,3)):
            z=(z[0]%p,z[1]%p);w=(z[0],-z[1]%p)
            for r in range(7):
                for s in range(4):
                    for j in range(5):
                        for A in (0,1,7):
                            m=min(r,s)
                            # Direct polynomial in Z: Z^(r-m) W^(s-m) (ZW-A)^m
                            c=[(1,0)]
                            for _ in range(r-m): c=poly_fp2_mul(c,[(0,0),(1,0)],D,p)
                            for _ in range(s-m): c=[mul(v,w,D,p) for v in c]
                            for _ in range(m): c=poly_fp2_mul(c,[(-A%p,0),w],D,p)
                            direct=(0,0)
                            for k in range(j,len(c)):
                                v=mul(c[k],power(z,k-j,D,p),D,p)
                                direct=add(direct,scale(v,falling(k,j),p),p)
                            transported=(0,0)
                            for t in range(m+1):
                                v=source_ordinary(z,D,p,r-t,s-t,j)
                                transported=add(transported,scale(v,comb(m,t)*(-A)**t,p),p)
                            assert direct==transported
                            tests+=1
    print("PHASE155_MOVING_FRAME_JETS_PASS",tests,flush=True)

def poly_fp2_mul(a,b,D,p):
    out=[(0,0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=add(out[i+j],mul(x,y,D,p),p)
    return out

def square_channels(Q,D,p,R,S,hasse):
    channels=[]
    for x,y in Q:
        for j in range(S):
            channels.append(((x%p,y%p),j,0))
            if y: channels.append(((x%p,y%p),j,1))
    M=[]
    for r in range(R):
        for s in range(S):
            row=[]
            for z,j,k in channels:
                value=partial_coefficient(z,D,p,r,s,j)
                if not hasse: value=scale(value,factorial(j),p)
                row.append(value[k])
            M.append(row)
    return M

def jet_scheme_and_mass_primes():
    p,D,R,S=31,163,30,5
    Qs=(
      (13,29,[(x,1) for x in range(-2,3)]+[(x,0) for x in range(-10,10)]),
      (14,22,[(x,1) for x in range(-5,6)]+[(x,0) for x in range(-4,4)]),
      (15,22,[(x,1) for x in range(-7,8)]),
    )
    factorial_scale=1
    for j in range(S): factorial_scale=factorial_scale*pow(factorial(j),R,p)%p
    assert factorial_scale==1   # Fermat: R=p-1; NOT an integral equivalence.
    for radius,expected,Q in Qs:
        assert all(x*x+D*y*y<=radius*radius for x,y in Q)
        assert quotient_rank(Q,D,p,R,S)==R*S
        E=square_channels(Q,D,p,R,S,False)
        H=square_channels(Q,D,p,R,S,True)
        assert len(E)==len(E[0])==R*S
        rank,det=rank_det_mod(E,p)
        h_rank,h_det=rank_det_mod(H,p)
        assert rank==h_rank==R*S and det==expected
        assert det==h_det*factorial_scale%p
        print("PHASE155_FAT_POINT",radius,"nodes",len(Q),
              "quotient_rank",rank,"ordinary_det",det,"Hasse_det",h_det,flush=True)
    Q=Qs[-1][2]
    for q,expected in ((2,(8,20)),(3,(18,30)),(5,(50,50))):
        A=square_channels(Q,D,q,R,S,False)
        H=square_channels(Q,D,q,R,S,True)
        ranks=(rank_det_mod(A,q)[0],rank_det_mod(H,q)[0])
        assert ranks==expected
        print("PHASE155_MASS_PRIME",q,"ordinary_Hasse_ranks",ranks,flush=True)
    assert factorial(0)*factorial(1)*factorial(2)*factorial(3)*factorial(4)==288
    assert 288**60==2**300*3**120
    print("PHASE155_GRAM_FACTORIAL_REMAINDER v2=300 v3=120",flush=True)

def sharp_real_root_control():
    # General paper proof: multiplicative Fourier in a in Fp* diagonalizes
    # blocks by r+s mod R; each block is falling-factorial Vandermonde.
    for p in (3,5,7,11,31):
        R=p-1
        for S in sorted({1,2,min(3,R),min(5,R)}):
            if S>R: continue
            E=[]
            for r in range(R):
                for s in range(S):
                    E.append([falling(r,j)*pow(a,r+s-j,p)%p if j<=r else 0
                              for a in range(1,p) for j in range(S)])
            assert rank_det_mod(E,p)[0]==R*S
            for t in range(R):
                rs=[(t-s)%R for s in range(S)]
                disc=1
                for i in range(S):
                    for j in range(i+1,S): disc=disc*(rs[j]-rs[i])%p
                assert disc!=0
    print("PHASE155_SHARP_FOURIER_JETS_PASS (non-production large radius)",flush=True)

if __name__=="__main__":
    source_match()
    jet_precision()
    radial_frame_precision()
    jet_scheme_and_mass_primes()
    sharp_real_root_control()
    print("PHASE155_JET_PRECISION_PASS",flush=True)
