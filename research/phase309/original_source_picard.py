#!/usr/bin/env python3
"""Phase309: original-source observation restriction with a genuine Picard obstruction.

The source matrix is obtained by retaining rows (1,Z) and j=0 from the
unchanged original polynomial source, then explicitly base-changing
coefficients from Z to the maximal integer ring O_K. The Picard class
belongs to this *O-linear restricted map*, NOT automatically to the full
original integer trace Gram or any uniform field theorem.
"""
from dataclasses import dataclass
from math import gcd, isqrt
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
for name in ("phase206","phase304","phase308"):
    sys.path.insert(0,str(ROOT/"research"/name))
import source_probe
import highjet_d203_original as original_d203
import picard_tendrils as ideals
from adaptive_torsion_family import principalization_scanner

CASES=(
    (203,3,0,4,((6,7),(7,120)),671),
    (187,7,2,2,((6,11),(11,196)),1055),
    (167,2,0,11,((6,5),(5,92)),527),
)


@dataclass(frozen=True)
class RestrictedSource:
    D: int
    p: int
    r: int
    rho: int
    R: int
    S: int
    J: int
    observations: tuple
    selected_original_source_labels: tuple
    field_source_type: str = "O_K x O_K after explicit scalar extension"
    integer_source_unchanged: bool = True

    def __post_init__(self):
        if self.selected_original_source_labels!=((0,0),(1,0)):
            raise ValueError("not the preregistered original source rows")
        if self.S<1 or self.R<2 or self.J<1:
            raise ValueError("original source lacks required rows or jet zero")


def maximal_points(D,rho):
    """Independent genuine maximal-order norm ball, not the even integer order."""
    m=ideals.order_parameter(D)
    out=[]
    b_max=isqrt(4*rho*rho//D)
    for b in range(-b_max,b_max+1):
        xmax=isqrt(4*rho*rho-D*b*b)
        for x in range(-xmax,xmax+1):
            if (x-b)%2==0:
                a=(x-b)//2
                assert ideals.norm((a,b),D)<=rho*rho
                out.append((a,b))
    assert len(out)==len(set(out))
    return tuple(out)


def patch_source(D,p,r):
    m=ideals.order_parameter(D)
    if p<2 or any(p%q==0 for q in range(2,isqrt(p)+1)):
        raise ValueError("patch rational prime required")
    if (r*r-r+m)%p != 0:
        raise ValueError("r is NOT a root of the maximal-order relation mod p")
    if (2*r-1)%p == 0:
        raise ValueError("simple split root required, not ramification")
    rho,R,S,J,_=source_probe.params(D)
    points=maximal_points(D,rho)
    z=(-r,1)
    obs=((0,0),(p,0),z)
    if not all(q in points for q in obs):
        raise ValueError("nonexistent original observation in requested patch")
    assert (0,0) in points and (1,0) in points
    return RestrictedSource(D,p,r,rho,R,S,J,obs,((0,0),(1,0))),points


def exact_patch_matrix(ps):
    """3 observations x 2 polynomial source rows, entries in O coordinates."""
    return tuple(((1,0),z) for z in ps.observations)


def two_by_two_minors(A,D):
    """Determinant over commutative O, not a scalar Euclidean Gram determinant."""
    assert len(A)>=2 and all(len(row)==2 for row in A)
    out=[]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            left=ideals.mul(A[i][0],A[j][1],D)
            right=ideals.mul(A[j][0],A[i][1],D)
            out.append((left[0]-right[0],left[1]-right[1]))
    return tuple(out)


def trace_pair(x,y,D):
    a,b=x
    c,d=y
    m=ideals.order_parameter(D)
    return 2*a*c+a*d+b*c+2*m*b*d


def original_integer_trace_gram(ps):
    """Exactly the source's trace-Hermitian Gram on selected j=0 coordinates."""
    z0=((1,0),)*3
    z1=ps.observations
    rows=(z0,z1)
    return tuple(tuple(sum(trace_pair(x,y,ps.D) for x,y in zip(s,t))
                       for t in rows) for s in rows)


def original_d203_oracle(ps,q):
    """Compare original frozen 100x1052 source at BOTH ordinary j0/j1."""
    assert ps.D==203 and (ps.R,ps.S,ps.J)==(50,2,2)
    original_d203.guard()
    frozen=original_d203.qmax(ps.rho)
    assert tuple(frozen)==q
    assert len(q)==263
    mod=ps.p**6
    E=original_d203.evaluate_original_jets(q,ps.R,ps.S,ps.J,mod)
    # Source row 0 means 1; row 2 means Z, as in original r-major/s-minor.
    comparisons=0
    for z in ps.observations+((1,0),):
        i=q.index(z)
        for row,polyr in ((0,0),(2,1)):
            expected0=(1,0) if polyr==0 else z
            expected1=(0,0) if polyr==0 else (1,0)
            for jet,expected in ((0,expected0),(1,expected1)):
                c=2*(jet*len(q)+i)
                assert (int(E[row,c]),int(E[row,c+1]))==tuple(
                    x%mod for x in expected)
                comparisons+=2
    return {
       "entire_parent_original_matrix_shape":list(E.shape),
       "exact_original_coordinates_compared":comparisons,
       "original_row_indices":[0,2],
       "original_ordinary_jet_indices":[0,1],
       "actual_source_q":len(q),
       "frozen_parent_source_reused":True
    }


def saturation_witness(ps):
    """b=conj(z)/p is in I^-1 but not O when b_omega=-1/p."""
    D,p=ps.D,ps.p
    z=(-ps.r,1)
    c=ideals.conjugate(z)
    numerator=ideals.norm(z,D)
    assert numerator%p==0
    assert c[1]==-1 and c[1]%p!=0
    # a=0, b=conj(z)/p. All coordinates of A(a,b) are INTEGRAL.
    pb=c
    zb=(numerator//p,0)
    assert ideals.mul(z,c,D)==(numerator,0)
    return {
        "b_in_ideal_inverse_but_not_O_K":"conjugate(z)/p",
        "b_numerator_O_coordinates":c,
        "pb_integer_coordinates":pb,
        "zb_integer_coordinates":zb,
        "b_not_integral":True,
        "saturation_strictly_larger_than_original_O_free_image":True,
        "augmented_observation_z1_value_not_integral":True,
    }


def patch_certificate(D,p,r,order,expected_gram,expected_det):
    ps,points=patch_source(D,p,r)
    A=exact_patch_matrix(ps)
    assert A==(((1,0),(0,0)),((1,0),(p,0)),((1,0),(-r,1)))
    minors=two_by_two_minors(A,D)
    assert minors==((p,0),(-r,1),(-r-p,1))
    idx=ideals.ideal_z_index(D,minors)
    assert idx==p
    # This O-ideal is the *actual* (p,omega-r) maximal ideal.
    assert ideals.ideal_z_index(D,((p,0),(-r,1)))==p
    cls=principalization_scanner(D,p,r,order)
    assert cls["first_principal_power"]==order

    G=original_integer_trace_gram(ps)
    assert G==expected_gram,(D,G,expected_gram)
    assert G[0][0]==6
    t=2*p+1-2*r
    nz=ideals.norm((-r,1),D)
    assert G[0][1]==t and G[1][1]==2*(p*p+nz)
    det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
    assert det==expected_det
    assert nz%p==0 and (2*r-1)%p!=0
    assert det%p==(-(1-2*r)**2)%p
    assert det%p !=0
    # Counterworld: adding observation 1 produces a unit minor 1.
    augmented=A+(((1,0),(1,0)),)
    minors_aug=two_by_two_minors(augmented,D)
    assert (1,0) in minors_aug
    assert ideals.ideal_z_index(D,minors_aug)==1
    witness=saturation_witness(ps)
    parent=original_d203_oracle(ps,points) if D==203 else {
       "native_original_params":[ps.rho,ps.R,ps.S,ps.J],
       "all_required_points_in_actual_norm_ball":True,
       "source_rows_and_original_j0_exist":True,
       "no_claim_of_full_phase304_frozen_matrix":True,
    }
    return {
        "D":D,"p":p,"root_r":r,"rho":ps.rho,
        "source_rows":ps.selected_original_source_labels,
        "actual_original_j0_points":ps.observations,
        "base_change":"O_K tensor_Z Z^2 into O_K^2, explicitly",
        "original_Z_source_unchanged":ps.integer_source_unchanged,
        "three_original_maximal_minors":minors,
        "minor_ideal_norm":idx,
        "ideal_class_order":order,
        "saturated_image_type":"O_K direct_sum I_inverse",
        "saturated_steinitz_class":"[I] inverse",
        "strict_saturation_element":witness,
        "original_restricted_trace_Gram":G,
        "original_restricted_trace_Gram_det":det,
        "det_mod_p":det%p,
        "local_nonprincipal_ideal_Does_NOT_force_Gram_p_mass":order>1,
        "add_actual_observation_z1_minor_unit":True,
        "after_z1_minor_ideal_norm":1,
        "NOT_full_original_100row_Picard_class":True,
        "parent_source_faithfulness":parent,
    }


def main():
    results=[patch_certificate(*case) for case in CASES]
    # Separately distinguish the principal D163/p41 ring-level boundary:
    # it is NOT a subpatch of that field's ACTUAL original observation ball.
    rejected=False
    try:
        patch_source(163,41,0)
    except ValueError:
        rejected=True
    assert rejected
    # Deliberately incorrect r for a known nonsplit residue must be rejected.
    wrong=False
    try:
        patch_source(203,5,0)
    except ValueError:
        wrong=True
    assert wrong
    print("PHASE309_ACTUAL_SOURCE_PICARD_PATCH_PASS",{
       "native_field_patch_certificates":results,
       "D163_p41_not_in_original_observation_ball_rejected":True,
       "D203_p5_wrong_root_rejected":True,
       "global_original_Gram_not_changed":True,
       "no_uniform_class_one_bound_improvement":True,
    },flush=True)


if __name__=="__main__":
    main()
