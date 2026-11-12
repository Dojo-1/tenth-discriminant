#!/usr/bin/env python3
"""Phase294-D: exact four-level signed p-adic observation-support tower.

Preregistered at 10d6b86 BEFORE implementation. Not a p^k Gram-rank
theorem and NEVER an additional saturated primitive determinant factor.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase294"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from moving_normalized_field_chart import hensel_alpha,original_guard

P=5
LEVELS=(1,2,3,13)
EXPECTED={
  1:dict(mass=104,int_active=20,unit_active=8,galois_pairs=4,inv_fixed=0),
  2:dict(mass=276,int_active=200,unit_active=200,galois_pairs=100,inv_fixed=4),
  3:dict(mass=276,int_active=552,unit_active=552,galois_pairs=276,inv_fixed=4),
 13:dict(mass=276,int_active=552,unit_active=552,galois_pairs=276,inv_fixed=4),
}
PARENT="79bc80f9cc1f28129762bcc828576b86932c27e3"

def guard():
    original_guard()
    observed=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase294/moving_normalized_field_chart.py"],
        cwd=ROOT,text=True).strip()
    assert observed==PARENT

def support_measure(Q,k,alpha):
    mod=P**k
    return Counter((x%mod,(alpha*y)%mod) for x,y in Q)

def signed_diff(after,before):
    return {z:after[z]-before[z] for z in after.keys()|before.keys()
            if after[z]!=before[z]}

def profile(Q,k,alpha):
    mod=P**k
    before=support_measure(Q,k,1)
    after=support_measure(Q,k,alpha)
    assert sum(before.values())==sum(after.values())==len(Q)
    delta=signed_diff(after,before)
    assert sum(delta.values())==0
    assert sum(abs(v) for v in delta.values())%2==0
    mass=sum(abs(v) for v in delta.values())//2
    unit={z:w%P for z,w in delta.items() if w%P}
    assert all(z[1]%P!=0 for z in unit)
    for (x,y),v in delta.items():
        assert delta.get((x,(-y)%mod),0)==v
        assert delta.get(((-x)%mod,(-y)%mod),0)==v
    galois={}
    for x,y in unit:
        q=(x,min(y,(-y)%mod))
        galois.setdefault(q,0)
        galois[q]+=1
    assert all(v==2 for v in galois.values())
    inv_fixed=sum(1 for x,y in galois if x==(-x)%mod)
    result=dict(
       mass=mass,
       int_active=len(delta),
       unit_active=len(unit),
       galois_pairs=len(galois),
       inv_fixed=inv_fixed
    )
    return result,delta

def pushforward(delta,k):
    """Push level k+1 signed integer measures down to modulus 5^k."""
    mod=P**k
    sums=Counter()
    for (x,y),v in delta.items():
        z=(x%mod,y%mod)
        sums[z]+=v
    return {z:v for z,v in sums.items() if v}

def main():
    guard()
    alpha=hensel_alpha()
    rho,R,S,J,Q=params(583)
    rho2,R2,S2,J2,Q2=params(587)
    assert (rho,R,S,J,len(Q))==(53,145,5,5,383)
    assert (rho2,R2,S2,J2,len(Q2))==(53,146,5,5,383)
    assert Q==Q2 and len(Q)==len(set(Q))
    assert Counter(y for x,y in Q)==Counter({
         -2:43,-1:95,0:107,1:95,2:43})
    assert (alpha%5,alpha%25,alpha%125)==(2,17,67)
    assert (583*alpha*alpha-587)%(P**13)==0

    output={}
    deltas={}
    for k in LEVELS:
        observed,d=profile(Q,k,alpha)
        assert observed==EXPECTED[k],("preregistered support filtration failed",
                                      k,observed,EXPECTED[k])
        negative,neg_d=profile(Q,k,-alpha)
        assert negative==observed and neg_d==d
        identity,identity_d=profile(Q,k,1)
        assert identity["mass"]==0 and not identity_d
        output[str(k)]=observed
        deltas[k]=d
        print("PHASE294D_P_ADIC_SUPPORT_LEVEL",{
            "k":k,"modulus":P**k,**observed,
            "conjugate_sign_alpha_invariance":True
        },flush=True)

    # Exact pushforward in the F5-adic residue tower, no sampled
    # approximation and no p-adic real-time interpretation.
    for low,high in ((1,2),(2,3),(3,13)):
        assert pushforward(deltas[high],low)==deltas[low]
        assert output[str(low)]["mass"]<=output[str(high)]["mass"]
    # Matched geometric null: equal transverse x width makes level1
    # residue support exactly invariant, but not higher levels.
    rect=[(x,y) for y in range(-2,3) for x in range(-21,22)]
    assert len(rect)==215
    rectangle={}
    for k in LEVELS:
        result,_=profile(rect,k,alpha)
        rectangle[str(k)]=result
    assert rectangle["1"]["mass"]==0
    assert rectangle["2"]["mass"]==172
    assert rectangle["3"]["mass"]==172
    assert rectangle["13"]["mass"]==172
    # Original δ1 rank40 applies ONLY over F5. By k2 the support
    # has inversion-fixed Galois orbit channels with x=0, so the
    # p1 balanced parity count is not a general k-th-level theorem.
    assert output["1"]["inv_fixed"]==0
    assert all(output[str(k)]["inv_fixed"]==4 for k in (2,3,13))
    assert output["1"]["galois_pairs"]==4
    assert output["2"]["galois_pairs"]==100
    assert output["3"]["galois_pairs"]==276

    print("PHASE294D_SIGNED_SUPPORT_FILTRATION",{
        "source_original_D583_complete_rows":725,
        "source_D587_first725_only_diagnostic":True,
        "original_Q_point_count":len(Q),
        "alpha_mod5_13":alpha,
        "original_D583_support_versus_formal_moved_support_levels":output,
        "signed_integer_residue_measures_pushforward_exactly":True,
        "total_variation_mass_nondecreasing_under_refinement":True,
        "matched_equal_width_rectangle_levels":rectangle,
        "new_inversion_fixed_galois_orbits_at_k2":4,
        "rank40_even20_odd20_ONLY_at_k1_field":True,
        "no_claim_that_level_k_active_points_equal_Gram_rank":True,
        "no_primitive_p5_valuation_or_uniform_field_theorem":True
    },flush=True)
    print("PASS Phase294-D four-level signed p5-adic support filtration",flush=True)

if __name__=="__main__":
    main()
