# E42 — ALL ORIGINAL MAXIMAL MINORS KEEP THEIR PRIME FACTORS

*19 November 2026 · exact integral source-row theorem candidate.*

## Universal conditional statement

Let E be the SAME integer n x m ordinary-jet source evaluation
and F its integral row quotient. Suppose

    U E = diag(d_i) F,
    det(U)=+1 or -1,

with U an integral matrix. For EVERY choice of n columns
(including repeated selections, whose determinant is zero),
the corresponding maximal square minor obeys

    product_i d_i | det(E[:,columns]).

If p divides product_i d_i, no n-column minor can be
nonzero modulo that same p. In particular the same E cannot
have full row rank mod p when extraction has positive
p-content. An auxiliary q != p may still detect full rank.

This is an algebraic result about all actual E columns
when hE is source-supplied. The existence of such E/U
from a particular original thin ellipse remains an
explicit independent proof obligation.

## One complete source-matched finite experiment

The actual original source is
    Q={(1,0),(6,0),(11,0)}, D=25, J=1, R=3, S=1.

Its integer ordinary-jet evaluation and exact
positive trace column metric are

    E=[[1,1,1],[1,6,11],[1,36,121]],
    B=diag(2,2,2).

The theorem checks on the actual Tenth source definition

    E B E^T =
       integerRectangularTraceGram Q 25 1 3 1.

The extracted polynomial basis U for
(1,Z-1,(Z-1)^2) is unimodular:

    U=[[1,0,0],[-1,1,0],[1,-2,1]], detU=1,
    d=(1,5,25),
    F=[[1,1,1],[0,1,2],[0,1,4]],
    U E=diag(d) F.

The selected square evaluation determinant is exactly 250,
divisible by 5 and NOT divisible by 7. Thus SAME E, two
distinct modular jobs:
    mod5: the original E loses row rank;
    mod7: a nonzero determinant witnesses full row rank.

Neither is a claim about inertness of 7 in the relevant
quadratic field; D=25 is not a fundamental discriminant
parameter eligible for the 307^4 theorem.

## Relation to issue #51

This supplies the general all-maximal-minors factor
theorem requested in the external two-prime method
comparison, plus an explicitly source-matched internal
integer-jet example. It does NOT import any external
author's different evaluation matrix, selected complex
minor or auxiliary-prime class number argument.

The distinction between a FULL positive Gram determinant
and a SINGLE selected minor remains load-bearing:
the Gram is a weighted sum of squared maximal minors
under a correctly typed source E and diagonal B.
An upper estimate of one selected minor cannot bound
the full Gram above.

## Release floor and kill conditions

E42 is a Lean proof CANDIDATE until exact-head focused
and full-root allowed-axiom checks pass. Even after that,
the large thin-ellipse E_Q and proof of correct auxiliary
prime existence remain open.

Reject any source change, same-prime rank assertion
contradicting a positive p-content row extraction, or
inequality direction mixing a selected minor with the
full original Gram.

No new 307^4 bound, external proof equivalence, ETH or
P-vs-NP inference follows.
