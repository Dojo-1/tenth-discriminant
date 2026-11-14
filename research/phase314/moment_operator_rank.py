#!/usr/bin/env python3
"""Phase314-G: compute the actual F5 image dimension of the 78-moment
linear operator, NOT the rank of any of its 100x100 or 40x40 outputs.

All 78 source coefficient matrices are those from the *already tested*
full 300 signed-ray + 25 nonunit original primitive Gram oracle.
Upper triangular flattening identifies Sym_N(F5) with F5^(N(N+1)/2).
We compute rank(L), nullity(L), an explicit kernel if present, and
independently verify the actual original moment vector maps to its Gram.

The rank of a parameter-to-matrix map does NOT bound the rank of any
individual resulting matrix. Nonunit sign symmetry constrains
ACTUAL norm-ball moment counts but not arbitrary formal F5 coefficients.
"""
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for folder in ("phase206","phase311","phase313","phase314"):
    sys.path.insert(0,str(ROOT/"research"/folder))
from wild_quadratic_gram import (
    all_tame,unit_and_nonunit_coefficients,count_moments_signed,
    count_moments_unrestricted
)
from ray_to_original_gram import (
    ray_and_nonunit_strata,ray_count_Gram_D203,ray_count_Gram_D163_native,
    embed_integer_pair_to_omega
)
from inert_trace_radicals import rank_f5
import highjet_d203_original as pilot
import source_probe


def first_null_vector(A):
    """Deterministic independent row-echelon F5 kernel witness.

    rank_f5 from Phase311 computes the *rank*, this implementation
    independently builds a first free-variable kernel certificate.
    """
    matrix=np.asarray(A,dtype=np.int64).copy()%5
    rows,cols=matrix.shape
    pivot_cols=[]
    r=0
    for c in range(cols):
        options=np.flatnonzero(matrix[r:,c])
        if not len(options):
            continue
        pivot=r+int(options[0])
        if pivot!=r:
            matrix[[r,pivot]]=matrix[[pivot,r]]
        inverse=pow(int(matrix[r,c]),-1,5)
        matrix[r,c:]=(matrix[r,c:]*inverse)%5
        if r+1<rows:
            values=matrix[r+1:,c].copy()[:,None]
            matrix[r+1:,c:]=(matrix[r+1:,c:]-values*matrix[r:r+1,c:])%5
        pivot_cols.append(c)
        r+=1
        if r==rows:
            break
    assert rank_f5(A)==len(pivot_cols)
    free=[j for j in range(cols) if j not in set(pivot_cols)]
    if not free:
        return None,len(pivot_cols)
    v=np.zeros(cols,dtype=np.int64)
    v[free[0]]=1
    for row in range(len(pivot_cols)-1,-1,-1):
        c=pivot_cols[row]
        v[c]=(-int(np.dot(matrix[row,c+1:],v[c+1:])))%5
    assert np.any(v)
    assert not np.any((A@v)%5)
    return v,len(pivot_cols)


def moment_Gram_operator_certificate(D):
    if D not in (203,163):
        raise ValueError("only frozen original row sources D203 and D163")
    uc,nc,meta=unit_and_nonunit_coefficients(D)
    tame=all_tame(D)
    assert len(tame)==12
    n=100 if D==203 else 40
    idx=np.triu_indices(n)
    labels=[]
    matrices=[]
    for c in tame:
        for j in range(6):
            labels.append(("unit",c,j))
            matrices.append(uc[c][j])
    for j in range(6):
        labels.append(("nonunit",None,j))
        matrices.append(nc[j])
    assert len(labels)==len(matrices)==78
    assert all(np.array_equal(M,M.T) for M in matrices)
    A=np.column_stack([M[idx] for M in matrices])%5
    assert A.shape==(n*(n+1)//2,78)
    kernel,rank=first_null_vector(A)
    assert 0<=rank<=78
    nullity=78-rank
    assert (kernel is None)==(nullity==0)
    k_support=None
    if kernel is not None:
        k_support=[{"moment":labels[i],"coefficient_mod5":int(kernel[i])}
                   for i in range(len(labels)) if kernel[i]%5]
        assert len(k_support)>0
        assert np.array_equal(A@kernel%5,np.zeros(A.shape[0],dtype=np.int64))

    if D==203:
        Q=tuple(pilot.qmax(24))
        assert len(Q)==263
        direct,_=ray_count_Gram_D203(Q)
    else:
        rho,R,S,J,Qint=source_probe.params(D)
        assert (rho,R,S,J)==(21,40,1,1)
        Q=tuple(embed_integer_pair_to_omega(x) for x in Qint)
        assert len(Q)==109
        direct,_=ray_count_Gram_D163_native(Q)
    units,nonunits=ray_and_nonunit_strata(Q,D)
    m_unit=count_moments_signed(units)
    m_non=count_moments_unrestricted(nonunits)
    mvec=np.asarray(
        [v for c in tame for v in m_unit.get(c,(0,)*6)]
        + list(m_non),dtype=np.int64)
    assert len(mvec)==78
    actual_upper=(A@mvec)%5
    assert np.array_equal(actual_upper,direct[idx]),(
        "full 78-moment operator does NOT reproduce SAME original Gram")
    assert rank_f5(direct)==(63 if D==203 else 23)

    # Genuine actual sign closure forces sum u=0 for the FIRST nonunit
    # lift moments; this is NOT an additional formal kernel of A.
    assert sum(nonunits.values())==9
    assert m_non[1]==m_non[2]==0
    assert all(nonunits[u]==nonunits[(-u[0]%5,-u[1]%5)] for u in nonunits)

    return {
        "D":D,
        "source":"D203 exact original maximal Q263" if D==203
                  else "D163 exact original INTEGER order Q109",
        "original_source_rows":n,
        "actual_original_Q":len(Q),
        "full_symmetrical_Gram_coordinate_dim":int(A.shape[0]),
        "raw_signed_300_plus_25_ray_lift_bins":325,
        "quadratic_second_jet_parameters":78,
        "exact_F5_rank_of_moment_to_Gram_LINEAR_MAP":rank,
        "formal_moment_nullity_78_minus_operator_rank":nullity,
        "explicit_kernel_witness_if_any":k_support,
        "original_actual_G_matrix_rank_F5":rank_f5(direct),
        "original_actual_Gram_cells_reconstructed_by_operator":int(direct.size),
        "actual_nonunit_sign_odd_moments_x_y_vanish":[m_non[1],m_non[2]],
        "no_invalid_inference_matrix_rank_le_operator_rank":True,
        "no_class_one_or_uniform_cutoff_inference":True,
    }


def main():
    print("PHASE314_EXACT_WILD_TO_GRAM_OPERATOR_RANK_PASS",
          [moment_Gram_operator_certificate(D) for D in (203,163)],
          flush=True)


if __name__=="__main__":
    main()
