# Phase123: reconstruct the actual two-sided arithmetic bridge

Base182ea000b901a1bebc98992b22ffb3a80cd53c56, after Argon's published
review06d3986 of frozen39e9ce3. All173reviewed modules are unchanged;
current202module source and its separate CI are not independent review.
This is a NEW exposition/definition-level check cycle. Phase122 remains
stopped, byte-exact and unrepaired. No Lean invocation or proof promotion.

## Deliverables and exact scope

Write one concise human derivation from original integer derivative rows:
A=Z[t]/(t^2+D); ordinaryZderivatives withWfixed; E includes both coordinates
at every original sample/derivative; B repeats(2,2D); G=E B E^T is the
existing integerRectangularTraceGram. Selected order is not assumed maximal.

For odd primep with-Dnonsquare modp, derive z^p=conjugate(z)modp for all
selected-order samples. Every ORDINARY derivative ofX^p-W has apfactor,
including derivativep; Leibniz then gives p^k for every jet of B0*(X^p-W)^k.
For row(r,s), k=min(floor(r/p),S-1-s). Its binomial expansion stays inside
the original rectangle and defines unitriangular integerU_p. Construct
integral quotient coordinates Ehat explicitly sample by sample. Establish
U_p E=Delta_p Ehat, hence U_p G U_p^T=Delta_p K Delta_p with
K=Ehat B Ehat^T INTEGRAL. Shared pivot receives p^(2k), not merely p^k.
Sum weights by reflecting s; detU_p=1 gives p^(2valuationWeight) dividing
SAME integerdetG. Separate positivity/count, maximal-order class-number
input and geometric estimates from this purely local factorization.
Match every step to exact existing Lean declarations. Include empty rows,
empty samples/derivatives, absent local congruence, divided-derivative and
one-sided-pivot failures. No new cutoff or novelty claim from this cycle.

## One sealed definition-level arithmetic check

Implement a NEW standard-library Python oracle from the displayed formulas,
without importing production or prior trial drivers. Fixed local pairs:
(D,p)=(1,3),(19,3),(2,5),(1,7). Fixed rectangles:
(R,S)=(0,2),(2,0),(1,1),(4,2),(9,3). For each use J=0,1,p,p+1.
Fixed distinct originalQ={(0,0),(1,0),(0,1),(1,1),(-1,1)}.
Exactly80cases; no grid/threshold changes. Construct direct polynomial
products and ordinary derivatives separately from binomial matrix action.
Check Frob coordinates, jet action, integral quotient coordinates,
G=E B E^T, UGU^T=Delta K Delta, detU=1, exact determinants and reflected
weight sum. Include zero determinants; never infer positivity from them.

Fixed negative controls: [p] has divisible row/column but not p^2det;
D2,p3 violates the missing nonsquare/Frob premise; third Hasse derivative
ofX^3 atzero is1 while ordinary derivative is6; dropping originalfactor2
changes the constant-row Gram from2cardQ (fixed controlJ=1). No hypothetical stronger
valuation or cutoff is accepted by finite cases.

ONE Python invocation,60seconds total; subprocess timeout stops it.
No repair/retry/hidden pilot after mathematical, implementation or resource
failure. Record exact script, stdout/stderr, native result, elapsed time
and hashes. Memory is NOT measured or claimed bounded by this harness;
small fixed dimensions are a workload bound, not a peak-memory measurement.
Archive failed outcomes too. Reading/verifying saved results is not replay.

This cycle may update the current short guide/navigation with the derivation,
but freezes all Lean modules, pins, workflows, old evidence/protocols/reviews.
Register any successor47.5bproof, classification interface, radial law or
exact frozen Lean replay separately before execution. Full six-part goal
remains active beyond this slice. No new reviewer, automatic merge or Tao
posting is authorized. Public review findings remain exact-version scoped.

Pre-implementation correction: the initially written2cardQ*J was not an
exact constant-row identity forJ>1: positive derivatives of1 vanish.
The corrected negative control usesJ=1 and exact2cardQ. This was caught
during definition-level reasoning before any oracle code or execution.
The original protocol remains preserved in commit25db00e.
