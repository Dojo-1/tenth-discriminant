# Phase353 — direct original-cell certificate for uniform thin-ellipse interpolation

**19 November 2026. Research-only, no field-bound promotion.**

## Exact source and constants

Use the UNCHANGED source definitions:

- `R(D)=floor(D/4)`, `S(D)=floor(R(D)/25)`,
- `t=fourthRoot D=sqrt(sqrt D)`,
- `rho=thinRadius D=ceil((11/25)*t^3)`,
- `Q=ellipsePairs D rho` with *every* integer coordinate pair satisfying `x^2+D*y^2<=rho^2`.

The pre-existing `ellipsePairs_cell_area_bound` is **already kernel checked**. It states that for `rho >= (1+sqrt D)/2`:

`pi*(rho-(1+sqrt D)/2)^2 <= card(Q)*sqrt D`.

For `t>=21`, the elementary inequality `(1+t^2)/2 <= t^3/40` holds. Therefore

`rho - (1+sqrt D)/2 >= (11/25-1/40)*t^3 = (83/200)*t^3`.

Using `pi>3` and exact rational arithmetic,

`3*(83/200)^2 =20667/40000 >20400/40000=51/100`.

Thus

`card(Q)*t^2 >= pi*(rho-(1+t^2)/2)^2 > (51/100)*t^6 >= (2R+S)*t^2`.

Since `t>0`, the ORIGINAL strict interpolation guard follows for every integer `D>=21^4=194481`:

`2*(R-1)+(S-1) < card(ellipsePairs D (thinRadius D))`.

Unlike the Phase352 five-band method, this proof reuses a **pre-existing measured-lattice cell-area theorem** with a sharper, direct comparison; it does not introduce polygonal inner rectangles, change the sample, or invoke a numerical approximation to pi.

## Evidence
- The Lean module and exact-head focused workflow are present on this branch.
- Until these runs succeed, label the new statement **H**, not fresh **P**.
- The source area theorem itself is pre-existing P relative to Lean encoding.

## Falsifiers and strict boundaries
- Any failed `D>=21^4` source cardinality or radius guard refutes the proposed theorem.
- Remove the lattice-cell margin `(1+sqrt D)/2` and the argument is invalid.
- Try `t=20` as a negative check for the **particular error bound** `delta <= t^3/40` (it fails); that does NOT assert actual point-count failure.
- This is a **geometry-only** theorem. It does NOT improve the analytic upper, inert-prime source lower, strict scalar contradiction, maximal-order identification, or actual field bound. PR #232 and issue #50 remain independent.
- The Phase352 five-band argument remains valid as an independent geometric certificate (subject to its own formalization), not silently retired.

**Theorem:** `TenthDiscriminant.FirstCertificate.Tuned.thin_radius_interpolation_count_21`.

**Source:** `lean/TenthDiscriminant/Phase353DirectCellAreaCount.lean`. **Focused CI:** `.github/workflows/phase353-direct-cell-area-21-count.yml`.
