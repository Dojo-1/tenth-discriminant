# Phase281 — preregistration: full D403 third Smith layer (NO outcomes yet)

Date: 2026-11-12. Registered **before** writing or executing Phase281 computation.
This is an AI-authored continuation of the user-originated Tenth Discriminant programme.
Phase280 PR #171 was merged at `b00b8391279d316165e6a29c436e500ebd98ed9a`.
A Phase281 result is **not** a bound on class-number-one discriminants or Dirichlet-L zeroes.

## Mathematical source and invariants

Freeze exactly the Phase280 `D=403`, `rho=40`, `R=100`, `S=J=4`, all 219 ellipse points,
all 400 original monomial rows and 1752 real/imaginary ordinary-jet coordinates,
original `B=diag(2,806,...)`, with `W` fixed under ordinary `d/dZ`.
Match inert `p=3,5` and split negative-control `p=11`.
Unimodular row normalization is permitted; no change of source rows, trace metric,
observation set, jets or point enumeration.

At inert p, use the **same Phase280** integral binomial Frobenius source,
`k(r,s)=min(floor(r/p),3-s)`, and count its old factor **once**
(`F_3=570`, `F_5=550`). At p=11 use no inert row transformation,
`F_11=0`. Check original coefficients are divisible by `p^k`
before dividing. Retain the original, unnormalized source for independent checks.

## Preregistered primary question

Use a **fixed K=3** precision `Z/p^3`, and report the first three elementary
divisor grade counts `(r0,r1,r2,r>=3)` of the full 400-row normalized evaluation
matrix `C0`. Entries in `>=3` are **right-censored**.

Derive ONLY the evaluation-index lower certificate

`I_3 = r1 + 2*r2 + 3*r>=3`

and, under the separately established full-row Q-rank hypothesis, the original Gram
lower certificate `v_p(det G) >= 2*(F_p+I_3)`.

**No primitive saturated pairing H is constructed by this K=3 experiment.**
No finite K can declare an exact index while its censored count is positive.
Do not add mod-p Gram radicals to index or primitive remainder.

## Fixed controls and predictions

- Exact replay of Phase280 capped K=2 FULL profiles from the K=3 output:
  p3 `(90,36,274)`; p5 `(240,15,145)`; p11 `(132,66,202)`.
  Enforce `r0(K3)=r0(K2)` and `r1(K3)=r1(K2)`;
  `r2(K3)+r>=3(K3)=r>=2(K2)`.
- Replay Phase208 selected `k>=2` subset capped K2 histograms separately;
  **never add** selected-row indices to full indices.
- Retain ALL four ordinary derivatives. Compare dropping j=3 as a forbidden
  source-change control and fail if its reported rank does not match Phase280:
  p3 81, p5 180, p11 99 (versus 90,240,132 on full source).
- Use independent rank implementations, exact integer-jet oracle and
  truncated dual-jet oracle on pre-fixed rows/points; verify `p^k` division.
- Verify Smith profile invariance under unimodular integral row shear and column
  reversal. Any column operations are INTERNAL to Smith and must not be
  propagated to B without the corresponding congruence transport.
- Use the original `B` for all Gram diagnostics; at split p11 show that
  replacing `806` by `2` is an invalid metric change.
- Toy exact Smith profiles for `diag(1,p,p^2,p^3)` at K3, including unit shears.
- Freeze source hash and implementation revision at first execution; run
  deterministic resource bounded CI (<=25 minutes), use pinned dependencies.
  Resource exhaustion -> **INCONCLUSIVE**, never truncate rows/columns,
  increase precision or silently modify expectations.

## Preconditions and arithmetic caveat

The K3 profile is an invariant of the **original normalized evaluation lattice**
under left/right unimodular changes, not of an arbitrarily column-transformed
trace pairing. If the unchanged original Gram is positive definite over Q,
Cauchy-Binet supplies the stated lower bound because B is integral.
Independently recheck the field/source and interpolation/full-rank premise:
the archived numeric guard `219 > 2*(100-1)+(4-1)=201` is a previous
source-specific claim, **not** a substitute for review of its hypotheses.

## Falsification, stopping and promotion

- FAIL and do not publish promoted results on K2 replay mismatch, wrong
  jet/metric, inconsistent oracles, Smith invariance violation, incorrect
  Frobenius count, determinant normalization error or field-character mismatch.
- If all 400 factors close before K3, a future separately preregistered
  **primitive pairing** test may use row bookkeeping to reconstruct
  the saturated lattice and `H=Cprim B Cprim^T`.
  No retroactive primitive-pairing claim is permitted on this branch.
- If some factors are censored, report `r>=3`, the lower certificate,
  and the exact unknown depth; do not increase K post hoc.
- Compare p3/p5 with split p11, but treat three cases as distinct fibers;
  a split-prime valuation is a **negative specificity control**, not an
  inert-prime counterexample to a theorem whose hypotheses include inertness.
- The fixed-K certificate satisfies `I_K <= KRS`.
  For any fixed finite set P, the added normalized log mass obeys
  `(2/(R^2*S))*sum_(p in P) I_K(p) log p <= (2K/R)*sum_(p in P) log p`.
  For fixed K and fixed P it tends to zero as R grows. This is a
  **methodological no-go**, not an upper bound on true deeper valuations.

## Evidence labels and merge gate

[P] Classical Smith/Cauchy-Binet divisibility conditional on the full-rank
source and integral B. [M] Phase280 finite observations on merged main.
[H] Whether a second source has a positive primitive saturated residual
and whether any uniform residual contributes new non-overlapping mass.
[R] Unsaturated Gram radical as independently additive determinant mass.
[S] Moving-frame interpretation as a transport of lattice filtrations,
not an extra theorem.

Pre-registration alone is neither a successful experiment nor a mergeable
new mathematical result. Implement on this branch only after scope is frozen;
require exact-head focused arithmetic, Markdown, root Lean, negative controls
and mathematical source review. Keep independent semantic review #50 and
actual-field PR #157 open. Do not merge this planning-only PR.
