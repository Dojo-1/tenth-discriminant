#!/usr/bin/env python3
"""Phase310: whole ORIGINAL D203 source under conjugate split-prime mirrors.

Full 100x1052 original O-coordinate evaluation at p=3, Q263 genuine points,
both ordinary Z-jets, and original integer Hermitian trace Gram. The two
residue-field views are not two independent vector worlds: on a conjugation-
closed source they differ by an exact observation permutation.

This is source arithmetic, not a quantum effect, Picard-class equivalence, or
a stronger class-number-one discriminant cutoff.
"""
from collections import Counter
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for dirname in ("phase304","phase307","phase308"):
    sys.path.insert(0, str(ROOT/"research"/dirname))
import highjet_d203_original as original
from source_saturation import independent_original_jets

D,P,K=203,3,3
MOD=P**K
R,S,J=50,2,2


def original_q():
    original.guard()
    rho, R0, S0, J0, _=original.params(D)
    assert (rho,R0,S0,J0)==(24,R,S,J)
    q=tuple(original.qmax(rho))
    assert len(q)==263
    return q


def conjugation_permutation(q):
    """Genuine integer-ring conjugation tau(a,b)=(a+b,-b)."""
    index={z:i for i,z in enumerate(q)}
    if len(index)!=len(q):
        raise ValueError("duplicate original observation")
    ids=[]
    for a,b in q:
        conjugate=(a+b,-b)
        if conjugate not in index:
            raise ValueError("observation subset is not conjugation-invariant")
        ids.append(index[conjugate])
    assert all(ids[ids[i]]==i for i in range(len(q)))
    return tuple(ids)


def split_roots(d,p):
    m=(d+1)//4
    roots=tuple(r for r in range(p) if (r*r-r+m)%p==0)
    if len(roots)!=2 or roots[0]==roots[1]:
        raise ValueError("not a simple split quadratic residue algebra")
    assert (roots[0]+roots[1])%p==1%p
    return roots


def residue_field_projection(E,root,p):
    """O_K as Z+Z*omega; project each original coefficient a+b omega."""
    E=np.asarray(E,dtype=np.int64)
    if E.ndim!=2 or E.shape[1]%2:
        raise ValueError("not O-coordinate pairs")
    return (E[:,0::2]+root*E[:,1::2])%p


def f_rank(M,p):
    """Independent plain row-reduction rank over prime field Fp."""
    A=np.asarray(M,dtype=np.int64).copy()%p
    n,m=A.shape
    rank=0
    for col in range(m):
        pos=next((i for i in range(rank,n) if A[i,col]),None)
        if pos is None:
            continue
        if pos!=rank:
            A[[rank,pos],:]=A[[pos,rank],:]
        inv=pow(int(A[rank,col]),-1,p)
        A[rank,col:]=(A[rank,col:]*inv)%p
        for i in range(rank+1,n):
            v=int(A[i,col])
            if v:
                A[i,col:]=(A[i,col:]-v*A[rank,col:])%p
        rank+=1
        if rank==n:
            break
    return rank


def polynomial_jet_remainders(rmax):
    """x^r modulo (x^3-x)^2 = x^6+x^4+x^2 over F3."""
    out=[]
    current=[1,0,0,0,0,0]
    for r in range(rmax):
        out.append(tuple(current))
        # multiply by x and replace x^6 with -x^4-x^2
        carry=current[5]
        nextpoly=[0]+current[:5]
        nextpoly[4]=(nextpoly[4]-carry)%3
        nextpoly[2]=(nextpoly[2]-carry)%3
        current=[t%3 for t in nextpoly]
    assert out[0]==(1,0,0,0,0,0)
    assert out[6]==(0,0,2,0,2,0)
    return out


def check_symbolic_jet_span(X):
    """Original 100 monomial rows must be in 12 basis rows mod3."""
    remainders=polynomial_jet_remainders(R)
    assert X.shape[0]==R*S
    basic=tuple(2*r+s for r in range(6) for s in range(S))
    assert f_rank(X[list(basic),:],3)==12
    count=0
    for r in range(R):
        for s in range(S):
            target=X[2*r+s,:]
            reconstructed=sum(
                coeff*X[2*u+s,:]
                for u,coeff in enumerate(remainders[r])
            )%3
            assert np.array_equal(reconstructed,target),(
                "ordinary j0/j1 quotient reduction failed",r,s)
            count+=len(target)
    return {
        "ordinary_derivative_kernel":"(x^3-x)^2=x^6+x^4+x^2",
        "remainder_basis_per_W_monomial":6,
        "number_original_W_monomials":S,
        "basis_rank_F3":12,
        "source_coordinate_comparisons":count,
    }


def two_jet_column_permutation(X0, q):
    """Permute actual observations independently within each ORIGINAL jet."""
    ids=conjugation_permutation(q)
    N=len(q)
    idx=tuple(j*N+ids[i] for j in range(J) for i in range(N))
    assert len(idx)==J*N
    assert all(idx[idx[i]]==i for i in range(J*N))
    return X0[:,list(idx)],idx


def fixed_points(q):
    return sum((a+b,-b)==(a,b) for a,b in q)


def actual_source_certificate():
    q=original_q()
    E=original.evaluate_original_jets(q,R,S,J,MOD)
    independently=independent_original_jets(q,D,MOD)
    assert E.shape==(100,1052)==independently.shape
    assert np.array_equal(E,independently)
    roots=split_roots(D,P)
    assert roots==(0,1)
    X0=residue_field_projection(E,roots[0],P)
    X1=residue_field_projection(E,roots[1],P)
    assert X0.shape==X1.shape==(100,526)

    X0_perm,idx=two_jet_column_permutation(X0,q)
    assert np.array_equal(X1,X0_perm),(
        "full original source conjugate mirror identity failed")
    assert sum(idx[i]!=i for i in range(len(idx)))>0

    # The actual O_K Hermitian trace pairing, not same-side Euclidean dots.
    originalG=original.original_trace_gram(E,len(q),J,P)
    cross=(X0@X1.T+X1@X0.T)%P
    mirror=(2*(X0@X0_perm.T))%P
    assert originalG.shape==(100,100)
    assert np.array_equal(originalG,cross),(
        "actual full source Gram does not match conjugate cross pairing")
    assert np.array_equal(cross,mirror),(
        "conjugate mirror not an involution for this source")
    assert np.array_equal(originalG,originalG.T)

    residue_pairs=Counter(((a%3,(a+b)%3) for a,b in q))
    assert set(residue_pairs)==set((x,y) for x in range(3) for y in range(3))
    span0=check_symbolic_jet_span(X0)
    span1=check_symbolic_jet_span(X1)
    r0=f_rank(X0,P)
    r1=f_rank(X1,P)
    rg=f_rank(originalG,P)
    assert (r0,r1)==(12,12)
    assert rg<=12

    # A wrong same-embedding trace is falsified independently of summation
    # coincidences: for x=y=omega at roots 0 and1, the Hermitian trace=0
    # but the same-embedding sum of squares=1 mod3.
    omega=(0,1)
    left,right=omega[0]+omega[1]*roots[0],omega[0]+omega[1]*roots[1]
    correct=(2*left*right)%P
    fake=(left*left+right*right)%P
    assert correct==0 and fake==1

    # Hostile: the full source is invariant under conjugation, but an
    # arbitrarily truncated non-conjugate observation subset is NOT.
    culprit=(0,1)
    assert culprit in q and (1,-1) in q
    truncated=tuple(z for z in q if z!=culprit)
    try:
        conjugation_permutation(truncated)
    except ValueError:
        rejected=True
    else:
        rejected=False
    assert rejected

    try:
        split_roots(D,5)
    except ValueError:
        inert_rejected=True
    else:
        inert_rejected=False
    assert inert_rejected

    # A rank deficiency cannot be upgraded to a global bound without
    # integral determinant nonvanishing and a uniform original Gram theorem.
    return {
        "original_D":D,"full_Q":len(q),
        "original_R_S_J":[R,S,J],
        "entire_original_omega_coordinate_checks":int(E.size),
        "source_evaluation_shape":list(E.shape),
        "two_F3_residue_evaluation_shapes":[list(X0.shape),list(X1.shape)],
        "conjugation_involution_fixed_actual_points":fixed_points(q),
        "conjugation_mirror_coordinate_checks":int(X0.size),
        "full_original_integer_Gram_cells_checked":int(originalG.size),
        "whole_source_split_embedding_ranks_F3":[r0,r1],
        "actual_full_source_Gram_rank_F3":rg,
        "original_Gram_radical_dimension_F3":100-rg,
        "conditional_if_nonzero_integer_det_lower_v3":100-rg,
        "exact_ordinary_jet_quotient_span_checks":[span0,span1],
        "distinct_actual_residue_pairs":len(residue_pairs),
        "individual_residue_pair_counts_mod3":{
            str(k):v%3 for k,v in sorted(residue_pairs.items())
        },
        "wrong_same_embedding_dot_pairing_rejected":True,
        "nonconjugation_invariant_actual_point_truncation_rejected":True,
        "inert_p5_false_split_rejected":True,
        "no_picard_or_field_bound_promotion":True,
    }


def main():
    data=actual_source_certificate()
    print("PHASE310_FULL_ORIGINAL_SPLIT_MIRROR_PASS",data,flush=True)


if __name__=="__main__":
    main()
