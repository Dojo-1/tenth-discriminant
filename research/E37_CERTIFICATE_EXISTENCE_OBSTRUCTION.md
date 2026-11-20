# E37 — CERTIFY THE SOURCE, OR REFUSE THE PRIME

19 November 2026 · source-integrity research draft.

## Critical correction: the generic theorem was already there

GramDivisibility.lean already proves generic n-row determinant
divisibility under an integer unimodular two-sided diagonal factor.
RectangularGramFactor.lean already constructs the original ordinary-jet
factorization under explicit pointwise Frobenius congruences.
RankDivisorCompatibility.lean already covers every maximal minor of
the unchanged rectangular observation matrix.

Do not claim novelty for the generic n-row theorem. E37 specifically
tests when its hypothesis DOES and DOES NOT hold on original sources.

## Positive original-source certificate

D=25,J=1,R=2,S=1, Qshift={(1,0),(6,0)}.

    Gshift=[[4,14],[14,74]], det=100
    U=[[1,0],[-1,1]], det(U)=1
    d=(1,5), K=[[4,2],[2,2]]
    U Gshift U^T = diag(d) K diag(d).

Existing generic GramDivisibility then gives 25 | det(Gshift).
This keeps the ORIGINAL Qshift and original ordinary-Z derivatives.

## Universal negative certificate

For E31 Qunit={(0,0),(1,0)} the original Gram determinant is 4.
E37 proves no integer two-by-two matrices U,K can satisfy BOTH:

    det(U)=1
    U Gunit U^T = diag(1,5) K diag(1,5).

Otherwise the existing generic theorem gives the contradiction 25|4.
This rules out EVERY det-one certificate of this prescribed shape,
not just a particular proposed U.

## Fake terminal matrix

V=[[1,0],[0,5]], det(V)=5, produces the same terminal Gram from
Gunit with original determinant 4 as the valid U from Gshift with
original determinant 100. V is excluded by the unimodularity gate.

## Future source-specific frontier

The canonical full rectangular prime valuation already exists under
the inert-prime/Frobenius premise. New work must independently check
the 307^4 thin support, prime-by-prime hypotheses and same-Gram
upper/lower chain. Split/ramified controls and both maximal-order
charts are mandatory. No stronger cutoff follows from E37.

Evidence [H] until exact-head focused and full-root CI/axiom audit.
No ETH/P-vs-NP, p-adic infinite theorem or new geometric holonomy
claim is established here.

Kill any certificate relying on altered Q, nonunimodular scaling,
a substitute Gram/minor, Hasse jets in place of ordinary derivatives,
or HK's unconjugated trace instead of the original positive metric.
