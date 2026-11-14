#!/usr/bin/env python3
"""Phase314-F: HELD-OUT radius60 stress of genuine ray50 ideal convolution.

D43 (h1), D163 (h1), D187 (h>1) all have 2,5 INERT and hence
the SAME ABSTRACT local signed ray unit group C3 × C12 × C5²,
900 conductor50 classes (not identical omega-coordinate charts).
Only in h1 fields does FULL principal-ideal ray convolution hold.

This computes actual maximal-order norm balls rho60 (NOT their native
R,S,J field-theorem sources), exact class tags and independent ideal
norm-shell totals a_K(n). It tests genuine nontrivial coprime products,
not vacuous identity/zero comparisons. Compressed 216 wild-jet spectra
must give the SAME product as full 900-tag convolution.

For D187 nonh1, sqrt(-187)=2omega-1 has norm187=11*17 while
there are NO elements norm11 or17; their ideal classes multiply to1.
The local ray group alone cannot detect this global failure.
"""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase308","phase311","phase312","phase313","phase314"):
    sys.path.insert(0,str(ROOT/"research"/p))
from adaptive_torsion_family import independent_reduced_forms
from fermat_lift import mul
from inert_trace_radicals import full_omega_q
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from tame_wild_ray import ray_tag,tag_mul,norm_mod5,ring_unit_orbits
from truncated_ray_convolution import direct_jet50,moment_product_six


RHO=60
CAP=RHO*RHO
D_H1=(43,163)
D_NONH1=187


def field_inert_controls(D):
    assert D%8==3 # -D fundamental ≡5 mod8 -> 2 inert
    assert (-D)%5 in (2,3) # 5 inert
    assert ((D+1)//4)%2==1
    # Actual residue ring at 2 is F4 and has three units.
    three=((1,0),(0,1),(1,1))
    assert all((z[0]*z[0]+z[0]*z[1]+((D+1)//4)*z[1]*z[1])%2==1
               for z in three)
    assert len({mul(a,b,D,2) for a in three for b in three})==3
    local=ring_unit_orbits(D)
    assert local["sign_quotient_classes"]==300
    assert local["local_unit_group_C12_x_C5_squared"]
    return True


def ray50_tag(D,z):
    if gcd(quadratic_norm(z,D),10)!=1:
        raise ValueError("ray50 needs original 2 and5 units")
    return ((z[0]%2,z[1]%2),ray_tag(z,D))


def ray50_mul(D,a,b):
    return (mul(a[0],b[0],D,2),tag_mul(a[1],b[1],D))


def actual_maximal_ideal_spectra(D):
    Q=tuple(full_omega_q(D,RHO))
    seen=set(Q)
    assert len(Q)==len(seen)
    bins=defaultdict(Counter)
    count=0
    for z in Q:
        if z==(0,0):
            continue
        nz=(-z[0],-z[1])
        assert nz in seen
        if z>nz:
            continue
        n=quadratic_norm(z,D)
        if gcd(n,10)!=1:
            continue
        t=ray50_tag(D,z)
        assert t==ray50_tag(D,nz)
        bins[n][t]+=1
        count+=1
    return Q,bins,count


def convolute_full(D,a,b):
    c=Counter()
    for ta,na in a.items():
        for tb,nb in b.items():
            c[ray50_mul(D,ta,tb)]+=na*nb
    return +c


def multiply_second_jets(D,A,B):
    c=defaultdict(lambda:[0]*6)
    for (r2,ca),ua in A.items():
        for (s2,cb),ub in B.items():
            k=(mul(r2,s2,D,2),tag_mul((ca,(0,0)),(cb,(0,0)),D)[0])
            vals=moment_product_six(ua,ub)
            tgt=c[k]
            for i in range(6):
                tgt[i]=(tgt[i]+vals[i])%5
    return {k:tuple(v) for k,v in c.items() if any(v)}


def h1_heldout(D):
    assert D in D_H1
    assert len(independent_reduced_forms(D))==1
    field_inert_controls(D)
    q,bins,num=actual_maximal_ideal_spectra(D)
    eligible=tuple(n for n in range(1,CAP+1) if gcd(n,10)==1)
    assert len(eligible)==1440
    # Independent Dedekind zeta ideal coefficients, not generated from
    # principal-element counts. This is a FINITE test of known h1.
    shell_checks=0
    for n in eligible:
        assert sum(bins[n].values())==all_ideal_count_at_norm(D,n),(
            "h1 global total-ideal shell discrepancy",D,n)
        shell_checks+=1
    assert shell_checks==len(eligible)
    jets={n:direct_jet50(bins[n]) for n in eligible}
    nontrivial=0
    ray_checks=0
    moment_checks=0
    sample=[]
    support=sorted(n for n in bins if n>1 and bins[n] and gcd(n,10)==1)
    for i,m in enumerate(support):
        for n in support[i:]:
            if m*n>CAP or gcd(m,n)!=1:
                continue
            product=bins[m*n]
            # Full 900-class group, not just 216 quotient.
            assert product==convolute_full(D,bins[m],bins[n]),(
                "heldout h1 exact FULL ray convolution",D,m,n)
            assert jets[m*n]==multiply_second_jets(D,jets[m],jets[n]),(
                "heldout h1 compressed 216-jet convolution",D,m,n)
            nontrivial+=1
            ray_checks+=len(product)
            moment_checks+=6*len(jets[m*n])
            if len(sample)<7:
                sample.append({"m":m,"n":n,"mn":m*n,
                               "principal_ideal_product_classes":len(product)})
    assert nontrivial>4,("heldout not stronger than previous 4 products",D)
    return {
        "D":D,
        "class_number_from_independent_reduced_forms":1,
        "heldout_rho":RHO,
        "native_field_theorem_source_not_substituted":True,
        "actual_maximal_order_Q_points":len(q),
        "actual_prime_to10_principal_ideals":num,
        "all_ideal_total_shell_checks":shell_checks,
        "full_900_ray_class_cap":900,
        "closed_second_jet_cap":216,
        "nontrivial_nonidentity_coprime_ideal_shell_products":nontrivial,
        "full_ray_distribution_nonzero_cells_compared":ray_checks,
        "compressed_second_moment_cells_compared":moment_checks,
        "sample_nontrivial_ideal_products":sample,
        "no_new_field_Gram_or_cutoff_claim":True
    }


def nonh1_counterworld():
    D=D_NONH1
    assert len(independent_reduced_forms(D))>1
    field_inert_controls(D)
    q,bins,num=actual_maximal_ideal_spectra(D)
    omega=(-1,2) # sqrt(-187)=2omega-1
    assert omega in q
    assert quadratic_norm(omega,D)==187==11*17
    assert not bins[11] and not bins[17]
    assert all_ideal_count_at_norm(D,11)==1
    assert all_ideal_count_at_norm(D,17)==1
    assert sum(bins[187].values())>=1
    assert not convolute_full(D,bins[11],bins[17])
    assert bins[187]!=convolute_full(D,bins[11],bins[17])
    return {
        "D":D,
        "class_number_from_independent_reduced_forms":
            len(independent_reduced_forms(D)),
        "same_inert2_and5_local_group_C3_x_C12_x_C5_squared":True,
        "heldout_rho":RHO,
        "maximal_order_Q":len(q),
        "principal_ideals_prime_to10":num,
        "nonprincipal_ramified_ideal_factor_norms":[11,17],
        "both_ideal_total_norm11_and_norm17":1,
        "both_principal_counts_at_norm11_and_norm17":0,
        "principal_count_at_product_norm187":sum(bins[187].values()),
        "principal_only_convolution_fails_despite_same_local_ray_group":True,
        "not_claimed_native_original_Gram":True
    }


def main():
    positive=[h1_heldout(D) for D in D_H1]
    negative=nonh1_counterworld()
    print("PHASE314_HELDOUT_GLOBAL_RAY50_STRESS_PASS",{
        "h1_fields":positive,
        "same_local_ring_nonh1_control":negative,
        "radius60_not_native_field_theorem":True,
        "no_global_valuation_promotion":True
    },flush=True)


if __name__=="__main__":
    main()
