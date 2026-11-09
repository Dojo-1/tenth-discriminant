#!/usr/bin/env python3
"""Phase202 exact 28D symmetric form pencil over F7, Issue #131.

Only t=0 (Q16) and t=1 (Q25) are actual observation supports.
Other t are *formal F7 residue-weight interpolations*, not number fields.
The evaluation-rank/pairing-radical split is tracked separately.
"""
from placewise_jet_probe import jets, points, trace_gram, rank_p
from residue_count_transport import residue_counts, independent_jet


def rref(M,p):
    A=[[z%p for z in row] for row in M]
    n=len(A);m=len(A[0]);k=0;piv=[]
    for j in range(m):
        h=next((i for i in range(k,n) if A[i][j]),None)
        if h is None:continue
        A[h],A[k]=A[k],A[h]
        inv=pow(A[k][j],-1,p)
        for c in range(j,m):A[k][c]=A[k][c]*inv%p
        for i in range(n):
            if i!=k and A[i][j]:
                v=A[i][j]
                for c in range(j,m):A[i][c]=(A[i][c]-v*A[k][c])%p
        piv.append(j);k+=1
        if k==n:break
    return A,piv


def nullspace(M,p):
    a,piv=rref(M,p)
    free=[j for j in range(len(M[0])) if j not in piv]
    ret=[]
    for j in free:
        v=[0]*len(M[0]);v[j]=1
        for i,c in enumerate(piv):v[c]=(-a[i][j])%p
        ret.append(v)
    return ret


def pairing(H,v,w,p):
    return sum(v[i]*H[i][j]*w[j]
               for i in range(len(v)) for j in range(len(w)))%p


def effective_channels(D,R,S,J,active,p):
    E=[]
    for r in range(R):
        for s in range(S):
            row=[]
            for j in range(J):
                for x,y in active:
                    a,b=independent_jet(D,r,s,j,x,y,p)
                    row.extend((a,b))
            E.append(row)
    return E


def main():
    D,R,S,J,p=215,53,2,2,7
    N=R*S
    G=[]
    for rho in (16,25):
        _,_,_,A=jets(D,R,S,J,rho,p)
        G.append(trace_gram(A,D,p))
    G0,G1=G
    increment=[[(G1[i][j]-G0[i][j])%p for j in range(N)]
               for i in range(N)]
    c0=residue_counts(points(D,16),p)
    c1=residue_counts(points(D,25),p)
    assert set(c0)==set(c1) and len(c0)==21
    n=28
    results=[]
    for t in range(p):
        full=[[(G0[i][j]+t*increment[i][j])%p for j in range(N)]
              for i in range(N)]
        quotient=[row[:n] for row in full[:n]]
        r_full=rank_p(full,p);r_quot=rank_p(quotient,p)
        assert r_full==r_quot
        active=[z for z in sorted(c0)
                if ((1-t)*c0[z]+t*c1[z])%p]
        rankE=rank_p(effective_channels(D,R,S,J,active,p),p)
        assert rankE>=r_quot
        row={"t":t,"active_residue_classes":len(active),
             "effective_evaluation_rank":rankE,"Gram_rank":r_quot,
             "evaluation_kernel_dim":n-rankE,
             "pairing_radical_dim":rankE-r_quot}
        results.append(row)
        print("FORM_STRATUM",row)
    assert [d["Gram_rank"] for d in results]==[28,26,28,18,28,28,28]
    assert results[1]["pairing_radical_dim"]==2
    assert results[3]["evaluation_kernel_dim"]==10
    assert results[3]["pairing_radical_dim"]==0

    H1=[row[:n] for row in G1[:n]]
    v=nullspace(H1,p)
    assert len(v)==2
    Hdelta=[row[:n] for row in increment[:n]]
    tangent=[[pairing(Hdelta,x,y,p) for y in v] for x in v]
    assert tangent==[[0,0],[0,0]]
    print("CROSSING_FORM",{"parameter":1,
        "tangent_restricted_to_radical":tangent,
        "transverse":False,
        "radical_basis_sparse":[[(i,a) for i,a in enumerate(w) if a]
                                 for w in v]})
    print("PASS: exact 28D form pencil, two distinct degeneracy mechanisms")


if __name__=="__main__":
    main()
