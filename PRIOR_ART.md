# Prior art — current reading note (3 November 2026)

**Scope:** primary-source comparison and attribution, **not** an independent reproof or a ranking of authors. The historical 21 October snapshot is preserved below for auditability, but its dated absence and review-status claims are **retired**, not current.

- **twinheterodox:** [v0.7.0](https://github.com/twinheterodox/tenth-discriminant/tree/v0.7.0/versions/v7) reports $q<570$ by a unified derivative-determinant, auxiliary-inert-prime and finite-field-rank argument, followed by finite completion to the nine known class-number-one discriminants. The [review ledger](https://github.com/twinheterodox/tenth-discriminant/blob/main/versions/v7/REVIEW.md) reports another-model cross-check; it explicitly does **not** claim human peer review or formal Lean verification of v7.
- **Elementary companion:** [twinheterodox's separate proof](https://github.com/twinheterodox/tenth-discriminant/tree/elementary-v0.1.0/companions/elementary) reports $q<32768$; [DrMurphyIsIn's Lean/nanoda adaptation](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant) applies to this *companion*, **not** to v7. Its detailed checker claims have not been independently replayed in this repository. The dated statement below, "No Lean formalization", is obsolete.
- **rStation / Chung / other investigators:** distinct interpolation-determinant and rank-window approaches report sharper cutoffs; see the [current challenge index](https://rstation.ai/problems/tenth_discriminant) and [example 331 exclusion](https://rstation.ai/problems/tenth_discriminant/papers/28). Numerical endpoints and the status of a finite classification must be labeled separately.
- **This repository:** the fully integrated [PR #123](https://github.com/Dojo-1/tenth-discriminant/pull/123) yields the weaker $q<323^4$ theorem *within the Lean encoding*. Source correctness and independent human semantic reconstruction remain open in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). A stronger source-local 322 fourth-root target remains **unmerged research**. Do not imply independent priority, competition with the smaller cutoffs, or endorsement by any named researcher.
- **Proposed transport:** the old [method comparison](METHOD_COMPARISON_CURRENT.md) already recorded the weighted Cauchy–Binet and same-prime rank/divisor obstruction. The [new typed alignment note](https://github.com/Dojo-1/tenth-discriminant/blob/research/phase200-same-gram-field322/research/bridges/EXTERNAL_DETERMINANT_ALIGNMENT_20261103.md) refines their source scope; it claims **no equality** between twinheterodox's selected minor and our full trace Gram and records no collaboration.

---

## Archived 21 October snapshot (historical; superseded)


**Historical snapshot, not a current absence claim.** A26October source
check finds later reported QRH-based Lean developments, including h<=2,
in a different repository. They have not been replayed here. See the
[pinned, premise-aware comparison](METHOD_COMPARISON_CURRENT.md). The
original dated record below is retained; it does not establish priority.


**For class number one, our track GREEN-H1-E is an independent rediscovery of an already-published route.**

twinheterodox (Codex-assisted), same route (h=1 split-prime lattice count + Green's derivative determinant):
| paper | bound | review status |
|---|---|---|
| v4 | q < 4000 | reviewed (per their record) |
| v5 | q < 2000 | manual mathematical audit passed |
| v6 / v6.1 (17 pp.) | q < 570 | independent review PENDING |
| elementary companion (8 pp.) | q < 32 768 | "passed independent verification" (owner confirmation; no reviewer identity/report) |
Their research log credits Kyle Pratt (Tao comment 698476) with disk interpolation — the analogue of our norm-ellipse idea.
No Lean formalization in any of their versions.

Neighbouring routes in the thread: Ross (Banks + zero-forcing, d < 10¹⁰); Larsson (|D| < 50 000); QRH routes (d ≤ 653,
incl. Tao); van Dijk / Pescador variants; LemmaLab higher class numbers (QRH-conditional).

## Still open (as far as found)
1. Lean formalization of an elementary route (e.g. the 8-page elementary companion).
2. Independent audit of twinheterodox v6.
3. Class number <= H by the elementary route (our flow/, step 1 done; no one else found).
