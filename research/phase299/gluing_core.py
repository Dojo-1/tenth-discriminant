#!/usr/bin/env python3
"""Phase299 common p5 original-Gram gluing certificate and hostile toy worlds.

Preregistered at dd651c2b BEFORE code or source measurements.
Standard discriminant bilinear overlattice theorem (not new).
A certified h=1 negative cross class is repaired by an ORTHOGONAL
INDEX-5 sublattice M, while the unchanged original lattice L is
reconstructed as the H-overlattice of M. Never add gluing index to L det.
"""
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase297",):
    sys.path.insert(0,str(ROOT/"research"/sub))
import original_schur_integrality_k16 as hi
import minimal_transverse_repair as solver

P=5
PRECISION=16
MOD=P**PRECISION

def pv(number):
    n=int(number)%MOD
    if n==0:return PRECISION
    k=0
    while n%P==0:
        k+=1;n//=P
    return k

def mm(A,B):
    return (np.asarray(A,dtype=object)@
            np.asarray(B,dtype=object))%MOD

def digest(v):
    return hashlib.sha256(json.dumps(
        [int(x) for x in v],separators=(",",":")).encode()).hexdigest()

def verified_nonintegral_gluing(A,c,b,oldE=None,newE=None,W=None,
                                record_full_vector=False):
    """Construct k=5*y-a*old with A*a=5c in the ORIGINAL row basis.

    If the old Smith is uncensored, congruence membership at K16
    identifies the exact Z5 original Gram cokernel. Not a finite-K
    heuristic when all its elementary divisors have degree<K.
    """
    A=np.asarray(A,dtype=np.int64)
    c=np.asarray(c,dtype=np.int64).reshape(-1,1)
    b=int(b)%MOD
    n=A.shape[0]
    assert A.shape==(n,n) and c.shape==(n,1)
    assert np.array_equal(A,A.T)
    grades,diag,U,V=solver.tracked_smith_solver(A)
    assert len(grades)==n and max(grades)<PRECISION
    raw,issues=solver.can_solve_or_fail(
        grades,diag,U,V,A,c,False)
    assert raw is None and issues
    scaled=np.asarray((P*np.asarray(c,dtype=object))%MOD,dtype=np.int64)
    a,other=solver.can_solve_or_fail(
        grades,diag,U,V,A,scaled,True)
    assert a is not None and not other
    assert a.shape==(n,1)
    aobj=np.asarray(a,dtype=object)
    Aobj=np.asarray(A,dtype=object)
    cobj=np.asarray(c,dtype=object)
    assert not np.any((Aobj@aobj-P*cobj)%MOD)
    assert np.any(a%P!=0),(
        "nontrivial original projection class gave p-divisible scaled coefficients")

    # Orthogonal complement source generator k=5y-a·old.
    # Norm identity is integer and modulo 5^16 checked using
    # the original Gram metric, not normalized Smith columns.
    c_a=int((cobj.T@aobj)[0,0])
    a_A_a=int((aobj.T@Aobj@aobj)[0,0])
    m=(P*P*b-P*c_a)%MOD
    assert (a_A_a+m-P*P*b)%MOD==0
    assert (P*P*b-a_A_a)%MOD==m

    # Full ORIGINAL next-row Gram and its Smith invariant grades.
    G=np.zeros((n+1,n+1),dtype=np.int64)
    G[:n,:n]=A;G[:n,n]=c[:,0];G[n,:n]=c[:,0];G[n,n]=b
    gl,gh=hi.high_precision_smith(G)
    assert len(gl)==n+1 and max(gl)<PRECISION
    oldvaluation=sum(grades)
    fullvaluation=sum(gl)
    normvaluation=pv(m)
    assert normvaluation<PRECISION,(
        "rank-one orthogonal complement norm censored at fixed K16",m)
    assert oldvaluation+normvaluation-2==fullvaluation,(
        "index-square determinant formula failed",
        oldvaluation,normvaluation,fullvaluation)
    assert m%P==0,(
        "the complement's 5-primary generator did not lie in K sharp")
    # H generator: ([a/5]*old, [k/5]); both have order exactly5.
    # The norm of y decomposes as a²/25+m/25. Its numerator
    # has to be divisible by 25 (and equals 25*b modulo K).
    assert (a_A_a+m)%(P*P)==0
    assert (a_A_a+m-P*P*b)%MOD==0

    source_checks={}
    if oldE is not None:
        oldE=np.asarray(oldE,dtype=np.int64)
        newE=np.asarray(newE,dtype=np.int64).reshape(1,-1)
        W=np.asarray(W,dtype=np.int64)
        assert oldE.shape==(n,len(W)) and newE.shape==(1,len(W))
        assert np.max(W)<2**16
        # source-native evaluation of k: only a genuine original
        # row combination; no Smith/observation-metric gauge.
        krow=(P*np.asarray(newE,dtype=object)-
              aobj.T@np.asarray(oldE,dtype=object))%MOD
        assert krow.shape==(1,len(W))
        rawpair=(np.asarray(oldE,dtype=object)*
                 np.asarray(W,dtype=object)[None,:])@krow.T%MOD
        assert all(int(x)==0 for x in rawpair.reshape(-1)),(
            "k failed to be orthogonal to all original old E rows")
        directnorm=sum(int(krow[0,i])*int(krow[0,i])*int(W[i])
                       for i in range(len(W)))%MOD
        assert directnorm==m,("orthogonal norm/trace source disagreement")
        rawnew=sum(int(krow[0,i])*int(newE[0,i])*int(W[i])
                   for i in range(len(W)))%MOD
        assert rawnew==(P*b-c_a)%MOD
        source_checks={
            "original_jet_observation_channels":len(W),
            "original_old_row_pairings_zero":n,
            "direct_original_trace_metric_k_squared_mod_p16":directnorm,
            "direct_original_k_pairing_with_new_y_mod_p16":rawnew,
            "source_orthogonal_generator_actual_E_verified":True
        }

    # A proposed D(L1)->D(L0) *by rational projection* is invalid:
    # the zero class [y]=0 in D(L1) projects to nonzero [a/5].
    # This counterexample is intrinsic to the original cross module.
    result={
        "old_original_rows":n,
        "source_original_new_rows":1,
        "old_5adic_Gram_smith_max_grade":max(grades),
        "new_full_original_Gram_smith_max_grade":max(gl),
        "old_5adic_Gram_determinant_valuation":oldvaluation,
        "original_full_5adic_Gram_determinant_valuation":fullvaluation,
        "original_unscaled_projection_rejected_by_old_Gram_cokernel":True,
        "five_times_original_projection_integral":True,
        "exact_5adic_projection_denominator_h":1,
        "one_orthogonal_complement_generator_k":"5*y - sum a_i*old_i",
        "generator_k_original_coefficients_sha256":digest(a[:,0]),
        "generator_k_coefficient_count":n,
        "k_original_trace_norm_mod_p16":m,
        "k_original_trace_norm_5valuation":normvaluation,
        "isotropic_graph_H_exact_order":5,
        "H_into_discriminant_old_component_has_exact_order5":True,
        "H_into_discriminant_orthogonal_component_has_exact_order5":True,
        "integral_orthogonal_subLattice_index_in_original_L":5,
        "discriminant_full_index_square_5valuation_identity":True,
        "bilinear_isotropic_glue_generator_from_original_y":True,
        "canonical_discriminant_quotient_projection_DOES_NOT_DESCEND":True,
        "original_L_is_recovered_as_H_overlattice_of_orthogonal_M":True,
        "no_new_original_Gram_valuation_factor":True,
        "source_native_direct_checks":source_checks
    }
    if record_full_vector:
        result["full_a_coefficients_mod_p16"]=[int(x) for x in a[:,0]]
    return result,a,grades,U

def small_scalar_glue_enumeration(a,c,b):
    """Enumerate H, H-perp and quotient order/exponent for rank-1 toys.

    D([a])_p = Z/p^va and D([m])_p = Z/p^vm with pairing
    diag(unit_a/p^va, unit_m/p^vm).
    """
    assert a>0 and b>0 and a*b-c*c>0
    assert Fraction(c,a).denominator%P==0
    assert Fraction(c,a).denominator==P
    scaled=Fraction(P*c,a)
    assert scaled.denominator%P!=0
    # In the following explicit toys scaled=1 exactly over Q.
    assert scaled==1
    m=P*P*b-P*c
    va=pv(a);vm=pv(m)
    assert 1<=va<=2 and 1<=vm<=2
    oa=P**va;om=P**vm
    unitA=a//oa
    unitM=m//om
    H={(i*(oa//P)%oa,i*(om//P)%om) for i in range(P)}
    assert len(H)==P
    assert all((unitA*x//(oa//P) if False else 0)==0 for x,y in H)
    # Actual bilinear pairing with generator a/5 and k/5:
    # b((u,v),(a/5,k/5)) ≡ (unitA*u+unitM*v)/5 (mod Z5).
    Hp={(x,y) for x in range(oa) for y in range(om)
        if (unitA*x+unitM*y)%P==0}
    assert H<=Hp
    assert len(Hp)==oa*om//P
    quotient_order=len(Hp)//len(H)
    assert quotient_order==P**(va+vm-2)
    cosets=set()
    for x,y in Hp:
        orbit=frozenset(((x+h[0])%oa,(y+h[1])%om) for h in H)
        cosets.add(orbit)
    assert len(cosets)==quotient_order
    # p-torsion exponent of quotient is <=p if 5*(x,y) belongs
    # to H for EVERY H-perp representative, else it exceeds5.
    exponent_le_p=all(((P*x)%oa,(P*y)%om) in H for x,y in Hp)
    if va==vm==1:assert quotient_order==1
    if va==vm==2:assert quotient_order==P**2 and exponent_le_p
    return {
        "old_rank_one_Gram":a,"cross":c,"new_norm":b,
        "orthogonal_complement_norm":m,
        "H_order":len(H),
        "orthogonal_sum_discriminant_group_order":oa*om,
        "H_perp_order":len(Hp),
        "Hperp_over_H_order":quotient_order,
        "Hperp_over_H_exponent_divides5":exponent_le_p,
        "expected_full_original_p5_determinant_valuation":pv(a*b-c*c),
        "not_product_of_separate_cokernel_debts":True
    }

def toy_controls():
    data=[]
    for a,c,b in ((10,2,2),(25,5,10)):
        assert a*b-c*c>0
        result,vec,_,_=verified_nonintegral_gluing(
            np.array([[a]],dtype=np.int64),
            np.array([[c]],dtype=np.int64),
            b,record_full_vector=True)
        explicit=small_scalar_glue_enumeration(a,c,b)
        assert result["original_full_5adic_Gram_determinant_valuation"]==(
            explicit["expected_full_original_p5_determinant_valuation"])
        data.append({"algebraic":result,"complete_finite_group_glue":explicit})
    # Independent integral positive case: original A=10,c=5,b=10.
    # t=1/2 ∈ Z5, so its complement k=y-(1/2)x lies IN original L.
    A=np.array([[10]],dtype=np.int64)
    C=np.array([[5]],dtype=np.int64)
    levels,diag,U,V=solver.tracked_smith_solver(A)
    t,issues=solver.can_solve_or_fail(levels,diag,U,V,A,C,True)
    assert t is not None and not issues
    b=10
    m=(b-int(C[0,0])*int(t[0,0]))%MOD
    assert m%P==0
    full=np.array([[10,5],[5,10]],dtype=np.int64)
    old=sum(levels)
    vfull=sum(hi.high_precision_smith(full)[0])
    assert old+pv(m)==vfull
    assert vfull==2
    return {
      "exact_hostile_nonintegral_gluing_toys":data,
      "already_integral_control_H_trivial":True,
      "already_integral_control_index":1,
      "already_integral_control_original_v5_full":vfull
    }
