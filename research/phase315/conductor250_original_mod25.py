#!/usr/bin/env python3
"""Phase315-B/C: exact source-preserving ray125/250 -> ORIGINAL Gram mod25.

D163 h1 original Lean integer source:
  O'=Z[sqrt(-163)], rho21, Q109, R40/S=J1;
  15 integral shears Z^r-Z^(r-24) and EXACT /5 divisions.

Conductor125 unit tags (tame mod5/±, corrected two-digit wild log
L mod25) determine both signed generators modulo125. For nonunits
z=5u, retain u=z/5 mod25 separately (625 possible first lifts).

Conductor250 (2 inert) adds the F4 residue tag; FULL maximal-order
h1 ray class shells convolve BEFORE selecting odd norms with mod2
residue1, adding even norm elements and 5-divisible observations.

All actual original 40x218 primitive source coordinates and all
1600 primitive Gram cells modulo25 are compared against independent
integer-pair Z[sqrt(-163)] evaluator. The old 78 F5 moments are
INSUFFICIENT to distinguish all mod25 Gram contributions.
No extra original determinant valuation inferred.
"""
from collections import Counter,defaultdict
from math import gcd
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase312","phase313","phase314","phase315"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from fermat_lift import mul
from inert_trace_radicals import full_omega_q,rank_f5
from norm_shell_bridge import quadratic_norm,all_ideal_count_at_norm
from ray_to_original_gram import embed_integer_pair_to_omega,ray_count_Gram_D163_native
from conductor2_order_gate import coprime_odd_non5_pairs
from wild_log125 import (
    TOP,M,add,scale,norm,is_unit,signed_ray125_tag,
    signed_ray125_mul,signed_ray125_sign,exhaustive_lift_table
)
import source_probe

D=163
RHO=21
R=40
MOD=25
RAW=125


def pair_original_mul(x,y):
    a,b=x;c,d=y
    return ((a*c-D*b*d)%RAW,(a*d+b*c)%RAW)


def primitive_omega_rows(z):
    """SAME integer polynomial row labels 1,Z,...,Z^39 modulo25.

    The exact Frobenius25 shear requires Z modulo125 BEFORE /5.
    """
    z=(z[0]%RAW,z[1]%RAW)
    powers=[(1,0)]
    for i in range(1,R):
        powers.append(mul(powers[-1],z,D,RAW))
    rows=[]
    for r in range(R):
        if r<25:
            rows.append((powers[r][0]%MOD,powers[r][1]%MOD))
        else:
            diff=((powers[r][0]-powers[r-24][0])%RAW,
                  (powers[r][1]-powers[r-24][1])%RAW)
            assert diff[0]%5==diff[1]%5==0,(
                "invalid exact original Frobenius25 source shear",z,r)
            rows.append((diff[0]//5,diff[1]//5))
    return np.asarray(rows,dtype=np.int64)


def gram_from_omega(E):
    E=np.asarray(E,dtype=np.int64)%MOD
    A,B=E[:,0::2],E[:,1::2]
    return (2*(A@A.T)+(A@B.T)+(B@A.T)
            +((D+1)//2)*(B@B.T))%MOD


def gram_of_observations(zs):
    E=np.zeros((R,2*len(zs)),dtype=np.int64)
    for q,z in enumerate(zs):
        E[:,2*q:2*q+2]=primitive_omega_rows(z)
    return gram_from_omega(E)


def original_integer_source_oracle():
    rho,r,s,j,Q=source_probe.params(D)
    assert (rho,r,s,j)==(21,40,1,1)
    q=tuple(Q)
    assert len(q)==109 and len(set(q))==109
    Eraw=np.zeros((R,2*len(q)),dtype=np.int64)
    for idx,(x,y) in enumerate(q):
        power=(1,0)
        for r in range(R):
            Eraw[r,2*idx:2*idx+2]=power
            power=pair_original_mul(power,(x,y))
    Eint=np.zeros_like(Eraw)
    for r in range(R):
        if r<25:
            Eint[r,:]=Eraw[r,:]%MOD
        else:
            diff=(Eraw[r,:]-Eraw[r-24,:])%RAW
            assert not np.any(diff%5)
            Eint[r,:]=diff//5
    Eint%=MOD
    A,B=Eint[:,0::2],Eint[:,1::2]
    Gint=(2*(A@A.T+D*(B@B.T)))%MOD
    Eomega=np.zeros_like(Eint)
    Eomega[:,0::2]=(A-B)%MOD
    Eomega[:,1::2]=(2*B)%MOD
    Gomega=gram_from_omega(Eomega)
    assert np.array_equal(Gint,Gomega)

    qomega=tuple(embed_integer_pair_to_omega(z) for z in q)
    E2=np.zeros_like(Eomega)
    for idx,z in enumerate(qomega):
        E2[:,2*idx:2*idx+2]=primitive_omega_rows(z)
    assert np.array_equal(E2,Eomega),(
        "unmodified original integer pair source != independent omega evaluation")
    assert np.array_equal(gram_from_omega(E2),Gint)
    old_mod5,_=ray_count_Gram_D163_native(qomega)
    assert np.array_equal(old_mod5,Gint%5)
    assert rank_f5(Gint%5)==23
    return q,qomega,Gint,{
        "unchanged_original_integer_source_Q":len(q),
        "unchanged_original_source_rows":R,
        "original_primitive_source_coordinates_verified":int(Eint.size),
        "original_primitive_Gram_cells_directly_verified":int(Gint.size),
        "source_exact_divided_rows":15,
        "original_primitive_modulus":MOD,
        "original_source_f5_primitive_rank":rank_f5(Gint%5),
        "not_the_maximal_order_source":True,
    }


def unit_and_nonunit_counts(qomega):
    counts=Counter()
    non=Counter()
    seen=set(qomega)
    for z in qomega:
        opposite=(-z[0],-z[1])
        assert opposite in seen
        if is_unit(z,D):
            if z<opposite:
                tag=signed_ray125_tag(z,D)
                assert tag==signed_ray125_tag(opposite,D)
                counts[tag]+=1
        else:
            assert z[0]%5==z[1]%5==0
            u=(z[0]//5%MOD,z[1]//5%MOD)
            non[u]+=1
    assert 2*sum(counts.values())+sum(non.values())==len(qomega)
    return counts,non


def gram_from_unit_rays_and_nonunit_lifts(counts,non,lookup):
    G=np.zeros((R,R),dtype=np.int64)
    for (c,w),n in counts.items():
        z=lookup[(c,w)]
        # Signed generator pair mod125, independent of the choice of
        # representative in the original norm-ball.
        G=(G+n*gram_of_observations((z,signed_ray125_sign(z))))%MOD
    for u,n in non.items():
        z=((5*u[0])%RAW,(5*u[1])%RAW)
        G=(G+n*gram_of_observations((z,)))%MOD
    return G


def first_vs_second_wild_collision():
    z1=(1,0)
    z2=(26,0)
    from tame_wild_ray import ray_tag
    assert ray_tag(z1,D)==ray_tag(z2,D),(
        "frozen formal first-level collision failed")
    t1=signed_ray125_tag(z1,D)
    t2=signed_ray125_tag(z2,D)
    assert t1!=t2 and t1[0]==t2[0]
    A=gram_of_observations((z1,signed_ray125_sign(z1)))
    B=gram_of_observations((z2,signed_ray125_sign(z2)))
    assert np.array_equal(A%5,B%5)
    diff=(B-A)%MOD
    assert np.any(diff),(
        "same 5-ray tag already determined signed source Gram mod25")
    ij=np.argwhere(diff)[0]
    return {
        "formal_unit_residues_mod125":[z1,z2],
        "same_first_level_ray_tag":True,
        "different_second_digit_wild_log":list(t1[1])!=list(t2[1]),
        "same_signed_primitive_Gram_mod5":True,
        "different_signed_primitive_Gram_mod25":True,
        "first_differing_original_Gram_cell":[int(ij[0]),int(ij[1])],
        "first_Gram_difference_mod25":int(diff[ij[0],ij[1]]),
        "NOT_claimed_two_actual_elements_of_original_norm_ball":True,
    }


def full_ray250_ideal_distribution(Qmax):
    bins=defaultdict(Counter)
    all_actual=0
    for z in Qmax:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if gcd(n,10)!=1:
            continue
        tag=((z[0]%2,z[1]%2),signed_ray125_tag(z,D))
        opposite=(-z[0],-z[1])
        assert tag==((opposite[0]%2,opposite[1]%2),
                     signed_ray125_tag(opposite,D))
        bins[n][tag]+=1
        all_actual+=1
    return bins,all_actual


def ray250_mul(a,b):
    return (mul(a[0],b[0],D,2),
            signed_ray125_mul(a[1],b[1],D))


def full_ray250_convolution(a,b):
    ans=Counter()
    for t,n in a.items():
        for s,m in b.items():
            ans[ray250_mul(t,s)]+=n*m
    return +ans


def selected_original_from_global(Qmax,full):
    selected=Counter()
    odd=0
    even=0
    for n,A in full.items():
        assert gcd(n,10)==1
        for (res2,t125),multiplicity in A.items():
            if res2==(1,0):
                selected[t125]+=multiplicity
                odd+=multiplicity
    for z in Qmax:
        if z==(0,0) or z>(-z[0],-z[1]):
            continue
        n=quadratic_norm(z,D)
        if n%2==0 and n%5!=0:
            assert z[1]%2==0 # inert 2 -> already in original order
            selected[signed_ray125_tag(z,D)]+=1
            even+=1
    return selected,odd,even


def full_original_mod25_certificate():
    lookup,local=exhaustive_lift_table(D)
    qint,qomega,Gdirect,source=original_integer_source_oracle()
    unit,non=unit_and_nonunit_counts(qomega)
    assert sum(unit.values())==50
    assert sum(non.values())==9
    Grecovered=gram_from_unit_rays_and_nonunit_lifts(unit,non,lookup)
    assert np.array_equal(Grecovered,Gdirect),(
        "same ORIGINAL integer-order Gram failed conductor125 reconstruction")

    Qmax=tuple(full_omega_q(D,RHO))
    assert len(Qmax)==225
    full,number=full_ray250_ideal_distribution(Qmax)
    eligible=tuple(n for n in range(1,442) if gcd(n,10)==1)
    assert len(eligible)==177
    for n in eligible:
        assert sum(full[n].values())==all_ideal_count_at_norm(D,n)
    pairs=0
    for m,n in coprime_odd_non5_pairs():
        assert full[m*n]==full_ray250_convolution(full[m],full[n]),(
            "full class-one conductor250 norm-shell convolution broken",m,n)
        pairs+=1
    assert pairs==270

    projected,odd,even=selected_original_from_global(Qmax,full)
    assert odd==26 and even==24
    assert projected==unit,(
        "conductor250 global class-one projection differs from original source")
    Gfromglobal=gram_from_unit_rays_and_nonunit_lifts(projected,non,lookup)
    assert np.array_equal(Gfromglobal,Gdirect)
    collision=first_vs_second_wild_collision()
    return {
        "field_D":D,
        "class_number_one_imported_not_proved_by_local_ray":1,
        "original_integer_source":source,
        "full_signed_ray125_unit_classes":local["signed_unit_ray125_count"],
        "full_signed_ray250_unit_class_capacity":3*local["signed_unit_ray125_count"],
        "global_maximal_order_Q":len(Qmax),
        "actual_maximal_order_principal_ray250_ideals":number,
        "all_prime_to10_norm_shell_total_ideal_checks":len(eligible),
        "full_22500_class_conductor250_coprime_products_checked":pairs,
        "original_unit_ray125_principal_ideals":sum(unit.values()),
        "original_nonunit_first_lift_observations":sum(non.values()),
        "original_odd_norm_selected_unit_ideals":odd,
        "original_even_norm_selected_unit_ideals":even,
        "same_ORIGINAL_Gram_mod25_entries_direct_and_local_and_global":int(Gdirect.size),
        "same_ORIGINAL_Gram_mod5_rank":rank_f5(Gdirect%5),
        "strict_collision_first_digit_vs_second_digit":collision,
        "does_NOT_upgrade_exact_v5_77_or_bound_322pow4":True,
    }


def main():
    print("PHASE315_CONDUCTOR250_ORIGINAL_GRAM_MOD25_PASS",
          full_original_mod25_certificate(),flush=True)


if __name__=="__main__":
    main()
