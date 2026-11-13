#!/usr/bin/env python3
"""Phase311-C: ORIGINAL inert Gram mod5 from only 25 residue multiplicities.

This is an exact compression of the unnormalized original ordinary-jet
source modulo5. It does NOT apply after source-row /5 primitive saturation:
the latter retains higher 5-adic lift data invisible to residue counts.
"""
from collections import Counter
from math import isqrt
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for name in ("phase206","phase304","phase311"):
    sys.path.insert(0,str(ROOT/"research"/name))
import source_probe
import highjet_d203_original as d203_original
from inert_trace_radicals import (field_checks,full_omega_q,rank_f25,
                                 rank_f5,trace_gram_from_original,
                                 d203_full_source,matched_full_source,
                                 omega_product)

P=5


def full_original_residue_evaluator(q,d,R,S,J):
    """Exact original Z^r W^s ordinary Z-jet, reduced modulo5."""
    field_checks(d)
    assert R>0 and S>0 and J>0 and len(q)>0
    n=R*S
    E=np.zeros((n,2*J*len(q)),dtype=np.int64)
    for qi,z in enumerate(q):
        powers=[(1,0)]
        for r in range(1,R):
            powers.append(omega_product(powers[-1],z,d,P))
        w=(z[0]+z[1],-z[1])
        wpowers=[(1,0)]
        for s in range(1,S):
            wpowers.append(omega_product(wpowers[-1],w,d,P))
        for r in range(R):
            falling=1
            for jet in range(min(J,r+1)):
                if jet>0:
                    falling=(falling*(r-jet+1))%P
                if falling==0:
                    continue
                for s in range(S):
                    v=omega_product(powers[r-jet],wpowers[s],d,P)
                    i=r*S+s
                    c=2*(jet*len(q)+qi)
                    E[i,c]=falling*v[0]%P
                    E[i,c+1]=falling*v[1]%P
    return E


def residue_census(q,d):
    field_checks(d)
    counts=Counter((a%5,b%5) for a,b in q)
    # Source is required to be conjugation-closed as an ACTUAL multiset.
    for (a,b),count in counts.items():
        conjugate=((a+b)%5,(-b)%5)
        assert counts[conjugate]==count
    return counts


def weighted_gram_from_residue_representatives(E,weights,d):
    E=np.asarray(E,dtype=np.int64)%5
    n=E.shape[0]
    a,b=E[:,0::2],E[:,1::2]
    w=np.asarray(weights,dtype=np.int64).reshape(1,-1)%5
    assert w.shape[1]==a.shape[1]
    coef=(d+1)//2
    gw=(2*((a*w)@a.T)+(a*w)@b.T+(b*w)@a.T
        +coef*((b*w)@b.T))%5
    assert gw.shape==(n,n)
    assert np.array_equal(gw,gw.T)
    return gw


def compressed_original_gram(q,d,R,S,J):
    counts=residue_census(q,d)
    bins=tuple(sorted(counts))
    C=full_original_residue_evaluator(bins,d,R,S,J)
    m=[counts[z] for z in bins]
    weights=m*J
    G=weighted_gram_from_residue_representatives(C,weights,d)
    # Only bins with positive integer multiplicity are used in rank(E);
    # bins with m ≡0 mod5 still matter for the SOURCE image.
    rE=rank_f25(C,d)
    rG=rank_f5(G)
    nonzero=sum(1 for x in m if x%5!=0)
    upper=nonzero*min(J,5)
    assert rG<=min(rE,upper)
    # Standard full-column pullback theorem. It is an equality ONLY when
    # the original residue-jet evaluation spans every active channel.
    full_column_span=(rE==len(bins)*min(J,5))
    if full_column_span:
        assert rG==upper,(
            "surjective original residue-jet pullback must preserve W rank",d)
    assert all(counts[z]==counts[((z[0]+z[1])%5,(-z[1])%5)]
               for z in bins)
    return G,{
        "D":d,
        "actual_observation_count":len(q),
        "source_rows":R*S,
        "original_R_S_J":[R,S,J],
        "observed_distinct_F25_residue_classes":len(bins),
        "nonzero_mod5_multiplicity_classes":nonzero,
        "zero_mod5_multiplicity_classes":len(bins)-nonzero,
        "effective_ordinary_jets_mod5":min(J,5),
        "source_rank_F25":rE,
        "original_Gram_rank_F5":rG,
        "rank_upper_bound_from_weights":upper,
        "induced_trace_radical_dimension":rE-rG,
        "full_original_residue_jet_span":full_column_span,
        "surjective_weighted_pullback_rank_exact_if_applicable":(
            (rG==upper) if full_column_span else None),
        "actual_residue_weights_mod5":{str(z):counts[z]%5 for z in bins},
        "only_original_unscaled_source_supported":True,
        "cannot_compute_primitive_trace_from_residues_alone":True,
        "no_class_number_one_implication":True,
    }


def direct_original_verification(q,d,R,S,J,compressed,full=True):
    E=full_original_residue_evaluator(q,d,R,S,J)
    if full:
        g_direct=trace_gram_from_original(E,d)
        assert np.array_equal(g_direct,compressed),(
            "original uncompressed and residue-weighted Gram differ",d)
        checked=(R*S)**2
    else:
        selected=tuple(range(min(R*S,10)))
        g_direct=trace_gram_from_original(E[list(selected),:],d)
        assert np.array_equal(g_direct,compressed[np.ix_(selected,selected)])
        checked=len(selected)**2
    return checked,E


def original_arms():
    results=[]
    for d in (163,187,203):
        if d==203:
            q,Eparent,_=d203_full_source()
            rho,R,S,J=(24,50,2,2)
        else:
            q,Eparent,_=matched_full_source(d)
            rho,R,S,J=(21,40,1,1)
        compressed,row=compressed_original_gram(q,d,R,S,J)
        direct_count,E=direct_original_verification(
            q,d,R,S,J,compressed,full=True)
        assert np.array_equal(E,Eparent%5),(
            "residue evaluator differs from frozen original",d)
        if d==203:
            frozen=d203_original.original_trace_gram(
                Eparent,len(q),J,5)
            assert np.array_equal(compressed,frozen)
        assert (row["source_rank_F25"],row["original_Gram_rank_F5"])==(
            (50,38) if d==203 else (25,25))
        row["independent_exact_original_Gram_cells_checked"]=direct_count
        row["independent_original_source_coordinates_checked"]=int(E.size)
        results.append(row)
    return results


def larger_native_D427():
    d=427  # squarefree 7*61, 7 ramified, and norm7 impossible since m=107
    rho,R,S,J,_=source_probe.params(d)
    assert (R,S,J)==(106,4,4)
    assert 427==7*61 and (d+1)//4==107
    q=full_omega_q(d,rho)
    assert len(q)==len(set(q))
    assert (d+1)//4>7 and isqrt(7)**2!=7
    compressed,row=compressed_original_gram(q,d,R,S,J)
    count,_=direct_original_verification(q,d,R,S,J,compressed,full=False)
    row["native_original_rho"]=rho
    row["ten_by_ten_direct_actual_original_Gram_cells_checked"]=count
    row["D427_non_h1_norm7_ramified_obstruction"]=True
    old_weight=sum(min(r//5,t) for r in range(R) for t in range(S))
    assert old_weight==586
    old_lower=2*old_weight
    first_level_nullity_floor=R*S-row["original_Gram_rank_F5"]
    assert first_level_nullity_floor==356
    assert old_lower==1172 and old_lower>first_level_nullity_floor
    row["existing_valuationWeight"]=old_weight
    row["existing_double_weight_lower_bound"]=old_lower
    row["original_mod5_Gram_nullity_floor"]=first_level_nullity_floor
    row["new_first_level_floor_does_not_beat_existing_weight"]=True
    return row


def non_surjective_abstract_control():
    # NOT an original observation source: one row and two abstract F25
    # channels. Weights [1,4] both nonzero, but the pullback cancels.
    C=np.asarray([[1,0,1,0]],dtype=np.int64)
    W=[1,4]
    assert rank_f25(C,203)==1
    G=weighted_gram_from_residue_representatives(C,W,203)
    assert G.shape==(1,1) and int(G[0,0])==0
    assert rank_f5(G)==0
    return {"ambient_weight_nonzero_channels":2,
            "source_rank_F25":1,
            "pulled_back_Gram_rank_F5":0,
            "surjective_equality_claim_refused":True}


def controls():
    arms=original_arms()
    larger=larger_native_D427()
    # Synthetic MULTISET: add five copies of actual zero observation.
    # The original source itself is unchanged; this is only an algebraic
    # metamorphic test of the *mod5* residue multiplicity compression.
    q,_E,_=matched_full_source(163)
    assert (0,0) in q
    copied=tuple(q)+((0,0),)*5
    G0,_=compressed_original_gram(q,163,40,1,1)
    G1,_=compressed_original_gram(copied,163,40,1,1)
    assert np.array_equal(G0,G1)
    # Ordinary fifth derivative of any integral monomial carries a
    # falling product of five consecutive integers and vanishes in char5.
    for r in (5,6,17,101,106):
        falling=1
        for j in range(5):
            falling=(falling*(r-j))%5
        assert falling==0
    return {
        "full_original_D163_D187_D203_arms":arms,
        "larger_native_D427_hostile_control":larger,
        "non_surjective_abstract_two_channel_counterworld":non_surjective_abstract_control(),
        "all_four_actual_full_residue_spans_surjective":all(
            x["full_original_residue_jet_span"] for x in arms+[larger]),
        "adding_five_synthetic_zero_observations_leaves_mod5_Gram_fixed":True,
        "fifth_ordinary_Z_derivative_identically_zero_mod5":True,
        "no_primitive_source_info_from_residue_counts":True,
        "no_new_original_field_bound":True
    }


def main():
    print("PHASE311_ORIGINAL_RESIDUE_COMPRESSION_PASS",controls(),flush=True)


if __name__=="__main__":
    main()
