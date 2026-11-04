#!/usr/bin/env python3
"""Phase208-A POST-RESULT safe layer cake from an explicit sparse row map.

The sparse trial residual can have eigenvalues >1. Do NOT claim that
-sum(log(trial eigenvalues)) is a positive lower. Use Nopt>=Ntrial
and integrate NONNEGATIVE optimal-mode counts instead. Issue #150
records this correction before implementation.
"""
from fractions import Fraction as F
from sparse_schur_map import run

def check():
    a=run(283)
    assert all(v["trial"]==0 for v in a["counts"].values())
    b=run(403)
    counts=b["counts"]
    labels=("1/2","1/8","1/1024")
    trial=[counts[k]["trial"] for k in labels]
    optimal=[counts[k]["optimal"] for k in labels]
    assert trial==[47,32,7] and optimal==[65,33,12]
    assert all(t<=o for t,o in zip(trial,optimal))
    # On [0,ln2), [ln2,3ln2), [3ln2,10ln2),
    # N_opt(e^-x)>=N_trial at lower threshold of that band.
    bands=trial[0]+2*trial[1]+7*trial[2]
    assert bands==160
    # ln2 > 56/81 (strict, 2-term artanh(1/3) lower).
    lower=F(56*bands,81)
    normalized=lower/F(b["R"]**2*b["S"])
    assert lower==F(8960,81)
    assert normalized==F(28,10125)
    print("SAFE_SPARSE_LAYER_CAKE",{
        "D":403,"trial_counts":trial,"optimal_counts":optimal,
        "safe_log_floor":str(lower),"normalized_floor":str(normalized),
        "claim_is_about_OPTIMAL_log_saving_not_trial_log":True,
        "source_map_is_explicit_and_sparse":True,
        "uniform_D_lower_bound":False},flush=True)
    print("PASS Phase208 safe sparse map post-result layer cake",flush=True)

if __name__=="__main__":check()
