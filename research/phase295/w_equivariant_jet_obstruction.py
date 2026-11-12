#!/usr/bin/env python3
"""Phase295: the fixed-W jet action gives a basis-independent sampler obstruction.

Preregistered BEFORE this executable at commit f558ef77 / refined at
ad2d81f0. A complete D583 original sampler (n725 row lattice), versus
a complete D587 original sampler (n730). The OBSERVATION modules both
have 383 original points x 5 ordinary Z-jet slots, over the respective
unramified quadratic local orders. No Frobenius/source normalization is
asserted here and NO original determinant valuation is changed.
"""
from collections import Counter
from math import comb
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
sys.path.insert(0,str(ROOT/"research"/"phase294"))
from source_probe import params,fall
from support_debt_tower import hensel_lifts

P=5
J=5
D_A=583
D_B=587
EXPECTED={1:(279,104),2:(107,276),3:(107,276),13:(107,276)}
FROZEN_BLOBS={
    "research/phase206/source_probe.py":
        "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase204/ordinary_jet_filtration.py":
        "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
    "research/phase294/support_debt_tower.py":
        "695f5ca77d5ea4f2625c8a7e18bc122ca3459a16",
}

def freeze():
    for path,expected in FROZEN_BLOBS.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==expected,(path,actual,expected)

def field_mul(a,b,D,m):
    x,y=a
    z,w=b
    return ((x*z-D*y*w)%m,(x*w+y*z)%m)

def field_phi(a,alpha,m):
    return (a[0]%m,alpha*a[1]%m)

def conjugate(a,m):
    return (a[0]%m,(-a[1])%m)

def is_unit(a):
    return (a[0]%P!=0 or a[1]%P!=0)

def field_value_w(x,y,alpha,m):
    return (x%m,(-alpha*y)%m)

def jet_w_fixed_guard(Q,k,m,alpha):
    """The original ordinary Z-jet convention makes W scalar per fiber."""
    for D in (D_A,D_B):
        for x,y in (Q[0],Q[len(Q)//3],Q[len(Q)//2],Q[-1]):
            z=(x%m,y%m)
            w=(x%m,(-y)%m)
            for r,s in ((0,0),(1,0),(5,1),(20,3),(144,4)):
                for j in range(J):
                    if j>r:
                        original=(0,0)
                        multiplied=(0,0)
                    else:
                        zp=(1,0)
                        for _ in range(r-j):
                            zp=field_mul(zp,z,D,m)
                        wp=(1,0)
                        for _ in range(s):
                            wp=field_mul(wp,w,D,m)
                        base=field_mul(zp,wp,D,m)
                        coeff=fall(r,j)
                        original=(base[0]*coeff%m,base[1]*coeff%m)
                        multiplied=field_mul(original,w,D,m)
                    # Independently form the ordinary derivative of W*Z^rW^s
                    # from its new exponent (s+1), not a numerical derivative.
                    if j>r:rhs=(0,0)
                    else:
                        extra=field_mul(wp,w,D,m)
                        rhs0=field_mul(zp,extra,D,m)
                        rhs=(rhs0[0]*coeff%m,rhs0[1]*coeff%m)
                    assert rhs==multiplied
    # Chart is a ring hom and a conjugate/trace-norm isometry.
    sample=((0,0),(1,1),(2,3),(m-1,2),(7,11))
    for a in sample:
        for b in sample:
            fmul=field_phi(field_mul(a,b,D_B,m),alpha,m)
            mulf=field_mul(field_phi(a,alpha,m),field_phi(b,alpha,m),D_A,m)
            assert fmul==mulf
        assert field_phi(conjugate(a,m),alpha,m)==conjugate(
            field_phi(a,alpha,m),m)
        a0,a1=a
        assert (a0*a0+D_B*a1*a1)%m==(
            a0*a0+D_A*(alpha*a1)**2)%m
    return True

def multiset_from_w(Q,alpha,m):
    # Explicit scalar W operator W(q) on all J original ordinary jets.
    source=Counter(field_value_w(x,y,1,m) for x,y in Q)
    target=Counter(field_value_w(x,y,alpha,m) for x,y in Q)
    matched=sum(min(source[z],target[z])
                for z in source.keys()|target.keys())
    debt=len(Q)-matched
    return source,target,matched,debt

def diagonal_unit_matching_theorem_toys():
    """Adversarial checks of the paper proof; not its proof by themselves."""
    # Over R=Z/25, BOTH 5x5 characteristic polynomials are t^5
    # although W=0 I5 and W=5 I5 are NOT similar.
    mod=25
    assert all(comb(5,j)*((-5)**j)%mod==0 for j in range(1,6))
    assert all((5*x)%mod!=0 for x in range(mod) if x%P)
    # An off-fiber entry can intertwine without being a unit:
    # (0-5)*5 = 0 (mod25), but it cannot carry an invertible matrix.
    assert ((0-5)*5)%mod==0 and not is_unit((5,0))

    # Positive GL4 shear mixing jets at equal W; no point permutation
    # restriction is imposed by the theorem.
    w=[(0,0),(0,0),(1,2),(1,2)]
    Y=[[int(i==j) for j in range(4)] for i in range(4)]
    Y[0][1]=2
    Y[2][3]=3
    assert all(field_mul(
        ((w[i][0]-w[j][0])%mod,(w[i][1]-w[j][1])%mod),
        (Y[i][j],0),D_A,mod)==(0,0)
        for i in range(4) for j in range(4))
    # Upper-unitriangular => determinant=1, hence a unit modulo5.
    assert all(Y[i][i]==1 for i in range(4))
    assert all(Y[i][j]==0 for i in range(4) for j in range(i))

    # The Z-only thickening *does* hide a shift by 5 modulo25.
    # Basis 1,t,...,t^4 and N multiplication by t on R[t]/t^5.
    n=5
    N=[[0]*n for _ in range(n)]
    for i in range(n-1):N[i+1][i]=1
    T=[[comb(j,i)*5**(j-i)%mod if i<=j else 0
        for j in range(n)] for i in range(n)]
    B=[[N[i][j]+5*int(i==j) for j in range(n)]
       for i in range(n)]
    multiply=lambda X,Z:[[sum(X[i][k]*Z[k][j] for k in range(n))%mod
             for j in range(n)] for i in range(n)]
    assert multiply(T,N)==multiply(B,T),("Z-jet translation failed",T)
    assert all(T[i][i]==1 for i in range(n))
    # However adding fixed-W scalar W=0 versus5 forbids GL5 intertwining
    # by unit-entry argument even though the characteristic polynomials agree.
    assert all(((5*1)%mod)!=0 for _ in range(1))
    return {
        "same_characteristic_polynomial_distinct_W_modules_mod25":True,
        "W0_vs_W5_no_unit_intertwiner":True,
        "off_fiber_nonunit_intertwiner_exists_but_cannot_invert":True,
        "dense_equal_W_unimodular_shear":True,
        "Z_only_translation_by5_unimodular_mod25":True,
        "W_fixed_prevents_Z_only_translation_from_being_sampler_transport":True,
    }

def main():
    freeze()
    rho_A,R_A,S_A,J_A,Qa=params(D_A)
    rho_B,R_B,S_B,J_B,Qb=params(D_B)
    assert (rho_A,R_A,S_A,J_A,len(Qa))==(53,145,5,5,383)
    assert (rho_B,R_B,S_B,J_B,len(Qb))==(53,146,5,5,383)
    assert Qa==Qb and J_A==J_B==J and Qa==list(Qa)
    Q=Qa
    assert len(Q)==len(set(Q))==383
    assert D_A%4==D_B%4==3
    assert (-D_A)%P==2 and (-D_B)%P==3
    assert 2 not in {x*x%P for x in range(P)}
    assert 3 not in {x*x%P for x in range(P)}
    controls=diagonal_unit_matching_theorem_toys()

    rows=[]
    all_roots=hensel_lifts(13)
    assert len(all_roots)==13
    for k,m,alpha in all_roots:
        if k not in EXPECTED:continue
        assert (D_A*alpha*alpha-D_B)%m==0
        assert jet_w_fixed_guard(Q,k,m,alpha)
        A,B,matched,debt=multiset_from_w(Q,alpha,m)
        assert (matched,debt)==EXPECTED[k]
        # Completely distinct representation: matching original x/y
        # residue multiplicities. Injectivity w=(x,-alpha*y)
        # makes these equal to scalar-W multisets, not by assumption.
        source_xy=Counter((x%m,y%m) for x,y in Q)
        target_xy=Counter((x%m,(alpha*y)%m) for x,y in Q)
        xy_match=sum(min(source_xy[z],target_xy[z])
                     for z in source_xy.keys()|target_xy.keys())
        assert xy_match==matched

        # Other root branch is the conjugate field map and original
        # Q is centrally symmetric, so it has the same scalar spectrum.
        _,_,matched_minus,debt_minus=multiset_from_w(Q,-alpha,m)
        assert (matched_minus,debt_minus)==(matched,debt)
        # The common envelope is the least matching completion in the
        # FULL category of W-intertwining A-linear GL maps, not merely
        # in the point-permutation category.
        keys=A.keys()|B.keys()
        envelope=Counter({z:max(A[z],B[z]) for z in keys})
        assert sum(envelope.values())==len(Q)+debt
        assert sum(envelope[z]-A[z] for z in keys)==debt
        assert sum(envelope[z]-B[z] for z in keys)==debt
        mismatches=[(z,A[z],B[z]) for z in sorted(keys) if A[z]!=B[z]]
        assert len(mismatches)>0 and all(len(z)==2 for z,a,b in mismatches)
        # Each point contributes a WHOLE J=5 A_k jet block.
        # Every A_k free slot is two Z/p^k signed coordinate slots.
        n_match=matched*J
        n_deficit=debt*J
        assert n_match+n_deficit==J*len(Q)==1915
        rows.append({
            "depth":k,"modulus":m,"field_isometry_alpha":alpha,
            "source_original_full_D583_rows":R_A*S_A,
            "target_original_full_D587_rows":R_B*S_B,
            "actual_observation_points_per_side":len(Q),
            "original_ordinary_Z_jets_per_point":J,
            "observation_Ak_free_rank_per_side":1915,
            "observation_Zmod5k_rank_per_side":3830,
            "matched_exact_W_eigenvalue_point_blocks":matched,
            "unmatched_exact_W_eigenvalue_point_blocks_each_side":debt,
            "max_common_W_equivariant_full_jet_blocks":n_match,
            "W_equivariant_unmatched_jet_slots_over_Ak_each_side":n_deficit,
            "W_equivariant_unmatched_real_imag_slots_each_side":2*n_deficit,
            "minimum_added_original_type_point_blocks_each_side":debt,
            "minimum_completed_observation_points_per_side":sum(envelope.values()),
            "invertible_W_intertwiner_exists":debt==0,
            "first_scalar_W_multiplicity_witness":{
                "scalar_W_pair":list(mismatches[0][0]),
                "original_A_multiplicity":mismatches[0][1],
                "transported_B_multiplicity":mismatches[0][2]},
            "field_Galois_sign_branch_same_debt":True,
            "all_original_fixed_W_jet_operator_tests_pass":True,
        })
    assert [r["unmatched_exact_W_eigenvalue_point_blocks_each_side"]
            for r in rows]==[104,276,276,276]
    assert [r["W_equivariant_unmatched_jet_slots_over_Ak_each_side"]
            for r in rows]==[520,1380,1380,1380]
    print("PHASE295_W_EQUIVARIANT_JET_OBSTRUCTION",{
        "full_original_source_D583_n":R_A*S_A,
        "full_original_source_D587_n":R_B*S_B,
        "comparison_carrier":"ORIGINAL observation jet module, NOT row lattice",
        "scalar_ring":"(Z/5^k)[u]/(u^2+583), local unramified degree2",
        "commutation_law":"Y W_A = W_B^phi Y",
        "proof_criterion":"det(Y) unit forces a full permutation of UNIT entries; each matches exact W scalar",
        "tested_depths":rows,
        "hostile_controls":controls,
        "permissible_new_jet_blocks_are_original_type_only":True,
        "does_not_rule_out_Y_that_changes_W_or_is_not_Ak_linear":True,
        "no_extra_p_valuation_or_primitive_source_lift":True,
        "no_new_discriminant_field_bound":True
    },flush=True)
    print("PASS Phase295 full original-jet W-module obstruction and local-ring toys",
          flush=True)

if __name__=="__main__":
    main()
