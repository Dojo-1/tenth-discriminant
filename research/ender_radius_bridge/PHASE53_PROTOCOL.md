# Phase53: a fixed uniform normalized gain from recovered3/5 mass

Base published9154317; existing CI40290045330 is live and security analysis
passed. No push/cancel/restart while that run is live. No extra agent.

Fixed target, chosen before execution: if S>=100 and25*S<=R<=26*S, prove
`3/50 <= (recoveredPrimeMassLower R S I-certifiedPrimeMassLower R S I)/
comparisonScale R S` for every real tail parameter I. Also supply the
implied raw-normalized lower bound plus3/50. This is a scaled budget gain,
not a new numerical discriminant cutoff.

Method: count rows r>=p*S, where each min(floor(r/p),t) equals t, to prove
the generic Nat lower bound `(R-p*S)*S*(S-1) <= 2*valuationWeight R S p`
for p>0. Use p=3,5 and the existing rational log2 certificate to obtain
log3>=1 and log5>=1. The coarse dimension bounds give a numerator at least
(2079/50)*S^3 and scale at most676*S^3, enough for3/50 without searching
parameters or evaluating new prime tables.

Controls: reject dropping p>0 using p=0,R=4,S=2, and reject dropping the
lower-S guard altogether using R=25,S=1 (zero recovered gain). Do not
claim100 is sharp or necessary. Natural subtraction/cardinality guards
must be explicit when casting to reals; do not replace floors by reals.

Budget: at most3 builds,600s/8192MB per process,1200s cumulative, stop after
any resource stop. Preserve each failed full source/raw record before at
most2 local elaboration repairs. No numerical pilot, parameter scan,
inherited proof edits, weakened target or fallback success. New module
and root import only. After acceptance: root, signatures/controls/axioms,
source correspondence and evidence integrity; future exact-head CI separate.

Existing tail, class-number/inertness and geometric/floor/ceiling guards
remain necessary to apply the production budget to the actual Gram.
A new endpoint requires a later separately registered proof. Preserve
the unchanged10^11 cutoff and distinguish that from this fixed positive
gain. No classification, novelty, optimality, higher-class-number, review,
merge or Tao-submission claim.
