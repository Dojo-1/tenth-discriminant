#!/usr/bin/env python3
"""Phase307-A/B: entire actual D203 100-row p-adic source, moving frames.

Independent exact omega-coordinate evaluation oracle; Phase304 frozen pilot
only supplies the actual original point set and comparison matrix. No new
class-number theorem or 322^4 bound is claimed.
"""
from collections import Counter
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
for name in ("phase304", "phase305", "phase297"):
    sys.path.insert(0, str(ROOT / "research" / name))
import highjet_d203_original as pilot
from frobenius_hermite_rank import kernel_census
from original_schur_integrality_k16 import high_precision_smith

D, P, K = 203, 5, 5
MOD = P**K
R, S, J = 50, 2, 2
N = R*S
RAW_RANK = 2*J*263


def omega_product(x, y, d, modulus):
    """Independent maximal-order chart, omega^2=omega-(d+1)/4."""
    a, b = x
    c, t = y
    m = (d+1)//4
    return ((a*c-m*b*t)%modulus,
            (a*t+b*c+b*t)%modulus)


def omega_conjugate(z):
    a, b = z
    return a+b, -b


def independent_original_jets(points, d, modulus):
    """Full R*S x (2*J*Q) original ordinary Z-jets, holding W fixed."""
    q = len(points)
    e = np.zeros((N, 2*J*q), dtype=np.int64)
    for i, z in enumerate(points):
        powers = [(1, 0)]
        for r in range(1, R):
            powers.append(omega_product(powers[-1], z, d, modulus))
        w = omega_conjugate(z)
        for r in range(R):
            for s in range(S):
                row = 2*r+s
                for j in range(J):
                    if j > r:
                        continue
                    value = powers[r-j]
                    if s:
                        value = omega_product(value, w, d, modulus)
                    falling = 1 if j == 0 else r
                    column = 2*(j*q+i)
                    e[row, column] = (falling*value[0])%modulus
                    e[row, column+1] = (falling*value[1])%modulus
    return e


def rank_mod5(rows):
    """Standalone plain finite-field Gaussian rank; no pilot rank helper."""
    basis = {}
    for raw in rows:
        v = [int(x)%5 for x in raw]
        for pivot in sorted(basis):
            t = v[pivot]
            if t:
                b = basis[pivot]
                for j in range(pivot, len(v)):
                    v[j] = (v[j]-t*b[j])%5
        pivot = next((j for j, x in enumerate(v) if x), None)
        if pivot is not None:
            inv = pow(v[pivot], -1, 5)
            basis[pivot] = [(z*inv)%5 for z in v]
    return len(basis)


def original_fifty_row_saturation(e):
    """Source Z-unimodular shears, followed by explicit 1/5 superlattice."""
    assert e.shape == (N, RAW_RANK)
    t = np.asarray(e, dtype=object).copy()
    chosen = []
    for r in range(5, R):
        i = 2*r
        # (Z^5-W)Z^(r-5) at original row labels (r,0),(r-5,1).
        t[i, :] = (np.asarray(e[i, :], dtype=object)
                   -np.asarray(e[2*(r-5)+1, :], dtype=object))%MOD
        chosen.append(i)
    for a in range(5):
        i = 2*(45+a)+1
        # Z^(45+a)W -2 Z^(26+a)+Z^(2+a).
        t[i, :] = (np.asarray(e[i, :], dtype=object)
                   -2*np.asarray(e[2*(26+a), :], dtype=object)
                   +np.asarray(e[2*(2+a), :], dtype=object))%MOD
        chosen.append(i)
    assert len(chosen)==50 and len(set(chosen))==50
    assert all(not any(int(v)%5 for v in t[i, :]) for i in chosen)
    prim = t.copy()
    for i in chosen:
        prim[i, :] = np.asarray(t[i, :],dtype=object)//5
    # Each change is an elementary integral row shear. K rows are disjoint
    # from F rows, and F companions are odd indices 1..89 (never K odd91..99).
    return t, prim, set(chosen)


def gram_from_primitives(prim, q, J, modulus):
    return pilot.original_trace_gram(
        np.asarray(prim, dtype=np.int64), q, J, modulus)


def trace_gram_independent_subset(e, q):
    """Independent direct omega trace pairing on 12 named source rows."""
    ids = (0,1,2,3,4,5,48,49,50,51,98,99)
    m = (D+1)//2
    out = {}
    for i in ids:
        for k in ids:
            val=0
            for pos in range(0, e.shape[1], 2):
                a,b=int(e[i,pos]),int(e[i,pos+1])
                c,d=int(e[k,pos]),int(e[k,pos+1])
                val += 2*a*c+a*d+b*c+m*b*d
            out[(i,k)]=val%MOD
    return out


def full_gram_covariance(e, gram, q):
    """Two noncommuting integral moving frames, congruence NOT equality."""
    # Small support elementary row operations on full 100 rows.
    a=np.asarray(e,dtype=object).copy()
    a[0,:] = (a[0,:]+2*a[1,:])%MOD
    a[2,:] = (a[2,:]-a[3,:])%MOD
    b=np.asarray(e,dtype=object).copy()
    b[1,:] = (b[1,:]+b[2,:])%MOD
    # F1 then F2 applied by row changes; reverse order differs.
    ab=a.copy()
    ab[1,:]=(ab[1,:]+ab[2,:])%MOD
    ba=b.copy()
    ba[0,:]=(ba[0,:]+2*ba[1,:])%MOD
    ba[2,:]=(ba[2,:]-ba[3,:])%MOD
    assert not np.array_equal(ab,ba), "source frame generators commute unexpectedly"
    # Gram covariance via separately transformed entries.
    ga=pilot.original_trace_gram(
        np.asarray(a,dtype=np.int64),q,J,MOD)
    gexpected=np.asarray(gram,dtype=object).copy()
    # row0 <- row0+2 row1; row2 <- row2-row3, with untouched partner rows.
    m0=np.asarray(gram,dtype=object)
    gexpected[0,:]=(m0[0,:]+2*m0[1,:])%MOD
    gexpected[2,:]=(m0[2,:]-m0[3,:])%MOD
    gexpected[:,0]=(gexpected[:,0]+2*gexpected[:,1])%MOD
    gexpected[:,2]=(gexpected[:,2]-gexpected[:,3])%MOD
    assert np.array_equal(ga,np.asarray(gexpected,dtype=np.int64))
    assert rank_mod5(a)==rank_mod5(e)
    return dict(noncommuting_frames=True, whole_source_rank_preserved=True,
                exact_100x100_gram_covariance=True)


def split_D211_hostile_control():
    """At split p5, Frobenius need not equal complex conjugation."""
    omega=(0,1)
    z=(1,0)
    for _ in range(5):
        z=omega_product(z,omega,211,5)
    wc=omega_conjugate(omega)
    defect=((z[0]-wc[0])%5,(z[1]-wc[1])%5)
    assert defect!=(0,0), "split-field false control unexpectedly inert"
    return defect


def smith_depth_data(exponents):
    # Each exponent is finite; alpha/aleph indexing does not increase it.
    length=sum(exponents)
    ns=list(range(max(exponents)+3))
    k_values=[sum(min(n,b) for b in exponents) for n in ns]
    layers=[k_values[n+1]-k_values[n] for n in range(len(ns)-1)]
    assert all(layers[n]==sum(b>n for b in exponents)
               for n in range(len(layers)))
    assert sum(layers)==length
    assert layers[-1]==0
    return {"finite_depth_layers":layers,"evaluation_index_log5":length,
            "depth_limit":k_values[-1]}


def main():
    pilot.guard()
    rho,r,s,j,old=pilot.params(D)
    assert (rho,r,s,j,len(old))==(24,R,S,J,127)
    q=pilot.qmax(rho)
    assert len(q)==263
    source=pilot.evaluate_original_jets(q,R,S,J,MOD)
    independent=independent_original_jets(q,D,MOD)
    assert source.shape==(100,1052)==independent.shape
    assert np.array_equal(source,independent),(
        "independent omega oracle does not match original 100-row source")

    census=kernel_census(R,S,J,P)
    assert (census["kernel_dimension"],census["valuationWeight"])==(50,45)
    first_rank=rank_mod5(source)
    assert first_rank==50,("original mod5 evaluation rank",first_rank)

    changed,prim,selected=original_fifty_row_saturation(source)
    assert len(selected)==50 and rank_mod5(prim)==100
    # These checks plus elementary source shears imply exactly 50 unit and
    # 50 valuation-one source evaluation Smith factors (over Z5).
    source_smith={0:50,1:50}
    depth=smith_depth_data([0]*50+[1]*50)
    assert depth["evaluation_index_log5"]==50

    g0=pilot.original_trace_gram(source,len(q),J,MOD)
    gr_direct=trace_gram_independent_subset(independent,len(q))
    assert all(gr_direct[xy]==int(g0[xy]) for xy in gr_direct)
    gm=pilot.original_trace_gram(
        np.asarray(changed,dtype=np.int64),len(q),J,MOD)
    gp=gram_from_primitives(prim,len(q),J,MOD//5)

    # Exact original same-Gram factorization with one index-square factor.
    for i in range(N):
        for k in range(N):
            factor=(5 if i in selected else 1)*(5 if k in selected else 1)
            check_mod=MOD if factor>1 else MOD//5
            assert int(gm[i,k])%check_mod == (
                factor*int(gp[i,k]))%check_mod, (i,k,factor)

    e_levels,e_hist=high_precision_smith(g0,K=K)
    p_levels,p_hist=high_precision_smith(gp,K=K-1)
    assert max(e_levels)<K and max(p_levels)<K-1
    assert e_hist=={0:38,1:12,2:25,3:24,4:1},e_hist
    assert p_hist=={0:63,1:36,2:1},p_hist
    assert sum(e_levels)==138==2*50+sum(p_levels)
    assert rank_mod5(gp)==63 and rank_mod5(prim)==100
    frames=full_gram_covariance(source,g0,len(q))
    split=split_D211_hostile_control()
    print("PHASE307_FULL_SOURCE_SATURATION_PASS",{
        "actual_D203_original_source_shape":[N,RAW_RANK],
        "full_source_independent_omega_coordinate_checks":N*RAW_RANK,
        "full_maximal_order_Q":len(q),"original_J":J,
        "finite_field_source_rank":first_rank,
        "primitive_source_rank_F5":rank_mod5(prim),
        "source_evaluation_smith":source_smith,
        "source_saturation_index_v5":depth["evaluation_index_log5"],
        "source_smith_depth_layers":depth["finite_depth_layers"],
        "primitive_Gram_smith":p_hist,
        "primitive_trace_radical_dimension":100-rank_mod5(gp),
        "primitive_Gram_det_v5":sum(p_levels),
        "original_Gram_smith":e_hist,"original_Gram_det_v5":sum(e_levels),
        "original_Gram_factorization_checked_cells":N*N,
        "original_Gram_independent_trace_oracle_cells":len(gr_direct),
        "moving_frames":frames,"split_p5_D211_control":split,
        "inert_is_not_class_number_one":True,
        "no_new_field_discriminant_bound":True
    },flush=True)


if __name__=="__main__":
    main()
