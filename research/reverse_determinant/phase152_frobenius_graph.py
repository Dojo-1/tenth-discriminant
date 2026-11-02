#!/usr/bin/env python3
"""Phase152: original ordinary-Z jets on the characteristic-p Frobenius graph.

Exact p-rank and determinant controls; mathematical theorem in the dossier.
No Hasse-jet substitution, new field cutoff, or assumed actual h(-D)=1.
"""
from __future__ import annotations
from math import ceil, sqrt, isqrt, log, prod
from pathlib import Path
from sympy import isprime, prevprime

def pair_mul(a,b,d,p):
    return ((a[0]*b[0]-d*a[1]*b[1])%p,
            (a[0]*b[1]+a[1]*b[0])%p)

def powers(z,n,d,p):
    out=[(1,0)]
    for _ in range(n):out.append(pair_mul(out[-1],z,d,p))
    return out

def falling(r,j):
    z=1
    for i in range(j):z*=r-i
    return z

def eval_rows(Q,d,R,S,J,p):
    """Original (r)_j Z^(r-j) W^s and paired real/imag integer columns mod p."""
    assert 1<=J<=R and 1<=S<=R
    E=[[0]*(len(Q)*2*J) for _ in range(R*S)]
    for t,(x,y) in enumerate(Q):
        zp=powers((x%p,y%p),R-1,d,p)
        wp=powers((x%p,-y%p),S-1,d,p)
        for r in range(R):
            for s in range(S):
                row=E[r*S+s]
                for j in range(min(r,J-1)+1):
                    a,b=pair_mul(zp[r-j],wp[s],d,p)
                    f=falling(r,j)%p
                    row[2*J*t+2*j]=f*a%p
                    row[2*J*t+2*j+1]=f*b%p
    return E

def rank_det_mod(E,p):
    """Independent finite-field elimination; determinant for a square full-rank E."""
    A=[r[:] for r in E]
    n=len(A);m=len(A[0]);rank=0;det=1
    for col in range(m):
        if rank==n:break
        k=next((i for i in range(rank,n) if A[i][col]),None)
        if k is None:continue
        if k!=rank:
            A[k],A[rank]=A[rank],A[k]
            det=-det%p
        pivot=A[rank][col]
        det=det*pivot%p
        inv=pow(pivot,-1,p)
        A[rank][col:]=[(v*inv)%p for v in A[rank][col:]]
        row=A[rank]
        for i in range(rank+1,n):
            factor=A[i][col]
            if factor:
                for j in range(col+1,m):
                    A[i][j]=(A[i][j]-factor*row[j])%p
                A[i][col]=0
        rank+=1
    return rank,det if n==m and rank==n else None

def conjugate_residues(Q,p):
    roots=[]
    for x,y in Q:
        roots.append((x%p,y%p))
        if y%p:roots.append((x%p,(-y)%p))
    return roots

def test_case(d,p,R,S,J,Q,rho):
    assert p>2 and isprime(p) and pow((-d)%p,(p-1)//2,p)==p-1
    assert R<=p and J<=p
    assert all(x*x+d*y*y<=rho*rho for x,y in Q)
    roots=conjugate_residues(Q,p)
    assert len(roots)==len(set(roots))
    degree=R-1+p*(S-1)
    sufficient=J*len(roots)>degree
    rank,det=rank_det_mod(eval_rows(Q,d,R,S,J,p),p)
    return dict(D=d,p=p,R=R,S=S,J=J,rho=rho,nodes=len(Q),
                roots=len(roots),multiplicity=J*len(roots),
                degree=degree,sufficient=sufficient,rank=rank,
                target=R*S,det=det,
                old_guard=(2*(R-1)+(S-1)<len(Q)),
                p_below_class_one_inert_cut=(p<(d+1)/4))

def raw_hadamard_product(Q,d,R,S,J):
    """Exact original trace-Gram diagonal product, WITHOUT inverse Gram."""
    diag=[]
    for r in range(R):
        for s in range(S):
            acc=0
            for x,y in Q:
                norm2=x*x+d*y*y
                for j in range(min(r,J-1)+1):
                    acc+=2*falling(r,j)**2*norm2**(r+s-j)
            assert acc>0
            diag.append(acc)
    return prod(diag)

def source_check():
    from phase147_prime_adequacy import original_eval
    p=31;d=19;Q=[(-1,1),(0,0),(2,-1)]
    A=eval_rows(Q,d,8,4,4,p)
    B=original_eval(Q,d)
    assert B.shape==(32,24)
    assert all(A[i][j]==int(B[i,j])%p
               for i in range(32) for j in range(24))
    print('PASS: source-matched original Phase140/147 ordinary-Z jets',flush=True)

def main():
    source_check()
    Q16=[(x,1) for x in range(-7,9)]
    a=test_case(163,31,30,5,5,Q16,16)
    assert (a['roots'],a['multiplicity'],a['degree'])==(32,160,153)
    assert a['sufficient'] and a['rank']==150
    assert not a['old_guard'] and a['p_below_class_one_inert_cut']
    print('FROBENIUS SUFFICIENT D163',a,flush=True)

    Q15=[(x,1) for x in range(-7,8)]
    opt=test_case(163,31,30,5,5,Q15,15)
    assert opt['rank']==150 and opt['det']==22
    assert not opt['sufficient']  # do NOT promote a sufficient test to necessary!
    assert 2*5*len(Q15)==150
    print('ONE-NODE-SLACK COUNTERWORLD D163',opt,flush=True)

    # Each integer radius has its own exactly certified minimum-node support.
    hadamards=[]
    cases=((13,range(-2,3),range(-10,10),25,29,5),
           (14,range(-5,6),range(-4,4),19,22,11),
           (15,range(-7,8),range(0,0),15,22,15))
    for rho,nonreal,real,nmin,residue,kmax in cases:
        Q=[(x,1) for x in nonreal]+[(x,0) for x in real]
        assert len(Q)==nmin
        assert all(x*x+163*y*y<=rho*rho for x,y in Q)
        assert 2*isqrt(rho*rho-163)+1==kmax
        positions=[]
        for t,(_,y) in enumerate(Q):
            for j in range(5):
                positions.append(10*t+2*j)
                if y:positions.append(10*t+2*j+1)
        assert len(positions)==150
        E=eval_rows(Q,163,30,5,5,31)
        rank,det=rank_det_mod([[row[j] for j in positions] for row in E],31)
        assert (rank,det)==(150,residue)
        assert nmin==max(15,30-kmax)
        bound=raw_hadamard_product(Q,163,30,5,5)
        hadamards.append(bound)
        print('PARETO D163',dict(radius=rho,min_nodes=nmin,
              maximum_nonreal_orbits=kmax,det_mod31=det,
              raw_Hadamard_log_normalized=log(bound)/(30*30*5)),flush=True)
    assert hadamards[0]<hadamards[1]<hadamards[2]  # exact integer comparison
    assert 12*12<163 and (2*12+1)*5<150

    b=test_case(43,7,6,2,2,[(x,0) for x in range(-3,4)],5)
    assert b['sufficient'] and b['rank']==12 and not b['old_guard']
    print('ALL-REAL NULL D43',b,flush=True)

    # Under p<R, P(Z,W)=Z^p-W lies in the polynomial rectangle
    # and vanishes with ALL original ordinary-Z derivatives j<p mod p.
    E=eval_rows([(x,0) for x in range(-4,5)],43,8,2,2,7)
    assert all((a-b)%7==0 for a,b in zip(E[7*2],E[1]))
    print('COUNTERWORLD p<R: Z^p-W is a nonzero modular row relation',flush=True)

    # Pure geometric scale illustration. DO NOT infer actual h(-D)=1
    # or p inert for this large D: it is a hypothetical field parameter.
    D=41_006_250_003
    m=(D+1)//4;p=int(prevprime(m))
    assert m/2<p<m and isprime(p)
    delta=sqrt(D+1)/2
    rho=ceil(delta+sqrt(p*sqrt(D)/3))
    assert 2*rho<p and rho<0.31*D**0.75
    print('HYPOTHETICAL geometry only:',dict(D=D,p=p,R=p-1,
        rho=rho,old_radius_approx=0.52*D**0.75,
        radius_ratio=rho/(0.52*D**0.75)),flush=True)
    print('PHASE152_FROBENIUS_GRAPH_PASS',flush=True)

if __name__=='__main__': main()
