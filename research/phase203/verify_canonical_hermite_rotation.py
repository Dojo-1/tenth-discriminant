#!/usr/bin/env python3
"""Phase203: constructive ordinary-jet Hermite rotation, Issues #133/#134.

Source: ordinary Z derivatives with W fixed, split order at a residue prime.
H_{p,2} is the confluent (value, first derivative) evaluation isomorphism,
U=H^-1 (direct sum of rotations) H.  No field-discriminant cutoff follows.
No equality of residue fibres across DIFFERENT characteristics is assumed.
"""
from math import prod
from check_intertwiner_f7 import U_at, matmul, det_mod


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def inverse(A,p):
    n=len(A)
    a=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        t=next((i for i in range(j,n) if a[i][j]%p),None)
        assert t is not None,"Hermite matrix singular"
        a[j],a[t]=a[t],a[j]
        v=pow(a[j][j],-1,p)
        a[j]=[v*x%p for x in a[j]]
        for i in range(n):
            if i!=j and a[i][j]:
                c=a[i][j]
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[j])]
    assert all(a[i][j]==int(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in a]


def local_hermite(p):
    n=2*p
    H=[[0]*n for _ in range(n)]
    O=[[0]*n for _ in range(n)]
    for a in range(p):
        for r in range(n):
            H[2*a][r]=pow(a,r,p)
            H[2*a+1][r]=(r*pow(a,r-1,p))%p if r else 0
        O[2*a][2*a+1]=1
        O[2*a+1][2*a]=p-1
    U=matmul(matmul(inverse(H,p),O,p),H,p)
    assert matmul(U,U,p)==[[-int(i==j)%p for j in range(n)] for i in range(n)]
    assert det_mod(U,p)==1
    return H,U


def apply_transpose(M,v,p):
    return [sum(M[i][j]*v[i] for i in range(len(v)))%p
            for j in range(len(M[0]))]


def run(p,root):
    assert 0<root<p and root*root%p!=0
    n=2*p
    H,U=local_hermite(p)
    if p==7:
        assert U==U_at(7),"prior 49-entry matrix is not canonical Hermite rotation"
    # Apply the same polynomial rotation for each s=0,1, keeping W fixed.
    C=[[0]*(2*n) for _ in range(2*n)]
    for r in range(n):
        for t in range(n):
            for s in range(2):
                C[2*r+s][2*t+s]=U[r][t]

    checked=0
    for x in range(p):
        for y in range(p):
            z,w=(x+root*y)%p,(x-root*y)%p
            for zz,ww in ((z,w),(w,z)):
                v0=[pow(zz,r,p)*pow(ww,s,p)%p
                    for r in range(n) for s in range(2)]
                v1=[(r*pow(zz,r-1,p)*pow(ww,s,p))%p if r else 0
                    for r in range(n) for s in range(2)]
                assert apply_transpose(C,v0,p)==v1
                assert apply_transpose(C,v1,p)==[(-z)%p for z in v0]
            checked+=1

    print("SPLIT_HERMITE_ROTATION",{
        "p":p,"sqrt_minus_D":root,"D_residue":(-root*root)%p,
        "source_rows":4*p,"original_jet_depth":2,
        "split_residue_pairs":checked,"Hermite_dimension":2*p,
        "det_U":1,"U_squared":"-I",
        "pointwise_ordinary_jet_rotation":True,
        "Fp2_field_from_U":p%4==3
    })


def main():
    for p,root in ((5,2),(7,3),(11,4)):
        run(p,root)
    assert (2*2)%5==(-1)%5
    assert pow(-1%7,(7-1)//2,7)==6
    assert pow(-1%11,(11-1)//2,11)==10
    # An inert node u^2=-1 at p7 has (u^7-u)^2=-4=3 !=0.
    assert (-4)%7==3
    # Ordinary j>=p differentiation is not faithfully parametrized by
    # p independent jets: p! is zero in characteristic p.
    assert prod(range(1,8))%7==0
    print("GUARDED_NEGATIVES",{
        "p5_minus_one_square_no_field_extension":True,
        "p7_p11_minus_one_nonsquare":True,
        "p7_inert_D1_Hermite_source_invalid":True,
        "higher_ordinary_derivative_factorial_guard":True
    })
    print("PASS exact split-place Hermite ordinary-jet source rotation")


if __name__=="__main__":
    main()
