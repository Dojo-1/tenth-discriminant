# Phase56: fixed50-billion endpoint from sharper existing weights

Base80107ff; the mathematical62.5b proof86abe21 and its first bounded
review remain frozen. Current publication CI40358914884 is live. Do not
push/cancel/restart while it is live. No further reviewer is authorized.

Fixed target before execution: actual absolute field discriminant below
50000000000 for every totally complex rational degree-two number field
of class number one, with no generator, old-cutoff, finite-answer or
numerical premise. Same R=floor(D/4), S=floor(R/25), J=S, rho=ceil(.52D^.75),
actual Gram, derivative convention, existing prime weights and tail budget.

Strengthen only the conservative recovery estimate: retain log3>=1.09
and log5>=1.6 rather than both>=1. Derive log3 from2^19<=3^12 and the
existing rational log2 certificate; use the existing log5 certificate.
For S>=100 and25S<=R<=26S, saturated rows give numerator>=55.4202*S^3
and scale<=676*S^3, enough for a fixed81/1000 normalized gain. No new
prime table, valuation exponent, pilot, scan or optimization search.

Generalize geometric helper guards to450^4=41006250000, retaining the
same proof structure, with root>=450 and radius/R<=521/90000. Existing
endpoint correction remains<=.001. A geometry-only log>=24 follows
from450^4=2^4*3^8*5^8 and the stated log certificates. Preserve old100b
and62.5b conclusions and old log lemmas with explicit weaker-helper
guard conversions in their callers; do not silently strengthen them.

At50b=2^10*5^11, existing Mathlib log2 and rational log5 give
logD>=24.6304. Fixed comparison:
.999997u-5.820+.081 > .8u-.813 for u>=24.6304.
New code must compose the SAME production/tail/actual-Gram sandwich
and actual-field transport, never call the old62.5b or earlier cutoffs.

Changes limited to a stronger-gain module, geometric/helper guard
generalizations in TunedRadiusFamily/TunedAnalyticCutoff, explicit guard
conversions in RecoveredAnalyticCutoff, a new50b module and root imports.
Preserve all previously frozen sources via their Git commits and archived
records; earlier review55 applies to86abe21, not these new edits.

Controls: reject dropping S guard atS1; exact endpoint factorizations;
reject the new affine comparison atlogD=24.6; retain strict inertness and
radius-rounding controls. Do not claim the endpoint/gain is optimal.

Budget: at most3 target builds,600s/8192MB per process,1200s cumulative,
stop after any resource stop. Preserve all changed mathematical sources
and raw records at each failed build before at most2 local repairs.
No weakened target, alternative endpoint search or partial-lemma success
substitution. If stopped, keep the reviewed/public62.5b cutoff current.
After acceptance: root, fresh signatures/controls/dependency exclusions
(including old62.5b roots), axiom audit, correspondence, evidence integrity,
human explanation and current documents. Exact-head CI separate. No merge,
Tao submission, full classification, novelty, human review or optimality claim.
