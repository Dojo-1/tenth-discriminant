# Phase297-D — preregister explicit integral projection on the minimal index-five transverse sublattice

**2026-11-13. AFTER Phase297-C exact focused CI #43375859310 completed SUCCESS, BEFORE this final constructive implementation.** Same source as A/B/C: the full original D587 n730 row lattice, Q383/J=S5/rho53, original integer monomials and ordinary Z-jets with W held fixed, original B=diag(2,1174). Keep all parent helpers and field arithmetic unchanged. No Work mode, no merge and no actual-field cutoff change.

## Frozen facts and new constructive target

Phase297-B checked ALL original old Gram 725 elementary divisors at K16, max v5=14, and proved
- even old363/new2: cross Gram columns already in image of old even Gram over Z5;
- odd old362/new3: cross Gram columns generate exactly `Z/5` inside old odd Gram cokernel.

Phase297-C independently produced an ORIGINAL row functional `ell` of length362 over `Z/5^14` with `ell*A_odd=0` in ALL 362 original columns and
`ell*C_odd=(0,0,4*5^13) (mod5^14)`, with the three new odd rows r145,s0/s2/s4. Witness SHA-256 compact JSON `b09bb9c1a2e40772932c25f8edf984898d2ed3606d7e689e135dab554504815b`. Since the generated cokernel subgroup has order5 and ell restricted to it is nonzero, it is injective on that subgroup. Thus the individual s0,s2 classes vanish; the s4 class generates the entire Z/5 subgroup. This uniquely points to scaling **ONE** original new odd row, `Z^145 W^4`, by p5; the other original four new rows need no scaling.

**Goal:** build deterministic explicit integral solutions T to `A T=C'` modulo 5^16, where C' consists of the **unchanged** original new-row cross pairings except that the original r145,s4 column is multiplied by5. Do this in each C2 parity separately, respecting original Q, jets and metric. These modular T are genuine integral p16 row coefficients on the modified lattice. The exact p-adic existence is a theorem because all old Smith grades <16; the finite T are independently reproducible approximations.

## Original-lattice and module theorem [P-paper]

For the genuine 730-dimensional original row lattice `L`, define the sublattice

```
L' = span_Z5{old original rows r<145,
             new original rows (145,0),(145,1),(145,2),(145,3),
             FIVE TIMES original row (145,4)}.
```

This is a Z5 sublattice of index exactly5 in the original row basis, **not** a GL730(Z5) automorphism of L. Its cross pairing C' satisfies `C' ⊂ A Z5^725`, so one can choose `T∈Mat725×5(Z5)` with `A T=C'`. The change of basis `new'_j → new'_j − sum_i T_ij old_i` is a legitimate integral unipotent row frame on L' (determinant1), and it splits the Gram over Z5 into `A ⊕ S'`, where `S'=D'−C'^T A^{-1}C'`. It is symmetric and integral because all rows and T are integral.

Since row scaling has determinant5, the modified Gram det satisfies
`v5(det G_L') = v5(det G_L) + 2 = 3926`; Schur det valuation `v5(det S')=69+2=71`; by inversion parity even remains28 and odd becomes43. These are **a different index-five lattice's** determinant valuations, not new factors for the ORIGINAL field Gram, whose v5 remains3924. The minimality of index5 follows from the generated cokernel subgroup of order5, so no smaller p-local sublattice of the five new directions can have integral orthogonal projection.

## Preregistered construction/verification gates

1. Freeze source code blobs before tests: `research/phase297/original_schur_integrality_k16.py` `aa3678001c69a7235dca638638d2dab4c55b05b3`; `research/phase297/odd_dual_witness_k16.py` `6b5052e53e15448f37e1b3a52c7ba8cbbcbc63a4`; and all original Phase206/204/292 helper guards. Rebuild ORIGINAL Eraw mod5^16 with the previous 800 exact ordinary-jet checks and six-row original Gram oracle. No synthetic points and no p-adic source normalization substituted for an original row.
2. Independently diagonalize each original old sector Gram A modulo p16 with **tracked simultaneous integral-modular row U and column V transformations**, verifying `U A V = diagonal` modp16 and U,V invertible mod5. The internal Smith column transform V is used ONLY as a linear solver on the SAME ORIGINAL Gram equation; it is **not transported to original observation coordinates or trace metric B**.
3. For each of the five actual original new-row cross columns after scaling only (145,4) by5, solve the diagonal congruences `diag_i * z_i = (U C')_i mod5^16`; require divisibility by each `5^e_i`, choose a deterministic solution z and set `T=V z mod5^16`. Verify **all 725×5 entries** of `A T=C'` modulo5^16 in original row order. Require both parity sectors and original even/odd cross pairings; check no mixing between parity subspaces.
4. Negative control: without scaling (145,4), the odd primitive diagonal source equation must FAIL a divisibility gate (not merely a post hoc histogram). On replacing that column by 5 times itself, the gate must SUCCEED. Check that **all four other new rows** solve WITHOUT scaling. Add a toy A=[10], C=[2] showing unscaled fail and scaled solution exists, and A=[10],C=[5] showing integral already.
5. Record deterministic SHA256 digest of the 725×5 matrix of `T mod5^16` (e.g. JSON row-major), exact module ranks, and full original residual. The determinant of the row transform on L' must be unit1; its inclusion into original L has index5. Do not confuse the two.
6. STOP if old Smith profiles differ from Phase297-B (even sum1930; odd1925; old max grade14), the dual outcome from Phase297-C changes, U A V check fails, any original residual nonzero, any cross parity element nonzero, or an unscaled supposedly integral column fails. Preserve failed CI; do not alter D, p, observations or new-row scaling.

[P-paper] elementary index-five kernel repair and unipotent integral orthogonalization, Schur det under row scaling.
[M after CI] explicit deterministic 725×5 p16 projection coefficients and all-entry original trace Gram/block elimination.
[H] a uniform arithmetic transport for h1-admissible fields and an improved tenth-discriminant cutoff.
[R] presenting the index-five modification as an original lattice gauge or adding its p2 determinant to original 3924.
