# Phase293-C — preregister explicit primitive pairing transport modulo 125

**2026-11-12. AFTER Phase293-B focused CI PASS [#43289725529](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43289725529), BEFORE Phase293-C code/results.** This is a new constructive calculation, but uses the SAME previously recorded original source helpers and full primitive saturation data. It is not independent peer review. No change to the observational support or actual-field branches.

## Observed premise, frozen before construction

Two objects: the COMPLETE original D583 p5 primitive trace pairing on 725 original rows, versus the p5 primitive pairing on the FIRST 725 original rows of D587 with its unchanged full original Q383 and B587. The latter remains a **row-restricted diagnostic**, not the full D587 number-field source. Both full original row sets have **same old Frobenius index 1350, secondary source index560, original Gram v5=3855**. They are NOT identified by a rational/integer number-field chart.

Phase293-B computed full primitive odd-prime central-inversion sector invariants:

| sector | p^0 primitive Jordan component | p^1 primitive Jordan component |
|---|---|---|
| even 363 rows | rank345, det unit Legendre +1 | rank18, det unit Legendre -1 |
| odd 362 rows | rank345, det unit Legendre +1 | rank17, det unit Legendre +1 |

These are the SAME on D583 and D587-725 diagnostic, with no p^2 or p^3 residual levels; this is now a retrospective construction target, not a fresh prediction. The classical odd-p Jordan classification implies an **abstract Z5 pairing isometry** exists in each parity. Construct an explicit finite witness modulo 5^3 =125, and verify it entry-by-entry; do not assume an explicit original evaluation/source transport follows.

## Exact constructive algorithm [P-paper; to be instrumented]

1. Rebuild and independently saturate each source's EVEN 363 and ODD 362 original rows using the FROZEN Phase292 K9 source Smith and Phase293-B original observation columns. Keep original ordinary j0..4, Q383, and B_D=diag(2,2D), no permutations of the ORIGINAL observation channel lattice, no extra p-local factors.
2. For each primitive symmetric H mod125, use a **new tracked unimodular CONGRUENCE** Jordan diagonalizer `T H T^T = diag(5^e u)` over Z/125: choose minimum-valuation diagonal pivots, expose a diagonal by simultaneous `e_i->e_i+e_j` if only a unit offdiagonal exists, eliminate cross terms with simultaneous row/column shears, and record T mod125. Verify T is invertible mod5, full exact congruence and match the prior independent Phase293-B Jordan ranks and Legendre signs.
3. Pair source and target Jordan components grade by grade. For diagonal unimodular blocks `diag(a_i)`, `diag(b_i)` over Z/125 (for grade p^1 these are arbitrary lifts of the unit classes mod25), construct a fully explicit `S` with `S diag(a) S^T=diag(b) mod125`. In rank >=2, choose x,y mod5 with `a x²+c y²=b mod5`, Hensel-lift one unit coordinate to mod125, then the unimodular 2x2 row change
   `[[x,y],[-c*y,a*x]]` sends `diag(a,c)` to `diag(b,a*c*b)`. Match n-1 target diagonals recursively; the final quotient b_last/a_last has square residue by the prior grade determinant-class check, so Hensel-lift a square root and scale last row. Explicitly verify each block congruence and rank mod5. Grade e1 only requires congruence after multiplying by 5 modulo125; constructing the lifted unit-level congruence modulo125 is a stronger sufficient check.
4. Assemble parity-sector S as block-diagonal in the Jordan grade ordering and compute `X=T_target^{-1} S T_source mod125`. Require `rank_F5(X)=n_sector` AND `X H_source X^T = H_target mod125` entry-by-entry on the full 363x363 and 362x362 matrices. Build a deterministic SHA-256 of the integer-residue matrix X (after checking, no huge artifact required) for reproducibility; do not claim a Z-integral 725x725 gauge, only **GL_n(Z/125)** pairing congruence. No identity on C/E/Q is claimed.
5. Re-check the previously proven fact that original fixed-support row-Z Gram entries differ by 4272 (p5 unit) and that local field isometry moves 104 points outside original Q. These prove the construction cannot simply be reinterpreted as the obvious identity-frame/source-permutation transport.
6. Negative controls: rank-one `<1>` vs `<2>` have equal Smith but opposite p5 unit signs and MUST FAIL unit-block matching; matching rank-2 `<1,1>` vs `<2,2>` MUST CONSTRUCT an explicit invertible mod125 congruence; a mixed-grade diag `<1,2,5,10>` vs permuted `<2,1,10,5>` must also succeed. On failure, retain output and diagnose; do NOT fit a new source, prime or precision.

**[P-paper]** existence of Z5 isometry conditional on Jordan symbols, integral odd-p binary norm representation + Hensel lift, exact congruence identities.
**[M after CI]** an explicit 363+362-dimensional mod125 pairing isometry with reproducible digests.
**[H]** a compatible map of the original evaluation lattices, original Q observations, and D583/D587 fields, or any uniform h1 discriminator.
**[R]** using an abstract mod125 primitive-pairing isometry as an uncounted new valuation of an original Gram or as a GL_n(Z) moving frame.
Keep PR draft/stacked, independent source-to-field human review #50/#51 and root Lean separate.
