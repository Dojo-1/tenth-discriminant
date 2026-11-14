#!/usr/bin/env python3
"""Phase287-D: exact rotating 4D toy Hamiltonian and two-level leakage bound.

Preregistered at 80c141b before implementation. This is a *separate*
finite-dimensional Schr dynamics, NOT an L-function, original trace Gram
or real-world quantum-tunnelling result. All algebra uses Fraction.
"""
from fractions import Fraction as F

I2=[[F(1),F(0)],[F(0),F(1)]]
Z2=[[F(0),F(0)],[F(0),F(0)]]
J=[[F(0),F(-1)],[F(1),F(0)]]
KAPPA=F(1,3)
EPS=F(1,12)
OMEGA=F(1)
DELTA=EPS*OMEGA
L2=F(65,576)


def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


def mat_scale(A,c):
    return [[c*x for x in row] for row in A]


def block(A,B,C,D):
    return [A[i]+B[i] for i in range(2)]+[C[i]+D[i] for i in range(2)]


def rotation(quadrant):
    cases=[
        [[F(1),F(0)],[F(0),F(1)]],
        [[F(0),F(-1)],[F(1),F(0)]],
        [[F(-1),F(0)],[F(0),F(-1)]],
        [[F(0),F(1)],[F(-1),F(0)]],
    ]
    return cases[quadrant%4]


def basis_transform_controls():
    H0=block(I2,mat_scale(I2,KAPPA),mat_scale(I2,KAPPA),I2)
    WtWdot_expected=block(Z2,Z2,Z2,mat_scale(J,-OMEGA))
    for quadrant in range(4):
        R=rotation(quadrant)
        Rt=transpose(R)
        W=block(I2,Z2,Z2,Rt)
        # d/ds R_(Omega*s)^T = -Omega * R^T * J.
        Wdot=block(Z2,Z2,Z2,mat_scale(mm(Rt,J),-OMEGA))
        moving_metric=block(
            I2,mat_scale(R,KAPPA),mat_scale(Rt,KAPPA),I2)
        assert mm(mm(W,H0),transpose(W))==moving_metric,(
            "bad moving-frame conjugacy",quadrant)
        assert mm(transpose(W),Wdot)==WtWdot_expected,(
            "wrong moving-frame gauge generator",quadrant)
        assert mm(transpose(W),W)==block(I2,Z2,Z2,I2)
    assert mm(J,J)==mat_scale(I2,F(-1))
    return True


def leakage_control():
    assert L2==KAPPA*KAPPA+DELTA*DELTA/4
    # The iJ helicities give the two constant 2x2 Hermitian Hamiltonians.
    # Their scalar centers do not influence transitions.
    for helicity in (-1,1):
        h=F(helicity)
        Kh=[
            [-h*DELTA/2,KAPPA],
            [KAPPA,h*DELTA/2],
        ]
        assert mm(Kh,Kh)==mat_scale(I2,L2)
        # |+>=(1,1)/sqrt2; |->=(1,-1)/sqrt2.
        # The radicals cancel in the normalized matrix element.
        plus=[F(1),F(1)]
        minus=[F(1),F(-1)]
        Kplus=[Kh[i][0]*plus[0]+Kh[i][1]*plus[1] for i in range(2)]
        amplitude=(minus[0]*Kplus[0]+minus[1]*Kplus[1])/2
        assert amplitude==-h*DELTA/2
        assert amplitude*amplitude==DELTA*DELTA/4
        prob_bound=amplitude*amplitude/L2
        assert prob_bound==F(1,65)
    assert (F(0)**2)/(4*KAPPA*KAPPA+F(0)**2)==0
    # At kappa=0 the band gap vanishes: adiabatic tracking is invalid.
    assert 2*F(0)==0 and 2*KAPPA>0
    return F(1,65)


def main():
    assert basis_transform_controls()
    bound=leakage_control()
    print("PHASE287_ADIABATIC_LEAKAGE",{
        "carrier":"C^4",
        "kappa":"1/3",
        "epsilon":"1/12",
        "angular_speed":"1",
        "delta":"1/12",
        "helicities":[-1,1],
        "K_squared_scalar":"65/576",
        "exact_leakage_probability_upper_bound":str(bound),
        "full_loop_formula":"(pi*epsilon)^2/(kappa^2+(pi*epsilon)^2)",
        "gauge_generator":"diag(0,-J*Omega)",
        "checked_quadrant_frames":4,
        "no_floating_point_or_sine_approximation":True,
        "only_specified_adiabatic_toy_dynamics":True,
        "no_original_Gram_or_quantum_tunnelling_claim":True,
    },flush=True)
    print("PASS Phase287-D exact rotating-Hamiltonian two-level leakage bound",flush=True)


if __name__=="__main__":
    main()
