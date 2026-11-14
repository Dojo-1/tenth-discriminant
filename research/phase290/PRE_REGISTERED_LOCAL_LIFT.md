# Phase290-B: preregister modular radical lifting and wall determinant polynomial

**Date: 2026-11-12, AFTER first Phase290 original-source CI PASS [#43255011442](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43255011442), BEFORE Phase290-B code.** This is a *new* independently implemented oracle, but still AI-authored and correlated with the existing source. The first run already measured six-row original D563 p-local Gram exponents: at p5 (old six zeros, new [0,0,0,0,0,2]), at p7 (old six zeros, new [0,0,0,0,0,1]); E has full 6/6 rank mod p5 and p7 in BOTH supports. Those observations are a **retrospective regression baseline**, not blind predictions.

## Exact frozen source

Use exact original D563, rho51, R140,S=J5, inner Q285 with |y|<=1 and new DeltaQ74 at |y|=2, full Q359. Keep the six monomial labels [(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)], full original ordinary Z-jets, metric (2,2D), and original helper hashes in the Phase290-A protocol. Import the 6x6 integer G_minus, G_delta, G_plus from `noether_smith_wall.py`, independently validate them through the Phase206 mixed-moment Gram oracle, and do not modify either source or the Phase290-A test.

## A. Hensel-style kernel lifting in the SAME original Gram

For p=5 and p=7, use a separate exact modular Gauss-Jordan solver (not the existing minor-GCD algorithm) to find the 1D kernel of G_plus mod p, choosing its first free coordinate=1, other free coordinates=0. Given primitive vector v_k with G_plus v_k=0 mod p^k, solve
  G_plus * w ≡ -(G_plus v_k / p^k) mod p
and set v_(k+1)=v_k+p^k w. The solution exists iff the RHS belongs to the image mod p. For symmetric G, the obstruction is also the pairing against the left radical.

**Frozen consistency target derived from previously observed Smith factors:**
- p=5: one primitive kernel line mod5, a lift mod25 exists; a lift mod125 does NOT exist (one exponent exactly 2).
- p=7: one primitive kernel line mod7, a lift mod49 does NOT exist (one exponent exactly 1).
- G_minus mod5 and mod7 is nonsingular; this is new restricted-pairing degeneracy rather than evaluation source rank loss.
- On every permitted lift, check all six entries of Gv divisible by p^k, not only a scalar residual. Retain a failed-lift certificate consisting of the nonzero left-radical obstruction modp. If any expectation fails, STOP and report it without moving a threshold.

These are algebraic consequences of the **known** small Smith profile, not new independent evidence for a field theorem; the different solver is a coding-error control.

## B. Integer wall-parameter polynomial, no fake smooth integer gauge

Define formal `G(t)=G_minus+t G_delta` and `f(t)=det G(t) in Z[t]`, degree <=6. The only actual source endpoints are t=0 (the inner diagnostic) and t=1 (the FULL original source). Build f by the **Leibniz permutation polynomial** (720 terms for 6x6; no numeric interpolation, floats, determinants of a different size, or modified Gram) and independently verify f(0)=det G_minus, f(1)=det G_plus, f(2)=det(G_minus+2G_delta), and f(-1)=det(G_minus-G_delta). Confirm P G(t) P = G(t) coefficientwise under the existing inversion parity.

For p in {3,5,7}, evaluate roots `f(t)=0 mod p` for ALL t in Fp and the exact derivative `f'(t) mod p` at each root, especially t=1 for p5/p7. **No derivative order, root multiplicity or other roots have been preregistered as predictions**; treat these as exploratory outputs. At t=1 the already observed determinant divisibility by 5² and 7 is a frozen regression check. A root of f modp at some formal t is NOT a new ideal/prime or an allowed original-source specialization unless t is exactly the original endpoint.

## Epistemic gates

[P-paper] elementary Smith/radical lifting equivalence and determinant polynomial; [M once focused CI passes] actual finite root/derivative data and the independently replayed p5/p7 depths; [H] useful uniform control of full original 700-row primitive pairing radicals across multiple support walls; [R] inferring a monotone Gram valuation or field theorem from PSD wall interpolation. No extra p-unit to add to Phase207 lower or #157. Do not merge automatically; keep independent mathematical semantics and root Lean review gates.
