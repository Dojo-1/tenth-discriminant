#!/usr/bin/env python3
"""Phase148: finite arithmetic chamber, exact common-support minimum and
inverse-free raw Hadamard minimax, using original ordinary Z jets.

Frozen rho=5, R=8, S=J=4, D=17..21. Source lineage:
Phase140 original -> Phase147 parameterized entrywise-checked evaluator.
P-paper: ordinary integer/p-local Smith identities, monotone Hadamard bound.
M: exhaustive finite experiment. Not a field-discriminant theorem.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
from math import comb, prod
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from phase147_prime_adequacy import (
    R,S,J,N, qellipse, original_eval, dabs, F2_blocks, F3_blocks,
    rank2, rank3, rankprime, full_image_certificate, lnint, falling,
)

DS=(17,18,19,20,21)
OPTIMAL=[(-2,-1),(-2,0),(-1,-1),(-1,0),(0,-1),(0,0),
         (1,-1),(1,0),(2,-1)]
GREEDY=[(-3,0),(-2,0),(-2,1),(-1,0),(-1,1),
        (0,0),(0,1),(1,1),(2,1)]
BAD=[(-2,0),(-1,-1),(-1,0),(0,0),(0,1),(1,1),(5,0)]

def raw_diagonal(nodes,d):
    """Exact integer diagonal of the ORIGINAL positive trace Gram."""
    diag=[]
    for r in range(R):
        for s in range(S):
            total=0
            for x,y in nodes:
                n=x*x+d*y*y
                for j in range(min(r,J-1)+1):
                    total+=2*falling(r,j)**2*n**(r+s-j)
            diag.append(total)
    assert len(diag)==N and all(z>0 for z in diag)
    return diag

def raw_upper(nodes,d):
    """Exact product, never a floating objective or inverse-Gram estimate."""
    return prod(raw_diagonal(nodes,d))

def source_gram(nodes,d):
    E=original_eval(nodes,d)
    G=E*Matrix.diag(*([2,2*d]*(E.cols//2)))*E.T
    assert list(G.diagonal())==raw_diagonal(nodes,d)
    determinant=dabs(G)
    assert 0<determinant<=raw_upper(nodes,d)
    return determinant

def pivot_minor_mod(C,p):
    basis={}
    indices=[]
    for j in range(C.cols):
        v=[int(C[i,j])%p for i in range(N)]
        for i in range(N-1,-1,-1):
            if not v[i]:continue
            if i in basis:
                b=basis[i]; k=v[i]
                v=[(u-k*w)%p for u,w in zip(v,b)]
            else:
                inv=pow(v[i],-1,p)
                basis[i]=[(inv*w)%p for w in v]
                indices.append(j)
                break
        if len(indices)==N:return indices
    return None

def relative_group(C):
    """Exact HNF+Smith using a checked nonzero 32-square minor as modulus."""
    for prime in (101,103,107,109,113,127):
        cols=pivot_minor_mod(C,prime)
        if cols is None:continue
        minor=dabs(C[:,cols]);assert minor%prime!=0
        H=hermite_normal_form(C,D=minor)
        size=dabs(H)
        sn=smith_normal_form(H,domain=ZZ)
        factors=[abs(int(sn[i,i])) for i in range(N)
                 if abs(int(sn[i,i]))!=1]
        assert prod(factors)==size
        return size,factors
    raise AssertionError("No certified rational-full-rank minor in probe primes")

def main():
    assert (R,S,J,N)==(8,4,4,32)
    universe=qellipse(17)
    assert len(universe)==21 and all(qellipse(d)==universe for d in DS)
    assert all(set(q).issubset(universe) for q in (OPTIMAL,GREEDY,BAD))
    # Eight real-axis nodes give a source-compatible nonzero square minor,
    # independent of d, which is a valid modular HNF modulus for every full E.
    real=original_eval([(x,0) for x in range(-4,4)],19)
    minor=real[:,[8*t+2*j for t in range(8) for j in range(J)]]
    base_witness=dabs(minor)
    assert base_witness>0
    C={}; B2={}; B3={}
    for d in DS:
        E=original_eval(universe,d)
        H=hermite_normal_form(E,D=base_witness)
        transformed=H.inv()*E
        assert all(x.q==1 for x in transformed)
        C[d]=transformed.applyfunc(int)
        B2[d]=F2_blocks(C[d])
        B3[d]=F3_blocks(C[d])
        assert rank2(B2[d],range(len(universe)))==N
        assert rank3(B3[d],range(len(universe)))==N
    print("PASS: five identical 21-node geometries, five source-matched integral images",flush=True)

    # A smaller conflict core: the pair d=17,18 alone excludes all 8-node
    # common supports. For confidence, compare fast rank with generic mod-p
    # Gaussian elimination on deterministic members of the critical class.
    pair_r3=Counter();both_binary=both_ternary=0
    all_binary=all_ternary=0
    samples=[]
    for inds in combinations(range(len(universe)),8):
        p2_17=rank2(B2[17],inds)==N
        p2_18=rank2(B2[18],inds)==N
        if p2_17 and p2_18:
            both_binary+=1
            rank18=rank3(B3[18],inds)
            pair_r3[rank18]+=1
            if rank18==N:both_ternary+=1
            if both_binary%1133==0:samples.append(inds)
        if not (p2_17 and p2_18):continue
        if not all(rank2(B2[d],inds)==N for d in (19,20,21)):continue
        all_binary+=1
        if all(rank3(B3[d],inds)==N for d in DS):all_ternary+=1
    assert both_binary==35748 and both_ternary==0
    assert dict(pair_r3)=={
         13:2,17:194,18:1082,21:1812,22:11074,24:256,
         25:2560,26:14704,28:608,29:448,30:3008}
    assert all_binary==1728 and all_ternary==0
    for inds in samples:
        assert rank2(B2[17],inds)==rankprime(C[17],inds,2)
        assert rank2(B2[18],inds)==rankprime(C[18],inds,2)
        assert rank3(B3[18],inds)==rankprime(C[18],inds,3)
    print("EXHAUSTIVE 8-point: C(21,8)=",comb(21,8),
          "pair p2 passes",both_binary,"pair D18 p3 passes",both_ternary,
          "all-five p2 passes",all_binary,"all-five p3 passes",all_ternary,
          "maximum pair D18 ternary rank",max(pair_r3),flush=True)

    # Exact combinatorial search over ALL 9-point supports, not a greedy
    # optimizer. Every adequate support must pass both modular prefilters.
    valid_candidates=[]
    nine_binary=nine_ternary=0
    for inds in combinations(range(len(universe)),9):
        if not all(rank2(B2[d],inds)==N for d in DS):continue
        nine_binary+=1
        if not all(rank3(B3[d],inds)==N for d in DS):continue
        nine_ternary+=1
        q=[universe[i] for i in inds]
        valid_candidates.append((raw_upper(q,21),inds))
    assert nine_binary==11232 and nine_ternary==768
    valid_candidates.sort()
    best_upper,best_inds=valid_candidates[0]
    best=[universe[i] for i in best_inds]
    assert best==OPTIMAL,(best,OPTIMAL)
    ties=sum(1 for v,inds in valid_candidates if v==best_upper)
    assert ties>=1
    for d in DS:
        inds=list(best_inds)
        Cs=C[d][:,[8*t+j for t in inds for j in range(8)]]
        assert full_image_certificate(Cs)
        assert rankprime(C[d],inds,2)==N
        assert rankprime(C[d],inds,3)==N
        assert rankprime(C[d],inds,5)==N
    # The exact raw diagonal is weakly increasing in D. Thus the maximum
    # of the raw bound across this chamber is attained at D=21, for ANY Q.
    for candidate in (OPTIMAL,GREEDY):
        upper=[raw_upper(candidate,d) for d in DS]
        assert upper==sorted(upper)
        for d in DS:
            det=source_gram(candidate,d)
            assert raw_upper(candidate,d)>=det
    assert best_upper < raw_upper(GREEDY,21)
    print("EXHAUSTIVE 9-point: C(21,9)=",comb(21,9),
          "all-five binary passes",nine_binary,
          "binary+ternary passes",nine_ternary,
          "exact minimax ties",ties,flush=True)
    print("EXACT OPTIMAL common9 support:",best,flush=True)
    print("optimal upper log at D21",f"{lnint(best_upper):.12f}",
          "greedy upper log",f"{lnint(raw_upper(GREEDY,21)):.12f}",flush=True)
    for d in DS:
        det=source_gram(best,d)
        orig=source_gram(universe,d)
        upper=raw_upper(best,d)
        assert det<orig
        print("D",d,"logdet optimized",f"{lnint(det):.9f}",
              "logdet full",f"{lnint(orig):.9f}",
              "log raw upper",f"{lnint(upper):.9f}",flush=True)

    # The same 7-node support has different prime-primary failures inside
    # the SAME sampling geometry. Neither 'p divides D' nor a fixed prime
    # screening list is a complete rule.
    expected={
        17:(1377,[3,3,3,51]),
        18:(2187,[3,3,3,3,3,9]),
        19:(1,[]),
        20:(12960000,[60,60,60,60]),
        21:(2401,[7,7,7,7]),
    }
    bad_inds=[universe.index(q) for q in BAD]
    for d in DS:
        bad=C[d][:,[8*t+j for t in bad_inds for j in range(8)]]
        index,factors=relative_group(bad)
        assert (index,factors)==expected[d],(d,index,factors)
        print("fixed bad7 support D",d,"relative index",index,
              "nonunit Smith factors",factors,flush=True)
    print("PHASE148_PASS: pairwise p-local obstruction, five-D minimum9, exact Hadamard minimax",flush=True)

if __name__=="__main__":
    main()
