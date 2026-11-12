#!/usr/bin/env python3
"""Phase291-B: at original fixed K8, measure 5-adic depth2 primitive pairing.

Preregistered bcbf77a8 AFTER original full-source p5 K8 result but
BEFORE this 700x700 mod25 residual computation. No changed source.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase280"))
from full_d403_second_layer import first_two_smith
from full700_primitive_gate import (
    D,R,S,J,N,QSIZE,source_guard,normalized_original,
    smith_cap,rank_fast,gram_mod_np
)
from source_probe import params

P=5
K=8
MOD=P**K
EXPECTED={0:620,1:5,5:15,6:60}
ORACLE_BLOB="7abffdf4f4916dacef08ebe097e5eed700837ad4"

def main():
    source_guard()
    observed=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase280/full_d403_second_layer.py"],
        cwd=ROOT,text=True).strip()
    assert observed==ORACLE_BLOB
    rho,r,s,j,Q=params(D)
    assert (rho,r,s,j,len(Q))==(51,R,S,J,QSIZE)
    assert (-D)%P==2
    C0,old,histk=normalized_original(P,K,Q,True)
    assert old==1300 and histk=={0:160,1:150,2:140,3:130,4:120}
    levels,hist,Cprim5,U=smith_cap(C0,P,K,include_row_map=True)
    assert hist==EXPECTED and max(levels)==6 and len(levels)==N
    assert sum(levels)==440 and Cprim5 is not None
    assert rank_fast(Cprim5,P)==N
    assert N*MOD*MOD < (1<<63)

    # U*C0 is reconstructed in ORIGINAL observation columns. The
    # internally swapped Smith columns are NOT carried into B.
    numerator=(U@C0)%MOD
    C25=np.zeros(C0.shape,dtype=np.int64)
    for i,e in enumerate(levels):
        d=P**e
        assert e+2<=K
        assert np.all(numerator[i]%d==0)
        C25[i]=(numerator[i]//d)%(P*P)
    assert np.array_equal(C25%P,Cprim5%P)
    assert rank_fast(C25%P,P)==N

    H25=gram_mod_np(C25,P*P,D,J*len(Q))
    H5=gram_mod_np(Cprim5,P,D,J*len(Q))
    assert np.array_equal(H25%P,H5)
    assert rank_fast(H5,P)==684
    assert np.array_equal(H25,H25.T)

    toy=np.diag([1,P,P*P]).astype(np.int64)
    assert first_two_smith(toy,P)=={"0":1,"1":1,">=2":1}
    profile=first_two_smith(H25,P)
    assert profile["0"]==684 and profile["1"]+profile[">=2"]==16
    # A different row / column unimodular change leaves Smith invariant.
    shear=H25.copy()
    shear[0,:]=(shear[0,:]+shear[1,:])%(P*P)
    shear[:,0]=(shear[:,0]+shear[:,1])%(P*P)
    assert np.array_equal(shear,shear.T)
    assert first_two_smith(shear,P)==profile
    assert first_two_smith(H25.T,P)==profile
    n1=profile["1"]
    ng2=profile[">=2"]
    lower=2*(old+sum(levels))+n1+2*ng2
    assert lower==3496+ng2

    print("PHASE291B_FULL700_PRIMITIVE_DEPTH2",{
      "D":D,"original_rows":N,"source_Q":len(Q),
      "all_ordinary_jets":J,"all_original_channels":C25.shape[1],
      "original_metric":"2,2D",
      "previously_counted_old_F5":old,
      "exact_secondary_source_index":sum(levels),
      "max_secondary_level":max(levels),
      "fixed_source_K":K,
      "primitive_precision_proven":2,
      "primitive_C_rank_mod5":rank_fast(C25%P,P),
      "primitive_H_rank_mod5":rank_fast(H25%P,P),
      "primitive_H_5adic_residual_levels_capped2":profile,
      "residual_v5_exact" if ng2==0 else "residual_v5_lower":n1+2*ng2,
      "full_original_v5_exact" if ng2==0 else "full_original_v5_lower":lower,
      "unresolved_primitive_levels_at_2":ng2,
      "historical_phase280_independent_smith_oracle":True,
      "unimodular_shear_profile_invariance":True,
      "no_extra_source_or_Frobenius_counted_twice":True,
      "no_actual_field_theorem":True
    },flush=True)
    print("PASS Phase291-B original full-source fixed-K8 primitive depth2",flush=True)

if __name__=="__main__":
    main()
