#!/usr/bin/env python3
"""Two nonintegral original-row extensions, with actual gluing H (Phase300).

Preregistered at ef74ac1d before code, source outcomes, or CI.
Both D163 chains were selected RETROSPECTIVELY from Phase298-B's
exhaustive scan. No altered observation/jet metric or new field bound.
"""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
for part in ("phase206", "phase297", "phase298", "phase299"):
    sys.path.insert(0, str(ROOT / "research" / part))
import class_one_d163_composition as original
import minimal_transverse_repair as solver
import original_schur_integrality_k16 as smith
import gluing_core as glue

P, K, MOD = 5, 16, 5**16
FROZEN = {
    "research/phase206/source_probe.py": "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase298/class_one_d163_composition.py": "e8cae60a662ca59cade8acd741c2d5d4f4982d6a",
    "research/phase297/minimal_transverse_repair.py": "22b0077a2424553021a4c9859f92f0fe3efc2fe7",
    "research/phase299/gluing_core.py": "dba83c3fd8a07734f0bc2a7ec6724c0362fbdf9a",
}

def guard():
    original.guard()
    for path, sha in FROZEN.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", "HEAD:" + path], cwd=ROOT, text=True
        ).strip()
        assert actual == sha, ("changed original source", path, actual, sha)

def obj(A):
    return np.asarray(A, dtype=object)

def residue(A):
    return np.asarray(obj(A) % MOD, dtype=np.int64)

def dot(A, B):
    return (obj(A) @ obj(B)) % MOD

def smith_fully_resolved(A):
    exponents, hist = smith.high_precision_smith(A)
    assert exponents and max(exponents) < K, ("Smith censored", hist)
    return exponents, hist

def debt(A, C):
    aa, _ = smith_fully_resolved(A)
    bb, _ = smith_fully_resolved(
        np.concatenate((A, C), axis=1))
    assert all(b <= a for a, b in zip(aa, bb))
    return sum(aa) - sum(bb)

def solve_order_five(A, C, name):
    n = len(A)
    assert A.shape == (n,n) and C.shape == (n,1)
    exponents, diagonal, U, V = solver.tracked_smith_solver(A)
    assert max(exponents) < K
    impossible, reasons = solver.can_solve_or_fail(
        exponents, diagonal, U, V, A, C, False)
    assert impossible is None and reasons, ("expected nonintegral", name)
    a, reasons = solver.can_solve_or_fail(
        exponents, diagonal, U, V, A, residue(P * obj(C)), True)
    assert a is not None and not reasons
    assert not np.any((dot(A,a) - P*obj(C)) % MOD)
    assert debt(A,C) == 1, ("expected exactly order five", name)
    return residue(a), dict(sorted(Counter(exponents).items()))

def v5(x):
    return glue.pv(int(x))

def group(a21):
    """Enumerate H=L2/N of order25 using original row relations."""
    c = int(a21) % MOD
    cosets = {((5*i + c*j)%25, j%5)
              for i in range(5) for j in range(5)}
    assert len(cosets) == 25
    assert all(((x+u)%25,(y+v)%5) in cosets
               for x,y in cosets for u,v in cosets)
    y1 = lambda k: ((5*k)%25, 0)
    y2 = lambda k: ((c*k)%25, k%5)
    assert y1(5) == y2(25) == (0,0)
    ord2 = next(k for k in range(1,26) if y2(k) == (0,0))
    assert ord2 == (25 if c%5 else 5)
    assert y2(5) == y1(c)
    return {
        "H_order":25,
        "all_distinct_cosets":25,
        "a21_mod5":c%5,
        "y1_order":5,
        "y2_order":ord2,
        "H_group":"Z/25" if ord2==25 else "(Z/5)^2",
        "extension_non_split":bool(c%5)
    }

def weighted(E, F, W):
    return (obj(E)*obj(W)[None,:])@obj(F).T % MOD

def double_glue(G_in, label, E=None, W=None):
    """Build N=L0 orthogonal K1 orthogonal K2 inside ORIGINAL L2."""
    G=residue(G_in)
    n=G.shape[0]-2
    assert n >= 1 and np.array_equal(G,G.T)
    A=G[:n,:n]
    G1=G[:n+1,:n+1]
    a1, old_hist = solve_order_five(A,G[:n,n:n+1],label+" first")
    a2, mid_hist = solve_order_five(
        G1,G[:n+1,n+1:n+2],label+" second")
    a21=int(a2[n,0])
    B=np.eye(n+2,dtype=object)
    B[:n,n]=-obj(a1[:,0])
    B[n,n]=5
    B[:n,n+1]=-obj(a2[:n,0])
    B[n,n+1]=-a21
    B[n+1,n+1]=5

    N=dot(dot(B.T,G),B)
    assert np.array_equal(N[:n,:n],obj(A))
    assert not np.any(N[:n,n:]) and not np.any(N[n:,:n])
    assert int(N[n,n+1])==int(N[n+1,n])==0
    m1,m2=int(N[n,n]),int(N[n+1,n+1])
    e1,e2=v5(m1),v5(m2)
    assert e1<K and e2<K
    oldv=sum(smith_fully_resolved(A)[0])
    midv=sum(smith_fully_resolved(G1)[0])
    full_exps, full_hist=smith_fully_resolved(G)
    fullv=sum(full_exps)
    assert midv == oldv+e1-2
    assert fullv == midv+e2-2 == oldv+e1+e2-4

    # Original y1,y2 represented as rational N-frame coordinates,
    # numerator over 25: B*q_i = 25*e_yi.
    q1=np.asarray([*(5*int(z) for z in a1[:,0]),5,0],dtype=object)
    q2=np.asarray([*(5*int(a2[i,0])+a21*int(a1[i,0])
                     for i in range(n)), a21,5],dtype=object)
    unit1=np.zeros(n+2,dtype=object);unit1[n]=25
    unit2=np.zeros(n+2,dtype=object);unit2[n+1]=25
    assert not np.any((B@q1-unit1)%MOD)
    assert not np.any((B@q2-unit2)%MOD)

    # Each original generator is in N^#; its bilinear pairing
    # with every N generator must be 5-adically integral.
    for q in (q1,q2):
        assert not np.any((N@q)%25)
    for i,q in ((n,q1),(n+1,q2)):
        for j,r in ((n,q1),(n+1,q2)):
            numerator=int((q@N@r)%MOD)
            assert numerator%625==0
            assert (numerator-625*int(G[i,j]))%MOD==0

    native={}
    if E is not None:
        E=obj(E)
        W=obj(W)
        assert E.shape[0]==n+2 and E.shape[1]==len(W)
        k1=(5*E[n:n+1]-obj(a1).T@E[:n])%MOD
        k2=(5*E[n+1:n+2]-obj(a2[:n]).T@E[:n]
            -a21*E[n:n+1])%MOD
        assert not np.any(weighted(E[:n],k1,W))
        assert not np.any(weighted(E[:n+1],k2,W))
        assert not np.any(weighted(k1,k2,W))
        assert int(weighted(k1,k1,W)[0,0])==m1
        assert int(weighted(k2,k2,W)[0,0])==m2
        EN=np.vstack((E[:n],k1,k2))
        assert np.array_equal(weighted(EN,EN,W),N)
        native={"original_jet_channels":len(W),
                "all_original_old_vs_k1_zero":n,
                "all_first_stage_vs_k2_zero":n+1,
                "full_N_Gram_replayed_in_original_trace":True}
    return {
       "case":label,"old_rows":n,"original_final_rows":n+2,
       "first_and_second_projection_denominator":[5,5],
       "old_v5":oldv,"intermediate_v5":midv,"original_final_v5":fullv,
       "k1_norm_mod5pow16":m1,"k2_norm_mod5pow16":m2,
       "k1_norm_v5":e1,"k2_norm_v5":e2,
       "orthogonal_subLattice_index_in_original":25,
       "determinant_index_square_subtraction":-4,
       "all_bilinear_glue_pairs_integral":True,
       "original_L2_recovered_from_isotropic_H":True,
       "H":group(a21),
       "old_Smith_hist":old_hist,"intermediate_Smith_hist":mid_hist,
       "original_final_Smith_hist":full_hist,
       "a1_original_row_coordinates_sha256":hashlib.sha256(
           json.dumps(a1[:,0].tolist(),separators=(",",":")).encode()).hexdigest(),
       "a2_original_row_coordinates_sha256":hashlib.sha256(
           json.dumps(a2[:,0].tolist(),separators=(",",":")).encode()).hexdigest(),
       "original_E_jet_trace_controls":native,
       "no_new_original_determinant_mass":True
    }

def toys():
    datasets=[
     ("cyclic", [[25,5,1],[5,10,0],[1,0,10]], "Z/25", Fraction(-1,9),2240),
     ("split", [[25,5,0],[5,10,1],[0,1,10]], "(Z/5)^2",Fraction(5,9),2225)
    ]
    results=[]
    for name,grid,expected,expected_a21,expected_det in datasets:
        A,c1,c2=grid[0]
        b1,e,b2=grid[1][1],grid[1][2],grid[2][2]
        det1=A*b1-c1*c1
        det2=A*(b1*b2-e*e)-c1*(c1*b2-e*c2)+c2*(c1*e-b1*c2)
        assert A>0 and det1==225>0 and det2==expected_det>0
        t2=[Fraction(b1*c2-c1*e,det1),
            Fraction(-c1*c2+A*e,det1)]
        assert Fraction(c1,A)==Fraction(1,5)
        assert 5*t2[1]==expected_a21
        assert any(t.denominator%5==0 for t in t2)
        assert all((5*t).denominator%5!=0 for t in t2)
        measured=double_glue(grid,name)
        assert measured["H"]["H_group"]==expected
        assert measured["original_final_v5"]==v5(det2)
        results.append({"toy":name,
                        "second_rational_projection":[str(t) for t in t2],
                        "actual_scaled_second_y1_coefficient":str(5*t2[1]),
                        "full_integer_determinant":det2,
                        "certificates":measured})
    assert results[0]["certificates"]["H"]["H_order"]==25
    assert results[1]["certificates"]["H"]["H_order"]==25
    hostile=np.array([[5,1,0],[1,5,0],[0,0,1]],dtype=np.int64)
    assert debt(hostile[:1,:1],hostile[:1,1:2])==1
    assert debt(hostile[:2,:2],hostile[:2,2:3])==0
    return {"two_distinct_order25_positive_definite_toys":results,
            "one_nonintegral_then_integral_negative_control":True}

def gauge_toy():
    grid=np.array([[25,5,1],[5,10,0],[1,0,10]],dtype=object)
    F=np.eye(3,dtype=object)
    F[0,0]=-1
    F[2,1]=1
    g=double_glue(grid,"original_toy_frame")
    h=double_glue((F@grid@F.T)%MOD,"filtration_preserving_GL_frame")
    assert g["H"]["H_group"]==h["H"]["H_group"]=="Z/25"
    assert g["original_final_v5"]==h["original_final_v5"]
    assert g["a1_original_row_coordinates_sha256"]!=(
           h["a1_original_row_coordinates_sha256"])
    return {"filtration_preserving_unimodular_frame":True,
            "same_abstract_glue_group_and_original_valuation":True,
            "coordinate_projection_coefficients_not_invariant":True}

def original_h1_cases():
    field=original.field_h1_background()
    G,E,W,source=original.original_j1_source()
    assert (source["R"],source["S"],source["J"],source["Q"])==(40,1,1,109)
    results={}
    for n in (33,38):
        # Chosen retrospectively from the previously EXHAUSTIVE
        # 38 original contiguous source triples.
        assert debt(G[:n,:n],G[:n,n:n+1])==1
        assert debt(G[:n+1,:n+1],G[:n+1,n+1:n+2])==1
        info=double_glue(G[:n+2,:n+2],f"original_D163_n{n}",
                         E[:n+2],W)
        assert info["H"]["H_order"]==25
        results[f"L{n}_L{n+1}_L{n+2}"]=info
        print("PHASE300_ORIGINAL_H1_CHAIN",{
            "n":n,"group":info["H"],
            "old_v5":info["old_v5"],
            "full_v5":info["original_final_v5"],
            "k1_v5":info["k1_norm_v5"],
            "k2_v5":info["k2_norm_v5"]},flush=True)
    return {"field_class_number_one_background":field,
            "original_integer_order_Q109_J1":source,
            "two_original_chains":results,
            "retrospectively_fixed_from_Phase298_complete_scan":True,
            "not_uniform_high_J_field_theorem":True}

def main():
    guard()
    toy_results=toys()
    gauge=gauge_toy()
    actual=original_h1_cases()
    print("PHASE300_TWO_NONINTEGRAL_GLUE",{
      "prime":5,"precision":16,"original_source_not_modified":True,
      "positive_definite_counterworlds":toy_results,
      "unimodular_gauge":gauge,
      "original_class_one_field_source":actual,
      "same_order25_NOT_same_group_type":True,
      "index25_squared_correction_NOT_new_original_mass":True,
      "no_discriminant_cutoff_improvement":True},flush=True)
    print("PASS Phase300 double nonintegral gluing, original D163, and group structure",
          flush=True)

if __name__=="__main__":
    main()
