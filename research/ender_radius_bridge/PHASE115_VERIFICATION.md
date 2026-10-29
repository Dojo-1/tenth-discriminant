# Phase115 verification: finite checks pass; cutoff remains a candidate

Status: FINITE_CHECKS_PASS_PAPER_CANDIDATE_ONLY. This cycle has a complete
paper derivation and a passing sealed finite exact trial. It has NO new
Lean theorem, all-D machine proof, production integration or CI result.
Published h1 cutoff:50billion. Fixed paper candidate:48billion.

Registered at6fbb7a3c14465c8e03436051acbd8baa093255aa, before implementation
and execution; base47563334e5374f15d490ece98a7ed1184a6822cd. This is a NEW
monic radial row basis, not repair/replay of the stopped113or114campaigns.

## Exact execution and scope

From the research repository root:

    ./research/ender_radius_bridge/run_phase115.ps1

The saved command invokes Python3.11 with:

    python research/ender_radius_bridge/phase115_radial_centering.py --output <recorded-data-path>

One native exit0, elapsed1.6893528s; fixed cap120s and8192MB per owned
process. Sampled per-process peak20647936bytes, not a simultaneous exact
process-tree peak. No resource stop, repeat, repair, grid/threshold change,
imported old driver, external library or floating-point calculation.

All162registered matrix cases completed. They include99positive and63zero
determinants; the positive count includes empty matrices with determinant1.
No zero determinant is advertised as a positive arithmetic lower bound.
All7,770sampled jet comparisons and7,770radial-envelope checks pass.
The original and directly differentiated transformed jets give exactly
H=T G T^T, with original factor2. The explicit integer T is lower triangular
with diagonal1, inverse T_-a and checked composition T_a T_-1=T_(a-1).
Both determinant and residue ranks mod3/mod5 match. Actual odd-nonsquare
prime powers divide the original determinant at their inherited exponent.

All4,910fixed coefficient cases pass the finite hypergeometric identity
and full Leibniz bound;3,516eligible checks verify the(5/8)^s factor.
Nine explicit false-claim witnesses pass: factor2; ordinary versus divided
derivatives; center sign; missing Leibniz term; actual row norm can grow;
S1gain zero; integer-centering rounding error; singular not positive; and
the false naive h^s factor when all factors get differentiated.
These controls are finite; their passage does not discharge universal
quantifiers in the paper proof.

## Candidate endpoint certificate

Four rational logarithm certificates use100positive atanh-series terms
and an explicit geometric tail. They establish the fixed lower bounds
log2>=.6931,log3>=1.09,log5>=1.609,log(8/5)>=.46 in rational arithmetic.
The paper scale gain is at least2277/169000>13/1000. The fixed factorization
48b=2^13*3*5^9 gives logD>=24.5813 and affine margin

    (999997/1000000-4/5)*24.5813 -5.739 +.813 +.013
      =31862561/10000000000 = .0031862561 >0.

The slope is positive. No endpoint or centering search was performed.
A new Lean proof must still construct the integer row operator, derive
its same-Gram ordinary-jet action, prove the all-parameter coefficient
and uniform upper bounds, replace the geometric estimate and compose the
actual-field conclusion. In particular the existing fifty_normalized_lower
wrapper has a50bguard and is NOT applied below it; the candidate instead
needs a new composition from the450^4-domain raw lower and strong recovery
lemmas with freshly proved floor guards. No old cutoff theorem is a premise.

## Preserved evidence and verifier

PHASE115_RAW.zip contains source/data-jsonl/stdout/stderr/native-result,
exactly5files. PHASE115_RESULTS.json stores raw/source hashes and scope.
The source is byte-exact to the one executed snapshot. No source repair.
Earlier tracked evidence and production sources are frozen by Git blob
comparison, with exceptions only for current reader docs and.agent state.

    python research/ender_radius_bridge/verify_phase115_results.py

This verifier reads saved evidence, checks matrix congruence and determinants
from the recorded matrices, the rational certificates and frozen Git blobs.
It NEVER imports/executes the trial or reconstructs its jet/coefficient grid.
Its PASS confirms preserved finite evidence, not a new checked cutoff.
No Lean/root build, new CI, publication, merge, reviewer or Tao posting.

[Short human guide](RADIAL_CENTERING_GUIDE.md) ·
[Full paper derivation](RADIAL_CENTERING_DERIVATION.md) ·
[Preregistered protocol](PHASE115_PROTOCOL.md).

Remote reconciliation: a read-only git fetch found main still at
4b2492f11a1b3d2bf7831eb15487504865a8ff88. No new review-folder or
TAO_OBJECTIVE_AUDIT.md change appears on main relative to published source
7913eba. The pinned production branch remains7913eba. This is not evidence
about an unpublished or still-running external review.

Reader verification: 558 relative file links resolve across the nine
current reader documents. README and the objective ledger remain61lines.
