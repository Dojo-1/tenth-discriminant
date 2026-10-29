# Phase119: a smaller upper bound on the same integer determinant

Register before new source or invocation. Base39e8eaf2d9ccf008671ecc93abcc7477c98194a3,
branch codex/radial-jet-majorant, secondary checkout. Primary cache/source
stays ab5558ff7b482a6bec185b37115b6faf57a82c28. Published PR41 mergee74028a
has passing exact-head and automatic postmerge CI; those runs do not check119.

## Fixed mathematical target

Start from the ACTUAL RadialOperator.gram, zsqrtdJetGram and integerJet.
Prove its real diagonal is2 times the sum of squared norms of the ACTUAL
RadialJetMajorant.jet over unchanged q in Q and j<S. The trace pairing,
ordinary derivatives, original rectangle and selected quadratic order stay
unchanged. No substitute integer matrix, real orthogonal lattice change,
new valuation, supplied quantitative bound or assumed positive determinant.

Use accepted118 to bound every diagonal by the original uniform radial
majorant, multiplied by (13/20)^(2s) exactly when r>=9S. Every other row
retains factor1; high derivatives vanish. Bound logs only under the original
point-count/depth guards giving positive definiteness. Retain the exact
factor2, max(1,r/rho) correction, positive sample-count bound, integer radius,
and original row-major indexing.

Prove the exact sum of penalties over the rectangle is
 (R-9S)S(S-1)log(20/13),
with natural-number truncation and explicit zero/empty cases as applicable.
Use ordinary Hadamard plus the existing logarithmic sum/integral bound to
prove, for the SAME G=integerRectangularTraceGram Q D S R S,
 log(detG) <= enderUpperB R S S rho n -(R-9S)S(S-1)log(20/13),
under D>0,R,S>=1,rho>=5,rho<R,Q.card>2(R-1)+(S-1),
norm(pairEval D q)<=rho for q in Q,n>0,Q.card<=n. No class-number premise.

For S>=100 and25S<=R<=26S, derive the sufficient normalized improvement
 log(detG)/(R^2 S) <= enderUpperB/(R^2 S)-.010.
Finally instantiate Q=ellipsePairs D rho with the UNCHANGED production
Tuned.R, Tuned.S, Tuned.rho and padded upper sample count, for EVERY
D>=41006250000. Reprove the required floor/aspect/centering/cardinality guards
from existing definitions and geometric lemmas. Obtain the actual integer
determinant upper bound normalized by the same comparisonScale:
 log(detG)/comparisonScale <= .8logD-.823.
This is the full119 target, not acceptance of coefficient/row identities alone.
It still leaves recovered lower comparison, endpoint certificate and actual
field48b theorem, unchanged integration and exact-head CI before a new cutoff.

## Reuse, fixed controls and evidence

The successful118 namespace body is copied BYTE-EXACT as a local dependency
in the new standalone source, since it has no installed production import.
Its reports are not copied; its19 types/2 data bodies/proofs remain exact.
This necessary dependency compilation is not a standalone118 replay for style.
No old118 file, production file/root or stopped113/114 source is edited.

Fixed same-source controls: constant row factor2; empty row rectangle det1;
the singleton Q={(0,0)},D=3,R=S=J=1 has actual determinant2; an empty sample
set with nonempty rectangle has determinant0, so no positive-log theorem is
claimed there; centered Q11 at the origin has norm-square144 at rho5,a12,
while the old observable has value0. S=1 has zero aggregate penalty; the
penalty sum is0 if R<=9S. Preserve these witnesses against dropping factor2,
assuming pointwise row domination or ignoring positivity.

Freeze every new public type and complete data definition before first call.
At most2 proof-only repairs/private helpers; no weakened target or removed
control. Every new public type, whole new namespace, and three fresh closures
(actual diagonal, same-integer logarithmic bound, production normalized bound)
are checked, excluding the same70 old roots and all nonstandard axioms.
Only propext, Classical.choice and Quot.sound are permitted.

## Resources and stop rule

At most3 full standalone Lean invocations,600s/8192MB per owned process,
1200s cumulative, default heartbeat/recursion limits unchanged. STOP permanently
on any inner/outer resource stop; no remaining-slot use, probes, rescaling or
limit increase. No numerical trial, old experiment replay, root build,
integration, CI dispatch, publication, new reviewer or Tao posting in119.
Preserve each full source/stdout/stderr/result before repair and exact diffs.
After terminal outcome archive raw evidence, write a read-only verifier,
update current README61/STATUS/FORMALIZATION/objective ledger61/reply and a
short human guide. Freeze earlier Git blobs except current readers/task state.
The published bound remains50 billion until the full new actual-field proof
and integration/CI pass. Goal remains the stronger justified bound, not merely
compatibility of another coordinate frame.
