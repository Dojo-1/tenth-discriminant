#!/usr/bin/env python3
"""Phase307-I: genuine Picard/ideal-class obstruction in quadratic maximal orders.

Paper theorem: Pic(Spec O_K)=Cl(O_K) for Dedekind O_K. This finite
ring-map/norm harness checks particular ideal classes; it does NOT compute a
Cech cocycle, a full class group, or a new discriminant bound.
"""
from math import isqrt


def squarefree(d):
    return d>0 and all(d%(n*n) for n in range(2,isqrt(d)+1))


def mvalue(d):
    if d<=0 or d%4!=3 or not squarefree(d):
        raise ValueError("fundamental imaginary-quadratic D=3 mod4 required")
    return (d+1)//4


def omega_mul(x,y,d):
    a,b=x
    c,e=y
    m=mvalue(d)
    return a*c-m*b*e, a*e+b*c+b*e


def omega_norm(x,d):
    a,b=x
    return a*a+a*b+mvalue(d)*b*b


def defining_polynomial(x,d,p):
    m=mvalue(d)
    return (x*x-x+m)%p


def residue_roots(d,p):
    if p<2 or not all(p%q for q in range(2,isqrt(p)+1)):
        raise ValueError("rational prime p required")
    return tuple(r for r in range(p) if defining_polynomial(r,d,p)==0)


def psi(x,r,p):
    a,b=x
    return (a+b*r)%p


def independent_bounded_homomorphism(d,p,r):
    """Polynomial relation plus explicit independent multiplication checks."""
    assert defining_polynomial(r,d,p)==0
    count=0
    for a in range(-3,4):
      for b in range(-3,4):
       for c in range(-3,4):
        for e in range(-3,4):
         x,y=(a,b),(c,e)
         product=omega_mul(x,y,d)
         assert psi(product,r,p)==psi(x,r,p)*psi(y,r,p)%p
         count+=1
    return count


def local_ideal_class_certificate(d,p):
    m=mvalue(d)
    roots=residue_roots(d,p)
    result={
        "D":d,"p":p,"m":m,
        "polynomial_roots":roots,
        "roots_give_surjective_O_to_Fp":bool(roots),
        "ideal_I_p_omega_minus_r_norm_p_if_root":bool(roots),
        "bounded_ring_multiplicativity_checks":0,
        "nonprincipal_norm_obstruction":False,
        "principal_boundary_example":False,
    }
    for r in roots:
        result["bounded_ring_multiplicativity_checks"]+=independent_bounded_homomorphism(d,p,r)
    if not roots:
        result["no_root_no_degree_one_ideal_from_this_recipe"]=True
        return result
    # Since a^2+a*b+m*b^2 >=m for all nonzero b, p<m and p
    # not a rational square rule out norm p, hence principal generator.
    if p<m and isqrt(p)**2!=p:
        result["nonprincipal_norm_obstruction"]=True
        result["Picard_class_nontrivial"]=True
        return result
    # At D163,p41=m, omega and bar(omega) provide explicit norm-p generators.
    if d==163 and p==41:
        witness={0:(0,1),1:(1,-1)}
        assert set(roots)==set(witness)
        for r in roots:
            gen=witness[r]
            assert omega_norm(gen,d)==p
            assert psi(gen,r,p)==0
        result["principal_boundary_example"]=True
        result["Picard_class_nontrivial"]=False
    return result


def main():
    expected=((203,3,(0,1),51),
              (187,7,(2,6),47),
              (167,2,(0,1),42))
    for d,p,roots,m in expected:
        cert=local_ideal_class_certificate(d,p)
        assert cert["polynomial_roots"]==roots
        assert cert["m"]==m
        assert cert["nonprincipal_norm_obstruction"]
        assert cert["bounded_ring_multiplicativity_checks"]==len(roots)*7**4
        print("PHASE307_PICARD_NONPRINCIPAL_CERT",cert,flush=True)
    inert=local_ideal_class_certificate(163,3)
    assert inert["polynomial_roots"]==()
    assert not inert["nonprincipal_norm_obstruction"]
    boundary=local_ideal_class_certificate(163,41)
    assert boundary["polynomial_roots"]==(0,1)
    assert boundary["principal_boundary_example"]
    assert not boundary["nonprincipal_norm_obstruction"]
    print("PHASE307_PICARD_FIELD_BRIDGE_PASS",{
        "nonprincipal_D203_p3_D187_p7_D167_p2":True,
        "inert_D163_p3_no_false_split_ideal":True,
        "D163_p41_norm_m_boundary_principal":True,
        "Pic_Spec_OK_equals_class_group_is_P_paper":True,
        "no_Cech_class_or_full_class_group_computed":True,
        "no_new_uniform_field_or_discriminant_bound":True
    },flush=True)


if __name__=="__main__":
    main()
