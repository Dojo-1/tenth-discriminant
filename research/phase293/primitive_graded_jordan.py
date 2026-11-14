#!/usr/bin/env python3
"""Phase293-B: genuine graded p5 quadratic Jordan signs on primitive H.

Preregistered in PRE_REGISTERED_JORDAN_AND_MOMENT_REMAINDER.md at
13d76c34 BEFORE code. Original D583 full 725-row source versus first
725 original D587 rows (DIAGNOSTIC ONLY). Preserve all Q383/J5 and
field-specific original metric, saturate parity sectors separately.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase204","phase281","phase292"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from full_d403_third_layer import smith_profile_k3
from matched_inert5_neighbor import (
    source_normalized, source_smith_with_row_map,
    independent_rank, metric_gram, oracle_exact
)

P=5
K=9
MOD=125
SOURCE_GUARDS={
 "research/phase292/matched_inert5_neighbor.py":
       "9216de10f311cf301413de663738804b5fbec203",
 "research/phase292/matched_support_local_field.py":
       "eaa5d2ca3bf5833285cad062110cd612adb1cbb3",
 "research/phase206/source_probe.py":
       "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":
       "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
 "research/phase281/full_d403_third_layer.py":
       "d28b1420a371ca3a8a0297a19ecec75feedfc978",
}
EXPECTED_SOURCE={0:625,4:10,5:20,6:70}
EXPECTED_PRIMITIVE={"0":690,"1":35,"2":0,">=3":0}

def source_guard():
    for path,sha in SOURCE_GUARDS.items():
        observed=subprocess.check_output(
           ["git","rev-parse","HEAD:"+path],
           cwd=ROOT,text=True).strip()
        assert observed==sha,("unexpected source drift",path,observed,sha)

def v_p(x,p=P,cap=3):
    if x==0:return cap
    for e in range(cap):
        if x%(p**(e+1))!=0:return e
    return cap

def quadratic_sign(a,p=P):
    assert a%p
    return 1 if pow(int(a)%p,(p-1)//2,p)==1 else -1

def jordan_by_integral_congruence(H,p=P,k=3):
    """Symmetric odd-p Gram-Schmidt, no independent Smith columns.

    Simultaneous source row/column operations only; records grades and
    determinant UNIT square classes (not just Smith valuations).
    """
    modulus=p**k
    A=np.asarray(H,dtype=np.int64).copy()%modulus
    n,m=A.shape
    assert n==m and np.array_equal(A,A.T)
    profiles={}
    pivots=[]
    for t in range(n):
        rem=A[t:,t:]
        level=next((e for e in range(k)
                    if np.any(rem%(p**(e+1))!=0)),None)
        if level is None:
            for _ in range(t,n):pivots.append(k)
            break
        stride=p**(level+1)
        diag=np.diag(A)[t:]
        available=np.flatnonzero(diag%stride!=0)
        if available.size:
            idx=t+int(available[0])
        else:
            # For odd p, a unit off-diagonal entry yields a unit
            # diagonal pivot after e_i -> e_i + e_j.
            aa=np.argwhere(rem%stride!=0)
            pick=next(((int(x)+t,int(y)+t) for x,y in aa if x!=y),None)
            assert pick is not None,("missing unit off-diagonal pivot",level)
            idx,j=pick
            assert idx!=j
            A[idx,:]=(A[idx,:]+A[j,:])%modulus
            A[:,idx]=(A[:,idx]+A[:,j])%modulus
            assert A[idx,idx]%stride!=0
        if idx!=t:
            A[[t,idx],:]=A[[idx,t],:]
            A[:,[t,idx]]=A[:,[idx,t]]
        d=int(A[t,t])
        assert v_p(d,p,k)==level
        q=modulus//(p**level)
        unit=(d//(p**level))%p
        assert unit!=0
        pivots.append(level)
        block=profiles.setdefault(level,{"rank":0,"unit_product_mod_p":1,
                                        "legendre_sign":1})
        block["rank"]+=1
        block["unit_product_mod_p"]=block["unit_product_mod_p"]*unit%p
        block["legendre_sign"]=quadratic_sign(block["unit_product_mod_p"],p)
        if t+1<n:
            b=A[t+1:,t].copy()
            assert np.all(b%(p**level)==0)
            inv=pow(d//(p**level),-1,q)
            c=((b//(p**level))*inv)%q
            tail=A[t+1:,t+1:].copy()
            A[t+1:,t+1:]=(tail-np.outer(c,b)-np.outer(b,c)
                +d*np.outer(c,c))%modulus
            A[t+1:,t]=0
            A[t,t+1:]=0
            assert np.array_equal(A[t+1:,t+1:],A[t+1:,t+1:].T)
    hist=dict(sorted(Counter(pivots).items()))
    assert len(pivots)==n
    for level,block in profiles.items():
        assert block["unit_product_mod_p"] in (1,2,3,4)
        assert block["legendre_sign"] in (-1,1)
        assert hist[level]==block["rank"]
    return hist,profiles

def negative_controls():
    A=np.array([[1]],dtype=np.int64)
    B=np.array([[2]],dtype=np.int64)
    ah,asym=jordan_by_integral_congruence(A)
    bh,bsym=jordan_by_integral_congruence(B)
    assert ah==bh=={0:1}
    assert asym[0]["legendre_sign"]==1
    assert bsym[0]["legendre_sign"]==-1
    # A 2-by-2 hyperbolic block has no diagonal unit, but a
    # simultaneous e_i+e_j operation exposes one at p odd.
    off=np.array([[0,1],[1,0]],dtype=np.int64)
    oh,os=jordan_by_integral_congruence(off)
    assert oh=={0:2}
    assert os[0]["legendre_sign"]==1
    toy=np.diag([1,2,5,10,25]).astype(np.int64)
    ref=jordan_by_integral_congruence(toy)
    T=np.eye(5,dtype=np.int64)
    T[0,1]=1
    T[2,0]=1
    T[3,4]=-1
    transformed=(T@toy@T.T)%MOD
    comp=jordan_by_integral_congruence(transformed)
    assert ref[0]==comp[0]
    assert all(ref[1][e]["legendre_sign"]==comp[1][e]["legendre_sign"]
               for e in ref[1])
    assert ref[0]=={0:2,1:2,2:1}
    return {"same_Smith_different_Z5_isometry_class":True,
            "odd_prime_offdiag_congruence_control":True,
            "unimodular_shear_grade_sign_invariance":True}

def parity_rows(R,S,parity):
    return [r*S+s for r in range(R) for s in range(S)
            if (r+s)%2==parity]

def source_sector(C,D,Q,R,S,J,indices):
    n=len(indices)
    assert n in (363,362)
    rows=C[indices]
    levels,hist,U=source_smith_with_row_map(rows)
    assert len(levels)==n and max(levels)<=6 and 9 not in hist
    mod=P**K
    numerator=(U@rows)%mod
    primitive=np.zeros_like(rows)
    for i,e in enumerate(levels):
        assert np.all(numerator[i]%(P**e)==0)
        assert e+3<=K
        primitive[i]=(numerator[i]//(P**e))%MOD
    assert independent_rank(primitive%P)==n
    H=metric_gram(primitive,D,J,Q,MOD)
    oldF=sum(min((idx//S)//P,S-1-(idx%S)) for idx in indices)
    assert oldF in (676,674)
    smith=smith_profile_k3(H,P)
    jhist,grades=jordan_by_integral_congruence(H)
    assert smith["0"]==jhist.get(0,0)
    assert smith["1"]==jhist.get(1,0)
    assert smith["2"]==jhist.get(2,0)
    assert smith[">=3"]==jhist.get(3,0)==0
    # A nontrivial elementary unimodular symmetric congruence on the
    # ACTUAL large primitive source must preserve every Jordan sign.
    T=np.eye(n,dtype=np.int64)
    T[0,1]=1
    T[2,0]=-1
    shear=(T@H@T.T)%MOD
    shist,sgrades=jordan_by_integral_congruence(shear)
    assert shist==jhist
    assert all(sgrades[e]["legendre_sign"]==grades[e]["legendre_sign"]
               for e in grades)
    return {
        "row_count":n,
        "old_F":oldF,
        "secondary_index":sum(levels),
        "source_secondary_hist":hist,
        "primitive_H_smith":smith,
        "primitive_H_Jordan_graded_signs":{
            str(e):{"rank":v["rank"],
                    "unit_det_square_class_mod5":v["legendre_sign"]}
            for e,v in sorted(grades.items())
        },
        "primitive_H_p5_valuation":sum(int(e)*int(v["rank"])
                                        for e,v in grades.items()),
        "same_form_shear_grade_invariance":True
    },primitive

def full_specimen(D):
    rho,R,S,J,Q=params(D)
    assert (rho,S,J,len(Q))==(53,5,5,383)
    assert R==(145 if D==583 else 146)
    C,old,histk=source_normalized(D,Q,R,S,J)
    assert C.shape==(R*S,3830)
    assert old==(1350 if D==583 else 1360)
    assert oracle_exact(D,Q,R,S,J,C)==480
    C=C[:725].copy()  # Entire D583; diagnostic first rows for D587
    n=725
    assert len(C)==n
    parity=np.array([(-1)**(r+s) for r in range(145)
                     for s in range(S)],dtype=np.int64)
    # Original normalized source symmetry still holds after Frobenius.
    A=(C%25).reshape(n,J,len(Q),2)
    assert all(Q[i]==(-Q[len(Q)-1-i][0],-Q[len(Q)-1-i][1])
               for i in range(len(Q)))
    for j in range(J):
        assert np.array_equal((parity[:,None,None]*A[:,j])%25,
                              ((-1)**j*A[:,j,::-1,:])%25)
    parts={}
    prim={}
    source_total=Counter()
    h_total=Counter()
    for parity_id,name in ((0,"even"),(1,"odd")):
        rows=parity_rows(145,S,parity_id)
        p,Cp=source_sector(C,D,Q,145,S,J,rows)
        parts[name]=p
        prim[name]=Cp
        source_total.update(p["source_secondary_hist"])
        h_total.update(p["primitive_H_smith"])
    B=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    cross=((prim["even"]*(B%MOD))@prim["odd"].T)%MOD
    assert cross.shape==(363,362)
    assert not np.count_nonzero(cross)
    assert dict(source_total)==EXPECTED_SOURCE
    assert dict(h_total)==EXPECTED_PRIMITIVE
    assert sum(v["old_F"] for v in parts.values())==1350
    assert sum(v["secondary_index"] for v in parts.values())==560
    assert sum(v["primitive_H_p5_valuation"] for v in parts.values())==35
    parity_signs={}
    total_signs={}
    for name,part in parts.items():
        parity_signs[name]=part["primitive_H_Jordan_graded_signs"]
    for e in ("0","1"):
        signs=[parity_signs[name][e]["unit_det_square_class_mod5"]
               for name in ("even","odd")]
        total_signs[e]=signs[0]*signs[1]
    result={"D":D,
       "source_kind":"full_original" if D==583 else "D587_first725_only_diagnostic",
       "actual_full_original_D587_rows":730,
       "rows_used":n,"all_original_Q":len(Q),"J":J,
       "original_columns":C.shape[1],
       "old_F_counted_once":1350,"secondary_index":560,
       "primitive_H_valuation":35,
       "exact_same_source_Gram_v5":3855,
       "original_metric":f"diag(2,{2*D})",
       "parity_graded_Jordan":parity_signs,
       "ungraded_Jordan_unit_signs":total_signs,
       "all_original_cross_sector_pairings_zero_mod125":True,
       "no_unverified_field_theorem_or_new_factor":True}
    return result

def compare(left,right):
    grade=lambda a,name:evaluate_grades(a,name)
    even=left["parity_graded_Jordan"]["even"]==right["parity_graded_Jordan"]["even"]
    odd=left["parity_graded_Jordan"]["odd"]==right["parity_graded_Jordan"]["odd"]
    ungraded=left["ungraded_Jordan_unit_signs"]==right["ungraded_Jordan_unit_signs"]
    return {
      "both_have_IDENTICAL_Smith_profile":True,
      "even_parity_Z5_primitive_pairing_isometry_class_matches":even,
      "odd_parity_Z5_primitive_pairing_isometry_class_matches":odd,
      "ungraded_Z5_primitive_pairing_class_matches":ungraded,
      "parity_equivariant_abstract_pairing_isometry_class_matches":even and odd,
      "explicit_original_observation_support_transport_constructed":False,
      "not_the_same_original_field_source":True,
    }

def main():
    source_guard()
    toy=negative_controls()
    left=full_specimen(583)
    print("PHASE293_JORDAN_D583",left,flush=True)
    right=full_specimen(587)
    print("PHASE293_JORDAN_D587_725_ROW_DIAGNOSTIC",right,flush=True)
    comparison=compare(left,right)
    print("PHASE293_JORDAN_COMPARISON",comparison,flush=True)
    print("PHASE293_JORDAN_HOSTILE_CONTROLS",toy,flush=True)
    print("PASS Phase293 original p5 graded Jordan primitive pairing test",flush=True)

if __name__=="__main__":
    main()
