#!/usr/bin/env python3
"""Phase303-F: independent HALF-INTEGRAL (p,q) source + DVR Smith oracle.

Preregistered at 4c5fc499 BEFORE this code. This arithmetic core
does not use omega-basis multiplication, numpy, original Smith,
or source_probe. Reference source is imported ONLY AFTER results.
"""
from collections import Counter
from math import isqrt
from pathlib import Path
import subprocess
import sys

D=163
CUT=441
N=40
P=5
K=16
MOD=5**16
ROOT=Path(__file__).resolve().parents[2]
FROZEN_REF="e68f66dac1c914a97c0fe93655a693053f80386f"

def mult(x,y):
    p,q=x;r,s=y
    a=p*r-D*q*s
    b=p*s+q*r
    assert a%2==0 and b%2==0,(
        "half integral algebra product not integral",x,y)
    return (a//2,b//2)

def norm(x):
    p,q=x
    n=p*p+D*q*q
    assert n%4==0,("integral algebraic norm failed",x)
    return n//4

def inner(x,y):
    p,q=x;r,s=y
    t=p*r+D*q*s
    assert t%2==0
    return t//2

def enumerated_half_integral_points():
    # N=(p²+Dq²)/4. |q|<=3 and |p|<=42 exactly.
    assert D*4*4>4*CUT
    Q=[]
    for q in range(-3,4):
        for p in range(-44,45):
            if (p-q)%2:continue
            if p*p+D*q*q<=4*CUT:
                Q.append((p,q))
    assert len(Q)==len(set(Q))
    assert all(norm(x)<=CUT for x in Q)
    assert all(p*p+D*q*q>4*CUT for q in range(-3,4)
               for p in (-45,45,46,-46))
    even=[z for z in Q if z[1]%2==0]
    odd=[z for z in Q if z[1]%2!=0]
    assert (len(Q),len(even),len(odd))==(225,109,116)
    return Q,even,odd

def independent_exact_integer_gram(Q):
    powers=[]
    for z in Q:
        p=[(2,0)]
        for k in range(1,N):
            p.append(mult(p[-1],z))
        assert norm(z)*2==inner(z,z)
        powers.append(p)
    G=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i,N):
            g=sum(inner(powers[q][i],powers[q][j])
                  for q in range(len(Q)))
            G[i][j]=G[j][i]=g
    assert all(G[i][j]==G[j][i]
               for i in range(N) for j in range(N))
    return G

def vp5_mod(x):
    x=int(x)%MOD
    if not x:return K
    v=0
    while x%5==0:
        v+=1;x//=5
    return v

def independent_dvr_smith(G):
    """Over Z/5^16: elementary row/column operations, pure Python.

    Pivot with minimum valuation in the remaining submatrix, clear
    row and column by unit inverses modulo 5^(16-e), preserving all
    lower elementary divisors. NEVER import NumPy/old Smith code.
    """
    n=len(G)
    assert all(len(row)==n for row in G)
    A=[[int(G[i][j])%MOD for j in range(n)]for i in range(n)]
    levels=[]
    for k in range(n):
        pivot=None
        for i in range(k,n):
            for j in range(k,n):
                v=vp5_mod(A[i][j])
                if pivot is None or v<pivot[0]:
                    pivot=(v,i,j)
        assert pivot is not None
        e,i,j=pivot
        assert e<K,("smith source censored at original K16",k,e)
        A[k],A[i]=A[i],A[k]
        for row in A:
            row[k],row[j]=row[j],row[k]
        z=A[k][k]
        assert vp5_mod(z)==e
        pp=5**e
        quotient=MOD//pp
        unit=(z//pp)%quotient
        inv=pow(unit,-1,quotient)
        for r in range(k+1,n):
            x=A[r][k]
            assert x%pp==0
            c=(x//pp)*inv%quotient
            if c:
                for t in range(k,n):
                    A[r][t]=(A[r][t]-c*A[k][t])%MOD
            assert A[r][k]==0
        for cidx in range(k+1,n):
            x=A[k][cidx]
            assert x%pp==0
            c=(x//pp)*inv%quotient
            if c:
                for r in range(k,n):
                    A[r][cidx]=(A[r][cidx]-c*A[r][k])%MOD
            assert A[k][cidx]==0
        assert all(A[k][t]==0 and A[t][k]==0 for t in range(k+1,n))
        levels.append(e)
    assert levels==sorted(levels)
    return levels,dict(sorted(Counter(levels).items()))

def adversarial_smith_oracle():
    controls=[
      ([[0,5],[5,0]],{1:2}),
      ([[0,5,0],[5,0,0],[0,0,25]],{1:2,2:1}),
      ([[10,2],[2,2]],{0:2}),
      ([[1,0,0],[0,25,0],[0,0,125]],{0:1,2:1,3:1})
    ]
    results=[]
    for G,expected in controls:
        grades,hist=independent_dvr_smith(G)
        assert hist==expected,(G,hist,expected)
        results.append({"shape":len(G),
                        "expected":expected,
                        "independent_result":hist})
    return results

def compare_after_independent_results(Q,even,Geven,Gfull,sm_even,sm_full):
    # Only here import the earlier AI code; both the alternate SOURCE
    # and standalone Smith profiles are already fully constructed.
    sys.path.insert(0,str(ROOT/"research"/"phase303"))
    import maximal_order_source as reference
    reference.freeze()
    expected_sha=subprocess.check_output(
      ["git","rev-parse","HEAD:research/phase303/maximal_order_source.py"],
      cwd=ROOT,text=True).strip()
    assert expected_sha==FROZEN_REF
    reference_arms=reference.all_arms()
    mapping_full=[(2*a+b,b)for a,b in reference_arms["Qfull"]]
    mapping_even=[(2*a+b,b)for a,b in reference_arms["Qeven"]]
    assert Q==mapping_full and even==mapping_even
    for A,B,label in ((Geven,reference_arms["G_even"],"even"),
                      (Gfull,reference_arms["G_full"],"full")):
        for i in range(N):
            for j in range(N):
                assert int(A[i][j])==int(B[i,j]),(
                   "independent half-integer Gram disagrees with omega",
                   label,i,j,A[i][j],int(B[i,j]))
    assert sm_even=={0:15,2:8,3:7,4:10}
    assert sm_full=={0:25,2:15}
    return {
       "original_vs_alternate_source_pairs_match_all":225,
       "original_even_vs_alternate_pairs_match_all":109,
       "all_independent_big_integer_Gram_cells_match_each_arm":3200,
       "no_reuse_of_omega_multiplication_in_standalone_engine":True,
       "no_reuse_of_original_Smith_in_independent_core":True,
       "not_independent_human_peer_review":True
    }

def main():
    controls=adversarial_smith_oracle()
    Q,even,odd=enumerated_half_integral_points()
    Geven=independent_exact_integer_gram(even)
    Gfull=independent_exact_integer_gram(Q)
    level_even,hist_even=independent_dvr_smith(Geven)
    level_full,hist_full=independent_dvr_smith(Gfull)
    assert hist_even=={0:15,2:8,3:7,4:10}
    assert hist_full=={0:25,2:15}
    assert (sum(level_even),sum(level_full))==(77,30)
    print("PHASE303F_INDEPENDENT_CALCULATED_BEFORE_REFERENCE",{
        "alternative_half_integral_source_total":len(Q),
        "original_even_source_points":len(even),
        "genuinely_new_odd_numerators":len(odd),
        "standalone_old_Smith":hist_even,
        "standalone_full_Smith":hist_full,
        "standalone_old_Gram_v5":sum(level_even),
        "standalone_full_Gram_v5":sum(level_full),
        "hostile_modular_Smith_controls":controls,
        "original_sources_not_imported_before_this_record":True
    },flush=True)
    compare=compare_after_independent_results(
        Q,even,Geven,Gfull,hist_even,hist_full)
    print("PHASE303F_HALF_INTEGRAL_INDEPENDENT_REPLAY_VERDICT",{
       "original_full_source_field_D":D,
       "norm_cutoff":CUT,
       "comparison_with_frozen_omega_source_after_independent_calculation":
           compare,
       "no_censored_p16_smith_factors":True,
       "no_unproved_class_one_uniform_theorem":True,
       "no_original_field_bound_changed":True
    },flush=True)
    print("PASS Phase303-F independent (p,q) maximal-order Gram and DVR Smith",flush=True)

if __name__=="__main__":
    main()
