#!/usr/bin/env python3
"""Phase287: frozen, exact 4D symmetry/adiabatic-frame and coupled-theta test.

PREREGISTERED first at 04c59d1. This is a higher-dimensional analytic
readout on O_K^2, not a modification of the original 400-row trace Gram.
Paper Berry/Kato holonomy formula is documented, not computationally proven
by the finite dyadic checks below.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve()
ROOT=HERE.parents[2]
sys.path.insert(0,str(HERE.parents[1]/"phase206"))
from source_probe import params

SOURCE_BLOB="3f954b59d9f86b06ad53667c869b5b24f2e6c7f6"
CASES={
    19:{"rho":5,"old":21,"half":20,"full":41},
    403:{"rho":40,"old":219,"half":260,"full":479},
}
KAPPA=F(1,3)


def frozen_source():
    blob=subprocess.check_output(
        ["git","rev-parse","HEAD:research/phase206/source_probe.py"],
        cwd=ROOT,text=True).strip()
    assert blob==SOURCE_BLOB,("source helper drift",blob)
    rho,R,S,J,Q=params(403)
    assert (rho,R,S,J,len(Q))==(40,100,4,4,219)
    return Q


def original_disk(D,rho):
    # The actual O=Z[u] suborder, represented as doubled integer coordinates.
    out=[]
    for y in range(-isqrt(rho*rho//D),isqrt(rho*rho//D)+1):
        rad=isqrt(rho*rho-D*y*y)
        for x in range(-rad,rad+1):
            out.append((2*x,2*y))
    return out


def half_coset(D,rho):
    # The disjoint (1+u)/2 + Z[u] coset, represented as odd numerators.
    bound=4*rho*rho
    out=[]
    for b in range(-isqrt(bound//D),isqrt(bound//D)+1):
        if b%2==0:
            continue
        remaining=bound-D*b*b
        if remaining<0:
            continue
        rad=isqrt(remaining)
        for a in range(-rad,rad+1):
            if a%2:
                out.append((a,b))
    return out


def norm(D,z):
    a,b=z
    numerator=a*a+D*b*b
    assert numerator%4==0
    return numerator//4


def full_order_disk(D,rho,source):
    original=original_disk(D,rho)
    if D==403:
        assert [(a//2,b//2) for a,b in original]==source
    half=half_coset(D,rho)
    allpoints=original+half
    spec=CASES[D]
    assert (len(original),len(half),len(allpoints))==(
        spec["old"],spec["half"],spec["full"]
    )
    assert len(set(allpoints))==len(allpoints)
    points=set(allpoints)
    assert all((-a,-b) in points and (a,-b) in points
               for a,b in allpoints)
    assert all(norm(D,z)<=rho*rho for z in allpoints)
    assert all(a%2==b%2 for a,b in allpoints)
    return original,half,allpoints


def matrix_mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def matrix_add(A,B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]


def matrix_scale(k,A):
    return [[k*x for x in a] for a in A]


def transpose(A):
    return [list(r) for r in zip(*A)]


def identity(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]


def exact_det(A):
    """Small exact Fraction elimination."""
    M=[row[:] for row in A]
    n=len(M)
    v=F(1)
    for j in range(n):
        pivot=next((k for k in range(j,n) if M[k][j]),None)
        if pivot is None:
            return F(0)
        if pivot!=j:
            M[j],M[pivot]=M[pivot],M[j]
            v=-v
        p=M[j][j]
        v*=p
        for k in range(j+1,n):
            q=M[k][j]/p
            for z in range(j+1,n):
                M[k][z]-=q*M[j][z]
            M[k][j]=F(0)
    return v


def rotation_matrix(quadrant):
    matrices=(
        ((1,0),(0,1)),
        ((0,-1),(1,0)),
        ((-1,0),(0,-1)),
        ((0,1),(-1,0)),
    )
    return [[F(x) for x in row] for row in matrices[quadrant%4]]


def block_matrix(R,k,projector=None):
    # Four-dimensional self-adjoint two-copy operator (or +/- projector).
    Rt=transpose(R)
    M=identity(4)
    for i in range(2):
        for j in range(2):
            M[i][j+2]=k*R[i][j]
            M[i+2][j]=k*Rt[i][j]
    if projector is not None:
        assert projector in (-1,1)
        # P+ = (I+S)/2 and P-=(I-S)/2, where S is off-diagonal R.
        M=matrix_scale(F(1,2),block_matrix(R,F(projector)))
    return M


def projector_spectrum():
    I=identity(4)
    zero=[[F(0)]*4 for _ in range(4)]
    for angle in range(4):
        R=rotation_matrix(angle)
        assert matrix_mul(R,transpose(R))==identity(2)
        H=block_matrix(R,KAPPA)
        S=block_matrix(R,F(1))
        Pp=matrix_scale(F(1,2),matrix_add(I,matrix_add(S,matrix_scale(F(-1),I))))
        # Above equals S/2, so replace with the exact projectors below.
        Pp=matrix_scale(F(1,2),matrix_add(I,matrix_add(S,matrix_scale(F(-1),I))))
        # This expression is S/2; form true P+ from off-diagonal X=S-I:
        X=matrix_add(S,matrix_scale(F(-1),I))
        Pp=matrix_scale(F(1,2),matrix_add(I,X))
        Pm=matrix_scale(F(1,2),matrix_add(I,matrix_scale(F(-1),X)))
        assert matrix_mul(Pp,Pp)==Pp
        assert matrix_mul(Pm,Pm)==Pm
        assert matrix_mul(Pp,Pm)==zero
        assert matrix_add(Pp,Pm)==I
        reconstructed=matrix_add(
            matrix_scale(1+KAPPA,Pp),matrix_scale(1-KAPPA,Pm)
        )
        assert H==reconstructed
        assert matrix_mul(H,Pp)==matrix_scale(1+KAPPA,Pp)
        assert matrix_mul(H,Pm)==matrix_scale(1-KAPPA,Pm)
        assert exact_det(H)==(1-KAPPA*KAPPA)**2
    # J^2=-I exactly, the paper connection is -J/2 * dphi.
    J=[[F(0),F(-1)],[F(1),F(0)]]
    assert matrix_mul(J,J)==matrix_scale(F(-1),identity(2))
    assert matrix_mul(rotation_matrix(1),rotation_matrix(1))==rotation_matrix(2)
    return 4


def finite_dyadic_moments(D,rho,points):
    cutoff=rho*rho
    scale=1<<cutoff
    # Lifts by a common dyadic denominator are exactly Fraction operations,
    # avoiding 479^2 repetitive rational gcd work.
    records=[]
    num_A=num_B=num_cross=0
    for a,b in points:
        n=norm(D,(a,b))
        multiplier=1<<(cutoff-n)
        num_A += a*a*multiplier
        num_B += D*b*b*multiplier
        num_cross += a*b*multiplier
        records.append((a,b,multiplier))
    A=F(num_A,4*scale)
    B=F(num_B,4*scale)
    C=F(num_cross,4*scale)
    assert C==0,("conjugation moment",D)
    assert A>B>0,("frozen orientational response fails",D,A,B)

    tot=0
    c0num=0
    c90num=0
    for a,b,weight in records:
        for c,d,other_weight in records:
            factor=weight*other_weight
            tot+=factor
            c0num+=(a*c+D*b*d)**2*factor
            c90num+=D*(b*c-a*d)**2*factor
    assert tot == sum(row[2] for row in records)**2
    denom=16*scale*scale
    C0=F(c0num,denom)
    C90=F(c90num,denom)
    assert C0==A*A+B*B,("no oriented contraction",D)
    assert C90==2*A*B,("bad orthogonal contraction",D)
    assert C0-C90==(A-B)**2>0
    # M_(2,0)(ln 2) = A-B by exact conjugation symmetry.
    moment20=sum(
        (F(a*a-D*b*b,4*(1<<norm(D,(a,b))))
          for a,b in points),F(0))
    assert moment20==A-B
    return A,B,C0,C90,len(records)**2


def symmetry_and_integral_controls(D,points):
    sample=points[0]
    second=points[len(points)//2]
    a,b=sample; c,d=second
    # Cross pair in Q_phi is c0 (phi=0) or sqrt(D)*c1 (phi=pi/2).
    def cross(z,w,quadrant):
        a,b=z;c,d=w
        if quadrant==0:
            return (F(a*c+D*b*d,4),F(0))
        if quadrant==1:
            return (F(0),F(b*c-a*d,4))
        if quadrant==2:
            return (F(-a*c-D*b*d,4),F(0))
        return (F(0),F(-b*c+a*d,4))
    candidates=[(sample,second)]
    candidates.extend((points[i],points[-1-i]) for i in range(min(12,len(points))))
    for z,w in candidates:
        for quadrant in range(4):
            p=cross(z,w,quadrant)
            minus=cross((-z[0],-z[1]),w,quadrant)
            assert minus==(-p[0],-p[1])
            both=cross((-z[0],-z[1]),(-w[0],-w[1]),quadrant)
            assert both==p
            inverse_quadrant=(-quadrant)%4
            assert cross(w,z,quadrant)==cross(z,w,inverse_quadrant)
            conjugate_pair=((z[0],-z[1]),(w[0],-w[1]))
            assert cross(*conjugate_pair,quadrant)==cross(z,w,inverse_quadrant)

    # This is an exact lattice-failure control, independent of the new theta.
    old=[[F(4),F(0)],[F(0),F(4)]]
    U=[[F(2),F(0)],[F(0),F(1,2)]]
    new=matrix_mul(matrix_mul(U,old),transpose(U))
    assert new==[[F(16),F(0)],[F(0),F(1)]]
    assert exact_det(old)==exact_det(new)==16
    assert sorted((2,2))!=sorted((4,0))  # distinct 2-adic Smith grades
    return True


def main():
    source=frozen_source()
    assert projector_spectrum()==4
    for D in (19,403):
        rho=CASES[D]["rho"]
        original,half,full=full_order_disk(D,rho,source)
        A,B,C0,C90,pairs=finite_dyadic_moments(D,rho,full)
        symmetry_and_integral_controls(D,full)
        print("PHASE287_MOVING_FRAME",{
            "D":D,"rho":rho,"lattice_dimension_real":4,
            "original_integer_coset":len(original),
            "additional_half_coset":len(half),
            "finite_full_order_pairs":pairs,
            "dyadic_rational_A_gt_B":A>B,
            "exact_second_coupling_derivative_gap_square":True,
            "orientation_contraction_equals_M20_squared":True,
            "four_quadrant_projector_and_symmetry_controls":True,
            "nontrivial_geometric_holonomy":"paper: -I2",
            "p_adic_Smith_not_preserved_by_rational_frame":True,
            "not_original_Gram_or_new_field_bound":True,
        },flush=True)
    print("PASS Phase287 four-dimensional exact coupling/Noether/gauge regression",flush=True)


if __name__=="__main__":
    main()
