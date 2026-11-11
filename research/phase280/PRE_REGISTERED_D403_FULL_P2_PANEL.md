# Phase280 — D403 full 400-row p² Smith: registered BEFORE code

Date 2026-11-11. This is a second-source scaling / falsification experiment following the exact Phase279 D283 p3 residual=29, p5 residual=0 result. The general experiment objective is USER-ORIGINATED. This specific implementation and protocol are AI-authored.

## Original source, frozen

D=403 (13*31, odd squarefree, 403≡3 mod4), rho=40, R=100, S=J=4, ALL 219 ellipse points from x²+403y²≤40²; n=400 original (r,s) rows, m=2*219*4=1752 integer coordinates, ordinary ∂Z^j jet for j=0,1,2,3, W held fixed during differentiation; exact trace metric B=diag(2,806,2,806,...). No changed ellipse, derivative, field, sign, channel or metric.

Matched primes p=3 and p=5 are inert (chi_{-403}(p)=-1), while p=11 is SPLIT (chi=+1) and has no valid inert-prime Frobenius row divisor. All p are odd units for 2D.

For p inert set k_(r,s)=min(floor(r/p),3-s), and use F_(r,s)=sum_{t=0}^k (-1)^t binom(k,t) Z^(r-pt) W^(s+t), which is an integral unimodular row change of the ORIGINAL E. Divide its ordinary jets by p^k only after verifying that each source coordinate is divisible by p^k. Existing Frobenius source exponents F3=570,F5=550 are ALREADY COUNTED; split F11=0. Division recovers C0 modulo p² from original integer source evaluated modulo p^(k+2), bounded by p^5.

## Frozen primary test and stop rule

Calculate on the FULL n=400 rows the first TWO levels of p-adic Smith of normalized C0 over Z/p², producing histogram (0:r0,1:r1,>=2:r2). Do not imply >=2 is exact; fixed precision K=2 and NO post hoc increase. Use vectorized integer modular unit-pivot elimination, then rank of divided p-block modp.

Primary outputs each p3,p5,p11: splitting character and literal old Fp, r0/r1/r2, lower index I_p=r1+2r2, certified TOTAL lower bound

    v_p(det original G403)>=2*(F_p+I_p)

provided the original rational Gram is full rank. This is a lower bound on evaluation lattice index (primitive residual not evaluated).

SECONDARY: calculate rank of the SAME normalized source C0 modp with a logically independent row-echelon algorithm, and rank of its UNSATURATED Gram C0 B C0^T modp using the original B and an independently coded rank algorithm. Record image pairing radical = rank C0-rank Gram, but DO NOT count that radical as extra p-adic determinant factors (Phase277 primitive-saturation kill).

## Known prior results that MUST match, not new predictions

Phase207/208 used the SAME D403 source but ONLY the selected k>=2 rows, already reported:

- p3 subset rows188: 0:54,1:18,>=2:116, subset index >=250.
- p5 subset rows180: 0:120,1:15,>=2:45, subset index >=105.

The full-row source reduction must reproduce the earlier subset histograms when the same p²-Smith routine is restricted to those selected rows. If mismatch, FAIL, do not silently edit expected numbers.

The prior original-source D283 exact v3=1217 with primitive residual=29, v5=520 primitive-unit result remain prior work. D403 comparisons are between DIFFERENT sources and never an equality or transport.

## Negative and metamorphic controls

1. D403 p11 split; do NOT factor (Z^11-W) or assign an inert F11. Same original metric must be retained.
2. All 1752 columns, both signed channels, all four ordinary Z jets. Dropping j3 is a WRONG-source control: calculate changed rank and report difference; do not silently accept missing j3.
3. Selected fixed first/middle/last source rows across all s=0..3 and original Q points (first/mid/last), check all j using a separate exact integer-jet oracle from Phase204 for k=0 and an independently implemented truncated polynomial dual-jet oracle from Phase207 for k>=1.
4. The source old Fp is counted once, with the subset I2⊂FULL not added as an independent extra valuation.
5. Bflat=diag(2,2,...) is a forbidden metric substitution. At p11, weights 806≡3 vs 2, so the metric differs; explicitly verify this diagnostic while computing only original B Gram rank for claims.
6. Two rank routines must agree on the full C0 modp and the 400x400 Gram; column reversal/row shear invariance must hold for the first Smith histogram, or FAIL. If high compute budget is reached, stop INCONCLUSIVE rather than truncate the source or raise resource limits.
7. Toy diag(1,p,p²) and elementary row/column unit shears reproduce levels {0:1,1:1,>=2:1}.
8. Requires original full rank over Q to interpret determinant divisibility. Cite existing interpolation/positivity criterion |Q|=219 > 2(R−1)+(S−1)=201, but this source-to-linear independence bridge is not independently reviewed here.

## Conjecture ladder and epistemic labels

- P (classical linear algebra): determinant factorization under integral row change + p-exact row diagonal, Smith valuations of maximal minors, Cauchy-Binet with integral B.
- M (after exact-head CI): full-row modp² results; matched inert/split rank and wrong-metric controls.
- H: a uniform excess primitive restricted-pairing mass survives saturation on admissible large-D class-number-one sources and contributes R²S logD.
- R: unsaturated radical dimension as automatic additional mass (Phase277/279).
- R: treating selected k>=2 row index and full C0 index as independent additive contributions.

Merge rule: this is a finite reproducible computational panel only, **not** a changed class-number-one field result or a Siegel-zero theorem. Before merge require exact-head arithmetic CI + Markdown, source audit and no failed checks. Issue #50 stays open, PR157 cannot merge on this evidence. PR165 independent finite-CRT human review remains separate.

Outcome even if fully negative is valuable: no added first/second layer ⇒ look to deeper primitive strata only after separately frozen scope.
