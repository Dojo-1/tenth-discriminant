# Phase 196 — Toward fourth root 327 without inventing another prime

*3 November 2026 · candidate [H] until exact-head Lean and whole-root controls pass.*

The previous milestone was not a scalar preflight: [PR #116](https://github.com/Dojo-1/tenth-discriminant/pull/116) merged the formally checked **328⁴ actual-field** statement. Its independent semantic reconstruction remains [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).

Here we test whether a small improvement in the *existing real-analytic inequality* combines with the separately checked Phase192 arithmetic to reach the next fourth-root cutoff. We do not change the trace pairing, point support, derivative convention, number field or the inventory of inert primes.

## Fix one integer, then squeeze it from both sides

Keep exactly the original pair-observation set \(Q_D=\mathrm{ellipsePairs}(D,\mathrm{thinRadius}(D))\), original ordinary derivatives of the rectangular monomials with \(W\) held fixed, and the original trace weights \(2,2D\). Call the resulting integer evaluation matrix \(E_D\), and its positive trace Gram

~~~math
G_D=E_D B_D E_D^{\mathsf T},\qquad
\Delta_D=\det G_D>0.
~~~

The divisor and the upper bound must constrain **this same \(\Delta_D\)**. The larger padded ellipse provides only a bound on the number of nodes; its Gram determinant is not a substitute.

The original dimensions remain \(R=\lfloor D/4\rfloor\) and \(S=\lfloor R/25\rfloor\). At the target floor, the interpolation-count proof must be rechecked with root **327**, not imported from the old 328 case.

## Two small improvements, but neither is a field theorem alone

**Sharper analytic constant.** The previous proof threw away useful precision by using only \(\log(521/1000)\le-0.650\). In fact the same radius admits

~~~math
\log(521/1000)
=\log(521/500)-\log 2
\le 21/500-6931/10000
=-6511/10000
\le-651/1000.
~~~

The same original upper-\(B\) normalized identity then has the following proposed bound, subject to 327-specific guard proofs:

~~~math
\frac{B(R,S,\rho,n)}{R^2S}
\le\frac45\log D-\frac{814}{1000}.
~~~

The generic \(-23/2000\) radial saving and \(-1/10\) contraction saving would turn it into the same-thin-Gram upper

~~~math
\frac{\log\Delta_D}{R^2S}
\le\frac45\log D-\frac{1851}{2000}.
~~~

**Stronger original-prime lower.** The already focused-Lean-checked [Phase192 certificate](../../lean/TenthDiscriminant/RecoveryGainFloorRatio.lean) uses only the existing odd primes 3 and 5 and the exact floor identity \(25S\le R\le25S+24\), recovering \(0.0895\) of normalized arithmetic mass. If its hypotheses are established at the 327 floor and the same original Gram has positive determinant, the proposed odd-plus-once-binary lower reads

~~~math
\frac{999997}{1000000}\log D-\frac{57305}{10000}
+\frac14\log2
\le\frac{\log\Delta_D}{R^2S}.
~~~

No new or second binary factor is allowed.

## Independent rational collision test

The N=5 finite logarithm checker targets

~~~math
\frac{57899}{10000}\le\log327\le\frac{579}{100},
\qquad D\ge327^4\implies\log D\ge\frac{231596}{10000}.
~~~

Using the already certified \(\log2\ge6931/10000\), the prospective scalar gap is exactly

~~~math
\left(\frac{999997}{1000000}-\frac45\right)\frac{231596}{10000}
-\frac{57305}{10000}+\frac{1851}{2000}
+\frac{6931}{40000}
=\frac{313803}{2500000000}>0.
~~~

This is approximately \(0.0001255212\). The artificial test at \(\log D=23.15\) **must not** falsely yield the strict separation.

## Formal checkpoints and kill conditions

The research branch contains separate source files for the logarithm, 327 ellipse geometry, trace-Gram positivity, normalized odd/binary lower, matched analytic upper, scalar overlap, and actual-field return. Focused GitHub Actions workflows compile them separately. Their presence in a branch is not a completed proof. Do not import them into the production root, merge or publicize 327 as a theorem until their exact-head builds, source identity, axiom inspection, negative controls, and full-root CI pass.

Reject the proposed descent if the 327 interpolation guard fails, the sharpened \(-0.814\) analytic bound does not follow from the unchanged identity, the Phase192 gain cannot be specialized at \(D\ge327^4\), the once-counted binary factor is doubled, an observation support or the trace metric changes, or an unproved older-domain hypothesis sneaks into the chain. Independent mathematician reconstruction in Issue #50 remains open *even if every CI passes*.

The working strategy is to **transport verified structure across a nearby fourth-root boundary, without pretending the old guard has transported with it**. In this instance, the arithmetic and analytic channels are separate; their junction is one positive integer determinant, and the return to the field remains the final, most scrutinized edge.
