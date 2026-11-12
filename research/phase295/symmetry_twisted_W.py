#!/usr/bin/env python3
"""Phase295-B: test original inversion/Galois-twisted scalar W transport.

Separately preregistered at 214009bb AFTER Phase295-A CI but BEFORE
this executable. Four natural twists are a DECLARED finite group, not
a search over unconstrained observation-side matrices.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase204","phase294","phase295"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from ordinary_jet_filtration import jet
from support_debt_tower import hensel_lifts
from w_equivariant_jet_obstruction import (
    P,D_A,D_B,J,freeze,field_value_w
)

PARENT_BLOB="e91561f848bdd5aea4aaf3cc65c5d883ce12ec4a"
EXPECTED={1:(279,104),2:(107,276),3:(107,276),13:(107,276)}

def guard():
    freeze()
    actual=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase295/w_equivariant_jet_obstruction.py"],
        cwd=ROOT,text=True
    ).strip()
    assert actual==PARENT_BLOB

def action(kind,q):
    x,y=q
    if kind=="identity":return (x,y)
    if kind=="central_inversion":return (-x,-y)
    if kind=="field_conjugation":return (x,-y)
    if kind=="inversion_times_conjugation":return (-x,y)
    raise ValueError(kind)

ACTIONS=("identity","central_inversion","field_conjugation",
         "inversion_times_conjugation")

def matching(source,target):
    n=sum(source.values())
    assert n==sum(target.values())
    pairs=sum(min(source[key],target[key])
              for key in source.keys()|target.keys())
    return pairs,n-pairs

def jet_symmetry(Q):
    # This checks exactly the ORIGINAL ordinary Z-jet polynomial source,
    # not a generic p-adic jet with W derivatives.
    count=0
    for D in (D_A,D_B):
        for point in (Q[0],Q[len(Q)//3],Q[len(Q)//2],Q[-1]):
            inverted=action("central_inversion",point)
            conjugated=action("field_conjugation",point)
            for r,s in ((0,0),(1,0),(4,0),(5,1),(10,4)):
                for j in range(J):
                    original=jet(D,r,s,j,point)
                    inverted_value=jet(D,r,s,j,inverted)
                    sign=(-1)**(r+s-j)
                    assert inverted_value==tuple(sign*a for a in original)
                    conj_value=jet(D,r,s,j,conjugated)
                    assert conj_value==(original[0],-original[1])
                    count+=2
    return count

def hostile_asymmetric_control():
    # Symmetry is essential; one cannot declare the four twists
    # equivalent for an arbitrary observation support.
    toy=[(1,1),(2,1)]
    m=5
    alpha=2
    baseline=Counter(field_value_w(x,y,alpha,m) for x,y in toy)
    conjugate=Counter(field_value_w(
        *action("field_conjugation",q),alpha,m) for q in toy)
    assert baseline!=conjugate
    assert matching(baseline,conjugate)==(0,2)
    return True

def main():
    guard()
    _,ra,sa,ja,Qa=params(D_A)
    _,rb,sb,jb,Qb=params(D_B)
    assert (ra,sa,ja,len(Qa))==(145,5,5,383)
    assert (rb,sb,jb,len(Qb))==(146,5,5,383)
    assert Qa==Qb
    Q=Qa
    qs=set(Q)
    assert len(qs)==383
    assert all({action(kind,q) for q in Q}==qs for kind in ACTIONS)
    checked=jet_symmetry(Q)
    assert checked==2*2*4*5*5
    assert hostile_asymmetric_control()

    evidence=[]
    for k,mod,alpha in hensel_lifts(13):
        if k not in EXPECTED:continue
        assert (D_A*alpha*alpha-D_B)%mod==0
        source=Counter(field_value_w(x,y,1,mod) for x,y in Q)
        reference=Counter(field_value_w(x,y,alpha,mod) for x,y in Q)
        results={}
        for kind in ACTIONS:
            transformed=Counter(field_value_w(
                *action(kind,q),alpha,mod) for q in Q)
            assert transformed==reference,("symmetry changes spectrum",k,kind)
            got=matching(source,transformed)
            assert got==EXPECTED[k],(k,kind,got)
            # Independent x/y residue comparison for this specific
            # geometric point action, not the earlier scalar-W oracle.
            original=Counter((x%mod,y%mod) for x,y in Q)
            moved=Counter((x%mod,(alpha*y)%mod)
                          for x,y in (action(kind,q) for q in Q))
            assert matching(original,moved)==got
            results[kind]={
                "common_point_eigenspaces":got[0],
                "missing_original_point_jet_blocks_per_side":got[1],
                "missing_original_Ak_jet_slots_per_side":J*got[1],
                "GL_W_equivariant_iso_exists":got[1]==0
            }
        assert len(results)==4
        evidence.append({"k":k,"modulus":mod,"alpha":alpha,
                         "twisted_W_module_categories":results})
    assert len(evidence)==4
    print("PHASE295B_ORIGINAL_Q_SYMMETRY_TWISTS",{
       "original_D583_row_count":ra*sa,
       "original_D587_row_count":rb*sb,
       "same_literal_full_original_Q":len(Q),
       "actual_J_ordinary_Z_jets_W_fixed":J,
       "test_category":"A_k-linear invertible W-intertwiners AFTER specified scalar involution",
       "twists_tested":list(ACTIONS),
       "original_jet_C2_and_Galois_coordinate_identities_checked":checked,
       "hostile_nonsymmetric_Q_breaks_twist_equivalence":True,
       "graded_evidence":evidence,
       "no_arbitrary_moving_W_automorphism_or_ZW_exchange_excluded":True,
       "no_actual_field_valuation_or_class_one_theorem":True
    },flush=True)
    print("PASS Phase295-B natural symmetry-twisted original W-jet obstruction",
          flush=True)

if __name__=="__main__":
    main()
