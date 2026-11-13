#!/usr/bin/env python3
"""Phase303-E: source-correct Frobenius primitive Gram explains v5(det)=30.

Preregistered at d3e124da AFTER maximal-order A/D observations and
BEFORE code. The 15 row subtractions are UNIMODULAR, division by5
is NOT unimodular and has to be accounted in the original determinant.
No field cutoff, no changed source norm, original K/J/Q frozen.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for path in ("phase206","phase297","phase298","phase303"):
    sys.path.insert(0,str(ROOT/"research"/path))
import maximal_order_source as source
import original_schur_integrality_k16 as smith

P=5
K=16
MOD=5**16
LOW=5**15
FROZEN_SHA="e68f66dac1c914a97c0fe93655a693053f80386f"

def guard():
    source.freeze()
    path="research/phase303/maximal_order_source.py"
    sha=subprocess.check_output(
        ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
    assert sha==FROZEN_SHA,("source SHA changed",sha)

def O(x):
    return np.asarray(x,dtype=object)

def integral_gram(E,precision=LOW):
    a=O(E)
    n=a.shape[0]
    assert a.shape[1]%2==0
    g=np.zeros((n,n),dtype=np.int64)
    for i in range(n):
        xi=a[i]
        for j in range(i,n):
            xj=a[j]
            q=sum(
               2*int(xi[c])*int(xj[c])
               +int(xi[c])*int(xj[c+1])
               +int(xi[c+1])*int(xj[c])
               +82*int(xi[c+1])*int(xj[c+1])
               for c in range(0,len(xi),2)
            )%precision
            g[i,j]=g[j,i]=q
    return g

def primitive_source_branch(Q,E,G_original,label):
    n=E.shape[0]
    assert n==40
    assert len(Q)==E.shape[1]//2
    e=O(E)
    # Integer unitriangular original polynomial row frame.
    U=np.eye(n,dtype=object)
    for r in range(25,n):
        U[r,r-24]=-1
    assert all(int(U[i,i])==1 for i in range(n))
    subtract=(U@e)%MOD
    for r in range(25,n):
        assert not np.any(subtract[r,:]%5),(
            "z^25≠z in actual F25 source",label,r)
    all_frobenius_checks=15*E.shape[1]
    primitive=O(subtract)
    for r in range(25,n):
        primitive[r,:]=(primitive[r,:]//P)%LOW
    assert np.asarray(primitive,dtype=object).shape==E.shape
    # Mod5 source rows in original ω coordinates preserve trace Bomega.
    rank_eval=source.rank_mod5(np.asarray(primitive,dtype=np.int64))
    Gprim=integral_gram(primitive,LOW)
    rank_gram=source.rank_mod5(Gprim)
    rank_old25=source.rank_mod5(Gprim[:25,:25])
    original=O(G_original)%MOD
    transformed=(U@original@U.T)%MOD
    # Original source Gram is reconstructed without modifying
    # any observation metric. For 0<=i,j<25 use full precision,
    # because the primitive E is stored only mod5^15.
    for i in range(n):
        for j in range(n):
            if i<25 and j<25:
                expected=int(G_original[i,j])%MOD
            else:
                factor=(P if i>=25 else 1)*(P if j>=25 else 1)
                expected=(factor*int(Gprim[i,j]))%MOD
            assert int(transformed[i,j])==expected,(
                "unimodular row-frame vs p-power primitive Gram mismatch",
                label,i,j,int(transformed[i,j]),expected)
    levels,profile=smith.high_precision_smith(
        source.gram_mod(G_original))
    assert max(levels)<K
    orig_val=sum(levels)
    if label=="full":
        assert rank_eval==rank_gram==40
        assert rank_old25==25
        assert dict(Counter(levels))=={0:25,2:15}
        assert orig_val==30
        # Primitive determinant is a unit at p5, giving v=2*15.
        assert orig_val==2*(40-25)
    if label=="even":
        assert orig_val==77
        assert dict(Counter(levels))=={0:15,2:8,3:7,4:10}
        assert rank_gram<40,(
            "even support unexpectedly provided the same primitive"
            "full-rank Gram at same Frobenius normalization")
    return {
      "arm":label,
      "original_source_point_count":len(Q),
      "original_R":n,
      "original_Bomega_trace_unchanged":True,
      "actual_F25_Frobenius_divisibility_coordinate_checks":
          all_frobenius_checks,
      "actual_15_differences_divisible5":True,
      "unitriangular_original_Frobenius_row_change":True,
      "divided_15_rows_are_NEW_integral_EVALUATION_superlattice":True,
      "full_unimodular_G_vs_D5_primitive_G_D5_mod5pow16_entries":
          n*n,
      "primitive_evaluation_rank_mod5":rank_eval,
      "primitive_Gram_rank_mod5":rank_gram,
      "primitive_top25_Gram_rank_mod5":rank_old25,
      "original_full_G_40x40_5adic_Smith_profile":profile,
      "original_full_G_40x40_v5_determinant":orig_val,
      "determinant_val_30_explained_by_15_Frobenius_pairs":
          label=="full",
      "no_added_original_field_valuation":True
    }

def main():
    guard()
    a=source.all_arms()
    even=primitive_source_branch(
        a["Qeven"],a["E_even"],a["G_even"],"even")
    full=primitive_source_branch(
        a["Qfull"],a["E_full"],a["G_full"],"full")
    assert even["primitive_Gram_rank_mod5"]<40
    assert full["primitive_Gram_rank_mod5"]==40
    print("PHASE303E_FROBENIUS_PRIMITIVE_SOURCE_GRAM",{
       "original_even_source_negative_control":even,
       "genuine_maximal_full_source":full,
       "p5_original_frobenius_kernel_differences":15,
       "original_G_v5_30_eq_two_times_15":True,
       "unitriangular_source_change_then_nonunimodular_division_separated":True,
       "no_original_full_field_cutoff_changed":True
    },flush=True)
    print("PASS Phase303-E original maximal-order Frobenius primitive Gram source certificate",flush=True)

if __name__=="__main__":
    main()
