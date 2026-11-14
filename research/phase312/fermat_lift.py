#!/usr/bin/env python3
"""Quadratic inert-five Fermat quotient and correctly typed local transports.

O_D = Z[omega], omega²=omega-(D+1)/4.
epsilon(x)=(x^5-conj(x))/5 mod5 uses mod25 ring arithmetic.
All operations below are exact integer modular operations. This is
classical unramified Frobenius/p-derivation arithmetic, not a new theorem.
"""
from math import isqrt

P=5

def check_field(D):
    if D<=3 or D%4!=3 or any(D%(k*k)==0 for k in range(2,isqrt(D)+1)):
        raise ValueError("requires squarefree D>3, D=3 mod4")
    if (-D)%5 not in (2,3):
        raise ValueError("requires inert prime5")

def mul(x,y,D,mod):
    m=(D+1)//4
    a,b=x;c,d=y
    return ((a*c-m*b*d)%mod,(a*d+b*c+b*d)%mod)

def add(x,y,mod):
    return ((x[0]+y[0])%mod,(x[1]+y[1])%mod)

def scale(t,x,mod):
    return ((t*x[0])%mod,(t*x[1])%mod)

def sub(x,y,mod):
    return ((x[0]-y[0])%mod,(x[1]-y[1])%mod)

def conjugate(x,mod=None):
    out=(x[0]+x[1],-x[1])
    return out if mod is None else (out[0]%mod,out[1]%mod)

def power(x,k,D,mod):
    if k<0:raise ValueError("negative exponent")
    y=(1,0)
    while k:
        if k&1:y=mul(y,x,D,mod)
        x=mul(x,x,D,mod)
        k//=2
    return y

def field_inverse(x,D):
    check_field(D)
    m=(D+1)//4
    a,b=x
    n=(a*a+a*b+m*b*b)%5
    if not n:raise ZeroDivisionError("zero quadratic field element")
    return scale(pow(n,-1,5),conjugate(x),5)

def epsilon(x,D):
    check_field(D)
    z5=power(x,5,D,25)
    bar=conjugate(x)
    numer=[(z5[i]-bar[i])%25 for i in range(2)]
    if any(v%5 for v in numer):
        raise AssertionError("inert Frobenius integrality failed")
    return (numer[0]//5,numer[1]//5)

def eta(x,D):
    check_field(D)
    z25=power(x,25,D,25)
    numer=[(z25[i]-x[i])%25 for i in range(2)]
    if any(v%5 for v in numer):
        raise AssertionError("F25 Frobenius² integrality failed")
    return (numer[0]//5,numer[1]//5)

def check_fermat_laws(x,y,D):
    e=epsilon(mul(x,y,D,25),D)
    rhs=add(mul(epsilon(x,D),conjugate(y),D,5),
            mul(conjugate(x),epsilon(y,D),D,5),5)
    assert e==rhs,(D,x,y,e,rhs)
    assert eta(x,D)==conjugate(epsilon(x,D),5)
    # The addition law has an explicit cross-polynomial term. Do not
    # mistakenly treat epsilon as an additive derivation.
    addition=epsilon(add(x,y,25),D)
    cross=(0,0)
    from math import comb
    for k in range(1,5):
        term=mul(power(x,k,D,5),power(y,5-k,D,5),D,5)
        cross=add(cross,scale(comb(5,k)//5,term,5),5)
    assert addition==add(add(epsilon(x,D),epsilon(y,D),5),cross,5)
    return True

def local_ring_transport(D,E):
    """O_D/25 -> O_E/25; chosen mod5 identity omega_D -> omega_E.

    Allowed only when the two residue polynomials agree mod5.
    The *corrected* omega-image uses Hensel t; raw omega identification
    modulo25 is generally NOT a ring homomorphism.
    """
    check_field(D);check_field(E)
    mD=(D+1)//4
    mE=(E+1)//4
    if (mD-mE)%5:
        raise ValueError("different mod5 omega coordinate chart")
    coefficient=(mE-mD)//5
    t=scale(coefficient,field_inverse((-1,2),E),5)
    omega_image=(5*t[0]%25,(1+5*t[1])%25)
    residue=sub(add(mul(omega_image,omega_image,E,25),
                    (mD,0),25),omega_image,25)
    assert residue==(0,0),(D,E,t,residue)
    assert conjugate(omega_image,25)==sub((1,0),omega_image,25)
    def phi(x):
        return add((x[0],0),scale(x[1],omega_image,25),25)
    return phi,{
        "D_source":D,"D_target":E,
        "hensel_correction_t":t,
        "omega_image_mod25":omega_image,
        "same_mod5_residue_algebra":True,
        "raw_omega_mapping_not_a_mod25_ring_hom_if_m_diff":
            (mD-mE)%25!=0,
    }


def transport_controls(D,E,coordinate_radius=3):
    phi,metadata=local_ring_transport(D,E)
    checks=0
    for a in range(-coordinate_radius,coordinate_radius+1):
      for b in range(-coordinate_radius,coordinate_radius+1):
        x=(a,b)
        assert epsilon(x,D)==epsilon(phi(x),E)
        assert phi(conjugate(x,25))==conjugate(phi(x),25)
        for c,d in ((1,0),(0,1),(-2,3),(3,-1)):
            y=(c,d)
            assert phi(mul(x,y,D,25))==mul(phi(x),phi(y),E,25)
            checks+=1
    metadata["bounded_multiplicativity_tests"]=checks
    metadata["bounded_epsilon_covariance_tests"]=(2*coordinate_radius+1)**2
    return metadata

def main():
    sample=[(0,0),(1,0),(6,0),(0,1),(1,2),(-4,3)]
    for D in (43,163,183,203):
        for x in sample:
            for y in sample:
                check_fermat_laws(x,y,D)
    assert epsilon((1,0),163)==(0,0)
    assert epsilon((6,0),163)==(4,0)
    records=[transport_controls(43,163),transport_controls(163,183),
             transport_controls(43,183)]
    print("PHASE312_INERT_FERMAT_LIFT_PASS",{
        "twisted_product_and_nonlinear_addition_controls":len(sample)**2*4,
        "same_residue_1_vs_6_distinct_epsilon":True,
        "corrected_local_ring_transports":records,
        "no_h1_conclusion_from_local_ring_equivalence":True,
    },flush=True)

if __name__=="__main__":
    main()
