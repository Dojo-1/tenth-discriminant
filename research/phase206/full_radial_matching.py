#!/usr/bin/env python3
"""Phase206-A prereg #142: fixed exhaustive parity-separated Fischer matching.

It does not search or reorder pairs to maximize observed savings.
All ordinary derivative j<S, original Q and original trace metric.
"""
from source_probe import params,fibers,pair_data

def run(D):
    rho,R,S,J,Q=params(D)
    ds=list(range(1-S,R))
    parity=[[d for d in ds if d%2==k] for k in (0,1)]
    pairs=[(q[i],q[i+1]) for q in parity for i in range(0,len(q)-1,2)]
    assert len(set(d for x in pairs for d in x))==2*len(pairs)
    logs=[];covered=0
    for d,e in pairs:
        assert e==d+2
        (a,b),_,_,_,gain=pair_data(D,Q,R,S,J,d)
        assert gain>=-1e-7
        logs.append(max(0.,gain));covered+=a+b
    result={'D':D,'rho':rho,'R':R,'S':S,'J':J,'Q':len(Q),
       'pairs':len(pairs),'covered_rows':covered,'total_rows':R*S,
       'gain_min':min(logs),'gain_max':max(logs),'sum_log_gain':sum(logs),
       'normalized':sum(logs)/(R*R*S)}
    print('FIXED_FULL_MATCHING',result,flush=True)
    if D==283:
        assert len(pairs)==35 and covered==138
        assert abs(result['normalized']-0.0026746620876993534)<1e-10
    if D==403:
        assert len(pairs)==51 and covered==398
        assert abs(result['normalized']-0.0068646046855468275)<1e-10

if __name__=='__main__':
    run(283);run(403)
    print('PASS fixed complete matching, no uniform constant claimed')
