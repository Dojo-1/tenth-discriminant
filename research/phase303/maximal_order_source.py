#!/usr/bin/env python3
"""Phase303 A+B: genuine maximal-order D163 source vs original even suborder.

Preregistered f3eccd01 BEFORE implementation/results. Original rho21,
R40/S=J1, 40 unchanged Z^r monomial rows, squared norm cutoff441.
No replacement of the repo's integer-order result. Rerun via GitHub CI.
"""
from collections import Counter
from math import isqrt
from pathlib import Path
import json
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase297","phase298","phase303"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from source_probe import params,gram as legacy_gram
import class_one_d163_composition as previous
import original_schur_integrality_k16 as smith

D=163
P=5
K=16
MOD=P**K
R=40
RHO=21
BOMEGA=np.asarray([[2,1],[1,82]],dtype=np.int64)
BOLD=np.asarray([[2,0],[0,326]],dtype=np.int64)
T=np.asarray([[1,-1],[0,2]],dtype=np.int64)
FROZEN={
  "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
  "research/phase298/class_one_d163_composition.py":"e8cae60a662ca59cade8acd741c2d5d4f4982d6a",
}

def freeze():
    previous.guard()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
        assert actual==sha,("old original source drift",path,actual,sha)

def mul(x,y):
    a,b=x;c,d=y
    return (a*c-41*b*d, a*d+b*c+b*d)

def conjugate(z):
    a,b=z
    return (a+b,-b)

def norm(z):
    a,b=z
    return a*a+a*b+41*b*b

def trace(z):
    a,b=z
    return 2*a+b

def pairing(u,v):
    a,b=u;c,d=v
    return 2*a*c+a*d+b*c+82*b*d

def qmax():
    Q=[]
    # Since N=(a+b/2)^2+163 b²/4≤441, |b|≤3 and
    # |a|≤sqrt441+|b|/2<25. The enumeration is EXHAUSTIVE.
    assert 163*4*4>4*(RHO*RHO)
    for b in range(-3,4):
        for a in range(-25,26):
            if norm((a,b))<=RHO*RHO:
                Q.append((a,b))
    assert len(Q)==len(set(Q))
    assert all(norm(q)<=441 for q in Q)
    assert all(norm((26,b))>441 and norm((-26,b))>441
               for b in range(-3,4))
    return Q

def pows(q):
    out=[(1,0)]
    for r in range(1,R):
        out.append(mul(out[-1],q))
    return out

def independent_maximal_gram(Q,label):
    # Direct coordinate trace and separately a multiplicative trace
    # moment oracle. They share the source points/powers but NOT the
    # underlying Gram contraction code.
    powers=[pows(q) for q in Q]
    G=np.zeros((R,R),dtype=object)
    moment=np.zeros((R,R),dtype=object)
    E=np.zeros((R,2*len(Q)),dtype=np.int64)
    for qi,power in enumerate(powers):
        for r,(a,b) in enumerate(power):
            E[r,2*qi]=a%MOD
            E[r,2*qi+1]=b%MOD
    for r in range(R):
        for s in range(r,R):
            direct=sum(pairing(power[r],power[s])
                       for power in powers)
            moment_value=sum(trace(mul(power[r],conjugate(power[s])))
                             for power in powers)
            assert direct==moment_value,(
                "maximal trace vs multiplicative moment fail",label,r,s)
            G[r,s]=G[s,r]=direct
            moment[r,s]=moment[s,r]=moment_value
    assert np.array_equal(G,G.T)
    assert np.array_equal(G,moment)
    assert len(Q)>=R
    # Bomega is positive definite over reals, and polynomial degree
    # <=39 cannot vanish at >=40 distinct quadratic algebra points.
    # Hence the real Gram is PD (independent of its p-adic defects).
    assert int(BOMEGA[0,0])>0
    assert int(np.linalg.det(BOMEGA))==D
    return G,E,{
      "arm":label,
      "source_points":len(Q),
      "all_1600_exact_integer_Gram_cells_compared":True,
      "maximal_source_trace_and_multiplicative_moment_agree":True,
      "original_rho":RHO,
      "original_monomial_rows":R,
      "original_jet_count":1,
      "trace_Bomega":BOMEGA.tolist(),
      "source_real_positive_definite_by_polynomial_root_argument":True
    }

def rank_mod5(M):
    """Independent small F5 Gaussian elimination, NOT p16 Smith."""
    mat=[[int(y)%P for y in row] for row in M]
    if not mat:return 0
    h=len(mat);w=len(mat[0]);rank=0
    for col in range(w):
        pivot=next((i for i in range(rank,h) if mat[i][col]%P),None)
        if pivot is None:continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        u=pow(mat[rank][col],-1,P)
        for j in range(col,w):mat[rank][j]=mat[rank][j]*u%P
        for i in range(rank+1,h):
            c=mat[i][col]
            if c:
                for j in range(col,w):
                    mat[i][j]=(mat[i][j]-c*mat[rank][j])%P
        rank+=1
        if rank==h:break
    return rank

def gram_mod(G):
    return np.asarray(np.asarray(G,dtype=object)%MOD,dtype=np.int64)

def rank_profile(G,E,Q,label,expected_residues):
    residues={(a%P,b%P) for a,b in Q}
    assert len(residues)==expected_residues,(
        "source residue support prereg count failed",label,len(residues))
    assert all(((a+b)%P,(-b)%P) in residues for a,b in residues)
    rankE=rank_mod5(E)
    assert rankE==expected_residues,(
        "finite field polynomial evaluation rank disagrees",label,rankE)
    g=gram_mod(G)
    grank=rank_mod5(g)
    full_levels,full_hist=smith.high_precision_smith(g)
    censored=max(full_levels)>=K
    return {
       "arm":label,
       "finite_support_points":len(Q),
       "distinct_F25_source_residue_classes":len(residues),
       "F5_original_monomial_evaluation_rank":rankE,
       "F5_original_Gram_rank":grank,
       "full_40_row_p16_censored":censored,
       "full_40_row_p16_Smith_histogram":full_hist,
       "full_40_row_Gram_det_v5_if_uncensored":
           None if censored else sum(full_levels),
       "source_order_layer_histogram":
           dict(sorted(Counter(b for a,b in Q).items()))
    }

def prefix_debts(G):
    g=gram_mod(G)
    result=[]
    for n in range(1,R):
        A=g[:n,:n]
        C=g[:n,n:n+1]
        ea,ha=smith.high_precision_smith(A)
        eb,hb=smith.high_precision_smith(
            np.concatenate([A,C],axis=1))
        censored=max(ea)>=K
        if not censored:
            assert all(y<=x for x,y in zip(ea,eb))
            delta=sum(ea)-sum(eb)
            assert delta>=0
        else:delta=None
        result.append({
           "new_original_monomial_row_power":n,
           "original_prefix_Gram_censored":censored,
           "original_source_cross_cokernel_index_log5":
                delta,
           "original_Gram_max_old_grade_capped16":max(ea)
        })
        if n in (13,18,22,25,33,34,38):
            print("PHASE303_PREFIX_CROSS",{
               "new_row":n,"cross_cokernel_log5":delta,
               "censored":censored},flush=True)
    return result

def all_arms():
    rho,Rp,S,J,Qold=params(D)
    assert (rho,Rp,S,J,len(Qold))==(RHO,R,1,1,109)
    Tobj=np.asarray(T,dtype=object)
    assert np.array_equal(T.T@BOMEGA@T,BOLD)
    assert int(np.linalg.det(T))==2
    Qfull=qmax()
    Qeven=[q for q in Qfull if q[1]%2==0]
    Qodd=[q for q in Qfull if q[1]%2!=0]
    translated=[(x-y,2*y) for x,y in Qold]
    assert Qeven==translated,(
        "even maximal source is NOT exact original source image",
        len(Qeven),len(translated))
    assert set(Qodd).isdisjoint(set(Qeven))
    assert Qodd
    legacy_exact=legacy_gram(D,Qold,1,[(r,0) for r in range(R)])
    G_even,E_even,e_meta=independent_maximal_gram(Qeven,"maximal_even_control")
    G_full,E_full,f_meta=independent_maximal_gram(Qfull,"maximal_full")
    assert all(int(G_even[i,j])==int(legacy_exact[i][j])
               for i in range(R) for j in range(R))
    # More stringent: every original coordinate of EVERY 40 monomial
    # evaluation row transported under T exactly, modulo5^16.
    _,E_old,_,legacy_source=previous.original_j1_source()
    assert E_old.shape==(R,218)
    raw_coordinate_checks=0
    for r in range(R):
        for k in range(len(Qold)):
            a=int(E_old[r,2*k]);b=int(E_old[r,2*k+1])
            assert int(E_even[r,2*k])==(a-b)%MOD
            assert int(E_even[r,2*k+1])==(2*b)%MOD
            raw_coordinate_checks+=2
    return {
        "Qold":Qold,"Qeven":Qeven,"Qfull":Qfull,"Qodd":Qodd,
        "G_even":G_even,"G_full":G_full,
        "E_even":E_even,"E_full":E_full,
        "source_metadata":{
           "rho":rho,"R":Rp,"S":S,"J":J,
           "legacy_original_Q":len(Qold),
           "maximal_even_Q":len(Qeven),
           "maximal_new_odd_b_Q":len(Qodd),
           "maximal_full_Q":len(Qfull),
           "index_two_order_coordinate_matrix":T.tolist(),
           "original_B_old":BOLD.tolist(),
           "maximal_Bomega":BOMEGA.tolist(),
           "B_transport_exact_all_entries":True,
           "T_unit_in_Z5_but_not_unimodular_over_Z":True,
           "every_original_even_support_Gram_entry_equal":1600,
           "raw_legacy_to_even_jet_coordinate_checks":raw_coordinate_checks,
           "maximal_even_independent_oracles":e_meta,
           "maximal_full_independent_oracles":f_meta,
           "legacy_source_independent_oracle":legacy_source
        }
    }

def hostile_source_enlargement():
    # E=[1,2] with trace weights diag(2,2): Gram 10 v5=1.
    # Add a source column e=1 with same weight2: Gram 12 v5=0.
    old=2*(1+4);aug=old+2
    assert old==10 and aug==12
    assert old%P==0 and aug%P!=0
    return {
       "old_real_positive_Gram":old,"augmented_real_positive_Gram":aug,
       "v5_old":1,"v5_augmented":0,
       "adding_original_observation_columns_not_Gram_v5_monotone":True,
       "evaluation_image_can_only_enlarge_under_extra_columns":True
    }

def main():
    freeze()
    a=all_arms()
    even=a["Qeven"];full=a["Qfull"]
    evenp=rank_profile(a["G_even"],a["E_even"],even,
                       "maximal_even",15)
    fullp=rank_profile(a["G_full"],a["E_full"],full,
                       "maximal_full",25)
    print("PHASE303_SOURCE_RANK_RESULT",{
        "source_even":evenp,"source_full":fullp,
        "original_exact_coordinate_transport":a["source_metadata"],
        "positive_definite_counterworld":hostile_source_enlargement()
    },flush=True)
    old_debts=prefix_debts(a["G_even"])
    full_debts=prefix_debts(a["G_full"])
    old_first=[n for n,rec in enumerate(old_debts,1)
               if rec["original_source_cross_cokernel_index_log5"]]
    full_first=[n for n,rec in enumerate(full_debts,1)
                if rec["original_source_cross_cokernel_index_log5"]]
    # The 38 previous original prefix cases 1..38 had exactly seven
    # NONintegral steps; 39 is a new measurement, not a prediction.
    assert [n for n in old_first if n<=38]==[
        13,18,22,25,33,34,38]
    def counts(records):
        return {
          "fully_resolved_39_stage_count":
            sum(not r["original_prefix_Gram_censored"] for r in records),
          "censored_stage_count":
            sum(r["original_prefix_Gram_censored"] for r in records),
          "all_observed_nonintegral_new_original_monomial_powers":
            [r["new_original_monomial_row_power"] for r in records
             if r["original_source_cross_cokernel_index_log5"] is not None
             and r["original_source_cross_cokernel_index_log5"]>0],
          "all_39_actual_prefix_stage_records":records
        }
    print("PHASE303_ALL_SOURCE_PROFILES_AND_ORIGINAL_PREFIXES",{
      "field_D":D,
      "old_integer_order_source":counts(old_debts),
      "maximal_order_full_source":counts(full_debts),
      "even_and_full_maximal_Gram_source_rank":{
          "even":evenp,"full":fullp
      },
      "maximal_source_new_points_are_odd_b":len(a["Qodd"]),
      "NO_new_original_field_cutoff_or_Gram_mass_claim":True,
      "same_norm_cutoff_same_original_40_monomial_rows":True
    },flush=True)
    print("PASS Phase303 maximal order matched source transport and full support Gram/rank",flush=True)

if __name__=="__main__":
    main()
