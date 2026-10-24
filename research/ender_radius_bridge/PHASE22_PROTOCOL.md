# Phase 22 preregistration: the exact factorial/Legendre bridge

Date: 2026-10-24. Base: draft PR #28 head `36e6f9a`, pinned Lean CI
`40093798308` and CodeQL passed. This protocol precedes proof edits.

## Exact target

Define the actual factorial mass
`H(R)=sum_{r<R} log(r!)=log(product_{r<R} r!)`.
Using the pinned Mathlib log-factorization and Legendre theorems, prove
the finite exact identity

`H(R) = sum_{prime p<R} log(p) * sum_{j>=1, p^j<R} floorSum(R,p^j)`.

All sums must have explicit finite ranges. A common exponent range
`1<=j<R` is permitted after proving its sufficiency; powers `p^j>=R`
must contribute zero. The prime `2` is included in this identity. Retain
the existing `floorSum` definition and its checked production closed form.
No prime-distribution estimate or classification theorem is an input.

For `R>=2`, also attempt the exact production scalar lower bound with
`N=R-1`:

`H(R) >= (N^2/2)log(N)-3N^2/4+N/2+1/4`.

The intended proof compares increasing functions with exact real
integrals. Do not substitute a different numerical lower formula or
change `prime_mass`, its clipping rule, radius, cutoff or certificates.
If the scalar estimate does not close, preserve the checked identity and
name the precise integral/summation obligation.

## Controls and boundary

Check `R=0,1,2` for the identity and equality of the scalar bound at
`R=2`. Check `product_{r<5} r! = 288 = 2^5*3^2` and the matching prime-power
floor sums. Reject omission of prime `2` already at `R=3`, and reject a
composite index being treated as a prime factorization term. Include a
power exactly equal to `R` to check the strict loop endpoint. No `sorry`,
new axiom or unproved numeric premise.

This phase does not by itself prove Ender's `prime_mass` lower bound:
small-prime subtraction, higher-power/tail estimates and clipping remain
to be connected. Exact Arb interpretation, universal closure, even cases
and classification also remain open. Run targeted Lean, full build,
source correspondence, compiled dependency audit and inherited negative
controls on the published proof head. Keep the PR draft and unmerged.

## Execution record

Protocol-only commit `b7a43ea4d488aff555163d3eb7a2f9fca0c0486b`
preceded all new proof edits. `FactorialPrimeMass.lean` checks both targets:
the exact finite identity for all natural `R`, and the unchanged production
scalar lower expression for `R≥2`. It first proves the stronger integral
bound with final terms `N−1/4`, then weakens to production `N/2+1/4`.
Ten controls compile, including the omitted-two, composite-index and
missing-domain-guard falsifiers. No production code or certificate changed.

Development failures were proof-engineering repairs: a redundant `ring`
after a closed goal was removed; the global `interior_subset` name replaced
an incorrect namespace; natural-one versus real-one coercions at the
integral/sum interface were normalized explicitly. No mathematical guard
was removed and no failed strengthening was promoted to a theorem.

From `lean/`, `lake env lean TenthDiscriminant/FactorialPrimeMass.lean`
and the full `lake build` pass locally (6712 steps). `python verify_sources.py`
passes all 250 endpoint pairs. From the repository root, `git diff --check`
and `python -m json.tool .agent/state.json` pass; local Markdown file targets
resolve. The generated, untracked `lean/lake-manifest.json` is not published.
The complete published-head dependency audit and inherited negative controls
are delegated to the pinned Linux CI workflow, not claimed from a partial
Windows wrapper run. The current head's CI result is reported at delivery.
The source-correspondence check only matches the saved interval endpoints;
it does not verify Arb inequalities. Full `prime_mass` weight conversion,
tail bounds and clipping, numerical interpretation, universal closure and
classification remain open. The result is classical; no novelty claim.
