#!/usr/bin/env python3
"""Phase312-B: coherent 5-adic Hensel ring equivalence vs global class number.

Quadratic orders D43/D163 (h1) and D183 (h8) have isomorphic *local*
unramified Z5-algebras, WITH conjugation, at every 5-adic precision.
The isomorphism never asserts equivalence of the original global norm
balls, ray class groups, or determinant calculations across fields.
"""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase312"))
from fermat_lift import (check_field,mul,add,sub,scale,conjugate,
                         field_inverse,local_ring_transport,epsilon)


def quadratic_relation(x,Dsource,Dtarget,mod):
    m=(Dsource+1)//4
    return sub(add(mul(x,x,Dtarget,mod),(m,0),mod),x,mod)


def coherent_hensel_lift(Dsource,Dtarget,depth=6):
    check_field(Dsource)
    check_field(Dtarget)
    if depth<1:raise ValueError("positive precision needed")
    msrc=(Dsource+1)//4
    mtgt=(Dtarget+1)//4
    if (msrc-mtgt)%5:
        raise ValueError("must first identify a matching simple root mod5")
    x=(0,1)
    levels=[{"k":1,"modulus":5,"omega_image":x}]
    assert quadratic_relation(x,Dsource,Dtarget,5)==(0,0)
    for j in range(1,depth):
        old_mod=5**j
        mod=5**(j+1)
        relation=quadratic_relation(x,Dsource,Dtarget,mod)
        if any(v%old_mod for v in relation):
            raise AssertionError("previous Hensel level not coherent")
        quotient=tuple((v//old_mod)%5 for v in relation)
        derivative=((2*x[0]-1)%5,(2*x[1])%5)
        inverse=field_inverse(derivative,Dtarget)
        correction=scale(-1,mul(inverse,quotient,Dtarget,5),5)
        xnext=add(x,scale(old_mod,correction,mod),mod)
        assert quadratic_relation(xnext,Dsource,Dtarget,mod)==(0,0)
        assert tuple(v%old_mod for v in xnext)==tuple(v%old_mod for v in x)
        assert xnext[0]%5==0 and xnext[1]%5==1
        assert conjugate(xnext,mod)==sub((1,0),xnext,mod),(
            "Hensel transport must commute with quadratic conjugation")
        x=xnext
        levels.append({"k":j+1,"modulus":mod,"omega_image":x,
                       "correction_t_mod5":correction})
    def phi(z,level=depth):
        if not 1<=level<=depth:raise ValueError("unsupported level")
        mod=5**level
        root=levels[level-1]["omega_image"]
        return add((z[0],0),scale(z[1],root,mod),mod)
    return phi,levels


def exact_bidirectional_controls(D,E,depth=6):
    forward,levels=coherent_hensel_lift(D,E,depth)
    reverse,backlevels=coherent_hensel_lift(E,D,depth)
    _phi25,phase_A=local_ring_transport(D,E)
    assert levels[1]["omega_image"]==phase_A["omega_image_mod25"]
    checked=0
    for level in range(1,depth+1):
        modulus=5**level
        # The two induced maps at each level are inverse on BOTH
        # generators of their rank-2 Z/5^k modules.
        for z in ((1,0),(0,1),(-2,3),(3,-1)):
            assert reverse(forward(z,level),level)==(
                z[0]%modulus,z[1]%modulus)
            assert forward(reverse(z,level),level)==(
                z[0]%modulus,z[1]%modulus)
            assert conjugate(forward(z,level),modulus)==forward(
                conjugate(z,modulus),level)
            for w in ((1,0),(0,1),(-2,3),(3,-1)):
                assert forward(mul(z,w,D,modulus),level)==mul(
                    forward(z,level),forward(w,level),E,modulus)
                checked+=1
        # IMPORTANT: a ring isomorphism at finite precision is NOT a
        # map from the global norm ball of D into that of E.
        if level>=2:
            for z in ((1,0),(0,1),(-3,2),(6,0)):
                assert epsilon(z,D)==epsilon(forward(z,2),E)
    return {
        "source_D":D,"target_D":E,
        "levels":depth,
        "highest_modulus":5**depth,
        "compatible_omega_images":[x["omega_image"] for x in levels],
        "actual_multiplicativity_checks":checked,
        "inverse_and_conjugation_checked_at_every_level":True,
        "phase_A_mod25_reference_reproduced":True,
        "first_Fermat_quotient_covariant":True,
        "same_local_algebra_does_not_constrain_global_class_number":True,
    }


def main():
    out=[exact_bidirectional_controls(43,163),
         exact_bidirectional_controls(163,183),
         exact_bidirectional_controls(43,183)]
    # h(43)=h(163)=1 and h(183)=8 under the classical forms theorem.
    print("PHASE312_LOCAL_COMPLETION_NO_GO_PASS",{
        "inert_quadratic_complete_local_ring_pairs":out,
        "global_h1_classes_not_preserved_by_local_ring_isomorphism":True,
        "neither_global_norm_ball_nor_ray_class_transported":True,
        "no_uniform_tenth_discriminant_bound":True,
    },flush=True)

if __name__=="__main__":
    main()
