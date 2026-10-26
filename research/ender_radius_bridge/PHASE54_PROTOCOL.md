# Phase54: fixed recovered-budget cutoff at500^4

Base published bd2a207. CI40331755630 is live; do not replace its head
before terminal verification. No new agent. This is a bounded proof
attempt, not a numerical search or a new classification announcement.

Fixed target: for an actual totally complex rational degree-two number
field with class number one, prove its actual absolute discriminant is
less than62500000000. This equals500^4, the inherited radius threshold.
Retain the same R=floor(D/4), S=floor(R/25), J=S, rho=ceil(.52D^.75),
same Gram, ordinary derivatives, weights, tail budget and prime constants.

Generalize only helper assumptions in TunedRadiusFamily and the upper
helpers of TunedAnalyticCutoff from100000000000 to62500000000. Preserve
the existing log>=25.3 lemma and all100b public conclusions. Add a separate
log>=24.8 lemma using62500000000=2^8*5^12 and existing log certificates.
Reuse unchanged helper bodies where possible; normalized lower uses the
new log guard, while the old separation still uses the old log lemma.

New module RecoveredAnalyticCutoff composes raw lower+.06<=recovered,
recovered<=the original production expression, actual-tail antitonicity,
and the existing actual-Gram upper comparison. The new separation is
(.999997u-5.820)+.06 > .8u-.813 for u>=24.8.
Prove S>=100 and25S<=R<=26S from the integer dimensions. Construct actual
field transport through the existing squarefree-root representation.

No dependency on the old100b/200b/700b cutoff conclusions, finite-answer
classification, finite masks, supplied generator, floating inequalities,
new axioms or unproved numerical premises is permitted in the new bound.
Imports may include these declarations; inspect the new theorem's actual
transitive constant closure separately. Existing even-case exclusion is
allowed; it is not a prior large odd-discriminant cutoff.

Controls: exact log24.8 affine separation, false log24.7 separation,
500^4 endpoint identity and inherited strict inertness/radius controls.
No claim that the new endpoint is optimal or the method's limit.

Budget: at most3 target builds,600s and8192MB per process,1200s cumulative;
stop after any resource stop. Preserve each full failed changed source
and raw output before at most2 local proof repairs. Do not weaken the
target/guards, search alternative endpoints or relabel a partial lemma
as the full target. If stopped, preserve the previous public cutoff.
After acceptance: full root, signatures/controls/axioms, dependency
exclusion, source correspondence, evidence integrity, human guide and
README/STATUS/FORMALIZATION/accounting. New exact-head CI stays separate.
No merge, Tao submission, novelty or full classification claim.
