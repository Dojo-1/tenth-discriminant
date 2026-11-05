# Phase228 — one combined source matrix, no assumed commutation

**Verification status at submission: CI PENDING.** Draft PR #157 only.

The old polynomial source is the integer monomial rectangle with row-major labels
\`i = r*S+s\`. At an odd inert prime \`p\`, define
\`k=min(floor(r/p),S-1-s)\` and \`ell=floor(s/p^2)\`.
The proposed row is

\[
P_{r,s}=Z^{r-pk}W^{s-p^2\ell}(Z^p-W)^k(W^{p^2}-W)^\ell.
\]

For \`0<=t<=k\`, \`0<=u<=ell\` its binomial expansion uses only
\`(r-pt,\;s+t-(p^2-1)u)\` with integer coefficient
\`(-1)^(t+u)*binom(k,t)*binom(ell,u)\`.

The combined matrix \`Phase228.combinedBasisMatrix R S p\` is defined
using *both indices in one sum*. This is NOT the product of separately
truncated row matrices. If a term is not the leading \`(0,0)\`, its row-major
label is strictly lower; the leading coefficient is exactly one. The
target theorem is therefore \`det U=1\`.

## Boundary and kill conditions

- Formal theorem must compile in the pinned Lean 4.19 root and scoped CI.
- Every theorem's axiom report must be limited to propext/Classical.choice/Quot.sound.
- The row \`(3,9)\` in \`R=4,S=11,p=3\` must have old monomial
  columns 42,34,10,2 with coefficients +1,-1,-1,+1.
- The p=1 degeneration must not be silently accepted; all structural
  statements demand \`2<=p\`.
- Any failure of finite target bounds, triangularity, or determinant-one
  retires the additive SOURCE MATRIX hypothesis pending repair.

## Still unproved

1. Exact polynomial identity between \`U\` acting on original monomials
   and \`P_{r,s}\` for all indices.
2. Equality after every original ordinary Z-derivative at original
   integer-pair conjugate observations.
3. Same-gram factorization \`UGUᵀ=diag(p^(k+ell)) K diag(p^(k+ell))\`.
4. Exact sum-of-exponents identity and consequent integer divisor
   \`p^(2(F+B)) | det(original G)\`.
5. \`ThinUpper321\`, actual-field bridge, external human review.

No threshold promotion. The accepted 322^4 endpoint remains unchanged.
The finite locally generated coefficient checks are correlated
with the candidate and are NOT an independent witness.
