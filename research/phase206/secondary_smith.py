#!/usr/bin/env python3
"""Phase206-B prereg #143: SECONDARY p-adic Smith at EXACT precision K=6.

Keeps ROW operations V (p-unit); never applies Smith COLUMN transforms
to the original trace metric. Truncation at 6 stays explicitly unresolved.
"""
from collections import Counter
from source_probe import params, eval_mod, old_frobenius_C0, rank_mod, gram_mod

def capped_val(x,p,K):
    if x==0:return K
    v=0
    while x%p==0:v+=1;x//=p
    return v

def smith_with_row_map(C,p,K=6):
    M=p**K;n=len(C);m=len(C[0])
    A=[[x%M for x in row] for row in C]
    V=[[int(i==j) for j in range(n)] for i in range(n)]
    levels=[]
    for k in range(n):
        best=(K,None,None)
        for i in range(k,n):
            for j in range(k,m):
                if A[i][j]:
                    v=capped_val(A[i][j],p,K)
                    if v<best[0]:best=(v,i,j)
                if best[0]==0:break
            if best[0]==0:break
        v,i,j=best
        if v==K:
            levels.extend([K]*(n-k));break
        A[k],A[i]=A[i],A[k];V[k],V[i]=V[i],V[k]
        for row in A:row[k],row[j]=row[j],row[k]
        factor=p**v;mod=M//factor
        pivot=A[k][k]
        assert pivot%factor==0
        inverse=pow(pivot//factor,-1,mod)
        for i in range(k+1,n):
            if A[i][k]:
                assert A[i][k]%factor==0
                t=(A[i][k]//factor)*inverse%mod
                A[i]=[(a-t*b)%M for a,b in zip(A[i],A[k])]
                V[i]=[(a-t*b)%M for a,b in zip(V[i],V[k])]
        for j in range(k+1,m):
            if A[k][j]:
                assert A[k][j]%factor==0
                t=(A[k][j]//factor)*inverse%mod
                for i in range(n):A[i][j]=(A[i][j]-t*A[i][k])%M
        levels.append(v)
    assert len(levels)==n and rank_mod(V,p)==n
    if K in levels:return levels,None
    # Reconstruct the original-source normalized rows from V*C,
    # NOT from column-diagonalized A=V*C*W.
    C1=[]
    for i,v in enumerate(levels):
        factor=p**v;row=[]
        for j in range(m):
            z=sum(V[i][r]*C[r][j] for r in range(n))%M
            assert z%factor==0
            row.append(z//factor%p)
        C1.append(row)
    assert rank_mod(C1,p)==n
    return levels,C1

def run(p):
    D=283;rho,R,S,J,Q=params(D);K=6
    assert (rho,R,S,J,len(Q))==(31,70,2,2,169)
    assert (-D)%p not in {x*x%p for x in range(p)}
    E=eval_mod(D,Q,R,S,J,p,K+1)
    C0=old_frobenius_C0(E,R,S,p,K+1)
    levels,C1=smith_with_row_map(C0,p,K)
    hist=dict(sorted(Counter(levels).items()))
    idx=sum(levels)
    result=dict(D=D,p=p,R=R,S=S,J=J,K=K,old_Fp=R-p,
                old_2Fp=2*(R-p),second_levels=hist,
                second_index_lower=idx,fully_primitive=C1 is not None)
    if C1 is None:
        result['new_exponent_lower']=2*idx
        result['total_vp_lower']=2*(R-p)+2*idx
        result['unresolved_level_6_count']=hist.get(K,0)
    else:
        H=gram_mod(C1,D,p)
        h_rank=rank_mod(H,p)
        result['primitive_H_rank_modp']=h_rank
        result['primitive_H_nullity']=R*S-h_rank
        result['new_exponent_lower']=2*idx+R*S-h_rank
        result['total_vp_lower']=2*(R-p)+result['new_exponent_lower']
        if h_rank==R*S:
            result['vp_det_exact']=result['total_vp_lower']
    print('SECONDARY_SMITH',result,flush=True)
    if p==3:
        assert hist=={0:36,1:9,2:9,4:36,5:9,6:41}
        assert result['total_vp_lower']==1058 and C1 is None
    if p==5:
        assert hist=={0:60,1:15,2:30,3:20,4:15}
        assert C1 is not None and result['vp_det_exact']==520

if __name__=='__main__':
    run(3)
    run(5)
    print('PASS Phase206 second-stage Smith with explicit original-source row map')
