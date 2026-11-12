#!/usr/bin/env python3
"""Phase281 fixed K=3 D403 full-row Smith test. No primitive H claim.

Mathematical source, stop rules and outcomes are governed by
PRE_REGISTERED_D403_K3.md committed at 2d049a2 BEFORE this program.
All results are finite; no uniform class-number-one/discriminant theorem.
"""
from math import comb
from pathlib import Path
import subprocess
import sys
import numpy as np

THIS = Path(__file__).resolve()
RESEARCH = THIS.parents[1]
for mod in ("phase280", "phase207", "phase206", "phase204"):
    sys.path.insert(0, str(RESEARCH / mod))

from source_probe import params, fall, mul, rank_mod
from middle_frobenius import old_k, pair_powers, source_dualjet
from ordinary_jet_filtration import jet as integer_jet
from full_d403_second_layer import first_two_smith, vec_rank

D, R, S, J, POINTS, N, M, K = 403, 100, 4, 4, 219, 400, 1752, 3
OLD_F = {3: 570, 5: 550, 11: 0}
FULL_K2 = {3: {"0": 90, "1": 36, ">=2": 274},
           5: {"0": 240, "1": 15, ">=2": 145},
           11: {"0": 132, "1": 66, ">=2": 202}}
SUBSET_K2 = {3: {"0": 54, "1": 18, ">=2": 116},
             5: {"0": 120, "1": 15, ">=2": 45}}
DROP_J3 = {3: 81, 5: 180, 11: 99}

# Git blob identities of the unchanged original source and pilot oracles.
# Reject changes to imports instead of silently switching experiments.
SOURCE_BLOBS = {
    "research/phase280/full_d403_second_layer.py": "7abffdf4f4916dacef08ebe097e5eed700837ad4",
    "research/phase206/source_probe.py": "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase207/middle_frobenius.py": "f4df80ec6fc6d16a20be717aeb3c8ff135f16a3c",
    "research/phase204/ordinary_jet_filtration.py": "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}

def check_source_blobs():
    root = THIS.parents[2]
    for path, expected in SOURCE_BLOBS.items():
        got = subprocess.check_output(
            ["git", "rev-parse", "HEAD:" + path], cwd=root, text=True
        ).strip()
        assert got == expected, (path, got, expected)
    print("PASS source git-blob freeze", flush=True)


def field_type(p):
    val = (-D) % p
    assert val != 0, "ramified prime unexpectedly used"
    return "split" if val in {x*x % p for x in range(p)} else "inert"


def original_normalized_source(p, Q):
    """Construct original ordinary-jet source to K=3 after old frame ONCE.

    To divide by p^k and retain K digits, compute original numerator modulo
    p^(K + max k), not merely modulo p^K. This is exact integer modular
    arithmetic; no floating-point or Hasse derivative substitution.
    """
    inert = field_type(p) == "inert"
    assert inert == (p in (3, 5))
    max_k = S-1 if inert else 0
    q = p ** (K + max_k)
    red = p ** K
    cache = []
    for x, y in Q:
        z = (x % q, y % q)
        w = (x % q, (-y) % q)
        cache.append((pair_powers(z, R, q),
                      pair_powers(w, S-1, q)))
    C = np.zeros((N, M), dtype=np.int64)
    f = 0
    for r in range(R):
        for s in range(S):
            k = old_k(r, s, p) if inert else 0
            f += k
            divide = p**k
            i = r*S+s
            for j in range(J):
                for qi, (zp, wp) in enumerate(cache):
                    real = imag = 0
                    for t in range(k+1):
                        a = r-p*t
                        if a < j:
                            continue
                        zprod = mul(zp[a-j], wp[s+t], D, q)
                        c = (-1 if t & 1 else 1)*comb(k, t)*fall(a, j)
                        real = (real+c*zprod[0])%q
                        imag = (imag+c*zprod[1])%q
                    assert real%divide == 0 and imag%divide == 0, (
                        "nonintegral Frobenius quotient", p, r, s, j, qi)
                    col = 2*(j*len(Q)+qi)
                    C[i, col] = (real//divide) % red
                    C[i, col+1] = (imag//divide) % red
    assert f == OLD_F[p], (p, f, OLD_F[p])
    return C, q


def smith_profile_k3(mat, p):
    """Exact rectangular elementary-divisor profile, censored at exponent 3.

    Unit-pivot row/column operations are confined to Smith computation.
    They are NEVER used to alter the signed trace metric in the Gram.
    """
    mod = p**K
    A = np.array(mat, dtype=np.int64, copy=True) % mod
    n = A.shape[0]
    hist = []
    for level in range(K):
        t = 0
        while t < min(A.shape):
            loc = None
            for j in range(t, A.shape[1]):
                ix = np.flatnonzero(A[t:, j] % p)
                if ix.size:
                    loc = (t + int(ix[0]), j)
                    break
            if loc is None:
                break
            i, j = loc
            if i != t:
                A[[t, i]] = A[[i, t]]
            if j != t:
                A[:, [t, j]] = A[:, [j, t]]
            pivot = int(A[t, t])
            assert pivot % p != 0
            inv = pow(pivot, -1, mod)
            if t+1 < A.shape[0]:
                factors = (A[t+1:, t]*inv) % mod
                A[t+1:, t+1:] = (
                    A[t+1:, t+1:] - factors[:, None]*A[t, t+1:]
                ) % mod
                A[t+1:, t] = 0
            t += 1
        hist.append(t)
        A = A[t:, t:]
        if level < K-1:
            assert np.all(A % p == 0), ("bad Smith-tail division", p, level)
            A = A // p
            mod //= p
    assert sum(hist) <= n
    return {"0": hist[0], "1": hist[1], "2": hist[2],
            ">=3": n-sum(hist)}


def toy_controls(p):
    T = np.diag([1,p,p*p,p*p*p]).astype(np.int64)
    expected = {"0": 1, "1": 1, "2": 1, ">=3": 1}
    assert smith_profile_k3(T, p) == expected
    T[0] += T[1]
    T[:, 1] += T[:, 0]
    assert smith_profile_k3(T, p) == expected
    assert smith_profile_k3(T[:, ::-1], p) == expected


def source_oracles(C, p, Q, q):
    """Independent exact jets and a dual-number polynomial on frozen probes."""
    selected = [(0,0), (1,3), (p,0), (2*p,0),
                (50,1), (99,0), (99,3)]
    if p in (3,5):
        selected += [(3*p,0), (2*p,1)]
    selected = sorted(set((r,s) for r,s in selected if r<R))
    mod = p**K
    for r,s in selected:
        k = old_k(r,s,p) if p in (3,5) else 0
        for qi in (0, len(Q)//2, len(Q)-1):
            x,y = Q[qi]
            for j in range(J):
                real = imag = 0
                for t in range(k+1):
                    rr = r-p*t
                    if rr < j:
                        continue
                    z0,z1 = integer_jet(D,rr,s+t,j,(x,y))
                    coeff = (-1 if t&1 else 1)*comb(k,t)
                    real += coeff*z0
                    imag += coeff*z1
                assert real % p**k == imag % p**k == 0
                col = 2*(j*len(Q)+qi)
                assert (int(C[r*S+s,col]), int(C[r*S+s,col+1])) == (
                    (real//p**k)%mod, (imag//p**k)%mod), (
                        "exact-jet oracle mismatch", p,r,s,j,qi)
            if k:
                z = (x%q, y%q)
                w = (x%q, (-y)%q)
                jets = source_dualjet(z,w,r,s,k,p,q)
                for j in range(J):
                    orig = [0,0]
                    for t in range(k+1):
                        rr = r-p*t
                        if rr<j:
                            continue
                        za,zb = integer_jet(D,rr,s+t,j,(x,y))
                        c = (-1 if t&1 else 1)*comb(k,t)
                        orig[0] += c*za
                        orig[1] += c*zb
                    assert tuple(v%q for v in orig) == tuple(
                        int(v)%q for v in jets[j]), (
                            "dual-number jet mismatch",p,r,s,j,qi)
    return len(selected)


def main():
    check_source_blobs()
    rho, r0, s0, j0, Q = params(D)
    assert (rho,r0,s0,j0,len(Q)) == (40,R,S,J,POINTS)
    assert 2*len(Q)*J == M
    assert (-D)%3 == 2 and (-D)%5 == 2 and (-D)%11 == 4
    assert len({(r,s) for r in range(R) for s in range(S)}) == N
    for p in (3,5,11):
        toy_controls(p)
        C,q = original_normalized_source(p,Q)
        assert C.shape == (N,M)
        oracle_count = source_oracles(C,p,Q,q)
        mod = p**K
        full2 = first_two_smith(C%(p*p),p)
        assert full2 == FULL_K2[p], (p, full2, FULL_K2[p])
        full3 = smith_profile_k3(C,p)
        assert full3["0"] == full2["0"]
        assert full3["1"] == full2["1"]
        assert full3["2"] + full3[">=3"] == full2[">=2"]
        r = vec_rank(C%p,p)
        assert r == full3["0"] == rank_mod((C%p).tolist(),p)
        rows = [(r0,s0) for r0 in range(R) for s0 in range(S)]
        subset = None
        if p in SUBSET_K2:
            ids = [r0*S+s0 for r0,s0 in rows if old_k(r0,s0,p)>=2]
            subset = first_two_smith(C[ids]%(p*p),p)
            assert subset == SUBSET_K2[p], (p,subset,SUBSET_K2[p])
        # ORIGINAL signed trace metric, untouched by Smith column operations.
        w = np.tile(np.array([2,2*D],dtype=np.int64),J*len(Q))
        A = C%p
        G = ((A*(w%p))@A.T)%p
        assert np.array_equal(G,G.T)
        grank = vec_rank(G,p)
        assert grank == rank_mod(G.tolist(),p) and grank<=r
        drop = vec_rank(A[:,:2*(J-1)*len(Q)],p)
        assert drop == DROP_J3[p], (p,drop,DROP_J3[p])
        assert 2*D%p != 0
        if p==11:
            assert 2*D%p != 2%p, "Euclidean metric false comparator collapsed"
        T = C.copy()
        T[0] = (T[0]+T[-1])%mod
        assert smith_profile_k3(T,p) == full3, "unimodular row-shear failure"
        assert smith_profile_k3(C[:,::-1],p) == full3, "column reversal failure"
        index_lower = full3["1"] + 2*full3["2"] + 3*full3[">=3"]
        assert index_lower <= K*N
        print("FULL_D403_PHASE281_K3",{
            "D":D,"p":p,"splitting":field_type(p),"R":R,"S":S,"J":J,
            "point_count":len(Q),"source_shape":C.shape,
            "source_modulus":q,"old_F_once":OLD_F[p],
            "K3_histogram":full3,
            "K2_replay":full2,"Phase208_subset_K2_replay":subset,
            "eval_index_lower_capped3":index_lower,
            "conditional_original_Gram_vp_lower":2*(OLD_F[p]+index_lower),
            "rank_C_modp":r,"rank_original_Gram_modp":grank,
            "unsaturated_image_radical_NOT_ADDITIVE":r-grank,
            "rank_without_j3_WRONG_SOURCE":drop,
            "oracle_row_count":oracle_count,
            "primitive_pairing_NOT_computed":True,
            "exact_total_determinant_valuation_NOT_computed":True,
        },flush=True)
    print("PASS Phase281 D403 fixed K3: 3 matched primes, full original signed source",flush=True)

if __name__ == "__main__":
    main()
