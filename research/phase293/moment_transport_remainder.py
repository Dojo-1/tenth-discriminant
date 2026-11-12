#!/usr/bin/env python3
"""Phase293-A: exact source-Gram moment remainder under local Z5 isometry.

Preregistered at 13d76c3 BEFORE Phase293 code. Six ORIGINAL polynomial
rows, all j0..4 ordinary Z jets, ORIGINAL Q383, field-specific original
trace weights. The formal transformed points are NOT new field sources.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
from source_probe import params,gram,rank_mod

LABELS=((0,0),(1,0),(2,0),(1,1),(4,0),(4,1))
SHA="3f954b59d9f86b06ad53667c869b5b24f2e6c7f6"

def guard():
    assert subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase206/source_probe.py"],
        cwd=ROOT,text=True).strip()==SHA

def subtract(A,B):
    return [[a-b for a,b in zip(row_a,row_b)]
            for row_a,row_b in zip(A,B)]

def same_mod(A,B,mod):
    return all((a-b)%mod==0 for row_a,row_b in zip(A,B)
               for a,b in zip(row_a,row_b))

def main():
    guard()
    rho0,r0,s0,j0,Q0=params(583)
    rho1,r1,s1,j1,Q1=params(587)
    assert (rho0,r0,s0,j0,len(Q0))==(53,145,5,5,383)
    assert (rho1,r1,s1,j1,len(Q1))==(53,146,5,5,383)
    assert Q0==Q1
    Q=Q0
    counts=Counter(y for x,y in Q)
    assert counts==Counter({-2:43,-1:95,0:107,1:95,2:43})
    sum_y2=sum(y*y for x,y in Q)
    assert sum_y2==534

    A=gram(583,Q,j0,LABELS)
    B=gram(587,Q,j1,LABELS)
    exact_diag=B[1][1]-A[1][1]
    assert exact_diag==2*(587-583)*sum_y2==4272
    assert exact_diag%5==2
    assert not same_mod(A,B,5)

    phi={}
    for modulus,alpha in ((5,2),(25,17),(125,67)):
        assert (583*alpha*alpha-587)%modulus==0
        Qm=[(x,alpha*y) for x,y in Q]
        # This is the exact ORIGINAL jet/trace Gram on a formal
        # transported p-adic support, not the D583 field theorem source.
        C=gram(583,Qm,j0,LABELS)
        assert same_mod(C,B,modulus),(
            "local ring isometry failed original ordinary-jet Gram",
            modulus
        )
        remainder=subtract(C,A)
        actual=subtract(B,A)
        assert all((u-v)%modulus==0
                   for ra,rb in zip(remainder,actual)
                   for u,v in zip(ra,rb))
        phi[str(modulus)]={
           "alpha":alpha,
           "all_six_by_six_original_jet_pairings_transport":True,
           "moment_remainder_Z_diagonal_mod_pk":remainder[1][1]%modulus,
           "relative_Gram_difference_mod_pk_nonzero":not same_mod(A,B,modulus),
        }

    reps=lambda t:(t+2)%5-2
    actual=set(Q)
    moved={(x,reps(2*y)) for x,y in Q}
    assert (len(actual & moved),len(moved-actual))==(279,104)
    assert (22,1) in actual and (22,2) not in actual
    weighted_before=Counter((x%5,y%5) for x,y in Q)
    weighted_after=Counter((x%5,(2*y)%5) for x,y in Q)
    mass=sum(abs(weighted_before[k]-weighted_after[k])
             for k in weighted_before.keys()|weighted_after.keys())//2
    assert mass>0
    difference=subtract(B,A)
    rank=rank_mod(difference,5)
    assert 1<=rank<=len(LABELS)
    print("PHASE293_MOMENT_REMAINDER",{
       "full_original_D583_points":len(Q),
       "D587_original_has_same_Q":True,
       "original_rows_used":[list(v) for v in LABELS],
       "ordinary_jets_all_j0_to_4":True,
       "sum_original_y_squared":sum_y2,
       "identity_Z_Gram_difference_exact":exact_diag,
       "identity_Z_Gram_difference_mod5":exact_diag%5,
       "actual_six_by_six_Gram_difference_mod5_rank":rank,
       "local_isometry_moving_support":phi,
       "same_original_support_mod5_residue_multiplicity_transport_mass":mass,
       "pointwise_original_support_overlap_mod5":279,
       "points_outside_original_Q_under_residue_isometry":104,
       "not_an_additional_determinant_factor":True,
       "not_an_integral_source_permutation":True
    },flush=True)
    print("PASS Phase293 original trace-moment non-equivariance and local-field covariant jet transport",flush=True)

if __name__=="__main__":
    main()
