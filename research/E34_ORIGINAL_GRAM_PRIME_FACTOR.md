# E34 — THE ORIGINAL GRAM DECIDES

**19 November 2026 · research-only, stacked on E33.**

## Exact source contract

Reuse the **real original source object**
integerRectangularTraceGram Q D J 2 1, with rows (0,0),(1,0),
ordinary Z-jets holding W fixed, integer coefficient pairs, and
trace weights (2,2D). Nothing is substituted for this Gram.

## New sufficient source entry factorization

For any integer p and two-row Gram
G = [[a,b],[c,d]], if

    p | b,   p | c,   p² | d,

then, by the original two-by-two determinant,
    p² | det G = a*d-b*c.

The Lean theorem original_two_row_gram_prime_factor is conditional
on those precise entry facts for the ACTUAL original Gram at Q,D,J.
It is **not** an unconditional consequence of a nontrivial kernel
in the index-k coefficient map.

## Positive and negative sampled controls

The source algebra is the same D=25 at J=1, R=2, S=1.

    Q_unit = {(0,0),(1,0)}
    Q_five = {(0,0),(5,0)}.

Both contain two distinct original integer lattice points.
Their actual complete integer Gram matrices are:

    G(Q_unit)=[[4,2],[2,2]],      det=4;
    G(Q_five)=[[4,10],[10,50]],  det=100.

For Q_five, 5 divides both offdiagonal entries, 25 divides
the second diagonal entry, and 25 divides det(G). The theorem
connects the row-factor certificate to the FULL same-source
integer Gram and not a convenient auxiliary minor.

For Q_unit, 5 does not divide det(G) even though the ambient
conductor-five frame has a nontrivial mod-5 kernel (E31).
**Same sample cardinality is NOT the same arithmetic source.**

E24's index-five embedding transports G(Q_five) without changing
the actual matrix only if the entire support is transported along
the same integer order inclusion.

## Why this does not sharpen 307^4

The two-point source does not satisfy the large thin-ellipse support
or field/class-number premises. This example only proves how
arithmetic source information CAN yield an actual Gram factor
when the **original jet image row** has the needed divisibility.
There is no new p-adic exponent on the 307-source thin Q.

A viable next theorem must prove source-locked integral extraction
    U E_Q = Delta_p F
with U unimodular, F integral, and E_Q the ORIGINAL complete
ordinary-jet matrix, followed by a certified positive trace identity
    G_Q = E_Q B E_Q^T
with B unchanged. Then det(G_Q) can inherit squared row-extraction
factors. E34 is only the first small n=2 gate.

## The independent bridge mismatch (HK-034)

HardnessKernel.GaussianPrime.gpair(x,y) computes 2 Re(x*y),
while Tenth.integerPairTrace(1,a,b) computes 2 Re(a*conj(b)).
The positive Gram must use the CONJUGATED second argument in any
cross-repository dictionary. A direct identification is false at
x=y=i (-2 versus +2).

## Evidence discipline

E34 remains a proof candidate until exact-head focused and full-root
Lean/axiom/negative-control checks. E31 must remain a negative
control; Phase350 307^4 is separately formal-green and still requires
independent semantic human review. Keep all such differences explicit.

**Kill rule:** any valuation that disappears after restoring the original
Q, derivative order, trace pairing, or full Gram is retired.
