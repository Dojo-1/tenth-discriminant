#!/usr/bin/env python3
"""Phase294-B: FULL p5-Frobenius-normalized source under MOVED Q.

Preregistered at 44a34a5 BEFORE code and CI. This is an explicit
Z/5^9 chart change for ALL 725x3830 normalized entries with moved
observations, NOT a statement about the original D583 Q or a
primitive/Smith new valuation.
"""
from collections import Counter
from pathlib import Path
import subprocess
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for sub in ("phase206","phase292"):
    sys.path.insert(0,str(ROOT/"research"/sub))
from source_probe import params
from matched_inert5_neighbor import (
    source_normalized,oracle_exact
)

P,K=5,9
D_A,D_B=583,587
R,S,J=145,5,5
FROBENIUS_OLD=1350
K_NUM=K+(S-1)
Q_MOD=P**K_NUM
MOD=P**K
BLOB_GUARDS={
 "research/phase206/source_probe.py":
       "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
 "research/phase204/ordinary_jet_filtration.py":
       "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
 "research/phase292/matched_inert5_neighbor.py":
       "9216de10f311cf301413de663738804b5fbec203",
}

def original_guard():
    for path,sha in BLOB_GUARDS.items():
        observed=subprocess.check_output(
           ["git","rev-parse","HEAD:"+path],
           cwd=ROOT,text=True).strip()
        assert observed==sha,("changed original-source helper",path,observed,sha)

def hensel_alpha():
    """Root of D_A*a^2=D_B in Z/(5^13), with root2 modulo5."""
    root=2
    assert (D_A*root*root-D_B)%P==0
    for exp in range(1,K_NUM):
        p_pow=P**exp
        error=D_B-D_A*root*root
        assert error%p_pow==0
        derivative=2*D_A*root
        assert derivative%P
        step=((error//p_pow)*pow(derivative,-1,P))%P
        root+=step*p_pow
        assert (D_A*root*root-D_B)%(p_pow*P)==0
    assert 0<=root<Q_MOD
    assert (D_A*root*root-D_B)%Q_MOD==0
    assert (root%5,root%25,root%125)==(2,17,67)
    # The naive residue-level chart 2 does NOT extend to modulus 25.
    assert (D_A*2*2-D_B)%25!=0
    return root

def source_gram_frozen_samples(C,D):
    """A bounded exact Gram oracle; multiplication never overflows int64."""
    ids=[0,1,5,25,99,143,333,500,724]
    assert len(ids)==9 and max(ids)<725
    V=np.asarray(C[ids],dtype=np.int64)%MOD
    weights=np.tile(np.array([2,2*D],dtype=np.int64),J*383)%MOD
    assert len(weights)==3830
    # Entrywise product is REDUCED BEFORE np.matmul:
    # at most 3830*(5^9-1)^2 <2^63.
    assert 3830*MOD*MOD < 2**63
    G=((V*weights)%MOD@V.T)%MOD
    assert np.array_equal(G,G.T)
    # Independent original trace-coordinate scalar dot checks.
    for i,j in ((0,0),(1,4),(4,8),(6,6),(8,8)):
        scalar=sum((int(V[i,c])*int(weights[c])*int(V[j,c]))
            for c in range(3830))%MOD
        assert scalar==int(G[i,j])
    return G

def original_residue_support_remainder(Q):
    before=Counter((x%P,y%P) for x,y in Q)
    after=Counter((x%P,(2*y)%P) for x,y in Q)
    mass=sum(abs(after[z]-before[z])
             for z in before.keys()|after.keys())//2
    assert mass==104
    assert (22,1) in Q and (22,2) not in Q
    return mass

def main():
    original_guard()
    rho_a,Ra,Sa,Ja,Qa=params(D_A)
    rho_b,Rb,Sb,Jb,Qb=params(D_B)
    assert (rho_a,Ra,Sa,Ja,len(Qa))==(53,R,S,J,383)
    assert (rho_b,Rb,Sb,Jb,len(Qb))==(53,146,S,J,383)
    assert Qa==Qb
    assert (-D_A)%5==2 and (-D_B)%5==3
    alpha=hensel_alpha()
    assert (2*D_A*alpha*alpha-2*D_B)%Q_MOD==0
    # This is a FORMAL moved Q, not Q_A and not an actual D583 ellipse.
    moved=[(x,(alpha*y)%Q_MOD) for x,y in Qb]
    assert len(moved)==383 and len(set(moved))==383
    assert moved!=Qa
    assert (22,alpha%Q_MOD) in moved
    assert (22,alpha%Q_MOD) not in Qa

    print("PHASE294B_MOVED_SOURCE",{
      "phase":"building D587 FIRST725 ORIGINAL ROW diagnostic",
      "alpha_mod5_13":alpha,"source_numerator_mod":Q_MOD,
    },flush=True)
    C_B,F_B,hist_B=source_normalized(D_B,Qb,R,S,J)
    assert C_B.shape==(725,3830)
    assert F_B==FROBENIUS_OLD
    assert hist_B=={0:165,1:155,2:145,3:135,4:125}
    checks_B=oracle_exact(D_B,Qb,R,S,J,C_B)
    assert checks_B==480
    print("PHASE294B_MOVED_SOURCE",{
      "phase":"building D583 source on FORMAL MOVED points; NOT original Q_A",
    },flush=True)
    C_A,F_A,hist_A=source_normalized(D_A,moved,R,S,J)
    assert C_A.shape==(725,3830)
    assert (F_A,hist_A)==(F_B,hist_B)
    checks_A=oracle_exact(D_A,moved,R,S,J,C_A)
    assert checks_A==480

    transported=C_B.copy()
    # B FIELD VALUE CHART -> A FIELD VALUE CHART:
    # (a,b) -> (a,alpha*b). Source row indices remain IDENTITY.
    transported[:,1::2]=(transported[:,1::2]*alpha)%MOD
    comparison=(C_A-transported)%MOD
    assert np.count_nonzero(comparison)==0,(
        "FULL normalized original Z-jet transport failed",
        int(np.count_nonzero(comparison)),
        tuple(int(x) for x in np.argwhere(comparison)[0])
    )
    assert np.array_equal(C_A%P,transported%P)
    assert C_A.shape[0]*C_A.shape[1]==2_776_750
    G_A=source_gram_frozen_samples(C_A,D_A)
    G_B=source_gram_frozen_samples(C_B,D_B)
    assert np.array_equal(G_A,G_B)
    # FROBENIUS division has been carried at the exact same old
    # levels in BOTH fields: no new or independent p-adic mass.
    assert sum((min(r//P,S-1-s)) for r in range(R) for s in range(S))==1350

    # NEGATIVE CONTROL: an unchanged original point is not its moved
    # image even at p5; row Z and jet j0 expose this directly.
    idx=Qb.index((22,1))
    # At row Z=(r1,s0), k=0: imaginary coordinate in B is +1,
    # in the moved A is alpha; at fixed Q_A it would be +1.
    col=2*idx+1
    assert int(C_B[1*S+0,col])%P==1
    assert int(C_A[1*S+0,col])%P==alpha%P==2
    assert (alpha-1)%P!=0
    support_mass=original_residue_support_remainder(Qa)
    # Safe p-adic precision rule cannot be shortened after dividing:
    assert 4+K==K_NUM
    assert (5%5)==(10%5) and (5//5)%5!=(10//5)%5
    # A SPLIT p7 control: no inert p7 Frobenius re-use.
    assert (-D_B)%7 in {u*u%7 for u in range(7)}

    print("PHASE294B_FULL_NORMALIZED_MOVING_CHART",{
      "source_A":"D583 FORMAL MOVED Q, NOT original number-field Q",
      "source_B":"D587 FIRST725 original rows, original Q; DIAGNOSTIC",
      "original_D587_full_source_row_count_unmodified":730,
      "source_rows_frozen":R*S,
      "all_original_Q_point_indices":len(Qb),
      "all_original_ordinary_Z_jet_orders":list(range(J)),
      "all_original_value_coordinate_channels":C_A.shape[1],
      "source_entries_checked_exactly_mod5_9":C_A.size,
      "prime":P,"normalized_source_precision_exponent":K,
      "original_numerator_precision_exponent":K_NUM,
      "Hensel_alpha_mod5_13":alpha,
      "alpha_reductions_mod5_25_125":[alpha%5,alpha%25,alpha%125],
      "source_normalizations_existing_old_F5_counted_once":F_A,
      "same_original_Frobenius_k_histogram":hist_A,
      "original_ordinary_integer_jet_oracle_coordinate_checks":
           checks_A+checks_B,
      "complete_row_identity_field_chart_covariant":True,
      "original_field_specific_trace_metrics_covariant":True,
      "frozen_9_by_9_normalized_trace_Gram_covariant_mod5_9":True,
      "original_Q_residue_support_transport_mass":support_mass,
      "fixed_Q_row_Z_imag_mismatch_mod5":[1,alpha%5],
      "RAW_support_rank40_does_not_equal_primitive_source_rank":True,
      "no_additional_Smith_factor_or_class_one_field_theorem":True
    },flush=True)
    print("PASS Phase294-B full n725 original normalized p5^9 moving-source covariance",flush=True)

if __name__=="__main__":
    main()
