#!/usr/bin/env python3
"""Phase303-C: exact arithmetic applicability wall and elementary h1 controls.

Preregistered f3eccd01 BEFORE code or new field/sampler measurement.
This is a classical norm/split-prime obstruction and a source-policy
audit, NOT a new zero-free region or tenth discriminant bound.
"""
from math import isqrt
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
from source_probe import params

P=5
D=163
KNOWN_H1=(1,2,3,7,11,19,43,67,163)

def primes_under(bound):
    out=[]
    for n in range(2,bound):
        if all(n%p for p in range(2,isqrt(n)+1)):
            out.append(n)
    return out

def kronecker_split(D,p):
    """D ≡3 mod4; K=Q(sqrt(-D)), Δ=-D fundamental."""
    disc=-D
    if p==2:
        return "split" if disc%8==1 else (
          "inert" if disc%8==5 else "ramified")
    if D%p==0:return "ramified"
    sq={j*j%p for j in range(p)}
    return "split" if disc%p in sq else "inert"

def qmax_norm(D,a,b):
    assert D%4==3
    return a*a+a*b+((D+1)//4)*b*b

def source_policy():
    rows=[]
    for d in KNOWN_H1:
        if d%4!=3:
            rows.append({"D":d,"original_repo_params_admissible":False,
                         "why":"D mod4 !=3",
                         "original_source_R":None,
                         "original_source_J":None})
            continue
        rho,R,S,J,Q=params(d)
        rows.append({
           "D":d,
           "original_repo_params_admissible":True,
           "rho":rho,
           "original_source_R":R,
           "original_source_J":J,
           "original_source_S":S,
           "original_source_observations":len(Q)
        })
        assert J<=1
        if d!=163:assert J==0
        else:assert J==1 and R==40 and len(Q)==109
    assert max(x["original_source_J"] for x in rows
               if x["original_source_J"] is not None)==1
    # J=floor(R/25) >= 2 => R>=50 => D>=200, while all known
    # h1 imaginary quadratic radicands <=163.
    assert 163<200 and (200//4)//25>=2
    return {
        "known_heegner_radicands_as_classical_external_background":
            list(KNOWN_H1),
        "original_source_policy_per_class_one_field":rows,
        "largest_source_faithful_J_among_known_class_one_fields":1,
        "source_faithful_J_ge2_requires_D_at_least":200,
        "no_known_actual_h1_high_jet_source_under_original_formula":True,
        "class_number_one_classification_is_external_prior_art_NOT_this_programs_proof":True,
        "hypothetical_large_h1_field_theorems_need_uniform_arguments":True
    }

def exact_norm_prime_obstruction(D):
    assert D>3 and D%4==3
    lower=(D+1)//4
    primes=primes_under(lower)
    data={}
    for p in primes:
        status=kronecker_split(D,p)
        # A norm-p element is impossible: if b !=0, N(a+bω)
        # >= D*b*b/4, hence N >= (D+1)/4 for b odd; b even
        # gives N>=D*b*b/4 >= D when |b|>=2.
        # For b=0, N=a² can't be a rational prime.
        assert all(qmax_norm(D,a,b)!=p
                   for b in range(-2,3)
                   for a in range(-isqrt(lower)-2,isqrt(lower)+3))
        data[p]=status
    split=[p for p,s in data.items() if s=="split"]
    return {
      "field_D":D,
      "field_discriminant":-D,
      "fundamental_principal_norm_form":[1,1,lower],
      "strict_splitting_obstruction_prime_bound":lower,
      "all_primes_below_principal_norm_threshold":data,
      "split_primes_that_force_nonprincipal_prime_ideal":split,
      "if_h1_then_these_split_primes_must_be_empty":True,
      "no_new_nonexistence_theorem_for_arbitrarily_large_D":True
    }

def matched_arithmetic_h1_and_counterworld():
    yes=exact_norm_prime_obstruction(163)
    no=exact_norm_prime_obstruction(23)
    assert not yes["split_primes_that_force_nonprincipal_prime_ideal"]
    assert no["split_primes_that_force_nonprincipal_prime_ideal"]==[2,3]
    # In Qsqrt(-23), delta=-23 ≡1 mod8 so 2 splits, but
    # principal norm a²+ab+6b² cannot equal 2.
    assert (-23)%8==1
    assert all(qmax_norm(23,a,b)!=2
               for a in range(-5,6) for b in range(-2,3))
    return {
       "genuine_h1_D163_control":yes,
       "hostile_D23_split_two_nonprincipal_counterworld":no,
       "primitive_split_prime_norm_obstruction_is_classical":True,
       "no_field_cutoff_from_fixed_D163_source_Gram":True
    }

def order_change_multiplication():
    # Direct ring-level check of the conductor2 coordinate map,
    # independent of the E/Gram source code in Phase303-A.
    def oldmul(x,y):
        a,b=x;c,d=y
        return (a*c-163*b*d,a*d+b*c)
    def om(x,y):
        a,b=x;c,d=y
        return (a*c-41*b*d,a*d+b*c+b*d)
    def phi(q):
        x,y=q
        return (x-y,2*y)
    checked=0
    for a in range(-2,3):
        for b in range(-2,3):
            for c in range(-2,3):
                for d in range(-2,3):
                    assert phi(oldmul((a,b),(c,d)))==om(phi((a,b)),phi((c,d)))
                    checked+=1
    # Trace Gram congruence, p5-local order index:
    # T=[[1,-1],[0,2]], Bw=[[2,1],[1,82]],
    # T^t Bw T=diag(2,326), detT=2 a 5-adic unit.
    T=((1,-1),(0,2))
    B=((2,1),(1,82))
    left=[[sum(T[k][i]*B[k][l]*T[l][j]
               for k in range(2) for l in range(2))
           for j in range(2)]for i in range(2)]
    assert left==[[2,0],[0,326]]
    assert 2%P!=0
    return {
      "exact_multiplication_conductor2_coordinate_checks":checked,
      "original_old_trace_Gram_congruence":left,
      "local_order_index2_is_p5_unit":True,
      "integer_order_not_equal_maximal_order_at_p2":True,
      "finite_observation_support_must_be_tracked_separately":True
    }

def main():
    policies=source_policy()
    arithmetic=matched_arithmetic_h1_and_counterworld()
    local=order_change_multiplication()
    print("PHASE303C_ACTUAL_H1_NORM_AND_SOURCE_FEASIBILITY",{
      "source_original_policy":policies,
      "arithmetic_class_number_one_split_prime_controls":arithmetic,
      "maximal_order_vs_original_suborder_exact_ring_map":local,
      "logical_status_of_field_prior_art":"classical, not independently Lean-checked here",
      "tenth_discriminant_existing_integrated_bound": "322^4",
      "higher_jet_h1_uniform_field_bridge":"OPEN",
      "NO new field cutoff":True
    },flush=True)
    print("PASS Phase303-C maximal-order field arithmetic and high-J h1 feasibility wall",flush=True)

if __name__=="__main__":
    main()
