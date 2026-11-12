#!/usr/bin/env python3
"""Phase294-A: finite p-adic tower of original sampling-support debt.

Pre-registered at commit 97821fec BEFORE implementation/results.
This is a multiset/point-matching obstruction, NOT Gram valuation mass.
"""
from collections import Counter, defaultdict, deque
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
from source_probe import params

P=5
D_A=583
D_B=587
MAX_K=13
FROZEN_SOURCE="3f954b59d9f86b06ad53667c869b5b24f2e6c7f6"

def source_guard():
    actual=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase206/source_probe.py"],
        cwd=ROOT,text=True).strip()
    assert actual==FROZEN_SOURCE,("original source changed",actual)

def hensel_lifts(max_k=MAX_K, initial=2):
    """Compute the chosen exact 5-adic root 583*alpha^2=587."""
    assert initial%P in (2,3)
    alpha=initial%P
    assert (D_A*alpha*alpha-D_B)%P==0
    out=[]
    for k in range(1,max_k+1):
        mod=P**k
        assert (D_A*alpha*alpha-D_B)%mod==0
        out.append((k,mod,alpha))
        if k==max_k:break
        deriv=(2*D_A*alpha)%P
        assert deriv!=0
        error=D_B-D_A*alpha*alpha
        assert error%mod==0
        digit=((error//mod)%P)*pow(deriv,-1,P)%P
        alpha+=mod*digit
    return out

def residue_counter(points,mod,alpha=1):
    return Counter((x%mod,(alpha*y)%mod) for x,y in points)

def debt_from_counters(A,B):
    assert sum(A.values())==sum(B.values())
    matched=sum(min(A[key],B[key]) for key in A.keys()|B.keys())
    l1=sum(abs(A[key]-B[key]) for key in A.keys()|B.keys())
    assert l1==2*(sum(A.values())-matched)
    return sum(A.values())-matched,matched

def matching_by_residue(points,alpha,mod):
    """Actual independent-labeled point pairs, selected deterministically."""
    available=defaultdict(deque)
    for i,(x,y) in enumerate(points):
        available[(x%mod,y%mod)].append(i)
    pairs=[]
    unmatched_right=[]
    for j,(x,y) in enumerate(points):
        key=(x%mod,(alpha*y)%mod)
        if available[key]:
            pairs.append((available[key].popleft(),j))
        else:
            unmatched_right.append(j)
    consumed={i for i,j in pairs}
    unmatched_left=[i for i in range(len(points)) if i not in consumed]
    assert len(unmatched_left)==len(unmatched_right)
    assert all(
        (points[i][0]-points[j][0])%mod==0 and
        (points[i][1]-alpha*points[j][1])%mod==0
        for i,j in pairs
    )
    return pairs,unmatched_left,unmatched_right

def bipartite_maximum_matching(points,alpha,mod):
    """Separate augmenting-path matching oracle; no Counter used here."""
    n=len(points)
    adj=[]
    for x,y in points:
        adj.append([j for j,(a,b) in enumerate(points)
                    if (x-a)%mod==0 and (y-alpha*b)%mod==0])
    left=[-1]*n
    right=[-1]*n
    distance=[-1]*n
    def bfs():
        queue=deque()
        free=False
        for i in range(n):
            if left[i]==-1:
                distance[i]=0
                queue.append(i)
            else:distance[i]=-1
        while queue:
            i=queue.popleft()
            for j in adj[i]:
                mate=right[j]
                if mate==-1:free=True
                elif distance[mate]<0:
                    distance[mate]=distance[i]+1
                    queue.append(mate)
        return free
    def dfs(i):
        for j in adj[i]:
            mate=right[j]
            if mate==-1 or (distance[mate]==distance[i]+1 and dfs(mate)):
                left[i]=j
                right[j]=i
                return True
        distance[i]=-1
        return False
    matched=0
    while bfs():
        for i in range(n):
            if left[i]==-1 and dfs(i):matched+=1
    assert matched==sum(i!=-1 for i in left)==sum(j!=-1 for j in right)
    return matched

def negative_controls(Q,lifts):
    for k,mod,alpha in lifts:
        A=residue_counter(Q,mod)
        for trivial in (+1,-1):
            assert debt_from_counters(A,residue_counter(Q,mod,trivial))[0]==0
        only_center=[(x,y) for x,y in Q if y==0]
        assert len(only_center)==107
        assert debt_from_counters(
            residue_counter(only_center,mod),
            residue_counter(only_center,mod,alpha))[0]==0
    full_grid=[(x,y) for x in range(-2,3) for y in range(-2,3)]
    assert len(full_grid)==25
    d1,_=debt_from_counters(
        residue_counter(full_grid,5),
        residue_counter(full_grid,5,lifts[0][2]))
    d2,_=debt_from_counters(
        residue_counter(full_grid,25),
        residue_counter(full_grid,25,lifts[1][2]))
    assert (d1,d2)==(0,20)
    # This Frobenius-divided source row is integer at all REAL-axis
    # integer sampling points, but is NOT 1-Lipschitz over Z_5.
    f=lambda x:(x**5-x)//5
    assert f(0)==0 and f(5)==624 and f(5)%5==4
    assert 0%5==5%5
    assert (0,0) in Q and (5,0) in Q
    assert (f(5)-f(0))%5!=0
    return {
      "trivial_local_frames_alpha_plus_minus_one_debt_zero":True,
      "centerline_points_match_all_precision":107,
      "full_5x5_grid_depth1_compatible_depth2_fails":[0,20],
      "original_real_axis_Frobenius_divided_counterexample":{
         "original_points":[[0,0],[5,0]],"f5_at_first":0,
         "f5_at_second":624,"difference_mod5":4
      },
      "raw_points_mod5_do_not_determine_divided_source_mod5":True
    }

def main():
    source_guard()
    params_a=params(D_A)
    params_b=params(D_B)
    rho_a,ra,sa,ja,Qa=params_a
    rho_b,rb,sb,jb,Qb=params_b
    assert (rho_a,ra,sa,ja,len(Qa))==(53,145,5,5,383)
    assert (rho_b,rb,sb,jb,len(Qb))==(53,146,5,5,383)
    assert Qa==Qb
    Q=Qa
    assert len(Q)==len(set(Q))==383
    counts=Counter(y for x,y in Q)
    assert counts=={-2:43,-1:95,0:107,1:95,2:43}
    lifts=hensel_lifts()
    assert lifts[:3]==[(1,5,2),(2,25,17),(3,125,67)]
    assert len(lifts)==MAX_K
    controls=negative_controls(Q,lifts)

    tower=[]
    debt_previous=0
    for k,mod,alpha in lifts:
        A=residue_counter(Q,mod)
        B=residue_counter(Q,mod,alpha)
        debt,matched=debt_from_counters(A,B)
        pairs,ua,ub=matching_by_residue(Q,alpha,mod)
        assert len(pairs)==matched and len(ua)==len(ub)==debt
        assert debt>=debt_previous
        predicted=(104 if k==1 else 276)
        assert debt==predicted,(k,debt,predicted)
        # The *other* local square-root branch must give the SAME debt,
        # since the original Q is invariant under imaginary y->-y.
        other=debt_from_counters(A,residue_counter(Q,mod,-alpha))[0]
        assert other==debt
        if k in (1,2,3):
            independent=bipartite_maximum_matching(Q,alpha,mod)
            assert independent==matched
        else:independent=None
        if k>=2:
            assert matched==107
            assert all(Q[i][1]==0 and Q[j][1]==0 for i,j in pairs)
        canonical_sha=sha256(json.dumps(
            pairs,separators=(",",":")
        ).encode()).hexdigest()
        tower.append({
            "precision_power":k,
            "modulus":mod,
            "alpha_residue":alpha,
            "original_points_each":len(Q),
            "maximum_residue_point_matches":matched,
            "minimum_unmatched_original_points_each_side":debt,
            "minimum_added_points_each_side_for_equal_multisets":debt,
            "minimum_common_envelope_point_count":len(Q)+debt,
            "unmatched_original_coordinate_channels_each_side":2*ja*debt,
            "independent_bipartite_maximum_matches":independent,
            "canonical_maximal_partial_matching_sha256":canonical_sha,
        })
        debt_previous=debt
    assert [x["minimum_unmatched_original_points_each_side"] for x in tower]==[
        104]+[276]*12
    assert tower[1]["minimum_unmatched_original_points_each_side"]-tower[0][
        "minimum_unmatched_original_points_each_side"]==172
    assert MAX_K==K_SOURCE_NUMERATOR
    print("PHASE294_SUPPORT_DEBT_TOWER",{
       "original_D583_complete_rows":ra*sa,
       "original_D587_complete_rows_NOT_COMPARABLE":rb*sb,
       "original_Q_literal_equal":True,
       "original_all_jet_orders":ja,
       "matched_row_diagnostic_only":True,
       "source_numerator_precision_K":K_SOURCE_NUMERATOR,
       "tower":tower,
       "controls":controls,
       "proof_scope":"residue multiset and point-by-point transport only",
       "no_primitive_pairing_or_actual_field_valuation_added":True
    },flush=True)
    print("PASS Phase294-A monotone p-adic point-support debt tower with 13 exact levels",
          flush=True)

# p^9 secondary source precision + max old Frobenius k=4.
K_SOURCE_NUMERATOR=13

if __name__=="__main__":
    main()
