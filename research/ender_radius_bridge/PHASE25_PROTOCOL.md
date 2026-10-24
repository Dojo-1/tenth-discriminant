# Phase 25 preregistration: exact numerical certificates, first interval

Date: 2026-10-24. Base `6717eee`, pinned CI `40100457533` and CodeQL
`40100456379` passed. Register before proof edits or numerical replay.

## Fixed input and replay

Use only the first recorded interval `[700000000000,875000000000]`,
`C=20`, `P=10000`, `R=D1//4`, `S=J=R//20`, and production's unchanged
integer radius/vertical padding at 160-bit Arb precision. No parameter
search, new interval, changed cutoff or saved certificate. Record the exact
integer witness, lower/upper values and replay result without treating any
Arb value as a Lean premise. The local Python lacks flint; an isolated
workspace runtime may install the declared `python-flint==0.9.0` pin.

## Proof attempt

Develop exact rational enclosures for logarithms from the pinned Mathlib
odd-power series. For `0≤z<1`, the N-term sum
`L=2*sum_{k<N} z^(2k+1)/(2k+1)` must bound
`log(1+z)-log(1−z)` below; its upper bound is
`L+2*z^(2N+1)/((2N+1)*(1−z²))`. Prove the remainder, not just positivity
of the truncated series. Binary range reduction is permitted if its exact
logarithm identity is proved. All certificate arithmetic must be rational
and kernel-checked; no `native_decide`, new axiom or trusted Arb parser.

Attempt to verify the fixed witness's real radius and floor-padding guards
using squared rational inequalities and pinned 20-decimal pi bounds. Then
attempt the strict mathematical lower/upper comparison for that same input,
composed with `classNumber_ne_one_of_ender_comparison`. Do not replace the
mathematical production expressions with an unrelated cutoff argument.
If the full strict comparison does not close, preserve the exact checked
enclosure/guard results and name the unclosed obligation. A replay pass or
sound enclosure library alone is not a checked interval exclusion.

## Controls and reporting

Check zero log argument-transform, empty prefix, a positive log-two witness,
and reject treating an empty truncated sum as an upper bound. Verify that
an invalid rational enclosure is rejected. Keep interval endpoints and all
production tools unchanged. Preserve environment and proof failures.
Update current README/STATUS/FORMALIZATION and the human guide. Run full
pinned CI on the exact published head. Keep PR #28 draft/unmerged.
All other intervals, universal closure, even cases and classification remain
open until separately proved. No novelty or checked-cutoff claim from partial work.

## Registered implementation repair after observed verifier failures

The monolithic rational-normalization table proof crashed after 77.335612 s.
The 32-row pilot passed, but the full chunked version with a 16384-KB thread
stack crashed after 539.5711452 s and was observed using 16653869056 bytes
of working memory. Exact records are in `PHASE25_PROOF_FAILURES.json`.
Neither failure is a mathematical counterexample or an accepted table proof.

Before further implementation, register this repair: retain the identical
fixed interval, radius, prime table, eight-term series and 10^12 rounding.
Prove that a raw integer polynomial/common-denominator representation equals
the already checked rational prefix and remainder. Check enclosures by integer
cross-multiplication, with a kernel reduction proof of the Boolean result.
No `native_decide`, trusted native arithmetic oracle, changed bound or relaxed
row/coverage/budget obligation. The purpose is a smaller proof representation,
not a weaker statement. Keep all earlier proof attempts and negative records.

### Registered division-witness refinement

The monitored sequential integer attempt was stopped at 222.7429775 s after
its sampled working set reached 8590958592 bytes. The current Boolean row
checker still evaluates large divisions/remainders in factorial and valuation
coefficients. Before the next repair, register their removal from verification:
the generator may supply quotient, remainder and floor-sum witnesses, checked
by `R=q*k+m`, `m<q` and the exact scaled floor-sum identity. Prime-power witness
lists must include every contributing power or prove the remainder is zero.
The fixed square-sum coefficient is also supplied and proved once. Keep the
same input, coefficients, weights, log bounds, coverage and budget obligations.
Prove the new checker sound; no trusted division oracle or weakened target.
