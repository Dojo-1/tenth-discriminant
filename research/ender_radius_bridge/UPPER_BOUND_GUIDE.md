# Why Ender's upper formula bounds the actual Gram

The new checked step is an estimate on one unchanged matrix. At the
positive integer radius `rho` used by the Ender campaign, with `rho<R`,
Lean proves

$$2\sum_{\substack{p<R\\p\text{ odd prime}}}F(p)\log p
\;\le\;\log\prod_iG_{ii}\;\le\;U_B(R,S,S,n,\rho),$$

provided the quadratic field has class number one, `D` is squarefree
with `D≡3 (mod 4)`, `R<(D+1)/4`, the checked chosen-radius guard holds,
and **`n` is at least the actual ellipse point count**. The last premise
is visible: Ender's particular upper point-count estimate remains to be
proved in Lean. The factorial lower estimate and numerical contradictions
also remain open. This theorem supplies no new discriminant cutoff.

## A row has one radius cost and one derivative cost

For row `(r,s)` and derivative order `j≤r`, the observation is
`(r)_j z^(r-j) conjugate(z)^s`. Its squared magnitude is exactly

$$(r)_j^2|z|^{2(r+s-j)}.$$

Every sample satisfies `|z|≤rho`. Also `(r)_j≤r^j`. Put
`m_r=max(1,r/rho)`. Then `r≤rho*m_r`, so each derivative observation
costs at most `rho^(2(r+s))*m_r^(2(J-1))` when `j<J`.
There are at most `nJ` observations, and the trace normalization is two:

$$G_{(r,s),(r,s)}\le
2nJ\,\rho^{2(r+s)}m_r^{2(J-1)}.$$

If `j>r`, the observation is zero. The origin is retained and ordinary
derivatives are used throughout. The checked chosen-radius interpolation
theorem supplies positive diagonals, so taking their logarithms is legal.

## Sum the rows, then estimate the derivative correction

Taking logarithms and summing over the original `R` by `S` rectangle gives

$$RS\log(2nJ)
+2\log\rho\left[\frac{SR(R-1)}2+\frac{RS(S-1)}2\right]
+2S(J-1)\sum_{r<R}\max(0,\log(r/\rho)).$$

The first two terms are exact sums. For an **integer** radius, the last
sum begins at `r=rho`; every earlier term is zero. The logarithm increases,
so its left-endpoint rectangles lie below the integral:

$$\sum_{r<R}\max(0,\log(r/\rho))
\le\int_\rho^R\log(t/\rho)\,dt
=R\log(R/\rho)-R+\rho.$$

Production `upper_B` adds one further nonnegative `log(R/rho)` to this
correction. Thus the checked estimate implies its unchanged expression.
Lean also checks that Python's two integer `//2` operations equal the
displayed triangular-number coefficients exactly. The spare endpoint
term is checked slack, with no optimization experiment or novelty claim.

## Where to inspect the proof

[EnderUpperB.lean](../../lean/TenthDiscriminant/EnderUpperB.lean) names the
steps: `traceGram_diagonal_le_uniform`, `rectangular_log_row_sum`,
`log_derivative_correction_le_upperB`, and
`ellipse_primeMass_log_le_upperB`. All variables must be explicitly bound;
automatic implicit variables are disabled in this module.

The controls include radius one, the constant row's factor two,
derivatives above the degree, zero observations, and empty samples.
Concrete one-row counterexamples reject an understated radius or count.
The [Phase 20 record](PHASE20_PROTOCOL.md) preserves the target, proof
repairs, verification and scope. The next geometric task is to prove that
Ender's specific `n_up` really bounds the full ellipse count; the next
arithmetic task is to put his factorial expression below the exact prime
sum on the left.
