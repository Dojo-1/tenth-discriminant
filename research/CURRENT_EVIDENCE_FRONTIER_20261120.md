# Research evidence frontier — 20 November 2026

This is a dated evidence register, not an external referee report. For live merge/CI state always check the exact GitHub PR head and workflow logs. Historical STATUS.md entries are retained, not overwritten.

## Publication authority (main)

The publicly integrated Lean-encoded actual-field result remains the strict bound
`(NumberField.discr K).natAbs < 322^4 = 10,750,371,856`
for totally complex degree-two fields K of class number one (PR #126). This is an **actual field-discriminant statement**, not a claim about the auxiliary Gram determinant itself. Lean compilation validates the encoded theorem under its transitive axioms; independent human source-to-field reconstruction is still open in issue #50. The research-only 321^4 field theorem (#157) and 307^4 field theorem (#232) have their own verified heads and different merge status. Do not silently promote either to main.

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
| Original sign/CRT observer chain | E41 #253, E43 #255, E44 #256, E45 #257 merged on respective research parents | P relative to encoded source observer; neither an intrinsic curvature nor an actual-Gram determinant gain |
| Three-moment observer E42 | #254 historical branch; consolidation #264 | P at old exact head; integration needs NEW combined-head verification |
| 307^4 actual field research endpoint | #232, based on 307 source lower/upper and field charts | P relative to exact-head encoding; independent human semantic review open |
| 302^4 scalar U(D)<L(D) | #260 merged into Phase351 research | P relative to encoding; **not** a bound on any source Gram until both source bounds are independently established |
| 302^4 original radius ratio | #262 merged into Phase350 research | P relative to encoding; corrects false 76*t^3 guard by true 75*t^3 guard |
| 302^4 conditional original-Gram binary-plus-odd lower | #263 merged into Phase355 research | P relative to encoding **under explicit squarefree odd-chart, classNumber=1, positive original Gram hypotheses**; source-fidelity review open |
| 302^4 SAME original-Gram analytic upper | #265 draft | H until exact-head full-root Lean, permitted axioms and semantic source review pass |
| 302^4 actual-field theorem | Not claimed | H. Requires same original G upper + lower + scalar + maximal-order even/odd field transport, all at exactly D>=302^4, then independent review |

## Corrections / negative controls (load-bearing)

1. The old conservative Phase342 count certificate fails below 307 for its chosen rational inequality; exact full ellipse counts remain ample at tested 301/302.
2. At D=302^4, the 307 argument's R>=76*t^3 guard is FALSE. The 302 line uses a separately proved R>=75*t^3, never silently weakens the old theorem.
3. The analytic cell-area sufficient estimate fails its chosen coefficient at t=13, but original full-ellipse counts are still sufficient there. Avoid conflating proof failure with source failure.
4. The Phase355 scalar expressions are not yet jointly proved as upper and lower bounds for the identical Gram at 302^4.
5. At D=301^4 the Phase355 scalar lower-minus-upper expression is negative (bounded exact/decimal research controls); no 301 proof follows from the unchanged coefficients.
6. Complete ellipse is conjugation-saturated: independent sign toggles cannot create a new injective full source; E44's aggregated Gaussian CRT gap vanishes at D=1 on full ellipses even when some sparse sources are separable.
7. The source-to-field semantic review #50 stays open after any model-authored proof, green workflow, or merge.

## Continuation gates

A. Finish #265: full-root compile and transitive-axiom audit for a 302 same-gram analytic upper. Failure means a named theorem or numeric guard must be corrected, NOT assumed.

B. Consolidate #261/#262/#260/#263/#265 into one fresh exact-head **source-locked** proof branch with identical Qthin, J, R, S, trace, determinant and normalization, no duplicate prime counting.

C. Only then construct a **research** actual-field statement at 302^4 using the explicit odd/even ring-of-integers chart, and submit to an independent number theorist. Do not change main or close #50 before this.

D. Keep the separate E46 observer consolidation as measurement theory; any new arithmetic factor requires a new exact integral row certificate on all original source samples.

All branches and PRs retain date-stamped evidence; the historical five-band Phase352 paper argument is superseded as the best sufficient count certificate by the proved 14^4 geometry, not erased.
