#!/usr/bin/env python3
"""Phase285: finite Noether C2 disk-lens and exact theta moments, original trace metric.

Protocol frozen at 5a4cbee before this code. D19 is a known hand-checkable
toy; D403 operates on the REAL original Q219 and a 16-row PRINCIPAL MINOR
of the original 400-row, four-ordinary-jet integer source. No full 400-row
Smith/Gram determinant, no field bound, no Siegel-zero result.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, isqrt
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE.parents[1] / "phase206"))
sys.path.insert(0, str(HERE.parents[1] / "phase204"))
from source_probe import params
from ordinary_jet_filtration import jet

BLOBS = {
    "research/phase206/source_probe.py": "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase204/ordinary_jet_filtration.py": "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}
PRIMES = (2, 3, 5, 7, 11)


def freeze_original_helpers():
    for path, expected in BLOBS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", "HEAD:" + path], cwd=ROOT, text=True
        ).strip()
        assert actual == expected, ("original source drift", path, actual, expected)


def disk(D, rho):
    assert D > 0 and rho > 0
    ybound = isqrt(rho * rho // D)
    return [(x, y) for y in range(-ybound, ybound + 1)
            for x in range(-isqrt(rho*rho-D*y*y), isqrt(rho*rho-D*y*y)+1)]


def window(Q, D, rho, symmetric):
    bound = rho * rho
    if symmetric:
        return [(x,y) for x,y in Q if (x-1)**2 + D*y*y <= bound
                and (x+1)**2 + D*y*y <= bound]
    return [(x,y) for x,y in Q if (x-1)**2 + D*y*y <= bound]


def pair_mul(D, a, b):
    return (a[0]*b[0] - D*a[1]*b[1], a[0]*b[1] + a[1]*b[0])


@lru_cache(None)
def pair_power(D, z, n):
    assert n >= 0
    if n == 0:
        return (1,0)
    if n % 2 == 0:
        v = pair_power(D,z,n//2)
        return pair_mul(D,v,v)
    return pair_mul(D,pair_power(D,z,n-1),z)


def fall(n,j):
    if n < j:
        return 0
    z = 1
    for k in range(j):
        z *= n-k
    return z


def exact_gram(D,Q,labels,J):
    """Original sign-preserving trace metric 2*(re*re + D*im*im)."""
    n=len(labels)
    G=[[0 for _ in labels] for _ in labels]
    for z in Q:
        for j in range(J):
            v=[jet(D,r,s,j,z) for r,s in labels]
            for i,(a,b) in enumerate(v):
                for k in range(i,n):
                    c,d = v[k]
                    G[i][k] += 2*(a*c+D*b*d)
    for i in range(n):
        for k in range(i):
            G[i][k] = G[k][i]
    return G


def gram_via_moments(D,Q,labels,J):
    """Derivative of finite Theta_Q at tau=xi=eta=0, exact integer algebra."""
    @lru_cache(None)
    def M(a,b):
        assert a>=0 and b>=0
        real=0
        imag=0
        for z in Q:
            zbar=(z[0],-z[1])
            prod=pair_mul(D,pair_power(D,z,a),pair_power(D,zbar,b))
            real+=prod[0]
            imag+=prod[1]
        return real,imag
    n=len(labels)
    G=[[0]*n for _ in range(n)]
    for i,(r,s) in enumerate(labels):
        for k,(rr,ss) in enumerate(labels):
            val=0
            for j in range(min(J,r+1,rr+1)):
                m=M(r-j+ss,s+rr-j)
                val += 2*fall(r,j)*fall(rr,j)*m[0]
            G[i][k]=val
    return G,M


def det_bareiss(A):
    n=len(A)
    if n==0:
        return 1
    v=[row[:] for row in A]
    previous=1
    sign=1
    for k in range(n-1):
        if v[k][k]==0:
            pivot=next((a for a in range(k+1,n) if v[a][k]),None)
            if pivot is None:
                return 0
            v[k],v[pivot]=v[pivot],v[k]
            sign=-sign
        q=v[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=v[i][j]*q-v[i][k]*v[k][j]
                assert num%previous==0, ("Bareiss noninteger", k,i,j)
                v[i][j]=num//previous
            v[i][k]=0
        previous=q
    return sign*v[n-1][n-1]


def v_p(n,p):
    assert n!=0
    n=abs(n)
    c=0
    while n%p==0:
        n//=p
        c+=1
    return c


def parity_indexes(labels):
    even=[i for i,(r,s) in enumerate(labels) if (r+s)%2==0]
    odd=[i for i,(r,s) in enumerate(labels) if (r+s)%2==1]
    return even,odd


def principal(G,idx):
    return [[G[i][j] for j in idx] for i in idx]


def best_pair_certificate(G,labels):
    """Exact 2x2 Hadamard-Fischer correction on this selected submatrix."""
    best=Fraction(0)
    for i,(r,s) in enumerate(labels):
        for j in range(i+1,len(labels)):
            rr,ss=labels[j]
            if (r+s+rr+ss)%2:
                continue
            assert G[i][i]>0 and G[j][j]>0
            c=Fraction(G[i][j]**2,G[i][i]*G[j][j])
            assert 0<=c<1
            best=max(best,c)
    return best


def inspect_gram(D,Q,labels,J,expected_v,require_symmetric):
    G=exact_gram(D,Q,labels,J)
    via,M=gram_via_moments(D,Q,labels,J)
    assert G==via, ("original trace Gram differs from finite-theta moments",D,len(Q))
    e,o=parity_indexes(labels)
    off=sum(1 for i in e for j in o if G[i][j]!=0)
    if require_symmetric:
        assert off==0,("nonzero even-odd block on symmetric sampling",D)
        for a in range(7):
            for b in range(7-a):
                if (a+b)%2:
                    assert M(a,b)==(0,0), ("odd mixed moment survived",a,b)
    else:
        assert off>0, "wrong-symmetry comparator failed"
    det=det_bareiss(G)
    assert det>0, "selected Gram not positive definite"
    if require_symmetric:
        assert det==det_bareiss(principal(G,e))*det_bareiss(principal(G,o))
    vals=tuple(v_p(det,p) for p in PRIMES)
    assert vals==expected_v, ("valuation regression changed",D,len(Q),vals,expected_v)
    return G,det,off,best_pair_certificate(G,labels)


def old_frame_parity_full_400():
    """All original 400 monomials, not only the 16-row numerical witness."""
    R,S=100,4
    checked=0
    for p in (3,5,7):
        for r in range(R):
            for s in range(S):
                k=min(r//p,S-1-s)
                for h in range(k+1):
                    exponent_r=r-p*h
                    exponent_s=s+h
                    assert exponent_r>=0 and exponent_s<S
                    assert (exponent_r+exponent_s-r-s)%2==0
                    checked+=1
    # At p=2, Z^2-W changes parity under (Z,W)->(-Z,-W).
    assert (2+0)%2 != (0+1)%2
    return checked


def audit_case(D,rho,labels,J,expected):
    Q0=disk(D,rho)
    Q1=window(Q0,D,rho,True)
    QA=window(Q0,D,rho,False)
    assert (len(Q0),len(Q1),len(QA))==expected["points"]
    assert len(set(Q0))==len(Q0)
    assert set(Q1)<set(Q0) and set(QA)<set(Q0)
    assert all((-x,-y) in set(Q0) for x,y in Q0)
    assert all((-x,-y) in set(Q1) for x,y in Q1)
    assert any((-x,-y) not in set(QA) for x,y in QA)
    G0,det0,cross0,corr0=inspect_gram(D,Q0,labels,J,expected["full"],True)
    G1,det1,cross1,corr1=inspect_gram(D,Q1,labels,J,expected["lens"],True)
    GA,detA,crossA,corrA=inspect_gram(D,QA,labels,J,expected["asym"],False)
    excluded=[z for z in Q0 if z not in set(Q1)]
    deletion=exact_gram(D,excluded,labels,J)
    assert all(G0[i][k]-G1[i][k]==deletion[i][k]
               for i in range(len(labels)) for k in range(len(labels)))
    assert det1<det0
    if D==19:
        assert G0==[[42,0],[0,640]] and det0==26880
        assert G1==[[30,0],[0,356]] and det1==10680
        assert GA==[[36,18],[18,498]] and detA==17604
    else:
        assert (len(Q0)*J*2,100*4)==(1752,400)
        assert crossA==64, ("expected nonzero 8x8 cross-parity entries",crossA)
    print("PHASE285_FINITE_THETA_LENS",{
        "D":D,"rho":rho,"points_full_lens_asymmetric":[len(Q0),len(Q1),len(QA)],
        "source_rows_tested":len(labels),"original_full_rows":400 if D==403 else None,
        "full_original_Q_and_ordinary_J":D==403,
        "theta_moment_equals_trace_gram":True,
        "symmetric_even_odd_cross_zero":cross0==cross1==0,
        "asymmetric_cross_nonzero":crossA,
        "det_original_digits":len(str(det0)),
        "det_lens_digits":len(str(det1)),
        "lens_det_strictly_lower":True,
        "vp_full":list(expected["full"]),"vp_lens":list(expected["lens"]),
        "vp_asymmetric":list(expected["asym"]),
        "best_two_by_two_saving_full_approx":round(float(corr0),6),
        "best_two_by_two_saving_lens_approx":round(float(corr1),6),
        "not_a_full_400_row_determinant":True,
        "no_new_field_bound":True,
    },flush=True)



def maximal_order_half_coset(D,rho):
    """Exact enumeration of the missing (1+u)/2 + Z[u] within |z|<=rho."""
    assert D%4==3
    bound=4*rho*rho
    ax=2*rho
    by=isqrt(bound//D)
    count=0
    least=None
    for b in range(-by,by+1):
        if b%2==0:
            continue
        for a in range(-ax,ax+1):
            if a%2==0:
                continue
            norm_numerator=a*a+D*b*b
            if norm_numerator<=bound:
                assert norm_numerator%4==0
                norm=norm_numerator//4
                count+=1
                least=norm if least is None else min(least,norm)
    return count,least


def main():
    freeze_original_helpers()
    rho,R,S,J,Q=params(403)
    assert (rho,R,S,J,len(Q))==(40,100,4,4,219)
    assert Q==disk(403,40)
    assert old_frame_parity_full_400()>=1200
    for D in (19,403):
        assert D%4==3 and (D+1)%4==0
        # Missing maximal-order coset cannot be treated as a far-away tail.
    assert maximal_order_half_coset(19,5)==(20,5)
    assert maximal_order_half_coset(403,40)==(260,101)
    print("PHASE285_HALF_COSET",{
        "D19_rho5": [20,5],
        "D403_rho40": [260,101],
        "not_in_original_source": True,
        "not_an_infinite_theta_tail": True,
    },flush=True)
    audit_case(19,5,[(0,0),(1,0)],1,{
        "points":(21,15,18),
        "full":(8,1,1,1,0),"lens":(3,1,1,0,0),"asym":(2,3,0,0,0),
    })
    audit_case(403,40,[(r,s) for r in range(4) for s in range(4)],4,{
        "points":(219,213,216),
        "full":(56,7,1,1,0),"lens":(56,7,0,1,0),"asym":(80,7,0,0,2),
    })
    print("PASS Phase285 source-exact parity, lens and finite-theta regression",flush=True)


if __name__=="__main__":
    main()
