# Phase362 — rebuild the SAME original integer-Gram analytic upper at 301^4
20 November 2026. Frozen before constructing the new Lean proof modules. RESEARCH ONLY.

## Object and target

Fix all original definitions:
- natural D, R=floor(D/4), S=floor(R/25), t=D^(1/4);
- thinRadius=ceil((11/25)t^3), padded rho=ceil((13/25)t^3);
- Qthin = complete original integer ellipse x²+Dy²<=thinRadius²;
- original ordinary-Z jets holding W fixed, order J=S, row-major rectangle R×S;
- original trace pairing (2,2D) and integerRectangularTraceGram G_D;
- comparisonScale(R,S)=R²S. The padded ellipse is used ONLY for the number-of-points majorant.

**Theorem target** for every D≥301⁴:

$$
\frac{\log\det G_D}{R(D)^2 S(D)}
\le \frac45\log D-\frac{4821}{5000}.
$$

This is an ANALYTIC upper of an unchanged original Gram, not a 301 field cutoff. The constant is exactly

$$
815/1000 + 1377/10000 + 23/2000 = 4821/5000.
$$

## Dependencies / predictions / controls

1. The 14⁴ original ellipse count and integer-Gram positivity (Phase354) imply both source rank and padded-count positivity for the new 301 domain.
2. Reprove 301 dimensions and log(R) floors; do not reuse any assertion conditional on D>=302⁴.
3. The 301 original padded radius satisfies R >= 75 t³, rho <=521/1000*t³, rho/R<=521/75000, with the exact ceil convention and full arbitrary-integer domain.
4. Reprove the original padded Ender upper:
   enderUpperB(R,S,S,rho, ellipsePaddedUpperCount(D,rho,Y))/comparisonScale(R,S)
   <= (4/5) log D - 815/1000
   for all D>=301⁴. A finite D=301⁴ source-faithful numerical check showed slack ≈0.00312 but is M ONLY.
5. Apply Phase361's exact-head Lean checked stronger original 847/1000 radius ratio, gaining 1377/10000; apply existing TightRadialSaving normalized_integer_upper_tight to SAME Qthin, gaining 23/2000.
6. Explicit negative controls remain: the old Phase355 fixed-upper scalar gap at D=301⁴ is negative; no stronger 301 theorem is inferred from that old fixed envelope. A broken 76*t³ guard cannot be recycled.

## Kill condition and promotion

No widening D hypothesis back to 302, no padded Gram substitution, no selected minor, no modified derivative or trace weights, no added prime power, no floating-point proof, no explicit or hidden axiom. Exact-head focused/full-root Lean and permitted transitive-axiom checks mandatory. The original 301 same-Gram ARITHMETIC lower and actual NumberField.discr K transport are separate open theorems. Keep independent review issue #50 open and do not promote any 301 theorem to main from scalar tests.

Evidence: H new 301 analytic upper until exact-head Lean and source audit; M bounded scalar diagnostic; P relative to 301 radius theorem Phase361; external semantic fidelity H.
