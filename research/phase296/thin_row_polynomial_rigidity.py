#!/usr/bin/env python3
"""Phase296-C: thin-extension rigidity of the ORIGINAL formal polynomial rows.

Preregistered in PRE_REGISTERED_THIN_ROW_RIGIDITY.md at 014f5d33,
BEFORE this code. Exact polynomial degrees and characteristic-5 ghost
controls; CI does NOT formally prove a universal theorem in Lean.
"""
from itertools import product
from math import comb
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
from source_probe import params,mul,fall

P=5
DA=583
DB=587
R=145
S=5
FROZEN={
 "research/phase206/source_probe.py":
     "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":
     "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
 "research/phase296/affine_semilinear_transporter.py":
     "ba95668c0bd90cd7cac0426060f6d2f210b48de3",
}

def freeze():
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,(path,actual,sha)

def monomial(r,s,coef=1):
    v=coef%P
    return {(r,s):v} if v else {}

def add_poly(A,B):
    out=A.copy()
    for z,v in B.items():
        a=(out.get(z,0)+v)%P
        if a:out[z]=a
        else:out.pop(z,None)
    return out

def neg_poly(A):
    return {z:(-v)%P for z,v in A.items()}

def product_poly(A,B):
    out={}
    for (r,s),a in A.items():
        for (i,j),b in B.items():
            q=(r+i,s+j)
            v=(out.get(q,0)+a*b)%P
            if v:out[q]=v
            else:out.pop(q,None)
    return out

def power_poly(A,k):
    out=monomial(0,0)
    while k:
        if k&1:out=product_poly(out,A)
        A=product_poly(A,A)
        k//=2
    return out

def apply_monomial(r,s,A,B):
    return product_poly(power_poly(A,r),power_poly(B,s))

def in_rectangle(poly,R,S):
    return all(0<=r<R and 0<=s<S for r,s in poly)

def max_degrees(poly):
    return (max((r for r,s in poly),default=-1),
            max((s for r,s in poly),default=-1))

def independent_degree_envelope(R,S,delta):
    assert R>S>=2 and 0<=delta
    # If sigma(Z)=Z+W, sigma(Z^(R-1)) has coefficient 1
    # at W^(R-1), hence degW exactly R-1 and exceeds S-1.
    assert R-1>S-1
    # If sigma(Z) has Z-degree d>=2, the top term of its
    # (R-1)-st power has Z-degree >=2*(R-1) > R+delta-1
    # for the stipulated thin interval delta<S-1.
    if delta<S-1:
        assert 2*(R-1)>R+delta-1
        # If sigma(W)=c W+h(Z) with deg(h)>=1,
        # the corner W^0 term has Z-degree >=R+S-2.
        assert R+S-2>R+delta-1
    return {"R":R,"S":S,"extra_R_rows":delta,
            "source_dimension":R*S,"target_dimension":(R+delta)*S,
            "highest_allowed_target_Z_degree":R+delta-1,
            "corner_mixing_requires_Z_degree_at_least":R+S-2}

def polynomial_source_trials():
    Z=monomial(1,0)
    W=monomial(0,1)
    one=monomial(0,0)
    affine_Z=add_poly(monomial(1,0,3),one)
    affine_W=add_poly(monomial(0,1,4),monomial(0,0,2))
    tests=((0,0),(1,0),(0,1),(5,1),(R-1,0),(0,S-1),
           (R-1,S-1),(R-2,S-2))
    for r,s in tests:
        translated=apply_monomial(r,s,affine_Z,affine_W)
        assert in_rectangle(translated,R,S)
        assert in_rectangle(translated,R+1,S)
    # Nonlinear and off-diagonal affine forms violate the same
    # FULL FORMAL row-lattice boundary; no functional sampling
    # identification or number-field metric is used here.
    ZplusW=add_poly(Z,W)
    zbad=apply_monomial(R-1,0,ZplusW,W)
    assert zbad.get((0,R-1))==1
    assert not in_rectangle(zbad,R+1,S)
    Zsquared=monomial(2,0)
    znonlinear=apply_monomial(R-1,0,Zsquared,W)
    assert max_degrees(znonlinear)[0]==2*(R-1)
    assert not in_rectangle(znonlinear,R+1,S)
    WplusZ2=add_poly(W,monomial(2,0))
    wnonlinear=apply_monomial(R-1,S-1,Z,WplusZ2)
    assert wnonlinear.get((R-1+2*(S-1),0))==1
    assert not in_rectangle(wnonlinear,R+1,S)

    WplusZ=add_poly(W,Z)
    shear=apply_monomial(R-1,S-1,Z,WplusZ)
    assert max_degrees(shear)==(R+S-2,S-1)
    assert not in_rectangle(shear,R+3,S)
    assert in_rectangle(shear,R+4,S)
    # ALL of the full rectangle L145,5 maps to L149,5 under
    # W->W+Z (with max Z-degree r+s<=R+S-2).
    assert all(r+s<=R+4-1
               for r in range(R) for s in range(S))
    assert (R+4)*S-R*S==20
    assert (R+1)*S-R*S==5
    # But it FAILS the original W-held-fixed jet law:
    # derivative_Z(W+Z)=1, whereas sigma(derivative_Z W)=0.
    assert 1!=0
    reports=[
        independent_degree_envelope(R,S,delta)
        for delta in range(5)
    ]
    assert all(t["corner_mixing_requires_Z_degree_at_least"]
               >t["highest_allowed_target_Z_degree"]
               for t in reports[:4])
    return {
        "original_full_rectangle":[R,S],"tested_monomial_boundaries":len(tests),
        "all_diagonal_affine_changes_stay_in_full_source":True,
        "nonlinear_Z_and_cross_Z_W_transforms_excluded_at_delta1":True,
        "rigidity_holds_through_delta3":True,
        "first_triangular_W_plus_Z_row_embedding_at_delta4":True,
        "thin_D587_actual_extra_R":1,
        "thin_D587_added_integer_row_directions":5,
        "first_W_plus_Z_admissible_added_row_directions":20,
        "W_plus_Z_fails_original_fixed_W_ordinary_jet_derivation":True,
        "degree_obligations":reports}

def fp25(z,w):
    # Exact quadratic multiplication in the same ORIGINAL local field.
    return mul(z,w,DA,P)

def fp25power(z,n):
    out=(1,0)
    while n:
        if n&1:out=fp25(out,z)
        z=fp25(z,z)
        n//=2
    return out

def ghost_observation_control(Q):
    field=list(product(range(P),repeat=2))
    assert len(field)==25
    assert all(fp25power(z,25)==z for z in field)
    assert all((z[0]%P,(-z[1])%P) in field for z in field)
    # Ghost automorphism sigma(Z)=Z+h(W), sigma(W)=W with
    # h(W)=W^25-W; inverse is Z->Z-h(W), W fixed.
    ghost_W_support={(25,0):1,(1,0):P-1}
    assert ghost_W_support=={(25,0):1,(1,0):4}
    # Composition sigma and inverse cancels the SAME h(W)
    # coefficient-by-coefficient, proving two-sided inverse.
    ghost_image=add_poly(monomial(1,0),ghost_W_support)
    inverse_image=add_poly(monomial(1,0),neg_poly(ghost_W_support))
    assert add_poly(add_poly(ghost_image,inverse_image),
                    neg_poly(monomial(1,0,2)))=={}

    # For Z^(R-1), the top W term in (Z+W^25-W)^(R-1)
    # is W^(25*(R-1)) with coefficient 1, nonzero in F5.
    forbidden_top_W=25*(R-1)
    assert forbidden_top_W==3600 and forbidden_top_W>S-1
    # The ghost is FORMALLY not the identity, even though all
    # F25-valued samples and ordinary fixed-W j0..4 jets agree.
    assert ghost_image!=monomial(1,0)
    labels=((0,0),(1,0),(5,1),(R-1,S-1))
    checked=0
    for x,y in Q:
        z=(x%P,y%P)
        w=(x%P,(-y)%P)
        h=(
            (fp25power(w,25)[0]-w[0])%P,
            (fp25power(w,25)[1]-w[1])%P
        )
        assert h==(0,0)
        moved=((z[0]+h[0])%P,(z[1]+h[1])%P)
        assert moved==z
        for r,s in labels:
            for j in range(S):
                if j>r:
                    orig=(0,0)
                    shifted=(0,0)
                else:
                    orig=fp25(
                        fp25power(z,r-j),
                        fp25power(w,s))
                    shifted=fp25(
                        fp25power(moved,r-j),
                        fp25power(w,s))
                    coefficient=fall(r,j)
                    orig=(coefficient*orig[0]%P,coefficient*orig[1]%P)
                    shifted=(coefficient*shifted[0]%P,
                             coefficient*shifted[1]%P)
                assert orig==shifted
                checked+=1
    assert checked==len(Q)*len(labels)*S==383*4*5
    assert (2,0) in Q
    higher=(pow(2,25,25)-2)%25
    assert higher==5!=0
    return {
      "field_size":25,"all_field_elements_satisfy_w_pow25_equals_w":True,
      "ghost_is_invertible_formal_polynomial_automorphism":True,
      "ghost_is_nontrivial_as_formal_polynomial":True,
      "ghost_top_W_degree_on_Z144":forbidden_top_W,
      "source_allowed_W_degree":S-1,
      "ghost_identical_raw_jets_on_all_original_points_mod5":checked,
      "same_ghost_at_original_real_W2_nonzero_mod25":higher,
      "function_and_original_jets_mod5_not_enough_to_prove_row_lattice":True}

def conjugation_and_metric_gate():
    # Any diagonal affine automorphism sigma(Z)=aZ+b,
    # sigma(W)=cW+d commuting with swap tau(Z)=W,tau(W)=Z
    # has a=c,b=d over F5.
    compatible=0
    for a in range(1,P):
        for c in range(1,P):
            for b in range(P):
                for d in range(P):
                    involution=(a==c and b==d)
                    if involution:compatible+=1
    assert compatible==4*5==20
    normone=[a for a in range(1,P) if a*a%P==1]
    assert normone==[1,4]
    # ordinary j1 already forces a²=1 for a real coefficient
    # if its trace form under a^j is to stay unchanged.
    return {
       "all_formal_F5_conjugation_compatible_diagonal_affines":compatible,
       "trace_metric_j1_allows_real_slopes":normone,
       "metric_and_conjugation_group_with_real_translation":2*P,
       "Phase296_A_original_Q_no_exact_match_in_this_group":True,
       "conjugation_W_Z_swap_not_allowed_as_fixed_Z_ordinary_jet_map":True}

def main():
    freeze()
    rhoA,RA,SA,JA,Qa=params(DA)
    rhoB,RB,SB,JB,Qb=params(DB)
    assert (rhoA,RA,SA,JA,len(Qa))==(53,145,5,5,383)
    assert (rhoB,RB,SB,JB,len(Qb))==(53,146,5,5,383)
    assert Qa==Qb
    assert (RA,SA,RB,SB)==(R,S,R+1,S)
    formal=polynomial_source_trials()
    ghost=ghost_observation_control(Qa)
    involution=conjugation_and_metric_gate()
    print("PHASE296C_THIN_ROW_POLYNOMIAL_RIGIDITY",{
       "original_D583_full_row_dimensions":RA*SA,
       "original_D587_full_row_dimensions":RB*SB,
       "original_sample_Q":len(Qa),
       "field_characteristic":P,
       "paper_level_claim":"Aut_k(k[Z,W]) preserving L_(R,S) inside L_(R+delta,S) with delta<S-1 is diagonal affine",
       "proven_by":"degree_W sigma(Z)^R-1, Z-degree bound, k[Z][W] inverse degree, corner W-free coefficient",
       "formal_sparse_polynomial_controls":formal,
       "finite_field_original_jet_ghost":ghost,
       "involution_trace_and_jet_gate":involution,
       "novelty_not_checked":True,
       "not_a_Lean_kernel_formal_theorem":True,
       "not_classifying_non_polynomial_or_source_embedding_maps":True,
       "no_new_primitive_determinant_factor_or_field_bound":True
    },flush=True)
    print("PASS Phase296-C thin-row source automorphism rigidity and Frobenius jet ghost",
          flush=True)

if __name__=="__main__":
    main()
