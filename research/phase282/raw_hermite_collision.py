#!/usr/bin/env python3
"""Phase282: source-faithful raw modular Hermite/collision-rank test, D403.

The protocol and predictions were fixed at d2e5b36 before this program.
This is RAW original evaluation, NOT Frobenius-normalized C0 or a Gram
determinant. No class-number-one or exceptional-zero claim.
"""
from math import comb
from pathlib import Path
import subprocess
import sys
import numpy as np

HERE = Path(__file__).resolve()
RESEARCH = HERE.parents[1]
for sub in ("phase206", "phase207", "phase204", "phase280"):
    sys.path.insert(0, str(RESEARCH / sub))

from source_probe import params, mul, fall, rank_mod
from middle_frobenius import pair_powers, source_dualjet
from ordinary_jet_filtration import jet as integer_jet
from full_d403_second_layer import vec_rank

D, R, S, J, N, POINTS, M = 403, 100, 4, 4, 400, 219, 1752
PRIMES = (3,5,7,11)
TYPE = {3:"inert",5:"inert",7:"inert",11:"split"}
RAW_RANKS = {3:27,5:60,7:84,11:132}
WITHOUT_J3 = {3:27,5:45,7:63,11:99}
FROZEN_BLOBS = {
    "research/phase206/source_probe.py": "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase207/middle_frobenius.py": "f4df80ec6fc6d16a20be717aeb3c8ff135f16a3c",
    "research/phase204/ordinary_jet_filtration.py": "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
    "research/phase280/full_d403_second_layer.py": "7abffdf4f4916dacef08ebe097e5eed700837ad4",
}

def frozen_helper_check():
    root=HERE.parents[2]
    for path,known in FROZEN_BLOBS.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=root,text=True).strip()
        assert actual==known, ("source drift",path,actual,known)
    print("PASS Phase282 frozen source-helper blob IDs",flush=True)


def splitting(p):
    d=(-D)%p
    assert d
    return "split" if d in {x*x%p for x in range(p)} else "inert"


def build_raw_E(p,Q):
    """Original, UNNORMALIZED, ordinary Z jet of Z^r W^s modulo p."""
    assert splitting(p)==TYPE[p]
    cache=[]
    for x,y in Q:
        z=(x%p,y%p)
        w=(x%p,(-y)%p)
        cache.append((pair_powers(z,R,p),pair_powers(w,S-1,p)))
    A=np.zeros((N,M),dtype=np.int64)
    falling=[[fall(r,j)%p for j in range(J)] for r in range(R)]
    for r in range(R):
        for s in range(S):
            row=r*S+s
            for j in range(J):
                coeff=falling[r][j]
                if not coeff:
                    continue
                for qi,(zp,wp) in enumerate(cache):
                    re,im=mul(zp[r-j],wp[s],D,p)
                    c=2*(j*len(Q)+qi)
                    A[row,c]=(coeff*re)%p
                    A[row,c+1]=(coeff*im)%p
    assert A.shape==(N,M)
    return A


def check_original_jet_oracles(E,p,Q):
    """Two differently organized integer-source expansion probes."""
    labels=[(0,0),(1,3),(p,0),(2*p,0),(3*p,1),(50,1),(99,0),(99,3)]
    labels=sorted({(r,s) for r,s in labels if 0<=r<R and 0<=s<S})
    for r,s in labels:
        for qi in (0,len(Q)//2,len(Q)-1):
            x,y=Q[qi]
            z=(x%p,y%p);w=(x%p,(-y)%p)
            dual=source_dualjet(z,w,r,s,0,p,p)
            for j in range(J):
                c=2*(j*len(Q)+qi)
                observed=(int(E[r*S+s,c]),int(E[r*S+s,c+1]))
                exact=tuple(v%p for v in integer_jet(D,r,s,j,(x,y)))
                assert observed==exact,("integer oracle",p,r,s,j,qi)
                assert observed==tuple(v%p for v in dual[j]),(
                    "truncated dual-number oracle",p,r,s,j,qi)
    return len(labels)


def confirm_inert_phi(p,Q):
    """Phi(T)=(T^p-T)*((T^p-T)^2+4D) roots, distinct."""
    assert TYPE[p]=="inert"
    residues=set()
    for x,y in Q:
        z=(x%p,y%p);w=(x%p,(-y)%p)
        residues.add(z)
        zp=pair_powers(z,p,p)[p]
        assert zp==w,("Frobenius is not conjugation",p,x,y,zp,w)
        v=((zp[0]-z[0])%p,(zp[1]-z[1])%p)
        sq=mul(v,v,D,p)
        factor=((sq[0]+4*D)%p,sq[1])
        assert mul(v,factor,D,p)==(0,0),("Phi(root)!=0",p,x,y)
    # There are 3p distinct field roots of the monic degree-3p Phi.
    assert len(residues)==3*p,(p,len(residues))
    return len(residues)


def split_lagrange_coeffs(y,p,u):
    """[constant,T,T²] selector for c_y=2*y*u in F_p."""
    ys=(-1,0,1)
    c={v:2*v*u%p for v in ys}
    other=[v for v in ys if v!=y]
    a,b=c[other[0]],c[other[1]]
    denom=(c[y]-a)*(c[y]-b)%p
    assert denom
    inv=pow(denom,-1,p)
    coeff=[a*b%p,(-a-b)%p,1]
    coeff=[(v*inv)%p for v in coeff]
    for k in ys:
        value=sum(coef*pow(c[k],i,p) for i,coef in enumerate(coeff))%p
        assert value==int(y==k),(y,k,value)
    return coeff


def split_selector_witness(E,p,Q):
    """Explicit 132 ORIGINAL-rectangle row combinations spanning line jets."""
    assert p==11 and TYPE[p]=="split"
    u=2
    assert u*u%p==(-D)%p
    ys=(-1,0,1)
    h=J*p  # 44
    assert R>=(J+2)*p and S>=3 and J<p
    # Hermite Vandermonde basis: for each line y and a=0..43,
    # use L_y(Z^p-W)*Z^a; coefficient expansion only r<100,s<4.
    combinations=np.zeros((len(ys)*h,N),dtype=np.int64)
    for yi,y in enumerate(ys):
        selector=split_lagrange_coeffs(y,p,u)
        for a in range(h):
            target=yi*h+a
            for power,c in enumerate(selector):
                for s in range(power+1):
                    r=a+p*(power-s)
                    coeff=(c*comb(power,s)*(-1 if s&1 else 1))%p
                    assert r<R and s<S,(p,y,a,power,r,s)
                    row=r*S+s
                    combinations[target,row]=(combinations[target,row]+coeff)%p

    # Pick one original ellipse point for each unique (y,z) line coordinate.
    # Projection to the root u=+2 is a legal Fp-linear map of the original
    # two signed coordinate columns, not a new field/source.
    representative={}
    for qi,(x,y) in enumerate(Q):
        if y in ys:
            representative.setdefault((y,(x+u*y)%p),qi)
    assert len(representative)==len(ys)*p
    projected=np.zeros((N,len(ys)*h),dtype=np.int64)
    for yi,y in enumerate(ys):
        for j in range(J):
            for z in range(p):
                qi=representative[(y,z)]
                c=2*(j*len(Q)+qi)
                projected[:,yi*h+j*p+z]=(E[:,c]+u*E[:,c+1])%p
    W=(combinations @ projected)%p
    assert W.shape==(3*h,3*h)

    # Off-stratum blocks vanish exactly, not just in rank.
    for yi,y in enumerate(ys):
        for zi,zz in enumerate(ys):
            block=W[yi*h:(yi+1)*h,zi*h:(zi+1)*h]
            if yi!=zi:
                assert not np.any(block),("selector leaks across stratum",y,zz)

    # On the chosen stratum the block must equal Hermite jets of
    # 1,Z,...,Z^43 at every Z=z in F11.
    for yi,y in enumerate(ys):
        block=W[yi*h:(yi+1)*h,yi*h:(yi+1)*h]
        for a in range(h):
            for j in range(J):
                for z in range(p):
                    expected=(fall(a,j)*pow(z,a-j,p))%p if a>=j else 0
                    assert int(block[a,j*p+z])==expected,(
                        "Hermite block mismatch",y,a,j,z)
        assert vec_rank(block,p)==h
        assert rank_mod(block.tolist(),p)==h
    assert vec_rank(W,p)==3*h
    assert rank_mod(W.tolist(),p)==3*h
    return W.shape[0]


def main():
    frozen_helper_check()
    rho,R0,S0,J0,Q=params(D)
    assert (rho,R0,S0,J0,len(Q))==(40,R,S,J,POINTS)
    assert M==2*len(Q)*J
    assert {y for x,y in Q}=={-1,0,1}
    for p in PRIMES:
        strata={y:{x%p for x,yy in Q if yy==y} for y in (-1,0,1)}
        assert all(v==set(range(p)) for v in strata.values()),(p,strata)
        E=build_raw_E(p,Q)
        oracles=check_original_jet_oracles(E,p,Q)
        raw=vec_rank(E,p)
        assert raw==rank_mod(E.tolist(),p)==RAW_RANKS[p],(
            "wrong raw full rank",p,raw,RAW_RANKS[p])
        # Wrong-source deletion only: the ordinary raw third derivative
        # vanishes entirely in characteristic three.
        without=vec_rank(E[:,:2*(J-1)*len(Q)],p)
        assert without==WITHOUT_J3[p],(p,without,WITHOUT_J3[p])
        if p==3:
            assert not np.any(E[:,2*(J-1)*len(Q):]),"raw j=3 nonzero mod3"
        if TYPE[p]=="inert":
            nodes=confirm_inert_phi(p,Q)
            t=min(J,p)
            s0_rows=[r*S for r in range(3*p*t)]
            assert len(s0_rows)==RAW_RANKS[p] and max(s0_rows)<N
            witness=vec_rank(E[s0_rows],p)
            assert witness==rank_mod(E[s0_rows].tolist(),p)==3*p*t
            witness_type="inert s=0 first 3pt monomials"
        else:
            nodes=3*p
            witness=split_selector_witness(E,p,Q)
            witness_type="split Lagrange(Z^p-W)*Z^a original row span"
        print("PHASE282_RAW_HERMITE",{
            "D":D,"p":p,"splitting":TYPE[p],
            "rows":N,"columns":M,"ellipse_points":len(Q),
            "distinct_modular_nodes":nodes,
            "nonzero_jet_orders":min(J,p),
            "raw_modp_rank":raw,
            "rank_without_j3_WRONG_SOURCE":without,
            "rank_witness":witness,
            "witness_type":witness_type,
            "source_oracle_row_count":oracles,
            "NO_smith_index_from_raw_rank":True,
            "NO_primitive_pairing_computed":True,
        },flush=True)
    print("PASS Phase282 original raw D403 inert/split Hermite collision ranks",flush=True)

if __name__=="__main__":
    main()
