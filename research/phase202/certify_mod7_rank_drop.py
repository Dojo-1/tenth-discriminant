#!/usr/bin/env python3
"""Post-discovery *preregistered replication* of a Phase202 rank phenomenon.

See Issue #131. The initial p=7 observation was exploratory/post hoc.
This verifies exact witnesses and negative controls; it claims no new
discriminant bound and does not identify different Gram matrices.
"""
from placewise_jet_probe import jets, channels, trace_gram, rank_p


def rref(M, p):
    A=[[v%p for v in row] for row in M]
    if not A: return A,[]
    n,m=len(A),len(A[0])
    k=0; piv=[]
    for j in range(m):
        t=next((i for i in range(k,n) if A[i][j]),None)
        if t is None: continue
        A[t],A[k]=A[k],A[t]
        inv=pow(A[k][j],-1,p)
        for h in range(j,m):A[k][h]=A[k][h]*inv%p
        for i in range(n):
            if i!=k and A[i][j]:
                c=A[i][j]
                for h in range(j,m):A[i][h]=(A[i][h]-c*A[k][h])%p
        piv.append(j);k+=1
        if k==n:break
    return A,piv


def nullspace(M,p):
    A,piv=rref(M,p)
    free=[j for j in range(len(M[0])) if j not in set(piv)]
    out=[]
    for j in free:
        v=[0]*len(M[0]);v[j]=1
        for i,c in enumerate(piv):v[c]=(-A[i][j])%p
        out.append(v)
    return out


def det_mod(M,p):
    A=[[z%p for z in row] for row in M]
    n=len(A); det=1
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        assert k is not None
        if j!=k:A[j],A[k]=A[k],A[j];det=-det
        v=A[j][j];det=det*v%p
        inv=pow(v,-1,p)
        for i in range(j+1,n):
            c=A[i][j]*inv%p
            for h in range(j,n):A[i][h]=(A[i][h]-c*A[j][h])%p
    return det%p


def image(E,v,p):
    return [sum(E[i][j]*v[i] for i in range(len(v)))%p
            for j in range(len(E[0]))]


def sparse_vector(n,values):
    v=[0]*n
    for i,x in values:v[i]=x
    return v


def check(rho,expected_count,expected_G_rank,minor_indices,expected_det):
    D,R,S,J,p=215,53,2,2,7
    Q,rows,cols,A=jets(D,R,S,J,rho,p)
    assert len(Q)==expected_count
    assert 2*D%p==3  # Trace channel weights are 2,3: both nonzero.
    E=channels(A);G=trace_gram(A,D,p)
    rank_E=rank_p(E,p)
    assert rank_E==28
    _,pcols=rref(G,p)
    rank_G=len(pcols)
    assert rank_G==expected_G_rank
    assert len(minor_indices)==rank_G
    principal=[[G[i][j] for j in minor_indices] for i in minor_indices]
    assert det_mod(principal,p)==expected_det

    # Upper rank bound through independently verifiable full nullspace basis.
    basis=nullspace(G,p)
    assert len(basis)==R*S-rank_G
    assert rank_p(basis,p)==len(basis)
    assert all(all(sum(x*y for x,y in zip(row,v))%p==0 for row in G)
               for v in basis)
    images=[image(E,v,p) for v in basis]
    assert rank_p(images,p)==rank_E-rank_G
    print('CERT',{'D':D,'p':p,'rho':rho,'points':len(Q),'N':R*S,
          'rank_E':rank_E,'rank_G':rank_G,
          'radical_dim':rank_E-rank_G,'principal_minor_size':rank_G,
          'principal_minor_det_mod7':expected_det,
          'nullspace_dimension':len(basis)})

    if rho==25:
        # Two compact *source-row* vectors in ker G but not ker E^T.
        v1=sparse_vector(R*S,[(4,3),(7,3),(8,2),(12,5),(15,5),
                               (16,1),(19,6),(20,2),(24,1)])
        v2=sparse_vector(R*S,[(5,5),(6,4),(9,2),(10,4),(14,6),
                               (17,2),(18,3),(21,5),(22,3),(26,1)])
        assert all(all(sum(x*y for x,y in zip(row,v))%p==0 for row in G)
                   for v in (v1,v2))
        assert rank_p([image(E,v1,p),image(E,v2,p)],p)==2
        print('WITNESS',{'rho':rho,'radical_vectors_sparse':[
            [(i,x) for i,x in enumerate(v) if x] for v in (v1,v2)]})
    return E,G


if __name__=='__main__':
    E16,G16=check(16,59,28,list(range(28)),4)
    E25,G25=check(25,133,26,list(range(24))+[25,27],2)
    assert len(E16[0])<len(E25[0])
    # p=11 is the declared comparison; neither restricted pairing degenerates.
    for rho in (16,25):
        _,_,_,A=jets(215,53,2,2,rho,11)
        E=channels(A);G=trace_gram(A,215,11)
        assert rank_p(E,11)==rank_p(G,11)==44
    print('PASS: p=7 exact rank reversal, nonzero minors, full nullspaces, '
          'two explicit radical vectors, p=11 control')
