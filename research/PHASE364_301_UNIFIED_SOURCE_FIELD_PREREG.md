# Phase364 — SAME original 301^4 source-to-field integration (preregistered)
20 November 2026. RESEARCH ONLY. H UNTIL EXACT HEAD CI AND INDEPENDENT MATHEMATICAL RECONSTRUCTION.

## Fixed source (no substitution)
D : Nat, D >= 301^4 = 8208541201; odd quadratic chart D mod 4 = 3; Squarefree D.
R(D)=floor(D/4), S(D)=floor(R(D)/25), J=S.
thinRadius=ceil((11/25)D^(3/4)); padded rho=ceil((13/25)D^(3/4)).
Qthin = complete ellipsePairs D (thinRadius D).
G_D = integerRectangularTraceGram Qthin D S R S, using ORIGINAL ordinary Z jets holding W fixed, row-major R x S, weights (2,2D). No other Gram or selected minor.
g_D = log(det G_D)/comparisonScale(R,S), comparisonScale=R^2 S.
Padded ellipse supplies cardinality majorant ONLY.

## Independent source ingredients copied without modification
- Phase362 #272 upper: g_D <= (4/5) log D - 4821/5000; precise original Qthin and G_D.
- Phase363 #274 lower: L(D) <= g_D under Squarefree D, odd chart, class-number-one, det G_D>0; specialize Q to exactly Qthin.
- Phase362 original Gram positivity at new 301 domain.
- Phase361 #270 scalar strict U_301(D) < L(D) for all D>=301^4.
- Phase359 #267 field chart transport, unchanged in mathematical structure but NEW 301 application must be freshly checked.

Both Phase362/363 share identical Phase362Dimensions301 blob SHA e7928ea5966749139e2686fddeaf1d1b07765310. Phase363 source files are copied byte-for-byte from ac8123f91540fb2d12a40fdde086dd379daa192e.
Phase364Field301Candidate is explicitly a NEW theorem attempt, NOT automatically proved by importing checked modules on separate branches.

## Predictions and falsifiers
Prediction (H): there is an exact-head Lean theorem odd_large_classNumber_ne_one_301; then odd/even maximal-order chart and actual NumberField.discr transport provide a conditional encoded strict 301^4 field theorem.
Kill if: missing import or incompatible Q/J/R/S, incorrect comparisonScale, unknown/transitively disallowed axioms, hidden 302-only domain, proof-escape, failing known-false controls, wrong conductor factor, inability to reconstruct prime valuations / field chart, or integer-Gram substitution.
Scalar endpoint cross-check: at D=301^4, L-U approximately +0.00168688585618 [M, high-precision numerical check only]. The classical OLD 301 fixed upper -1923/2000 still fails (negative control); the new result requires Phase361's -4821/5000.

## Verification / publication boundary
1. Dedicated exact-head focused lake build of Phase364Field301Candidate and print transitive axioms.
2. Full-root lake build, source-to-certificate audit, known-false-proof controls on exact new head.
3. Verify both original Phase362/363 separate full-root jobs have succeeded at original heads (their focused jobs are green).
4. Independently reconstruct full source valuations, original weighted Gram Hadamard, odd/even maximal-order chart and actual field discriminant transport. Review issue #50 stays OPEN.
5. Do NOT merge this or underlying work into public main from Lean CI alone. Public main still states strict 322^4. No new Siegel-zero conclusion. E30/E31 conductor counterexample keeps additional p-adic factors out.

Status: P only for dependencies already freshly checked. Phase364 as combined statement H pending this new head's CI; intended mathematical semantics H independent review.
