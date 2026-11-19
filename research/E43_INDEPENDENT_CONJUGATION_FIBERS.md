# E43 — INDEPENDENT CONJUGATION AS AN OBSERVER FIBER

19 November 2026 · all-original-jet symmetry and falsification target.

## The key improvement over E41

The repository ALREADY proved in ObservationConjugation.lean that
the entire original integerRectangularTraceGram is invariant when
ALL original samples are conjugated. Do not claim novelty for that.

E43 proposes a *strictly stronger* original-source statement:
for any original finite Q, original Nat D,J,R,S and ANY function f
such that

    (a) f is INJECTIVE ON THE ORIGINAL FINITE SUPPORT Q,
    (b) for each q in Q, f(q)=q OR f(q)=pairConj(q),

the entire original full rectangular trace Gram satisfies

    G(Q.image f, D,J,R,S) = G(Q,D,J,R,S).

This follows pointwise from the already-proved
integerDerivativeRow_conj and integerPairTrace_conj, then
Finset.sum_image under the required injection. No change to
the original ordinary Z-jet convention, sample multiplicity,
or positive trace is made.

This is not a gauge-equivalence theorem for arbitrary
connections or a lossless information transport: the original
source support is different even when the observation agrees.

## Concrete non-global obstruction

Qplus={(0,1),(1,1)}
Qmixed={(0,1),(1,-1)}.

Qmixed is neither Qplus nor the GLOBAL conjugate of Qplus.
But the partial map that conjugates only points with REAL
coefficient 1 carries Qplus bijectively to Qmixed.
Hence E43 predicts their complete original integer Gram
is identical for EVERY D,J,R,S.

The E41 two-row low-jet witness is therefore just one fiber
of a much more general source-to-observer symmetry.

This corrects a tempting extrapolation in E42:
increasing ordinary-jet rows alone CANNOT resolve this
particular independent-conjugation ambiguity while the
observation remains a sum of pointwise positive trace pairings.
To resolve it one must alter the observation class (for
example add oriented cross-sample measurements); that is
not a free formal inference or admissible same-Gram bound.

## Collision falsifier

Qcollision={(0,1),(0,-1)}.

Conjugate ONLY the first element, leaving the second fixed.
Both map to (0,-1). The output Finset has one point, so
sample cardinality is lost and the original full Gram changes.

Any claimed invariance that omits injectivity-on-Q is false.
This is a source-level, exactly measured negative control.

## Verification and no-overclaim boundaries

- Lean E43 proof candidate: original full Gram identity,
  partial flip involution/injectivity, concrete source pair,
  and noninjective-collision negative control.
- Focused workflow and full root allowed-axiom audit must pass
  at the exact committing head before P.
- Existing ObservationConjugation remains P from previous
  root-certified source; this branch is not a rediscovery.
- E31 conductor kernel does NOT create additional original-Gram
  prime factors automatically.
- HK Gaussian split-prime CRT observations are an algebraic
  *different measurement regime*; do not identify their
  recovering properties with this fixed trace-Gram.
- The Phase350 307^4 actual-field theorem has separate large-Q,
  source-to-field and independent mathematical review gates.
- No new p-adic, ETH/P-vs-NP, holonomy, asymptotic performance,
  or smaller field-discriminant bound follows from E43.

The correct categorical phrasing is: the fixed Gram observation
factors through a quotient of finite original supports by
injective independent-conjugation maps. Full orbit/equivalence
structure is a separate theorem target, not yet formalized.

## Next adversarial test

If the observation is changed to include oriented cross-sample
pairings, pre-register exactly which operator and coefficients
are being added; compare against the original fixed Gram and
a matched classical alternative. Any apparent new divisibility
that only exists in the changed observation is NOT a new factor
of the original Ender source determinant.
