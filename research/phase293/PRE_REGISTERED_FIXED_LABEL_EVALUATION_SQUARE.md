# Phase293-D — preregister a decisive fixed-index original-evaluation transport test

**2026-11-12, AFTER explicit primitive pairing GL_363+GL_362(Z/125) isometries passed Phase293-C [#43290487081](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43290487081), BEFORE the following new code/outcomes.** The earlier experiments are preserved. This is a different and stricter question: does the *canonical local field-coordinate transform with the original observation point labels frozen* lift the primitive-pairing isometry to a commutative evaluation square? This does not ask for all arbitrary observation-side isometries.

## Exact proposed square, with row convention and metric orientation

- Source A: complete ORIGINAL D583/R145/S=J5/Q383, 725 row labels, original B_A = diag(2,1166).
- Source B: FIRST725-row **diagnostic** of original D587/R146/S=J5/Q383, original B_B = diag(2,1174); keep all original Q383 and J5 observations. Not the complete original D587 730-row field source.
- Both original sources are inert p5, have OLD F5=1350, secondary source index560, saturated full rank725 and primitive H p5 profile `{0:690,1:35}`. The parity sectors (363 even/362 odd) have explicit pairing isometries mod125 from Phase293-C, but those matrices were NOT selected to match evaluation embeddings.
- The quadratic-order isometry `phi:u587 -> alpha*u583` has `alpha≡67 mod125` and `alpha^{-1}≡28 mod125`. To express A observation values (a,b) in B's imaginary-coordinate chart on the **SAME indexed observation channel**, fix `Y=diag(1,28)` for EACH of the 5*383 original channel pairs. Then EXACTLY `Y B_B Y^T=B_A mod125`. The identity-on-Q-index evaluation square would require some row matrix `X∈GL_725(Z/125)` with `C_B = X C_A Y mod125`; under this hypothesis the primitive metric pairing congruence follows automatically. **This is NOT the physical field isometry's actual point transport** (which maps q to φq), but a deliberately adversarial attempt to freeze the source labels. Do not extend a negative result to all Y.

## Mathematically decisive finite rank test

Split rows into the original C2 parity sectors (363,362) over odd p5. Rebuild the actual original `C_A,prim125` and `C_B,prim125` in the unchanged ORIGINAL observation columns with Phase292 K9 source Smith, tracked row map only, and both field-specific metrics; check all original source helper blob hashes and historical Smith profiles. For each parity:

1. Let `A=(C_A,prim125 * Y) mod125`, `B=C_B,prim125 mod125`. Both have full row rank n mod5. Select **n pivot columns** of A by independent finite-field Gaussian elimination on its row module; those n columns form invertible `A_P`.
2. Compute the unique candidate `X=B_P (A_P)^{-1} mod125`, using an entirely integral modular inverse. This is the UNIQUE row linear map that could satisfy the square on the pivot columns. Verify it reproduces B on pivot columns.
3. Compare `X A` and B on **ALL 3,830** original observation channels modulo5 and modulo125. If even a SINGLE mismatch occurs modulo5, **no row matrix X (invertible or not)** can satisfy this fixed-label Y square modulo5, hence none modulo125 or over Z5. Produce the first witness as (primitive row index, ordinary jet j, original Q point, channel real/imag, expected vs actual residue) and record the exact number of nonzero residual entries. If mod5 matches, test mod125; if all match, require X full rank mod5 and the metric pairing congruence. The outcome is intentionally UNKNOWN beforehand.
4. Check the original mod5 residue-multiplicity transport mismatch: with y→2y mod5, the point-residue multiplicity measures of Q and φQ are different; their L1 half-mass is 104. This independently forbids a simple Q-point permutation compatible with φ, but says nothing about arbitrary dense observation isometries.
5. Exact toy positive control: two independent rows in F5^3 with `A=[[1,0,1],[0,1,1]]`, `B=[[1,1,2],[1,0,1]]` must admit an invertible X. Negative toy `B=[[1,0,2],[0,1,1]]` must give a nonzero residual. A single false positive kills the harness.
6. If a failure occurs, do NOT change α, the source row truncation, choose a favorable observation permutation, alter K or recover a new X from the pairing classification after seeing the outcome. Keep the result as a precise **typed noncommuting square** for this particular Y.

## Evidence and limits

[P-paper] full row-rank pivot candidate equivalence, metric-map identity, odd-p parity direct sum, no-bijection when residue multiplicity distributions mismatch.
[M after CI] existence or obstruction of the fixed-index field-value Y square at p5 and mod125, including exact witness and parity.
[H] any more general original-Q-permuting/jet-mixing observation-side Y, orthogonal-complement extension, original integer GL725(Z) or uniform h1 theorem.
[R] “abstract primitive pairing isometry automatically intertwines the original jet evaluation maps”.
No new prime valuation or source admissibility claim; maintain stacked draft and independent reviews #50/#51.
