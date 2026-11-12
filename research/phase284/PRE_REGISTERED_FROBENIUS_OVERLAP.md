# Phase284 — first-Bockstein/Frobenius overlap on the original D403 source

Preregistered 12 Nov 2026 before authoring or running Phase284 code. AI-assisted paper algebra, no human-independent mathematical validation.

## Exact source and prior art

Use **unchanged** D403, rho40, R100, S=J4, Q219; both signed integer coordinates, all ordinary Z-jets j=0..3 with W fixed, raw E (not Frobenius-normalized C0 or an unweighted Gram). Inert p=3. Frozen original-source oracles:
- `research/phase206/source_probe.py` git blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`
- `research/phase204/ordinary_jet_filtration.py` git blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`

Phase208 already defines the integral unitriangular Frobenius row basis:
`k(r,s)=min(r//3, S-1-s)`,
`P_(r,s)(Z,W)=Z^(r-3*k) W^s (Z^3-W)^k`,
and normalized integer ordinary-jet row `C_(r,s)=T(P_(r,s))/3^k`. The source proof of divisibility and the determinant valuation contribution `F3=sum_(r,s) k(r,s)=570` are **prior work**. PR #173 merged source-correct raw Hermite ranks and draft #174 measured 9 first-Bockstein witnesses. Do not claim priority for the Frobenius frame.

## Frozen hypothesis / proof target

Set `H=Z^3-W`, `f_a=Z^a H` for `a=0,...,8` (the same nine witnesses), and uniquely `a=3q+b`, `0<=q,b<=2`. The exact polynomial identity in Z[Z,W] is

`f_a = sum_(t=0)^q binom(q,t) Z^b W^t H^(q+1-t)`.

Each summand is **exactly** the prior integral Frobenius-frame row `P_(r,s)` with `r=b+3(q+1-t)`, `s=t`, and **actual** old exponent `k(r,s)=q+1-t>=1`. In particular, no row with k=0 appears. Division by 3 is integral in all original ordinary jet channels. Then

`T(f_a)/3 = sum_(t=0)^q binom(q,t) 3^(q-t) C_(b+3(q+1-t),t)`

exactly over the integers. Mod 3, the only survivor is

`T(f_a)/3 mod3 = C_(b+3,q) mod3`.

The nine normalized right-hand rows are distinct `k=1` Frobenius rows; their j3 reduction is `2*z^(3q+b)` on the 9 F9 residue nodes and has rank nine. **These exact nine raw first-lift classes are carried by already-counted p3 Frobenius source factors. They do not add nine new units to the old F3 or to any evaluation-index or primitive-pairing lower bound.** Do NOT infer that all other Bockstein classes are accounted for, or that the entire raw Smith module is exhausted.

## Fixed executable controls

1. Read original Q directly from `params(403)`, verify rho40/R100/SJ4/Q219 and all nine mod3 residue nodes, and assert source blob IDs at HEAD. Distinguish exact integer coefficient arithmetic from reduction.
2. Assert the full 400-row old exponent sum equals **570**. The nine selected `(b+3,q)` rows must be distinct and have k=1.
3. For all a=0..8, all four original ordinary Z-jets, every one of 219 original points and both integer-coordinate channels, compare **exact integers**: direct f_a jets (two ordinary original monomials) versus their full binomial expansion into the old Frobenius basis.
4. For every contributing frame row and every original source jet, assert coordinatewise exact divisibility by 3^k. Compare the exact quotient identity to the proposed weighted sum of old **normalized** rows, not just mod3 ranks.
5. Verify the mod3 quotient identity against the one distinguished k=1 row and confirm independent modular rank 9 using two different rank algorithms; ensure j3 follows 2*z^a using a separate modular quadratic-algebra power routine.
6. Negative: replacing old row exponents by all ones must FAIL the exact Frobenius depth profile for q>=1. A cap S=2 must violate the legal source-row expansion for q=2; do not silently extend outside the rectangle. At split p11, Z^11-W is not 11-divisible at (x,y)=(0,1).
7. Confirm the ordinary j3 vs Hasse coefficient distinction explicitly: j3(Z^3)=6, Hasse degree3 coefficient 1. Preserve all four jets, even if j3 vanishes raw modulo p3.
8. Bounded stdlib-only CI (<=10 minutes), separate preregistration, code, observations and workflow revisions. Stop on mismatches without editing predictions.

## Evidence / stop rule

[P-paper after independent reconstruction] exact polynomial frame decomposition and Frobenius overlap of these nine witnesses. [M after successful CI] source-exact equality on frozen D403. [R] treating the nine first-Bockstein witnesses as nine **additional** independent valuation units. [H] any new residual pairing or uniform source-family improvement after complete saturation.

No assertion of a new discriminant bound, finite-field classification, independent human review or Siegel-zero conclusion. Do not merge until exact-head focused, Markdown and full Lean audits pass. PR #157/#50 remain separate semantic gates.
