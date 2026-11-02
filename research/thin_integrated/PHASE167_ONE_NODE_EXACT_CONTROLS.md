# Phase167 — A one-node exact sanity check

We should not ask anyone to trust a wall of Lean declarations before
showing what the integer Gram **actually is** in one simple case.

Take **D=7**, **J=R=S=1**. There is just one monomial, the constant
`Z^0W^0=1`, and the only jet is its **ordinary** order-zero derivative.
At the integer-pair observation `(0,0)`, the integer coordinate result
is `(1,0)`. The original trace weight is not optional:

```text
integerPairTrace(7, (1,0), (1,0))
  = 2 * (1*1 + 7*0*0)
  = 2.
```

Thus the original `1×1` Gram is `[2]`, determinant **2**, and no
alternative derivative convention or sample normalization is involved.

**Matched controls:** at the translated observation `(1,0)` the same
constant row again gives determinant **2**. With **both** distinct
observations the trace sum is **4** (support changes the determinant).
With the **empty** support the determinant is **0**, demonstrating why
a general logarithm theorem *must* require positivity separately.

The source exponent at `R=S=1` equals **1**; the odd prime set below
`R=1` is empty, so its product equals 1, not zero. The exact elementary
identity becomes `log(2)=log(2)` on a small, concrete, actual Gram.
The calculation needs neither `D≥450⁴` nor a class-number-one witness.

[Lean file](../../lean/TenthDiscriminant/OneNodeTraceControls.lean)
contains separate direct-computation theorems for the origin, translation,
two-node sum, empty-node control, exponent, empty odd-prime set and log
equality. All claims are **CI pending** until pinned Lean and whole-root
source/axiom/negative-control checks pass. Tests share the source
implementation and are not an independent human peer review.

This is a check on the meaning of the formalized object, not a
discriminant-cutoff improvement. It complements the nonvacuous
arbitrary-Q source theorem in [Phase166 PR #85](https://github.com/Dojo-1/tenth-discriminant/pull/85).
