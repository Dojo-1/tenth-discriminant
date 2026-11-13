# Phase310-C — post-B full original rank certificate and source-index determinant floor

Date 2026-11-13. Written AFTER Phase310-B finite depth10 split-Hensel results were observed on hosted CI (D203/p3, local histograms equal, 46/100 source factors and 65/100 Gram factors censored). The following predictions and controls are frozen BEFORE C code.

## Mathematical problem being solved

We know on the exact same ORIGINAL 100-row D203 trace Gram:

    G=2 X0 P_tau X0^T over Z_3

with X0 an integral 100x526 split-prime local source and P_tau an involutive unimodular 526x526 permutation. Phase310-B computed a *censored lower bound* on the local Smith exponent sum, sum_i b_i>=658, but did not certify K-rank100 over the local 3-adic fraction field. We must not claim the stronger bound v3(det G)>=2*658 without independently certifying that X0 has full row rank and G has nonzero determinant.

### Predeclared independent nonvanishing certificate

At rational prime ell=101, f(T)=T²-T+51 splits at simple roots r=46 and 56. This is **not the p3 source index prime**; it is a separate good reduction prime used solely to prove an original evaluation map minor is NONZERO. Evaluate the unchanged 100x1052 ORIGINAL D203 source modulo101, project O→F101 via omega→r for both roots, and perform rank-revealing modular elimination on the 100x526 resulting matrix. Prediction: rank100 at both roots. Record 100 pivot columns and independently compute the 100x100 pivot submatrix determinant modulo101; prediction: nonzero.

A single such nonzero minor of the O_K evaluation over F101 proves the original K-linear evaluation has full row rank100. After embedding K in Q_3 at the simple split p3 root, X0 has full row rank over Q_3. The associated original positive Hermitian trace form is **positive definite over the complex embedding**, hence det G is a positive nonzero integer.

Negative controls: duplicate one original source row to reduce modular rank to99; wrong root must be rejected; verify ALL 105,200 unchanged original-source coordinates against a genuinely separate omega ring evaluator modulo101, and verify the original source observations and jets are unchanged.

### Promoted conditional arithmetic bound

For full-rank X0 over Z_3, Smith form gives U X0 V = [D|0], D=diag(3^b_i), with U,V invertible over Z_3. Inserting into original G=2 X0 P X0^T gives

    v3(det G) >= 2 sum_i b_i >= 2*658 = 1316.

The middle 100x100 factor from V P V^T has coefficients in Z_3, hence integral determinant; the inequality holds if det G !=0. Report this as [P-paper+M certificate] for THIS D203 fixed original source, not as a uniform field theorem. It may overlap the known valuationWeight lower bounds and must not be added to them. If modular rank100 fails at ell101, try **predeclared** ell ∈{109,113,127,131,137,149} for a split root only; preserve which candidate failed and do not claim 101 succeeded. No unbounded cherry-picking.

## Stop rule

If no tested ell gives full row rank with a nonzero determinant minor, retain only Phase310-B censored profile; do not promote the source-square lower bound or claim original Gram nonvanishing. No changes to full original source, existing 322^4 bound, main branch, or whole-root proof semantics.
