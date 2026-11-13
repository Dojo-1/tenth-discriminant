#!/usr/bin/env python3
"""Phase309-B: original trace Gram as pairing of conjugate split embeddings.

No arbitrary scalar Gram replacement: the exact parent original Hermitian
trace pairing is checked as a cross-pairing of two different residue worlds.
This is finite field arithmetic, NOT quantum entanglement or a field bound.
"""
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase309"))
import original_source_picard as source
import picard_tendrils as ideals


def embedding_r(x, root, p):
    a,b=x
    return (a+b*root)%p


def split_embeddings(D,p,r):
    ps,q=source.patch_source(D,p,r)
    r2=(1-r)%p
    m=ideals.order_parameter(D)
    assert (r2*r2-r2+m)%p==0
    if r2==r:
        raise ValueError("not a simple split prime, embeddings coincide")
    return (r%p,r2),ps


def mod_rank(A,p):
    """Independent finite-field row reduction with no numpy dependency."""
    rows=[list(map(lambda x:int(x)%p,row)) for row in A]
    k=0
    for c in range(len(rows[0])):
        pivot=next((i for i in range(k,len(rows)) if rows[i][c]),None)
        if pivot is None:
            continue
        rows[k],rows[pivot]=rows[pivot],rows[k]
        inv=pow(rows[k][c],-1,p)
        rows[k]=[v*inv%p for v in rows[k]]
        for i in range(len(rows)):
            if i==k:
                continue
            factor=rows[i][c]
            rows[i]=[(a-factor*b)%p for a,b in zip(rows[i],rows[k])]
        k+=1
        if k==len(rows):
            break
    return k


def residue_eval(A,r,p):
    return tuple(tuple(embedding_r(x,r,p) for x in row) for row in A)


def cross_trace_gram(X,Y,p):
    """X^T Y + Y^T X, with X,Y observation×source matrices."""
    assert len(X)==len(Y) and len(X[0])==len(Y[0])
    cols=len(X[0])
    return tuple(tuple(sum(X[k][i]*Y[k][j]+Y[k][i]*X[k][j]
                           for k in range(len(X)))%p
                       for j in range(cols)) for i in range(cols))


def same_embedding_fallacy(X,Y,p):
    """Deliberately wrong: conjugation omitted, so pair same components."""
    cols=len(X[0])
    return tuple(tuple(sum(X[k][i]*X[k][j]+Y[k][i]*Y[k][j]
                           for k in range(len(X)))%p
                       for j in range(cols)) for i in range(cols))


def independent_bilinear_pair_controls(D,p,r,r2):
    """Check original trace identity on 7^4 O-pairs, not only the patch."""
    m=ideals.order_parameter(D)
    n=0
    for a in range(-3,4):
      for b in range(-3,4):
       for c in range(-3,4):
        for d in range(-3,4):
         x,y=(a,b),(c,d)
         # Source's original symmetric Hermitian trace in omega coords.
         original=(2*a*c+a*d+b*c+2*m*b*d)%p
         cross=(embedding_r(x,r,p)*embedding_r(y,r2,p)
                +embedding_r(x,r2,p)*embedding_r(y,r,p))%p
         assert original==cross,(D,p,r,x,y)
         n+=1
    return n


def certify(D,p,r,expected_gram,expected_det):
    (r1,r2),ps=split_embeddings(D,p,r)
    A=source.exact_patch_matrix(ps)
    X=residue_eval(A,r1,p)
    Y=residue_eval(A,r2,p)
    assert X==((1,0),(1,0),(1,0))
    delta=(1-2*r)%p
    assert delta!=0
    assert Y==((1,0),(1,0),(1,delta))
    rk=(mod_rank(X,p),mod_rank(Y,p))
    assert rk==(1,2)
    G=source.original_integer_trace_gram(ps)
    assert G==expected_gram
    gram_cross=cross_trace_gram(X,Y,p)
    assert gram_cross==tuple(tuple(v%p for v in row) for row in G)
    assert gram_cross==((6%p,delta),(delta,0))
    det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
    assert det==expected_det and det%p==(-(delta**2))%p
    assert det%p!=0
    wrong=same_embedding_fallacy(X,Y,p)
    assert wrong != gram_cross
    pair_count=independent_bilinear_pair_controls(D,p,r1,r2)
    assert pair_count==7**4
    return {
       "D":D,"p":p,"split_embeddings_roots":[r1,r2],
       "rank_first_embedding":rk[0],
       "rank_second_embedding":rk[1],
       "original_trace_cross_gram_mod_p":gram_cross,
       "original_det_mod_p":det%p,
       "same_side_dot_pairing_is_wrong":True,
       "all_hermitian_trace_pairs_compared":pair_count,
       "Picard_obstruction_Does_NOT_imply_p_Gram_mass":True,
       "true_global_field_bound_NOT_updated":True,
    }


def main():
    cases=((203,3,0,((6,7),(7,120)),671),
           (187,7,2,((6,11),(11,196)),1055),
           (167,2,0,((6,5),(5,92)),527))
    out=[certify(*case) for case in cases]
    try:
        split_embeddings(203,5,0)
        raise AssertionError("inert prime was accepted as split")
    except ValueError:
        pass
    print("PHASE309_SPLIT_EMBEDDING_CROSS_PAIRING_PASS",{
        "patches":out,
        "inert_p5_false_split_rejected":True,
        "not_physical_entanglement":True,
        "not_full_original_field_bound":True
    },flush=True)


if __name__=="__main__":
    main()
