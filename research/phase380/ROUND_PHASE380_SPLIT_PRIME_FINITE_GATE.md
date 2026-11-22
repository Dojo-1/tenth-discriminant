# Phase380 — finite split-prime gate, independent of analytic cutoff
**22 November 2026 · AI-assisted draft · not a proof of RH or a stronger cutoff**

## Scope and result
This phase preserves the original trace-Gram line and the Phase378/379 analytic branch. Assuming the **external** conditional analytic implication `ZF(7/8) and h(K)=1 => |disc(K)|<=652`, establish the finite classification by a *different elementary obstruction*: small split rational primes. No Heegner classification is used in the enumeration, though standard quadratic ideal and reduced-form theorems remain imported mathematics.

**Finite result (local Python run):** in `1<=d<=652` exactly 199 integers have `-d` negative fundamental discriminant. For 190 a split prime `p<=31` has norm too small to be principal; the remaining nine are `3,4,7,8,11,19,43,67,163`. The independent verifier also enumerates primitive reduced positive-definite binary quadratic forms and counts one reduced class for exactly those nine, **assuming the standard Gauss correspondence** between reduced classes and ideal class groups.

## Elementary mathematical lemma
For `D=-d<0` fundamental, let `p` be split in `K=Q(sqrt D)`. If `h(K)=1`, a prime ideal above `p` is principal with generator of norm `p`.

If `d` is odd (`d==3 mod 4`), the integer norm is
`Q(x,y)=x²+xy+((d+1)/4)y²=(x+y/2)²+(d/4)y²`.
If `y=0`, its norm is a square and cannot equal prime `p`; for odd `y`, the half-integral square is at least `1/4`; for even nonzero `y`, `y²>=4`. Therefore `p>=(d+1)/4`.

If `d` is even, `D=4m` with `m==2 or 3 mod 4`. Then
`Q(x,y)=x²+(d/4)y²`; for prime `p`, `y!=0`, hence `p>=d/4`.

**Consequently:** a split `p` with `4p<d+1` for odd `d`, or `4p<d` for even `d`, forces `h(K)>1`.

The strict bounds cannot be changed into non-strict ones: for `d=163`, `p=41` is split and `4p=d+1`, consistent with the principal norm form `(1,1,41)`.

## Verification and limits
`split_prime_certificate.py`: pure-Python integer producer, tests splitting by Euler criterion for odd primes and discriminant mod 8 at 2. Its exact output in the local run:
- fundamental discriminants: **199**
- excluded by split-prime obstruction: **190**
- largest witness: **31**
- remaining: **3,4,7,8,11,19,43,67,163**
- prime-witness counts for p=2,3,5,7,11,13,17,19,23,31: **67,48,31,18,10,7,3,2,3,1**.

`verify_split_prime_witnesses.py`: separate self-contained implementation, trial-factorization discriminant detection, splitting by direct modular-square residue enumeration, independent reduced-form count. Its acceptance asserts all numbers above and the positive reduced-form result.

Run:
```sh
python3 research/phase380/split_prime_certificate.py
python3 research/phase380/verify_split_prime_witnesses.py
```

The producer and verifier were both exercised locally; this draft does **not** claim a Lean build, Prolog execution, independently refereed classification, or a new zero-free theorem. Proof status is **M for bounded exact computation**, **P conditional on classical quadratic-arithmetic correspondences** for the split-prime implication, and **A** for the Phase379 analytic cutoff. An independent proof of the original trace-Gram source-to-field return remains outstanding at issue #50.

## Research line interfaces
- **Tao discriminant:** the new finite gate completes the classification *under the previously imported 7/8 zero-free and Epstein hypotheses*. It does not improve the 652 bound or the original independent integer trace-Gram public 322^4 bound.
- **Alpöge / Dirichlet GRH:** precisely extract nonvanishing for primitive quadratic characters at real `s in (7/8,1)`; formal verification of a larger RH theorem does not verify our use of the character or its analytic normalization.
- **Masullo:** retain two explicit invalid trace-operator identities and the incomplete Hecke divisor theorem as distinct audit targets; do not import his zero-freeness as a premise.
- **Conductor–Zero:** PR #12 was merged on 21 Nov 2026. Euler factors preserve zeros **with multiplicities** only in the stated open right half-plane; the boundary requires separate analysis.
- **Ihara / Selberg:** an off-circle Ihara pole from `|lambda|>2sqrt q` is a different spectral phenomenon, with no general implication from quadratic GRH.
- **Original determinant:** issue #50 remains open. PR #289 is stacked on #288; Phase380 is stacked on #289 rather than silently modifying main or the determinant approach.

## Next gates
1. Formalize split-prime obstruction and its actual number-field interpretation in Lean, without placeholder axioms, and compare with the ordinary proof.
2. Formalize the Epstein/Poisson normalization and exact rational envelope rather than mistaking Python assertions for analytic continuation.
3. Independently reconstruct one original trace-Gram source-to-field return to address issue #50.

**Authorship:** AI-assisted proof exposition and finite test design; locally executed integer scripts; no human peer review claimed.
