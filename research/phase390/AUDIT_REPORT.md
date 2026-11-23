# Phase390 — original ordinary-jet Gram / maximal-order semantic audit

**23 November 2026. Scope frozen to Phase360 SHA `e720d2679e9292e101a39afd8f1b7720863e42f5`.**
This is an AI-assisted, independently *structured* arithmetic reconstruction, **not an independent human number-theoretic referee**. It does not alter the published `322^4` main theorem or promote the unified `302^4` research theorem. External issue [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains OPEN.

## Verdict

The bounded tests found **no mismatch** in the original full rectangular integer trace Gram when the *same physical sample set* is transported from the source suborder into the maximal-order chart. All six finite Gram matrices match, and a nontrivial 36-row source Gram satisfies the existing local binary, 3-adic and 5-adic exponent lower bounds. We also verified the fourth-root-302 original-ellipse count and the scalar switch from negative (301) to positive (302). Two dangerous overgeneralizations were explicitly falsified: replacing Q with the full maximal-order lattice changes the Gram, and changing the strict norm/inert-prime cutoff p<c to p<=c includes split primes. These results constrain the independent review, **but do not close the production high-jet valuation or actual-field correspondence obligations**.

## Exact claim under review

For a totally complex degree-two field K of class number one, Phase359 asserts

    |disc(K)| < 302^4 = 8,318,169,616.

The proof uses one auxilliary integer `det(G_Q)`, with

    Q = {(x,y) in Z^2 : x^2+D*y^2 <= thinRadius(D)^2},
    R = floor(D/4), S=J=floor(R/25),
    E_(r,s),(z,j) = (d/dZ)^j [Z^r W^s] at Z=z, W=conj(z),
    G_Q = E_Q diag(2,2D) E_Q^T.

The ordinary derivative fixes W. The determinant of G_Q is **not** the field discriminant.

## Strongest surviving result — a full-jet field-chart identity

For squarefree D=4c-1, the maximal order is Z[omega] with

    omega=(1+sqrt(-D))/2, omega^2=omega-c.

The SOURCE suborder point x+y sqrt(-D) has maximal-order coordinates

    T(x,y)=(x-y,2y), det(T)=2.

The maximal-order multiplication is independently implemented as

    (u,v)*(a,b) = (u*a-c*v*b, u*b+v*a+v*b),
    conjugate(u,v)=(u+v,-v).

The maximal trace Gram channel metric is

    B_max=[[2,1],[1,2c]].

The exact identity is

    T^T B_max T = diag(2,2D) = B_source.

More importantly, all ordinary source derivatives commute with T:

    T(derivative_Z^j(Z^r W^s) at source z)
      = derivative_Z^j(Z^r W^s) at maximal-coordinate T(z)

for every r,s,j, using the same frozen-W convention. The resulting **entire** ordered Gram is equal over the integers, provided the maximal-order code evaluates precisely the transported **same Q**.

The new `Phase390FullJetMaximalChart.lean` states this for **arbitrary finite Q, J, R, S** under D=4c-1. The full pinned build and axiom audit are a mandatory promotion gate; do not label it Lean P until successful. This statement neither equates the source suborder with the whole maximal order nor transfers p-adic valuation through a non-unimodular map.

### Bounded computational witnesses

The separately structured source/maximal ring arithmetic and Bareiss determinant oracles checked `R=3,S=2,J=2` on the complete source ellipses:

| D | radius | Source Q points | Full maximal-order points | Same-Q 6x6 Grams | Enlarged-Q Grams |
| --: | --: | --: | --: | :-- | :-- |
| 3 | 4 | 33 | 61 | exactly equal | unequal |
| 7 | 5 | 29 | 61 | exactly equal | unequal |
| 11 | 6 | 35 | 71 | exactly equal | unequal |
| 19 | 7 | 37 | 77 | exactly equal | unequal |
| 43 | 8 | 35 | 63 | exactly equal | unequal |
| 163 | 15 | 61 | 117 | exactly equal | unequal |

All entries, all rows, all ordinary jets and both complete determinants are integer-exact. This is a finite independent CODE PATH, not an external mathematician. Real-path differentiation of W instead of frozen-W gives a different row already at r=s=j=1,z=1+sqrt(-3).

## Explicit arithmetic exponent check on one original positive Gram

For the canonical class-one field D=163, Q=ellipsePairs(163,18), R=S=J=6, the complete source Gram has 36 rows and 87 source points. Integer Bareiss elimination finds the following valuations:

| p | Phase331/323 required exponent | Direct v_p(det G) | Slack |
| --: | --: | --: | --: |
| 2 | 84 | 216 | 132 |
| 3 | 30 | 36 | 6 |
| 5 | 10 | 21 | 11 |

The coded source formulas checked are

    e_2 = R*S + 2*(S*sum_(r<R) floor(r/4) + R*sum_(s<S) floor(s/4)),
    F_p = sum_(r<R,s<S) min(floor(r/p),s),
    e_p = 2*(F_p + R*sum_(s<S) floor(s/p^2))  [for selected odd p].

No separate p=2 exponents are multiplied; no two different source Grams are combined. These are nonvacuous FINITE checks of the actual original determinant; they do **not** prove universal row-factoring, the large production source or analytic bounds.

## Sharp counterexample to a weakened inert-prime premise

In the maximal-order chart, the norm is

    N(u+v*omega)=u^2+uv+c*v^2, c=(D+1)/4.

The proof uses the STRICT gate p<c: no element with nonzero v can have norm p<c, and a rational integer cannot have prime norm p. If class number one, a split/ramified prime ideal of norm p<c would be principal, a contradiction.

At the endpoint p=c, the element omega itself has norm c. In six classical examples D=7,11,19,43,67,163, c=2,3,5,11,17,41 is prime and the polynomial X^2-X+c has the distinct roots 0 and 1 modulo c. Hence **p=c actually splits**. The case D=163,p=41 is a particularly clear strict-bound falsifier. Never rewrite p<c as p<=c. In Phase360 the selected R=floor(D/4) indeed satisfies R<c.

The map T has determinant 2 and loses invertibility modulo 2, although it is invertible modulo all odd primes. This does NOT invalidate the existing binary Gram argument, which is proved directly in original source coordinates. It **does** invalidate a proposed naive transfer of 2-adic row indices by treating T as a unimodular lattice change.

## Exact geometric count and independent scalar sanity

An integer `isqrt` vertical-slice count of the **full** original ellipse, without enumerating billions of points, gives:

| fourth root | D | thin radius | |Q| | interpolation requirement | margin |
| --: | --: | --: | --: | --: | --: |
| 301 | 8,208,541,201 | 11,999,197 | 4,992,989,319 | 4,186,356,009 | +806,633,310 |
| 302 | 8,318,169,616 | 12,119,188 | 5,058,469,573 | 4,242,266,501 | +816,203,072 |

The pointwise margin is exact for the two displayed D, and the 301 count also passes. Hence **source count alone cannot imply the new cutoff**. Phase354's general cardinality theorem remains the load-bearing universal step.

A separately transcribed 75-digit `Decimal.ln` calculation of Phase355's same scalar formulas gives

    L(301^4)-U(301^4) = -0.001013114143820733...
    L(302^4)-U(302^4) = +0.001640248469081680...

This is only an independently computed **floating/Decimal diagnostic**, not an interval proof of the log inequalities or of the universal 302 separation. The exact Lean rational-log certificate remains required.

## Specification -> implementation -> test drift

**Aligned, within checked scope:** the source E rows use original ordinary derivatives, row-major (r,s), all j<J, all Q, exact trace weights and one determinant. The maximal-order recomputation keeps Q fixed and uses a different ring multiplication and norm.

**Rejected representation change:** a complete maximal-order ellipse contains additional half-integral physical points (odd omega coefficient). On all six checked examples, replacing the source Q with it produces a different Gram and determinant. This is not a coordinate lift; it is a different sampling experiment.

**Unverified high-stakes step:** the source-to-field field theorem in Phase359 depends on the complete production-scale p-adic valuation at inert primes, and on the odd/even ring-of-integers correspondence. A passing Lean build validates the formal definitions but cannot substitute for independent mathematical assessment of the intended source-level Frobenius row normalization and all chart assumptions. In particular, our low-dimensional tests do not reproduce the exponents for billions of original rows.

## Controls and resource parity

The two chart implementations use identical (D,rho,R,S,J), exactly the same physical Q, every source row, exact integer trace channels, and the same determinant algorithm. The **changed** Q_max experiment is explicitly a non-matched negative control. No stochastic sampling, smooth surrogate, selected minor or floating determinant is used for the full-Gram comparisons. The scalar-only Decimal experiment is separately marked numerical, not proof.

The independent code was written within the same AI-assisted workflow and shares the stated mathematics; it is an *independent implementation path*, not an independent human witness.

## Evidence ledger

| Claim | Status | Artifact |
| --- | --- | --- |
| Phase360 302^4 theorem as encoded | P relative to frozen Lean theorem | Phase359Field302Candidate.lean, full-root run 44707796788 |
| Universal original-jet Gram chart identity | H until fresh exact-head Lean CI | Phase390FullJetMaximalChart.lean |
| Six exact finite source-chart Gram equalities | M, bounded exact integer | independent_source_oracle.py + CI |
| Non-equivalence of full maximal-order resampling | M, bounded counterexamples | same oracle negative controls |
| D163 finite p=2,3,5 valuation comparisons | M, exact finite | same oracle/tests |
| Point counts at 301^4 and 302^4 | M, exact integer values | vertical integer slicing |
| Decimal scalar sign | M, numeric | scalar_endpoint_oracle.py |
| Universal p-adic source-to-field semantic derivation | H, open | external review issue #50 |
| Masullo, Selberg/Ihara, Siegel-zero consequences | H, NOT supplied | separate research lines |

## Next bounded experiment, with stop rule

Reconstruct from scratch **one production-scale p-adic row divisor** in the original W-fixed jet family for an eligible inert odd prime. Work symbolically with the source Frobenius quotient and original sample pairs; distinguish index-sensitive full integer-row transformations from reductions modulo p. Before promoting any improved field bound, require: exact primal source identity; unimodular transformation; strict p<c field-ideal norm bridge; matching source product exponent; independent small-parameter hostile control; and independent human review of the maximal-order correspondence.

**Kill condition:** any nonintegral quotient, determinant of row transformation other than +/-1, changed sampling Q, wrong W derivative or illicit duplicate p factor retires the proposed bridge. **Stop condition:** if the production valuation correspondence remains unverified, do not compensate by widening the geometry/analogy ontology or claiming another numerical cutoff.

The full audit manifest is `research/phase390/audit_manifest.json`. It records evidence by claim and keeps the original issue #50 open.
