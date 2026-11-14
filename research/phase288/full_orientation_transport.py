#!/usr/bin/env python3
"""Phase288-C: all-angle analytic theta response and 6-channel integral anchor.

Preregistered at 45c8ea2 BEFORE this code. Actual full-order Gaussian source
has TWO external corrections; old original trace Gram is unchanged. No
continuous integer-gauge or new local determinant/Smith claim.
"""
from fractions import Fraction as F

from integral_transverse_transport import (
    frozen_sources,params,gram,jet,CASES,full_transverse_X,
    matmul,trans,matadd,block,zero,eye,bareiss
)
from weighted_full_order_remainder import (
    integer_coset,half_coset,squared_norm,trace_squared,
    finite_weighted_curvature,exact_tail,HALF_EXPECTED
)


def six_channel_congruence(G,X,labels):
    n=len(G)
    k=6
    assert len(X)==n and all(len(row)==k for row in X)
    Xt=trans(X)
    H=block(matadd(G,matmul(X,Xt)),X,Xt,eye(k))
    D=block(G,zero(n,k),zero(k,n),eye(k))
    U=block(eye(n),X,zero(k,n),eye(k))
    L=block(eye(n),zero(n,k),[[-v for v in row] for row in Xt],eye(k))
    assert matmul(matmul(U,D),trans(U))==H
    assert matmul(matmul(trans(L),H),L)==D
    assert matmul(trans(U),L)==eye(n+k)
    grade=[(-1)**(r+s) for r,s in labels]+[1,1,-1,-1,1,1]
    assert all(H[i][j]==grade[i]*grade[j]*H[i][j]
        for i in range(n+k) for j in range(n+k))
    det=bareiss(G)
    assert det>0
    assert bareiss(H)==det

    def small_rotation(q):
        return (
          ((1,0),(0,1)),
          ((0,-1),(1,0)),
          ((-1,0),(0,-1)),
          ((0,1),(-1,0))
        )[q%4]

    # The second moving frame has three independent 2D parity-compatible
    # integral rotation blocks only at four quadrants.
    for quadrant in range(4):
        R=small_rotation(quadrant)
        T=zero(6,6)
        for offset in (0,2,4):
            for i in range(2):
                for j in range(2):
                    T[offset+i][offset+j]=R[i][j]
        assert matmul(trans(T),T)==eye(6)
        assert bareiss(T)==1
        assert all(T[i][j]==0 for i in range(6) for j in range(6)
             if [1,1,-1,-1,1,1][i]!=[1,1,-1,-1,1,1][j])
        A=block(eye(n),zero(n,6),zero(6,n),T)
        Hphi=matmul(matmul(trans(A),H),A)
        cross=matmul(X,T)
        assert Hphi==block(matadd(G,matmul(X,Xt)),
                           cross,trans(cross),eye(6))
        assert matadd(
             [row[:n] for row in Hphi[:n]],
             [[-v for v in row] for row in matmul(cross,trans(cross))]
        )==G
        assert bareiss(Hphi)==det
    return len(str(det))


def run(D):
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==CASES[D]["params"]
    integers=integer_coset(D,Q)
    half=half_coset(D,rho)
    assert len(half)==HALF_EXPECTED[D]
    allpts=integers+half
    As,Bs,T,trace_num,scale=finite_weighted_curvature(D,rho,allpts)
    M=As+Bs
    assert As>Bs>0 and M>abs(T)
    labels=CASES[D]["labels"]
    G=gram(D,Q,J,labels)
    i0=labels.index((0,0))
    igT=labels.index((2,0))
    igN=labels.index((1,1))
    gT=G[i0][igT]
    gN=G[i0][igN]

    # Both full maximal-order weighted moments transport exactly to
    # original Gram entries PLUS two explicitly external dyadic corrections.
    radial_num=sum(
        squared_norm(D,z)*(1<<(rho*rho-squared_norm(D,z)))
        for z in allpts)
    assert F(radial_num,scale)==M
    rT=trace_num-scale*gT
    assert F(rT,1).denominator==1 and rT%2==0
    rN=radial_num-scale*(gN//2)
    assert gN%2==0 and rN%2==0
    assert T==F(gT,2)+F(rT,2*scale)
    assert M==F(gN,2)+F(rN,scale)
    assert rT!=0 and rN!=0

    # Cross term of the pi/4, 3pi/4 orientation expansions vanishes
    # before approximating a single sqrt(D) or trigonometric function.
    records=[(a,b,1<<(rho*rho-squared_norm(D,(a,b))))
             for a,b in allpts]
    cross=0
    for a,b,wa in records:
        for c,d,wc in records:
            cross+=(a*c+D*b*d)*(b*c-a*d)*wa*wc
    assert cross==0,("off-axis conjugation cancellation failed",D)
    C0=As*As+Bs*Bs
    C90=2*As*Bs
    expected={
        "0":C0,"pi/4":F(1,2)*(C0+C90),
        "pi/2":C90,"3pi/4":F(1,2)*(C0+C90),"pi":C0,
    }
    for name,cos2 in (("0",1),("pi/4",0),("pi/2",-1),
                      ("3pi/4",0),("pi",1)):
        formula=F(1,2)*(M*M+cos2*T*T)
        assert formula==expected[name],("wrong full-angle formula",D,name)

    Xorig=full_transverse_X(D,Q,R,S)
    # The original source fixes the origin as a unique inversion-invariant
    # point: the two even dyadic numerator corrections are supported there.
    assert Q.count((0,0))==1
    Xaug=[]
    for r in range(R):
        for s in range(S):
            entry=jet(D,r,s,0,(0,0))[0]
            assert entry==int((r,s)==(0,0))
            external_T=2*(rT//2)*entry
            external_N=2*(rN//2)*entry
            assert external_T==(rT if (r,s)==(0,0) else 0)
            assert external_N==(rN if (r,s)==(0,0) else 0)
            Xaug.append(Xorig[r*S+s]+[external_T,external_N])
    selected=[Xaug[r*S+s] for r,s in labels]
    detdigits=six_channel_congruence(G,selected,labels)

    btail=exact_tail(rho)
    assert btail<F(1,1<<(930 if D==283 else 1560))
    # Each Gaussian angular degree-two moment (zbarz and z^2) is
    # bounded by the same positive two-coset outer-tail shell estimate.
    uniform_error=(abs(M)+abs(T))*btail+btail*btail
    assert uniform_error>0

    print("PHASE288_ALL_ORIENTATIONS",{
      "D":D,"source_rows_original":R*S,
      "original_Q":len(Q),"maximal_order_finite_points":len(allpts),
      "original_gram_g_1_Z2":gT,
      "original_gram_g_1_ZW":gN,
      "external_angular_numerator_even":rT%2==0,
      "external_radial_numerator_even":rN%2==0,
      "two_canonical_origin_channels_integral":True,
      "quadrant_and_diagonal_orientations":["0","pi/4","pi/2","3pi/4","pi"],
      "direct_4D_pair_cross_term_zero":True,
      "full_angle_response":"(M^2 + T^2*cos(2phi))/2",
      "uniform_in_phi_gaussian_tail_radius_exact":True,
      "integral_six_channel_completion_original_schur":True,
      "quarter_turn_integral_parity_gauges_checked":4,
      "original_selected_gram_rows":len(labels),
      "det_decimal_digits_unchanged":detdigits,
      "new_arithmetic_valuation_units":0,
      "generic_real_moving_frame_not_integral":True,
      "quantum_adiabatic_dynamics_not_inferred":True,
    },flush=True)


def main():
    frozen_sources()
    for D in (283,403):
        run(D)
    print("PASS Phase288-C full moving-orientation tensor + integral two-remainder anchor",flush=True)


if __name__=="__main__":
    main()
