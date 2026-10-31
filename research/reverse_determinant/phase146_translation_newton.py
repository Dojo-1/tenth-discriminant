#!/usr/bin/env python3
"""Phase146: integer jet translation, rational centering and Newton-fiber cap.

Original ordinary Z jets with W held fixed and trace weights (2,2D).
Finite exact evidence is separate from the universal paper-level polynomial
identities. No Lean theorem, new class-number bound or solver claim.
Run: python3 research/reverse_determinant/phase146_translation_newton.py
"""
from __future__ import annotations
from math import comb, log
from sympy import Matrix, Rational, eye
from sympy.matrices.normalforms import hermite_normal_form
from phase144_verifier import D, R, S, J, FULL, FOUR, evaluation, lattice
from phase144_minimum_support import SIX
from phase145_ortho_anti_ambig import P, gram, natural_log
from phase140_exact_trim import qellipse

assert (D, R, S, J) == (19, 8, 4, 4)
N = R*S


def transport(a, r=R, s=S):
    """Row action for (Z+a)^r (W+a)^s; unit lower triangular over Z[a]."""
    return Matrix(r*s, r*s, lambda i,k:
        comb(i//s, k//s)*comb(i%s, k%s)*a**(i//s+i%s-k//s-k%s)
        if k//s <= i//s and k%s <= i%s else 0)


def arithmetic_pairs(a,b,d):
    return (a[0]*b[0]-d*a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def pair_power(a,k,d):
    ans=(1,0)
    for _ in range(k):
        ans=arithmetic_pairs(ans,a,d)
    return ans


def falling(r,j):
    out=1
    for k in range(j):
        out*=r-k
    return out


def evaluate_parameters(Q,d,r=R,s=S,jets=J):
    """Independent D-parameter realization; cross-check against original at D19."""
    columns=[]
    for x,y in Q:
        z,w=(x,y),(x,-y)
        zp=[pair_power(z,k,d) for k in range(r)]
        wp=[pair_power(w,k,d) for k in range(s)]
        rows=[]
        for rr in range(r):
            for ss in range(s):
                record=[]
                for jj in range(jets):
                    v=arithmetic_pairs(zp[rr-jj],wp[ss],d) if jj<=rr else (0,0)
                    f=falling(rr,jj)
                    record.append((f*v[0],f*v[1]))
                rows.append(record)
        for jj in range(jets):
            for channel in (0,1):
                columns.append([row[jj][channel] for row in rows])
    return Matrix(r*s,len(columns),lambda i,k:columns[k][i])


def det_int(m):
    v=int(m.det(method='domain-ge'))
    assert v!=0
    return abs(v)


def log_ratio(q):
    return natural_log(int(q.p))-natural_log(int(q.q))


def pinch(G,grading):
    return (G+grading*G*grading.T)/2


def chi(G,grading):
    dp=det_int(pinch(G,grading))
    dg=det_int(G)
    return natural_log(dp)-natural_log(dg),Rational(dp,dg)


def row_energy_diagonal(Q,d,r,s,jets,center):
    """Exact rational diagonal of the shifted polynomial-row Gram."""
    out=[]
    for rr in range(r):
        for ss in range(s):
            energy=Rational(0)
            for x,y in Q:
                qnorm=(Rational(x)-center)**2+d*y*y
                for jj in range(min(rr,jets-1)+1):
                    energy+=2*falling(rr,jj)**2*qnorm**(rr+ss-jj)
            out.append(energy)
    return out


def radius_majorant(Q,d,r,s,jets,center):
    """No Gram inverse: 2*card(Q)*sum_j (r)_j^2 * radius^(2(r+s-j))."""
    radius2=max((Rational(x)-center)**2+d*y*y for x,y in Q)
    return radius2,[2*len(Q)*sum(
        falling(rr,jj)**2*radius2**(rr+ss-jj)
        for jj in range(min(rr,jets-1)+1))
        for rr in range(r) for ss in range(s)]


def sumlog(diagonal):
    assert all(v>0 for v in diagonal)
    return sum(log_ratio(Rational(v)) for v in diagonal)


def finite_difference_cap(Q,r,s):
    """Retain at most degree+1 CONSECUTIVE nodes in each horizontal fiber."""
    degree=r+s-2
    ans=[]
    for y in sorted({b for _,b in Q}):
        xs=sorted(x for x,yy in Q if yy==y)
        assert xs==list(range(xs[0],xs[-1]+1))
        ans.extend((x,y) for x in xs[:degree+1])
    return sorted(ans)


def phase146_translation():
    E6=evaluation(SIX)
    Ef=evaluation(FULL)
    fourdet=det_int(evaluation(FOUR))
    Hfull,dfull=lattice(Ef,fourdet)
    H6,d6=lattice(E6,fourdet)
    assert Hfull==H6 and dfull==d6
    assert evaluate_parameters(FULL,19)==Ef  # No silent change of jet meaning.
    assert transport(0)==eye(N)
    assert transport(1)*transport(-1)==eye(N)
    assert transport(1)*transport(2)==transport(3)
    assert transport(1).det()==1
    for a in (-1,1,2):
        Qshift=[(x+a,y) for x,y in SIX]
        assert evaluation(Qshift)==transport(a)*E6
    shifted=[(x+1,y) for x,y in SIX]
    assert set(shifted).issubset(set(FULL))
    # The translated FOUR determinant is a valid nonsingular square minor.
    assert det_int(evaluation([(x+1,y) for x,y in FOUR]))==fourdet
    Hshift,dshift=lattice(evaluation(shifted),fourdet)
    assert Hshift==Hfull and dshift==dfull
    # This is an integer automorphism, not merely Smith-factor coincidence.
    Ct=Hfull.inv()*transport(1)*Hfull
    assert all(z.q==1 for z in Ct)
    assert Ct.det()==1
    print('PASS: source-matched integer translation, Q6+1 inside ellipse, stable full column image')

    G6=gram(E6)
    assert det_int(G6)>0
    T2=transport(2)
    G2=gram(evaluation([(x+2,y) for x,y in SIX]))
    assert G2==T2*G6*T2.T
    assert det_int(G2)==det_int(G6)
    P2=T2*P*transport(-2)
    assert P2*P2==eye(N)
    assert pinch(G2,P2)==T2*pinch(G6,P)*T2.T
    chi0,quot0=chi(G6,P)
    chi_moved,quot_moved=chi(G2,P2)
    chi_fixed,quot_fixed=chi(G2,P)
    assert quot_moved==quot0 and quot_fixed>quot0
    print('parity chi original, translated-fixed, translated-moving:',
          f'{chi0:.12f}',f'{chi_fixed:.12f}',f'{chi_moved:.12f}')
    print('PASS: move frame AND grading; fixed-grading rise is representation artifact')
    assert not set((x+2,y) for x,y in SIX).issubset(set(FULL))
    print('NOTE: +2 translation leaves the sampling ellipse; gauge control only')

    centered=[]
    for center in (Rational(0),Rational(-1,2)):
        Tcenter=transport(-center)
        Gc=Tcenter*G6*Tcenter.T
        exact=row_energy_diagonal(SIX,D,R,S,J,center)
        assert all(Gc[i,i]==exact[i] for i in range(N))
        assert det_int(Gc)==det_int(G6)
        radius2,coarse=radius_majorant(SIX,D,R,S,J,center)
        assert radius2 in (Rational(23),Rational(85,4))
        h=sumlog(exact); c=sumlog(coarse)
        assert h>=natural_log(det_int(G6)) and c>=h
        centered.append((center,radius2,h,c))
    assert centered[1][2]<centered[0][2]
    assert centered[1][3]<centered[0][3]
    for center,radius2,h,c in centered:
        print('center',center,'max_radius_squared',radius2,
              'actual-diagonal Hadamard log',f'{h:.9f}',
              'radius-only log bound',f'{c:.9f}')
    print('PASS: rational unimodular moving frame improves a certified (loose) upper without Gram inverse')


def phase146_cross_d():
    # Eight real x-axis points give a square full-rank original jet witness,
    # independent of d (imaginary coordinates are identically zero on y=0).
    realnodes=[(x,0) for x in range(-4,4)]
    Er=evaluation(realnodes)
    xr=Er[:,[8*t+2*j for t in range(8) for j in range(J)]]
    real_witness=det_int(xr)
    T1=transport(1)
    ratio={}
    stability={}
    for d in range(1,27):
        full=sorted(qellipse(d,5))
        Efull=evaluate_parameters(full,d)
        hf=hermite_normal_form(Efull,D=real_witness)
        index_full=det_int(hf)
        # A one-step translation is image-stable iff the right-endpoint
        # columns of each contiguous horizontal fiber are in the image.
        invh=hf.inv()
        global_test=all(v.q==1 for v in invh*T1*hf)
        boundary=[]
        for y in sorted({yy for _,yy in full}):
            xmax=max(x for x,yy in full if yy==y)
            boundary.append((xmax+1,y))
        boundary_test=all(v.q==1 for v in
                          invh*evaluate_parameters(boundary,d))
        assert global_test==boundary_test
        stability[d]=global_test
        if d<=21:
            assert set(SIX).issubset(set(full))
            W4=det_int(evaluate_parameters(FOUR,d))
            H6=hermite_normal_form(evaluate_parameters(SIX,d),D=W4)
            index6=det_int(H6)
            assert index6%index_full==0
            ratio[d]=index6//index_full
            assert (H6==hf)==(ratio[d]==1)
            if d in (13,17,19,21):
                print('cross-D',d,'points',len(full),'index ratio',
                      ratio[d],'translation-stable',global_test)
        if d in (18,23,24,25,26):
            print('boundary-D',d,'nodes',len(full),
                  'right-fiber boundary test',boundary_test)
    winners={d for d,k in ratio.items() if k==1}
    assert winners=={3,4,6,10,12,16,19}
    assert {d for d,s in stability.items() if not s}=={18,23,24,25}
    assert {d:ratio[d] for d in (13,17,19,21)}=={13:16,17:1296,19:1,21:112}
    print('image equality D=1..21:',sorted(winners))
    print('translation-instability D=1..26:',
          sorted(d for d,s in stability.items() if not s))
    print('PASS: 26 exact integer-parameter boundary controls; fixed six-point uniformity falsified')


def phase146_newton_cap():
    tests=((1,3,2,2,5),(3,3,2,2,5),(19,3,2,2,5),
           (26,3,2,2,5),(3,4,2,2,5))
    for d,r,s,jets,rho in tests:
        full=sorted(qellipse(d,rho))
        cap=finite_difference_cap(full,r,s)
        hf=hermite_normal_form(evaluate_parameters(full,d,r,s,jets))
        hc=hermite_normal_form(evaluate_parameters(cap,d,r,s,jets))
        assert hf==hc and len(cap)<len(full)
        degree=r+s-2
        # One-step Newton recurrence at every horizontal boundary with
        # at least (degree+2) consecutive nodes; integer coefficients.
        for y in {b for _,b in full}:
            xs=sorted(x for x,yy in full if yy==y)
            if len(xs)<=degree+1:
                continue
            x0=xs[0]
            predicted=Matrix.zeros(r*s,2*jets)
            for i in range(degree+1):
                coefficient=(-1)**(degree-i)*comb(degree+1,i)
                predicted+=coefficient*evaluate_parameters(
                    [(x0+i,y)],d,r,s,jets)
            actual=evaluate_parameters([(x0+degree+1,y)],d,r,s,jets)
            assert predicted==actual
        print('Newton cap d,R,S,J=',d,r,s,jets,'points',len(full),
              '->',len(cap),'same integral image')
    # At the declared production floor (450)^4, the simple cap removes
    # no point: even the longest horizontal fiber is 112x TOO SHORT.
    floor=450**4
    rr=floor//4; ss=rr//25
    rho=(13*450**3+24)//25
    largest_fiber=2*rho+1
    need=rr+ss-1
    assert floor==41006250000 and rho==47385000
    assert largest_fiber==94770001 and need==10661624999
    assert largest_fiber<need
    print('production-floor cap barrier: max fiber',largest_fiber,
          'needed',need,'ratio',f'{need/largest_fiber:.4f}')
    print('PASS: universal paper-level fiber identity, small finite HNF controls; cap idle at floor')


def main():
    phase146_translation()
    phase146_cross_d()
    phase146_newton_cap()
    print('PHASE146_PASS: integer translation, representation correction, D controls, Newton cap')


if __name__=='__main__':
    main()
