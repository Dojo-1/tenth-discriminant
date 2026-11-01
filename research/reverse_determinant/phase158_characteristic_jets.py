#!/usr/bin/env python3
"""Phase158: Walsh-inspired characteristic supports for ORIGINAL ordinary jets.

Bounded exact Fp tests; independent polynomial-quotient/obstruction oracle;
no numerical class-number-one cutoff is certified by this script.
"""
from __future__ import annotations
from mpmath import mp
from sympy import nextprime
from phase152_frobenius_graph import (eval_rows, rank_det_mod,
    conjugate_residues, raw_hadamard_product, source_check)
from phase155_jet_precision import annihilator, poly_mul, monomial_remainders
from phase156_transport_archim_jets import capacity, min_t2
from phase157_pi_tight_radius import profile

mp.dps=75

def pick_exact_roots(Q,p,D):
    """Select p conjugation-stable roots without expanding the original disk.

    Assumes y>=0 representatives, one real point, no residue collisions,
    and a total of at least p roots. The centered choice is a heuristic.
    """
    assert p%2==1 and len(Q)==len(set(Q))
    real=sorted((q for q in Q if q[1]==0),key=lambda q:(abs(q[0]),q[0]))
    nonreal=sorted((q for q in Q if q[1]>0),
                   key=lambda q:(q[0]*q[0]+D*q[1]*q[1],abs(q[0]),q[0]))
    assert real and len(real)+2*len(nonreal)>=p
    pairs=min(len(nonreal),(p-1)//2)
    nreal=p-2*pairs
    assert nreal%2==1 and 1<=nreal<=len(real)
    chosen=real[:nreal]+nonreal[:pairs]
    roots=conjugate_residues(chosen,p)
    assert len(roots)==len(set(roots))==p
    return chosen

def roots_count(Q):
    return sum(1 if y==0 else 2 for x,y in Q)

def obstruction_matrix(g,p,S):
    """For deg g=p-1, a square (S-1)x(S-1) forbidden-coefficient map."""
    assert len(g)==p and g[-1]%p==1 and 2<=S<=p-1
    h=[1]
    for _ in range(S):h=poly_mul(h,g,p)
    n=S-1
    return [[h[k*p-1-j] if 0<=k*p-1-j<len(h) else 0
             for j in range(n)] for k in range(1,S)]

def polynomial_quotient_rank(Q,D,p,R,S):
    g=annihilator(Q,D,p)
    h=[1]
    for _ in range(S):h=poly_mul(h,g,p)
    rem=monomial_remainders(h,R-1+p*(S-1),p)
    return rank_det_mod([rem[r+p*s] for r in range(R)
                         for s in range(S)],p)[0]

def finite_characteristic_controls():
    source_check()
    p,D,R,S=31,163,30,5
    full=[(x,0) for x in range(-13,14)]+[(x,1) for x in range(-2,3)]
    assert roots_count(full)==37
    assert pow((-D)%p,(p-1)//2,p)==p-1
    selected=pick_exact_roots(full,p,D)
    assert len(selected)==26 and roots_count(selected)==p
    assert set(selected).issubset(full)
    assert all(x*x+D*y*y<=13**2 for x,y in selected)
    erank,_=rank_det_mod(eval_rows(selected,D,R,S,S,p),p)
    qrank=polynomial_quotient_rank(selected,D,p,R,S)
    assert erank==qrank==R*S
    bfull=capacity(full,D,R,S,2)
    bselected=capacity(selected,D,R,S,2)
    assert (bfull,bselected)==(310,430)
    assert raw_hadamard_product(selected,D,R,S,S)<raw_hadamard_product(full,D,R,S,S)
    print('PHASE158_31_ROOTS',dict(radius=13,nodes=len(selected),
          roots=p,source_rank=erank,quotient_rank=qrank,
          beta2_full=bfull,beta2_selected=bselected),flush=True)
    cases=(
      (13,29,[(x,1) for x in range(-2,3)]+[(x,0) for x in range(-10,10)]),
      (14,23,[(x,1) for x in range(-5,6)]+[(x,0) for x in range(-4,4)]),
      (15,8,[(x,1) for x in range(-7,8)])
    )
    for rad,want,Q in cases:
        assert roots_count(Q)==p-1
        assert len(set(conjugate_residues(Q,p)))==p-1
        O=obstruction_matrix(annihilator(Q,D,p),p,S)
        rank_o,det_o=rank_det_mod(O,p)
        rank_q=polynomial_quotient_rank(Q,D,p,R,S)
        rank_e,_=rank_det_mod(eval_rows(Q,D,R,S,S,p),p)
        assert rank_o==S-1 and det_o==want
        assert rank_q==rank_e==R*S
        if rad==13:
            assert O==[[0,4,26,23],[29,19,21,5],
                       [2,14,9,14],[16,12,0,14]]
        print('PHASE158_OBSTRUCTION',dict(radius=rad,
              matrix_size=S-1,det_mod_p=det_o,original_rank=rank_e),flush=True)

def counterworlds():
    p,D,R,S=5,2,4,2
    Q=[(0,0),(2,0),(0,1)]
    g=annihilator(Q,D,p)
    assert g==[0,1,2,3,1]  # T(T-2)(T^2+2) over F5
    O=obstruction_matrix(g,p,S)
    rank_o,det_o=rank_det_mod(O,p)
    rank_e,_=rank_det_mod(eval_rows(Q,D,R,S,S,p),p)
    rank_q=polynomial_quotient_rank(Q,D,p,R,S)
    assert O==[[0]] and rank_o==0 and det_o is None
    assert rank_e==rank_q==7<R*S
    print('PHASE158_BAD_P_MINUS_ONE',dict(p=p,rank=rank_e,target=R*S),flush=True)
    # The full multiplicative group is a successful but expensive real-axis
    # p-1-root family: the radius cost is O(p), unlike the useful disk.
    for p,D,S in [(5,2,2),(7,1,3),(11,1,3)]:
        Q=[(x,0) for x in range(1,p)]
        assert pow((-D)%p,(p-1)//2,p)==p-1
        O=obstruction_matrix(annihilator(Q,D,p),p,S)
        r,d=rank_det_mod(O,p)
        erank,_=rank_det_mod(eval_rows(Q,D,p-1,S,S,p),p)
        assert r==S-1 and d is not None and erank==(p-1)*S
    print('PHASE158_REAL_AXIS_RADIUS_CONTROL_PASS',flush=True)

def numerical_budget_probe():
    # The actual p is only a prime parameter: NO claim about h(-D)=1.
    D=5_000_000_003
    m=(D+1)//4
    p=int(nextprime(5*m//6))
    assert p<m and 6*p>5*m
    old=profile(D,p,k=25)
    R,S=p-1,(p-1)//25
    beta=R*S+2*min_t2(R*S,p,S)
    selected_gain=mp.mpf(beta)*mp.log(2)/(mp.mpf(R)**2*S)
    selected_gap=old['lower']+selected_gain-old['upper']
    assert selected_gain>old['gain'] and selected_gap>old['gap']>0
    print('PHASE158_SOURCE_BUDGET',dict(D=D,p=p,rho=old['rho'],
          previous_upper_channel_cap=old['N'],selected_channel_cap=p,
          old_gap=mp.nstr(old['gap'],13),
          characteristic_gap=mp.nstr(selected_gap,13)),flush=True)

def main():
    finite_characteristic_controls()
    counterworlds()
    numerical_budget_probe()
    print('PHASE158_WALSH_CHARACTERISTIC_JETS_PASS: finite only',flush=True)

if __name__=='__main__':main()
