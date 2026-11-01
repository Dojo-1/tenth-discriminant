#!/usr/bin/env python3
"""Phase153: source-matched scalar audit for a conditional 25b field-bound candidate.

No new field theorem is proved by this executable. The all-D argument and
remaining Lean/human reconstruction gates are in PHASE153_BERTRAND_CANDIDATE.md.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
from mpmath import mp
from sympy import prevprime

mp.dps=75
F=mp.mpf
T=25_000_000_000
FAC=F(8646130782816)/10**12
LIN=F(6856198325360)/10**12
SQ=F(133259338177)/10**12
ERR=F(9892590181957053)/10**12
I=F(9210440367148)/10**12/10000+F(99995001)/10**12

def source_correspondence():
    root=Path(__file__).resolve().parents[2]
    files={
      'constants':('lean/TenthDiscriminant/PrimeLogConstants.lean',
                   ('8646130782816 / 1000000000000','6856198325360 / 1000000000000',
                    '133259338177 / 1000000000000','9892590181957053 / 1000000000000')),
      'tail':('lean/TenthDiscriminant/FirstIntervalScalars.lean',
              ('9210440367148 / 1000000000000','99995001 / 1000000000000')),
      'lower':('lean/TenthDiscriminant/NormalizedComparison.lean',
               ('def rawPrimeMassLower','theorem rawPrimeMassLower_normalized',
                'def comparisonScale (R S : Nat) : Real := (R : Real)^2 * S')),
      'upper':('lean/TenthDiscriminant/EnderUpperB.lean',
               ('noncomputable def enderUpperB','(R : Real) * S * Real.log (2 * n * J)')),
      'positivity':('lean/TenthDiscriminant/RadialCutoff.lean',
                    ('theorem prime_mass_log_lower_of_det_pos',))}
    for label,(path,needles) in files.items():
        data=(root/path).read_text()
        for needle in needles:assert needle in data,(label,needle)
    print('PASS frozen original-Lean coefficient and formula correspondence',flush=True)

def radius(D,p):
    d=F(D)
    return int(mp.ceil(mp.sqrt(d+1)/2+mp.sqrt(F(p)*mp.sqrt(d)/3)))

def normalized(R,S,rho,n):
    r=F(R);s=F(S);h=F(rho);n=F(n)
    c=1-1/(2*s)
    lower=(c*((1-1/r)**2*(mp.log(r-1)-F('1.5'))+(r-F('0.5'))/r**2)
          -c*(1-1/r)*(FAC+I-LIN)-2*c*ERR/r
          -(r-1)*(2*r-1)/(6*r*s)*(SQ+I))
    upper=(mp.log(2*n*s)/r+(1-s/r)*mp.log(h)
           +2*(s-1)/r*(mp.log(r)-1)
           +2*(s-1)/r**2*(h+mp.log(r/h)))
    # Independently assemble the ACTUAL source expressions before normalizing.
    v=r-1
    factorial=v*v/2*mp.log(v)-3*v*v/4+v/2+F('0.25')
    tri=r*(r-1)/2
    square=r*(r-1)*(2*r-1)/6
    directL=(2*(s-F('0.5'))*factorial
           -2*(s-F('0.5'))*tri*(FAC+I-LIN)
           -2*(s-F('0.5'))*r*ERR-square*(SQ+I))/(r*r*s)
    directU=(r*s*mp.log(2*n*s)+2*mp.log(h)*(s*r*(r-1)/2+r*s*(s-1)/2)
           +2*s*(s-1)*(r*mp.log(r/h)-r+h+mp.log(r/h)))/(r*r*s)
    assert abs(lower-directL)<F('1e-45')
    assert abs(upper-directU)<F('1e-45')
    return lower,upper

def rational_gates():
    # The following checks validate NUMERICAL CONSTANTS of explicit universal
    # paper inequalities; they do not themselves prove the algebraic estimates.
    assert 395**4<T and 50_000**2<3_000_000_000
    assert Q(49,20)**2>6 and Q(49,10)**2>24
    assert Q(49,20)/395*(1+Q(1,2*T))+Q(49,10)/395**3<Q(1,160)
    assert Q(161,160)*Q(20,69)*(1+Q(1,2*T))<Q(293,1000)
    assert Q(293,1000)*8/(395*(1-Q(8,T)))<Q(6,1000)
    cost=(Q(3,2)+Q(1,3_000_000_000-1)+Q(15,50_000)
          +Q(1791,1000)+Q(2*9893,3_000_000_000)
          +(Q(25)+Q(25,100_000_000))/3*Q(134281,1000000))
    assert cost<Q(4411,1000),cost
    residual=(Q(18,150_000)+Q(9,150_000)
              +Q(2,25)*(Q(6,1000)+Q(1,50_000))+Q(1,6_000_000_000))
    assert residual<Q(1,1000),residual
    assert mp.log(3)>F('1.09') and mp.log(8)<F('2.08') and mp.log(T)>F('23.9')
    gap=Q(1,5)*Q(239,10)-Q(44,100)*Q(208,100)-Q(3815,1000)-Q(1,1000000)
    assert gap>Q(4,100)
    print('PASS exact rational coefficient gates; symbolic gap target >',float(gap),flush=True)

def check_case(D,p,required=True):
    R=p-1;S=R//25;rho=radius(D,p)
    assert R>rho>5 and 25*S<=R<=26*S
    lower,upper=normalized(R,S,rho,4*D)
    if required:
        assert lower>=mp.log(R)-F('4.411')
        assert upper<=F('0.24')*mp.log(D)+F('0.56')*mp.log(R)-F('0.596')
        assert lower>upper
    return R,S,rho,float(lower),float(upper),float(lower-upper)

def main():
    source_correspondence()
    rational_gates()
    for D in (25_000_000_003,30_000_000_003,41_006_250_003,100_000_000_003):
        m=(D+1)//4
        for ratio in (F('0.50000001'),F('0.6'),F('0.83333334'),F('0.95'),F('0.99999')):
            p=int(mp.floor(m*ratio))  # NOT necessarily prime: ANALYTIC ENVELOPE stress test only.
            v=check_case(D,p)
            if ratio in (F('0.50000001'),F('0.83333334'),F('0.99999')):
                print('ENVELOPE',D,float(ratio),'rho',v[2],'gap',round(v[-1],9),flush=True)
    D=15_000_000_003;m=(D+1)//4
    assert check_case(D,m//2+1,False)[-1]<0  # boundary failure below T
    D=41_006_250_003;m=(D+1)//4
    p=int(prevprime(m))
    assert m/2<p<m  # not asserted inert for this ACTUAL D
    R,S,rho,L,U,gap=check_case(D,p)
    oldrho=int(mp.ceil(F(13)/25*F(D)**F('0.75')))
    _,oldU=normalized(R,S,oldrho,4*D)
    assert U<float(oldU) and gap>0.47
    print('MATCHED ORIGINAL GRAM',dict(D=D,p=p,R=R,S=S,rho=rho,oldrho=oldrho,
        lower=L,upper=U,gap=gap,matched_old_upper=float(oldU)),flush=True)
    print('PHASE153_BUDGET_PILOT_PASS: P-paper envelope candidate, no Lean field theorem',flush=True)

if __name__=='__main__':main()
