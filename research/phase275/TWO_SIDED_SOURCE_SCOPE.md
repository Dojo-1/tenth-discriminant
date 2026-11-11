# Phase275 — two-sided original-source motion, and a no-gain control

**Predeclared object:** the exact `integerDerivativeRow D r s j z` from `lean/TenthDiscriminant/IntegerTraceGram.lean`, with the conjugate variable W held fixed *during* ordinary Z differentiation. When the **observation point** is shifted by the real integer 3, both Z and W must change by 3. This is a finite, source-typed verification of a known Taylor transport identity, not a novel discriminant bound.

## First-order tube identity

For any integral bivariate polynomial F(Z,W), any j, and any real-axis integer shift u divisible by 3:

```text
partial_Z^j F(Z+u,W+u) =
 partial_Z^j F(Z,W) +
 u*(partial_Z^(j+1) F + partial_W partial_Z^j F)(Z,W) (mod 9).
```

At the largest retained jet j=2, the missing third Z derivative is divisible by 3! and so its coefficient u * partial_Z^3 F vanishes modulo 9. Thus first three **ordinary** Z derivatives are sufficient for this near-identity transport on the original row polynomial source, provided the W-lowering term is also retained. This is the p=3/J=3 case of the already established paper-level precision horizon in Phase274, now checked on a genuinely bivariate source.

For original row `F = Z^r W^s`, the actual row index-lowering identity is

```text
E'(r,s,j) = E(r,s,j) + 3*E(r,s,j+1) + 3*s*E(r,s-1,j) (mod 9),
```

where the unavailable j=3 term is set to zero at depth J=3. Its two integral coordinate channels are checked, not merely the real projection.

## Preregistered controls

- **Inert example:** D=7, p=3, since (-7 | 3)=-1.
- **Split negative control:** D=11, p=3, since (-11 | 3)=+1. The identical tube law must still hold; therefore this law itself is not an inert-prime divisibility result.
- **Observation:** z=(1,1) shifted to (4,1), keeping both original integer-pair channels.
- **Source rows:** 0<=r<4, 0<=s<3, 0<=j<3; all 72 cases (36 for each D) are enumerated by Lean `fin_cases; decide` with the original source `integerDerivativeRow`.
- **Independent-order Python check:** `research/phase275/two_sided_original_source.py` imports the original Phase204 ordinary-jet evaluator, constructs the two-sided action separately, and checks 3 centers x 3 allowed shifts in each local case, with group/inverse controls.
- **Hostile depth J=2:** the source-row combination `(Z-1)^2 W = Z^2 W - 2 ZW + W` has zero first two jets at z=(1,0). Its first derivative at z=(4,0) is 24=6 mod9, so NO function of the two retained source jets can perform the translation for both this polynomial and zero.

## Nonclaims / boundaries

The full source evaluated on the production `ellipsePairs` is **not** invariant under translating its support. The identities above compare polynomial jet values at two points. They do **not** identify the Gram built on Q with the Gram built on Q+3, or assert an analytic upper bound for either changed support.

The split-prime test is intentionally matched: a transport identity that works independently of inertness cannot be credited as new inert-prime mass. This is a semantic negative control against double counting the existing original combined Frobenius divisibility and ordinary-jet factorial layers.

**Status:** paper polynomial identity is classical; finite source-specific Lean controls and Python reproductions are initially H/M until exact-head CI completes. No universal p-adic theorem, new zero-free region, scalar bound or nonflat holonomy follows.

**Stop rule:** if either signed channel fails, the s-lowering term is absent, or the J=2 counterexample is not distinguished, stop the branch and correct the source semantics. **Promotion:** only the narrow finite source controls may become P after exact-head Lean plus axiom audit and CI; any uniform production determinant advantage requires an additional independently reviewed theorem on the original G=EBE^T.
