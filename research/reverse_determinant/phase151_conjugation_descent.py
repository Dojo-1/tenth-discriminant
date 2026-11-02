#!/usr/bin/env python3
"""Phase151: exact conjugation-local-system descent for ORIGINAL ordinary Z jets.

Depends on source-matched Phase144 + Phase147 evaluators. Paper proof in
PHASE151_CONJUGATION_WORLDLET.md. No new field bound or quantum claim.
"""
from math import log, prod
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from phase144_verifier import D,R,S,J,FULL,evaluation
from phase147_prime_adequacy import original_eval, qellipse, dabs

N=R*S
assert (D,R,S,J,N)==(19,8,4,4,32)


def orbit_reps(Q):
    X=set(Q)
    assert all((x,-y) in X and (-x,-y) in X for x,y in X)
    return sorted(q for q in X if q[1]>=0)


def gram(E,d):
    return E*Matrix.diag(*([2,2*d]*(E.cols//2)))*E.T


def weighted(reps,d):
    return sum(((1 if y==0 else 2)*gram(original_eval([(x,y)],d),d)
                for x,y in reps),Matrix.zeros(N))


def quotient_smith(Hbig,Hsmall):
    T=Hbig.inv()*Hsmall
    assert all(v.q==1 for v in T)
    S=smith_normal_form(T,domain=ZZ)
    return [abs(int(S[i,i])) for i in range(N) if abs(int(S[i,i]))>1]


def main():
    assert len(FULL)==21 and original_eval(FULL,D)==evaluation(FULL)
    P=Matrix.diag(*[(-1)**(i//S+i%S) for i in range(N)])
    nodes=[(x,0) for x in range(-4,4)]
    ER=original_eval(nodes,D)
    minor=ER[:,[8*t+2*j for t in range(R) for j in range(J)]]
    modulus=dabs(minor)
    assert modulus>0
    print('PASS: original Phase140/144 jets entrywise matched to Phase147 D19',flush=True)
    for d in (17,19,21,23,43):
        Q=qellipse(d);rep=orbit_reps(Q)
        E=original_eval(Q,d);F=original_eval(rep,d)
        for x,y in Q:
            C=original_eval([(x,-y)],d)
            A=original_eval([(-x,-y)],d)
            V=original_eval([(x,y)],d)
            for j in range(J):
                assert C[:,2*j]==V[:,2*j] and C[:,2*j+1]==-V[:,2*j+1]
                for axis in range(2):
                    assert A[:,2*j+axis]==((-1)**j)*P*V[:,2*j+axis]
        G=gram(E,d);U=gram(F,d);H=G-U
        assert G==weighted(rep,d)
        assert H==sum((gram(original_eval([q],d),d)
                       for q in rep if q[1]>0),Matrix.zeros(N))
        assert G==U+H and P*G*P==G and P*U*P==U
        g=dabs(G);u=dabs(U)
        assert g>=u>0 and g<=2**N*u
        if any(y for _,y in rep):assert g>u
        else:assert G==U
        a=hermite_normal_form(E,D=modulus)
        b=hermite_normal_form(F,D=modulus)
        assert a==b and a.shape==(N,N)
        # Holoportation: oriented representative columns reconstruct E exactly.
        locate={q:i for i,q in enumerate(rep)}
        back=Matrix.zeros(N,len(Q)*2*J)
        for t,(x,y) in enumerate(Q):
            i=locate[(x,abs(y))]
            for j in range(J):
                back[:,2*J*t+2*j]=F[:,2*J*i+2*j]
                back[:,2*J*t+2*j+1]=(1 if y>=0 else -1)*F[:,2*J*i+2*j+1]
        assert back==E
        # Integer Fourier sum/difference produces 2*nonreal columns and
        # is NOT an integral equivalence: negative matched control.
        FFour=F.copy()
        for i,(_,y) in enumerate(rep):
            if y:
                for k in range(2*J):
                    FFour[:,2*J*i+k]=2*F[:,2*J*i+k]
        h=hermite_normal_form(FFour,D=modulus)
        factors=quotient_smith(b,h)
        assert all(v==2 for v in factors) or not factors
        assert prod(factors)==dabs(h)//dabs(b)
        assert (d==43)==(len(factors)==0)
        # Hadamard is an independent inverse-free upper for these same Grams.
        dg=log(g)-log(u)
        dh=sum(log(int(G[k,k]))-log(int(U[k,k])) for k in range(N))
        rankH=H.rank()
        assert 0<=dg<=rankH*log(2)+1e-9
        assert 0<=dh<=N*log(2)+1e-9
        print('D',d,'points',len(Q),'orbits',len(rep),'Hrank',rankH,
              'delta_logdet',f'{dg:.12f}','delta_hadamard',f'{dh:.12f}',
              'Fourier_nonunit_index',dabs(h)//dabs(b),flush=True)
    # Smallest antipodal counterworld: in rows 1,Z, points x=+1,-1.
    anti=Matrix([[1,1],[1,-1]])
    assert anti.rank()==2 and anti[:,[0]].rank()==1
    print('PHASE151_PASS: exact C2 sheaf/orbit descent, p-local image, weighted SPD, reversible holoportation, nonunitary 2-primary and antipodal null',flush=True)


if __name__=='__main__':main()
