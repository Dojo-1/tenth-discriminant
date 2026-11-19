# E39 — SAMPLE SEPARATION, NOT AN ABSOLUTE COORDINATE

19 November 2026, source-exact ordinary-jet experiment.

## Problem

E31/Qunit, E34/Qfive, and E36/Qshift have equal cardinality,
the same integer trace pairing and the same two-row ordinary
Z-jet convention, but opposite p=5 determinant behavior.

Why does translating every original sample leave the arithmetic
determinant alone although the raw second-row jets change?

## Source-exact theorem target

For any D and DISTINCT real integer samples x,y, let
Qxy={(x,0),(y,0)}, J=1,R=2,S=1.

The two actual original ordinary-jet rows are 1 and Z. The
original positive integer trace pairing on real samples has
weight two. Thus E=[[1,1],[x,y]], B=2I, and

    Gxy = E B E^T
        = [[4, 2(x+y)], [2(x+y),2(x^2+y^2)]].

Therefore det Gxy = 4*(y-x)^2.

This is neither a newly selected minor nor a replacement
floating-space Gram. The Lean file attempts to establish the
identity directly for integerRectangularTraceGram on the
ACTUAL original Finset Qxy, with explicit distinctness.

The separation criterion gives:
    p | (y-x) => p^2 | det Gxy
for arbitrary integer p. It does not assert the converse
at the ramified prime two or on arbitrary complex supports.

## Moving frame, not resampling

For any integer c, define Uc=[[1,0],[-c,1]]. This matrix is
unimodular. It implements the legitimate integer row basis
(1,Z) -> (1,Z-c).

The exact covariance target is
    Uc G(x+c,y+c) Uc^T = G(x,y).

This is a comparison between two distinct source supports
with their explicit coordinate transformation tracked. It
does NOT make those supports literally equal. In particular
the determinant is invariant because det(Uc)=1.

## Controls

- Repeated x=y must collapse to one sample in the original
  Finset; treating it as two independent columns is INVALID.
- E31 Qunit=(0,1) => det4, no p5 divisor.
- E34 Qfive=(0,5) => det100.
- E36 Qshift=(1,6) => det100 under a valid unimodular shift.
- Nonunimodular V=diag(1,5) can manufacture the same terminal
  matrix from det4 source, but does NOT preserve its determinant.

Independent bounded integer oracle: 4,620 cases (distinct x,y
from -10..10 and c from -5..5) passed det and moving-frame
checks. This supports only the bounded computation, not the
general Lean statement.

## Evidence and next frontier

The general separation formula is elementary matrix algebra.
The attached E39 Lean source is [H] until exact-head
compilation/allowed-axiom audit succeeds. A fully compiled
proof would certify it for every distinct integer x,y,
not merely the 4,620 checked triples.

This is a two-real-sample case. It is not the large thin
complex ellipse used in the 307^4 field theorem. The full
original-source n-row inert-prime Frobenius bridge already
exists under explicit hypotheses; no novelty claimed for
that prior theorem.

Next task: identify which higher-dimensional original sampled
jet lattices admit a source-certified analogue of this
Vandermonde separation invariant, and compare its prime
factorization under unimodular row frames and matched nulls.
