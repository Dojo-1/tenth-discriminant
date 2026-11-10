# Phase272: Leibniz–Newton jet transport without false holonomy

**Status:** candidate Lean checks on a draft branch; no compile claim until exact-head CI and root audit. This is a source-preserving negative-control formalization, not a new tenth-discriminant bound or a claim of new general mathematics.

## Scope and known prior work

The repository already proves the source identity `integerDerivativeRow_eq_factorial_hasse` in `JetPrecisionBridge.lean`, the deeper jet factorial filtration in `JetFactorialFiltration.lean`, the characteristic-p precision boundary in Phase155, and original-source moving-frame translations in Phase146. Phase272 adds one **no-descent** statement: no function on ordinary-jet vectors reduced modulo 3 can translate the source data of *both* the zero polynomial and `Z^3` from basepoint zero to one.

The source is the same integer-pair ordinary derivative `integerDerivativeRow 19 3 0 j (a,0)`, with `W` held fixed and original source parameters. The Hasse jet is a DIAGNOSTIC control, never a substituted production Gram.

## The exact mathematical result (classical paper proof)

For a prime p and m>=0, let `P_m(F_p)` denote polynomials of degree <=m. Define

- `H_a(f) = ([t^j] f(a+t))_{j=0}^m`, the Taylor/Hasse coefficient vector;
- `J_a(f) = (f^(j)(a))_{j=0}^m`, the ordinary derivative vector.

Then `J_a=F_m H_a` with `F_m=diag(0!,1!,...,m!)`. Taylor-translation matrices in the Hasse frame are upper unitriangular:
`H_{a+u,j} = sum_{k>=j} binom(k,j) u^(k-j) H_{a,k}`. In characteristic p, `F_m` is invertible iff m<p. Thus ordinary-jet translation is well-defined on all vectors when m<p.

When m>=p, choose `f(X)=(X-a)^p`, `g=0`, `u=1`. Then `J_a(f)=J_a(g)=0`, including orders >=p, but `f(a+1)=1`, `g(a+1)=0`. Therefore **no function whatsoever on the reduced ordinary jets** can implement this translation for all source polynomials. This is not curvature or holonomy of a connection; it is failure of the data reduction to descend through translation.

The **integral** obstruction is the classical abelian group
`coker(F_m) = ⊕_{j=0}^m Z/(j!)`. At p:
`length_p(coker F_m) = sum_{j=0}^m sum_{h>=1} floor(j/p^h)`,
with graded multiplicities `r_h = #{j<=m : v_p(j!)>=h}`.
At p=3,m=8 the factorial valuations are
`[0,0,0,1,1,1,2,2,2]`, hence `r_1=6,r_2=3`, and total length 9.

These are standard facts about Hasse–Schmidt/Taylor differentiation and p-adic factorial divisibility. Novelty in the general claims is **not** asserted.

## Precision and the calculus analogy

SDG first-order infinitesimals satisfying `epsilon²=0` alone cannot encode a cubic's third Taylor coefficient. For higher jets one needs an appropriate higher-order nilpotent thickening, such as the formal algebra `Z[epsilon]/(epsilon^4)` for order 3. This elementary truncated polynomial algebra is not by itself a full SDG topos or a physical theory.

Newton's moving-frame intuition is represented by basepoint translations. Leibniz's integral coefficient data is represented by `H_a`. Where `J_a` loses information mod p, the translation square cannot be formed on the ordinary residue-jet quotient; the candidate 'diamond holonomy' is better classified as a *descent obstruction*.

## Relevance and stop rule

The tenth-discriminant production object is the **original ordinary Z-jet Gram**, not the coefficient-jet Gram. A change of columns to Hasse jets requires transporting the factorial column weights and original metric; otherwise it changes the arithmetic problem. Existing determinant lower bounds may ALREADY count these factorial valuations. No new p-adic determinant exponent, analytic upper bound, field cutoff, exceptional-zero result, or novelty claim follows from Phase272 alone.

**Kill condition:** If the zero/cubic counterexample fails, or the theorem accidentally proves only a weakened surrogate, reject the transport claim. If the source-specific Lean theorem compiles but says nothing new beyond existing factorial identities, retain only as a negative regression, not a claimed advance in the tenth-discriminant bound.

**Next discriminating research test:** for the SAME full original Gram and matched observation set, isolate valuation layers *after* the exact factorial normalization and already counted Frobenius row factors. Any proposed additional prime-mass gain must survive this accounting and a matched split-prime negative control.
