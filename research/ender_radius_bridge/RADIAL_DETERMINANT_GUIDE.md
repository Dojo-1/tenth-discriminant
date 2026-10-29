# One integer, a smaller geometric ceiling

**Status: the full Phase119 determinant upper bound is Lean-checked standalone.**
The checked class-number-one cutoff remains50 billion. This page explains
the checked connection from the derivative estimate to the actual
determinant, not a new classification claim.

The freedom is to change our observations while keeping their arithmetic
content. An integer row transformation of determinant1 preserves the same
integer determinant and every prime divisor. We use it to center the radial
quantity ZW. After W is set to conjugate Z, this is squared distance.
[Why the derivative estimate works](RADIAL_JET_GUIDE.md).

The next connection has five concrete parts:

1. **Read the actual diagonal.** Each transformed diagonal entry is exactly
   twice a sum of squared ordinary derivatives, at the original lattice
   points and derivative orders. This equality retains the factor2.
2. **Apply the uniform estimates.** The eligible row (r,s), with r>=9S,
   gains a factor(13/20)^s in every derivative column. Every remaining row
   keeps its previous uniform bound. Values at the origin are included.
3. **Bound the determinant.** Hadamard's inequality bounds the determinant
   by the product of diagonal entries. The determinant is still the same
   original integer; the diagonal entries themselves may change.
4. **Add the logarithmic savings.** Squaring gives exponent2s. Summing over
   s=0,...,S-1 gives S(S-1); there are R-9S eligible rows. The exact saving is

       (R-9S) S(S-1) log(20/13).

5. **Keep the production geometry.** The point-count estimate, radius,
   floor choices and derivative correction are unchanged. Under the exact
   aspect guards, the saving is at least0.010 times the scale R^2*S.

The theorem concerns the actual integer Gram G, and gives

    log(det G)/(R^2*S) <= 0.8 log D - 0.823

at the chosen radius for every D>=41,006,250,000. The old right-hand
constant was0.813. This is an upper estimate for the same arithmetic
quantity, without a class-number hypothesis.

Positivity matters before taking logarithms. The original point-count and
derivative-depth guards establish positive definiteness. With an empty
sample set and nonempty rectangle, the determinant is0: that case cannot
be inserted into the positive-log argument. Empty row rectangles instead
have determinant1. Both are explicit controls.

A further control keeps the geometric interpretation honest. At the origin,
ZW is0 while ZW-12 is-12. Its squared size is144, so the proof cannot rely
on every observation decreasing pointwise. It uses the uniform ceiling on
the whole disc and the preserved determinant.

The remaining cutoff step is to put the arithmetic lower bound on this
same integer, certify the fixed endpoint, and compose the actual-field
theorem. Integration and pinned CI must follow before publishing a smaller
checked cutoff. [Exact verification](PHASE119_VERIFICATION.md) · [Registered scope](PHASE119_PROTOCOL.md).
