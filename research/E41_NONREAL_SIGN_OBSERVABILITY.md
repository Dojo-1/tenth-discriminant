# E41 — THE NONREAL SOURCE HAS AN EXTRA CHANNEL

**19 November 2026. Research draft stacked on E39.**

## Claim and typed source

Actual two distinct integer-pair samples a=(x,y), b=(u,v), in
the SAME original Finset Q, source algebra D, ordinary Z-jet
J=1 and 1,Z row basis R=2,S=1, original factor-two positive trace.

The exact original Gram (NOT a selected minor or substitute
complex observation) is

    G = [[4, 2(x+u)],
         [2(x+u), 2(x²+u²+D(y²+v²))]].

Thus

    det G = 4 [(x-u)² + D(y-v)² + D(y+v)²]
          = 4 [(x-u)² + 2D(y²+v²)].

A naive Euclidean-style 4 [(x-u)² + D(y-v)²] fails when y+v≠0.
The extra 4D(y+v)² is **a source-observation remainder**, not a
claimed intrinsic geometric curvature or arithmetic conductor factor.

## A noninjective observer

Q1={(0,1),(1,1)} and Q2={(0,1),(1,-1)} are different original
integer-pair sample supports at D=3. Their ENTIRE J=1,R=2,S=1
trace Gram is identical, [[4,2],[2,14]], determinant 52.

The original positive Gram uses each sample's imaginary coefficient
only through its square in this observation regime. A per-point
imaginary sign may be unobservable even though it is a real
difference in the original source support.

This supports an observability claim, NOT a ring-isomorphism claim.
The operator's measurement rank and row set are load-bearing.

## Moving frame

Real-coordinate translation x->x+c and u->u+c remains compatible
with integer unimodular row frame [[1,0],[-c,1]].
Imaginary-coordinate translation has NOT been declared an equivalent
integer row frame: such a claim would require additional closure
of the polynomial source basis under quadratic imaginary constants.

## Controls and release

- The same-imaginary pair (0,1),(1,1) at D=3 has det 52 versus
  naive squared-distance 4.
- The two different supports above have identical full Gram.
- E39 real-source restriction y=v=0 recovers 4(x-u)².
- The E40 independent exact integer oracle checked 1,800 finite
  nonreal pairs; 1,440 falsified naive distance-only lift.
- E31's conductor kernel -> Gram divisibility shortcut remains retired.
- E36's nonunimodular frame counterworld remains active.
- The complete thin ellipse in Phase350 is NOT replaced by this
  toy two-point source; no new 307⁴ or faster classification claim.

Source: lean/TenthDiscriminant/E41ComplexSourceSignObserver.lean
Focused workflow: .github/workflows/e41-complex-source-sign-observer.yml
Root: lean/TenthDiscriminant.lean

Status H until exact-head focused/root Lean and permitted-axiom
audit. The algebraic identity may be checked independently but this
does not certify the Lean encoding until the CI gate passes.

## Next question

For the complete original sample Q and ordinary rows 1,Z at J=1,
the full Gram depends on three integer moments:
    N = |Q|,
    Sx = sum real coefficients,
    T = sum(real² + D imag²).

Then
    det G = 4 [N*T - Sx²].

Investigate source-specific moment and sign-observer equivalence
classes, their integral transport behavior, and their relation to
original row rank; do not treat them as all of the original source.
