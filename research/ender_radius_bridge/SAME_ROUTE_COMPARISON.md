# Three ways to spend the same determinant argument

In brief: our direct analytic bound is weaker than the two selected
writeups. Our contribution is the checked arithmetic-to-geometry chain
and finite canonical-field theorem, not a better analytic number. The
elementary companion suggests a focused future proof-port study; the
smaller `570` comes with a substantially heavier analytic dependency chain.

Phase40 is a bounded source comparison, preregistered in commit
`945b149`, not an independent audit or a new proof. Our mathematical
snapshot is `f1638018085b0167dedd6f7ef13d69dedd51f148`; both external
manuscripts are frozen at `44c7d6fcd8737df8a65cc13024677a14e4e451fb`.
The [source manifest](PHASE40_SOURCES.json) identifies all seven files read
in full, their original-byte hashes and immutable links. No external code
was run. The two manuscript blobs equal those at our earlier prior-art
anchor `95e8fe68da05790b99d828b5b6aff3f6dc479aa2`.

## The shared mathematical picture

Class number one turns small prime ideals into principal ideals, hence
into constrained quadratic norms. A nonzero integer built from ordinary
derivatives is then viewed in two ways: inert primes force divisibility;
complex size limits how large it can be. A contradiction appears when
the first budget exceeds the second. The useful comparison is *where
each proof gets nonvanishing and where it spends its analytic effort*.

All three use rectangular monomial labels and the relation
`z^p = conjugate(z)` at inert primes. They do not use the same integer
determinant. Our positive trace-Gram determinant is not interchangeable
with the squared norm of an arbitrarily selected interpolation minor.
Their constants must travel with their definitions.

## Comparison, with evidence classes kept separate

External results and review statuses below are **source-reported claims**,
not newly certified here. Our local checks and exact-head remote CI are
also separate; consult the publication verification record in draft PR28.

| Question | Our checked canonical-field route | Elementary companion | v6.1 |
|---|---|---|---|
| Parameter and direct analytic bound | Positive squarefree radicand `d`; both `d<2e11` and actual absolute field discriminant `q<2e11` | Absolute fundamental discriminant `q<32768` | Absolute fundamental discriminant `q<570` |
| Nonvanishing | Characteristic-zero jet uniqueness, ellipse cell-area count, positive trace-Gram; no auxiliary prime needed for rank | Auxiliary inert prime `R` in `(q^4,q^5]`; distinct nodes modulo `R`, multiplicity versus degree | Auxiliary inert prime in certified scale intervals; same finite-field rank mechanism |
| Geometry and dimensions | Selected lattice `x+y*sqrt(-D)`, ellipse/disk cutoff `rho`; `R=floor(D/4)`, `S=floor(R/20)`, `J=S`, `rho=ceil((11/20)*D^(3/4))` | Rectangular grid in the full integer ring; `S=floor(R/12)`, `J=ceil(R/48)`, enclosing radius `2*sqrt(R*sqrt(q))` | Disk in full integer ring; `S=floor(3R/64)`, `J=ceil(R/9)`, radius `sqrt((27/64)*R*v/pi)+rho`, `v=sqrt(q)/2`; its `rho` is the cell covering radius |
| Integer and normalization | Actual integral trace-Gram, `2*sum Re(row*conjugate(row))`; ordinary derivatives | `Delta = D0*conjugate(D0)` for one nonzero square minor; ordinary derivatives, no factorial division | Same minor-norm construction; ordinary derivatives, with factorial/Hasse bookkeeping in stronger valuation estimates |
| Prime-divisibility budget | Unitriangular row action, coordinatewise lifting and two-sided integral Gram factor; checked prime-mass assembly | Basic triangular Frobenius row action, including prime two; norm doubles row valuations | Basic action plus compatible higher Frobenius factors, residual/coupled gains and split/column factorials |
| Final comparison | Factorial/Legendre prime-mass lower bound versus counted Hadamard upper bound; four checked prime-log constants; affine envelopes cross for `log D>=26` | Elementary prime estimates and split-norm count; one uniform endpoint contradiction | Smoothed noninert-prime sum, eight finite refinements, positive averaging kernel, norm Euler product and explicit Poisson errors; five rational bands |
| Additional inputs | Generic Mathlib number-field/PID/Minkowski infrastructure, proved arithmetic/geometry bridges and kernel-checked finite constants | Standard quadratic ideal theory, finite fields, Hadamard and elementary analysis; factorial/binomial prime estimates proved in manuscript | Rosser--Schoenfeld estimates, classical analysis/special functions; published v5 for `q>=2000` (its README also identifies the v4 tail dependency) |
| Finite endgame | Full original interval below `7e11` checked by the unchanged certificate; nine actual positive class-number proofs, giving canonical-field iff | Source reports 4,095 necessary candidates, primes through31, then reduced forms for nine positives | Source reports70 necessary candidates, primes through109, then reduced forms for nine positives |
| Review/formal status | Lean checks; internal provenance and adversarial controls; independent human semantic/API/upstream review open | No formal verification; owner reports independent verification, but no reviewer identity or detailed report supplied | No formal verification; independent mathematical audit explicitly pending; earlier version reviews do not cover v6 |

For the parameter conversion, `q=d` if `d=3 mod4`, otherwise `q=4d`.
Thus the lists `1,2,3,7,11,19,43,67,163` and
`3,4,7,8,11,19,43,67,163` describe the same canonical fields, not a
disagreement. Our actual-discriminant theorem makes the analytic bounds
numerically comparable in `q`; it does **not** make the proof mechanisms,
review status or computational burdens equivalent.

The prime endpoint is also part of the interface. The external notes use
the strict obstruction `p<q/4`. Our odd-chart bridge proves the sharper
strict integer threshold `p<(D+1)/4`; `R=floor(D/4)` lies below it when
`D=3 mod4`. Neither argument licenses replacing a strict inequality by an
inclusive endpoint. In our analytic assembly prime two is handled by the
separate parity argument, not added silently to the odd-prime product.

## What this teaches us

Our direct analytic threshold is substantially weaker than **both**
selected source claims, including the simpler elementary proof. The
factor3.5 improvement is real but is not evidence that our arrangement is
near optimal. Conversely, quoting the classification consequence `d<=163`
as our analytic cutoff would erase the very comparison Tao asked for.

The elementary note is the most focused candidate for a future bounded
proof-port study: replace our characteristic-zero rank/count route by its
auxiliary-prime rank argument, and prove the required prime's existence
from norm counts. This is an inference from the architecture, not a
demonstrated improvement or an authorized change of theorem assumptions.
It would need a new preregistration; none of its constants is imported here.
V6.1 instead shows several additional optimization opportunities, but
porting its `570` would also require its earlier-version tail and analytic
certification chain. Reading its five bands does not close that dependency.

This answers one controlled part of Tao's comparison invitation. It is
not a survey of every writeup, an optimality result, independent review,
a higher-class-number result or a general Siegel-zero theorem. The root
README's separate Weber reconstruction uses modular machinery and is
outside this preselected same-route comparison. No submission was made.

## Primary-source anchors

- [Elementary proof](https://github.com/twinheterodox/tenth-discriminant/blob/44c7d6fcd8737df8a65cc13024677a14e4e451fb/companions/elementary/proof.tex): lines44–87 (parameter/endpoint),90–222 (prime estimates and auxiliary prime),224–415 (determinant and contradiction),417–483 (finite finish and status).
- [Elementary review record](https://github.com/twinheterodox/tenth-discriminant/blob/44c7d6fcd8737df8a65cc13024677a14e4e451fb/companions/elementary/REVIEW.md): independent-verification section explicitly limits the supplied review evidence.
- [V6.1 proof](https://github.com/twinheterodox/tenth-discriminant/blob/44c7d6fcd8737df8a65cc13024677a14e4e451fb/versions/v6.1/proof.tex): lines36–51 (parameter/tail),259–306 (matrix/rank),308–575 (valuation),792–984 (averaging/certification),986–1050 (finite finish and limits).
- [V6.1 review record](https://github.com/twinheterodox/tenth-discriminant/blob/44c7d6fcd8737df8a65cc13024677a14e4e451fb/versions/v6.1/REVIEW.md): pending review and explicit audit targets; review record is retained from v6.0.
- Our [analytic proof](ANALYTIC_CUTOFF_OPTIMIZATION_GUIDE.md), [classification guide](CLASSIFICATION_GUIDE.md) and [input map](PROOF_INPUT_GUIDE.md) distinguish theorem, finite evidence and provenance.
- [Tao's original challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/), re-read25 October: optimize and compare particular approaches, including informative larger bounds and clean human-verifiable arguments; do not prioritize speed or suppress attribution.
