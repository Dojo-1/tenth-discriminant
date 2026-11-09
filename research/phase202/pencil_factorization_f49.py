#!/usr/bin/env python3
"""Phase202 exact F49 determinant-polynomial and source-parity oracle.

Preregistered in Issue #131. Standard Python only, F49=F7[u]/(u*u+1).
Only t=0,1 of the form pencil are actual ellipse supports.
No external-minor equivalence or field-cutoff improvement.
"""
from placewise_jet_probe import jets, trace_gram

# Field encoding a+7*b, u^2=-1 (irreducible over F7).
ADD=[[0]*49 for _ in range(49)]
SUB=[[0]*49 for _ in range(49)]
MUL=[[0]*49 for _ in range(49)]
INV=[0]*49
for x in range(49):
    a,b=x%7,x//7
    for y in range(49):
        c,d=y%7,y//7
        ADD[x][y]=(a+c)%7+7*((b+d)%7)
        SUB[x][y]=(a-c)%7+7*((b-d)%7)
        MUL[x][y]=(a*c-b*d)%7+7*((a*d+b*c)%7)
    if x:
        inv=pow((a*a+b*b)%7,-1,7)
        INV[x]=(a*inv)%7+7*((-b*inv)%7)
assert all(MUL[x][INV[x]]==1 for x in range(1,49))


def determinant_at(H0,delta,t):
    n=len(H0)
    A=[[ADD[H0[i][j]][MUL[t][delta[i][j]]] for j in range(n)]
       for i in range(n)]
    det=1
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:
            A[k],A[pivot]=A[pivot],A[k]
            det=SUB[0][det]
        c=A[k][k]
        det=MUL[det][c]
        inv=INV[c]
        for i in range(k+1,n):
            factor=MUL[A[i][k]][inv]
            if factor:
                for j in range(k+1,n):
                    A[i][j]=SUB[A[i][j]][MUL[factor][A[k][j]]]
            A[i][k]=0
    return det


def eval_poly(c,t):
    y=0
    for a in reversed(c):y=ADD[MUL[y][t]][a]
    return y


def interpolate(xs,ys):
    n=len(xs)
    dd=ys[:]
    for order in range(1,n):
        for i in range(n-1,order-1,-1):
            dd[i]=MUL[SUB[dd[i]][dd[i-1]]][INV[SUB[xs[i]][xs[i-order]]]]
    poly=[0]
    for i in range(n-1,-1,-1):
        new=[0]*(len(poly)+1)
        for j,a in enumerate(poly):
            new[j]=ADD[new[j]][MUL[a][SUB[0][xs[i]]]]
            new[j+1]=ADD[new[j+1]][a]
        new[0]=ADD[new[0]][dd[i]]
        poly=new
    while len(poly)>1 and poly[-1]==0:poly.pop()
    return poly


def poly_matdet(B0,B1):
    n=len(B0)
    diff=[[(B1[i][j]-B0[i][j])%7 for j in range(n)] for i in range(n)]
    nodes=list(range(n+1))
    vals=[determinant_at(B0,diff,z) for z in nodes]
    coeff=interpolate(nodes,vals)
    assert len(coeff)<=n+1 and all(z<7 for z in coeff)
    assert all(eval_poly(coeff,z)==determinant_at(B0,diff,z)
               for z in range(n+1,49)), "F49 unused-node failure"
    return coeff


def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%7
    return out


def poly_pow(a,n):
    q=[1]
    for _ in range(n):q=poly_mul(q,a)
    return q


def main():
    D,R,S,J,p=215,53,2,2,7
    Grams=[];source=None
    for rho in (16,25):
        Q,rows,cols,A=jets(D,R,S,J,rho,p)
        G=trace_gram(A[:28],D,p)
        Grams.append(G)
        if rho==16:source=(Q,rows,cols,A)
    G0,G1=Grams
    even=[i for i in range(28) if sum(divmod(i,2))%2==0]
    odd=[i for i in range(28) if sum(divmod(i,2))%2==1]
    assert len(even)==len(odd)==14
    assert all(G[i][j]==0 for G in Grams for i in even for j in odd)
    def block(G,idx):return [[G[i][j] for j in idx] for i in idx]
    pe=poly_matdet(block(G0,even),block(G1,even))
    po=poly_matdet(block(G0,odd),block(G1,odd))
    P=poly_matdet(G0,G1)
    assert pe==po and poly_mul(pe,po)==P
    cubic1=[-2%7,3,0,1]
    cubic2=[2,-2%7,0,1]
    expected=poly_mul([2],poly_mul(
        poly_pow([-1%7,1],4),poly_mul(
        poly_pow([-3%7,1],12),poly_mul(
        poly_pow(cubic1,2),poly_pow(cubic2,2)))))
    assert P==expected
    candidate=poly_mul([3],poly_mul(
        poly_pow([-1%7,1],2),poly_mul(
        poly_pow([-3%7,1],6),poly_mul(cubic1,cubic2))))
    assert pe==candidate or pe==[(-x)%7 for x in candidate]
    Q,rows,cols,A=source
    removed={i for i,(j,x,y) in enumerate(cols) if (x,y)==(1,0)}
    assert len(removed)==J
    Aminus=[[v for i,v in enumerate(row) if i not in removed] for row in A[:28]]
    Gminus=trace_gram(Aminus,D,p)
    assert any(Gminus[i][j] for i in even for j in odd)
    print("EXACT_FACTOR",{"degree":len(P)-1,"factorization":
        "2*(t-1)^4*(t-3)^12*(t^3+3t-2)^2*(t^3-2t+2)^2",
        "coefficients_low_to_high":P,
        "parity_14d_block_polynomials_equal":True,
        "source_broken_parity_negative":True,
        "unused_field_nodes_verified":True})
    print("PASS F49 determinant polynomial, parity blocks and negative controls")


if __name__=="__main__":main()
