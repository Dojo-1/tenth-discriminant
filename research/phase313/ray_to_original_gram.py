#!/usr/bin/env python3
"""Phase313-D: EXACT global-principal-ray-spectrum to SAME primitive Gram.

The global object is the radius-bounded distribution of PRINCIPAL ideals
in the 300 signed conductor25 tame/wild classes. This does NOT by itself
classify all ideals when h>1, and it is not defined on 5-divisible ideals.

The finite source map requires an explicit disjoint valuation stratum:
for z=5u, epsilon(z)=-conjugate(u) mod5. With that stratum, the global
principal-ray count vector and ORIGINAL source row/jet coefficient maps
reconstruct the primitive Gram mod5:
  (D203, maximal-order original, R50/S=J2/rho24/Q263);
  (D163, h1, EXACT Lean integer-order original Z[sqrt(-163)]
         R40/S=J1/rho21/Q109 and 15 exact /5 source divisions).
No global v5 beyond the existing local calculations is inferred.
"""
from collections import Counter
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase304","phase307","phase311","phase312","phase313"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from tame_wild_ray import ray_tag,norm_mod5
from fermat_lift import epsilon,conjugate,add,mul,scale,power
from inert_trace_radicals import trace_gram_from_original,rank_f5
from primitive_moments import residue_jet_coefficients,field_dot
from source_saturation import original_fifty_row_saturation
from kernel_vs_weight import original_integer_ring_mul
import highjet_d203_original as pilot
import source_probe

P=5


def ray_and_nonunit_strata(q,D):
    """Disjoint, exhaustive actual-observation coverage: ± units / 5u."""
    Q=tuple(q)
    assert len(Q)==len(set(Q))
    seen=set(Q)
    counts=Counter()
    nonunits=Counter()
    for z in Q:
        minus=(-z[0],-z[1])
        assert minus in seen
        if norm_mod5(z,D):
            if z<minus:
                tag=ray_tag(z,D)
                assert tag==ray_tag(minus,D)
                counts[tag]+=1
        else:
            assert z[0]%5==0 and z[1]%5==0
            u=(z[0]//5%5,z[1]//5%5)
            nonunits[u]+=1
            # For ANY z divisible5, (z^5-conj(z))/5 = -conj(z/5)
            assert epsilon(z,D)==scale(-1,conjugate(u,5),5)
    assert 2*sum(counts.values())+sum(nonunits.values())==len(Q)
    return counts,nonunits


def wild_unit_features(residue,delta,D):
    """Actual epsilon=conjugate(residue)*delta; no arbitrary lift."""
    ep=mul(conjugate(residue,5),delta,D,5)
    return ((1,0),ep,conjugate(ep,5))


def nonunit_features(u,D):
    ep=scale(-1,conjugate(u,5),5)
    return ((1,0),ep,conjugate(ep,5))


def generated_D203_E(residues,features):
    """ORIGINAL Phase307 primitive row/ordinary-jet semantics, mod5."""
    n=len(residues)
    E=np.zeros((100,2*2*n),dtype=np.int64)
    for qidx,(z,u) in enumerate(zip(residues,features)):
        C=residue_jet_coefficients(z)
        for j in range(2):
            for i in range(100):
                e=field_dot(C[j,i],u)
                col=2*(j*n+qidx)
                E[i,col:col+2]=e
    return E


def ray_count_Gram_D203(q):
    """Linear count-transport F5^(300+25)->Sym_100(F5)."""
    tag_counts,nonunits=ray_and_nonunit_strata(q,203)
    G=np.zeros((100,100),dtype=np.int64)
    damaged_zero_wild=np.zeros_like(G)
    even=[i for i in range(100) if (i//2+i%2)%2==0]
    odd=[i for i in range(100) if (i//2+i%2)%2==1]
    parity_checks=0
    for (c,w),count in tag_counts.items():
        minus=((-c[0])%5,(-c[1])%5)
        residues=[c,minus]
        features=[wild_unit_features(c,w,203),
                  wild_unit_features(minus,w,203)]
        E=generated_D203_E(residues,features)
        # Actual sign-parity identity, including ordinary held-W jet.
        for i in range(100):
            r,s=divmod(i,2)
            for j in range(2):
                ca=E[i,2*(j*2+0):2*(j*2+0)+2]
                cb=E[i,2*(j*2+1):2*(j*2+1)+2]
                sign=1 if (r+s-j)%2==0 else -1
                assert np.array_equal(cb,(sign*ca)%5),(
                    "signed ray class orientation altered source parity",i,j)
                parity_checks+=2
        gram=trace_gram_from_original(E,203)
        assert not np.any(gram[np.ix_(even,odd)])
        G=(G+count*gram)%5
        # Deliberately discard the wild coordinate but RETAIN tame counts.
        e0=generated_D203_E(residues,[
            wild_unit_features(c,(0,0),203),
            wild_unit_features(minus,(0,0),203)])
        damaged_zero_wild=(damaged_zero_wild
                            +count*trace_gram_from_original(e0,203))%5
    unit_only=G.copy()
    for u,count in nonunits.items():
        e=generated_D203_E([(0,0)],[nonunit_features(u,203)])
        gram=trace_gram_from_original(e,203)
        G=(G+count*gram)%5
        damaged_zero_wild=(damaged_zero_wild+count*gram)%5

    assert 2*sum(tag_counts.values())+sum(nonunits.values())==len(q)
    return G,{
        "original_Q":len(q),
        "principal_ideal_count_prime_to5":sum(tag_counts.values()),
        "distinct_signed_tame_wild_ray_bins":len(tag_counts),
        "nonunit_observations":sum(nonunits.values()),
        "distinct_nonunit_first_lift_bins":len(nonunits),
        "signed_primitive_ordinary_jet_coordinates_parity_checked":parity_checks,
        "dropping_wild_changes_primitive_Gram":
            not np.array_equal(G,damaged_zero_wild),
        "dropping_nonunit_lifts_changes_primitive_Gram":
            not np.array_equal(G,unit_only),
        "source_map_count_linear_mod5":True,
        "all_300_ray_components_only_principal_ideals_when_nonh1":True,
    }


def complete_D203_source_certificate():
    pilot.guard()
    rho,R,S,J,_=pilot.params(203)
    assert (rho,R,S,J)==(24,50,2,2)
    q=tuple(pilot.qmax(rho))
    assert len(q)==263
    G,meta=ray_count_Gram_D203(q)
    original=pilot.evaluate_original_jets(q,R,S,J,25)
    _,primitive,selected=original_fifty_row_saturation(original)
    assert len(selected)==50
    direct=pilot.original_trace_gram(
        np.asarray(primitive,dtype=np.int64)%5,len(q),J,5)
    assert np.array_equal(G,direct),(
        "global ray-unit strata did NOT reconstruct SAME D203 primitive Gram")
    assert rank_f5(G)==63
    assert meta["nonunit_observations"]==9
    assert meta["principal_ideal_count_prime_to5"]==127
    return {
        "D":203,
        "source":"unchanged maximal-order original Q263 R50/S=J2",
        "same_original_primitive_Gram_cells_verified":G.size,
        "Gram_rank_F5":rank_f5(G),
        "source_5_divisions":len(selected),
        "ray_and_nonunit_sufficient_statistics":meta,
        "does_not_certify_full_higher_5adic_Smith":True,
        "no_class_one_global_bound_inferred":True
    }


def embed_integer_pair_to_omega(z):
    """x+y sqrt(-163) = (x-y)+2y omega, EXACT integral inclusion."""
    x,y=z
    return (x-y,2*y)


def native_integer_original_primitive(Q,mod=25):
    """Original Lean Z[sqrt(-163)] source and EXACT 15 /5 divisions."""
    n=len(Q)
    E=np.zeros((40,2*n),dtype=np.int64)
    for qi,z in enumerate(Q):
        val=(1,0)
        for r in range(40):
            E[r,2*qi:2*qi+2]=val
            val=original_integer_ring_mul(val,z,163,mod)
    prim=E.copy()
    for r in range(25,40):
        diff=(E[r,:]-E[r-24,:])%mod
        assert not np.any(diff%5)
        prim[r,:]=diff//5
    prim%=5
    return prim


def generated_D163_native_E(residues,features):
    """Original integer polynomial Z^r after Frobenius25 /5, in omega."""
    n=len(residues)
    E=np.zeros((40,2*n),dtype=np.int64)
    for qi,(z,u) in enumerate(zip(residues,features)):
        etaconj=u[2] # conjugate(epsilon)=(z^25-z)/5 mod5
        for r in range(40):
            if r<25:
                out=power(z,r,163,5)
            else:
                out=mul(power(z,r-25,163,5),etaconj,163,5)
            E[r,2*qi:2*qi+2]=out
    return E


def ray_count_Gram_D163_native(qomega):
    counts,nonunits=ray_and_nonunit_strata(qomega,163)
    G=np.zeros((40,40),dtype=np.int64)
    for (c,w),count in counts.items():
        minus=((-c[0])%5,(-c[1])%5)
        e=generated_D163_native_E(
            [c,minus],[wild_unit_features(c,w,163),
                       wild_unit_features(minus,w,163)])
        G=(G+count*trace_gram_from_original(e,163))%5
    for u,count in nonunits.items():
        e=generated_D163_native_E(
            [(0,0)],[nonunit_features(u,163)])
        G=(G+count*trace_gram_from_original(e,163))%5
    assert 2*sum(counts.values())+sum(nonunits.values())==len(qomega)
    return G,{
        "original_integer_observations":len(qomega),
        "principal_ideals_coprime_to5":sum(counts.values()),
        "distinct_signed_tame_wild_ray_bins":len(counts),
        "nonunit_observations":sum(nonunits.values()),
        "distinct_nonunit_lift_bins":len(nonunits),
    }


def complete_D163_original_integer_source_certificate():
    rho,R,S,J,Q=source_probe.params(163)
    assert (rho,R,S,J)==(21,40,1,1)
    Q=tuple(Q)
    assert len(Q)==109
    qomega=tuple(embed_integer_pair_to_omega(z) for z in Q)
    assert len(qomega)==len(set(qomega))

    prim_int=native_integer_original_primitive(Q,25)
    prim_omega=np.zeros_like(prim_int)
    prim_omega[:,0::2]=(prim_int[:,0::2]-prim_int[:,1::2])%5
    prim_omega[:,1::2]=(2*prim_int[:,1::2])%5
    # Verify 40*109 original field evaluation coordinates through a
    # SEPARATE epsilon-based single-point reconstruction, not just Gram.
    field_checked=0
    for qi,z in enumerate(qomega):
        r=z[0]%5,z[1]%5
        eps=epsilon(z,163)
        u=((1,0),eps,conjugate(eps,5))
        p=generated_D163_native_E([r],[u])
        assert np.array_equal(
            p[:,0:2],prim_omega[:,2*qi:2*qi+2]),(
                "actual Lean-original integer primitive lift mismatch",qi,z)
        field_checked+=80

    G_ray,census=ray_count_Gram_D163_native(qomega)
    G_omega=trace_gram_from_original(prim_omega,163)
    A,B=prim_int[:,0::2],prim_int[:,1::2]
    G_integer=(2*(A@A.T+163*(B@B.T)))%5
    assert np.array_equal(G_integer,G_omega),(
        "omega transfer must preserve original integer Hermitian trace")
    assert np.array_equal(G_ray,G_integer),(
        "GLOBAL principal ray strata fail SAME original integer-order Gram")
    assert census["nonunit_observations"]==9
    assert census["principal_ideals_coprime_to5"]==50
    return {
        "D":163,
        "class_number":1,
        "source":"EXACT original Lean Z[sqrt(-163)] integer pair Q109 rho21 R40 S=J1",
        "original_primitive_source_shape":[40,218],
        "original_integer_source_F25_coordinates_checked":field_checked,
        "original_integer_trace_to_omega_Gram_cells_checked":G_integer.size,
        "global_ray_to_same_original_primitive_Gram_cells_checked":G_ray.size,
        "native_source_exact_p_divided_rows":15,
        "Gram_rank_F5":rank_f5(G_ray),
        "ray_and_nonunit_sufficient_statistics":census,
        "class_one_norm_shell_convolution_now_has_TYPED_Gram_forward_map":True,
        "no_uniform_extra_valuation_asserted":True
    }


def main():
    a=complete_D203_source_certificate()
    b=complete_D163_original_integer_source_certificate()
    print("PHASE313_GLOBAL_RAY_TO_ORIGINAL_GRAM_PASS",{
        "D203_native_maximal_order":a,
        "D163_h1_native_integer_order":b,
        "same_original_Gram_semantic_transport_preserved":True,
        "wild_convolution_does_not_FORCE_rank_defect":True,
        "no_322_power4_cutoff_change":True,
    },flush=True)


if __name__=="__main__":
    main()
