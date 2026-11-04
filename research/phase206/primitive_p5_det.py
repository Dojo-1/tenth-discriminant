#!/usr/bin/env python3
"""Phase206-B independent modular determinant of fully primitive p5 Gram.

Preregistered Issue #143; row-reduction determinant is distinct from the
existing incremental-rank witness. Not an external/human verification.
"""
from source_probe import params,eval_mod,old_frobenius_C0,gram_mod,rank_mod
from secondary_smith import smith_with_row_map

def determinant_mod(A,p):
    A=[[x%p for x in row] for row in A];n=len(A);z=1
    for k in range(n):
        i=next((i for i in range(k,n) if A[i][k]),None)
        if i is None:return 0
        if i!=k:A[i],A[k]=A[k],A[i];z=-z
        pivot=A[k][k];z=z*pivot%p
        q=pow(pivot,-1,p)
        for i in range(k+1,n):
            t=A[i][k]*q%p
            if t:
                for j in range(k+1,n):A[i][j]=(A[i][j]-t*A[k][j])%p
                A[i][k]=0
    return z%p

def run():
    D,p,K=283,5,6
    rho,R,S,J,Q=params(D)
    C0=old_frobenius_C0(eval_mod(D,Q,R,S,J,p,K+1),R,S,p,K+1)
    levels,C1=smith_with_row_map(C0,p,K)
    assert C1 is not None and sum(levels)==195
    H=gram_mod(C1,D,p);v=determinant_mod(H,p)
    assert v==3 and rank_mod(H,p)==R*S
    # Simultaneous permutation preserves determinant of a congruence.
    P=[row[:] for row in H]
    i,j=0,R*S-1
    P[i],P[j]=P[j],P[i]
    for row in P:row[i],row[j]=row[j],row[i]
    assert determinant_mod(P,p)==v
    print('INDEPENDENT_MOD5_DET',{'D':D,'p':p,'detH1_mod5':v,
       'rank':R*S,'secondary_index':sum(levels),'exact_v5_original_Gram':
       2*(R-p)+2*sum(levels),'congruence_permutation_invariant':True},flush=True)

if __name__=='__main__':
    run()
    print('PASS p5 exact source residual unit verified by determinant')
