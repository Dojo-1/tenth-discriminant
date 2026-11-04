#!/usr/bin/env python3
"""Phase207-A post-result classical layer-cake deduction (Issue #146).

Recomputes frozen exact source Schur inertia, not a new preregistered
numerical experiment; no full Gram determinant or new matching.
"""
from fractions import Fraction as Q
from full_schur_spectrum import run

def certified_band_lower(result):
    c=result["counts"]
    # PREVIOUSLY registered/observed θ = 2^-1,2^-3,2^-6,2^-10.
    thresholds=("1/2","1/8","1/64","1/1024")
    numbers=[c[x] for x in thresholds]
    assert all(a>=b for a,b in zip(numbers,numbers[1:]))
    # L = int_0^∞ N(e^-t) dt >= (N1+2N2+3N3+4N4)*ln(2).
    bands=sum(width*value for width,value in zip((1,2,3,4),numbers))
    # Exact STRICT inequality ln(2)>2*(1/3+1/81)=56/81
    # from atanh(1/3)=sum_{h>=0}1/[(2h+1)*3^(2h+1)].
    rational_lower=Q(56*bands,81)
    normalized=rational_lower/Q(result["R"]**2*result["S"])
    return bands,rational_lower,normalized

def main():
    a=run(283)
    z,lower,norm=certified_band_lower(a)
    assert z==0 and lower==0
    b=run(403)
    z,lower,norm=certified_band_lower(b)
    assert z==251 and lower==Q(14056,81)
    # Compare rationally with the HISTORICAL conditional research target.
    old_target=Q(43,10000)
    assert norm>old_target
    assert 14056*10000>43*81*40000
    print("POST_RESULT_LAYER_CAKE",{
        "D":403,"registered_4_threshold_counts":[b["counts"][n] for n in
             ("1/2","1/8","1/64","1/1024")],
        "lower_bound_in_units_of_ln2":z,
        "strict_rational_log_saving_floor":str(lower),
        "strict_normalized_floor":str(norm),
        "above_historical_0_0043_at_this_D":True,
        "entire_original_Gram_det_NOT_used":True,
        "uniform_D_theorem":False},flush=True)
    print("PASS post-result finite exact Schur layer-cake deduction",flush=True)

if __name__=="__main__":main()
