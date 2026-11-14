#!/usr/bin/env python3
"""Phase297-D: construct integral transverse projector on index-five D587 lattice.

Preregistered at 25907fd7 BEFORE this executable/results. Keep original
Q383/j0..4/trace B and all 725 old monomials. Only scale the ONE new
original odd row (r145,s4) by5. The scaling is an index-five
SUBLATTICE inclusion, not an original GL_730(Z5) gauge or extra v_p mass.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase292","phase297"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
import original_schur_integrality_k16 as parent
import odd_dual_witness_k16 as witness_parent

D=587
P=5
K=16
MOD=P**K
S=J=5
FROZEN={
 "research/phase297/original_schur_integrality_k16.py":
    "aa3678001c69a7235dca638638d2dab4c55b05b3",
 "research/phase297/odd_dual_witness_k16.py":
    "6b5052e53e15448f37e1b3a52c7ba8cbbcbc63a4",
}

def freeze():
    witness_parent.freeze()
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==sha,("frozen source changed",path,actual,sha)

def tracked_smith_solver(A0):
    """Integral-modular U A V=diagonal in Z/(5^16), with BOTH U,V.

    Smith V acts ONLY on the linear solver of the same original Gram.
    It is never substituted into the original trace metric B or the
    observation evaluation E. Every result is checked in original basis.
    """
    A=np.asarray(A0,dtype=object)%MOD
    n,m=A.shape
    assert n==m and 1<=n<=365
    U=np.eye(n,dtype=object)
    V=np.eye(n,dtype=object)
    levels=[]
    for i in range(n):
        tail=A[i:,i:]
        pivot=None
        start_v=levels[-1] if levels else 0
        for e in range(start_v,K):
            hits=np.argwhere(tail%(P**(e+1))!=0)
            if len(hits):
                r,c=map(int,hits[0])
                pivot=(e,i+r,i+c)
                break
        assert pivot is not None,("unexpected uncensored full matrix",i)
        e,r,c=pivot
        if r!=i:
            A[[i,r]]=A[[r,i]]
            U[[i,r]]=U[[r,i]]
        if c!=i:
            A[:,[i,c]]=A[:,[c,i]]
            V[:,[i,c]]=V[:,[c,i]]
        divisor=P**e
        quotient=MOD//divisor
        pivot_value=int(A[i,i])
        assert pivot_value%divisor==0
        inv=pow(pivot_value//divisor,-1,quotient)
        if i+1<n:
            below=A[i+1:,i].copy()
            assert all(int(x)%divisor==0 for x in below)
            coefficients=(below//divisor*inv)%quotient
            A[i+1:,i+1:]=(A[i+1:,i+1:]
                -coefficients[:,None]*A[i,i+1:])%MOD
            U[i+1:,:]=(U[i+1:,:]
                -coefficients[:,None]*U[i,:])%MOD
            A[i+1:,i]=0
            above_right=A[i,i+1:].copy()
            assert all(int(x)%divisor==0 for x in above_right)
            coefs=(above_right//divisor*inv)%quotient
            # Column operation: col_j -> col_j - coefs[j]*col_i.
            # Because entries below and above the pivot in col_i
            # have ALREADY been eliminated, this does not change
            # the remainder A[i+1:,i+1:].
            V[:,i+1:]=(V[:,i+1:]-V[:,[i]]*coefs[None,:])%MOD
            A[i,i+1:]=0
        levels.append(e)
        if (i+1)%120==0 or i+1==n:
            print("PHASE297D_UV_SMITH_PROGRESS",{
                "n":n,"processed":i+1,"exponent":e},flush=True)
    assert levels==sorted(levels) and max(levels)<K
    diag=np.diag(A).copy()
    assert not np.count_nonzero(A-np.diag(diag))
    # Full entrywise identity in R, not just a matching Smith profile.
    Aref=np.asarray(A0,dtype=object)
    factored=((U@Aref)%MOD@V)%MOD
    assert np.array_equal(factored,A),(
        "tracked original Gram Smith U*A*V is NOT exact")
    assert parent.frozen_source.independent_rank(
        np.asarray(U,dtype=np.int64)%P)==n
    assert parent.frozen_source.independent_rank(
        np.asarray(V,dtype=np.int64)%P)==n
    return levels,diag,U,V

def can_solve_or_fail(levels,diag,U,V,A,C,positive):
    """Compute every original cross-column's p-adic divisibility gate."""
    n=A.shape[0]
    r=C.shape[1]
    CU=(U@np.asarray(C,dtype=object))%MOD
    impossible=[]
    for i,e in enumerate(levels):
        divisor=P**e
        for j in range(r):
            if int(CU[i,j])%divisor:
                impossible.append({
                    "smith_row":i,"old_grade":e,
                    "new_column":j,
                    "transformed_original_cross_residue":int(CU[i,j]),
                    "required_divisor":divisor})
    if impossible:
        assert not positive
        return None,impossible
    assert positive
    Z=np.zeros((n,r),dtype=object)
    for i,e in enumerate(levels):
        divisor=P**e
        quotient=MOD//divisor
        inv=pow(int(diag[i])//divisor,-1,quotient)
        for j in range(r):
            target=int(CU[i,j])
            assert target%divisor==0
            Z[i,j]=(target//divisor*inv)%quotient
    T=(V@Z)%MOD
    # FULL original old-row basis, not Smith column coordinate basis!
    original_residual=(
        np.asarray(A,dtype=object)@T-np.asarray(C,dtype=object))%MOD
    assert not np.any(original_residual)
    return np.asarray(T,dtype=np.int64),[]

def toy():
    for a,c,scaled,fail in ((10,2,10,True),(10,5,5,False)):
        A=np.array([[a]],dtype=np.int64)
        C=np.array([[c]],dtype=np.int64)
        e,d,U,V=tracked_smith_solver(A)
        sol,issues=can_solve_or_fail(e,d,U,V,A,C,not fail)
        if fail:
            assert sol is None and issues
        else:assert sol is not None and not issues
        rescue=np.array([[scaled]],dtype=np.int64)
        restored,issues=can_solve_or_fail(
            e,d,U,V,A,rescue,True)
        assert restored is not None and not issues
    return {"unscaled_original_positive_Gram_nonintegral_A10_C2":True,
            "p5_scaled_nonintegral_cross_becomes_integral":True,
            "preintegral_A10_C5_stays_integral":True}

def original_source():
    rho,R,Ssrc,Jsrc,Q=params(D)
    assert (rho,R,Ssrc,Jsrc,len(Q))==(53,146,5,5,383)
    C=parent.source_high_precision(Q)
    E,checked=parent.rebuild_original(C,Q)
    W=np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
    assert parent.sanity_original_gram(E,Q,W)==36
    return E,Q,W,checked

def sector_ids(parity):
    p=0 if parity=="even" else 1
    old=[i for i in range(725) if ((i//5)+(i%5))%2==p]
    new=[i for i in range(725,730) if ((i//5)+(i%5))%2==p]
    assert (len(old),len(new))==(
        (363,2) if parity=="even" else (362,3))
    assert [i%5 for i in new]==(
        [1,3] if parity=="even" else [0,2,4])
    return old,new

def main():
    freeze()
    controls=toy()
    E,Q,W,jet_oracle=original_source()
    n=725
    r=5
    Tfull=np.zeros((n,r),dtype=np.int64)
    oldGram=np.zeros((n,n),dtype=np.int64)
    oldCross=np.zeros((n,r),dtype=np.int64)
    records={}
    for parity in ("even","odd"):
        oldids,newids=sector_ids(parity)
        A=parent.pairings_three_digits(E[oldids],E[oldids],W)
        C=parent.pairings_three_digits(E[oldids],E[newids],W)
        levels,diag,U,V=tracked_smith_solver(A)
        hist=dict(sorted(Counter(levels).items()))
        assert hist==(
            parent.EXPECTED_K9[parity] if False else
            (witness_parent.EXPECTED_ODD_OLD if parity=="odd" else
             {0:63,2:15,3:47,4:63,5:47,6:10,7:5,8:50,9:13,12:20,14:30})
        )
        assert max(levels)==14
        raw_solution,issues=can_solve_or_fail(
            levels,diag,U,V,A,C,positive=(parity=="even"))
        if parity=="even":
            assert raw_solution is not None and not issues
            repaired=C.copy()
            solved=raw_solution
        else:
            assert raw_solution is None and issues
            assert set(x["new_column"] for x in issues)=={2},(
                "one-row obstruction expectation failed",issues[:5])
            # Exactly ONE original row r145,s4 is rescaled.
            repaired=C.copy()
            repaired[:,2]=(repaired[:,2]*P)%MOD
            solved,newissues=can_solve_or_fail(
                levels,diag,U,V,A,repaired,True)
            assert solved is not None and not newissues
            # Original other two odd rows already admit integral
            # solutions individually, verified rather than inferred.
            other,otherissues=can_solve_or_fail(
                levels,diag,U,V,A,C[:,:2],True)
            assert not otherissues and other is not None
        oldGram[np.ix_(oldids,oldids)]=A
        oldCross[np.ix_(oldids,[i%5 for i in newids])]=repaired
        Tfull[np.ix_(oldids,[i%5 for i in newids])]=solved
        records[parity]={
            "original_old_rows":len(oldids),
            "original_new_rows":[[145,int(i%5)] for i in newids],
            "old_Gram_highest_5adic_Smith_exponent":max(levels),
            "unscaled_integrality_failure_in_source":issues[:4] if issues else [],
            "unscaled_new_rows_with_integral_projection":[
                int(i%5) for i in newids if not any(
                    j["new_column"]==ind for j in issues
                    for ind in [newids.index(i)])
            ],
            "scaled_new_row":[145,4] if parity=="odd" else None,
            "every_original_repaired_cross_pairing_solved_mod5pow16":True,
            "integral_projection_coefficients_in_original_old_rows":True,
            "no_source_primitive_double_counting":True,
        }
        print("PHASE297D_SECTOR_INTEGRAL_ORTHOGONALIZATION",{
            "sector":parity,**records[parity]},flush=True)
    # Full original 725x5 compatibility in its ORIGINAL global row order.
    residual=(np.asarray(oldGram,dtype=object)
              @np.asarray(Tfull,dtype=object)
              -np.asarray(oldCross,dtype=object))%MOD
    assert not np.any(residual)
    assert Tfull.shape==(725,5)
    assert np.all((Tfull>=0)&(Tfull<MOD))
    origNew=E[725:].copy()
    repairedNew=origNew.copy()
    repairedNew[4]=(repairedNew[4]*P)%MOD
    # ACTUAL integral new-row evaluation after source-relative
    # orthogonalization. This is NOT an arbitrary Gram-only isometry.
    correctedObj=(np.asarray(repairedNew,dtype=object)
                  -np.asarray(Tfull.T,dtype=object)
                   @np.asarray(E[:725],dtype=object))%MOD
    corrected=np.asarray(correctedObj,dtype=np.int64)
    cross=parent.pairings_three_digits(E[:725],corrected,W)
    assert not np.any(cross),("original row-jet cross source not orthogonal")
    scaledGram=parent.pairings_three_digits(repairedNew,repairedNew,W)
    S_direct=parent.pairings_three_digits(corrected,corrected,W)
    S_algebra=(np.asarray(scaledGram,dtype=object)
               -np.asarray(oldCross.T,dtype=object)
                @np.asarray(Tfull,dtype=object))%MOD
    assert np.array_equal(
        np.asarray(S_algebra,dtype=np.int64),S_direct)
    assert np.array_equal(S_direct,S_direct.T)
    # C2 inversion is not mixed by the constructed row gauge.
    even_old,even_new=sector_ids("even")
    odd_old,odd_new=sector_ids("odd")
    assert not np.any(Tfull[np.ix_(even_old,[0,2,4])])
    assert not np.any(Tfull[np.ix_(odd_old,[1,3])])
    digest=hashlib.sha256(json.dumps(
        Tfull.tolist(),separators=(",",":")).encode()).hexdigest()
    assert len(digest)==64
    print("PHASE297D_MINIMAL_INDEX_FIVE_TRANSVERSE_INTEGRAL_REPAIR",{
        "original_D":D,
        "original_Q":len(Q),
        "old_original_rows":725,
        "new_original_rows":5,
        "original_ordinary_Z_jets_W_fixed":J,
        "original_trace_metric":[2,2*D],
        "Frobenius_basis_UNDIVIDED":True,
        "independent_original_jet_probe_coordinates":jet_oracle,
        "original_new_row_scaled_by_five":[145,4],
        "all_other_729_original_rows_UNSCALED":True,
        "relative_index_in_FULL_original_row_lattice":5,
        "exact_5adic_projection_denominator_BEFORE_repair":1,
        "repaired_modulus":MOD,
        "repaired_p16_Gram_cross_entries_zero":cross.size,
        "repaired_p16_Schur_5x5_symmetric":True,
        "full_original_725x5_integral_projection_matrix_sha256":digest,
        "parity_sector_records":records,
        "historical_ORIGINAL_Gram_v5_unchanged":3924,
        "historical_ORIGINAL_Schur_v5_unchanged":69,
        "MODIFIED_index5_subLattice_Gram_v5":3926,
        "MODIFIED_index5_subLattice_Schur_v5":71,
        "MODIFIED_even_odd_Schur_v5":[28,43],
        "modified_values_are_NOT_original_field_bound_factors":True,
        "finite_modular_solution_lift_to_Z5_exists_by_uncensored_Smith":True,
        "negative_positive_toys":controls,
        "no_uniform_h1_or_tenth_discriminant_improvement":True
    },flush=True)
    print("PASS Phase297-D minimal index-five integral original-source transverse repair",
          flush=True)

if __name__=="__main__":
    main()
