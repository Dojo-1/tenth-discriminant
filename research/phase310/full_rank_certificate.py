#!/usr/bin/env python3
"""Phase310-C: independent good-reduction minor proves full K-rank; p3 floor.

At ell=101, simple split roots 46/56 give exact rank-revealing 100x100
minors of the SAME original D203 100-row polynomial-jet evaluation.
This proves row independence over K and, via positive Hermitian trace,
det G !=0 over integers. Combined with the censored p3 local Smith profile
and the mirror factorization, it certifies a SAME-source lower bound.

This has NO uniform class-number-one implication (D203 has h=4).
"""
from pathlib import Path
import sys
import math

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for dirname in ("phase304","phase307","phase310"):
    sys.path.insert(0,str(ROOT/"research"/dirname))
import highjet_d203_original as original
from source_saturation import independent_original_jets
from split_dvr_smith import actual_D203_split_dvr

D=203
R,S,J=50,2,2
ALLOWED_GOOD_PRIMES=(101,109,113,127,131,137,149)


def prime(n):
    return n>=2 and all(n%t for t in range(2,math.isqrt(n)+1))


def simple_roots(d,ell):
    assert prime(ell)
    m=(d+1)//4
    return tuple(
        r for r in range(ell)
        if (r*r-r+m)%ell==0 and (2*r-1)%ell!=0
    )


def row_rank_and_pivot_columns(mat,p):
    """Exact finite-field Gaussian rank, returning original column indices."""
    a=np.asarray(mat,dtype=np.int64).copy()%p
    n,m=a.shape
    r=0
    pivots=[]
    for c in range(m):
        row=next((i for i in range(r,n) if a[i,c]),None)
        if row is None:
            continue
        if row!=r:
            a[[r,row],:]=a[[row,r],:]
        inverse=pow(int(a[r,c]),-1,p)
        a[r,c:]=(a[r,c:]*inverse)%p
        for i in range(r+1,n):
            q=int(a[i,c])
            if q:
                a[i,c:]=(a[i,c:]-q*a[r,c:])%p
        pivots.append(c)
        r+=1
        if r==n:
            break
    assert len(pivots)==r
    return r,tuple(pivots)


def determinant_mod_p(matrix,p):
    """Independent small exact square determinant modulo p, not a float."""
    a=np.asarray(matrix,dtype=np.int64).copy()%p
    if a.ndim!=2 or a.shape[0]!=a.shape[1]:
        raise ValueError("determinant requires square matrix")
    n=a.shape[0]
    d=1
    for col in range(n):
        row=next((i for i in range(col,n) if a[i,col]),None)
        if row is None:
            return 0
        if row!=col:
            a[[row,col],:]=a[[col,row],:]
            d=(-d)%p
        pivot=int(a[col,col])
        d=(d*pivot)%p
        inv=pow(pivot,-1,p)
        for i in range(col+1,n):
            factor=(int(a[i,col])*inv)%p
            if factor:
                a[i,col:]=(a[i,col:]-factor*a[col,col:])%p
    return int(d%p)


def independent_minor_known_controls():
    tri=np.asarray(((1,2,3),(0,3,1),(0,0,9)),dtype=np.int64)
    assert determinant_mod_p(tri,101)==27
    a=np.asarray(((1,2,0,0),(0,3,1,0),(0,0,9,1)),dtype=np.int64)
    rank,cols=row_rank_and_pivot_columns(a,101)
    assert rank==3 and cols==(0,1,2)
    duplicate=a.copy()
    duplicate[1,:]=duplicate[0,:]
    assert row_rank_and_pivot_columns(duplicate,101)[0]==2
    assert determinant_mod_p(a[:,cols],101)==27
    return {"known_triangular_det_mod101":27,
            "rectangular_minor_and_wrong_duplicate_rank":[3,2]}


def original_evaluation_at_good_prime(q,ell):
    E=original.evaluate_original_jets(q,R,S,J,ell)
    separately=independent_original_jets(q,D,ell)
    assert E.shape==(100,1052)==separately.shape
    assert np.array_equal(E,separately),(
        "different omega-source evaluator did not match all 105200 entries")
    return E


def rank_minor_good_prime(q,ell):
    roots=simple_roots(D,ell)
    if not roots:
        return {"ell":ell,"simple_roots":[], "status":"no_good_split_root"}
    E=original_evaluation_at_good_prime(q,ell)
    a,b=E[:,0::2],E[:,1::2]
    entries=[]
    matrices={}
    for root in roots:
        X=(a+root*b)%ell
        rank,pivots=row_rank_and_pivot_columns(X,ell)
        determinant=(determinant_mod_p(X[:,list(pivots)],ell)
                     if rank==R*S else None)
        if determinant is not None:
            assert determinant!=0
        matrices[root]=X
        entries.append({
            "root":root,
            "Fell_rank":rank,
            "100x100_minor_det_modell_if_full":determinant,
            "pivot_observation_jet_columns_if_full":
                list(pivots) if rank==R*S else None,
        })
    gram=original.original_trace_gram(E,len(q),J,ell)
    original_gram_det=determinant_mod_p(gram,ell)
    if len(roots)==2:
        X0,X1=matrices[roots[0]],matrices[roots[1]]
        assert np.array_equal(
            gram,(X0@X1.T+X1@X0.T)%ell)
    return {
      "ell":ell,"simple_roots":list(roots),"original_source_all_coordinates_checked":int(E.size),
      "rank_minor_witnesses":entries,
      "original_trace_Gram_det_mod_good_prime":original_gram_det,
      "any_full_rank_witness":any(x["Fell_rank"]==100 for x in entries),
    }


def source_index_square_lower_bound():
    controls=independent_minor_known_controls()
    original.guard()
    rho,r,s,j,_=original.params(D)
    assert (rho,r,s,j)==(24,R,S,J)
    q=tuple(original.qmax(rho))
    assert len(q)==263

    tried=[]
    winner=None
    for ell in ALLOWED_GOOD_PRIMES:
        record=rank_minor_good_prime(q,ell)
        tried.append(record)
        if record.get("any_full_rank_witness"):
            winner=record
            break
    if winner is None:
        raise AssertionError(
            "no preregistered split-prime modular minor proves full source rank")

    # Nonzero K-valued evaluation minor from finite-field reduction.
    # The original integer Gram is positive definite under the complex
    # Hermitian trace since the source rows are K-linearly independent.
    # Thus its determinant is a positive nonzero INTEGER.
    split=actual_D203_split_dvr()
    local_lower=split["local_index_lower_bound_log3"]
    assert local_lower>=658
    assert split["K_one_source_and_Gram_rank_F3"]==[12,12]
    # Full-rank local Smith X0 = U [D 0] V over Z_3. The middle
    # 100x100 matrix from 2 V P_tau V^T is integral over Z_3;
    # v3(det original G) >= 2 sum_i v3(D_ii).
    # The finite depth-10 source profile is a certified LOWER BOUND
    # on that sum even though 46 factors remain censored.
    derived_lower=2*local_lower
    assert derived_lower>=1316
    return {
      "good_prime_minor_oracles":controls,
      "first_predeclared_successful_good_prime":winner["ell"],
      "preregistered_good_prime_candidates_tested":tried,
      "fixed_original_D":D,"full_original_source_100_rows":True,
      "nonzero_O_K_minor_proves_original_K_linear_full_rank":True,
      "real_Hermitian_trace_Gram_positive_definite_by_full_row_rank":True,
      "p3_split_local_source_Smith_lower_bound":local_lower,
      "p3_split_local_source_censored_factors":
          split["local_smith_censored_count"],
      "derived_certified_original_Gram_v3_lower_bound":derived_lower,
      "not_exact_v3_and_not_independent_extra_prime_mass":True,
      "D203_is_class_number_four":True,
      "no_new_uniform_h1_or_tenth_discriminant_bound":True,
    }


def main():
    print("PHASE310_FULL_SOURCE_MINOR_AND_INDEX_SQUARE_PASS",
          source_index_square_lower_bound(),flush=True)


if __name__=="__main__":
    main()
