# Phase41: expose the aspect-ratio trade-off; one fixed new-family pilot

Baselinef7bbfaa0d20b561f67bf9627ee2ecf782a751e28. The previous goal turn
was progress: exact proof-headf163801 passed pinnedCI40153287923 and
security40153286062, record6392486504 before publication. Phase40 supplied
a frozen two-manuscript comparison. New publication CI40154838691 is
confirmed live onf7bbfaa; security40154836580 passed. Finish and record that
same run before a newer push; no restart after observation timeout.
Only inherited lean/lake-manifest.json is untracked. Goal stays active.

## Fixed mathematical question

The current Gram route pays for R/S in its quadratic prime loss while the
upper-bound slope improves when S/R decreases. Expose this trade-off in
one reusable lower-envelope theorem, instead of hardcoding R<=21S:

For R>=100000000, S>=500000, logR>=2, real K>=0 and R<=K*S, attempt

    rawLower/(R^2*S) >= .999997*logR - (3.294 + (56/1250)*K).

Use the same actual rawPrimeMassLower, four checked prime-log constants,
fixed tailBudget, factorial predecessors and clipping comparison. No new
analytic assumptions. Keep all existing definitions, theorem statements,
proofs, finite certificates, radius families and published cutoffs intact.
Add AspectRatioLowerEnvelope.lean, import it in the root if accepted.
Do not infer a new cutoff from this lower lemma alone.

## Exactly one observational pilot

Use the existing isolated python-flint0.9.0/numpy2.5.4 environment,
Arb256 bits, D=100000000003, R=floor(D/4), C=25, S=J=floor(R/25),
t=sqrt(sqrt(D)), rho=ceil((13/25)*t^3), K=251/10, P=10000.
This is a NEW auxiliary family, not a modification of flow/PREREG_ENDER.txt
or its saved campaign. No C/radius/threshold/precision search or fallback.

Check dimensions, R<=K*S, strict integer inertness endpoint, positive
radius and rho<R, original chosen-radius inequality, direct lower point
count and derivative-count guard, actual production prime-mass versus
upper_B, and both candidate affine envelopes

    rawLower/(R^2*S) >= .999997*logD - 5.820,
    upper_B/(R^2*S) <= .8*logD - .813.

Check scalar separation at u=25.3 and failure at u=25 with exact rational
arithmetic; check the dimension example R=25q+24 explains why R<=25S is
not generally valid. Record every assertion, ball string, command and exit
status. Do not test squarefreeness or infer universal validity from one D.
Run the pilot once with120s/8192MB, preserve a failure/resource stop without
retry or tuning. No external manuscript code or new dependency installed.

## Proof attempt, controls and delivery

One fixed Lean target,600s per owned process/8192MB; at most three generic
elaboration repairs under900s cumulative. Preserve every attempt; no retry
after resource stop or cap increase. Controls: old K=21 specialization,
K=25.1 specialization, exact scalar crossing/rejection and the floor guard
counterexample. No sorry, extra axiom, native_decide, weakened audit or pin.
After acceptance run full root, signatures/compiled axioms, unchanged source
and rejection gates, and pinned CI at the exact published head. Verify the
new theorem's input closure excludes old cutoffs, final iff, nine positives
and finite answer certificates. Verification is not an alternative pilot.

Explain the trade-off in one short human guide. Update current README,
STATUS, FORMALIZATION and objective accounting only to supported scope:
the checked analytic cutoff remains2e11 in this phase even if all local
tests pass. Universal new-family geometry/upper envelopes and cutoff are
explicit future proof obligations, requiring another preregistered cycle.
No merge, Tao post, novelty, optimality, independent review, arbitrary-field
representation, full-classification or all-objectives-complete claim.
