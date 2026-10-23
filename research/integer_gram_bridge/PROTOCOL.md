# Registered bridge attempt — one Gram matrix in two coordinate systems

Registered on 23 October 2026 before editing Lean proofs or running a new
bridge control. Base: merged `main` at `c77049288e0eac33f72739b255d8254ff3e6aca1`.
This is a new bounded proof bridge, not a change to `flow/PREREG_ENDER.txt`,
its parameters, certificates, or cutoff.

## Exact target

Represent `x + y sqrt(-D)` by the integer pair `(x,y)` with multiplication
`(a,b)*(c,d) = (ac-Dbd, ad+bc)` and conjugation `(a,b) -> (a,-b)`.
For the existing full `ellipsePairs D rho`, define the ordinary derivative
row with coefficient `r.descFactorial j`, zero for `j>r`. Pair it by
`2*(ac+Dbd)`, sum over the same points and `j < J`, and use the same
row-major labels `(i/S,i%S)` as `rectangularTraceGram`.

Prove in Lean, without assuming the intended equality, that casting every
entry of this integer matrix to `Real` gives the existing
`rectangularTraceGram (ellipsePoints D rho) J R S`. If feasible in this
bounded slice, prove the corresponding determinant equality after casting.
The commuting path must be explicit: integer-pair multiplication and
conjugation transport to complex multiplication and conjugation under
`latticePoint`, and the integer pairing transports to the existing
factor-of-two real trace entry. This is a coordinate identity, not an
appeal to geometric intuition as a proof premise.

## Controls, falsifiers, stop rule

Keep the origin, negative coordinates, ellipse boundary, ordinary `Z`
derivatives with `W` fixed, `j>r` zero columns, factor two, conjugation and
row order. A small exact matrix control must detect at least one dropped
normalization or column; if a planted mismatch survives, the bridge fails.
Duplicate points in arbitrary Python inputs are outside the finite-set
target; for positive `D`, `ellipsePoints_card` already proves injectivity.

Use Lean 4.19.0 and pinned Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`. Run source
correspondence, full build, compiled axiom audit and negative controls for
the source change. Preserve exact errors and negative outcomes. Stop short
of asserting equality with every Python input list until ordering and
duplicate semantics are separately checked. Do not infer inert-prime
divisibility, a valuation lower bound, the analytic contradiction, or a
class-number classification from matrix identification alone.

## Local result and preserved failure (23 October 2026)

The entrywise, matrix, determinant-cast and count-conditional positive-integer-
determinant theorems compiled with pinned Lean 4.19.0. The asymmetric `D=3`
single-point control checks all four matrix entries `[[2,6],[6,24]]` and
determinant `12`; a determinant-only check would miss the off-diagonal sign
mutation described in the human guide. `lake build` and
`python verify_sources.py` passed. The latter verifies source/endpoint
identity, not the saved Arb inequalities.

The sequential local Windows `python audit.py` run is **not a full pass**.
Its compiled scan reported `AUDIT_OK` with only `propext`, `Quot.sound` and
`Classical.choice`; import closure and several apparatus controls passed.
The wrapper then exited 1 when `apparatus_controls.py` exceeded its 240-second
subprocess limit. This failure remains recorded even if Linux CI passes.

The sequential local Windows `python negative_controls.py` run is also **not
a full pass**. Its completed probes rejected the false endpoint, coverage,
Gram-normalization and derivative claims as expected, but the wrapper exited
1 when `multiplicity_negative_controls.py` exceeded its 120-second subprocess
limit. Pinned Linux CI is still required; neither timed-out wrapper is
silently counted as green. No historical Ender certificate or cutoff was
changed.
