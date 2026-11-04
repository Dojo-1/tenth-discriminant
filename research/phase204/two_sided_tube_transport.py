#!/usr/bin/env python3
"""Phase204-B issue #137: two-sided nilpotent tube transport, original jets."""
from ordinary_jet_filtration import jet

def modpair(z,m):return z[0]%m,z[1]%m
def arr(D,R,S,p,z):
    return {(r,s,j):jet(D,r,s,j,z) for r in range(R)
            for s in range(S) for j in range(p)}
def act(A,R,S,p,delta):
    m=p*p;B={}
    for r in range(R):
        for s in range(S):
            for j in range(p):
                x=A[(r,s,j)]
                y=A[(r,s,j+1)] if j+1<p else (0,0)
                w=A[(r,s-1,j)] if s else (0,0)
                B[(r,s,j)]=((x[0]+delta*y[0]+delta*s*w[0])%m,
                            (x[1]+delta*y[1]+delta*s*w[1])%m)
    return B
def check(p,D):
    R,S=p+2,3;m=p*p;tested=0
    for z in ((0,0),(1,0),(1,1)):
        A={k:modpair(v,m) for k,v in arr(D,R,S,p,z).items()}
        for mult in (1,2):
            d=p*mult
            shifted={k:modpair(v,m) for k,v in
                     arr(D,R,S,p,(z[0]+d,z[1])).items()}
            assert act(A,R,S,p,d)==shifted
            tested+=len(A)
        assert act(act(A,R,S,p,p),R,S,p,2*p)==act(A,R,S,p,3*p)
        assert act(A,R,S,p,m)==A
    print("TUBE_JET_TRANSPORT",{"p":p,"D":D,"modulus":m,
      "jet_depth":p,"rectangular_rows":R*S,
      "checked_source_entries":tested,
      "two_sided_row_and_jet_action":True,
      "additive_shift_group_law":True})
def main():
    check(3,7);check(5,3);check(7,215)
    # A 2-jet alone cannot transport z=0 to z=7 in Z/49.
    zero=[0,0];f=[0,0] # f(Z)=Z² shares these first jets with zero
    shifted_f=[7*7%49,2*7%49]
    assert f==zero and shifted_f==[0,14] and shifted_f!=zero
    print("NEGATIVE_J2",{"p":7,"f":"Z^2","jets_at_0":[0,0],
         "jets_at_7":shifted_f,"need_higher_jet":True})
    print("PASS bivariate original-source p-jet unipotent thickened transport")
if __name__=="__main__":main()
