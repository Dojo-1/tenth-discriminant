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
