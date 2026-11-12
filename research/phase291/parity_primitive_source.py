#!/usr/bin/env python3
"""Phase291-D: source-integral even/odd primitive 5-adic sector audit.

Preregistered at f3dc07d BEFORE this code. Original 700 rows, all
original observation columns, old Frobenius factors counted once.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase281"))
from full_d403_third_layer import smith_profile_k3
from full700_primitive_gate import (
    D,R,S,J,N,QSIZE,source_guard,normalized_original,
    smith_cap,rank_fast,gram_mod_np,parity_check
)
from source_probe import params

P,K=5,9
MOD=P**K
EXPECTED={0:620,1:5,5:15,6:60}
EXPECTED_H={"0":684,"1":15,"2":1,">=3":0}
PHASE281_BLOB="d28b1420a371ca3a8a0297a19ecec75feedfc978"

def sector_primitive(source,rows):
    assert source.shape==(350,2*J*QSIZE)
    levels,hist,prim5,U=smith_cap(source,P,K,include_row_map=True)
    assert len(levels)==350 and max(levels)<K and prim5 is not None
    assert rank_fast(prim5,P)==350
    assert 350*MOD*MOD < (1<<63)
    numer=(U@source)%MOD
    C125=np.zeros_like(source)
    for i,e in enumerate(levels):
        d=P**e
        assert e+3<=K and np.all(numer[i]%d==0)
        C125[i]=(numer[i]//d)%(P**3)
    assert np.array_equal(C125%P,prim5%P)
    assert rank_fast(C125%P,P)==350
    return levels,hist,C125

def positive_operator_counterworld():
    A=np.diag([1,4]).astype(np.int64)
    X=np.array([[0,1],[1,0]],dtype=np.int64)
    assert int(X[0,0]*X[1,1]-X[0,1]*X[1,0])==-1
    assert not np.array_equal(A@X,-(X@A))
    assert np.array_equal((A@X+X@A)%5,np.zeros((2,2),dtype=np.int64))
    # In real SPD, (a_i+a_j)*Y_ij=0 forbids nonzero anticommuters.
    # A mod5 does not retain that ordered-positive spectral fact.
    return True

def main():
    source_guard()
    observed=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase281/full_d403_third_layer.py"],
        cwd=ROOT,text=True).strip()
    assert observed==PHASE281_BLOB
    rho,r,s,j,Q=params(D)
    assert (rho,r,s,j,len(Q))==(51,R,S,J,QSIZE)
    C,F,histk=normalized_original(P,K,Q,True)
    assert F==1300 and histk=={0:160,1:150,2:140,3:130,4:120}
    parity_check(C,P,Q)
    rows_by_parity={}
    old_by_parity={}
    for parity in (0,1):
        group=[r*S+s for r in range(R) for s in range(S)
               if (r+s)%2==parity]
        old=sum(min(r//P,S-1-s) for r in range(R)
                for s in range(S) if (r+s)%2==parity)
        assert len(group)==350 and old==650
        rows_by_parity[parity]=group
        old_by_parity[parity]=old
    assert sorted(rows_by_parity[0]+rows_by_parity[1])==list(range(N))
    assert sum(old_by_parity.values())==1300

    outcomes={}
    completed=[]
    second=Counter()
    htotal=Counter()
    index_sum=0
    for parity in (0,1):
        ids=rows_by_parity[parity]
        levels,sh,Cp125=sector_primitive(C[ids],ids)
        second.update({k:sh.get(k,0) for k in EXPECTED})
        index=sum(levels)
        index_sum+=index
        H=gram_mod_np(Cp125,P**3,D,J*len(Q))
        profile=smith_profile_k3(H,P)
        assert profile[">=3"]==0
        htotal.update(profile)
        hval=profile["1"]+2*profile["2"]
        vp=2*(old_by_parity[parity]+index)+hval
        outcomes["even" if parity==0 else "odd"]={
          "source_rows":len(ids),
          "old_F5":old_by_parity[parity],
          "secondary_index_exact":index,
          "source_Smith_histogram":sh,
          "primitive_rank_mod5":rank_fast(Cp125%P,P),
          "primitive_H_Smith_profile":profile,
          "primitive_H_v5_exact":hval,
          "original_sector_G_v5_exact":vp
        }
        completed.append(Cp125)
    assert dict(sorted(second.items()))==EXPECTED,(second,EXPECTED)
    assert index_sum==440
    assert dict(htotal)==EXPECTED_H,(htotal,EXPECTED_H)

    # Every even/odd original observation pairing vanishes modulo125:
    # this is an ALL 350x350 cross-block check, not sampled zeros.
    B=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    Ce,Co=completed
    cross=((Ce*(B%(P**3)))@Co.T)%(P**3)
    assert cross.shape==(350,350) and np.count_nonzero(cross)==0

    aggregate=sum(outcomes[x]["original_sector_G_v5_exact"]
                  for x in ("even","odd"))
    assert aggregate==3497
    assert positive_operator_counterworld()
    print("PHASE291D_PARITY_PRIMITIVE",{
      "D":D,"original_source_rows":N,"full_original_Q":len(Q),
      "original_observation_columns":C.shape[1],
      "all_ordinary_jets":J,"metric":"2,2D",
      "odd_p_symmetry":"central inversion C2 with Z5-unit half-projectors",
      "even_and_odd_sector_details":outcomes,
      "global_secondary_Smith_profile_reconstructed":dict(second),
      "global_primitive_H_Smith_profile_reconstructed":dict(htotal),
      "all_original_cross_sector_Gram_entries_zero_mod125":True,
      "source_and_primitive_valuation_sum_exact":aggregate,
      "positive_real_operator_can_anticommute_only_AFTER_mod5_reduction":True,
      "no_binary_half_projector_or_extra_inert_factor":True,
      "no_new_discriminant_field_theorem":True
    },flush=True)
    print("PASS Phase291-D original 350+350 parity-integral primitive reconstruction",flush=True)

if __name__=="__main__":
    main()
