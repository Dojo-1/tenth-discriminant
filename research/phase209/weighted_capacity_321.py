#!/usr/bin/env python3
"""Phase209-B/C: exact rational weighted column capacity and 321^4 margin.

No imported math computation; the generic inequalities are separately
proved in the Phase209 dossier and need Lean source bridging.
"""
from fractions import Fraction as F
from math import log

def min_cost(N,J,n,p):
    assert N>0 and J>0 and 0<=n<=N*J
    q,r=divmod(n,N)
    val=N*sum(j//(p*p) for j in range(q))+r*(q//(p*p))
    actual=sum(sorted([j//(p*p) for j in range(J) for _ in range(N)])[:n])
    assert val==actual
    # Count number of columns of valuation >= each level.
    layers=sum(max(0,n-N*(p*p)*h) for h in range(1,J//(p*p)+2))
    assert layers==val,(p,N,J,n,layers,val)
    assert F(val)>=F(n*(n-N),2*N*p*p)-n
    return val

def capacity_oracle():
    count=0
    for p in (3,5):
        for N in range(1,11):
            for J in (1,2,p*p-1,p*p,p*p+1,2*p*p+1):
                for n in range(1,J*N+1):
                    min_cost(N,J,n,p)
                    count+=1
    print("PHASE209_WEIGHTED_CAPACITY",{"bounded_cases":count,
        "first_n_minimum_exact":True,
        "layer_cake_formula_exact":True,
        "coarse_lower_Fraction":True},flush=True)

def endpoint_321():
    fourth_root=321;D=fourth_root**4;x=F(fourth_root)
    # Existing proven source: Q <= pi*rho^2/sqrtD+2rho+2floor(rho/sqrtD)+1.
    # Use pi <=22/7, rho<=11/25*x^3+1, sqrtD=x^2 and x>=321.
    Q_over_D=F(22,7)*(F(11,25)+1/x**3)**2+F(22,25)/x+3/x**4+F(22,25)/x**3+2/x**6
    assert Q_over_D<F(31,50)
    # For D>=321^4, R=floor(D/4)>=D/5,
    # S=floor(R/25)>=D/101, so S/N>=50/(31*101).
    S_over_N=F(50,31*101)
    # Old original-source baseline, with rational bounds already in Lean:
    # log3 >=1.098, log5>=1.609, log3<=1.10, log5<=1.61
    bonus=S_over_N*(F(1098,9000)+F(1609,25000))-F(5,D)*(
        (2+F(1,9))*F(11,10)+(2+F(1,25))*F(161,100))
    # Fourth-root321: logD >=4*5.7714 and log2 >=0.6931.
    u=4*F(57714,10000)
    old=(F(999997,1000000)-F(4,5))*u-F(57193,10000)+F(1853,2000)+F(6931,40000)
    margin=bonus+old
    assert old<0<bonus and margin>F(1,2000)
    print("PHASE209_EXACT_321_ENVELOPE",{
       "root":321,"D":D,
       "old_L_minus_U_rational":str(old),"old_gap":float(old),
       "Q_upper_ratio":str(Q_over_D),"Q_upper_decimal":float(Q_over_D),
       "frozen_Q_ratio":str(F(31,50)),
       "new_normalized_bonus_lower":str(bonus),
       "bonus_decimal":float(bonus),
       "conditional_margin_lower":str(margin),
       "margin_decimal":float(margin),"strictly_above_1_over_2000":True,
       "source_domain_321_not_yet_formal":True},flush=True)

if __name__=="__main__":
    capacity_oracle()
    endpoint_321()
    print("PASS Phase209 exact capacity and rational conditional endpoint",flush=True)
