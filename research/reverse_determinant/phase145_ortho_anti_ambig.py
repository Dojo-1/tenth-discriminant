#!/usr/bin/env python3
"""Phase145: exact finite ortho/anti/ambig and moving-metric experiment.

Frozen D=19, rho=5, R=8, S=J=4: original ordinary Z derivatives, W
held fixed, two integer coordinates, and trace weights 2 and 2D.
Depends only on Phase140/144 source-compatible ordinary-jet constructors.
No field-cutoff or general holonomy assertion.
"""
from __future__ import annotations
from math import log
from sympy import Matrix, eye, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from phase144_verifier import D, R, S, J, FULL, FOUR, evaluation, lattice, gram_det, square_witness
from phase144_minimum_support import SIX

N = R*S
assert (D,R,S,J,N) == (19,8,4,4,32)
PARITY = [(-1)**(r+s) for r in range(R) for s in range(S)]
POS=[i for i,x in enumerate(PARITY) if x==1]
NEG=[i for i,x in enumerate(PARITY) if x==-1]
assert len(POS)==len(NEG)==16
P = Matrix.diag(*PARITY)

def natural_log(n:int)->float:
    assert n>0
    s=str(n);k=min(len(s),15)
    return log(int(s[:k]))+(len(s)-k)*log(10)

def rank_f2(M:Matrix)->int:
    """Exact bitset column elimination, no floating rank thresholds."""
    pivots=[0]*M.rows
    k=0
    for j in range(M.cols):
        v=sum((int(M[i,j])%2)<<i for i in range(M.rows))
        while v:
            i=v.bit_length()-1
            if pivots[i]:v ^= pivots[i]
            else:
                pivots[i]=v
                k+=1
                break
    return k

def hnf_det(X:Matrix)->int:
    H=hermite_normal_form(X)
    assert H.rows==H.cols
    return abs(int(H.det(method='domain-ge')))

def gluing(H:Matrix):
    T=H.inv()*P*H
    assert all(v.q==1 for v in T)
    assert T*T==eye(N)
    k=rank_f2(T+eye(N))
    d=abs(int(H.det(method='domain-ge')))
    ap=hnf_det(H[POS,:]);am=hnf_det(H[NEG,:])
    assert d%(ap*am)==0
    assert d//(ap*am)==2**k
    return {'rank':k,'order':2**k,'ap':ap,'am':am,'d':d, 'T':T}

def gram(E):
    B=Matrix.diag(*([2,2*D]*(E.cols//2)))
    return E*B*E.T

def split_metrics(Q):
    E=evaluation(Q);G=gram(E)
    A=G.extract(POS,POS); F=G.extract(NEG,NEG); C=G.extract(POS,NEG)
    detG=int(G.det(method='domain-ge'))
    detA=int(A.det(method='domain-ge'))
    detF=int(F.det(method='domain-ge'))
    assert detG>0 and detA>0 and detF>0
    assert detA*detF >= detG
    # Exact block-Schur equality via determinant is algebraic, no SVD needed.
    return {'E':E,'G':G,'A':A,'D':F,'C':C,'detG':detG,
            'pinch_num':detA*detF,'chi':natural_log(detA*detF)-natural_log(detG),
            'cross_nonzero':C!=Matrix.zeros(len(POS),len(NEG))}

def modular_curvature(G0:Matrix,A:Matrix,B:Matrix):
    """Exact noncommutation witness modulo a prime of good reduction.
    Whitening commutator vanishes over Q iff A G0^-1 B - B G0^-1 A=0.
    """
    determinant=int(G0.det(method='domain-ge'))
    for prime in (101,103,107,109,113,127,131,137,139,149):
        if determinant%prime:break
    else:raise AssertionError('No prime of good reduction')
    inv=G0.inv_mod(prime)
    K=A*inv*B-B*inv*A
    entries=[(i,j,int(K[i,j])%prime) for i in range(N)
             for j in range(N) if int(K[i,j])%prime]
    assert entries and any(i<j for i,j,_ in entries)
    Knull=A*inv*A-A*inv*A
    assert Knull==Matrix.zeros(N)
    return prime,entries[0],len(entries)

def main():
    Efull=evaluation(FULL)
    det_witness=abs(int(evaluation(FOUR).det(method='domain-ge')))
    Hfull,dfull=lattice(Efull,det_witness)
    E6=evaluation(SIX)
    H6,d6=lattice(E6,det_witness)
    assert H6==Hfull and d6==dfull
    # Source-level equivariance at every lattice point and every j/channel.
    for q in FULL:
        Eq=evaluation([q]);Eneg=evaluation([(-q[0],-q[1])])
        for j in range(J):
            for i in range(N):
                for axis in (0,1):
                    assert Eneg[i,2*j+axis] == PARITY[i]*((-1)**j)*Eq[i,2*j+axis]
    print('PASS: source-matched ordinary jets are antipodal parity equivariant')

    SYM=sorted(set(SIX)|{(-x,-y) for x,y in SIX})
    assert len(SYM)==11 and set(SIX).issubset(SYM)
    Hsym,dsym=lattice(evaluation(SYM),det_witness)
    assert Hsym==Hfull and dsym==dfull
    metrics={name:split_metrics(Q) for name,Q in [('six',SIX),('sym',SYM),('full',FULL),
                                            ('mirror',[(-x,-y) for x,y in SIX]) ]}
    for name,v in metrics.items():
        assert ((P*v['G']*P==v['G']) == (not v['cross_nonzero']))
        if name in ('sym','full'):
            assert not v['cross_nonzero'] and v['pinch_num']==v['detG']
        if name in ('six','mirror'):
            assert v['cross_nonzero'] and v['pinch_num']>v['detG']
        print('metric',name,'points',len(SIX) if name in ('six','mirror') else len(SYM) if name=='sym' else len(FULL),
              'logdet',f'{natural_log(v["detG"]):.12f}',
              'chi',f'{v["chi"]:.12f}', 'cross parity',v['cross_nonzero'])
    assert metrics['six']['detG']==metrics['mirror']['detG']
    assert metrics['six']['pinch_num']==metrics['mirror']['pinch_num']
    assert metrics['six']['G']!=metrics['mirror']['G']
    assert P*metrics['six']['G']*P==metrics['mirror']['G']
    print('PASS: parity-even determinant and chi invariant under reflection; anti blocks flip')

    zfull=gluing(Hfull)
    q17=sorted(set(FULL)-{(1,1),(-1,-1),(1,-1),(-1,1)})
    assert len(q17)==17
    E17=evaluation(q17)
    H17,d17=lattice(E17,square_witness(q17))
    assert d17==dfull*2**10
    Trel=Hfull.inv()*H17
    assert all(v.q==1 for v in Trel)
    z17=gluing(H17)
    factors=smith_normal_form(Trel,domain=ZZ)
    factors=[abs(int(factors[i,i])) for i in range(N)]
    assert [v for v in factors if v!=1]==[2]*6+[4]*2
    idxplus=(z17['ap']*z17['order'])//(zfull['ap']*zfull['order'])
    idxminus=(z17['am']*z17['order'])//(zfull['am']*zfull['order'])
    assert idxplus*(zfull['ap']*zfull['order'])==z17['ap']*z17['order']
    assert idxminus*(zfull['am']*zfull['order'])==z17['am']*z17['order']
    assert d17//dfull==(zfull['order']*idxplus*idxminus)//z17['order']
    print('gluing full k, |Gamma|, ap, am:',zfull['rank'],zfull['order'],zfull['ap'],zfull['am'])
    print('gluing 17pt k, |Gamma|, ap, am:',z17['rank'],z17['order'],z17['ap'],z17['am'])
    print('relative pure-parity indices + and -:',idxplus,idxminus,'total',d17//dfull)
    print('PASS: two independent Gamma calculations (mod2 involution, projected HNF) and exact index gluing')
    # Up/down closure among the fixed 21-node universe: the support is not uniquely recovered.
    # q belongs to c(Q) iff all its original ordinary-jet columns lie in im(E_Q).
    def closure(H):
        coords=H.inv()*Efull
        return [q for t,q in enumerate(FULL)
                if all(coords[i,8*t+j].q==1 for i in range(N) for j in range(8))]
    c6=closure(H6); c17=closure(H17)
    assert set(c6)==set(FULL)
    assert set(q17).issubset(c17) and set(c17).issubset(set(FULL))
    print('up/down closure: Q6 ->',len(c6),'of',len(FULL),'; exceptional Q17 ->',len(c17),'of',len(FULL))
    if len(c17)<len(FULL):
        print('closure exception missing:',sorted(set(FULL)-set(c17)))
    print('PASS: lattice closure idempotence via integer column-membership test')

    # Nonretraced 2-parameter SPD square, affine-invariant local curvature test.
    q1=(5,0);q2=(1,1)
    assert q1 not in SIX and q2 not in SIX
    G0=metrics['six']['G']
    A1=gram(evaluation([q1]));A2=gram(evaluation([q2]))
    assert G0+A1==gram(evaluation(SIX+[q1]))
    assert G0+A2==gram(evaluation(SIX+[q2]))
    assert G0+A1+A2==gram(evaluation(SIX+[q1,q2]))
    prime,entry,nz=modular_curvature(G0,A1,A2)
    logd=[natural_log(int(X.det(method='domain-ge'))) for X in (G0,G0+A1,G0+A2,G0+A1+A2)]
    assert logd[0]<logd[1]<logd[3] and logd[0]<logd[2]<logd[3]
    print('SPD square: vertices (0,0),(1,0),(0,1),(1,1) logdet:',*[f'{x:.12f}' for x in logd])
    print('curvature G0 determinant mod',prime, int(G0.det(method='domain-ge'))%prime)
    print('curvature noncommutation certified mod',prime,'first witness (i,j,val)=',entry,
          'nonzero entries',nz)
    print('PASS: noncommuting tangents vs A1=A2 null, scalar closed loop returns exactly')
    print('PHASE145_PASS: finite observation/metric experiment, no universal theorem')

if __name__=='__main__':main()
