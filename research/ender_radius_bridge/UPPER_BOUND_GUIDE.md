# Why Ender's upper formula bounds the actual Gram

The new checked step is an estimate on one unchanged matrix. At the
positive integer radius `rho` used by the Ender campaign, with `rho<R`,
Lean proves

$$2\sum_{\substack{p<R\\p\text{ odd prime}}}F(p)\log p
\;\le\;\log\prod_iG_{ii}\;\le\;U_B(R,S,S,n,\rho),$$

provided the quadratic field has class number one, `D` is squarefree
with `D≡3 (mod 4)`, `R<(D+1)/4`, the checked chosen-radius guard holds,
and **`n` is at least the actual ellipse point count**. Phase 21 now proves
the needed geometric count and supplies it from an interval's lower endpoint.
The scalar factorial lower estimate is now checked separately; the full
prime-mass lower estimate and numerical contradictions remain open.
This theorem supplies no new discriminant cutoff.

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

## Why the geometric count is valid

Give every lattice point `(x,y)` with both coordinates nonzero an open
rectangle directed inward toward the two axes. In the first quadrant it
is `(x-1,x) × (sqrt(D)*(y-1),sqrt(D)*y)`; the other quadrants use the
corresponding inward rectangle. Every coordinate has smaller absolute
value than its lattice center, so the rectangle stays in the same disk.
Different points have disjoint rectangles, each of area `sqrt(D)`.
Thus the number `K` of points off the axes satisfies

$$K\sqrt D\le\pi\rho^2.$$

The remaining points lie on the axes. The nonzero horizontal axis has
`2rho` possible points. The vertical axis has
`2 floor(rho/sqrt(D))+1`, including the origin. Consequently

$$|E(D,\rho)|\le\frac{\pi\rho^2}{\sqrt D}
+2\rho+2\left\lfloor\frac\rho{\sqrt D}\right\rfloor+1.$$

At fixed radius the ellipse loses points as `D` increases, so an upper
count at the lower interval endpoint works throughout the interval. The
program floors an Arb **upper endpoint** when selecting its vertical
line count. Lean allows any upward padding `Y` of the exact floor; a
strict bound `rho/sqrt(D)<Y+1` suffices. Interpreting the recorded Arb
enclosures as those exact inequalities is still a numerical proof task.

## Where to inspect the proof

[EnderUpperB.lean](../../lean/TenthDiscriminant/EnderUpperB.lean) names the
steps: `traceGram_diagonal_le_uniform`, `rectangular_log_row_sum`,
`log_derivative_correction_le_upperB`, and
`ellipse_primeMass_log_le_upperB`. All variables must be explicitly bound;
automatic implicit variables are disabled in this module.

The upper-formula controls include radius one, the constant row's factor two,
derivatives above the degree, zero observations, and empty samples.
Concrete one-row counterexamples reject an understated radius or count.
[EllipseUpperCount.lean](../../lean/TenthDiscriminant/EllipseUpperCount.lean)
checks the geometric count and endpoint transfer, with radius-zero,
negative-coordinate, integer-boundary and axis-overcount controls. Its
public composition is `ellipse_primeMass_log_le_counted_upperB`.
The [Phase 20](PHASE20_PROTOCOL.md) and [Phase 21](PHASE21_PROTOCOL.md)
records preserve targets, repairs, verification and scope. The
[factorial bridge](FACTORIAL_LOWER_GUIDE.md) now checks the exact Legendre
identity and scalar lower expression. Its prime-power weights are not
the determinant's odd-prime weights. The [staircase proof](PRIME_MASS_LOWER_GUIDE.md)
now checks their finite conversion, small-prime subtraction, geometric
loss bounds and clipping, conditional on one reciprocal-prime tail estimate.
That analytic estimate remains open; the numerical task must still interpret
the saved enclosures and strict contradictions.
