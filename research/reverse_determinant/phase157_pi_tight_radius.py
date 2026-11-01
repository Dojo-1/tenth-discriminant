#!/usr/bin/env python3
"""Phase157: Archimedean 3.14<pi<3.15 radius budget, same original jet Gram.

This is a source-matched quantitative falsification harness and exact rational
gate checker. It does NOT prove Frobenius rank uniformly, Cauchy-Binet in Lean,
Nagura's theorem, or any new number-field cutoff.
"""
from fractions import Fraction as Q
from mpmath import mp
from sympy import nextprime
from phase153_bertrand_budget import normalized, source_correspondence
from phase156_transport_archim_jets import min_t2

mp.dps=75
F=mp.mpf
C=F(157)/50
PI_UP=F(63)/20

def improved_radius(D,p):
    d=F(D)
    delta=mp.sqrt(d+1)/2
    a=mp.sqrt(F(p)*mp.sqrt(d)/C)
    return int(mp.ceil(delta+a))

def area_capacity_upper(D,rho):
    d=F(D)
    delta=mp.sqrt(d+1)/2
    return int(mp.floor(PI_UP*(rho+delta)**2/mp.sqrt(d)))

def profile(D,p,k=25,c=F(157)/50):
    R=p-1
    S=R//k
    d=F(D)
    rho=int(mp.ceil(mp.sqrt(d+1)/2+mp.sqrt(F(p)*mp.sqrt(d)/c)))
    N=int(mp.floor(PI_UP*(rho+mp.sqrt(d+1)/2)**2/mp.sqrt(d)))
    assert S>0 and R*S <=N*S
    beta=R*S+2*min_t2(R*S,N,S)
    L,U=normalized(R,S,rho,4*D)
    gain=F(beta)*mp.log(2)/(F(R)**2*S)
    return {"D":D,"p":p,"k":k,"R":R,"S":S,"rho":rho,"N":N,
            "N_over_p":F(N)/p,"lower":L,"upper":U,
            "gain":gain,"gap":L+gain-U}

def rational_gates():
    c=Q(157,50)
    t=Q(107,207)  # (3.14-1)/(3.14+1)
    # log 3.14 = 2 sum_{j>=0} t^(2j+1)/(2j+1).
    # All remaining summands are positive.
    lo=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(5)),Q(0))
    assert lo>Q(143,125) # >1.144 exactly, no floating log inference
    e=Q(39,20*265)+Q(4,265**3)
    assert 265**4<5_000_000_000
    assert Q(39,10)**2 > Q(24,5)*c
    assert Q(5,4)**2 > Q(24,5)/c
    assert Q(63,20)/c*(1+Q(39,10*265)+Q(4,265**3))**2<Q(26,25)
    assert Q(26,25)*(1+Q(1,10**9))<Q(21,20)
    assert Q(5,4*265)*(1+e)*(1+Q(1,10**9))<Q(1,200)
    # An explicitly typed source-normalized upper, NOT an independent one:
    # .24 logD+.56 logR -(12/25)log c - .08 + (24/25)e + residual.
    const=-Q(12,25)*Q(143,125)-Q(2,25)+Q(24,25)*e+Q(1,2000)
    assert const < -Q(31,50) # <-0.62
    assert Q(69,100)*(Q(1,28)-Q(9,10**9))>Q(49,2000)
    # Nagura, log R > log D-log(24/5)-1e-6.
    margin=Q(1,5)*Q(223,10)-Q(44,100)*Q(157,100)-Q(4411,1000)+Q(31,50)+Q(49,2000)-Q(1,10**6)
    assert margin>Q(26,10000)
    assert mp.log(2)>F(".69") and mp.log(F(24)/5)<F("1.57")
    assert mp.log(5_000_000_000)>F("22.3")
    assert mp.log(C)>F("1.144")
    print("PHASE157_EXACT_RATIONAL_GATES_PASS",
          "logc_lower",float(lo),"N_over_p_max",float(Q(63,20)/c*(1+Q(39,10*265)+Q(4,265**3))**2),
          "uniform_gap_floor",float(margin),flush=True)

def sample_tests():
    for D in (4_500_000_003,5_000_000_003,5_500_000_003,
              6_000_000_003,8_000_000_003,25_000_000_003,
              100_000_000_003):
        m=(D+1)//4
        for ratio in (F(5)/6+F("1e-9"),F(".9"),F(".99999999")):
            p=int(mp.floor(F(m)*ratio))+1 # analytic only: NOT necessarily prime
            q=profile(D,p)
            if D>=5_000_000_000:
                R=q["R"]
                assert q["lower"]>=mp.log(R)-F("4.411")
                assert q["upper"]<=F(".24")*mp.log(D)+F(".56")*mp.log(R)-F(".62")
                assert q["N"]<F(26)*p/25 and q["N"]<F(21)*R/20
                assert q["rho"]<F(R)/200
                assert q["gain"]>F(".0245")
                assert q["gap"]>0
            if ratio<F(".834"):
                old=profile(D,p,c=F(3))
                print("PHASE157_ENDPOINT",D,"p",p,"rho3",old["rho"],
                      "rho314",q["rho"],"ratioN",mp.nstr(q["N_over_p"],9),
                      "old_gap",mp.nstr(old["gap"],11),
                      "tight_gap",mp.nstr(q["gap"],11),flush=True)
                if D==4_500_000_003: assert q["gap"]<0
                if D==5_000_000_003: assert old["gap"]<0<q["gap"]
    # A genuine prime in the Nagura interval as a numeric *parameter*;
    # no claim that the associated actual quadratic field has class number one.
    D=5_000_000_003
    m=(D+1)//4
    p=int(nextprime((5*m)//6))
    assert p<m and 6*p>5*m
    q=profile(D,p)
    assert q["gap"]>0
    print("PHASE157_ACTUAL_PRIME_PARAMETER",p,
          "radius",q["rho"],"margin",mp.nstr(q["gap"],14),flush=True)

def main():
    source_correspondence()
    rational_gates()
    sample_tests()
    print("PHASE157_PI_TIGHT_JET_RADIUS_PASS: finite/paper only; no field theorem",flush=True)

if __name__=="__main__":
    main()
