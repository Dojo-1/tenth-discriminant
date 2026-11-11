# Phase278 — a safe first-layer pairing bound

Registered on base `9c165b6eebf0fe366959bbafdc8c7d49a1f55f04`, before
implementing or invoking the new checker. This is a bounded proof-bridge
attempt following Phase277, not a search for a field cutoff.

**Target [paper, not Lean]:** for an integral n-by-m observation matrix C,
integral symmetric B, nonzero det(C B C^T), and prime p, put
r=rank(C mod p), q=rank(C B C^T mod p), d=n-r. Prove

    v_p(det(C B C^T)) >= max(2d, n-q).

The proposed proof uses one p-local row division and a block-rank bound.
It must not call the divided matrix primitive without checking full rank.
This is an elementary combination of existing rank/index bounds; no
novelty or new arithmetic mass is claimed.

**Fixed finite controls:** p=3, D=7, B=diag(2,14,2,14),
w=(1,0,1,1), z=(1,0,0,0). Exactly six matrices with row lists
[w], [3w], [w,z], [w,3z], [3w,z], [3w,3z]. Compare each with
its determinant-one row shear (identity in dimension one).
Check Gram factorization, exact valuations, modular ranks, index/pairing
separation, the safe bound and preservation under the shear. The fourth
case must reject 2d+(r-q); the first must show that primitive radical
dimension is only a valuation lower bound, not an exact valuation.
These are abstract trace-metric controls, not ordinary-jet sources.

**Budget:** one full checker invocation, 15 seconds wall-clock, Node
BigInt with no dependencies. No mathematical floating-point arithmetic.
Syntax checking is allowed before invocation. Preserve stdout, stderr,
exit status, timing and script SHA256; no retry after failure/resource stop.
No old campaign, Lean build, precision escalation or reviewer agent.
Update README and RESEARCH_NOW and perform one Rizz exposition/interface
review. Existing production mathematics, source metrics, pins, workflows
and historical evidence remain unchanged. Pinned CI, if published, belongs
to its exact new head; do not transfer inherited CI to this change.

**Acceptance:** a complete paper argument plus all six exact controls;
otherwise preserve the gap or failure. No new cutoff, classification,
uniform production residual mass or independent semantic review follows.
