#!/usr/bin/env python3
"""Independent finite Smith/Cauchy-Binet and active-weight trap controls.

Uses SymPy's integer Smith normal form; not the histogram implementation.
The first toy expectation v3(det Gram)=12 failed locally: actual=13,
showing primitive-pairing depth beyond the squared evaluation index.
This correction is preserved in Phase387 research notes.
"""
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def vp(n,p=3):
    n=abs(int(n));assert n>0
    a=0
    while n%p==0:n//=p;a+=1
    return a

def smith_exponents(F):
    diag=smith_normal_form(F,domain=ZZ)
    assert all(diag[i,i]!=0 for i in range(F.rows))
    return sorted(vp(diag[i,i]) for i in range(F.rows))

def smith_and_frames():
    basis=[Matrix([int(i==k) for i in range(5)]) for k in range(5)]
    e=basis
    F=Matrix.hstack(
        e[0],e[1],e[0]+9*e[2],e[1]+9*e[3],e[0]+9*e[4],
        e[0]+27*e[2],e[1]+27*e[3],e[0]+27*e[4],
        e[0]+81*e[2],e[1]+81*e[3])
    exps=smith_exponents(F)
    assert exps==[0,0,2,2,2],exps
    for depth in range(1,5):
        distinct=len({tuple(int(F[i,j])%3**depth for i in range(F.rows))
                      for j in range(F.cols)})
        visible=sum(a<depth for a in exps)
        assert visible<=distinct,(depth,visible,distinct)
    B=Matrix.diag(*([2]*F.cols))
    H=F*B*F.T
    v=vp(H.det())
    # This is >=2*sum exponents, NOT necessarily equal:
    # here a further primitive trace-pairing factor occurs.
    assert v==13 and 2*sum(exps)==12
    U=Matrix.eye(5);U[3,1]=4;U[4,0]=-7
    assert U.det()==1
    assert smith_exponents(U*F)==exps
    assert vp((U*H*U.T).det())==v
    Pm=Matrix.zeros(10,10)
    for i in range(10):Pm[i,(i*3)%10]=1
    assert abs(int(Pm.det()))==1
    assert smith_exponents(F*Pm)==exps
    assert (F*Pm)*(Pm.T*B*Pm)*(F*Pm).T==H
    print("PASS Smith layers, squared evaluation index and frame/permutation invariance")
    print("PRESERVED CORRECTION: Gram v3=13; squared evaluation index=12")

def reject_gram_active_count_for_evaluation():
    # Three duplicate e0 columns cancel in Gram modulo 3 but still
    # generate the e0 direction in the evaluation matrix. 'Active'
    # histogram weights are valid for H, not for generator counts of F.
    F=Matrix([[1,1,1,0],[0,0,0,1]])
    H=F*F.T
    assert H==Matrix.diag(3,1)
    assert F.rank()==2
    assert int(H[0,0])%3==0
    assert len({tuple(F[i,j] for i in range(2)) for j in range(4)})==2
    print("PASS active histogram weights cannot replace occupied source classes in F")

if __name__=="__main__":
    smith_and_frames()
    reject_gram_active_count_for_evaluation()
