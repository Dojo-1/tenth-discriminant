#!/usr/bin/env python3
"""Phase207-A (#146): predeclared full-matching generalized Schur modes.

Exact Fraction inertia; every original Q and ordinary j<J. NO float eigensolver.
Finite D283 and D403 examples, no class-number-one assumption.
"""
from fractions import Fraction as Q
from source_probe import params, fibers, gram, det, inv, mm, tr
from rational_schur_modes import det_fraction

def inertia(M):
    """Exact symmetric-congruence inertia; handles zero diagonal pivots."""
    A=[[Q(x) for x in row] for row in M]
    nneg=nzero=npos=0
    while A:
        n=len(A)
        i=next((i for i in range(n) if A[i][i]!=0),None)
        if i is not None:
            A[0],A[i]=A[i],A[0]
            for row in A: row[0],row[i]=row[i],row[0]
            a=A[0][0]
            if a>0:npos+=1
            else:nneg+=1
            A=[[A[r][s]-A[r][0]*A[0][s]/a for s in range(1,n)]
               for r in range(1,n)]
        else:
            pair=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
            if pair is None:
                nzero+=n;break
            i,j=pair
            P=[i,j]+[r for r in range(n) if r not in (i,j)]
            A=[[A[r][s] for s in P] for r in P]
            a=A[0][1];npos+=1;nneg+=1
            A=[[A[r][s]-(A[r][0]*A[1][s]+A[r][1]*A[0][s])/a
                for s in range(2,n)] for r in range(2,n)]
    assert nneg+nzero+npos==len(M)
    return nneg,nzero,npos

def block(G,k):
    return [row[:k] for row in G[:k]],[row[k:] for row in G[k:]],[row[k:] for row in G[:k]]

def pencil(A,B,C,t):
    Z=mm(mm(tr(C),inv(A)),C)
    S=[[Q(B[i][j])-Z[i][j] for j in range(len(B))] for i in range(len(B))]
    T=[[S[i][j]-t*B[i][j] for j in range(len(B))] for i in range(len(B))]
    return S,T

def theta_spec(R):
    return [("1/2",Q(1,2)),("1/8",Q(1,8)),("1/64",Q(1,64)),
            ("1/1024",Q(1,1024)),
            ("2^-ceil(R/10)",Q(1,2**((R+9)//10))),
            ("2^-ceil(R/4)",Q(1,2**((R+3)//4)))]

def run(D):
    rho,R,S,J,points=params(D)
    ds=list(range(1-S,R))
    groups=[[d for d in ds if d%2==h] for h in (0,1)]
    matching=[(q[k],q[k+1]) for q in groups for k in range(0,len(q)-1,2)]
    assert len(matching)==(35 if D==283 else 51)
    thresholds=theta_spec(R)
    counts={label:0 for label,_ in thresholds}
    modes=0;positive_pairs=0;shear_checked=False;regression={}
    for d,e in matching:
        I=fibers(R,S,d);K=fibers(R,S,e);a,b=len(I),len(K)
        assert a and b and e==d+2
        G=gram(D,points,J,I+K)
        A,B,C=block(G,a)
        da,db,dj=det(A),det(B),det(G)
        assert 0<dj<=da*db
        S0,T=pencil(A,B,C,Q(1,2))
        assert all(S0[i][j]==S0[j][i] for i in range(b) for j in range(b))
        # Positive definiteness; lower Schur determinant equals exact ratio.
        assert det_fraction(S0)>0
        assert det_fraction(S0)/db==Q(dj,da*db)
        assert inertia(S0)==(0,0,b)
        this={}
        for label,t in thresholds:
            X=[[S0[i][j]-t*B[i][j] for j in range(b)] for i in range(b)]
            neg,zero,pos=inertia(X)
            assert zero==0, ("registered threshold is exact eigenvalue",D,d,e,label)
            counts[label]+=neg
            this[label]=neg
        order=sorted([(v,label) for label,v in thresholds])
        assert all(this[order[k][1]]<=this[order[k+1][1]]
                   for k in range(len(order)-1))
        if dj<da*db:positive_pairs+=1
        modes+=b
        # Fixed deterministic gauge: first matching pair with B dim >=2.
        if not shear_checked and b>=2:
            U=[[Q(int(i==j)+(1 if i==0 and j==1 else 0)) for j in range(b)]
               for i in range(b)]
            Sg=mm(mm(U,S0),tr(U));Bg=mm(mm(U,B),tr(U))
            for label,t in thresholds:
                original=[[S0[i][j]-t*B[i][j] for j in range(b)] for i in range(b)]
                moved=[[Sg[i][j]-t*Bg[i][j] for j in range(b)] for i in range(b)]
                assert inertia(original)==inertia(moved)
            shear_checked=True
    assert shear_checked and positive_pairs>0
    old=(R//4-1,R//2-1,R-S-7)
    for d in old:
        I=fibers(R,S,d);K=fibers(R,S,d+2)
        G=gram(D,points,J,I+K)
        A,B,C=block(G,len(I))
        S0,_=pencil(A,B,C,Q(1,2))
        regression[d]=[inertia([[S0[i][j]-t*B[i][j] for j in range(len(B))]
                       for i in range(len(B))])[0] for t in (Q(1,2),Q(1,4),Q(1,8))]
    targets=([0,0,0] if D==283 else None)
    if D==283:assert all(x==targets for x in regression.values())
    if D==403:assert [sum(regression[d][k] for d in old) for k in range(3)]==[5,3,2]
    # Opposite parity: original reflection-orthogonal cross-moments.
    I=fibers(R,S,ds[0]);K=fibers(R,S,ds[0]+1)
    X=gram(D,points,J,I+K)
    assert all(X[i][len(I)+j]==0 for i in range(len(I)) for j in range(len(K)))
    assert gram(D,points,J,fibers(R,S,old[0])+fibers(R,S,old[0]+2))!=gram(D,points,J-1,fibers(R,S,old[0])+fibers(R,S,old[0]+2))
    print("PHASE207_DEEP_SCHUR",{"D":D,"R":R,"S":S,"rho":rho,"Q":len(points),
         "pairs":len(matching),"modes":modes,"pairs_with_coupling":positive_pairs,
         "counts":counts,"fractions_of_rows":{k:float(Q(v,R*S)) for k,v in counts.items()},
         "source_shear_invariant":shear_checked,"legacy_3pair_regression":regression},flush=True)

if __name__=="__main__":
    run(283)
    run(403)
    print("PASS Phase207 exact full matching Schur mode audit, no uniform theorem",flush=True)
