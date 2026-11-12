#!/usr/bin/env python3
"""Phase291-C: full 700-row primitive H modulo 125 at preregistered K=9.

Post-result preregistration at ce01409e; frozen source/rows/jets/metric,
no new field theorem, never add unsaturated Gram radical.
"""
from pathlib import Path
import subprocess
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase281","phase280"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from full_d403_third_layer import smith_profile_k3
from full_d403_second_layer import first_two_smith
from full700_primitive_gate import (
    D,R,S,J,N,QSIZE,source_guard,normalized_original,
    smith_cap,rank_fast,gram_mod_np,exact_source_oracle
)
from source_probe import params

P,K=5,9
EXPECTED={0:620,1:5,5:15,6:60}
EXPECTED_H25={"0":684,"1":15,">=2":1}
PHASE281_BLOB="d28b1420a371ca3a8a0297a19ecec75feedfc978"

def main():
    source_guard()
    actual=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase281/full_d403_third_layer.py"],
        cwd=ROOT,text=True).strip()
    assert actual==PHASE281_BLOB
    rho,r,s,j,Q=params(D)
    assert (rho,r,s,j,len(Q))==(51,R,S,J,QSIZE)
    assert (-D)%P==2 and (2*D)%P==1
    C0,F,oldhist=normalized_original(P,K,Q,True)
    assert F==1300 and oldhist=={0:160,1:150,2:140,3:130,4:120}
    checked=exact_source_oracle(C0,P,K,Q,True)
    assert checked==480
    levels,hist,Cp5,U=smith_cap(C0,P,K,include_row_map=True)
    assert hist==EXPECTED and len(levels)==N and max(levels)==6
    assert sum(levels)==440 and Cp5 is not None
    assert rank_fast(Cp5,P)==N
    mod=P**K
    assert N*mod*mod < (1<<63)
    V=(U@C0)%mod
    Cp125=np.zeros(C0.shape,dtype=np.int64)
    for i,v in enumerate(levels):
        d=P**v
        assert v+3<=K and np.all(V[i]%d==0)
        Cp125[i]=(V[i]//d)%(P**3)
    assert np.array_equal(Cp125%P,Cp5%P)
    assert rank_fast(Cp125%P,P)==N

    H125=gram_mod_np(Cp125,P**3,D,J*len(Q))
    assert np.array_equal(H125,H125.T)
    assert rank_fast(H125%P,P)==684
    h25=first_two_smith(H125%(P*P),P)
    assert h25==EXPECTED_H25,(h25,EXPECTED_H25)
    toy=np.diag([1,P,P*P,P**3]).astype(np.int64)
    assert smith_profile_k3(toy,P)=={"0":1,"1":1,"2":1,">=3":1}

    profile=smith_profile_k3(H125,P)
    assert profile["0"]==684 and profile["1"]==15
    assert profile["2"]+profile[">=3"]==1
    shear=H125.copy()
    shear[0,:]=(shear[0,:]+shear[1,:])%(P**3)
    shear[:,0]=(shear[:,0]+shear[:,1])%(P**3)
    assert np.array_equal(shear,shear.T)
    assert smith_profile_k3(shear,P)==profile
    assert smith_profile_k3(H125.T,P)==profile

    residual=profile["1"]+2*profile["2"]+3*profile[">=3"]
    vp=2*(F+sum(levels))+residual
    assert vp==3497+profile[">=3"]
    exact=profile[">=3"]==0
    print("PHASE291C_FULL700_PRIMITIVE_DEPTH3",{
       "D":D,"source_Q":len(Q),"full_original_rows":N,
       "original_observation_columns":C0.shape[1],
       "all_ordinary_jets":J,"original_metric":"2,2D",
       "fixed_K_secondary":K,"max_secondary_e":max(levels),
       "primitive_precision":3,
       "previous_F_counted_once":F,"secondary_index_exact":sum(levels),
       "primitive_C_full_rank_mod5":rank_fast(Cp125%P,P)==N,
       "primitive_H_mod5_rank":rank_fast(H125%P,P),
       "replayed_previous_H25_profile":h25,
       "new_primitive_H125_Smith_levels":profile,
       "primitive_H_v5_exact" if exact else "primitive_H_v5_lower":residual,
       "original_G_v5_exact" if exact else "original_G_v5_lower":vp,
       "unresolved_primitive_levels_ge3":profile[">=3"],
       "independent_preexisting_Phase281_Smith":True,
       "invariant_under_unimodular_shear_and_transpose":True,
       "original_integer_jet_oracle_checks":checked,
       "no_field_cutoff_or_extra_prime_added":True
    },flush=True)
    print("PASS Phase291-C fixed-K9 original full primitive mod125 test",flush=True)

if __name__=="__main__":
    main()
