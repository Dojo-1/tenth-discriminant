#!/usr/bin/env python3
"""Phase302: original D163 binary residual 5-adic primitive-line invariants.

Preregistered fbd13aec BEFORE code/results. 176 original source 2-planes,
six projective F5 flags per plane, and six Hensel approximations in a
fixed source asymmetry case (n13,s15,t31). No Work or new field cutoff.
"""
from collections import Counter,defaultdict
from pathlib import Path
import hashlib
import json
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for part in ("phase206","phase297","phase298","phase299","phase300","phase301"):
    sys.path.insert(0,str(ROOT/"research"/part))
import class_one_d163_composition as original
import same_parity_challenge as parity
import order_reversal_residuals as previous
import double_glue_original as gram_index
import minimal_transverse_repair as solver
import original_schur_integrality_k16 as smith

P,K,MOD=5,16,5**16
D=163
FIRST=(13,18,22,25,33,34,38)
FROZEN={
    "research/phase301/order_reversal_residuals.py":
      "f5cb041b625f61839518f6c2e18c91d71c7891ae",
    "research/phase301/joint_same_parity_census.py":
      "acd72002911b284bea6fda100435f552756c1532",
}

def freeze():
    previous.guard()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("source hash changed",path,actual,sha)

def O(x):
    return np.asarray(x,dtype=object)

def reduce(x):
    return np.asarray(O(x)%MOD,dtype=np.int64)

def weighted(E,F,W):
    return (O(E)*O(W)[None,:])@O(F).T%MOD

def v5(x):
    x=int(x)%MOD
    if x==0:return K
    v=0
    while x%P==0:
        x//=P;v+=1
    return v

def primitive_completion(x):
    x0,x1=(int(q) for q in x)
    assert x0%P!=0 or x1%P!=0
    y=(0,1) if x0%P else (1,0)
    determinant=x0*y[1]-x1*y[0]
    assert determinant%P!=0
    T=np.asarray([[x0,y[0]],[x1,y[1]]],dtype=object)
    return y,T

def intrinsic_flag(S,x):
    """The exact cross-image group order for a NONISOTROPIC primitive x.

    'exact' means norm is nonzero at the fixed p16 precision.
    """
    x=tuple(int(z) for z in x)
    assert x[0]%P or x[1]%P
    a=int((O(x)@O(S)@O(x))%MOD)
    r=O(x)@O(S)%MOD
    div=min(v5(r[0]),v5(r[1]))
    y,T=primitive_completion(x)
    C=(T.T@O(S)@T)%MOD
    assert int(C[0,0])==a
    assert int(C[0,1])==int(C[1,0])
    assert int((T.T@O(S)@T)[1,1])%MOD==int(C[1,1])
    if a==0:
        return {"censored":True,"flag":x,"norm_valuation_at_least":K,
                "pairing_ideal_depth":div}
    normdepth=v5(a)
    assert normdepth>=div
    c=int(C[0,1])
    crossdepth=v5(c)
    e=normdepth-div
    assert e==max(0,normdepth-crossdepth)
    return {
        "censored":False,
        "flag":x,
        "primitive_completion":y,
        "norm_v5":normdepth,
        "pairing_ideal_depth":div,
        "completion_cross_v5_capped16":crossdepth,
        "exact_stage_cokernel_log5_order":e
    }

def change_basis_invariance(S,x,original_epsilon):
    """Transport BOTH Gram and flag; merely changing the flag is different."""
    x0,x1=map(int,x)
    changes=[
       (np.asarray([[1,1],[0,1]],dtype=object),(x0-x1,x1)),
       (np.asarray([[0,1],[1,0]],dtype=object),(x1,x0)),
    ]
    for T,xprime in changes:
        S2=(T.T@O(S)@T)%MOD
        info=intrinsic_flag(S2,xprime)
        assert not info["censored"]
        assert info["exact_stage_cokernel_log5_order"]==original_epsilon
    return len(changes)

def rank_and_isotropy(S):
    d=min(v5(S[0,0]),v5(S[0,1]),v5(S[1,1]))
    assert d<K
    scale=P**d
    U=np.asarray([[int(S[i,j])//scale%P for j in range(2)]
                  for i in range(2)],dtype=np.int64)
    determinant=(int(U[0,0])*int(U[1,1])-int(U[0,1])**2)%P
    rank=2 if determinant else 1
    assert np.any(U%P)
    lines=[(1,t) for t in range(P)]+[(0,1)]
    roots=[]
    for x in lines:
        q=int((O(x)@O(U)@O(x))%P)
        if q==0:roots.append(x)
    assert len(roots)==(1 if rank==1 else (0 if len(roots)==0 else 2))
    if rank==2:
        assert len(roots) in (0,2)
    return d,rank,roots,U

def toy_worlds():
    worlds=[
      ("anisotropic",np.asarray([[1,0],[0,2]],dtype=np.int64),0),
      ("rank1_radical",np.asarray([[1,0],[0,25]],dtype=np.int64),1),
      ("hyperbolic_positive_definite",np.asarray([[1,1],[1,5]],dtype=np.int64),2)
    ]
    result=[]
    for name,S,want_roots in worlds:
        assert S[0,0]>0 and int(S[0,0])*int(S[1,1])-int(S[0,1])**2>0
        scale,rank,roots,U=rank_and_isotropy(S)
        assert len(roots)==want_roots
        lines=[(1,t) for t in range(P)]+[(0,1)]
        outcomes=[intrinsic_flag(S,x) for x in lines]
        assert all(not z["censored"] for z in outcomes)
        if name=="anisotropic":assert all(
            z["exact_stage_cokernel_log5_order"]==0 for z in outcomes)
        if name=="rank1_radical":
            vertical=intrinsic_flag(S,(0,1))
            assert (vertical["norm_v5"],vertical["pairing_ideal_depth"],
                    vertical["exact_stage_cokernel_log5_order"])==(2,2,0)
        if name=="hyperbolic_positive_definite":
            assert intrinsic_flag(S,(1,0))[
                "exact_stage_cokernel_log5_order"]==0
            assert intrinsic_flag(S,(0,1))[
                "exact_stage_cokernel_log5_order"]==1
        result.append({"toy":name,"normalized_rank_mod5":rank,
                       "primitive_isotropic_projective_lines_mod5":roots,
                       "all_six_primitive_F5_flag_epsilon":[z[
                           "exact_stage_cokernel_log5_order"] for z in outcomes],
                       "source_independent_not_new_field_data":True})
    return result

def source_residuals(G,E,W):
    all_cases=[]
    original_flag_hist=Counter()
    six_flag_hist=Counter()
    rank_hist=Counter()
    rank2_root_hist=Counter()
    by_n=defaultdict(Counter)
    censored=0
    gauge_transports=0
    first=None
    candidates_count=0
    for n in FIRST:
        # One original old prefix plus its first obstructed row Z^n.
        assert gram_index.debt(G[:n,:n],G[:n,n:n+1])==1
        ids=list(range(n+1))
        A=G[np.ix_(ids,ids)]
        eold=E[ids]
        levels,diag,U,V=solver.tracked_smith_solver(A)
        assert max(levels)<K
        candidates=list(range(n+2,40,2))
        residuals={}
        projectors={}
        for r in candidates:
            C=G[np.ix_(ids,[r])]
            assert gram_index.debt(A,C)==0
            t,issues=solver.can_solve_or_fail(levels,diag,U,V,A,C,True)
            assert t is not None and not issues
            assert not np.any((O(A)@O(t)-O(C))%MOD)
            corrected=(O(E[[r]])-O(t).T@O(eold))%MOD
            assert not np.any(weighted(corrected,eold,W))
            residuals[r]=corrected
            projectors[r]=t
            candidates_count+=1
        for si,s in enumerate(candidates):
            for t in candidates[si+1:]:
                # Independently construct S in the ORIGINAL sample's
                # 218 weighted real-imag channels, no Smith metric lift.
                Es,Et=residuals[s],residuals[t]
                aa=int(weighted(Es,Es,W)[0,0])
                bb=int(weighted(Et,Et,W)[0,0])
                cc=int(weighted(Es,Et,W)[0,0])
                assert cc==int(weighted(Et,Es,W)[0,0])
                check_a=(int(G[s,s])-int((O(G[np.ix_(ids,[s])]).T@
                         O(projectors[s]))[0,0]))%MOD
                check_b=(int(G[t,t])-int((O(G[np.ix_(ids,[t])]).T@
                         O(projectors[t]))[0,0]))%MOD
                check_c=(int(G[s,t])-int((O(projectors[s]).T@
                         O(G[np.ix_(ids,[t])]))[0,0]))%MOD
                assert (aa,bb,cc)==(check_a,check_b,check_c)
                S=np.asarray([[aa,cc],[cc,bb]],dtype=np.int64)
                d,rank,roots,U5=rank_and_isotropy(S)
                determinant=(int(aa)*int(bb)-int(cc)*int(cc))%MOD
                determinant_censored=determinant==0
                canonical_a=intrinsic_flag(S,(1,0))
                canonical_b=intrinsic_flag(S,(0,1))
                assert not canonical_a["censored"] and not canonical_b["censored"]
                forward=canonical_a["exact_stage_cokernel_log5_order"]
                reverse=canonical_b["exact_stage_cokernel_log5_order"]
                assert forward==max(0,v5(aa)-v5(cc))
                assert reverse==max(0,v5(bb)-v5(cc))
                original_flag_hist[f"{forward}->{reverse}"]+=1
                rank_hist[rank]+=1
                rank2_root_hist[len(roots) if rank==2 else -1]+=1
                by_n[n][f"{rank}_rank-{len(roots)}_roots"]+=1
                flags=[]
                for x in [(1,k) for k in range(P)]+[(0,1)]:
                    info=intrinsic_flag(S,x)
                    if info["censored"]:
                        censored+=1
                        flags.append({"flag":x,"censored_at_16":True})
                        continue
                    e=info["exact_stage_cokernel_log5_order"]
                    six_flag_hist[e]+=1
                    gauge_transports+=change_basis_invariance(S,x,e)
                    if rank==2:
                        assert (e>0)==(x in roots)
                    if rank==2 and not roots:
                        assert e==0
                    flags.append({"flag":x,"epsilon":e,
                                  "norm_depth":info["norm_v5"],
                                  "pairing_ideal_depth":info["pairing_ideal_depth"]})
                item={
                  "original_first_bad_monomial":n,
                  "original_later_s":s,"original_later_t":t,
                  "original_residual_S_mod5pow16":S.tolist(),
                  "original_scale_v5":d,
                  "normalized_mod5_rank":rank,
                  "normalized_mod5_Gram":U5.tolist(),
                  "mod5_isotropic_primitive_projective_lines":roots,
                  "residual_det_v5_capped16":v5(determinant),
                  "residual_det_censored":determinant_censored,
                  "original_forward_flag_epsilon":forward,
                  "original_reverse_flag_epsilon":reverse,
                  "six_mod5_projective_flag_profiles":flags,
                  "all_source_vs_Schur_entries_match":True
                }
                all_cases.append(item)
                if (n,s,t)==(13,15,31):
                    first={"S":S,"Es":Es,"Et":Et,"A":A,"eold":eold,
                           "original_row_ids":ids,
                           "source_item":item}
    assert len(all_cases)==176 and candidates_count==43
    assert dict(original_flag_hist)=={
        "0->0":117,"0->1":31,"1->0":21,"1->1":7}
    assert gauge_transports==2*(6*176-censored)
    assert first is not None
    return {
       "source_all_176_binary_forms_checked":176,
       "original_43_integral_source_projection_vectors":43,
       "original_forward_reverse_flag_transition_counts":
           dict(sorted(original_flag_hist.items())),
       "mod5_normalized_rank_counts":dict(sorted(rank_hist.items())),
       "rank2_0_or_2_isotropic_lines_counts":
           dict(sorted(rank2_root_hist.items())),
       "projective_F5_six_flag_obstruction_histogram":
           dict(sorted(six_flag_hist.items())),
       "p16_censored_primitive_flags":censored,
       "exact_original_flag_and_GLn_transport_checks":
           gauge_transports,
       "per_original_first_bad_row_rank_isotropy_counts":{
           str(n):dict(sorted(by_n[n].items())) for n in FIRST},
       "original_exact_source_case_records":all_cases,
       "no_uniform_field_or_original_Gram_mass_inference":True
    },first

def hensel_source_flags(G,E,W,first):
    S=first["S"]
    E_s=first["Es"];E_t=first["Et"]
    ids=first["original_row_ids"]
    original_n=len(ids)
    scale,rank,roots,U5=rank_and_isotropy(S)
    assert scale==2 and rank==2 and len(roots)==2
    assert (0,1) in roots
    assert (v5(S[0,0]),v5(S[1,1]),v5(S[0,1]))==(2,3,2)
    assert int(U5[0,1])%P!=0
    def q(u):
        # E_x = u*E_s + E_t, ORIGINAL corrected observation row.
        return (int(S[0,0])*u*u+2*int(S[0,1])*u
                +int(S[1,1]))%MOD
    root=0
    source_id=ids+[15,31]
    assert len(source_id)==16
    Goriginal=G[np.ix_(source_id,source_id)]
    original_levels,_=smith.high_precision_smith(Goriginal)
    assert max(original_levels)<K
    source_old=E[ids]
    raw_s=E[[15]]
    raw_t=E[[31]]
    assert len(W)==218
    stages=[]
    for m in range(1,7):
        if m>1:
            candidates=[root+j*(P**(m-1)) for j in range(P)]
            solutions=[u for u in candidates
                       if q(u)%(P**(scale+m))==0]
            assert len(solutions)==1,(
                "simple F5 root did not have unique Hensel lift",m,solutions)
            root=solutions[0]
        assert q(root)%(P**(scale+m))==0
        x=(root,1)
        intrinsic=intrinsic_flag(S,x)
        assert not intrinsic["censored"]
        e=intrinsic["exact_stage_cokernel_log5_order"]
        assert intrinsic["pairing_ideal_depth"]==scale
        assert e>=m
        # Row-level original two-row GL2(Z) change: first x=root*Z15+Z31,
        # then y=Z15. det=-1. Original rank16 span UNCHANGED.
        T2=np.asarray([[root,1],[1,0]],dtype=object)
        T=np.eye(16,dtype=object)
        T[14:,14:]=T2
        Gnew=(T@O(Goriginal)@T.T)%MOD
        Ex=(root*O(raw_s)+O(raw_t))%MOD
        En=np.vstack((O(source_old),Ex,O(raw_s)))%MOD
        assert np.array_equal(weighted(En,En,W),Gnew)
        levels,_=smith.high_precision_smith(
            np.asarray(Gnew,dtype=np.int64))
        assert levels==original_levels
        oldstage=np.asarray(Gnew[:15,:15],dtype=np.int64)
        cross=np.asarray(Gnew[:15,15:16],dtype=np.int64)
        debt=gram_index.debt(oldstage,cross)
        assert debt==e,("actual original-row Gram debt vs intrinsic flag",
                        m,root,debt,e)
        Esres=(root*O(E_s)+O(E_t))%MOD
        assert int(weighted(Esres,Esres,W)[0,0])==q(root)
        assert int(weighted(Esres,E_s,W)[0,0])==(
            root*int(S[0,0])+int(S[0,1]))%MOD
        stages.append({
          "hensel_depth":m,
          "unimodular_original_flag_coefficient_root":root,
          "primitive_new_first_flag":f"{root}*Z^15+Z^31",
          "original_source_pairing_ideal_depth":scale,
          "original_source_new_norm_v5":intrinsic["norm_v5"],
          "actual_stage_image_log5":debt,
          "at_least_requested_hensel_depth":True,
          "original_full_16_row_Smith_unchanged":True,
          "original_E_trace_Gram_replayed":True
        })
        print("PHASE302_HENSEL_ORIGINAL_FLAG",stages[-1],flush=True)
    return {
      "source_original_case":[13,15,31],
      "original_residual_2x2_Gram_mod5pow9":[[int(S[i,j])%(P**9) for j in range(2)] for i in range(2)],
      "original_normalized_residual_mod5_Gram":U5.tolist(),
      "original_residual_det_v5":v5((int(S[0,0])*int(S[1,1])-int(S[0,1])**2)%MOD),
      "residual_mod5_rank":rank,
      "primitive_scale_depth":scale,
      "source_mod5_isotropic_lines":roots,
      "source_hensel_six_fixed_depths":stages,
      "original_full_16_row_p5_Smith_val":
          sum(original_levels),
      "new_frame_is_unimodular_integer_row_combination_NOT_new_monomial":True,
      "no_new_original_source_Gram_determinant_factor":True,
      "arbitrary_depth_is_P_paper_Hensel_not_finite_CI_measurement":True
    }

def main():
    freeze()
    field=original.field_h1_background()
    G,E,W,meta=original.original_j1_source()
    assert (meta["R"],meta["S"],meta["J"],meta["Q"])==(40,1,1,109)
    parity.symmetry(G,E,W)
    toys=toy_worlds()
    census,case=source_residuals(G,E,W)
    hensel=hensel_source_flags(G,E,W,case)
    # Keep final main log modest: full 176 records remain reproducible
    # from source; exact results are summary + selected source witness.
    census.pop("original_exact_source_case_records")
    print("PHASE302_ORIGINAL_FLAG_DIVISIBILITY_VERDICT",{
       "field_class_one_background":field,
       "original_integer_order_J1_Q109_trace_source":meta,
       "source_independent_anisotropic_rank1_split_toys":toys,
       "source_176_binary_residual_flag_census":census,
       "original_order_asymmetry_hensel_flag_approximations":hensel,
       "p5_binary_isotropy_known_local_form_theory":True,
       "NO_global_maximal_order_high_J_or_tenth_cutoff_claim":True
    },flush=True)
    print("PASS Phase302 primitive-line pairing depth, original source flags and six Hensel lifts",flush=True)

if __name__=="__main__":
    main()
