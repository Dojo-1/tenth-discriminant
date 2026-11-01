#!/usr/bin/env python3
"""Phase154: prime-window geometry against the ORIGINAL ordinary-jet Gram.

Run from repository root. Proven classic prime intervals are INPUTS, not
proved by this program. Uniform inequalities have a separate paper proof
target, not a finite numerical theorem. Source coefficients use Phase153.
"""
from fractions import Fraction as F
import mpmath as mp
from sympy import nextprime
from phase153_bertrand_budget import normalized, radius, source_correspondence

mp.dps=75
M=mp.mpf

def constants():
    # D>=8e9, p/m>=5/6: exact gates in the paper proof.
    assert 298**4 < 8_000_000_000
    assert F(19,10*298)+F(4,298**3)<F(1,150)
    assert F(13,10*298)*(1+F(2,10**9))+F(3,298**2)+F(5,298**4)<F(1,200)
    # D>=5e9, p/m>=257/258: stricter prime-window input.
    assert 265**4 < 5_000_000_000
    assert F(7,4*265)+F(4,265**3)<F(1,150)
    assert F(6,5*265)*(1+F(2,10**9))+F(3,265**2)+F(5,265**4)<F(1,200)
    cost=(F(3,2)+F(1,10**9-1)+F(15,30000)+F(1791,1000)
          +F(19786,10**9)+(F(25)+F(25,40_000_000))*F(134281,1_000_000)/3)
    assert cost < F(4411,1000)
    endpoint=F(10,89000)+F(1,2500)+F(2,25*30000)
    assert endpoint < F(1,1000)
    assert -F(12,25)*F(109,100)-F(2,25)+F(24,25)*(F(1,150)+F(1,2*10**9))+endpoint < -F(595,1000)
    assert mp.log(3)>M('1.09')
    assert mp.log(8_000_000_000)>M('22.8')
    assert mp.log(5_000_000_000)>M('22.3')
    assert mp.log(M(24)/5)<M('1.57')
    assert mp.log(M(1032)/257)<M('1.4')
    gap8=F(1,5)*F(228,10)-F(44,100)*F(157,100)-F(3816,1000)-F(1,1_000_000)
    gap5=F(1,5)*F(223,10)-F(44,100)*F(14,10)-F(3816,1000)-F(1,1_000_000)
    assert gap8>F(53,1000) and gap5>F(27,1000)
    print('PRIME_WINDOW_RATIONAL_GATES_PASS',float(cost),float(gap8),float(gap5),flush=True)

def sample(D,gamma):
    m=(D+1)//4
    p=int(mp.floor(M(m)*gamma))+1  # analytic stress only; not necessarily prime/inert!
    R=p-1;S=R//25;rho=radius(D,p)
    L,U=normalized(R,S,rho,4*D)
    assert R>rho and 25*S<=R<=26*S
    return p,R,S,rho,L,U,L-U

def check(D,ratio,required):
    p,R,S,rho,L,U,gap=sample(D,ratio)
    if required:
        assert L >= mp.log(R)-M('4.411')
        assert U <= M('0.24')*mp.log(D)+M('0.56')*mp.log(R)-M('0.595')
        assert gap>0
    return p, R, S, rho, float(L),float(U),float(gap)

def main():
    source_correspondence()
    constants()
    for D in (5_000_000_003,6_000_000_003,8_000_000_003,10_000_000_003,25_000_000_003):
        nag=check(D,M(5)/6,D>=8_000_000_000)
        costa=check(D,M(257)/258,D>=5_000_000_000)
        print('ENDPOINT',D,'Nagura',round(nag[-1],9),'Costa',round(costa[-1],9),flush=True)
        if D==5_000_000_003:
            assert nag[-1]<0  # explicit negative control below Nagura scope
    for D,gamma in ((8_000_000_003,F(5,6)),(5_000_000_003,F(257,258))):
        m=(D+1)//4
        p=int(nextprime((m*gamma.numerator)//gamma.denominator))
        assert p<m and p*gamma.denominator>=m*gamma.numerator
        R,S,rho= p-1,(p-1)//25,radius(D,p)
        L,U=normalized(R,S,rho,4*D)
        assert L>U
        print('ACTUAL_PRIME_PARAMETER',D,p,'gap',float(L-U),flush=True)
    print('PHASE154_PASS: numeric and rational checks, NOT a field-theorem receipt',flush=True)

if __name__=='__main__':
    main()
