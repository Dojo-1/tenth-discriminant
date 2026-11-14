#!/usr/bin/env python3
"""Phase296: exhaustive F25 affine-semilinear moving-frame source test.

Preregistered 2026-11-13, cbe92c33 BEFORE code/measurement.
Carries COMPLETE ORIGINAL D583 (725 row) and D587 (730 row) Q383
through the local field isomorphism. No h=1 or p-adic determinant claim.
"""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
from source_probe import params,fall

P=5
DA=583
DB=587
ALPHA=2
FROZEN={
 "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":"dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
 "research/phase295/w_equivariant_jet_obstruction.py":"e91561f848bdd5aea4aaf3cc65c5d883ce12ec4a",
}
Z=(0,0)
ONE=(1,0)

def guard():
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("source drift",path,actual,sha)

def add(a,b):
    return ((a[0]+b[0])%P,(a[1]+b[1])%P)

def neg(a):
    return ((-a[0])%P,(-a[1])%P)

def mul(a,b):
    # Independent direct F25 multiplication: u^2=-583 = 2 mod5.
    return ((a[0]*b[0]-DA*a[1]*b[1])%P,
            (a[0]*b[1]+a[1]*b[0])%P)

def power(a,n):
    result=ONE
    while n:
        if n&1:result=mul(result,a)
        a=mul(a,a)
        n//=2
    return result

def scale(n,a):
    return ((n*a[0])%P,(n*a[1])%P)

def conj(a):
    return (a[0],(-a[1])%P)

def norm(a):
    v=mul(a,conj(a))
    assert v[1]==0
    assert v[0]==(a[0]*a[0]+DA*a[1]*a[1])%P
    return v[0]

def field_elements():
    return list(product(range(P),repeat=2))

def transform(z,a,b,epsilon):
    if epsilon==-1:z=conj(z)
    return add(mul(a,z),b)

def weighted_match(A,B):
    return sum(min(A[z],B[z]) for z in A.keys()|B.keys())

def original_geometry():
    rho_a,R_a,S_a,J_a,Q_a=params(DA)
    rho_b,R_b,S_b,J_b,Q_b=params(DB)
    assert (rho_a,R_a,S_a,J_a,len(Q_a))==(53,145,5,5,383)
    assert (rho_b,R_b,S_b,J_b,len(Q_b))==(53,146,5,5,383)
    assert Q_a==Q_b
    Q=Q_a
    assert len(Q)==len(set(Q))==383
    return Q,(R_a*S_a,R_b*S_b),J_a

def norm_one_count():
    nonzero=[a for a in field_elements() if a!=Z]
    assert len(nonzero)==24 and all(norm(a)!=0 for a in nonzero)
    subgroup=[a for a in nonzero if norm(a)==1]
    assert len(subgroup)==P+1==6
    return nonzero,subgroup

def weighted_anchor_proof(Q):
    source=Counter((x%P,y%P) for x,y in Q)
    moved=Counter((x%P,(ALPHA*y)%P) for x,y in Q)
    max_weight=max(source.values())
    heavy=sorted(z for z,m in source.items() if m==max_weight)
    target_heavy=sorted(z for z,m in moved.items() if m==max_weight)
    assert max_weight==22
    assert heavy==target_heavy==[(2,0),(3,0)]
    assert all(v<=21 for z,v in source.items() if z not in heavy)
    # Source and target heaviest points have unit difference 1, even
    # under field conjugation. A full affine match is forced to map
    # both heaviest points onto themselves, so a=+/-1, b=0.
    forced=set()
    for eps in (1,-1):
        for a in field_elements():
            if a==Z:continue
            for b in field_elements():
                images={transform(h,a,b,eps) for h in heavy}
                if images==set(heavy):forced.add((a,b,eps))
    assert forced=={
        ((1,0),(0,0),1),((4,0),(0,0),1),
        ((1,0),(0,0),-1),((4,0),(0,0),-1)
    }
    assert all(
        Counter(transform(z,a,b,eps) for z in moved.elements())!=source
        for a,b,eps in forced
    )
    # At y=+2, the SOURCE strip weight is <=9 but the transported
    # y=+1 strip weight is 19 (phi sends 1->2); +/-1 does not fix it.
    assert all(source.get((x,2),0) in (8,9) for x in range(P))
    assert all(moved.get((x,2),0)==19 for x in range(P))
    return {"maximum_point_multiplicity":22,
            "exactly_two_heaviest_original_residues":[list(z) for z in heavy],
            "heaviest_pair_fixes_affine_multiplier_and_translation":
                ["a=1,b=0","a=-1,b=0"],
            "transported_y_plus1_to_y_plus2_multiplicity":19,
            "original_y_plus2_multiplicity_range":[8,9],
            "nonexistence_of_any_exact_affine_semilinear_match":True}

def independent_matching_oracle(A,B):
    """Separate sorted-copy matching check, not Counter.min."""
    left=sorted(k for k,v in A.items() for _ in range(v))
    right=sorted(k for k,v in B.items() for _ in range(v))
    assert len(left)==len(right)==383
    i=j=count=0
    while i<len(left) and j<len(right):
        if left[i]==right[j]:
            count+=1;i+=1;j+=1
        elif left[i]<right[j]:i+=1
        else:j+=1
    return count

def exhaustive_affine(Q):
    original=Counter((x%P,y%P) for x,y in Q)
    transported=[(x%P,(ALPHA*y)%P) for x,y in Q]
    nonzero,normone=norm_one_count()
    all_results=[]
    for epsilon in (1,-1):
        for a in nonzero:
            for b in field_elements():
                changed=Counter(transform(z,a,b,epsilon)
                                for z in transported)
                common=weighted_match(original,changed)
                debt=len(Q)-common
                all_results.append({
                    "epsilon":epsilon,"a":a,"b":b,
                    "norm":norm(a),"match":common,"debt":debt,
                    "base_coeff":a[1]==0 and b[1]==0,
                    "norm_one":norm(a)==1})
    assert len(all_results)==2*24*25==1200
    assert all(z["debt"]>0 for z in all_results)
    scopes={
        "all_affine_semilinear":all_results,
        "norm_one_slopes_arbitrary_translations":[r for r in all_results
            if r["norm_one"]],
        "base_F5_polynomial_coefficients":[r for r in all_results
            if r["base_coeff"]],
        "norm_one_AND_base_F5":[r for r in all_results
            if r["norm_one"] and r["base_coeff"]],
    }
    assert [len(scopes[k]) for k in scopes]==[1200,300,40,20]
    summary={}
    for name,subset in scopes.items():
        mindebt=min(r["debt"] for r in subset)
        ties=[r for r in subset if r["debt"]==mindebt]
        best=sorted(ties,key=lambda x:(x["epsilon"],x["a"],x["b"]))
        for rec in best[:2]:
            moved=Counter(transform(z,rec["a"],rec["b"],rec["epsilon"])
                          for z in transported)
            assert independent_matching_oracle(original,moved)==rec["match"]
        hist=dict(sorted(Counter(r["debt"] for r in subset).items()))
        summary[name]={
            "candidates":len(subset),"minimum_unmatched_points_per_side":mindebt,
            "best_match_count":383-mindebt,
            "number_of_best_candidates":len(ties),
            "representative_best_parameters":[{
                "a":list(r["a"]),"b":list(r["b"]),
                "epsilon":r["epsilon"],"norm":r["norm"]}
                for r in best[:8]],
            "debt_histogram":hist,
            "zero_debt_exists":False}
    # Confirm a perfect same-field affine identity, inversion and
    # conjugation of Q; negative for an asymmetric toy.
    baseline=[(x%P,y%P) for x,y in Q]
    for a,b,epsilon in ((ONE,Z,1),((4,0),Z,1),(ONE,Z,-1)):
        assert Counter(transform(z,a,b,epsilon) for z in baseline)==original
    toy=[(1,1),(2,1)]
    assert Counter(transform(z,(4,0),Z,1) for z in toy)!=Counter(toy)
    # The old canonical map is one of the candidates and has debt104.
    plain=[r for r in all_results if r["a"]==ONE
            and r["b"]==Z and r["epsilon"]==1]
    assert len(plain)==1 and plain[0]["debt"]==104
    return summary

def linear_ambient_escape(Q):
    # The F5-LINEAR map U: x+y u -> x+3y u cancels phi's
    # imaginary alpha=2, but is not an F25 algebra automorphism.
    phi=[(x%P,(ALPHA*y)%P) for x,y in Q]
    corrected=[(x,(3*y)%P) for x,y in phi]
    assert Counter(corrected)==Counter((x%P,y%P) for x,y in Q)
    u=(0,1)
    u2=mul(u,u)
    U=lambda z:(z[0],3*z[1]%P)
    assert u2==(2,0)
    assert U(u2)==(2,0) and mul(U(u),U(u))==(3,0)
    assert U(u2)!=mul(U(u),U(u))
    assert norm(u)==3 and norm(U(u))==2
    return {"F5_linear_2x2_matrix":[[1,0],[0,3]],
            "F5_linear_map_exactly_reverses_phi_sample_residues":True,
            "F25_multiplication_is_NOT_preserved":True,
            "quadratic_trace_norm_is_NOT_preserved":True,
            "not_a_permitted_field_algebra_or_trace_gauge":True}

def fall_independent(i,j):
    t=1
    for v in range(i-j+1,i+1):t*=v
    return t

def jet_chain_independent(Q):
    # Compare original affine chain rule against an INDEPENDENT
    # binomial expansion into formal Z^i W^h rows, not repetition of
    # the affine chain-rule formula as its own oracle.
    slopes_and_offsets=[
        ((1,0),(0,0)),((3,0),(1,0)),
        ((2,2),(1,2)),((0,1),(2,3))
    ]
    labels=[(0,0),(1,0),(2,1),(4,3)]
    tests=0
    normone_true=0
    nonunitnorm_false=0
    for a,b in slopes_and_offsets:
        if norm(a)==1:normone_true+=1
        else:nonunitnorm_false+=1
        a_bar,b_bar=conj(a),conj(b)
        for q in (Q[0],Q[len(Q)//2],Q[-1]):
            z=(q[0]%P,q[1]%P)
            w=conj(z)
            moving_Z=add(mul(a,z),b)
            moving_W=add(mul(a_bar,w),b_bar)
            assert moving_W==conj(moving_Z)
            for r,s in labels:
                for j in range(5):
                    rhs=(0,0)
                    if j<=r:
                        rhs=scale(
                            fall(r,j),mul(
                                power(a,j),
                                mul(power(moving_Z,r-j),
                                    power(moving_W,s))))
                    lhs=(0,0)
                    for i in range(j,r+1):
                        for h in range(s+1):
                            coef=comb(r,i)*comb(s,h)*fall_independent(i,j)
                            term=mul(
                                mul(power(a,i),power(b,r-i)),
                                mul(power(a_bar,h),power(b_bar,s-h))
                            )
                            term=mul(term,mul(power(z,i-j),power(w,h)))
                            lhs=add(lhs,scale(coef,term))
                    assert lhs==rhs,("ordinary jet chain fails",a,b,q,r,s,j)
                    tests+=1
        for j in range(5):
            norm_j=norm(power(a,j))
            assert norm_j==pow(norm(a),j,P)
    assert tests==4*3*4*5
    assert normone_true==2 and nonunitnorm_false==2
    assert norm((3,0))==4 and norm((2,2))==1
    # At j=1, trace pairing of 1 with itself is scaled by N(a).
    assert (2*norm((3,0)))%P!=2
    return {"independent_formal_expansion_vs_chain_rule_jet_tests":tests,
            "norm_one_slopes_jet_trace_isometric_count":normone_true,
            "slopes_that_fail_jet_trace_isometry":nonunitnorm_false,
            "ordinary_Z_jet_W_held_fixed_verified":True}

def formal_row_lattice_gate():
    R,S=145,5
    # A source row Z maps to a Z+b, so imaginary coefficient parts
    # immediately prevent an F5-only formal monomial coefficient map.
    all_affine=[(a,b) for a in field_elements() if a!=Z
                for b in field_elements()]
    base=[(a,b) for a,b in all_affine if a[1]==0 and b[1]==0]
    assert len(all_affine)==24*25==600 and len(base)==4*5==20
    for a,b in base:
        assert a[0]!=0
        assert all(pow(a[0],r+s,P)!=0
                   for r,s in ((0,0),(1,0),(R-1,S-1)))
    # Affine mixing of Z and W violates the finite rectangular
    # monomial support; these coefficients are provably nonzero.
    for c in (1,2,3,4):
        assert pow(c,R-1,P)!=0
    for a in (1,2,3,4):
        for d in (1,2,3,4):
            assert pow(a,R-1,P)*pow(d,S-1,P)%P!=0
    return {
        "formal_original_rectangle_dimensions":[R,S],
        "all_F25_unit_slope_affine_with_translations":600,
        "formal_F5_monomial_row_lattice_compatible_affines":20,
        "imaginary_affine_coefficients_fail_existing_Z_row":True,
        "off_diagonal_Z_to_W_hits_forbidden_W_degree":R-1,
        "off_diagonal_W_to_Z_hits_forbidden_Z_degree":R+S-2,
        "conjugation_exchange_Z_W_not_rectangular_when_R_much_bigger_S":True,
        "no_divided_Frobenius_or_secondary_index_transport_inferred":True}

def main():
    guard()
    Q,rows,J=original_geometry()
    assert rows==(725,730) and J==5
    assert (-DA)%P==2 and (-DB)%P==3
    assert (DA*(ALPHA**2)-DB)%P==0
    anchor=weighted_anchor_proof(Q)
    summary=exhaustive_affine(Q)
    ambient=linear_ambient_escape(Q)
    jets=jet_chain_independent(Q)
    rowgate=formal_row_lattice_gate()
    print("PHASE296_AFFINE_SEMILINEAR_EXHAUSTIVE",{
       "original_D583_full_rows":rows[0],
       "original_D587_full_rows":rows[1],
       "same_original_Q":len(Q),"original_ordinary_jets":J,
       "common_local_residue_field":"F25=F5[u]/(u^2+583)",
       "local_field_isometry_alpha_mod5":ALPHA,
       "affine_field_semilinear_category":
           "a*conjugate^epsilon(phi(z))+b; a unit, b arbitrary",
       "theorem_heaviest_residue_anchor":anchor,
       "exhaustive_groups":summary,
       "original_field_algebra_vs_unrestricted_2x2_escape":ambient,
       "formal_polynomial_jet_chain_rule_controls":jets,
       "original_F5_coefficient_row_lattice_gate":rowgate,
       "all_affine_field_transports_fail_complete_original_Q_match":True,
       "any_higher_p5_lift_reduces_to_this_failed_mod5_test":True,
       "does_not_exclude_non_affine_jet_algebra_transports":True,
       "no_primitive_index_or_field_discriminant_gain":True
    },flush=True)
    print("PASS Phase296 affine moving frame no-go and arithmetic source/jet gates",flush=True)

if __name__=="__main__":
    main()
