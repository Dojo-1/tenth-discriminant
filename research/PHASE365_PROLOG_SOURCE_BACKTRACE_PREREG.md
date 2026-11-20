# Phase365 — GNU Prolog reverse-lineage / same-Gram adversarial companion

**20 November 2026 — research-only preregistration.** Companion to Phase364 PR #275, NOT a stronger field theorem. Code in research/prolog/phase365_adversarial.pl; source guard in scripts/phase365_lean_anchor_guard.py; workflow in .github/workflows/phase365-gnu-prolog-adversarial.yml.

## Central question

When Phase364 travels backwards from the proposed actual field-discriminant bound to an auxiliary original integer trace Gram, which dependencies preserve the *same source* and which valuation signals survive admissible integral row-frame transport? Seek exact small counterworlds to invalid transfers, never assume the theorem false because a changed toy source differs.

The frozen large-source contract is D>=301^4, R=floor(D/4), S=floor(R/25), J=S, Qthin=ellipsePairs D (thinRadius D), original ordinary-Z jets holding W fixed, integerPairTrace D a b = 2*(a.1*b.1+D*a.2*b.2), row-major (i.val/S,i.val%S), and G=integerRectangularTraceGram Qthin D S R S. Padded ellipse may supply ONLY a cardinality majorant.

## What Prolog does

- Reifies the claim dependency graph for Phase364 -> odd chart -> same-original upper/lower, positivity and scalar contradiction; performs cycle-guarded backward path enumeration.
- Checks manually declared source-signature compatibility and intentionally rejects padded Gram, Hasse derivative, changed J, wrong trace metric and changed row order. A separate Python textual anchor guard checks the ACTUAL named Lean declarations, including four deliberate source mutations; this is still not a Lean parser or theorem checker.
- Recomputes exact integer ordinary derivatives and two-/three-row trace Gram determinants for bounded REAL-ONLY samples (S=1, the original factor two).
- Searches bounded witness spaces for invalid selected-minor-to-Gram upper, p-factor transport across same-size samples, dual modular prime roles, raw-row p-divisibility necessity, and valuation preservation across changing derivative clock.
- Checks one genuine integral unimodular row congruence.

## Exact falsifiers and witnesses (bounded M)

| Source or witness | Exact result | What it tests |
|---|---|---|
| Q={(0,0),(5,0)}, R=2, J=S=1 | det G=100, v5=2 | Source p-factor exists |
| Q={(0,0),(1,0)} | det G=4, v5=0 | Same count does not preserve valuation |
| Qshift={(1,0),(6,0)} | G=[[4,14],[14,74]], det=100 | Raw G01=14 is not divisible by 5 |
| U=[[1,0],[-1,1]] on Qshift | UGU^T=[[4,10],[10,50]], det=100 | Legitimate unimodular transport |
| Q={(1,0),(6,0),(11,0)}, R=3,S=1 | det G_J = 500000,784400,799664 for J=1,2,3 | v5=6,2,0: derivative clock is NOT a gauge |
| E=[1 1], B=I | full Gram det=2, selected minor squared=1 | Selected minor not an upper |
| E=diag(3,1), p=3, q=5 | det E=0 mod3; nonzero mod5 | Divisor prime and rank-witness prime have different roles |

These toy samples do not assert anything new about the full thin ellipse, universal prime exponents, or a bound for quadratic fields.

## Fail-closed gates and promotion

1. Reject changed source, jet, metric, trace, row order, normalization, unrecognized theorem or any escaped negative mutation.
2. Reject failed Prolog exact arithmetic tests. Successful tests are finite facts relative to their own encoded objects, NOT proofs of Phase364.
3. Keep Phase364's Lean exact-head root checks and human source-to-field semantic reconstruction separate from Prolog. Do not promote a manually encoded contract into a theorem.
4. An apparent counterexample to a Lean theorem must be shown to satisfy the theorem's EXACT source and hypotheses, not a toy surrogate.
5. No new conductor-derived prime factor, padded Gram determinant or Siegel-zero conclusion. Main stays at the existing 322^4 public Lean encoding while the 301^4 research gate remains open.

## Reproduce

    python3 scripts/phase365_lean_anchor_guard.py
    gprolog --consult-file research/prolog/phase365_adversarial.pl --query-goal main

GNU Prolog main/0 returns exit code 0 on all controls passing and 1 otherwise. CI runs a fixed finite harness; it must not crawl unbounded argument spaces.

## Next formal bridge (H)

Construct a canonical original integer evaluation matrix E(Q,D,J,R,S) from the actual derivative rows, show a source-locked identity G=E B E^T for the trace metric B, and transport admissible unimodular U through it. Then distinguish operations preserving det G from operations changing the derivative observation clock. Do NOT infer universal valuation or field results from the finite Prolog toy.

**Human reconstruction checkpoint:** independently derive the shifted two-sample Gram and its unimodular U-congruence. Identify which hypothesis fails if one tries to transport its 5-adic valuation to Qunit or to J=2.


## E110 — non-real conjugate/source control (20 November 2026)

The first purely real test was not an adequate adversary for the conjugate factor W: it cannot distinguish z*z from z*conj(z). The harness now independently implements exact integer-pair multiplication (a+b*sqrt(-D)), conjugation, ordinary Z derivative with W held fixed, and the original positive trace 2*(ac+Dbd).

At the EXISTING Lean control from IntegerTraceGram.lean, Q={(0,1)}, D=3, J=2 and rows (0,0),(1,1), the exact Gram is [[2,6],[6,24]] with determinant 12. The false unconjugated replacement z*z=-3 flips the key off-diagonal contribution, whereas z*conj(z)=+3. This is a stronger independent check of the actual non-real source convention, still only one finite regression. The textual Lean guard now insists on the named nonreal theorem, pairConj in the derivative definition, and the original matrix, and kills an intentionally flipped sign. No additional field theorem is inferred.


## E111 — archimedean/p-adic clock-split theorem target (20 November 2026)

For a FIXED finite original lattice source Q and FIXED original row family, let G_J denote the original positive integer trace Gram at ordinary derivative depth J. The contribution added when J rises to J+1 is, in real coordinates, a sum of weighted outer products 2*a*a^T+2*D*b*b^T, hence positive semidefinite if D>=0. This gives the **paper-level** matrix inequality G_(J+1)-G_J >=_PSD 0, and suggests a Lean theorem at the real-cast original Gram (before any claim about determinants/fields).

The exact bounded example Q={(1,0),(6,0),(11,0)}, R=3,S=1 has

    G_2-G_1 = [[0,0,0],[0,6,72],[0,72,1264]]
    G_3-G_2 = [[0,0,0],[0,0,0],[0,0,24]]

The nontrivial principal 2x2 minor of the first increment is 6*1264-72^2 = 2400 >0. All increments are PSD in this fixed example; det G_1 < det G_2 < det G_3; nevertheless v5(det G_1)=6, v5(det G_2)=2, v5(det G_3)=0.

**New discriminator:** the archimedean positive-semidefinite observation order does NOT induce a monotone p-adic valuation order. The research should explicitly type an observation-clock morphism J->J+1 separately from an integral unimodular row-frame isomorphism U. No unlabeled "moving-frame invariance" may cross this distinction.

Lean promotion H: prove the original entrywise difference as an exact sum of outer products on one source and trace convention, then PSD over the reals. A separate independent integer witness already refutes naive monotonic valuation; do not hypothesize it generically.
