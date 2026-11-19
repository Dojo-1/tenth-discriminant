# E42 — THREE SOURCE MOMENTS, ONE OBSERVED GRAM

19 November 2026 · original-source information-classification draft.

## Exact source, not invented geometry

Retain the original integerRectangularTraceGram Q D 1 2 1:
- Q is the literal finite set of integer-pair observations (no duplicates).
- D is the original quadratic parameter.
- J=1 uses ordinary Z-jet order zero, W held fixed.
- R=2,S=1 gives exactly the two polynomial rows 1 and Z.
- The positive integral trace has weights 2 and 2D.

For arbitrary finite Q, define:
    N(Q) = cardinality Q
    X(Q) = sum_q q.real
    T_D(Q) = sum_q [q.real² + D*q.imag²].

The ENTIRE original 2x2 Gram is predicted to equal
    G(Q,D) = 2 [[N,X],[X,T_D]]
and hence
    det G(Q,D) = 4(N T_D - X²).

The exact source trace/jet definitions themselves are used in Lean.
This is a complete observation signature in the chosen 2-row
regime, not a statement about all R,S,J.

## Classification theorem target

For two finite supports Q,P under the SAME D,J=1,R=2,S=1:

    G(Q,D)=G(P,D)
      iff
    N(Q)=N(P), X(Q)=X(P), T_D(Q)=T_D(P).

Both directions require an exact Lean proof. A single equal
determinant would be insufficient; E42 compares the entire matrix.

The E41 partial imaginary-sign flip of a single sample produces
different supports with identical moment triple, hence identical
entire observed Gram. This is observation non-injectivity,
not source equality, ring isomorphism or new valuation.

The repository ALREADY proves global sample conjugation symmetry
for arbitrary original J,R,S in ObservationConjugation.lean.
E42 is not a rediscovery of that theorem; the three-moment
description gives the FULL equivalence relation on original
finite supports only for the chosen low-row observation regime.

## Rank control: complex versus real source

For Q={(0,1)}, the actual positive trace Gram determinant is 4D.
For Q={(0,0)}, it is 0. One nonreal sample contributes two
real-coordinate channels to the trace Gram, while a single real
sample does not. This is a rank/observability statement, not a
claim of computational performance.

## Negative controls

- Q is a Finset. Duplicate pair labels collapse: no fake extra
  independent observation is allowed.
- Other derivative orders and monomial bases do not inherit
  this three-moment completeness without separate proof.
- Per-point sign collisions are not in general global
  conjugation symmetries.
- Nonunimodular row scaling changes the determinant and is not
  an admissible equivalence.
- The large complex thin-ellipse source used in 307^4 has
  many more rows/jet channels, so this observer's fibers do
  not automatically generate a field discriminant improvement.

## Evidence and release

Lean source: lean/TenthDiscriminant/E42OriginalGramMomentSignature.lean
Focused workflow: .github/workflows/e42-original-gram-moment-signature.yml
Stack: E41 #253 over E39 #252.
Status H until exact-head focused/full-root CI and permitted-axiom
review prove the true encoded identities, not only a surrogate.

Research question: which extra ordinary-jet rows split the
three-moment observation fibers, under integral unimodular
frame transport, at fixed original Q and equal computational
resources? These are falsifiable rank tests, not a hardness claim.
