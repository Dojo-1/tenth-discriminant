# Radial frame: integrated operator, candidate size bound

**The integral radial operator is now integrated unchanged into the Lean
library and published in merged PR41.** Module build, full build, fresh
dependency checks and whole-library audit passed on their first invocations.
Pinned proof CI and same-head security passed before merge. Source, tested
merge and actual merge have identical trees. [Exact receipt](PR41_MERGE_RECEIPT.md).

The transformation changes the polynomial observations at the same points:

    Z^r W^s -> Z^(r-m) W^(s-m) (ZW-a)^m, m=min(r,s), a integer.

Its explicit integer matrix T has diagonal 1, determinant 1 and an integral
inverse. Directly differentiating the new polynomials agrees with applying
T to every old ordinary jet, with W held constant. The actual new integer
Gram is H=T G T^T and detH=detG. Its real cast and original prime divisor
therefore remain anchored to the original arithmetic object.

Real positive definiteness keeps the original point-count/depth guards.
Modulo every prime, including 2, the old and new Gram ranks agree. This
compares the two frames within each characteristic: it does not assert
that reduction preserves real rank or positive definiteness.

Individual row norms and polynomial multiplication can change. The
candidate improvement is a smaller UNIFORM geometric upper estimate.
The stronger0.013 saving remains paper. The sufficient0.010 gain now closes
the [FULL actual-field48-billion theorem](FORTY_EIGHT_BILLION_GUIDE.md)
standalone, including arithmetic lower bound, fixed endpoint and actual-field
transport. Unchanged integration and pinned CI remain. The published
integrated cutoff is **50 billion**.

The whole audit reports 5,450 logical declarations and 4,644 theorems.
Its 57 new logical declarations are exactly the radial-operator namespace;
no earlier logical declaration disappeared. All 27 public statements, six
definitions and proof bodies are unchanged from the accepted standalone
source. Runtime auxiliaries are recorded separately.

[Understand the operator and guards](RADIAL_OPERATOR_GUIDE.md) ·
[Exact integration evidence](PHASE117_VERIFICATION.md) ·
[Quantitative paper candidate](RADIAL_CENTERING_DERIVATION.md).
Published merge: e74028a; source: ab5558f. Phase120 now checks the full
actual-field48-billion theorem standalone; it has no new production import or CI.
No full classification, optimality or independent-review claim.
