#!/usr/bin/env python3
"""Phase318-C: exact one-dimensional first-radical-lift resonance pencil.

AFTER first Phase318 A/B data (not retroactively preregistered):
  50 local norm125 site shifts -> F5 image dimension 1 on 17d radical;
  16 active principal split-prime characters;
  p53,p227 synthetic first Smith e1 changes from7 to3.
Now pre-registered holdout tests of the FULL normal pencil
B_lambda=B_original+lambda*N, for lambda in F5, a specific
nonzero 7x7 determinant minor of degree<=rank(N), and FULL
native/heldout conductor250 ray convolution for all active split
prime characters (p53,p227 at rho60).

This is bounded exact linear algebra on SAME D163 original
integer-order Gram. Synthetic characters do not describe alternative
number fields. No new discriminant bound.
"""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase308","phase311","phase312","phase313",
               "phase314","phase315","phase316","phase317","phase318"):
    sys.path.insert(0,str(ROOT/"research"/folder))

from inert_trace_radicals import rank_f5,full_omega_q
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from local_wild_normal import signed_unit_sites,site_differentials
from split_prime_normal import (
    split_principal_prime_generators,one_prime_original_gram,
    global_ray_replay_one_prime,verify_exact_ideal_valuation_character,
    signed_wild_character_tag
)
from wild_log125 import exhaustive_lift_table
from conductor250_original_mod25 import (
    original_integer_source_oracle,full_ray250_convolution
)
from radical_tangent import (
    kernel_basis_mod5,first_radical_form,inverse_matrix_f5
)
from heldout_global_ray import nonh1_counterworld

D=163
P=5


def determinant_mod5(a):
    b=np.asarray(a,dtype=np.int64).copy()%P
    n,m=b.shape
    if n!=m:
        raise ValueError("square matrix required")
    sign=1
    det=1
    for j in range(n):
        pivot=next((i for i in range(j,n) if b[i,j]%P),None)
        if pivot is None:
            return 0
        if pivot!=j:
            b[[pivot,j]]=b[[j,pivot]]
            sign=-sign
        x=int(b[j,j])
        det=det*x%P
        inv=pow(x,-1,P)
        for i in range(j+1,n):
            if b[i,j]:
                factor=int(b[i,j])*inv%P
                b[i,j:]=(b[i,j:]-factor*b[j,j:])%P
    return (sign*det)%P


def choose_independent_minor(a):
    """Deterministic full-rank 7x7 minor, independent of determinant."""
    a=np.asarray(a,dtype=np.int64)%P
    q=a.shape[0]
    _,cols,_=kernel_basis_mod5(a)
    n=len(cols)
    assert n==rank_f5(a)
    rows=[]
    for i in range(q):
        test=rows+[i]
        if rank_f5(a[np.ix_(test,cols)])==len(test):
            rows.append(i)
            if len(rows)==n:
                break
    assert len(rows)==n
    d=determinant_mod5(a[np.ix_(rows,cols)])
    assert d!=0
    return tuple(rows),tuple(cols),d


def scale_of_one_dimensional_normal(n,base):
    n=np.asarray(n,dtype=np.int64)%P
    base=np.asarray(base,dtype=np.int64)%P
    assert n.shape==base.shape
    ij=np.argwhere(base)
    assert len(ij)>0
    i,j=ij[0]
    coefficient=int(n[i,j])*pow(int(base[i,j]),-1,P)%P
    assert np.array_equal(n,(coefficient*base)%P),(
        "normal image is NOT a one-dimensional pencil",i,j,coefficient)
    return coefficient


def global_ray_replay_radius60(pi):
    Q=tuple(full_omega_q(D,60))
    assert len(Q)==1785
    bins=defaultdict(Counter)
    for z in Q:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if gcd(n,10)!=1:
            continue
        tag=((z[0]%2,z[1]%2),signed_wild_character_tag(z,pi))
        assert tag==(((-z[0])%2,(-z[1])%2),
                     signed_wild_character_tag((-z[0],-z[1]),pi))
        bins[n][tag]+=1
    eligible=[n for n in range(1,3601) if gcd(n,10)==1]
    assert len(eligible)==1440
    for n in eligible:
        assert sum(bins[n].values())==all_ideal_count_at_norm(D,n),(
            "heldout original ideal mass failed",pi,n)
    support=sorted(n for n in bins if n>1 and bins[n])
    nontrivial=0
    for i,m in enumerate(support):
        for n in support[i:]:
            if m*n>3600 or gcd(m,n)!=1:
                continue
            assert bins[m*n]==full_ray250_convolution(
                bins[m],bins[n]),(
                    "heldout full ray250 coprime product failed",pi,m,n)
            nontrivial+=1
    assert nontrivial==59
    exact_products=verify_exact_ideal_valuation_character(pi,Q)
    return {
        "prime":quadratic_norm(pi,D),
        "heldout_radius":60,
        "heldout_maximal_order_Q":len(Q),
        "all_independent_prime_to10_ideal_shells":len(eligible),
        "genuine_nonidentity_coprime_full_ray250_products":nontrivial,
        "exact_ideal_character_multiplication_checks":exact_products,
        "original_integer_order_Q109_NOT_replaced":True,
    }


def normal_pencil_certificate():
    qint,qomega,G,_=original_integer_source_oracle()
    sites,non=signed_unit_sites(qomega)
    assert len(sites)==50 and len(non)==9
    bases,mats=site_differentials(sites)
    K,_,_=kernel_basis_mod5(G%P)
    assert K.shape==(40,17)
    B0=first_radical_form(G,K)
    assert rank_f5(B0)==7

    site_normals=tuple((K.T@H@K)%P for H in mats)
    nonzero_sites=[i for i,x in enumerate(site_normals) if np.any(x)]
    assert len(nonzero_sites)==8
    first=nonzero_sites[0]
    N=site_normals[first]
    n_rank=rank_f5(N)
    site_scales=[scale_of_one_dimensional_normal(x,N)
                 for x in site_normals]
    assert len(site_scales)==50
    assert sum(x!=0 for x in site_scales)==len(nonzero_sites)

    ranks={}
    for t in range(5):
        Bt=(B0+t*N)%P
        ranks[t]=rank_f5(Bt)
    assert ranks[0]==7
    assert max(ranks.values())<=17
    resonance=[t for t in range(5) if ranks[t]<ranks[0]]
    assert resonance,("post-A/B observed e1=3 but no normal pencil resonance")

    rows,cols,base_minor=choose_independent_minor(B0)
    determinant_values=[
        determinant_mod5(((B0+t*N)%P)[np.ix_(rows,cols)])
        for t in range(P)
    ]
    vandermonde=np.asarray([[pow(t,j,P) for j in range(P)]
                            for t in range(P)],dtype=np.int64)
    coef=(inverse_matrix_f5(vandermonde)@
          np.asarray(determinant_values,dtype=np.int64))%P
    assert all(sum(int(coef[k])*pow(t,k,P) for k in range(P))%P
               ==determinant_values[t] for t in range(P))
    assert all(int(coef[j])==0 for j in range(n_rank+1,P)),(
        "computed minor polynomial exceeds perturbation rank bound")
    assert determinant_values[0]==base_minor

    Q,primes,ramified=split_principal_prime_generators()
    assert len(Q)==225
    lookup,_=exhaustive_lift_table(D)
    active=[]
    char_results=[]
    e1_changed=[]
    for p,pi in sorted(primes.items()):
        a,normal=one_prime_original_gram(
            pi,sites,non,K,bases,mats,lookup,G)
        if not a["changed_signed_original_sites"]:
            assert not np.any(normal)
            continue
        lam=scale_of_one_dimensional_normal(normal,N)
        assert a["first_radical_lift_rank"]==ranks[lam],(
            "pencil rank disagrees with actual native synthetic Smith",p)
        assert a["original_first_two_smith_layers"][1]==ranks[lam]
        active.append(p)
        char_results.append({
            "prime":p,
            "normal_pencil_scalar_mod5":lam,
            "normal_restriction_rank":a["normal_restriction_rank"],
            "original_synthetic_first_two_smith":a[
                "original_first_two_smith_layers"],
            "normal_pencil_predicts_smith_e1":True,
        })
        if ranks[lam]!=ranks[0]:
            e1_changed.append(p)
    assert len(active)==16
    assert 41 in active and 53 in active and 227 in active
    assert 53 in e1_changed and 227 in e1_changed

    native_replays=[
        global_ray_replay_one_prime(primes[p],Q)
        for p in active
    ]
    assert len(native_replays)==16
    assert all(x["all_independent_h1_ideal_norm_shells"]==177
               and x["full_22500_conductor250_coprime_products"]==270
               for x in native_replays)
    heldout=[global_ray_replay_radius60(primes[p]) for p in (53,227)]
    negative=nonh1_counterworld()
    assert negative["D"]==187
    assert negative["principal_only_convolution_fails_despite_same_local_ray_group"]

    return {
        "D":D,
        "original_native_integer_order_Q":len(qomega),
        "original_mod5_Gram_radical_dim":K.shape[1],
        "original_first_lift_rank":rank_f5(B0),
        "complete_local_sites":len(site_normals),
        "nonzero_local_site_normals":len(nonzero_sites),
        "normal_image_dim":1,
        "first_nonzero_site":sites[first],
        "first_nonzero_normal_matrix_rank":n_rank,
        "all_50_local_normal_coefficients_mod5":site_scales,
        "exact_F5_normal_pencil_lambda_to_rank":ranks,
        "pencil_rank_drop_resonance_scalars":[int(x) for x in resonance],
        "specific_nonzero_original_7x7_minor_rows":rows,
        "specific_nonzero_original_7x7_minor_cols":cols,
        "minor_determinants_at_lambda_0_1_2_3_4":determinant_values,
        "degree_at_most_rankN_minor_polynomial_coefficients_mod5":
            [int(x) for x in coef],
        "minor_zero_scalars_not_automatically_full_rank_drop":
            [t for t in range(5) if determinant_values[t]==0],
        "active_global_split_prime_characters":len(active),
        "per_character_normal_pencil_scales_and_smith":char_results,
        "globally_multiplicative_synthetic_characters_changing_e1":e1_changed,
        "complete_16_character_native_conductor250_replay":native_replays,
        "heldout_radius60_p53_p227_full_ray250_convolutions":heldout,
        "nonh1_D187_principal_ray_failure_control":True,
        "no_new_field_or_discriminant_cutoff_improvement":True
    }


def main():
    print("PHASE318_NORMAL_PENCIL_GLOBAL_H1_HOLDOUT_PASS",
          normal_pencil_certificate(),flush=True)


if __name__=="__main__":
    main()
