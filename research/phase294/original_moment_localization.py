#!/usr/bin/env python3
"""Phase294-B: localize the 6x6 original trace-Gram transport remainder.

All ORIGINAL ordinary Z-jets, W frozen, full Q383 and original B.
The transported Q is a FORMAL p-adic source diagnostic, never the
original number-field source. Pre-registered 97821fec before code.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase206"))
sys.path.insert(0,str(ROOT/"research"/"phase294"))
from source_probe import params,mul,fall,gram,rank_mod
from support_debt_tower import (
    source_guard,hensel_lifts,matching_by_residue,debt_from_counters,
    residue_counter
)

D_A,D_B=583,587
P=5
J=5
LABELS=((0,0),(1,0),(2,0),(1,1),(4,0),(4,1))

def pow_pair(z,k,D,mod):
    t=(1,0)
    for _ in range(k):t=mul(t,z,D,mod)
    return t

def original_ordinary_jets_at_point(D,q,mod):
    """Six source rows, five ORIGINAL Z jets, both real/imag channels."""
    z=(q[0]%mod,q[1]%mod)
    w=(q[0]%mod,(-q[1])%mod)
    values=[]
    for r,s in LABELS:
        row=[]
        for j in range(J):
            if j>r:row.append((0,0));continue
            zpower=pow_pair(z,r-j,D,mod)
            wpower=pow_pair(w,s,D,mod)
            a,b=mul(zpower,wpower,D,mod)
            coeff=fall(r,j)
            row.append(((coeff*a)%mod,(coeff*b)%mod))
        values.append(row)
    return values

def local_metric_trace_matrix(D,q,mod):
    E=original_ordinary_jets_at_point(D,q,mod)
    n=len(E)
    out=[[0]*n for _ in range(n)]
    for i in range(n):
        for t in range(n):
            s=0
            for j in range(J):
                ai,bi=E[i][j]
                at,bt=E[t][j]
                s+=2*ai*at+2*D*bi*bt
            out[i][t]=s%mod
    assert all(out[i][j]==out[j][i] for i in range(n) for j in range(n))
    return out

def matrix_diff(A,B,mod):
    """A - B modulo the original prime power."""
    return [[(x-y)%mod for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]

def add_signed_in_place(A,B,mod,sign):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j]=(A[i][j]+sign*B[i][j])%mod

def independent_source_oracle(D,q,mod):
    ref=gram(D,[q],J,LABELS)
    own=local_metric_trace_matrix(D,q,mod)
    assert all(ref[i][j]%mod==own[i][j]
               for i in range(len(LABELS)) for j in range(len(LABELS)))
    return True

def main():
    source_guard()
    _,ra,sa,ja,Qa=params(D_A)
    _,rb,sb,jb,Qb=params(D_B)
    assert (ra,sa,ja,len(Qa))==(145,5,5,383)
    assert (rb,sb,jb,len(Qb))==(146,5,5,383)
    assert Qa==Qb and ja==jb==J
    Q=Qa
    ga=gram(D_A,Q,J,LABELS)
    gb=gram(D_B,Q,J,LABELS)
    assert gb[1][1]-ga[1][1]==4272
    assert rank_mod(matrix_diff(gb,ga,5),5)==5
    results=[]
    for k,mod,alpha in hensel_lifts(3):
        assert k in (1,2,3)
        assert (D_A*alpha*alpha-D_B)%mod==0
        transformed=[(x,alpha*y) for x,y in Q]
        formal=gram(D_A,transformed,J,LABELS)
        # This checks every ORIGINAL row-pair and every original jet
        # through an independent exact source routine.
        assert all((gb[i][j]-formal[i][j])%mod==0
                   for i in range(6) for j in range(6))
        pairs,ua,ub=matching_by_residue(Q,alpha,mod)
        debt,matched=debt_from_counters(
            residue_counter(Q,mod),
            residue_counter(Q,mod,alpha))
        assert len(pairs)==matched and len(ua)==len(ub)==debt
        assert debt==(104 if k==1 else 276)

        # All matched point original *RAW* ordinary polynomial jets
        # agree modulo m; no division by old/secondary p powers here.
        for i,j in pairs:
            x=original_ordinary_jets_at_point(D_A,Q[i],mod)
            y=original_ordinary_jets_at_point(D_A,transformed[j],mod)
            assert x==y,("matched original jets differ",k,i,j)

        residual=[[0]*6 for _ in range(6)]
        for i in ua:
            add_signed_in_place(
                residual,local_metric_trace_matrix(D_A,Q[i],mod),mod,-1)
        for j in ub:
            add_signed_in_place(
                residual,local_metric_trace_matrix(D_A,transformed[j],mod),
                mod,+1)
        original_difference=matrix_diff(gb,ga,mod)
        assert original_difference==residual,(
             "original Gram remainder localization failed",k)
        # Independently replay actual original-moment output on
        # single support points, both unchanged and formally moved.
        for point in (Q[0],Q[len(Q)//2],Q[-1],
                      transformed[0],transformed[-1]):
            assert independent_source_oracle(D_A,point,mod)

        digest=sha256(json.dumps(
            residual,separators=(",",":")
        ).encode()).hexdigest()
        results.append({
            "prime_power_exponent":k,"modulus":mod,"alpha":alpha,
            "original_source_points_each":len(Q),
            "maximum_matched_point_pairs":matched,
            "unmatched_signed_original_sample_summands_per_side":debt,
            "signed_original_moment_summands_total":2*debt,
            "original_six_by_six_Gram_difference_rank_mod5":
                rank_mod(original_difference,5),
            "all_36_original_Gram_entries_localized":True,
            "all_matched_original_raw_jets_congruent":True,
            "independent_original_point_Gram_oracle_passes":True,
            "signed_remainder_sha256":digest,
            "no_primitive_valuation_or_psd_claim":True,
        })
    assert [r["maximum_matched_point_pairs"] for r in results]==[
        279,107,107]
    assert [r["signed_original_moment_summands_total"] for r in results]==[
        208,552,552]
    print("PHASE294_ORIGINAL_MOMENT_LOCALIZATION",{
        "source_types":"full original D583 n725 vs full original D587 n730; six common rows only",
        "original_rows_tested":[list(t) for t in LABELS],
        "all_original_jets":J,
        "original_Q":len(Q),
        "original_metric_D583":"2,1166",
        "original_metric_D587":"2,1174",
        "layers":results,
        "original_identity_frame_Z_diagonal_defect":4272,
        "original_six_by_six_difference_rank_mod5":5,
        "formal_transformed_Q_is_not_original_field_source":True,
        "no_h1_or_uniform_discriminant_theorem":True
    },flush=True)
    print("PASS Phase294-B original-jet matrix remainder localized on unmatched p-adic samples",
          flush=True)

if __name__=="__main__":
    main()
