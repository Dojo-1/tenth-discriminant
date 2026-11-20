# Research evidence frontier — 20 November 2026

**Latest post-Phase360 update:** [E100 source-locked closure and 301 research queue](ROUND_20261120_PHASE360_362_HOUSEKEEPING.md). Historical entries below remain evidence, not a dynamic PR ledger.

This is a dated evidence register, not an external referee report. For live merge/CI state always check the exact GitHub PR head and workflow logs. Historical STATUS.md entries are retained, not overwritten.

## Publication authority (main)

The publicly integrated Lean-encoded actual-field result remains the strict bound
`(NumberField.discr K).natAbs < 322^4 = 10,750,371,856`
for totally complex degree-two fields K of class number one (PR #126). This is an **actual field-discriminant statement**, not a claim about the auxiliary Gram determinant itself. Lean compilation validates the encoded theorem under its transitive axioms; independent human source-to-field reconstruction is still open in issue #50. The research-only 321^4 (#157), 307^4 (#232) and 302^4 (#267) actual-field statements have verified Lean heads but are not independently refereed. Their merge status varies; do not silently promote any of them to main.

## The full original source (immutable)

- D : Nat; R(D)=floor(D/4), S(D)=floor(R/25).
- t = fourthRoot D = D^(1/4); thinRadius D = ceil((11/25)t^3); padded rho D = ceil((13/25)t^3).
- Qthin = all integer (x,y) with x^2+D y^2 <= thinRadius^2, not a selected subregion.
- E is the original ordinary derivative in Z holding W fixed; original row-major rectangle (R,S) and jet order J=S; B has original factor-two trace coefficients (2,2D).
- The invariant original integer is the complete Gram G=E B E^T. Its det is **not** the field discriminant.
- Padded geometry is allowed as a cardinality majorant only, not a substitute for G.

## Current exact-head research components

| Gate | PR / lineage | Evidence and limitation |
| --- | --- | --- |
| Complete thin count D>=21^4 | #258 merged into Phase352 | P relative to encoding for interpolation count only |
| Stronger count D>=14^4 and same integer Gram positivity | #259 merged into historical Phase353; #261 merged into Phase352 | P relative to encoding; no prime exponent or field bound |
| Original sign/CRT observer chain | E41 #253, E43 #255, E44 #256, E45 #257; E46 #264 merged as consolidation | P relative to encoded source observers; neither intrinsic curvature nor an actual-Gram determinant gain |
| Three-moment observer E42 | #254 closed as superseded by exact-head Lean-passing merged E46 #264 | P relative to original integer-Gram J=1, R=2, S=1 encoding; does not imply general source injectivity |
| 307^4 actual field research endpoint | #232, based on 307 source lower/upper and field charts | P relative to exact-head encoding; independent human semantic review open |
| 302^4 scalar U(D)<L(D) | #260 merged into Phase351 research | P relative to encoding; **not** a bound on any source Gram until both source bounds are independently established |
| 302^4 original radius ratio | #262 merged into Phase350 research | P relative to encoding; corrects false 76*t^3 guard by true 75*t^3 guard |
| 302^4 conditional original-Gram binary-plus-odd lower | #263 merged into Phase355 research | P relative to encoding **under explicit squarefree odd-chart, classNumber=1, positive original Gram hypotheses**; source-fidelity review open |
| 302^4 SAME original-Gram analytic upper | #265 merged into Phase350 research parent | P relative to exact-head Lean/source/allowed-axiom checks; external semantic validation open |
| 302^4 actual-field theorem | #267 component checked; unified Phase360 #268 full-root source/axiom checks passed and merged to Phase350 research parent | P relative to checked Lean encoding, independent number-theoretic semantic review H; not public main |

## Corrections / negative controls (load-bearing)

1. The old conservative Phase342 count certificate fails below 307 for its chosen rational inequality; exact full ellipse counts remain ample at tested 301/302.
2. At D=302^4, the 307 argument's R>=76*t^3 guard is FALSE. The 302 line uses a separately proved R>=75*t^3, never silently weakens the old theorem.
3. The analytic cell-area sufficient estimate fails its chosen coefficient at t=13, but original full-ellipse counts are still sufficient there. Avoid conflating proof failure with source failure.
4. Phase358 #265 original upper and Phase357 #263 lower concern the identical Gram at 302^4; Phase360 #268 passed the fresh combined-root/source/allowed-axiom audit. This is a research theorem, not external mathematical validation.
5. At D=301^4 the Phase355 scalar lower-minus-upper expression is negative (bounded exact/decimal research controls); no 301 proof follows from the unchanged coefficients.
6. Complete ellipse is conjugation-saturated: independent sign toggles cannot create a new injective full source; E44's aggregated Gaussian CRT gap vanishes at D=1 on full ellipses even when some sparse sources are separable.
7. The source-to-field semantic review #50 stays open after any model-authored proof, green workflow, or merge.

## Recent research-only integrations

- Original conductor counterexample E31 (#235): noninjective conductor observation does not force a 5-factor of the sampled original Gram.
- E32 (#237): a source nilpotent cannot inject into the reduced Gaussian target under square-compatible transport.
- E37 (#250): legitimate and impossible unimodular original-Gram certificates are sharply separated.
- E38 (#251): every finite conductor kernel is nonzero but the specified coherent representative thread is necessarily zero; this is not a general Mathlib p-adic-ring theorem.
- The historical E42 PR #254 was closed as superseded by merged E46 #264 rather than forced through a conflicting root.

## Continuation gates

A. Preserve verified 302^4 Phase360 #268 integration. Require fresh CI for the evolving Phase350 parent after later child merges; do not infer a 301 bound from 302.

B. At 301^4 Phase361 #270 checks the sharper original 847/1000 thin/padded ratio, 1377/10000 saving and conditional scalar contradiction. Phase362 #272 attempts the complete SAME ORIGINAL GRAM 301 analytic upper; H pending proof. The 301 arithmetic lower and actual field transport remain open.

C. The research actual-field statement exists at #267. Request independent **human** reconstruction of the exact integral valuations, original upper and maximal-order field chart in issue #50. A green root does not license a mainline proof promotion without this review.

D. E46 #264 has merged. Keep observation-loss controls distinct from arithmetic valuations: a new prime power still requires exact integral row certificates on the complete original source. Preserve E31 #235, E32 #237, E37 #250 and E38 #251 countercontrols, integrated into research parents.

All branches and PRs retain date-stamped evidence; the historical five-band Phase352 paper argument is superseded as the best sufficient count certificate by the proved 14^4 geometry, not erased.

## Open research lineage / housekeeping

The [open-PR dependency and triage register](OPEN_RESEARCH_PR_TRIAGE_20261120.md) distinguishes conductor/observer countercontrols, exact ordinary-jet factor certificates, finite clocks and the source-to-field proof queue. Review PR heads live; this dated table is a snapshot. Do not bulk-merge green workflows or mistake research branch integration for mainline publication.

**E30 kernel integration update:** #234 merged into E29 research; conflicting parallel #233 is replaced by source-clean #271, pending new exact-head checks. No infinite p-adic-ring theorem or extra original-Gram prime valuation follows from these finite tests.
