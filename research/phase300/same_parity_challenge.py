#!/usr/bin/env python3
"""Phase300-B: test all later same-parity extensions after seven h1 obstructions.

Preregistered at b96ab218, after Phase300-A showed split H in two
opposite-parity consecutive chains. Original D163, Q109, R40, J=S1.
No source alterations or post-result adaptive search.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for part in ("phase206","phase297","phase298","phase299","phase300"):
    sys.path.insert(0,str(ROOT/"research"/part))
from source_probe import params,gram
import class_one_d163_composition as original
import minimal_transverse_repair as repair
import double_glue_original as double

P=5
MOD=P**16
D=163
PRESELECTED=(13,18,22,25,33,34,38)
PARENT="b0f3fb527bb203228bf5ca3e7ea79f0a4a80b50f"

def guard():
    double.guard()
    path="research/phase300/double_glue_original.py"
    actual=subprocess.check_output(["git","rev-parse","HEAD:"+path],
                                   cwd=ROOT,text=True).strip()
    assert actual==PARENT,("unregistered parent edit",actual)

def symmetry(G,E,W):
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(21,40,1,1,109)
    assert set(Q)=={(-x,-y) for x,y in Q}
    exact=gram(D,Q,J,[(r,0) for r in range(R)])
    assert len(exact)==40 and len(exact[0])==40
    vanishing=[]
    for r in range(R):
        for s in range(R):
            assert int(exact[r][s])%MOD==int(G[r,s])
            if (r+s)%2:
                assert int(exact[r][s])==0
                assert int(G[r,s])==0
                vanishing.append((r,s))
    assert len(vanishing)==800
    # Independently verify the original raw monomial channel parity.
    # Each observation paired with its central inverse:
    qi={q:i for i,q in enumerate(Q)}
    for r in range(40):
        for i,q in enumerate(Q):
            j=qi[(-q[0],-q[1])]
            assert int(E[r,2*j])%MOD==(((-1)**r)*int(E[r,2*i]))%MOD
            assert int(E[r,2*j+1])%MOD==(((-1)**r)*int(E[r,2*i+1]))%MOD
    return {"exact_original_mixed_parity_Gram_zeros":800,
            "original_Q_central_inversion":True,
            "all_40_monomial_raw_parity_channels_checked":True}

def opposite_parity_control(G,n):
    """Produce a valid a21=0 scaled second projection without guessing.

    This confirms an exact parity-block reason for the observed split
    of original consecutive n33 and n38 chains, rather than relying
    on one possibly noncanonical finite Smith solution.
    """
    r=n+1
    assert (n+r)%2==1
    same=[i for i in range(n) if i%2==r%2]
    other=[i for i in range(n) if i%2!=r%2]
    A=G[np.ix_(same,same)]
    c=G[np.ix_(same,[r])]
    grades,diag,U,V=repair.tracked_smith_solver(A)
    assert max(grades)<16
    x,issues=repair.can_solve_or_fail(
        grades,diag,U,V,A,
        np.asarray((5*np.asarray(c,dtype=object))%MOD,dtype=np.int64),
        True)
    assert x is not None and not issues
    # Append y1 (opposite parity) as an explicitly ZERO coefficient.
    full=np.zeros((n+1,1),dtype=np.int64)
    full[same,:]=x
    assert not np.any(full[other,:])
    assert int(full[n,0])==0
    G1=G[:n+1,:n+1]
    C=G[:n+1,r:r+1]
    assert not np.any((np.asarray(G1,dtype=object)@
                       np.asarray(full,dtype=object)
                       -5*np.asarray(C,dtype=object))%MOD)
    assert int(G[n,r])==0
    return {"n":n,"next_row":r,
            "valid_original_scaled_solution_with_a21_exact_zero":True,
            "old_same_parity_row_count":len(same),
            "opposite_parity_cross_entries_zero":len(other)+1}

def complete_same_parity_challenge(G,E,W):
    hist=Counter()
    first_checks=[]
    tested=0
    certified=[]
    for n in PRESELECTED:
        old=G[:n,:n]
        c1=G[:n,n:n+1]
        first=double.debt(old,c1)
        assert first==1,("Phase298-B retrospective first stage drift",n,first)
        first_checks.append(n)
        for s in range(n+2,40,2):
            assert s%2==n%2
            tested+=1
            selected=list(range(n))+[n,s]
            L2=G[np.ix_(selected,selected)]
            G1=L2[:n+1,:n+1]
            c2=L2[:n+1,n+1:n+2]
            second=double.debt(G1,c2)
            hist[second]+=1
            assert second>=0
            if second==1:
                result=double.double_glue(
                    L2,f"original_D163_n{n}_r{s}",
                    E[selected,:],W)
                assert result["H"]["H_order"]==25
                certified.append({
                    "original_first_n":n,
                    "first_new_monomial":n,
                    "second_new_monomial":s,
                    "H_group":result["H"]["H_group"],
                    "a21_mod5":result["H"]["a21_mod5"],
                    "old_v5":result["old_v5"],
                    "final_v5":result["original_final_v5"],
                    "first_k_norm_v5":result["k1_norm_v5"],
                    "second_k_norm_v5":result["k2_norm_v5"],
                    "original_jet_source_checks":result[
                        "original_E_jet_trace_controls"],
                    "first_coeff_sha":result[
                        "a1_original_row_coordinates_sha256"],
                    "second_coeff_sha":result[
                        "a2_original_row_coordinates_sha256"],
                })
            print("PHASE300B_SAME_PARITY_SCAN",{
                "n":n,"last_original_r":s,
                "first_image_log5":first,
                "second_image_log5":second,
                "double_glue_certified":second==1},flush=True)
    assert first_checks==list(PRESELECTED)
    assert tested==43
    assert sum(hist.values())==tested
    counts=Counter(r["H_group"] for r in certified)
    return {"preselected_first_obstructions":list(PRESELECTED),
            "all_later_same_parity_chains_tested":tested,
            "second_stage_image_index_histogram":dict(sorted(hist.items())),
            "both_nonintegral_order5_cases":len(certified),
            "gluing_group_type_counts":dict(sorted(counts.items())),
            "all_qualifying_original_source_certificates":certified,
            "not_a_contiguous_degree_filtration_when_second_r_skipped":True,
            "no_result_selected_after_reading_outcomes":True}

def main():
    guard()
    field=original.field_h1_background()
    G,E,W,source=original.original_j1_source()
    sym=symmetry(G,E,W)
    standard=[opposite_parity_control(G,n) for n in (33,38)]
    census=complete_same_parity_challenge(G,E,W)
    print("PHASE300B_ORIGINAL_SOURCE_SYMMETRY_AND_CHALLENGE",{
        "class_one_field_background":field,
        "original_D163_source":source,
        "exact_central_inversion_parity_proof_checks":sym,
        "previous_contiguous_opposite_parity_forced_split":standard,
        "source_exact_same_parity_noncontiguous_census":census,
        "NO_new_original_Gram_valuation_factor":True,
        "NO_uniform_high_J_h1_discriminant_result":True},flush=True)
    print("PASS Phase300-B source parity mechanism and complete fixed same-parity challenge",
          flush=True)

if __name__=="__main__":
    main()
